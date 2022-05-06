# import numpy as np
# from autotune import TuningProblem
# from autotune.space import *
# import os, sys, time, json, math
# import ConfigSpace as CS
# import ConfigSpace.hyperparameters as CSH
# from skopt.space import Real, Integer, Categorical
# import csv, time 
# from csv import writer
# from csv import reader

# import pandas as pd
# from sdv.tabular import GaussianCopula
# from sdv.tabular import CopulaGAN
# from sdv.evaluation import evaluate
# from sdv.constraints import CustomConstraint, Between
import random, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--max_evals', type=int, default=10, help='maximum number of evaluations')
parser.add_argument('--n_refit', type=int, default=0, help='refit the model')
parser.add_argument('--seed', type=int, default=1234, help='set seed')
parser.add_argument('--top', type=float, default=0.1, help='how much to train')
parser.add_argument('--target', type=str, default='xl', help='target task')
parser.add_argument('-i', '--item', action='store', dest='alist',
                    type=int, nargs='*', default=[1, 2, 3],
                    help="Examples: -i item1 item2, -i item3")
args = parser.parse_args()

MAX_EVALS   = int(args.max_evals)
N_REFIT     = int(args.n_refit)
TOP         = float(args.top)
RANDOM_SEED = int(args.seed)
TARGET_task = str(args.target)
ITEM = args.alist
print ('max_evals',MAX_EVALS, 'number of refit', N_REFIT, 'how much to train', TOP, 'seed', RANDOM_SEED, 'target task', TARGET_task)

print (ITEM)

