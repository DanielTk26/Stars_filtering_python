# -*- coding: utf-8 -*-
"""p134.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aAo7Y0HCNRavdGDH-bM0tQsMPRHJwSUa
"""

from google.colab import files
data_to_load = files.upload()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

df = pd.read_csv("stars.csv")
df.head()

bools = []
for d in df.Distance:
    if d<=100:
        bools.append(True)
    else:
        bools.append(False)

is_dist = pd.Series(bools)
is_dist.head()

star_dist=df[is_dist]
star_dist.reset_index(inplace=True,drop=True)
star_dist.head()

star_dist.shape

gravity_bool = []
for g in star_dist.Gravity:
    if g<=350 and g>=150:
        gravity_bool.append(True)
    else :
        gravity_bool.append(False)

is_gravity = pd.Series(gravity_bool)
final_stars = star_dist[is_gravity]
final_stars.head()

final_stars.shape

final_stars.reset_index(inplace=True,drop=True)
final_stars.head()

final_stars.to_csv("stars_edited.csv")