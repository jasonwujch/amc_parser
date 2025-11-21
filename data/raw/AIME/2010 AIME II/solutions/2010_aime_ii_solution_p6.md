# 2010 AIME II Problem 6

## Problem

Find the smallest positive integer $n$ with the property that the polynomial $x^4 - nx + 63$ can be written as a product of two nonconstant polynomials with integer coefficients.

## Solution 1
You can factor the polynomial into two quadratic factors or a linear and a cubic factor.
For two quadratic factors, let $x^2+ax+b$ and $x^2+cx+d$ be the two quadratics, so that
\[(x^2 + ax + b )(x^2 + cx + d) = x^4 + (a + c)x^3 + (b + d + ac)x^2 + (ad + bc)x + bd.\]
Therefore, again setting coefficients equal, $a + c = 0\Longrightarrow a=-c$ , $b + d + ac = 0\Longrightarrow b+d=a^2$ , $ad + bc = - n$ , and so $bd = 63$ .
Since $b+d=a^2$ , the only possible values for $(b,d)$ are $(1,63)$ and $(7,9)$ . From this we find that the possible values for $n$ are $\pm 8 \cdot 62$ and $\pm 4 \cdot 2$ .
For the case of one linear and one cubic factor, doing a similar expansion and matching of the coefficients gives the smallest $n$ in that case to be $48$ .
Therefore, the answer is $4 \cdot 2 = \boxed{008}$ .

## Solution 2
Let $x^4-nx+63=(x^2+ax+b)(x^2+cx+d)$ . From this, we get that $bd=63\implies d=\frac{63}{b}$ and $a+c=0\implies c=-a$ . Plugging this back into the equation, we get $x^4-nx+63=(x^2+ax+b)\left(x^2-ax+\frac{63}{b}\right)$ . Expanding gives us $x^4-nx+63=x^4+\left(-a^2+b+\frac{63}{b}\right)x^2+\left(\frac{63a}{b}-ab\right)x+63$ . Therefore $-a^2+b+\frac{63}{b}=0$ . Simplifying gets us $b(a^2-b)=63$ . Since $a$ and $b$ must be integers, we can use guess and check for values of $b$ because $b$ must be a factor of $63$ . Note that $b$ cannot be negative because $a$ would be imaginary. After guessing and checking, we find that the possible values of $(a,b)$ are $(\pm 8, 1), (\pm 4, 7), (\pm 4, 9),$ and $(\pm 8, 63)$ . We have that $n=ab-\frac{63a}{b}$ . Plugging in our values for $a$ and $b$ , we get that the smallest positive integer value $n$ can be is $\boxed{008}$ . -Heavytoothpaste
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .