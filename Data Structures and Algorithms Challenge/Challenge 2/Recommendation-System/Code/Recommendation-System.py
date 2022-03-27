# Implementing libraries

import pandas as pd
import numpy as np
import math
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Import compressed sparse matrix library for computation 
from scipy.sparse import csr_matrix
# Importing SVD from surprise library for building recommender systems
# SVD is Singular Value Decompostion
from surprise import Reader, Dataset, SVD

df1 = pd.read_csv('dataset.txt', header = None, names = ['Cust_Id', 'Rating', 'Date'], usecols = [0,1,2])
df1['Rating'] = df1['Rating'].astype(float)

# Rename dataset and get indexes
data = df1
data.index = np.arange(0,len(df))