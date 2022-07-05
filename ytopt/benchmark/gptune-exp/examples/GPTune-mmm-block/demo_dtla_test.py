#! /usr/bin/env python

# GPTune Copyright (c) 2019, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S.Dept. of Energy) and the University of
# California, Berkeley.  All rights reserved.
#
# If you have questions about your rights to use or distribute this software,
# please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.
#
# NOTICE. This Software was developed under funding from the U.S. Department
# of Energy and the U.S. Government consequently retains certain rights.
# As such, the U.S. Government has been granted for itself and others acting
# on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in
# the Software to reproduce, distribute copies to the public, prepare
# derivative works, and perform publicly and display publicly, and to permit
# other to do so.
#


"""
Example of invocation of this script:

cd ./GPTune
. ./run_env.sh

$MPIRUN -n 1 python ./demo.py -nrun 20 -ntask 5 -perfmodel 0 -optimization GPTune

mpirun -n 1 python ./demo.py -nrun 20 -ntask 5 -perfmodel 0 -optimization GPTune

where:
    -ntask is the number of different matrix sizes that will be tuned
    -nrun is the number of calls per task
    -perfmodel is whether a coarse performance model is used
    -optimization is the optimization algorithm: GPTune,opentuner,hpbandster
"""


################################################################################
import sys
import os
import mpi4py
import logging

sys.path.insert(0, os.path.abspath(__file__ + "/../../../GPTune/"))
logging.getLogger('matplotlib.font_manager').disabled = True

from autotune.search import *
from autotune.space import *
from autotune.problem import *
from gptune import * # import all

import argparse
from mpi4py import MPI
import numpy as np
import time

# from callopentuner import OpenTuner
# from callhpbandster import HpBandSter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.dirname(HERE)+ '/plopper')
from plopper import Plopper

dir_path = os.path.dirname(os.path.realpath(__file__))
kernel_idx = dir_path.rfind('/')
kernel = dir_path[kernel_idx+1:]
obj = Plopper(dir_path+'/mmm_block.cpp',dir_path)

# from GPTune import *

################################################################################

# Define Problem

# YL: for the spaces, the following datatypes are supported:
# Real(lower, upper, transform="normalize", name="yourname")
# Integer(lower, upper, transform="normalize", name="yourname")
# Categoricalnorm(categories, transform="onehot", name="yourname")


# Argmin{x} objectives(t,x), for x in [0., 1.]


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-nodes', type=int, default=1,help='Number of machine nodes')
    parser.add_argument('-cores', type=int, default=2,help='Number of cores per machine node')
    parser.add_argument('-machine', type=str,default='-1', help='Name of the computer (not hostname)')
    parser.add_argument('-optimization', type=str,default='GPTune', help='Optimization algorithm (opentuner, hpbandster, GPTune)')
    parser.add_argument('-ntask', type=int, default=1, help='Number of tasks')
    parser.add_argument('-nrun', type=int, default=20, help='Number of runs per task')
    parser.add_argument('-perfmodel', type=int, default=0, help='Whether to use the performance model')
    parser.add_argument('-tvalue', type=float, default=1.0, help='Input task t value')
    parser.add_argument('-tla1', type=int, default=0, help='Whether perform TLA after MLA when optimization is GPTune') 
    parser.add_argument('-dsize', type=str,default='s', help='problem size')
    args = parser.parse_args()

    return args

input_sizes = {}
input_sizes['s']  = [int(100)] 
input_sizes['sm'] = [int(150)]
input_sizes['m']  = [int(200)]
input_sizes['ml'] = [int(250)]
input_sizes['l']  = [int(300)]
input_sizes['xl'] = [int(400)]

x1=['BLOCK_SIZE']
def objectives(point: dict):
    t = point['t']
    d_size = str(t)
#     print (point['x'])
#     print (d_size)
    def plopper_func(x):
        x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
#         value = [point[x1[0]]]
        value = x
        print('CONFIG:',point)
        params = ["BLOCK_SIZE"]
        result = obj.findRuntime(value, params, d_size)
        return result

    x = np.array([point['x']])
#     results = plopper_func(x)
    results = 1.0
    print('OUTPUT:%f',results)
    return [np.float(results)]

# test=1  # make sure to set global variables here, rather than in the main function
def models(point):
    """
    f(t,x) = exp(- (x + 1) ^ (t + 1) * cos(2 * pi * x)) * (sin( (t + 2) * (2 * pi * x) ) + sin( (t + 2)^(2) * (2 * pi * x) + sin ( (t + 2)^(3) * (2 * pi *x))))
    """
    # global test
    t = point['t']
    x = point['x']
    a = 2 * np.pi
    b = a * t
    c = a * x
    d = np.exp(- (x + 1) ** (t + 1)) * np.cos(c)
    e = np.sin((t + 2) * c) + np.sin((t + 2)**2 * c) + np.sin((t + 2)**3 * c)
    f = d * e + 1
    # print('dd',test)

    """
    f(t,x) = x^2+t
    """
    # t = point['t']
    # x = point['x']
    # f = 20*x**2+t
    # time.sleep(1.0)

    return [f*(1+np.random.uniform()*0.1)]

def cst1(x):
    return x <= 100

def main():

    import matplotlib.pyplot as plt
    global model_functions
    global tvalue
    
    global nodes
    global cores

    # Parse command line arguments
    args = parse_args()
    ntask = args.ntask
    nrun = args.nrun
    tvalue = args.tvalue
    TUNER_NAME = args.optimization
    perfmodel = args.perfmodel
    tla1 = args.tla1
    DSIZE = args.dsize
    tuning_metadata = {
        "tuning_problem_name": "xsbench",
        "use_crowd_repo": "no",
        "load_func_eval": "no",
        "machine_configuration": {
            "machine_name": "mymachine",
            "haswell": { "nodes": 1, "cores": 56 }
        },
        "software_configuration": {},
        "loadable_machine_configurations": {
            "mymachine": {
                "myprocessor": {
                    "nodes": 1,
                    "cores": 56
                }
            }
        },
        "loadable_software_configurations": {
        }
    }    
    
    (machine, processor, nodes, cores) = GetMachineConfiguration(meta_dict = tuning_metadata)
    print ("machine: " + machine + " processor: " + processor + " num_nodes: " + str(nodes) + " num_cores: " + str(cores))
    os.environ['MACHINE_NAME'] = machine
    os.environ['TUNER_NAME'] = TUNER_NAME

#     input_space     = Space([Real(99., 500., transform="normalize", name="t")])
#     parameter_space = Space([Real(1., 100., transform="normalize", name="x")])
    input_space     = Space([Integer(1, 500, transform="normalize", name="t")])
    parameter_space = Space([Integer(1, 100, transform="normalize", name="x")])
#     parameter_space = Space([Real(0., 1., transform="normalize", name="x")])
#     input_space = Space([Real(0., 0.0001, "uniform", "normalize", name="t")])
#     parameter_space = Space([Real(-1., 1., "uniform", "normalize", name="x")])

    output_space = Space([Real(float('-Inf'), float('Inf'), name="y")])
    constraints = {"cst1": "x >= 1 and x <= 100"}
    if(perfmodel==1):
        problem = TuningProblem(input_space, parameter_space,output_space, objectives, constraints, models)  # with performance model
    else:
        problem = TuningProblem(input_space, parameter_space,output_space, objectives, constraints, None)  # no performance model
    historydb = HistoryDB(meta_dict=tuning_metadata)
    computer = Computer(nodes=nodes, cores=cores, hosts=None)
    options = Options()
    options['model_restarts'] = 1

    options['distributed_memory_parallelism'] = False
    options['shared_memory_parallelism'] = False

    options['objective_evaluation_parallelism'] = False
    options['objective_multisample_threads'] = 1
    options['objective_multisample_processes'] = 1
    options['objective_nprocmax'] = 1

    options['model_processes'] = 1
    # options['model_threads'] = 1
    # options['model_restart_processes'] = 1

    # options['search_multitask_processes'] = 1
    # options['search_multitask_threads'] = 1
    # options['search_threads'] = 16


    # options['mpi_comm'] = None
    #options['mpi_comm'] = mpi4py.MPI.COMM_WORLD
    options['model_class'] = 'Model_LCM' #'Model_GPy_LCM'
    options['verbose'] = False
    # options['sample_algo'] = 'MCS'
    # options['sample_class'] = 'SampleLHSMDU'

    options.validate(computer=computer)

    if ntask == 1:
#         giventask = [[round(tvalue,1)]]
        giventask = [[300]]
    elif ntask == 2:
#         giventask = [[round(tvalue,1)],[round(tvalue*2.0,1)]]
        giventask = [[200],[100]]
#         giventask = [[100],[200]]
    elif ntask == 3:
#         giventask = [[round(tvalue,1)],[round(tvalue*2.0,1)]]
        giventask = [[300],[200],[100]]
    elif ntask == 4:
