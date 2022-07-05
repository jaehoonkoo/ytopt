import os
import sys
import subprocess
import random

class Plopper:
    def __init__(self,sourcefile,outputdir):

        # Initilizing global variables
        self.sourcefile = sourcefile
        self.outputdir = outputdir+"/tmp_files"

        if not os.path.exists(self.outputdir):
            os.makedirs(self.outputdir)


    #Creating a dictionary using parameter label and value
    def createDict(self, x, params):
        dictVal = {}
        for p, v in zip(params, x):
            dictVal[p] = v
        return(dictVal)

    #Replace the Markers in the source file with the corresponding Pragma values
    def plotValues(self, dictVal, inputfile, outputfile):
        with open(inputfile, "r") as f1:
            buf = f1.readlines()

        with open(outputfile, "w") as f2:
            for line in buf:
                modify_line = line
                for key, value in dictVal.items():
                    if key in modify_line:
                        if value != 'None': #For empty string options
                            modify_line = modify_line.replace('#'+key, str(value))

                if modify_line != line:
                    f2.write(modify_line)
                else:
                    #To avoid writing the Marker
                    f2.write(line)


    # Function to find the execution time of the interim file, and return the execution time as cost to the search module
    def findRuntime(self, x, params, d_size):
        interimfile = ""
        #exetime = float('inf')
        #exetime = sys.maxsize
        exetime = 1
        counter = random.randint(1, 10001) # To reduce collision increasing the sampling intervals

        interimfile = self.outputdir+"/"+str(counter)+".c"
#         interimfile = self.outputdir+"/void_1.c"

        # Generate intermediate file
        dictVal = self.createDict(x, params)
        self.plotValues(dictVal, self.sourcefile, interimfile)

        #compile and find the execution time
        tmpbinary = interimfile[:-2]

        kernel_idx = self.sourcefile.rfind('/')
        kernel_dir = self.sourcefile[:kernel_idx]

        cmd1 = "clang "  +interimfile +" " + kernel_dir + "/material.c " \
                + kernel_dir + "/utils.c " + " -I" + kernel_dir + \
                " -fopenmp -DOPENMP -fno-unroll-loops -O3 -mllvm -polly -mllvm -polly-process-unprofitable -mllvm -polly-use-llvm-names -ffast-math -march=native -o "+tmpbinary + " -lm" + " -I/lcrc/project/EE-ECP/jkoo/sw/clang13.2/llvm-project/release_pragma-clang-loop/projects/openmp/runtime/src"
        print (cmd1)
#         cmd2 = kernel_dir + "/exe.pl " +  tmpbinary
        cmd2 = 'srun -n 1 ' + tmpbinary + str(d_size)
        print (cmd2)
        #Find the compilation status using subprocess
        compilation_status = subprocess.run(cmd1, shell=True, stderr=subprocess.PIPE)

        #Find the execution time only when the compilation return code is zero, else return infinity
        if compilation_status.returncode == 0 :
        #and len(compilation_status.stderr) == 0: #Second condition is to check for warnings
            execution_status = subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE)
            exetime_run = execution_status.stdout.decode('utf-8').split('\n')[-3:]
            exetime_run = [float(s) for s in exetime_run] 
            print ('........................................',exetime_run)
            exetime = exetime_run
            if exetime == 0:
                exetime = 1
        else:
            print(compilation_status.stderr)
            print("compile failed")
        return exetime, cmd2, str(counter) #return execution time as cost
