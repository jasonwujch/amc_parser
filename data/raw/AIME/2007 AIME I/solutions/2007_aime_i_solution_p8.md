# 2007 AIME I Problem 8

## Problem

The polynomial $P(x)$ is cubic . What is the largest value of $k$ for which the polynomials $Q_1(x) = x^2 + (k-29)x - k$ and $Q_2(x) = 2x^2+ (2k-43)x + k$ are both factors of $P(x)$ ?

## Solution

## Solution 1
We can see that $Q_1$ and $Q_2$ must have a root in common for them to both be factors of the same cubic.
Let this root be $a$ .
We then know that $a$ is a root of $Q_{2}(x)-2Q_{1}(x) = 2x^{2}+2kx-43x+k-2x^{2}-2kx+58x+2k = 15x+3k$ , so $Q_{2}(a)-2Q_1(a)=15a+3k=0\implies a = \frac{-k}{5}$ .
We then know that $\frac{-k}{5}$ is a root of $Q_{1}$ so we get: $\frac{k^{2}}{25}+(k-29)\left(\frac{-k}{5}\right)-k = 0 = k^{2}-5(k-29)(k)-25k = k^{2}-5k^{2}+145k-25k$ or $k^{2}=30k$ , so $k=30$ is the highest.
We can trivially check into the original equations to find that $k=30$ produces a root in common, so the answer is $\boxed{030}$ .

## Solution 2
Again, let the common root be $a$ ; let the other two roots be $m$ and $n$ . We can write that $(x - a)(x - m) = x^2 + (k - 29)x - k$ and that $2(x - a)(x - n) = 2\left(x^2 + \left(k - \frac{43}{2}\right)x + \frac{k}{2}\right)$ .
Therefore, we can write four equations (and we have four variables ), $a + m = 29 - k$ , $a + n = \frac{43}{2} - k$ , $am = -k$ , and $an = \frac{k}{2}$ .
The first two equations show that $m - n = 29 - \frac{43}{2} = \frac{15}{2}$ . The last two equations show that $\frac{m}{n} = -2$ . Solving these show that $m = 5$ and that $n = -\frac{5}{2}$ . Substituting back into the equations, we eventually find that $k = \boxed{030}$ .

## Solution 3
Since $Q_1(x)$ and $Q_2(x)$ are both factors of $P(x)$ , which is cubic, we know the other factors associated with each of $Q_1(x)$ and $Q_2(x)$ must be linear. Let $Q_1(x)R(x) = Q_2(x)S(x) = P(x)$ , where $R(x) = ax + b$ and $S(x) = cx + d$ . Then we have that $((x^2 + (k-29)x - k))(ax + b) = ((2x^2+ (2k-43)x + k))(cx + d)$ . Equating coefficients, we get the following system of equations:
\begin{align} a = 2c \\ b = -d \\ 2c(k - 29) - d = c(2k - 43) + 2d \\ -d(k - 29) - 2ck = d(2k - 43) + ck \end{align}
Using equations $(1)$ and $(2)$ to make substitutions into equation $(3)$ , we see that the $k$ 's drop out and we're left with $d = -5c$ . Substituting this expression for $d$ into equation $(4)$ and solving, we see that $k$ must be $\boxed {030}$ .
~ anellipticcurveoverq

## Solution 4
Notice that if the roots of $Q_1(x)$ and $Q_2(x)$ are all distinct, then $P(x)$ would have four distinct roots, which is a contradiction since it's cubic.
Thus, $Q_1(x)$ and $Q_2(x)$ must share a root. Let this common value be $r.$
Thus, we see that we have \[r^2 + (k - 29)r - k = 0,\] \[2r^2 + (2k - 43)r + k = 0.\] Adding the two equations gives us \[3r^2 + (3k - 72)r = 0 \implies r = 0, 24 - k.\] Now, we have two cases to consider. If $r = 0,$ then we have that $Q_1(r) = 0 = r^2 + (k - 29)r - k \implies k = 0.$ On the other hand, if $r = 24 - k,$ we see that \[Q_1(r) = 0 = (24 - k)^2 + (k - 29)(24 - k) - k \implies k = \boxed{030}.\] This can easily be checked to see that it does indeed work, and we're done!
~Ilikeapos

## Solution 5
Since $Q_1(x) = x^2 + (k - 29)x - k$ and $Q_2(x) = 2x^2 + (2k - 43)x + k$ are both factors of the cubic polynomial $P(x)$ , and both are quadratics, the only way for them to divide the same cubic is if they share a common linear factor. Otherwise, their product would be degree 4, which is too large. Therefore, $P(x)$ can be factored as $P(x) = Q_1(x)(2x + a) = Q_2(x)(x + b)$ for some constants $a, b$ . We choose the linear factors so that both products have degree 3 with leading coefficient 2: since $Q_1$ has leading coefficient 1, its linear factor must have leading coefficient 2, and since $Q_2$ has leading coefficient 2, its linear factor must have leading coefficient 1.
Looking at constant terms on both sides, $-k \cdot a = k \cdot b$ , so $-k a = k b \implies a = -b.$
Next, expanding both sides and comparing the $x^2$ coefficients gives $a + 2k - 58 = 2b + 2k - 43.$ Substituting $a = -b$ , we get $-b + 2k - 58 = 2b + 2k - 43 \implies -b = 2b + 15 \implies b = -5, \quad a = 5.$
Finally, comparing the $x$ coefficients: $a(k - 29) - 2k = (2k - 43) b + k,$ which becomes $5(k - 29) - 2k = (2k - 43)(-5) + k,$ simplifying to $3k - 145 = -9k + 215.$ Solving for $k$ yields $12k = 360 \implies \boxed{30}.$
~MathKing555

## Video Solution
https://www.youtube.com/watch?v=bsRQZwO7n84&t=64s
These problems are copyrighted © by the Mathematical Association of America.