#! /usr/bin/env bash
source activate ytune
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/XSBench_exp/xsbench_ml
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rf_ml_xsbench.csv
# mv exe_times.npy exe_times_rf_ml_xsbench.npy
# python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
# mv results.csv results_rs_ml_xsbench.csv
# mv exe_times.npy exe_times_rs_ml_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/XSBench_exp/xsbench_ml
# python learnBO_1_kde_ytopt_all.v5.GS.py
# mv results_kde.csv results_kde_ml_xsbench.csv
# mv exe_times_kde.npy exe_times_kde_ml_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_ml_xsbench.csv
# mv exe_times_sdv.npy exe_times_sdv_ml_xsbench.npy
# python learnBO_1_kde_ytopt_all.v5.GS.py
# mv results_kde.csv results_kde_ml_xsbench.csv
# mv exe_times_kde.npy exe_times_kde_ml_xsbench.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_ml_xsbench_n.csv
# mv exe_times_sdv.npy exe_times_sdv_ml_xsbench_n.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv_30
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_ml_xsbench_30_n.csv
# mv exe_times_sdv.npy exe_times_sdv_ml_xsbench_30_n.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv_50
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_ml_xsbench_50_n.csv
# mv exe_times_sdv.npy exe_times_sdv_ml_xsbench_50_n.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv_rs
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_ml_xsbench_rs.csv
# mv exe_times_sdv.npy exe_times_sdv_ml_xsbench_rs.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv
# python learnBO_1_sdv_itr.py
# mv results_sdv_itr.csv results_sdv_ml_xsbench_itr.csv
# mv exe_times_sdv_itr.npy exe_times_sdv_ml_xsbench_itr.npy
cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv
python learnBO_1_sdv_time.py
mv results_sdv_time.csv results_sdv_ml_xsbench_time_re.csv
mv exe_times_sdv_time.npy exe_times_sdv_ml_xsbench_time_re.npy
# cd /gpfs/jlse-fs0/users/jkoo/code/kde/SDV/Benchmarks/XSBench_exp/xsbench_ml_sdv
# python learnBO_1_sdv_itr_time.py
# mv results_sdv_itr_time.csv results_sdv_ml_xsbench_itr_time_re.csv
# mv exe_times_sdv_itr_time.npy exe_times_sdv_ml_xsbench_itr_time_re.npy



