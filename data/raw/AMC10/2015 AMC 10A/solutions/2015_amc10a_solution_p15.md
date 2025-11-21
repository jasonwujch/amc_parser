# 2015 AMC 10A Problem 15

## Problem

Consider the set of all fractions $\frac{x}{y}$ , where $x$ and $y$ are relatively prime positive integers. How many of these fractions have the property that if both numerator and denominator are increased by $1$ , the value of the fraction is increased by $10\%$ ?

$\textbf{(A) }0\qquad\textbf{(B) }1\qquad\textbf{(C) }2\qquad\textbf{(D) }3\qquad\textbf{(E) }\text{infinitely many}$

## Solution 1
You can create the equation $\frac{x+1}{y+1}=\frac{11x}{10y}$
Cross multiplying and combining like terms gives $xy + 11x - 10y = 0$ .
This can be factored into $(x - 10)(y + 11) = -110$ .
$x$ and $y$ must be positive, so $x > 0$ and $y > 0$ , so $x - 10> -10$ and $y + 11 > 11$ .
Using the factors of 110, we can get the factor pairs: $(-1, 110),$ $(-2, 55),$ and $(-5, 22).$
But we can't stop here because $x$ and $y$ must be relatively prime.
$(-1, 110)$ gives $x = 9$ and $y = 99$ . $9$ and $99$ are not relatively prime, so this doesn't work.
$(-2, 55)$ gives $x = 8$ and $y = 44$ . This doesn't work.
$(-5, 22)$ gives $x = 5$ and $y = 11$ . This does work.
We found one valid solution so the answer is $\boxed{\textbf{(B) }1}$ .

## Solution 2
The condition required is $\frac{x+1}{y+1}=\frac{11}{10}\cdot\frac{x}{y}$ .
Observe that $x+1 > \frac{11}{10}\cdot x$ so $x$ is at most $9.$
By multiplying by $\frac{y+1}{x}$ and simplifying we can rewrite the condition as $y=\frac{11x}{10-x}$ . Since $x$ and $y$ are integer, this only has solutions for $x\in\{5,8,9\}$ . However, only the first yields a $y$ that is relative prime to $x$ .
There is only one valid solution so the answer is $\boxed{\textbf{(B) }1}$

## Solution 3
So from this question, we can get \(\frac{x+1}{y+1} = \frac{11x}{10y}\). We can transform this equation into \(x + 11 \cdot \left( \frac{x}{y} \right) = 10\). Two numbers are added to get 10, and one of them, \(x\), is a positive and prime integer. So the other number also has to be a positive integer. Therefore, \(11 \cdot \left( \frac{x}{y} \right)\) is a positive integer. The only possibility of this being true is when \(y\) and 11 cancel out, leaving a singular \(x\). So \(y = 11\) and \(x + x = 10\). Therefore, \(y = 11\) and \(x = 5\).
~POISONPOISSON

## Video Solution
https://youtu.be/p7g0hTxE9I8
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .