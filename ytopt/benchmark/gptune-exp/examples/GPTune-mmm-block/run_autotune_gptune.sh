#! /usr/bin/env bash
source activate gptune
cd ~/spack
. share/spack/setup-env.sh 
spack load gptune 
cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/GPTune-mmm-block
mpirun -n 1 python demo_tla1.py -nrun 5 -ntask 1 -perfmodel 0 -optimization GPTune
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_s
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_s_xsbench_re.csv
# mv exe_times.npy exe_times_rf_s_xsbench_re.npy
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rs_s_xsbench_re.csv
# mv exe_times.npy exe_times_rs_s_xsbench_re.npy