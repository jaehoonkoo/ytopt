#! /usr/bin/env bash
source activate ytune
cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/XSBench_exp/xsbench_m
python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rf_m_xsbench.csv
mv exe_times.npy exe_times_rf_m_xsbench.npy
python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rs_m_xsbench.csv
mv exe_times.npy exe_times_rs_m_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/lu_exp/lu_m
# python problem_all_rerun.py
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rs_m_lu.csv
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_m_lu.csv
#problem_all_rs.py
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=100 --learner RF