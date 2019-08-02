#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=run.sh
#SBATCH --mem=16GB
#SBATCH --output=./slu_%j.out
/usr/local/bin/matlab script_group_collect.m
