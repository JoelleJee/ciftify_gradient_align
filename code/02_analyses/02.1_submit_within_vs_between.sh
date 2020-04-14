#!/bin/sh
source ~/.virtualenvs/gradients/bin/activate
qbatch -b slurm -w 00:25:00 qbatch_within_vs_between.txt
