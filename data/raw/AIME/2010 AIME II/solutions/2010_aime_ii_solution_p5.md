# 2010 AIME II Problem 5

## Problem

Positive numbers $x$ , $y$ , and $z$ satisfy $xyz = 10^{81}$ and $(\log_{10}x)(\log_{10} yz) + (\log_{10}y) (\log_{10}z) = 468$ . Find $\sqrt {(\log_{10}x)^2 + (\log_{10}y)^2 + (\log_{10}z)^2}$ .

## Solution
Using the properties of logarithms, $\log_{10}xyz = 81$ by taking the log base 10 of both sides, and $(\log_{10}x)(\log_{10}y) + (\log_{10}x)(\log_{10}z) + (\log_{10}y)(\log_{10}z)= 468$ by using the fact that $\log_{10}ab = \log_{10}a + \log_{10}b$ .
Through further simplification, we find that $\log_{10}x+\log_{10}y+\log_{10}z = 81$ . It can be seen that there is enough information to use the formula $\ (a+b+c)^{2} = a^{2}+b^{2}+c^{2}+2ab+2ac+2bc$ , as we have both $\ a+b+c$ and $\ 2ab+2ac+2bc$ , and we want to find $\sqrt {a^2 + b^2 + c^2}$ .
After plugging in the values into the equation, we find that $\ (\log_{10}x)^2 + (\log_{10}y)^2 + (\log_{10}z)^2$ is equal to $\ 6561 - 936 = 5625$ .
However, we want to find $\sqrt {(\log_{10}x)^2 + (\log_{10}y)^2 + (\log_{10}z)^2}$ , so we take the square root of $\ 5625$ , or $\boxed{075}$ .

## Solution 2
Let $a=\log_{10}x$ , $b=\log_{10}y,$ and $c=\log_{10}z$ .
We have $a+b+c=81$ and $a(b+c)+bc=ab+ac+bc=468$ . Since these two equations look a lot like Vieta's for a cubic, create the polynomial $x^3-81x^2+468x=0$ (leave the constant term as $0$ to make things easy). Dividing by $x$ yields $x^2-81x+468=0$ .
Now we use the quadratic formula:
$x=\frac{81\pm\sqrt{81^2-4\cdot468}}{2}$
$x=\frac{81\pm\sqrt{4689}}{2}$
$x=\frac{81+3\sqrt{521}}{2}$ , $x=\frac{81-3\sqrt{521}}{2}$
Since the question asks for $\sqrt{a^2+b^2+c^2}$ (remember one of the values was the solution $x=0$ that we divided out in the beginning), we find:
$\sqrt{\left(\frac{81+3\sqrt{521}}{2}\right)^2+\left(\frac{81-3\sqrt{521}}{2}\right)^2}$
$=\sqrt{2\cdot\frac{81^2+(3\sqrt{521})^2}{4}}$
$=\sqrt{\frac{11250}{2}}$
$=\boxed{075}$
~bad_at_mathcounts

## Video solution
https://www.youtube.com/watch?v=Ix6czB_A_Js&t
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .