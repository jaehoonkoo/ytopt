# #GPyOpt - Cases are important, for some reason
# import GPyOpt
# from GPyOpt.methods import BayesianOptimization
# from collections import Counter, defaultdict
# #numpy
# import numpy as np
# from numpy.random import multivariate_normal #For later example

# import pandas as pd

#Plotting tools
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from numpy.random import multivariate_normal
import matplotlib.ticker as mtick
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os, sys
from mpl_toolkits.mplot3d import Axes3D
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors.kde import KernelDensity
# import random
from tqdm import tqdm

import numpy as np
from autotune import TuningProblem
from autotune.space import *
import os, sys, time, json, math
import ConfigSpace as CS
import ConfigSpace.hyperparameters as CSH
from skopt.space import Real, Integer, Categorical
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import csv
from csv import writer
from csv import reader
from sklearn import preprocessing
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.dirname(HERE)+ '/plopper')
from plopper import Plopper
def pretty_time(seconds):
    """Format time string"""
    seconds = round(seconds, 2)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02.2f" % (hours,minutes,seconds)

Time_start = time.time()
print ('time...now', Time_start)
cs = CS.ConfigurationSpace(seed=1234)
# number of threads
p0= CSH.OrdinalHyperparameter(name='p0', sequence=['4','5','6','7','8'], default_value='8')
#block size for openmp dynamic schedule
p1= CSH.OrdinalHyperparameter(name='p1', sequence=['100','200','400','640','800','1000','1280','1600','2000'], default_value='1000')
#clang unrolling
p2= CSH.CategoricalHyperparameter(name='p2', choices=["#pragma clang loop unrolling full", " "], default_value=' ')
#omp parallel
p3= CSH.CategoricalHyperparameter(name='p3', choices=["#pragma omp parallel for", " "], default_value=' ')
# tile size for one dimension for 2D tiling
p4= CSH.OrdinalHyperparameter(name='p4', sequence=['2','4','8','16','32','64','96','128','256'], default_value='96')
# tile size for another dimension for 2D tiling
p5= CSH.OrdinalHyperparameter(name='p5', sequence=['2','4','8','16','32','64','96','128','256'], default_value='256')
p6= CSH.OrdinalHyperparameter(name='p6', sequence=['10','20','40','64','80','100','128','160','200'], default_value='100')
#thread affinity type
p7= CSH.CategoricalHyperparameter(name='p7', choices=['compact','scatter','balanced','none','disabled', 'explicit'], default_value='none')
# omp placement
p8= CSH.CategoricalHyperparameter(name='p8', choices=['cores','threads','sockets'], default_value='cores')

cs.add_hyperparameters([p0, p1, p2, p3, p4, p5, p6, p7, p8])

dir_path = os.path.dirname(os.path.realpath(__file__))
kernel_idx = dir_path.rfind('/')
kernel = dir_path[kernel_idx+1:]
obj = Plopper(dir_path+'/mmp.c',dir_path)

x1=['p0','p1','p2','p3','p4','p5','p6','p7','p8']
exe_times = []
def myobj(point: dict):

  def plopper_func(x):
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    value = [point[x1[0]],point[x1[1]],point[x1[2]],point[x1[3]],point[x1[4]],point[x1[5]],point[x1[6]],point[x1[7]],point[x1[8]]]
    print('VALUES:',point[x1[0]])
    params = ["P0","P1","P2","P3","P4","P5","P6","P7","P8"]

    result = obj.findRuntime(value, params, ' -s large -m event -l 500000') # defined(MINI_DATASET) && !defined(SMALL_DATASET) && !defined(MEDIUM_DATASET) && !defined(LARGE_DATASET) && !defined(EXTRALARGE_DATASET) && !defined(HUGE_DATASET)
    return result

  x = np.array([point[f'p{i}'] for i in range(len(point))])  
  results = plopper_func(x)
  exe_times.append(results)
  np.save(dir_path+'/exe_times_kde.npy',exe_times)
#   results_s = sorted(results)
#   results_m = results_s[1:-1]
  print('OUTPUT:%f',results, float(np.mean(results[1:])))
  return float(np.mean(results[1:]))

param_names = cs.get_hyperparameter_names()
param_vals = [] 
param_obj = {}
for i, p_name in enumerate(param_names): #cs.get_hyperparameter_names()
#     print (i,p_name)
    try: # ordinal 
        vals = list(map(int,list(cs.get_hyperparameters()[i].sequence)))
        param_vals.append(vals)
        X = np.array(vals) 
        X = X[:,np.newaxis]
        transformer = preprocessing.MinMaxScaler().fit(X)
        param_obj[p_name] = transformer
    except: ## norminal 
        vals = list(cs.get_hyperparameters()[i].choices)
#         print (vals)
        param_vals.append(vals)
        X = np.array(vals) 
        X = X[:,np.newaxis]
        transformer = preprocessing.OneHotEncoder(drop='if_binary',sparse=False).fit(X)
        param_obj[p_name] = transformer
## add input
input_sizes = {}
input_sizes['s']  = [100000] 
input_sizes['sm'] = [500000]
input_sizes['m']  = [1000000]
input_sizes['ml'] = [2500000]
input_sizes['l']  = [5000000]
input_sizes['xl'] = [10000000]
## add inputs sizes 
vals = [input_sizes['s'][0], input_sizes['xl'][0]]
param_vals.append(vals)
X = np.array(vals) 
X = X[:,np.newaxis]
transformer = preprocessing.MinMaxScaler().fit(X)
param_obj['input'] = transformer
print (param_obj)
# #### selet by best top x%
if False:
    take_n = int(len(y_eval) * 0.1)
    take_idx = np.argsort(y_eval)[-take_n:]
    X_opt = X_eval[take_idx]
    print (X_opt)   
