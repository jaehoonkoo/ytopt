#! /usr/bin/env bash
source activate ytune
cd /gpfs/jlse-fs0/users/jkoo/code/kde/Benchmarks/lu_exp/lu_h
python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner DUMMY --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rs_h_lu.csv
python -m ytopt.search.ambs --evaluator ray --problem problem_all.Problem --max-evals=200 --learner RF --set-KAPPA 1.96 --acq-func gp_hedge --set-SEED 2468
mv results.csv results_rf_h_lu.csv