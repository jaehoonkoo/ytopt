# THIS BRANCH is UNDER CONSTRUCTION!! 

<p align="center">
<img src="docs/_static/logo/medium.png">
</p>

<!-- [![Documentation Status](https://readthedocs.org/projects/ytopt/badge/?version=latest)](https://ytopt.readthedocs.io/en/latest/?badge=latest)-->

# What is ytopt?
``ytopt`` is a machine-learning-based search software package that consists of sampling a small number of input parameter configurations, evaluating them, and progressively fitting a surrogate model over the input-output space until exhausting the user-defined time or the maximum number of evaluations. The package is built based on Bayesian Optimization that solves any optimization problem and is especially useful when the objective function is difficult to evaluate. It provides an interface that deals with unconstrained and constrained problems. The software is designed to operate in the manager-worker computational paradigm, where one manager node fits the surrogate model and generates promising input configurations and worker nodes perform the computationally expensive evaluations and return the outputs to the manager node. The asynchronous aspect of the search allows the search to avoid waiting for all the evaluation results before proceeding to the next iteration. As soon as an evaluation is finished, the data is used to retrain the surrogate model, which is then used to bias the search toward the promising configurations. 

<!--
``ytopt`` is a machine-learning-based search software package that consists of sampling a small number of input parameter configurations,
evaluating them, and progressively fitting a surrogate model over the input-output space until exhausting the user-defined time or maximum number of 
evaluations. The package provides two different class of methods: Bayesian Optimization and Reinforcement Learning.
The software is designed to operate in the manager-worker computational paradigm, where one manager node fits 
the surrogate model and generates promising input configurations and worker nodes perform the computationally expensive evaluations and 
return the outputs to the manager node.
The asynchronous aspect of the search allows the search to avoid waiting for all the evaluation results before proceeding to the next iteration. As 
soon as an evaluation is finished, the data is used to retrain the surrogate model, which is then used to bias the search toward the promising configurations. -->
# Directory structure
```
docs/	
    Sphinx documentation files
test/
    scipts for running benchmark problems in the problems directory
ytopt/	
    scripts that contain the search implementations  
ytopt/benchmark/	
    a set of problems the user can use to compare our different search algorithms or as examples to build their own problems
```

# Install instructions
The autotuning framework requires the following components: ConfigSpace, CConfigSpace (optional), scikit-optimize, autotune, and ytopt.

* We recommend creating isolated Python environments on your local machine using [conda](https://docs.conda.io/projects/conda/en/latest/index.html), for example:

```
conda create --name ytune python=3.7
conda activate ytune
```

* Create a directory for ytopt tutorial as follows:
```
mkdir ytopt
cd ytopt
```

* Install [ConfigSpace](https://github.com/ytopt-team/ConfigSpace.git):
```
git clone https://github.com/ytopt-team/ConfigSpace.git
cd ConfigSpace
pip install -e .
cd ..
```

* Install [scikit-optimize](https://github.com/ytopt-team/scikit-optimize.git):
```
git clone https://github.com/ytopt-team/scikit-optimize.git
cd scikit-optimize
pip install -e .
cd ..
```

* Install [autotune](https://github.com/ytopt-team/autotune.git):
```
git clone -b version1 https://github.com/ytopt-team/autotune.git
cd autotune
pip install -e . 
cd ..
```

* Install [ytopt](https://github.com/ytopt-team/ytopt.git):
```
git clone -b main https://github.com/ytopt-team/ytopt.git
cd ytopt
pip install -e .
```

* If you encounter installtion error, install psutil, setproctitle, mpich, mpi4py first as follows:
```
conda install -c conda-forge psutil
conda install -c conda-forge setproctitle
conda install -c conda-forge mpich
conda install -c conda-forge mpi4py
pip install -e .
```

* [Optinal] Install [CConfigSpace](https://github.com/argonne-lcf/CCS.git):
    * Prerequisites: `autotools` and the `gsl`
        * Ubuntu
          ```
          sudo apt-get install autoconf automake libtool libgsl-dev
          ```

        * MacOS
          ```
          brew install autoconf automake libtool gsl
          ```
    * Build and Install the library and python bindings:
      the `configure` command can take an optional `--prefix=` parameter to specify a
      different install path than the default one (`/usr/local`). Depending on the
      chosen location you may need elevated previleges to run `make install`.
      ```
      git clone git@github.com:argonne-lcf/CCS.git
      cd CCS
      ./autogen.sh
      mkdir build
      cd build
      ../configure
      make
      make install
      cd ../bindings/python
      pip install parglare==0.12.0
      pip install -e .
      ```
    * Setup environment:
      in order for the python binding to find the CConfigSpace library, the path to
      the library install location (`/usr/local/lib` by default) must be appended
      to the `LD_LIBRARY_PATH` environment variable on Linux, while on MacOS the
      `DYLD_LIBRARY_PATH` environment variable serves the same purpose. Alternatively
      the `LIBCCONFIGSPACE_SO_` environment variable can be made to point to the installed
      `libcconfigspace.so` file on Linux or to the installed `libcconfigspace.dylib`
      on MacOS. 

# Tutorials

## Static search space 

* [Autotuning the block matrix multiplication](https://github.com/ytopt-team/ytopt/tree/tutorial/docs/tutorials/mmm-block/tutorial-mmm-block.md)
* [Autotuning the OpenMP version of XSBench](https://github.com/ytopt-team/ytopt/tree/tutorial/docs/tutorials/omp-xsbench/tutorial-omp-xsbench.md)
* [Autotuning the OpenMP version of XSBench with constraints](https://github.com/ytopt-team/ytopt/tree/tutorial/docs/tutorials/omp-xsbench/tutorial-omp-xsbench-const.md)
* [Autotuning the hybrid MPI/OpenMP version of XSBench](https://github.com/ytopt-team/ytopt/tree/tutorial/docs/tutorials/mpi-omp-xsbench/tutorial-mpi-omp-xsbench.md)
* [Autotuning the hybrid MPI/OpenMP version of XSBench with constraints](https://github.com/ytopt-team/ytopt/tree/tutorial/docs/tutorials/mpi-omp-xsbench/tutorial-mpi-omp-xsbench-const.md)
* [Autotuning the OpenMP version of convolution-2d with constraints](https://github.com/ytopt-team/ytopt/tree/tutorial/docs/tutorials/convolution-2d/tutorial-convolution-2d-const.md)

## Tree search space 
* Check out first [Readme for tree space](https://github.com/ytopt-team/ytopt/blob/mcts/ytopt/search/mcts/README.md)
* [Autotuning tree space version of GEMM](https://github.com/ytopt-team/ytopt/blob/mcts/docs/tutorials/mcts-gemm/tutorial-mcts-gemm.md)

<!--# How do I learn more?

* Documentation: https://ytopt.readthedocs.io 

* GitHub repository: https://github.com/ytopt-team/ytopt -->


# Who is responsible?

The core ``ytopt`` team is at Argonne National Laboratory:

* Prasanna Balaprakash <pbalapra@anl.gov>, Lead and founder
* Romain Egele <regele@anl.gov>
* Paul Hovland <hovland@anl.gov>
* Xingfu Wu <xingfu.wu@anl.gov>
* Jaehoon Koo <jkoo@anl.gov>
* Brice Videau <bvideau@anl.gov>

The convolution-2d tutorial (source and python scripts) is contributed by:
* David Fridlander <davidfrid2@gmail.com>

<!--Modules, patches (code, documentation, etc.) contributed by:

* David Fridlander <davidfrid2@gmail.com>

# How can I participate?

Questions, comments, feature requests, bug reports, etc. can be directed to:

* Our mailing list: *ytopt@groups.io* or https://groups.io/g/ytopt

* Issues on GitHub

Patches are much appreciated on the software itself as well as documentation.
Optionally, please include in your first patch a credit for yourself in the
list above.

The ytopt team uses git-flow to organize the development: [Git-Flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/). For tests we are using: [Pytest](https://docs.pytest.org/en/latest/). -->

# Publications
* J. Koo, P. Balaprakash, M. Kruse, X. Wu, P. Hovland, and M. Hall, "Customized Monte Carlo Tree Search for LLVM/Polly's Composable Loop Optimization Transformations," in Proceedings of 12th IEEE International Workshop on Performance Modeling, Benchmarking and Simulation of High Performance Computer Systems (PMBS21), pages 82–93, 2021. DOI: [DOI 10.1109/PMBS54543.2021.00015](https://scwpub21:conf21%2f%2f@conferences.computer.org/scwpub/pdfs/PMBS2021-vSqRXl4nJSV5KT4jWO5cW/111800a082/111800a082.pdf)
* X. Wu, M. Kruse, P. Balaprakash, H. Finkel, P. Hovland, V. Taylor, and M. Hall, "Autotuning polybench benchmarks64with llvm clang/polly loop optimization pragmas using bayesian optimization (extended version)," Concurrency and Computation. Practice and Experience, vol. 11, 2021. ISSN 1532-0626 DOI: [10.1002/cpe.6683](https://doi.org/10.1002/cpe.6683) 
* X. Wu, M. Kruse, P. Balaprakash, H. Finkel, P. Hovland, V. Taylor, and M. Hall, "Autotuning PolyBench Benchmarks with LLVM Clang/Polly Loop Optimization Pragmas Using Bayesian Optimization," in Proceedings of 11th IEEE International Workshop on Performance Modeling, Benchmarking and Simulation of High Performance Computer Systems (PMBS20), pages 61–70, 2020. DOI: [10.1109/PMBS51919.2020.00012](https://ieeexplore.ieee.org/document/9307884) 
* P. Balaprakash, J. Dongarra, T. Gamblin, M. Hall, J. K. Hollingsworth, B. Norris, and R. Vuduc, "Autotuning in High-Performance Computing Applications," Proceedings of the IEEE, vol. 106, no. 11, 2018. DOI: [10.1109/JPROC.2018.2841200](https://ieeexplore.ieee.org/document/8423171) 
*  T. Nelson, A. Rivera, P. Balaprakash, M. Hall, P. Hovland, E. Jessup, and B. Norris, "Generating efficient tensor contractions for GPUs," in Proceedings of 44th International Conference on Parallel Processing, pages 969–978, 2015. DOI: [10.1109/ICPP.2015.106](https://ieeexplore.ieee.org/document/7349652) 

# Acknowledgements

* YTune: Autotuning Compiler Technology for Cross-Architecture Transformation and Code Generation, U.S. Department of Energy Exascale Computing Project (2017--Present) 
* Scalable Data-Efficient Learning for Scientific Domains, U.S. Department of Energy 2018 Early Career Award funded by the Advanced Scientific Computing Research program within the DOE Office of Science (2018--Present)
* PROTEAS-TUNE, U.S. Department of Energy ASCR Exascale Computing Project (2018--Present)

# Copyright and license

TBD
