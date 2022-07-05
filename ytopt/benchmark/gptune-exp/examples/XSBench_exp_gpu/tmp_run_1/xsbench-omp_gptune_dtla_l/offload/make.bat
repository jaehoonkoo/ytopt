clang -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda -Xopenmp-target -O3 Main.c XSutils.c Materials.c -o XSBench -lm
 
