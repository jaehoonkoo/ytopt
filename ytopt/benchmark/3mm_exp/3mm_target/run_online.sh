#!/bin/bash
#SBATCH --job-name=3mm_ytopt
#SBATCH --account=perfopt
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --output=stdout_sdv_run1.%j

# module load nvhpc/21.5-oxhtyof
source /soft/anaconda3/2020.02/etc/profile.d/conda.sh
source activate /home/jkoo/.conda/envs/ytune
cd /lcrc/project/EE-ECP/jkoo/code/ytopt/ytopt/benchmark/3mm_exp/3mm_target/
# ##############
python Run_online_TL.py --kernel_name 3mm --max_evals 30 --n_refit 30 --top 0.3 --nparam 10  --param_start 0 --target sm -itarget 110 120 130 140 150 -imin 16 18 20 22 24 -imax 3200 3600 4000 4400 4800
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_3mm.csv
# ##############
python Run_online_TL.py --kernel_name 3mm --max_evals 30 --n_refit 30 --top 0.3 --nparam 10  --param_start 0 --target ml -itarget 490 545 600 655 710 -imin 16 18 20 22 24 -imax 3200 3600 4000 4400 4800
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_3mm.csv
# ##############
python Run_online_TL.py --kernel_name 3mm --max_evals 30 --n_refit 30 --top 0.3 --nparam 10  --param_start 0 --target xl -itarget 1600 1800 2000 2200 2400 -imin 16 18 20 22 24 -imax 3200 3600 4000 4400 4800
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_3mm.csv
# ##############
python Run_online_TL.py --kernel_name 3mm --max_evals 30 --n_refit 5 --top 0.3 --nparam 10  --param_start 0 --target sm -itarget 110 120 130 140 150 -imin 16 18 20 22 24 -imax 3200 3600 4000 4400 4800
mv tmp_files tmp_files_sm
mv results_sdv.csv results_sdv_sm_3mm_refit.csv
# ##############
python Run_online_TL.py --kernel_name 3mm --max_evals 30 --n_refit 5 --top 0.3 --nparam 10  --param_start 0 --target ml -itarget 490 545 600 655 710 -imin 16 18 20 22 24 -imax 3200 3600 4000 4400 4800
mv tmp_files tmp_files_ml
mv results_sdv.csv results_sdv_ml_3mm_refit.csv
# ##############
python Run_online_TL.py --kernel_name 3mm --max_evals 30 --n_refit 5 --top 0.3 --nparam 10  --param_start 0 --target xl -itarget 1600 1800 2000 2200 2400 -imin 16 18 20 22 24 -imax 3200 3600 4000 4400 4800
mv tmp_files tmp_files_xl
mv results_sdv.csv results_sdv_xl_3mm_refit.csv
# ##############