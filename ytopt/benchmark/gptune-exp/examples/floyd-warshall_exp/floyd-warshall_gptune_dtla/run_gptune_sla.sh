#!/bin/bash
#SBATCH --job-name=1cpu_gptune
#SBATCH --account=perfopt
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=48:00:00
#SBATCH --output=stdout_gptune_sla_run1.%j

# module load nvhpc/21.5-oxhtyof
source activate /home/jkoo/.conda/envs/gptune/
cd ~/spack
. share/spack/setup-env.sh 
spack load gptune 
cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/floyd-warshall_exp/floyd-warshall_gptune_dtla
rm -rf ./tmp_results*
rm -rf ./tmp_files*
mkdir ./TLA_experiments
################################# RUN SLA for small 
# cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/XSBench_exp_gpu/xsbench-omp_gptune_dtla/offload
mkdir ./tmp_results
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 200 -ntask 1 -perfmodel 0 -optimization GPTune -dsize s 
mkdir ./TLA_experiments/SLA-GPTune-s-200/ 
mv gptune.db/floyd-warshall.json ./TLA_experiments/SLA-GPTune-s-200/floyd-warshall.json 
mv gptune.db/results.csv ./TLA_experiments/SLA-GPTune-s-200/results.csv
# mv save_results.npy save_results_sla_s_floyd-warshall.npy
# mv tmp_results tmp_results_sla_s
mv tmp_files tmp_files_sla_s
################################# RUN SLA for medium 
# cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/XSBench_exp_gpu/xsbench-omp_gptune_dtla/offload
mkdir ./tmp_results
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 200 -ntask 1 -perfmodel 0 -optimization GPTune -dsize m
mkdir ./TLA_experiments/SLA-GPTune-m-200/ 
mv gptune.db/floyd-warshall.json ./TLA_experiments/SLA-GPTune-m-200/floyd-warshall.json 
mv gptune.db/results.csv ./TLA_experiments/SLA-GPTune-m-200/results.csv
# mv save_results.npy save_results_sla_m_floyd-warshall.npy
# mv tmp_results tmp_results_sla_m
mv tmp_files tmp_files_sla_m

################################# RUN SLA for large 
# cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/XSBench_exp_gpu/xsbench-omp_gptune_dtla/offload
mkdir ./tmp_results
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 200 -ntask 1 -perfmodel 0 -optimization GPTune -dsize l 
mkdir ./TLA_experiments/SLA-GPTune-l-200/ 
mv gptune.db/floyd-warshall.json ./TLA_experiments/SLA-GPTune-l-200/floyd-warshall.json 
mv gptune.db/results.csv ./TLA_experiments/SLA-GPTune-l-200/results.csv
# mv save_results.npy save_results_sla_l_floyd-warshall.npy
# mv tmp_results tmp_results_sla_l
mv tmp_files tmp_files_sla_l

# ################################# RUN DTLA on sm 
# cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/XSBench_exp_gpu/xsbench-omp_gptune_dtla/offload
mkdir ./tmp_results
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 30 -ntask 1 -perfmodel 0 -optimization GPTune -dsize sm 
mkdir ./TLA_experiments/SLA-GPTune-sm-30/ 
mv gptune.db/floyd-warshall.json ./TLA_experiments/SLA-GPTune-sm-30/floyd-warshall.json 
mv gptune.db/results.csv ./TLA_experiments/SLA-GPTune-sm-30/results.csv
# mv save_results.npy save_results_sla_sm_floyd-warshall.npy
# mv tmp_results tmp_results_sla_sm
mv tmp_files tmp_files_sla_sm
################################# RUN SLA for medium 
# cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/XSBench_exp_gpu/xsbench-omp_gptune_dtla/offload
mkdir ./tmp_results
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 30 -ntask 1 -perfmodel 0 -optimization GPTune -dsize ml
mkdir ./TLA_experiments/SLA-GPTune-ml-30/ 
mv gptune.db/floyd-warshall.json ./TLA_experiments/SLA-GPTune-ml-30/floyd-warshall.json 
mv gptune.db/results.csv ./TLA_experiments/SLA-GPTune-ml-30/results.csv
# mv save_results.npy save_results_sla_ml_floyd-warshall.npy
# mv tmp_results tmp_results_sla_ml
mv tmp_files tmp_files_sla_ml

################################# RUN SLA for large 
# cd /lcrc/project/EE-ECP/jkoo/code/gptune/examples/XSBench_exp_gpu/xsbench-omp_gptune_dtla/offload
mkdir ./tmp_results
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 30 -ntask 1 -perfmodel 0 -optimization GPTune -dsize xl 
mkdir ./TLA_experiments/SLA-GPTune-xl-30/ 
mv gptune.db/floyd-warshall.json ./TLA_experiments/SLA-GPTune-xl-30/floyd-warshall.json 
mv gptune.db/results.csv ./TLA_experiments/SLA-GPTune-xl-30/results.csv
# mv save_results.npy save_results_sla_xl_floyd-warshall.npy
# mv tmp_results tmp_results_sla_xl
mv tmp_files tmp_files_sla_xl

