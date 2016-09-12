---
layout: post
title: "Predicting Run or Pass on Second Down"
icon: "http://i.imgur.com/cqbK361.jpg"
name: "PredictingRunOrPass"
---
<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>

The purpose of this notebook is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset.

<pre class="prettyprint py-html">
# First Let's import the necessary packages
import pandas as pd # Package used for working with dataframes
import numpy as np # Package used for working with arrays
import matplotlib.pyplot as plt #Package used visualizing our data
%matplotlib inline 
#This command causes plots to show up in notebook

#sklearn is the machine learning package
#First we load in the instances to preprocess our data
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import cross_validation

#Next we load the various algorithms we will be using:
#logistic regression, k-nearest neighbors, support vector machines, random trees and random forests
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

#Finally, the gridsearch instance will allow us to fine-tune our algorithms
from sklearn.grid_search import GridSearchCV

</pre>
