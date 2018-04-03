Experimental scripts and log files for the CAV 2018 accepted paper on Tangle Learning.

Quick start
===========
* Obtain and compile Oink
* Use download.sh to download and extract the benchmarks by Keiren
* Run Oink manually or use the benchmark scripts

Generating random games
=======================
* Use generate.py to generate the random games (needs "rngame" and "stgame" in tools/)

Compiling Oink
==============
* sources: https://www.github.com/trolando/oink
* requires CMake
* use "Release" build type in CMake (default)
* `cd oink`
* `mkdir build`
* `cd build`
* `cmake .. -DBUILD_EXTRA_TOOLS=1 ..`
* `make`
* then copy the `oink` executable into the `tools` directory

To run the experiments
======================
* in terminal: ./exp.py run 1
* with slurm: sbatch slurm.sh

To obtain the results to csv
============================
* just the finished experiments:./exp.py csv > results.csv
* with PAR2 score (penalize timeouts x2): ./exp.py csvpar2 > par2.csv

Running Oink on a single file
=============================
* `tools/oink --help`
* `tools/oink -v <filename> --<solver>`
* `tools/oink -v <filename> --otfatl`

Remarks
=======
* Log files used for the paper: logs.tar
* The csv files used for the paper: results.csv, par2.csv, tangles.csv
* Small random games used for the paper: random1 subdirectory
* Large random games used for the paper: random2 subdirectory
* Benchmark scripts: expfw.py, exp.py, slurm.sh
* Obtaining benchmark scripts: download.sh, generate.py
