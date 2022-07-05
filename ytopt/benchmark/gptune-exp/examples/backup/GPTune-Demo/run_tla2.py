rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.6 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-0.8-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-0.8-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-0.8-10/a.out.log

rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.6 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.0-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.0-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.0-10/a.out.log

#####################################################################

rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.6 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.2-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.2-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.2-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.6 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.4-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.4-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.4-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.6 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-0.8-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-0.8-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-0.8-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.6 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.0-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.0-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.0-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.6 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.2-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.2-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.2-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.6 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.4-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.4-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.4-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.6 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-0.8-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-0.8-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-0.8-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.6 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.0-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.0-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.0-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.6 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.2-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.2-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.2-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.6 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.6-1.4-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.6-1.4-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.6-1.4-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.8 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-0.6-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-0.6-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-0.6-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.8 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.0-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.0-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.0-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.8 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.2-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.2-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.2-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 0.8 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.4-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.4-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.4-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.8 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-0.6-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-0.6-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-0.6-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.8 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.0-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.0-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.0-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.8 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.2-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.2-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.2-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 0.8 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.4-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.4-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.4-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.8 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-0.6-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-0.6-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-0.6-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.8 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.0-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.0-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.0-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.8 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.2-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.2-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.2-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 0.8 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-0.8-1.4-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-0.8-1.4-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-0.8-1.4-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.0 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-0.6-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-0.6-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-0.6-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.0 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-0.8-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-0.8-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-0.8-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.0 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-1.2-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-1.2-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-1.2-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.0 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-1.4-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-1.4-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-1.4-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.0 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-0.6-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-0.6-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-0.6-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.0 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-0.8-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-0.8-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-0.8-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.0 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-1.2-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-1.2-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-1.2-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.0 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-1.4-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-1.4-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-1.4-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.0 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-0.6-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-0.6-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-0.6-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.0 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-0.8-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-0.8-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-0.8-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.0 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-1.2-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-1.2-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-1.2-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.0 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.0-1.4-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.0-1.4-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.0-1.4-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.2 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-0.6-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-0.6-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-0.6-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.2 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-0.8-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-0.8-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-0.8-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.2 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-1.0-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-1.0-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-1.0-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.2 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-1.4-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-1.4-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-1.4-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.2 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-0.6-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-0.6-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-0.6-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.2 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-0.8-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-0.8-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-0.8-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.2 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-1.0-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-1.0-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-1.0-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.2 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-1.4-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-1.4-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-1.4-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.2 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-0.6-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-0.6-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-0.6-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.2 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-0.8-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-0.8-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-0.8-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.2 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-1.0-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-1.0-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-1.0-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.4-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.2 -tvalue2 1.4 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.2-1.4-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.2-1.4-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.2-1.4-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.4 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-0.6-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-0.6-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-0.6-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.4 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-0.8-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-0.8-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-0.8-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.4 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-1.0-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-1.0-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-1.0-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 10 -tvalue 1.4 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-1.2-10
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-1.2-10/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-1.2-10/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.4 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-0.6-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-0.6-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-0.6-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.4 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-0.8-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-0.8-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-0.8-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.4 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-1.0-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-1.0-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-1.0-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 20 -tvalue 1.4 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-1.2-20
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-1.2-20/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-1.2-20/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.6-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.4 -tvalue2 0.6 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-0.6-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-0.6-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-0.6-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-0.8-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.4 -tvalue2 0.8 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-0.8-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-0.8-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-0.8-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.0-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.4 -tvalue2 1.0 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-1.0-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-1.0-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-1.0-30/a.out.log
rm -rf gptune.db
rm -rf a.out.log
cp -r TLA_experiments/SLA-GPTune-1.2-50 gptune.db
mpirun -n 1 python ./demo_TLA.py -ntask 2 -nrun 30 -tvalue 1.4 -tvalue2 1.2 -optimization GPTune | tee a.out.log
mkdir -p TLA_experiments/TLA2_task-1.4-1.2-30
mv gptune.db/GPTune-Demo.json TLA_experiments/TLA2_task-1.4-1.2-30/GPTune-Demo.json
mv a.out.log TLA_experiments/TLA2_task-1.4-1.2-30/a.out.log