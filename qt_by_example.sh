#!/bin/bash

# Run python in a conda environment
# Print Hello message
echo "Run .... with python in a conda environment"

# Activate conda environment
source /home/russ/anaconda3/etc/profile.d/conda.sh
conda activate py_12_misc

# Navigate to the directory with main.py
cd //mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example 

# Run the Python program
python main.py

# Deactivate the conda environment
conda deactivate

# here just wait for a keystroke ( or comment out )
read RESPONSE


