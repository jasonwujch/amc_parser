# 2021 AIME II Problem 4

## Problem

There are real numbers $a, b, c,$ and $d$ such that $-20$ is a root of $x^3 + ax + b$ and $-21$ is a root of $x^3 + cx^2 + d.$ These two polynomials share a complex root $m + \sqrt{n} \cdot i,$ where $m$ and $n$ are positive integers and $i = \sqrt{-1}.$ Find $m+n.$

## Solution 1 (Complex Conjugate Root Theorem and Vieta's Formulas)
By the Complex Conjugate Root Theorem, the imaginary roots for each of $x^3+ax+b$ and $x^3+cx^2+d$ are complex conjugates. Let $z=m+\sqrt{n}\cdot i$ and $\overline{z}=m-\sqrt{n}\cdot i.$ It follows that the roots of $x^3+ax+b$ are $-20,z,\overline{z},$ and the roots of $x^3+cx^2+d$ are $-21,z,\overline{z}.$
We know that \begin{align*} z+\overline{z}&=2m, & (1) \\ z\overline{z}&=m^2+n. & (2) \end{align*} Applying Vieta's Formulas to $x^3+ax+b,$ we have $-20+z+\overline{z}=0.$ Substituting $(1)$ into this equation, we get $m=10.$
Applying Vieta's Formulas to $x^3+cx^2+d,$ we have $-21z-21\overline{z}+z\overline{z}=0,$ or $-21(z+\overline{z})+z\overline{z}=0.$ Substituting $(1)$ and $(2)$ into this equation, we get $n=320.$
Finally, the answer is $m+n=\boxed{330}.$
~MRENTHUSIASM

## Solution 2 (Somewhat Bashy)
$(-20)^{3} + (-20)a + b = 0$ , hence $-20a + b = 8000$
Also, $(-21)^{3} + c(-21)^{2} + d = 0$ , hence $441c + d = 9261$
$m + i \sqrt{n}$ satisfies both $\Rightarrow$ we can put it in both equations and equate to 0.
In the first equation, we get $(m + i \sqrt{n})^{3} + a(m + i \sqrt{n}) + b = 0$ Simplifying this further, we get $(m^{3} - 3mn + am + b) + i(3m^{2} \sqrt{n} - n\sqrt{n} + a\sqrt{n}) = 0$
Hence, $m^{3} - 3mn + am + b = 0$ and $3m^{2} \sqrt{n} - n\sqrt{n} + a\sqrt{n} = 0 \Rightarrow 3m^{2} - n + a = 0 \rightarrow (1)$
In the second equation, we get $(m + i \sqrt{n})^{3} + c(m + i \sqrt{n})^{2} + d = 0$ Simplifying this further, we get $(m^{3} + m^{2}c - nc - 3mn + d) + i(3m^{2} \sqrt{n} - n\sqrt{n} + 2mc\sqrt{n}) = 0$
Hence, $m^{3} + m^{2}c - nc - 3mn + d = 0$ and $3m^{2} \sqrt{n} - n\sqrt{n} + 2mc\sqrt{n} = 0 \Rightarrow 3m^{2} - n + 2mc = 0 \rightarrow (2)$
Comparing (1) and (2),
$a = 2mc$ and $am + b = m^{2}c - nc + d \rightarrow (3)$
$b = 8000 + 20a \Rightarrow b = 40mc + 8000$ ; $d = 9261 - 441c$
Substituting these in $(3)$ gives, $2m^{2}c + 8000 + 40mc = m^{2}c - nc + 9261 - 441c$
This simplifies to $m^{2}c + nc + 40mc + 441c = 1261 \Rightarrow c(m^{2} + n + 40m + 441) = 1261$
Hence, $c|1261 \Rightarrow c \in {1,13,97,1261}$
Consider case of $c = 1$ :
$c = 1 \Rightarrow d = 8820$ Also, $a = 2m, b = 8000 + 40m$
$am + b = m^{2} - n + 8820$ (because c = 1) Also, $m^{2} + n + 40m = 820 \rightarrow (4)$ Also, Equation (2) gives $3m^{2} - n + 2m = 0 \rightarrow (5)$
Solving (4) and (5) simultaneously gives $m = 10, n = 320$
[AIME can not have more than one answer, so we can stop here ... Not suitable for objective exam]
Hence, $m + n = 10 + 320 = \boxed{330}$
-Arnav Nigam

## Solution 3 (Heavy Calculation Solution)
We start off by applying Vieta's, and we find that $a=m^2+n-40m$ , $b=20m^2+20n$ , $c=21-2m$ , and $d=21m^2+21n$ . After that, we use the fact that $-20$ and $-21$ are roots of $x^3+ax+b$ and $x^3+cx^2+d$ , respectively. Since substituting the roots back into the function returns zero, we have that $(-20)^3-20a+b=0$ and $(-21)^3+c\cdot (-21)^2+d=0$ . Setting these two equations equal to each other while also substituting the values of $a$ , $b$ , $c$ , and $d$ above gives us $21m^2+21n-1682m+8000=0$ . We then rearrange the equation into $21n = -21m^2+1682m-8000$ .
With this property, we know that $-21m^2+1682m-8000$ is divisible by $21$ , so $1682m-8000=0 \pmod{21}$ . This results in $2m-20=0 \pmod{21}$ , which finally gives us $m=10 \pmod{21}$ . We can test the first obvious value of $m$ , which is $10$ , to find that this works, and we get $m=10$ and $n=320$ . Therefore, the answer is $m + n = 10 + 320 = \boxed{330}.$
~Jske25
~sidkris (formatting edits)

## Solution 4 (Synthetic Division)
We note that $x^3 + ax + b = (x+20)P(x)$ and $x^3 + cx^2 + d = (x+21)Q(x)$ for some polynomials $P(x)$ and $Q(x)$ .
Through synthetic division (ignoring the remainder as we can set $b$ and $d$ to constant values such that the remainder is zero), $P(x) = x^2 - 20x + (400+a)$ , and $Q(x) = x^2 + (c-21)x + (441 - 21c)$ .
By the complex conjugate root theorem, we know that $P(x)$ and $Q(x)$ share the same roots, and they share the same leading coefficient, so $P(x) = Q(x)$ .
Therefore, $c-21 = -20$ and $441-21c = 400 + a$ . Solving the system of equations, we get $a = 20$ and $c = 1$ , so $P(x) = Q(x) = x^2 - 20x + 420$ .
Finally, by the quadratic formula, we have roots of $\frac{20 \pm \sqrt{400 - 1680}}{2} = 10 \pm \sqrt{320}i$ , so our final answer is $10 + 320 = \boxed{330}$
-faefeyfa

## Solution 5 (Fast and Easy)
We plug -20 into the equation obtaining $(-20)^3-20a+b$ , likewise, plugging -21 into the second equation gets $(-21)^3+441c+d$ .
Both equations must have 3 solutions exactly, so the other two solutions must be $m + \sqrt{n} \cdot i$ and $m - \sqrt{n} \cdot i$ .
By Vieta's, the sum of the roots in the first equation is $0$ , so $m$ must be $10$ .
Next, using Vieta's theorem on the second equation, you get $x1x2+x2x3+x1x3 = 0$ . However, since we know that the sum of the roots with complex numbers are 20, we can factor out the terms with -21, so $-21*(20)+(m^2+n)=0$ .
Given that $m$ is $10$ , then $n$ is equal to $320$ .
Therefore, the answer to the equation is $\boxed{330}$

## Solution 6 (solution by integralarefun)
Since $m+i\sqrt{n}$ is a common root and all the coefficients are real, $m-i\sqrt{n}$ must be a common root, too.
Now that we know all three roots of both polynomials, we can match coefficients (or more specifically, the zero coefficients).
First, however, the product of the two common roots is: \begin{align*} &&&(x-m-i\sqrt{n})(x-m+i\sqrt{n})\\ &=&&x^2-x(m+i\sqrt{n}+m-i\sqrt{n})+(m+i\sqrt{n})(m-i\sqrt{n})\\ &=&&x^2-2xm+(m^2-i^2n)\\ &=&&x^2-2xm+m^2+n \end{align*}
Now, let's equate the two forms of both the polynomials: \[x^3+ax+b=(x^2-2xm+m^2+n)(x+20)\] \[x^3+cx^2+d=(x^2-2xm+m^2+n)(x+21)\] Now we can match the zero coefficients. \[-2m+20=0\to m=10\text{ and}\] \[-42m+m^2+n=0\to-420+100+n=0\to n=320\text{.}\] Thus, $m+n=10+320=\boxed{330}$ .

## Video Solution
https://www.youtube.com/watch?v=sYRWWQayNyQ

## Video Solution by TheCALT
https://www.youtube.com/watch?v=HJ0EldshLuE
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .