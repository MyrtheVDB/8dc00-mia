# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:36:11 2019

@author: 20161879
"""

import sys
sys.path.append("../code")
import numpy as np
import matplotlib.pyplot as plt
import registration as reg
import registration_util as util

X = util.test_object(1)
X_scaled = reg.scale(2, 3).dot(X)

fig = plt.figure(figsize=(5,5))
ax1  = fig.add_subplot(111)
ax1.grid()
util.plot_object(ax1, X)
util.plot_object(ax1, X_scaled)