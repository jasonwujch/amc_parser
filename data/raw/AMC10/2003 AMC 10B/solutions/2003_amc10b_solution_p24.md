# 2003 AMC 10B Problem 24

## Problem

The first four terms in an arithmetic sequence are $x+y$ , $x-y$ , $xy$ , and $\frac{x}{y}$ , in that order. What is the fifth term?

$\textbf{(A)}\ -\frac{15}{8}\qquad\textbf{(B)}\ -\frac{6}{5}\qquad\textbf{(C)}\ 0\qquad\textbf{(D)}\ \frac{27}{20}\qquad\textbf{(E)}\ \frac{123}{40}$

## Solution 1
The difference between consecutive terms is $(x-y)-(x+y)=-2y.$ Therefore we can also express the third and fourth terms as $x-3y$ and $x-5y.$ Then we can set them equal to $xy$ and $\frac{x}{y}$ because they are the same thing.
\begin{align*} xy&=x-3y\\ xy-x&=-3y\\ x(y-1)&=-3y\\ x&=\frac{-3y}{y-1} \end{align*}
Substitute into our other equation.
\[\frac{x}{y}=x-5y\] \[\frac{-3}{y-1}=\frac{-3y}{y-1}-5y\] \[-3=-3y-5y(y-1)\] \[0=5y^2-2y-3\] \[0=(5y+3)(y-1)\] \[y=-\frac35, 1\]
But $y$ cannot be $1$ because then the first term would be $x+1$ and the second term $x-1$ while the last two terms would be equal to $x.$ Therefore $y=-\frac35.$ Substituting the value for $y$ into any of the equations, we get $x=-\frac98.$ Finally,
\[\frac{x}{y}-2y=\frac{9\cdot 5}{8\cdot 3}+\frac{6}{5}=\boxed{\textbf{(E)}\ \frac{123}{40}}\]

## Solution 2
Because this is an arithmetic sequence, we conclude from the first two terms that the common difference is $-2y$ . Therefore, $xy = x-3y$ and $\frac{x}{y}=x-5y$ . If we multiply $xy$ and $\frac{x}{y}$ , we see:
$xy\cdot\frac{x}{y} = (x-3y)(x-5y) = x^2 - 8xy + 15y^2$
Because $xy\cdot\frac{x}{y}$ , by basic multiplication, is $x^2$ , we have
$x^2 = x^2 - 8xy + 15y^2$
$8xy = 15y^2$
$8x = 15y$
$x = \frac{15y}{8}$
Now that we have $x$ in terms of $y$ , we substitute in $\frac{15y}{8}$ in for $x$ in $\frac{x}{y}$ (the fourth term). This leaves us with $\frac{\frac{15y}{8}}{y} = \frac{15}{8}$ .
Recall that $\frac{x}{y}$ can be written as $x - 5y$ . Thus, $x - 5y = \frac{15}{8}$ . Substitute in $\frac{15}{8}$ in for $x$ , and we see:
$\frac{15y}{8} - 5y = \frac{15}{8}$
$15y - 40y = 15$
$y = \frac{15}{-25} = \frac{-3}{5}$
Aha! This means $2y$ , the common difference, is $2\cdot y = 2\cdot \frac{-3}{5} = \frac{-6}{5}$ . Now, all we need to do is find the fifth term, which is just $\frac{x}{y}-2y$ . We can substitute known values to solve:
$\frac{x}{y}-2y = \frac{15}{8} - \frac{-6}{5} = \frac{15}{8} + \frac{6}{5} = \frac{75 + 48}{40} = \boxed{\textbf{(E)}\ \frac{123}{40}}$ .
~SXWang

## Solution 3
From the first two terms, we can figure out the common difference, $x-y-(x+y)=-2y$ . This means that the third, fourth and fifth terms are $x-3y$ , $x-5y$ and $x-7y$ respectively.
The third term is also equal to $xy$ , so $xy=x-3y$ , which can be rearranged to $xy+3y=x$ .
Dividing by y, we have $x+3=\frac{x}{y}$ .
$\frac{x}{y}$ happens to be the fourth term. Therefore, $\frac{x}{y}=x-5y=x+3$ .
$x-5y=x+3$
$-5y=3$
$y=-\frac{3}{5}$
Now that we have $y$ , we can substitute it into an equation above, like $\frac{x}{y}=x+3$ .
$\frac{x}{\frac{-3}{5}}=x+3$
$-\frac{5x}{3}=x+3$
$-\frac{5x+3x}{3}=3$
$-\frac{8x}{3}=3$
$8x=-9$
$x=\frac{-9}{8}$
As mentioned earlier, the fifth term we want in the end is equal to $x-7y$ . Substitute some more and...
$\frac{-9}{8}-7(\frac{-3}{5})=\frac{-9\cdot5}{8\cdot5}+\frac{-3\cdot-7\cdot8}{5\cdot8}=\frac{-45}{40}+\frac{168}{40}=\boxed{\textbf{(E)}\ \frac{123}{40}}$
(Alternatively, like the above solutions suggest, you could also use the admittedly easier $\frac{x}{y}-2y$ as the final step.)
~ a seesaw named owlly81 ~

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=wzNnrj51BAQ
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .