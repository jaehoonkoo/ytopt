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
cd /lcrc/project/EE-ECP/jkoo/code/ytopt/ytopt/benchmark/syr2k_exp/syr2k_target/
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 30 --top 0.3 --nparam 6 --param_start 0 --target sm -itarget 130 160 -imin 20 30 -imax 3000 3800 --seed 2022
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_syr2k_2022.csv
# ##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 30 --top 0.3 --nparam 6 --param_start 0 --target ml -itarget 600 720 -imin 20 30 -imax 3000 3800 --seed 2022
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_syr2k_2022.csv
# ##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 30 --top 0.3 --nparam 6 --param_start 0 --target xl -itarget 2000 2600 -imin 20 30 -imax 3000 3800 --seed 2022
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_syr2k_2022.csv
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 5 --top 0.3 --nparam 6 --param_start 0 --target sm -itarget 130 160 -imin 20 30 -imax 3000 3800 --seed 2022
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_syr2k_refit_2022.csv
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 5 --top 0.3 --nparam 6 --param_start 0 --target ml -itarget 600 720 -imin 20 30 -imax 3000 3800 --seed 2022
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_syr2k_refit_2022.csv
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 5 --top 0.3 --nparam 6 --param_start 0 --target xl -itarget 2000 2600 -imin 20 30 -imax 3000 3800 --seed 2022
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_syr2k_refit_2022.csv
##############
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 30 --top 0.3 --nparam 6 --param_start 0 --target sm -itarget 130 160 -imin 20 30 -imax 3000 3800 --seed 9999
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_syr2k_9999.csv
# ##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 30 --top 0.3 --nparam 6 --param_start 0 --target ml -itarget 600 720 -imin 20 30 -imax 3000 3800 --seed 9999
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_syr2k_9999.csv
# ##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 30 --top 0.3 --nparam 6 --param_start 0 --target xl -itarget 2000 2600 -imin 20 30 -imax 3000 3800 --seed 9999
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_syr2k_9999.csv
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 5 --top 0.3 --nparam 6 --param_start 0 --target sm -itarget 130 160 -imin 20 30 -imax 3000 3800 --seed 9999
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_syr2k_refit_9999.csv
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 5 --top 0.3 --nparam 6 --param_start 0 --target ml -itarget 600 720 -imin 20 30 -imax 3000 3800 --seed 9999
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_syr2k_refit_9999.csv
##############
python Run_online_TL.py --kernel_name syr2k --max_evals 30 --n_refit 5 --top 0.3 --nparam 6 --param_start 0 --target xl -itarget 2000 2600 -imin 20 30 -imax 3000 3800 --seed 9999
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_syr2k_refit_9999.csv