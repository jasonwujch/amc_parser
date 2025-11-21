# 2017 AMC 10A Problem 15

## Problem

Chloe chooses a real number uniformly at random from the interval $[0, 2017]$ . Independently, Laurent chooses a real number uniformly at random from the interval $[0, 4034]$ . What is the probability that Laurent's number is greater than Chloe's number?

$\textbf{(A) } \frac{1}{2} \qquad \textbf{(B) } \frac{2}{3} \qquad \textbf{(C) } \frac{3}{4} \qquad \textbf{(D) } \frac{5}{6} \qquad \textbf{(E) } \frac{7}{8}$

## Solution 1
We can use geometric probability to solve this. Suppose a point $(x,y)$ lies in the $xy$ -plane. Let $x$ be Chloe's number and $y$ be Laurent's number. Then obviously we want $y>x$ , which basically gives us a region above a line. We know that Chloe's number is in the interval $[0,2017]$ and Laurent's number is in the interval $[0,4034]$ , so we can create a rectangle in the plane, whose length is $2017$ and whose width is $4034$ . Drawing it out and dividing into 4 congruent triangles, we see that Laurent's winning area is 3 triangles and Chloe's is 1 triangle. $\boxed{\textbf{(C)}\ \frac{3}{4}}$ .

## Solution 2
Scale down by $2017$ to get that Chloe picks from $[0,1]$ and Laurent picks from $[0,2]$ . There are an infinite number of cases for the number that Chloe picks, but they are all centered around the average of $0.5$ . Therefore, Laurent has a winning range of $[X, 2]$ , where the average value of $X$ is $0.5$ . Thus the average winning length is $2-0.5=1.5$ out of a total length of $2-0=2$ . Therefore, the probability is $1.5/2=15/20=\boxed{\frac{3}{4} \space \text{(C)}}.$

## Solution 3 (Fakesolve)
In total there are $2018\times4034$ ways in which Laurene and Chloe can choose numbers (as same number cannot be chosen by both). If Chloe chooses 2017, then Lauren has 2017 ways to win. If Chloe chooses 2016, Lauren has 2018 ways to win, and so on until Chloe chooses 0, Lauren has 4034 ways to win. Thus the answer is:
$\frac{\text{number of ways lauren can win}}{\text{number of combinations}}=\frac{2017+2018+2019...+4034}{2018\times4034}$
Using arithmetic series formula:
$\frac{\frac{1}{2}(2018)(2017+4034)}{2018\times4034}=\frac{3}{4}$
$\fbox{C}$ is the correct answer.
~ Lion08 ~Theoneandonlymathman - Grammar mistakes
NOTE: Because the problem says real numbers, not integers, this solution may not always work.

## Solution 4 (Intuitive Casework)
Let Laurene's number \(L \in [0, 4034]\) and Chloé's number \(C \in [0, 2017]\). There is \(\frac{1}{2}\) chance where \(L \in (2017, 4034]\), in which case \(L > C\) regardless of Chloé's number. If \(L \in [0, 2017]\), again by \(\frac{1}{2}\) chance, \(C\) and \(L\) are independently chosen real numbers within the same interval. Then by symmetry, there's equal chance of one being greater than the other; this gives us \(\frac{1}{2} \times \frac{1}{2}\) chance.
The answer is \(\frac{1}{2} + \frac{1}{2} \times \frac{1}{2} = \boxed{\textbf{(C)}\ \frac{3}{4}}\)
~abghim

## Video Solution
A video solution for this can be found here: https://www.youtube.com/watch?v=PQFNwW1XFaQ
https://youtu.be/NB4KXQiqgi0
~savannahsolver

## Video Solution 2
https://www.youtube.com/watch?v=s4vnGlwwHHw&t=840s

## Video Solution
https://youtu.be/IRyWOZQMTV8?t=4163
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .