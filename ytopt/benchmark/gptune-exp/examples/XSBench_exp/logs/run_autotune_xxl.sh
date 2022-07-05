#! /usr/bin/env bash
source activate ytune
cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/XSBench_exp/xsbench_xxl
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rf_xxl_xsbench.csv
mv exe_times.npy exe_times_rf_xxl_xsbench.npy
python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rs_xxl_xsbench.csv
mv exe_times.npy exe_times_rs_xxl_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/lu_exp/lu_ml
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rs_ml_lu.csv
# mv exe_times.npy exe_times_rs_ml_lu.npy
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_ml_lu.csv
# mv exe_times.npy exe_times_rf_ml_lu.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/lu_exp/lu_sm
# python learnBO_1_kde_ytopt_6d.v4_1.GS.py
# mv results_kde.csv results_kde_sm_lu.csv
# mv exe_times_kde.npy exe_times_kde_sm_lu.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/lu_exp/lu_ml
# python learnBO_1_kde_ytopt_all.v4_1.GS.py
# mv results_kde.csv results_kde_ml_lu.csv
# mv exe_times_kde.npy exe_times_kde_ml_lu.npy
