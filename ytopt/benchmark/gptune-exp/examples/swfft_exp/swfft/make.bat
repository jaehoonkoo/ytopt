# fftw
module load cray-libsci
module load cray-fftw

cc -g -O2 -fopenmp -Wall -Wno-deprecated -std=gnu99 -DDFFT_TIMING=0 -I/opt/cray/pe/fftw/3.3.8.6/mic_knl/include -c -o distribution.o distribution.c  
CC -g -O2 -fopenmp -Wall -DDFFT_TIMING=0 -o TestDfft TestDfft.cpp distribution.o -fopenmp -I/opt/cray/pe/fftw/3.3.8.6/mic_knl/include -L/opt/cray/pe/fftw/3.3.8.6/mic_knl/lib -lfftw3_omp -lfftw3 -lm
