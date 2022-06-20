# -*- coding: utf-8 -*-
"""Data Visualization with Seaborn - Skeleton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TQQOq4A28zjTRGUpyX15a98U2YRytO8d

# 1. SEABORN SCATTERPLOT & COUNTPLOT
"""

# Seaborn is a visualization library that sits on top of matplotlib
# Seaborn offers enhanced features compared to matplotlib
# https://seaborn.pydata.org/examples/index.html

# import libraries 
import pandas as pd # Import Pandas for data manipulation using dataframes
import numpy as np # Import Numpy for data statistical analysis 
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import seaborn as sns # Statistical data visualization

# Import Cancer data 

cancer_df = pd.read_csv('cancer.csv')
cancer_df

# Check out the head of the dataframe
cancer_df.head()

# Check out the tail of the dataframe
cancer_df.tail()

# Plot scatter plot between mean area and mean smoothness
sns.scatterplot(x = 'mean area', y = 'mean smoothness', data = cancer_df, hue = 'target',)

# Let's print out countplot to know how many samples belong to class #0 and #1
sns.countplot(cancer_df['target'], label = 'counts')

"""**MINI CHALLENGE #1:**
- **Plot the scatterplot between the mean radius and mean area. Comment on the plot** 

"""

cancer_df = pd.read_csv('cancer.csv')
cancer_df

sns.scatterplot(x = 'mean radius', y = 'mean area', data = cancer_df, hue = 'target')
# As you can see here that as the mean radius increases mean area increases
# Not only this but no. of #0(non-cancer) is more than the #1(cancer)

"""# 2. SEABORN PAIRPLOT, DISPLOT, AND HEATMAPS/CORRELATIONS"""

# Plot the pairplot
sns.pairplot(cancer_df, hue = 'target', vars = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness'])

sns.heatmap(cancer_df.corr())

# Strong correlation between the mean radius and mean perimeter, mean area and mean primeter
plt.figure(figsize = (20, 15))
sns.heatmap(cancer_df.corr(), annot = True)

# plot the distplot 
# Displot combines matplotlib histogram function with kdeplot() (Kernel density estimate)
# KDE is used to plot the Probability Density of a continuous variable. 

sns.distplot(cancer_df['mean area'], bins = 5)

"""**MINI CHALLENGE #2:**
- **Plot two separate distplot for each target class #0 and target class #1**

"""

cancer_df = pd.read_csv('cancer.csv')
cancer_df

class_0_df = cancer_df[ cancer_df['target'] == 0 ]
class_0_df

class_1_df = cancer_df[ cancer_df['target'] == 1 ]
class_1_df

plt.figure(figsize = (12, 6))
sns.distplot(class_0_df['mean area'], bins = 25, color = 'blue')
sns.distplot(class_1_df['mean area'], bins = 25, color = 'red')