#!/bin/bash
#SBATCH --job-name=cov_ytopt
#SBATCH --account=perfopt
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --output=stdout_sdv_run1_seed.%j

# module load nvhpc/21.5-oxhtyof
source /soft/anaconda3/2020.02/etc/profile.d/conda.sh
source activate /home/jkoo/.conda/envs/ytune
cd /lcrc/project/EE-ECP/jkoo/code/ytopt/ytopt/benchmark/covariance_exp/covariance_target/
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 160 180 -imin 28 32 -imax 3800 4000 --seed 2022
# mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_covariance_2022.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 720 830 -imin 28 32 -imax 3800 4000 --seed 2022
# mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_covariance_2022.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 2600 3000 -imin 28 32 -imax 3800 4000 --seed 2022
# mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_covariance_2022.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 160 180 -imin 28 32 -imax 3800 4000 --seed 2022
# mv tmp_files tmp_files_sm_refit
mv results_sdv.csv results_sdv_sm_covariance_refit_2022.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 720 830 -imin 28 32 -imax 3800 4000 --seed 2022
# mv tmp_files tmp_files_ml_refit
mv results_sdv.csv results_sdv_ml_covariance_refit_2022.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 2600 3000 -imin 28 32 -imax 3800 4000 --seed 2022
# mv tmp_files tmp_files_xl_refit
mv results_sdv.csv results_sdv_xl_covariance_refit_2022.csv
##############
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 160 180 -imin 28 32 -imax 3800 4000 --seed 9999
# mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_covariance_9999.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 720 830 -imin 28 32 -imax 3800 4000 --seed 9999
# mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_covariance_9999.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 2600 3000 -imin 28 32 -imax 3800 4000 --seed 9999
# mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_covariance_9999.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 160 180 -imin 28 32 -imax 3800 4000 --seed 9999
# mv tmp_files tmp_files_sm_refit
mv results_sdv.csv results_sdv_sm_covariance_refit_9999.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 720 830 -imin 28 32 -imax 3800 4000 --seed 9999
# mv tmp_files tmp_files_ml_refit
mv results_sdv.csv results_sdv_ml_covariance_refit_9999.csv
##############
python Run_online_TL.py --kernel_name covariance --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 2600 3000 -imin 28 32 -imax 3800 4000 --seed 9999
# mv tmp_files tmp_files_xl_refit
mv results_sdv.csv results_sdv_xl_covariance_refit_9999.csv
##############