else:
    X_opt = []
    cutoff_p = 0.1

    '''
    #### problem       S       L         XL       XXL
    size (s)      :    12      355       355      355        - nuclides
    gridpoints (g):  11,303   11,303   238,847   501,578     - grid points per nuclide
    particle   (p): 500,000  500,000   500,000   500,000     -  
    lookup     (l):                                          - 
    '''
    n_param = len(param_names)
    for i_size, o3p_tmp in zip(['s','m','l'],[1.7527, 17.7599, 88.3151]):#['s','m','l']: 0.00106, 0.0266395, 3.972039
        dataframe = pd.read_csv("results_rf_"+str(i_size)+"_rsbench.csv") # PROBLEM_SIZE	BLOCK_SIZE	exe_time	LOG(exe_time)	speedup	elapsed_sec 
        array = dataframe.values
        X_eval = array[:,:n_param]#.astype(float) ## ### size, n1, n2, p1,p2,p3,p4,p5,exe_time,speedup       
#         X_eval_encode = np.copy(X_eval)
        X_eval = np.c_[X_eval, np.array([input_sizes[i_size]]*len(X_eval))]
        X_eval_encode = []
        for i, p_name in enumerate(param_obj.keys()):
            x_tmp = X_eval[:,i]
            x_tmp = x_tmp[:,np.newaxis]
            X_eval_encode.append(param_obj[p_name].transform(x_tmp)) ## [0,1]
        X_eval_en = X_eval_encode[0] 
        for i in range(1,len(X_eval_encode)):    
            X_eval_en = np.c_[X_eval_en,X_eval_encode[i]]
                
        y_eval = o3p_tmp / array[:,n_param].astype(float) ## speedup 
        take_n = round(len(y_eval) * cutoff_p)
        take_idx = np.argsort(y_eval)[-take_n:]
        X_opt.extend(X_eval_en[take_idx].astype(float))
#     print (X_opt) 
    
X_opt_norm = X_opt

colors = ['navy']#, 'cornflowerblue']#, 'darkorange']
kernels = ['gaussian']#, 'tophat']#, 'epanechnikov']

grid = GridSearchCV(KernelDensity(),
                    {'bandwidth': np.linspace(0.001, 10, 10000)},
                    cv=max(2,round(len(X_opt_norm)*0.2))) # 20-fold cross-validation

grid.fit(X_opt_norm)
print ('grid.best_params_',grid.best_params_)

bandwidth_size = grid.best_params_['bandwidth']

X_plot_cs = cs.sample_configuration(100000) 

X_plot = [] 
for c in X_plot_cs:
    value = list(dict(c).values())
    X_plot.append(value)

X_plot = np.c_[X_plot, np.array([input_sizes['sm']]*len(X_plot))]    

X_plot_0 = []
for i, p_name in enumerate(param_obj.keys()):
    x_tmp = X_plot[:,i]
    x_tmp = x_tmp[:,np.newaxis]
    X_plot_0.append(param_obj[p_name].transform(x_tmp)) ## [0,1]

X_plot_norm = X_plot_0[0] 
for i in range(1,len(X_plot_0)):    
    X_plot_norm = np.c_[X_plot_norm,X_plot_0[i]]

lw = 2
for color, kernel in zip(colors, kernels):
    kde = KernelDensity(kernel=kernel, bandwidth=bandwidth_size).fit(X_opt_norm)
    X_te = []
    for i in range(len(X_plot_norm)):
            log_den = kde.score_samples(np.array([X_plot_norm[i]]))
            X_te.append([X_plot[i][:-1],np.exp(log_den[0])])

N_infer = 200
X_test = np.copy(X_te)
take_n_te = N_infer
take_idx = np.argsort(-1*np.array(X_test)[:,1])[:take_n_te]
X_opt_te = []# np.array(X_test)[take_idx]
for idx in take_idx:
    x_sample = X_test[idx]
    X_opt_te.append([x_sample[0],x_sample[1]])

new_kde = X_opt_te

# name of csv file 
filename = "results_kde.csv"
fields   = ['p0','p1','p2','p3','p4','p5','p6','p7','p8','exe_time','density','elapsed_sec']
# fields   = ['p1','p2','p3','p4','p5','exe_time','density']
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
#     csvwriter.writerows(rows)

    evals_infer = []
    for idx in range(N_infer):
        sample_point_val = new_kde[idx][0][-n_param:]
        print (sample_point_val)
        sample_point = {x1[0]:sample_point_val[0],
                    x1[1]:sample_point_val[1],
                    x1[2]:sample_point_val[2],
                    x1[3]:sample_point_val[3],
                    x1[4]:sample_point_val[4],
                    x1[5]:sample_point_val[5],
                    x1[6]:sample_point_val[6],
                    x1[7]:sample_point_val[7],
                    x1[8]:sample_point_val[8]}
        print (sample_point)
        res          = myobj(sample_point)
        print (sample_point, res)
        evals_infer.append(res)
        now = time.time()
        elapsed = now - Time_start
        ss = [sample_point['p0']] + [sample_point['p1']] + [sample_point['p2']] + [sample_point['p3']] +[sample_point['p4']]+[sample_point['p5']]+[sample_point['p6']]+[sample_point['p7']]+[sample_point['p8']]+[res]+[new_kde[idx][1]]+[elapsed]
        csvwriter.writerow(ss)
        csvfile.flush()
csvfile.close()   





    
    
    

