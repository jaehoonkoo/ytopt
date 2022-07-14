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
cd /lcrc/project/EE-ECP/jkoo/code/ytopt/ytopt/benchmark/lu_exp/lu_target/
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 260 -imin 40 -imax 6000 --seed 2022
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_lu_2022.csv
# ##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 1200 -imin 40 -imax 6000 --seed 2022
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_lu_2022.csv
# ##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 4000 -imin 40 -imax 6000 --seed 2022
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_lu_2022.csv
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 260 -imin 40 -imax 6000 --seed 2022
mv tmp_files tmp_files_sm_refit
mv results_sdv.csv results_sdv_sm_lu_refit_2022.csv
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 1200 -imin 40 -imax 6000 --seed 2022
mv tmp_files tmp_files_ml_refit
mv results_sdv.csv results_sdv_ml_lu_refit_2022.csv
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 4000 -imin 40 -imax 6000 --seed 2022
mv tmp_files tmp_files_xl_refit
mv results_sdv.csv results_sdv_xl_lu_refit_2022.csv
##############
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 260 -imin 40 -imax 6000 --seed 9999
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_lu_9999.csv
# ##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 1200 -imin 40 -imax 6000 --seed 9999
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_lu_9999.csv
# ##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 30 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 4000 -imin 40 -imax 6000 --seed 9999
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_lu_9999.csv
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target sm -itarget 260 -imin 40 -imax 6000 --seed 9999
mv tmp_files tmp_files_sm_refit
mv results_sdv.csv results_sdv_sm_lu_refit_9999.csv
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target ml -itarget 1200 -imin 40 -imax 6000 --seed 9999
mv tmp_files tmp_files_ml_refit
mv results_sdv.csv results_sdv_ml_lu_refit_9999.csv
##############
python Run_online_TL.py --kernel_name lu --max_evals 30 --n_refit 5 --top 0.3 --nparam 5 --param_start 1 --target xl -itarget 4000 -imin 40 -imax 6000 --seed 9999
mv tmp_files tmp_files_xl_refit
mv results_sdv.csv results_sdv_xl_lu_refit_9999.csv
