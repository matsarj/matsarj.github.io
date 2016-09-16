---
layout: post
mainpic: "/blog/LogisticRegression/logistic_regression.png"
name: "Logistic Regression"
excerpt: "In this post I am going to investigate the machine learning algorithm known as logistic regression. Despite the name, this is actually a classification method."
---
In this post I am going to investigate the machine learning algorithm known as logistic regression. Despite the name, this is actually a classification method. In other words, we are using our features $$X$$ to predict a categorical variable $$y$$. In this post, we are going to assume that $$y$$ may take on just two values, 0 and 1. We will consider the more general question of what happens when there are 3 or more categories involved in a different post.

Instead of trying to immediately estimate the function $$ y = f(X) $$ which takes the values 0 and 1, it will be easier to approximate the probability function $$ p(y \vert X) $$. Then we may assign $$y$$ the value of 1 if we estimate a probability higher than .5, and the value 0 otherwise. One might attempt to approximate this probability function using linear regression, but there are a couple of obvious issues.

$$

\begin{itemize}
\item Issue 1
\item Issue 2

$$
