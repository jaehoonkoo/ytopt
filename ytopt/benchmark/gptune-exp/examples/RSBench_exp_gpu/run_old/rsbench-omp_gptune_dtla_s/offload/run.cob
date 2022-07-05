#!/bin/bash

module load ibm-wml-ce
conda activate ytune
python3 -m ytopt.search.ambs --evaluator ray --problem problem.Problem --max-evals=5 --learner RF
conda deactivate
