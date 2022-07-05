#! /usr/bin/env bash
source activate ytune
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/XSBench_exp/xsbench_sm
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_sm_xsbench.csv
# mv exe_times.npy exe_times_rf_sm_xsbench.npy
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rs_sm_xsbench.csv
# mv exe_times.npy exe_times_rs_sm_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/XSBench_exp/xsbench_sm
# python learnBO_1_kde_ytopt_all.v5.GS.py
# mv results_kde.csv results_kde_sm_xsbench.csv
# mv exe_times_kde.npy exe_times_kde_sm_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_sm_sdv
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_sm_xsbench_n.csv
# mv exe_times_sdv.npy exe_times_sdv_sm_xsbench_n.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_sm_sdv_30
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_sm_xsbench_30_n.csv
# mv exe_times_sdv.npy exe_times_sdv_sm_xsbench_30_n.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_sm_sdv_50
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_sm_xsbench_50_n.csv
# mv exe_times_sdv.npy exe_times_sdv_sm_xsbench_50_n.npy
# python learnBO_1_kde_ytopt_all.v5.GS.py
# mv results_kde_xx.csv results_kde_sm_xsbench_xx.csv
# mv exe_times_kde_xx.npy exe_times_kde_sm_xsbench_xx.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_sm_sdv_rs
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_sm_xsbench_rs.csv
# mv exe_times_sdv.npy exe_times_sdv_sm_xsbench_rs.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_sm_sdv
# python learnBO_1_sdv_time.py
# mv results_sdv_time.csv results_sdv_sm_xsbench_time.csv
# mv exe_times_sdv_time.npy exe_times_sdv_sm_xsbench_time.npy
cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_sm_sdv
python learnBO_1_sdv_itr_time.py
mv results_sdv_itr_time.csv results_sdv_sm_xsbench_itr_time.csv
mv exe_times_sdv_itr_time.npy exe_times_sdv_sm_xsbench_itr_time.npy















