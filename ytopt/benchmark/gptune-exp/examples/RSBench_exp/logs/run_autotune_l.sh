#! /usr/bin/env bash
source activate ytune
cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/RSBench_exp/rsbench_l
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_l_rsbench.csv
# mv exe_times.npy exe_times_rf_l_rsbench.npy
python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rs_l_rsbench.csv
mv exe_times.npy exe_times_rs_l_rsbench.npy

