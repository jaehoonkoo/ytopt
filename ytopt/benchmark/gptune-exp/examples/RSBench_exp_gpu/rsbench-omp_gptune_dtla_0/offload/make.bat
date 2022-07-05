module load xl
xlc_r -std=gnu99 -Wall -qsmp=omp -qoffload -O2  main.c material.c utils.c -o rsbench -lm
