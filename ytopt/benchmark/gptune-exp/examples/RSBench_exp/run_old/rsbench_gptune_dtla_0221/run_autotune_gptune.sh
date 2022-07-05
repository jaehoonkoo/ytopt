#! /usr/bin/env bash
source activate gptune
cd ~/spack
. share/spack/setup-env.sh 
spack load gptune 
### go the directory 
cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla
# mpirun -n 1 python demo_tla1.py -nrun 200 -ntask 3 -perfmodel 0 -optimization GPTune -tla 1

################################ RUN SLA for small 
# cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla_s
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 200 -ntask 1 -perfmodel 0 -optimization GPTune -dsize s 
mv gptune.db/rsbench.json ./TLA_experiments/SLA-GPTune-s-200/
mv save_results.npy save_results_sla_s_rsbench.npy

################################ RUN SLA for medium 
# cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla_m
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 200 -ntask 1 -perfmodel 0 -optimization GPTune -dsize m 
mv gptune.db/rsbench.json ./TLA_experiments/SLA-GPTune-m-200/
mv save_results.npy save_results_sla_m_rsbench.npy

################################ RUN SLA for large 
# cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla_l
rm -rf gptune.db
mpirun -n 1 python demo_sla.py -nrun 200 -ntask 1 -perfmodel 0 -optimization GPTune -dsize l
mv gptune.db/rsbench.json ./TLA_experiments/SLA-GPTune-l-200/
mv save_results.npy save_results_sla_l_rsbench.npy

################################# RUN DTLA on sm 
# cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla_sm
rm -rf gptune.db
python merge.py
mkdir -p gptune.db
mv db.out gptune.db/rsbench.json
mpirun -n 1 python demo_dtla.py -nrun 200 -ntask 4 -perfmodel 0 -optimization GPTune -dsize sm
mv gptune.db/rsbench.json ./TLA_experiments/DTLA-GPTune-sm-200/
mv save_results.npy save_results_dtla_sm_rsbench.npy

################################# RUN DTLA on ml
# cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla_sm
rm -rf gptune.db
python merge.py
mkdir -p gptune.db
mv db.out gptune.db/rsbench.json
mpirun -n 1 python demo_dtla.py -nrun 200 -ntask 4 -perfmodel 0 -optimization GPTune -dsize ml
mv gptune.db/rsbench.json ./TLA_experiments/DTLA-GPTune-ml-200/
mv save_results.npy save_results_dtla_ml_rsbench.npy

################################# RUN DTLA on xl 
# cd /gpfs/jlse-fs0/users/jkoo/code/gptune/examples/RSBench_exp/rsbench_gptune_dtla_sm
rm -rf gptune.db
python merge.py
mkdir -p gptune.db
mv db.out gptune.db/rsbench.json
mpirun -n 1 python demo_dtla.py -nrun 200 -ntask 4 -perfmodel 0 -optimization GPTune -dsize xl
mv gptune.db/rsbench.json ./TLA_experiments/DTLA-GPTune-xl-200/
mv save_results.npy save_results_dtla_xl_rsbench.npy

















