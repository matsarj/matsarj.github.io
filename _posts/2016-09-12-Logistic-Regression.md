---
layout: post
mainpic: "/blog/LogisticRegression/logistic_regression.png"
name: "Logistic Regression"
excerpt: "In this post I am going to investigate the machine learning algorithm known as logistic regression. Despite the name, this is actually a classification method."
---
In this post I am going to investigate the machine learning algorithm known as logistic regression. Despite the name, this is actually a classification method. In other words, we are using our features $$X$$ to predict a categorical response variable $$y$$, which represents qualitative data: yes/no, good/bad, small/medium/large, etc. For simplicity, we are going to assume that $$y$$ may take on just two values, $$0$$ and $$1$$. We will discuss the more general question of what happens when there are $$3$$ or more categories involved at the end of the post.

Given a new data point $$X = (x_1, x_2, ..., x_n)$$, we want to determine whether to assign it the value $$1$$ or $$0$$. Instead of trying to determine the function $$ y = f(X) $$ directly, logistic regression attempts to approximate $$ p(y=1 \vert X) $$, the conditional probability that $$y$$ is $$1$$ given that $$X$$ take on the values $$(x_1, x_2, ..., x_n)$$. Then we may assign this data point the value of $$1$$ if we estimate a probability higher than $$.5$$, and the value $$0$$ otherwise. A benefit in using this probability function, rather than $$f(X)$$ directly, is that it takes its values on an interval, and thus we may apply calculus methods. 

A first thought may be to approximate $$p(y = 1 \vert X)$$ by a line, but there is an obvious issue with this: any non-horizontal line (and note that a horizontal line would not be a useful approximation) takes values from negative infinity to infinity, while we know that $$ p(y = 1 \vert X) $$ should only take values from 0 to 1. 

To fix this, suppose our approximation to $$ p(y=1 \vert X) $$, let's call it $$ q(X) $$, takes its values in the open interval $$(0, 1)$$. The function $$\frac{x}{1-x}$$ takes this interval to the positive real numbers $$(0, \infty)$$, and the natural logarithm $$\text{ln}(x)$$ takes the positive reals to the entire real line $$(-\infty, \infty)$$. Thus applying these functions in succession takes the open interval $$(0, 1)$$ to $$(-\infty, \infty)$$. This composition, $$ \text{ln}( \frac{x}{1 - x}) $$, is called the $$\textbf{logit}$$ function. The graph of the logit function looks like this: 

<img src = '/blog/LogisticRegression/logit_function.png' style = "background:white; border: 2px solid black; width:50%; height:auto;"/>

Our complaint about $$ q(X) $$ not being a good candidate for linear regression is no longer true after applying the logistic function. The key idea 