#         giventask = [[round(tvalue,1)],[round(tvalue*2.0,1)]]
        giventask = [[input_sizes[DSIZE][0]],[input_sizes['s'][0]],[input_sizes['m'][0]],[input_sizes['l'][0]]]
        print ('.....target problem size is', DSIZE, giventask)
    else:
        giventask = [[round(tvalue*float(i+1),1)] for i in range(ntask)]

    model_functions = {}
    for i in range(1,len(giventask),1):
        tvalue_ = int(giventask[i][0])
        print ('======================================',tvalue_)
        meta_dict = {
            "tuning_problem_name":"xsbench",
            "modeler":"Model_LCM",
            "task_parameters":[[tvalue_]],
            "input_space": [{"name":"t","type":"int","transformer":"normalize","lower_bound":1,"upper_bound":500}],
            "parameter_space": [{"name":"x","type":"int","transformer":"normalize","lower_bound":1,"upper_bound":100}],
            "output_space": [{"name":"y","type":"real","transformer":"identity"}],
            "loadable_machine_configurations":{"mymachine":{"myprocessor":{"nodes":[1],"cores":53}}},
            "loadable_software_configurations":{}
        }
#         print (meta_dict)
        model_functions[tvalue_] = LoadSurrogateModelFunction(meta_path=None, meta_dict=meta_dict)               
        
    NI=len(giventask)  ## number of tasks
    NS=nrun ## number of runs 

    TUNER_NAME = os.environ['TUNER_NAME']

    if(TUNER_NAME=='GPTune'):
        data = Data(problem)
        gt = GPTune(problem, computer=computer, data=data, options=options, historydb=historydb, driverabspath=os.path.abspath(__file__))
        (data, modeler, stats) = gt.MLA(NS=NS, Igiven=giventask, NI=NI, NS1=int(NS/2))
        # (data, modeler, stats) = gt.MLA(NS=NS, Igiven=giventask, NI=NI, NS1=NS-1)
        print("stats: ", stats)
        """ Print all input and parameter samples """
        for tid in range(NI):
            print("tid: %d" % (tid))
            print("    t:%f " % (data.I[tid][0]))
            print("    Ps ", data.P[tid])
            print("    Os ", data.O[tid].tolist())
            print('    Popt ', data.P[tid][np.argmin(data.O[tid])], 'Oopt ', min(data.O[tid])[0], 'nth ', np.argmin(data.O[tid]))

#         if(tla1==1):
#             """ Call TLA for 2 new tasks using the constructed LCM model"""
#             print (gt)
            
# #             newtask = [[400, 500], [800, 600]]
#             newtask = [[400]]
#             (aprxopts, objval, stats) = gt.TLA1(newtask, NS=None)
#             print("stats: ", stats)

#             """ Print the optimal parameters and function evaluations"""
#             for tid in range(len(newtask)):
#                 print("new task: %s" % (newtask[tid]))
#                 print('    predicted Popt: ', aprxopts[tid], ' objval: ', objval[tid])            
            
            
#     if(TUNER_NAME=='opentuner'):
#         (data,stats)=OpenTuner(T=giventask, NS=NS, tp=problem, computer=computer, run_id="OpenTuner", niter=1, technique=None)
#         print("stats: ", stats)
#         """ Print all input and parameter samples """
#         for tid in range(NI):
#             print("tid: %d" % (tid))
#             print("    t:%f " % (data.I[tid][0]))
#             print("    Ps ", data.P[tid])
#             print("    Os ", data.O[tid].tolist())
#             print('    Popt ', data.P[tid][np.argmin(data.O[tid])], 'Oopt ', min(data.O[tid])[0], 'nth ', np.argmin(data.O[tid]))

#     if(TUNER_NAME=='hpbandster'):
#         (data,stats)=HpBandSter(T=giventask, NS=NS, tp=problem, computer=computer, run_id="HpBandSter", niter=1)
#         print("stats: ", stats)
#         """ Print all input and parameter samples """
#         for tid in range(NI):
#             print("tid: %d" % (tid))
#             print("    t:%f " % (data.I[tid][0]))
#             print("    Ps ", data.P[tid])
#             print("    Os ", data.O[tid].tolist())
#             print('    Popt ', data.P[tid][np.argmin(data.O[tid])], 'Oopt ', min(data.O[tid])[0], 'nth ', np.argmin(data.O[tid]))

if __name__ == "__main__":
    main()
