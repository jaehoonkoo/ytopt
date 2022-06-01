#!/bin/bash
#SBATCH --job-name=cov_ytopt
#SBATCH --account=perfopt
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --output=stdout_sdv_run1.%j

# module load nvhpc/21.5-oxhtyof
source /soft/anaconda3/2020.02/etc/profile.d/conda.sh
source activate /home/jkoo/.conda/envs/ytune
cd /lcrc/project/EE-ECP/jkoo/code/ytopt/ytopt/benchmark/floyd-warshall_exp/floyd-warshall_target/
# ##############
# python Run_online_TL.py --kernel_name floyd-warshall --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 340 -imin 60 -imax 8600
# mv tmp_files tmp_files_sm
# mv results_sdv.csv results_sdv_sm_floyd-warshall.csv
# # ##############
# python Run_online_TL.py --kernel_name floyd-warshall --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 1650 -imin 60 -imax 8600
# mv tmp_files tmp_files_ml
# mv results_sdv.csv results_sdv_ml_floyd-warshall.csv
# # ##############
# python Run_online_TL.py --kernel_name floyd-warshall --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 5600 -imin 60 -imax 8600
# mv tmp_files tmp_files_xl
# mv results_sdv.csv results_sdv_xl_floyd-warshall.csv
# ##############
python Run_online_TL.py --kernel_name floyd-warshall --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 340 -imin 60 -imax 8600
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_floyd-warshall_refit.csv
# ##############
python Run_online_TL.py --kernel_name floyd-warshall --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 1650 -imin 60 -imax 8600
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_floyd-warshall_refit.csv
# ##############
python Run_online_TL.py --kernel_name floyd-warshall --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 5600 -imin 60 -imax 8600
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_floyd-warshall_refit.csv
# mkdir ./tmp_results
# rm ytopt.log
# python -m ytopt.search.ambs --evaluator subprocess --problem problem_all.Problem --max-evals=30 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468 --set-NI 10
# mv results.csv results_rf_ml_xsbench.csv
# mv tmp_results tmp_results_rf_run1
# mv tmp_files tmp_files_rf_run1
# mv ytopt.log ytopt_rf_ml_xsbench_run1.log
# ##############
# rm ytopt.log
# mkdir ./tmp_results
# python -m ytopt.search.ambs --evaluator subprocess --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468 --set-NI 10
# mv results.csv results_rs_l_covariance.csv
# mv tmp_results tmp_results_rs_run1
# mv tmp_files tmp_files_rs_run1
# mv ytopt.log ytopt_rs_l_covariance_run1.log
# # ##############
# rm ytopt.log
# mkdir ./tmp_results
# python -m ytopt.search.ambs --evaluator subprocess --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468 --set-NI 10
# mv results.csv results_rf_l_covariance.csv
# mv tmp_results tmp_results_rf_run1
# mv tmp_files tmp_files_rf_run1
# mv ytopt.log ytopt_rf_l_covariance_run1.log
##############
# mkdir ./tmp_results
# python learnBO_1_sdv_itr.py
# mv results_sdv_itr.csv results_sdv_itr_ml_xsbench.csv
# mv tmp_results tmp_results_sdv_itr_run1
# mv tmp_files tmp_files_sdv_itr_run1
#############
# mkdir ./tmp_results
# python learnBO_1_sdv.py
# mv results_sdv.csv results_sdv_ml_xsbench.csv
# mv tmp_results tmp_results_sdv_run1
# mv tmp_files tmp_files_sdv_run1