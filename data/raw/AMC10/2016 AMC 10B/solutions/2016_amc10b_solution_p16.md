# 2016 AMC 10B Problem 16

## Problem

The sum of an infinite geometric series is a positive number $S$ , and the second term in the series is $1$ . What is the smallest possible value of $S?$

$\textbf{(A)}\ \frac{1+\sqrt{5}}{2} \qquad \textbf{(B)}\ 2 \qquad \textbf{(C)}\ \sqrt{5} \qquad \textbf{(D)}\ 3 \qquad \textbf{(E)}\ 4$

## Solution 1
The sum of an infinite geometric series is of the form: \[\begin{split} S & = \frac{a_1}{1-r} \end{split}\] where $a_1$ is the first term and $r$ is the ratio whose absolute value is less than 1.
We know that the second term is the first term multiplied by the ratio. In other words: \[\begin{split} a_1 \cdot r & = 1 \\ a_1 & = \frac{1}{r} \end{split}\]
Thus, the sum is the following: \[\begin{split} S & = \frac{\frac{1}{r}}{1-r} \\\\ S & =\frac{1}{r-r^2} \end{split}\]
Since we want the minimum value of this expression, we want the maximum value for the denominator, $-r^2+r$ . The maximum x-value of a quadratic with leading coefficient $-a$ is $\frac{-b}{2a}$ . \[\begin{split} r & = \frac{-(1)}{2(-1)} \\\\ r & = \frac{1}{2} \end{split}\]
Plugging $r$ $=$ $\frac{1}{2}$ into the quadratic yields: \[\begin{split} S & = \frac{1}{\frac{1}{2} -\left(\frac{1}{2}\right)^2} \\\\ S & = \frac{1}{\frac{1}{4}} \end{split}\]
Therefore, the minimum sum of our infinite geometric sequence is $\boxed{\textbf{(E)}\ 4}$ . (Solution by akaashp11)
As an extension to find the maximum value for the denominator we can find the derivative of $-r^2+r$ to get $1-2r$ . we know that this changes sign when $r = \frac{1}{2}$ so plugging it in into the original equation we find the answer is $\boxed{\textbf{(E)}\ 4}$ .

## Solution 2
After observation we realize that in order to minimize our sum $\frac{a}{1-r}$ with $a$ being the reciprocal of r, the common ratio $r$ has to be in the form of $\frac{1}{x}$ , with $x$ being an integer, as anything more than $1$ divided by $x$ would give a larger sum than a ratio in the form of $\frac{1}{x}$ .
The first term has to be $x$ , so then in order to minimize the sum, we have to minimize $x$ .
The smallest possible value for $x$ such that it is an integer that's greater than $1$ is $2$ . So our first term is $2$ and our common ratio is $\frac{1}{2}$ . Thus the sum is $\frac{2}{\frac {1}{2}}$ or $\boxed{\textbf{(E)}\ 4}$ . Solution 2 by No_One
(edited)

## Solution 3
We can see that if $a$ is the first term, and $r$ is the common ratio between each of the terms, then we can get \[S=\frac{a}{1-r} \implies S-Sr=a\] Also, we know that the second term can be expressed as $a\cdot r$ notice if we multiply $S-Sr=a$ by $r$ , we would get \[r(S-Sr)=ar \implies Sr-Sr^2=1 \implies Sr^2-Sr+1=0\] This quadratic has real solutions if the discriminant is greater than or equal to zero, or \[S^2-4\cdot S \cdot 1 \ge 0\] This yields that $S\le 0$ or $S\ge 4$ . However, since we know that $S$ has to be positive, we can safely conclude that the minimum possible value of $S$ is $\boxed{\textbf{(E)}\ 4}$ .

## Solution 4 (Quick Method)
Let the first term of the geometric series $x$ . Since it must be decreasing, we have $x>1$ and the third term is $\frac{1}{x}$ . Realize that by AM-GM inequality $x+\frac{1}{x} \ge 2$ with equality if $x = 1$ . However, we established that $x>1$ so that means $x+\frac{1}{x} > 2$ . So the sum of the first three terms of the sequence $x + \frac{1}{x} + 1$ is greater than $3$ , and the geometric series keeps continuing infinitely. This means the sum continues increasing. The only answer choice greater than $3$ is $\boxed{\textbf{(E)}\ 4}$ . ~skyscraper

## Solution 5 (Clever Algebra)
Let the first term be $k.$ The sum of the series is $\frac{k}{1- \frac{1}{k}} =\frac{k^2}{k-1}.$ Rewrite this as $\frac{k^2-2k+1}{k-1} +\frac{2k-1}{k-1} = k-1+\frac{2k-2}{k-1} +\frac{1}{k-1} = (k-1) + \left(\frac{1}{k-1}\right) + 2.$ By AM-GM we know that $(k-1) + \left(\frac{1}{k-1}\right) \ge 2$ so the minimum is $2+2 = \boxed{\textbf{(E)}\ 4}.$

## Solution 6 (Calculus)
Set the first term is $a.$ , the common ratio should be $\frac{1}{a}.$
The sum to infinity of the series is $S=\frac{a}{1-\frac{1}{a}}=\frac{a^2}{a-1}.$
Since $S$ is positive, we have $a>1.$ Define the function $f(a)=\frac{a^2}{a-1}$ , the domain of this function is $a>1.$
Let $f^{'}(a)=\frac{2a^2-2a-a^2}{(a-1)^2}=\frac{a(a-2)}{(a-1)^2}=0.$ We solve that $a=2.$
It's easy to find that when $1<a<2, f^{'}(a)<0,$ when $a>2, f^{'}(a)>0.$ Thus $f(a)$ has a minimum value when $a=2.$ , which is $f(2)=4.$ Choose $\boxed{\textbf{(E)}\ 4}.$
~PythZhou
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .