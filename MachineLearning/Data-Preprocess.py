#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 06:10:48 2017

@author: suniljacob
"""

#Import Library
import numpy as np
np.set_printoptions(threshold=100)
import matplotlib.pyplot as plt
import pandas as pd # import and manage datasets

#Import Dataset and create dependent and independent variables
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values # -1 - > take all the cols except the last one
Y = dataset.iloc[:,3].values 