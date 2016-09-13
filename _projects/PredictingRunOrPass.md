---
layout: post
title: "Predicting Run or Pass on Second Down"
icon: "/projects/PredictingRunOrPass/football.jpg"
mainpic: "/projects/PredictingRunOrPass/RunOrPass.jpg"
name: "1_PredictingRunOrPass"
excerpt: "The purpose of this project is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset."
---

The purpose of this project is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset. <a href = "https://github.com/matsarj/matsarj.github.io/blob/master/projects/PredictingRunOrPass/PredictingRunOrPass.html"> Here</a> is a link to the relevant jupyter notebook.

Before applying any sophisticated techniques, we considered a couple of basic prediction strategies. One such strategy is to simply always choose pass, since teams choose to pass on second down 58% of the time. On the other hand, if it is second and short, teams tend to run more than pass, as the following graphic shows.

<img src = '/projects/PredictingRunOrPass/pies.png' style = "background:white; border: 2px solid black; width:85%; height:auto;"/>

This suggests that we could get a decent prediction by choosing run when it is second down with five yards or fewer to go, and pass otherwise. Indeed, this results in a 62.6% accuracy when tested against our dataset. Our goal is to try to beat these simple predictions using machine learning techniques.

The first step is to prepare our data. We are going to limit ourselves to two features so that we can better visualize our predictions by plotting them on the plane. We can use the sklearn feature_selection module to choose the two best statistics for predicting pass or run. 

<img src = '/projects/PredictingRunOrPass/Feature_Selection.png' style = "background:white; border: 2px solid black; width:50%; height:auto;"/>

Based on these results, we choose the number of yards to go for a first down, as well as score differential, as the two features we will be using for our predictions. We can now plot all of the points in the data set, with pass plays colored blue, and run plays colored red.

<img src = '/projects/PredictingRunOrPass/second_downs.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>

The next step is to normalize our data, and split it into training and testing subsets. Again, sklearn will do this easily, using the preprocessing module to normalize the data and the crossvalidation module to split the data up. Here is a picture of the normalized testing subset, along with a visualization of our naive prediction on this subset.

<img src = '/projects/PredictingRunOrPass/normalized.png' style = "background:white; border: 2px solid black; width:70%; height:auto;"/>
