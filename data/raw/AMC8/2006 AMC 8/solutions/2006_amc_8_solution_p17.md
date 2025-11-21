# 2006 AMC 8 Problem 17

## Problem

Jeff rotates spinners $P$ , $Q$ and $R$ and adds the resulting numbers. What is the probability that his sum is an odd number?

[asy] size(200); path circle=circle((0,0),2); path r=(0,0)--(0,2); draw(circle,linewidth(1)); draw(shift(5,0)*circle,linewidth(1)); draw(shift(10,0)*circle,linewidth(1)); draw(r,linewidth(1)); draw(rotate(120)*r,linewidth(1)); draw(rotate(240)*r,linewidth(1)); draw(shift(5,0)*r,linewidth(1)); draw(shift(5,0)*rotate(90)*r,linewidth(1)); draw(shift(5,0)*rotate(180)*r,linewidth(1)); draw(shift(5,0)*rotate(270)*r,linewidth(1)); draw(shift(10,0)*r,linewidth(1)); draw(shift(10,0)*rotate(60)*r,linewidth(1)); draw(shift(10,0)*rotate(120)*r,linewidth(1)); draw(shift(10,0)*rotate(180)*r,linewidth(1)); draw(shift(10,0)*rotate(240)*r,linewidth(1)); draw(shift(10,0)*rotate(300)*r,linewidth(1)); label("$P$", (-2,2)); label("$Q$", shift(5,0)*(-2,2)); label("$R$", shift(10,0)*(-2,2)); label("$1$", (-1,sqrt(2)/2)); label("$2$", (1,sqrt(2)/2)); label("$3$", (0,-1)); label("$2$", shift(5,0)*(-sqrt(2)/2,sqrt(2)/2)); label("$4$", shift(5,0)*(sqrt(2)/2,sqrt(2)/2)); label("$6$", shift(5,0)*(sqrt(2)/2,-sqrt(2)/2)); label("$8$", shift(5,0)*(-sqrt(2)/2,-sqrt(2)/2)); label("$1$", shift(10,0)*(-0.5,1)); label("$3$", shift(10,0)*(0.5,1)); label("$5$", shift(10,0)*(1,0)); label("$7$", shift(10,0)*(0.5,-1)); label("$9$", shift(10,0)*(-0.5,-1)); label("$11$", shift(10,0)*(-1,0)); [/asy]

$\textbf{(A)}\ \frac{1}{4}\qquad\textbf{(B)}\ \frac{1}{3}\qquad\textbf{(C)}\ \frac{1}{2}\qquad\textbf{(D)}\ \frac{2}{3}\qquad\textbf{(E)}\ \frac{3}{4}$

## Solution
In order for Jeff to have an odd number sum, the numbers must either be Odd + Odd + Odd or Even + Even + Odd. We easily notice that we cannot obtain Odd + Odd + Odd because spinner $Q$ contains only even numbers. Therefore we must work with Even + Even + Odd and spinner $Q$ will give us one of our even numbers. We also see that spinner $R$ only contains odd, so spinner $R$ must give us our odd number. We still need one even number from spinner $P$ . There is only 1 even number: $2$ . Since spinning the required numbers are automatic on the other spinners, we only have to find the probability of spinning a $2$ in spinner $P$ , which is clearly $\boxed{\textbf{(B)}\ \frac{1}{3}}$

## Video Solution by WhyMath
https://youtu.be/KTEfZj8Chs4
### See Also