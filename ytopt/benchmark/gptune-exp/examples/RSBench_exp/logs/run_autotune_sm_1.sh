#! /usr/bin/env bash
source activate ytune
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/RSBench_exp/rsbench_sm
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_sm_rsbench.csv
# mv exe_times.npy exe_times_rf_sm_rsbench.npy
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rs_sm_rsbench.csv
# mv exe_times.npy exe_times_rs_sm_rsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/RSBench_exp/rsbench_sm
# python learnBO_1_sdv_itr_time.py
# mv results_sdv_itr_time.csv results_sdv_sm_rsbench_itr_time.csv
# mv exe_times_sdv_itr_time.npy exe_times_sdv_sm_rsbench_itr_time.npy
# python learnBO_1_sdv_time.py
# mv results_sdv_time.csv results_sdv_sm_rsbench_time.csv
# mv exe_times_sdv_time.npy exe_times_sdv_sm_rsbench_time.npy
cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/RSBench_exp/rsbench_sm
python learnBO_1_kde_ytopt_all.v5.GS.py
mv results_kde.csv results_kde_sm_rsbench.csv
mv exe_times_kde.npy exe_times_kde_sm_rsbench.npy
