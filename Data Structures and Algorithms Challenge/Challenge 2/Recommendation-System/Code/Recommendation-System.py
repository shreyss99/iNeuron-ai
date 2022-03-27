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