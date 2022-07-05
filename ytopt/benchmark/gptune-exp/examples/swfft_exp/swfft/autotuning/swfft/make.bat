# fftw
module load cray-libsci
module load cray-fftw

CC -g -O2 -fopenmp -Wall -Wno-deprecated -std=gnu99 -DDFFT_TIMING=0 -o TestDfft TestDfft.cpp distribution.c -I/opt/cray/pe/fftw/3.3.8.6/mic_knl/include -L/opt/cray/pe/fftw/3.3.8.6/mic_knl/lib -lfftw3_omp -lfftw3 -lm
