# 1999 AMC 8 Problem 2

## Problem

What is the degree measure of the smaller angle formed by the hands of a clock at 10 o'clock?

[asy] draw(circle((0,0),2)); dot((0,0)); for(int i = 0; i < 12; ++i) { dot(2*dir(30*i)); } label("$3$",2*dir(0),W); label("$2$",2*dir(30),WSW); label("$1$",2*dir(60),SSW); label("$12$",2*dir(90),S); label("$11$",2*dir(120),SSE); label("$10$",2*dir(150),ESE); label("$9$",2*dir(180),E); label("$8$",2*dir(210),ENE); label("$7$",2*dir(240),NNE); label("$6$",2*dir(270),N); label("$5$",2*dir(300),NNW); label("$4$",2*dir(330),WNW); [/asy]

$\textbf{(A)}\ 30 \qquad \textbf{(B)}\ 45 \qquad \textbf{(C)}\ 60 \qquad \textbf{(D)}\ 75 \qquad \textbf{(E)}\ 90$

## Solution 1
At $10:00$ , the hour hand will be on the $10$ while the minute hand on the $12$ .
This makes them $\frac{1}{6}$ th of a circle apart, and $\frac{1}{6}\cdot360^{\circ}=\boxed{\textbf{(C) } 60}$ .

## Solution 2
We know that the full clock is a circle, and therefore has 360 degrees. Considering that there are $12$ numbers, the distance between one number will be $360\div 12=30$ . If the time is $10:00$ , then the hour hand will be on $10$ , and the minute hand will be on, $12$ , making them $2$ numbers apart, so they will be $60$ degrees apart, or $\boxed{\textbf{(C) } 60}$
### Video(By YippieMath)
https://www.youtube.com/watch?v=qop08mDP6HY
### See Also