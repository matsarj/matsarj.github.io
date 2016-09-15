---
layout: post
title: "Predicting Run or Pass on Second Down"
icon: "/projects/PredictingRunOrPass/football.jpg"
mainpic: "/projects/PredictingRunOrPass/RunOrPass.jpg"
name: "1_PredictingRunOrPass"
excerpt: "The purpose of this project is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset."
---

The purpose of this project is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the <a href = "https://github.com/ryan-maas/project-nfl"> 2015 NFL Play-By-Play dataset </a>. <a href = "/projects/PredictingRunOrPass/PredictingRunOrPass.html"> Here </a> is a link to the relevant jupyter notebook.

Before applying any sophisticated techniques, we consider a couple of basic prediction strategies. One such strategy is to simply always choose pass, since teams choose to pass on second down 58% of the time. On the other hand, if it is second and short, teams tend to run more than pass, as the following graphic shows.

<img src = '/projects/PredictingRunOrPass/pies.png' style = "background:white; border: 2px solid black; width:85%; height:auto;"/>

This suggests that we can get a decent prediction by choosing run when it is second down with five yards or fewer to go, and pass otherwise. Indeed, this results in a 62.6% accuracy when tested against our dataset. Our goal is to try to beat these simple predictions using machine learning techniques.

First we must prepare our data. It is convenient to limit ourselves to two features for our predictions. By doing this, we may easily visualize our results by plotting them in the xy-plane. We use the sklearn method SelectKBest to choose the best two features from our dataset. 

<img src = '/projects/PredictingRunOrPass/Feature_Selection.png' style = "background:white; border: 2px solid black; width:50%; height:auto;"/>

Based on these results, we choose the number of yards to go for a first down, as well as score differential, as the two features we will be using for our predictions. Next we separate our data into two subsets. Namely, we have a training subset consisting of 80% of the data, and a testing subset consisting of the other 20%. Here is a plot the testing data, with run in red and pass in blue. The first plot represents the actual play calls and the second is our naive prediction.

<img src = '/projects/PredictingRunOrPass/second_downs.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

Some of the algorithms we will be using work better with our features normalized and standardized. Normalizing will scale the features so they take values between 0 and 1. Standardizing gives the data a standard normal distribution. Here is a plot of the same data we just showed, with the features normalized and standardized.

<img src = '/projects/PredictingRunOrPass/normalized.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

Now we can start playing with some machine learning algorithms! We'll start with <a href = "/blog/Logistic-Regression">logistic regression</a>. With sklearn it is as simple as running the following code:

<pre class="prettyprint py-html">

logistic = LogisticRegression()
logistic.fit(X_train, y_train)

logistic_prediction = logistic.predict(X_test)
</pre>

We write a function graphPredict to graph the prediction and give the accuracy. Plugging in our logistic regression model results in the following graph:

<img src = '/projects/PredictingRunOrPass/logistic.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

This results in a 63.6% accuracy on our testing set. We also run the cross_val_score function to find the accuracy on 5 different test/training splits, which when averaged together still results in a 63.6% accuracy. So the prediction obtained by logistic regression seems to be slightly better than the naive prediction.

We run the same procedure using other common classification algorithms, including: <a href = "/blog/k-NN">k-Nearest Neighbors</a>, <a href = "/blog/Support-Vector-Machines">Support Vector Machines</a>, <a href = "/blog/Decision-Trees">Decision Trees</a>, and <a href = "/blog/Random-Forests">Random Forests</a>. Here are the resulting graphs and accuracies of these algorithms.

<h2 style = "color: black; text-decoration: Underline;">61-Nearest Neighbors</h2>

<img src = '/projects/PredictingRunOrPass/support_vector_machine.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

<p style = "font-weight: bold;"> Accuracy on testing set: 64.8% <br> Average score on 5 splits: 64.9% </p>

<h2 style = "color: black; text-decoration: Underline;">Support Vector Machine</h2>

<img src = '/projects/PredictingRunOrPass/support_vector_machine.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

<p style = "font-weight: bold;"> Accuracy on testing set: 63.9% <br> Average score on 5 splits: 64.0% </p>

<h2 style = "color: black; text-decoration: Underline;">Decision Trees</h2>

<img src = '/projects/PredictingRunOrPass/support_vector_machine.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

<p style = "font-weight: bold;"> Accuracy on testing set: 56.1% <br> Average score on 5 splits: 57.5% </p>

<h2 style = "color: black; text-decoration: Underline;">Random Forests with 100 Estimators</h2>

<img src = '/projects/PredictingRunOrPass/support_vector_machine.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

<p style = "font-weight: bold;"> Accuracy on testing set: 61.6% <br> Average score on 5 splits: 62.5% </p>

In conclusion, many of these results give us better results than the naive strategy. The next step is to choose our parameters more carefully. For instance, how many neighbors would give the best result for k-NN? How many estimators should we use for random forests? Should we use a linear or polynomial (and what degree?) kernel for our support vector machine? We will tackle these issues in another post. Our new goal is to come up with a strategy which predicts correctly 70% of the time.
