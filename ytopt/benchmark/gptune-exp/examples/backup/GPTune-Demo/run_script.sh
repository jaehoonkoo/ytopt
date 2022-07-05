rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 30 -tvalue 0.6 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.6-30/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.6-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 40 -tvalue 0.6 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.6-40/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.6-40/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 50 -tvalue 0.6 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.6-50/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.6-50/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 10 -tvalue 0.8 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.8-10/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.8-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 20 -tvalue 0.8 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.8-20/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.8-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 30 -tvalue 0.8 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.8-30/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.8-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 40 -tvalue 0.8 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.8-40/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.8-40/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 50 -tvalue 0.8 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-0.8-50/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-0.8-50/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 10 -tvalue 1.0 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.0-10/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.0-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 20 -tvalue 1.0 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.0-20/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.0-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 30 -tvalue 1.0 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.0-30/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.0-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 40 -tvalue 1.0 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.0-40/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.0-40/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 50 -tvalue 1.0 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.0-50/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.0-50/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 10 -tvalue 1.2 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.2-10/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.2-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 20 -tvalue 1.2 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.2-20/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.2-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 30 -tvalue 1.2 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.2-30/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.2-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 40 -tvalue 1.2 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.2-40/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.2-40/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 50 -tvalue 1.2 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.2-50/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.2-50/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 10 -tvalue 1.4 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.4-10/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.4-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 20 -tvalue 1.4 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.4-20/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.4-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 30 -tvalue 1.4 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.4-30/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.4-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 40 -tvalue 1.4 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.4-40/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.4-40/a.out.log
rm -rf gptune.db
rm -rf a.out.log
mpirun -n 1 python ./demo.py -ntask 1 -nrun 50 -tvalue 1.4 -optimization GPTune | tee a.out.log
mv gptune.db/GPTune-Demo.json TLA_experiments/SLA-GPTune-1.4-50/GPTune-Demo.json
mv a.out.log TLA_experiments/SLA-GPTune-1.4-50/a.out.log
