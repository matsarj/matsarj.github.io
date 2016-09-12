---
layout: post
title: "Predicting Run or Pass on Second Down"
icon: "http://i.imgur.com/cqbK361.jpg"
name: "PredictingRunOrPass"
excerpt: "The purpose of this notebook is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset."
---
<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>

The purpose of this notebook is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset.

<pre class="prettyprint py-html">

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
%matplotlib inline 

from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import cross_validation

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

from sklearn.grid_search import GridSearchCV

</pre>
