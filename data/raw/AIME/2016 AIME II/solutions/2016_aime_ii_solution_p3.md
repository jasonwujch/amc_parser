# 2016 AIME II Problem 3

## Problem

Let $x,y,$ and $z$ be real numbers satisfying the system \begin{align*} \log_2(xyz-3+\log_5 x)&=5,\\ \log_3(xyz-3+\log_5 y)&=4,\\ \log_4(xyz-3+\log_5 z)&=4.\\ \end{align*} Find the value of $|\log_5 x|+|\log_5 y|+|\log_5 z|$ .

## Solution
First, we get rid of logs by taking powers: $xyz-3+\log_5 x=2^{5}=32$ , $xyz-3+\log_5 y=3^{4}=81$ , and $(xyz-3+\log_5 z)=4^{4}=256$ . Adding all the equations up and using the $\log {xy}=\log {x}+\log{y}$ property, we have $3xyz+\log_5{xyz} = 378$ , so we have $xyz=125$ . Solving for $x,y,z$ by substituting $125$ for $xyz$ in each equation, we get $\log_5 x=-90, \log_5 y=-41, \log_5 z=134$ , so adding all the absolute values we have $90+41+134=\boxed{265}$ .
Note: $xyz=125$ because we know $xyz$ has to be a power of $5$ , and so it is not hard to test values in the equation $3xyz+\log_5{xyz} = 378$ in order to achieve desired value for $xyz$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .