# 2008 AMC 8 Problem 25

## Problem

Margie's winning art design is shown. The smallest circle has radius 2 inches, with each successive circle's radius increasing by 2 inches. Which of the following is closest to the percent of the design that is black?

[asy] real d=320; pair O=origin; pair P=O+8*dir(d); pair A0 = origin; pair A1 = O+1*dir(d); pair A2 = O+2*dir(d); pair A3 = O+3*dir(d); pair A4 = O+4*dir(d); pair A5 = O+5*dir(d); filldraw(Circle(A0, 6), white, black); filldraw(circle(A1, 5), black, black); filldraw(circle(A2, 4), white, black); filldraw(circle(A3, 3), black, black); filldraw(circle(A4, 2), white, black); filldraw(circle(A5, 1), black, black); [/asy]

$\textbf{(A)}\ 42\qquad \textbf{(B)}\ 44\qquad \textbf{(C)}\ 45\qquad \textbf{(D)}\ 46\qquad \textbf{(E)}\ 48\qquad$

## Solution
Let the smallest circle be 1, the second smallest circle be 2, the third smallest circle be 3, etc. \[\begin{array}{c|cc} \text{circle \#} & \text{radius} & \text{area} \\ \hline 1 & 2 & 4\pi \\ 2 & 4 & 16\pi \\ 3 & 6 & 36\pi \\ 4 & 8 & 64\pi \\ 5 & 10 & 100\pi \\ 6 & 12 & 144\pi \end{array}\]
The entire circle's area is $144\pi$ . The area of the black regions is $(100-64)\pi + (36-16)\pi + 4\pi = 60\pi$ . The percentage of the design that is black is $\frac{60\pi}{144\pi} = \frac{5}{12} \approx \boxed{\textbf{(A)}\ 42}$ .

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=3363
~ pi_is_3.14
### See Also