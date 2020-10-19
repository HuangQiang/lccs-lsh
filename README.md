# LCCS-LSH

Locality-Sensitive Hashing Scheme based on Longest Circular Co-Substring

Paper accepted by SIGMOD 2020
**Locality-Sensitive Hashing Scheme based on Longest Circular Co-Substring. SIGMOD Conference 2020, Yifan Lei, Qiang Huang, Mohan S. Kankanhalli, Anthony K. H. Tung**

To build the project, use the following instructions:

Step 1: build lib for lshkit and get `lshkit-0.2.1/build/lib/liblshkit.a`:

```bash
cd lshkit-0.2.1/build
cmake ..
make -j
```

Step 2: build lib for SRS and get `SRS/libsrs.a`:

```bash
cd SRS
make libsrs.a
```

Step 3: build lib for QALSH and get `QALSH_Mem/libqalsh.a`:

```bash
cd QALSH_Mem
make libqalsh.a
```

Step 4: combine together and build LCCS-LSH

```bash
mkdir build
cd build
cmake ..
make -j
```

This will output the lccs binary. You can use

```bash
./lccs -h
```

for simple help information.

In order to make the program, you may need a compiler supporting c++17 and the program has the following additional dependencies:

**Boost** and **GSL** (required by lshkit)

for example, for ubuntu users, you should install GSL, Boost, and its program_options before the four steps above:

```bash
sudo apt-get install libboost-dev
sudo apt-get install libboost-program-options-dev
sudo apt-get install libgsl-dev
```

Other dependencies should be already included in this repository.

We provide the Mnist dataset as a simple example. To run the LCCS-LSH algorithm on the Mnist data, you can simply run the following instructions in the build folder (python 3+ required):

```python
python ../scripts/run_simple_experiment.py
```

This will work like a shell scirpt and invode the program using command line.

To run more experiments, you may need to prepare the datasets in the data folder properly like the Mnist dataset.
Once the datasets are properly prepared, you can simply run (in the build folder as well)

```python
python ../scripts/run_ground_truth.py
python ../scripts/run_time_recall.py
```

The plot scripts can be found in ./scripts/lccs_plot. You can run the plot_sigmod.py to reproduce the figures shown in the paper.

In order to run the scripts, you may need numpy, scipy and matplotlib.
The scripts will automatically use the latest result indicated by the timestamp in the result file name.

The datasets can be found in https://1drv.ms/u/s!Ascf3jEjrVdxg6c6w7CutkF0TpXgpA?e=fjnR80.