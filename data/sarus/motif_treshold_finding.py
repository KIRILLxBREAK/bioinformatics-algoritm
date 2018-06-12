#!/usr/bin/python3

import os
import numpy as np
import sys

# in '/bioinformatics/data/MARA/sarus'
#print(os.getcwd())
motifThresholdPath = '../MARA/HOCOMOCO/HOCOMOCOv9_AD_thresholds_PWM_hg19/' + sys.argv[1] + '_thresholds.txt'
#print(motifThresholdPath)

thresholds = np.genfromtxt(motifThresholdPath)[-1,0]
print(thresholds)
