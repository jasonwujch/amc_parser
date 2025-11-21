# 2002 AMC 12P Problem 20

## Problem

Let $f$ be a real-valued function such that

\[f(x) + 2f(\frac{2002}{x}) = 3x\]

for all $x>0.$ Find $f(2).$

$\text{(A) }1000 \qquad \text{(B) }2000 \qquad \text{(C) }3000 \qquad \text{(D) }4000 \qquad \text{(E) }6000$

## Solution
Setting $x = 2$ gives $f(2) + 2f(1001) = 6$ . Setting $x = 1001$ gives $2f(2) + f(1001) = 3003$ .
Adding these 2 equations and dividing by 3 gives $f(2) + f(1001) = \frac{6+3003}{3} = 1003$ .
Subtracting these 2 equations gives $f(2) - f(1001) = 2997$ .
Therefore, $f(2) = \frac{1003+2997}{2} = \boxed {\textbf{(B) }2000}$ .
### Note
We can find a closed form expression for $f$ using this method. We have that \[f(x) + 2f(\frac{2002}{x}) = 3x\] and plugging in $\frac{2002}{x}$ gives \[f(\frac{2002}{x}) + 2f(x) = 3(\frac{2002}{x}).\]
Let $a = f(x)$ and $b = f(\frac{2002}{x})$ . Then, we have \[a + 2b = 3x \tag{1}\] and \[2a + b = \frac{6006}{x} \tag{2}\]
We add equations $(1)$ and $(2)$ and divide by $3$ to get $a+b = x + \frac{2002}{x}$ . Subtracting this from equation $(2)$ gives us the closed form \[f(x) = \frac{4004}{x} - x\]
Indeed, plugging in $x=2$ gives us $f(2) = \frac{4004}{2} - 2 = \boxed {\textbf{(B) }2000}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .