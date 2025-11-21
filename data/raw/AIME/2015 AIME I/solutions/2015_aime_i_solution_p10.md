# 2015 AIME I Problem 10

## Problem

Let $f(x)$ be a third-degree polynomial with real coefficients satisfying \[|f(1)|=|f(2)|=|f(3)|=|f(5)|=|f(6)|=|f(7)|=12.\] Find $|f(0)|$ .

## Solution 1
Let $f(x)$ = $ax^3+bx^2+cx+d$ . Since $f(x)$ is a third degree polynomial, it can have at most two bends in it where it goes from up to down, or from down to up. By drawing a coordinate axis, and two lines representing $12$ and $-12$ , it is easy to see that $f(1)=f(5)=f(6)$ , and $f(2)=f(3)=f(7)$ ; otherwise more bends would be required in the graph. Since only the absolute value of $f(0)$ is required, there is no loss of generalization by stating that $f(1)=12$ , and $f(2)=-12$ . This provides the following system of equations. \[a + b + c + d = 12\] \[8a + 4b + 2c + d = -12\] \[27a + 9b + 3c + d = -12\] \[125a + 25b + 5c + d = 12\] \[216a + 36b + 6c + d = 12\] \[343a + 49b + 7c + d = -12\] Using any four of these functions as a system of equations yields $d = |f(0)| = \boxed{072}$
Note: You can use Gaussian elimination to solve these equations.

## Solution 2
By drawing the function, and similar to Solution 1, WLOG let $f(1)=f(5)=f(6)=12$ . Then, $f(2)=f(3)=f(7)$ . Set $g(x)+12=f(x)$ . Then the roots of $g(x)$ are $1,5,6$ . So, $g(x)=a(x-1)(x-5)(x-6)$ . Plug in $x=2$ to find a. We know \[-24=-12-12=f(2)-12=g(2)=a(1)(-3)(-4)=12a\] . So, $a=-2$ . Thus, $f(x)=g(x)+12=-2(x-1)(x-5)(x-6)+12$ , and then $|f(0)|=60+12=\boxed{072}$ .

## Solution 3
Without loss of generality, let $f(1) = 12$ . (If $f(1) = -12$ , then take $-f(x)$ as the polynomial, which leaves $|f(0)|$ unchanged.) Because $f$ is third-degree, write \[f(x) - 12 = a(x - 1)(x - b)(x - c)\] \[f(x) + 12 = a(x - d)(x - e)(x - f)\] where $\{b, c, d, e, f \}$ clearly must be a permutation of $\{2, 3, 5, 6, 7\}$ from the given condition. Thus $b + c + d + e + f = 2 + 3 + 5 + 6 + 7 = 23.$ However, subtracting the two equations gives $-24 = a[(x - 1)(x - b)(x - c) - (x - d)(x - e)(x - f)]$ , so comparing $x^2$ coefficients gives $1 + b + c = d + e + f$ and thus both values equal to $\dfrac{24}{2} = 12$ . As a result, $\{b, c \} = \{5, 6 \}$ . As a result, $-24 = a (12)$ and so $a = -2$ . Now, we easily deduce that $f(0) = (-2) \cdot (-1) \cdot (-5) \cdot (-6) + 12 = 72,$ and so removing the without loss of generality gives $|f(0)| = \boxed{072}$ , which is our answer.

## Solution 4
The following solution is similar to solution 3, but assumes nothing. Let $g(x)=(f(x))^2-144$ . Since $f$ has degree 3, $g$ has degree 6 and has roots 1,2,3,5,6, and 7. Therefore, $g(x)=k(x-1)(x-2)(x-3)(x-5)(x-6)(x-7)$ for some $k$ . Hence $|f(0)|=\sqrt{g(0)+144}=\sqrt{1260k+144}$ . Note that $g(x)=(f(x)+12)(f(x)-12)$ . Since $f$ has degree 3, so do $f(x)+12$ and $f(x)-12$ ; and both have the same leading coefficient. Hence $f(x)+12=a(x-q)(x-r)(x-s)$ and $f(x)-12=a(x-t)(x-u)(x-v)$ for some $a\neq 0$ (else $f$ is not cubic) where $\{q,r,s,t,u,v\}$ is the same as the set $\{1,2,3,5,6,7\}$ . Subtracting the second equation from the first, expanding, and collecting like terms, we have that \[24=a((t+u+v-(q+r+s))x^2-a(tu+uv+tv-(qr+qs+rs))x+a(tuv-qrs)\] which must hold for all $x$ . Since $a\neq 0$ we have that (1) $t+u+v=q+r+s$ , (2) $tu+uv+tv=qr+qs+rs$ and (3) $a(tuv-qrs)=24$ . Since $q+r+s+t+u+v$ is the sum of 1,2,3,5,6, and 7, we have $q+r+s+t+u+v=24$ so that by (1) we have $q+r+s=12$ and $t+u+v=12$ . We must partition 1,2,3,5,6,7 into 2 sets each with a sum of 12. Consider the set that contains 7. It can't contain 6 or 5 because the sum of that set would already be $\geq 12$ with only 2 elements. If 1 is in that set, the other element must be 4 which is impossible. Hence the two sets must be $\{2,3,7\}$ and $\{1,5,6\}$ . Note that each of these sets happily satisfy (2). By (3), since the sets have products 42 and 30 we have that $|a|=\frac{24}{|tuv-qrs|}=\frac{24}{12}=2$ . Since $a$ is the leading coefficient of $f(x)$ , the leading coefficient of $(f(x))^2$ is $a^2=|a|^2=2^2=4$ . Thus the leading coefficient of $g(x)$ is 4, i.e. $k=4$ . Then from earlier, $|f(0)|=\sqrt{g(0)+144}=\sqrt{1260k+144}=\sqrt{1260\cdot4+144}=\sqrt{5184}=72$ so that the answer is $\boxed{072}$ .

## Solution 5
Express $f(x)$ in terms of powers of $(x-4)$ : \[f(x) = a(x-4)^3 + b(x-4)^2 + c(x-4) + d\] By the same argument as in the first Solution, we see that $f(x)$ is an odd function about the line $x=4$ , so its coefficients $b$ and $d$ are 0. From there it is relatively simple to solve $f(2)=f(3)=-12$ (as in the above solution, but with a smaller system of equations): \[a(1)^3 + c(1) = -12\] \[a(2)^3 + c(2) = -12\] $a=2$ and $c=-14$ \[|f(0)| = |2(-4)^3 - 14(-4)| = \boxed{072}\]

## Solution 6 (Finite differences)
Because a cubic must come in a "wave form" with two points of inflection, we can see that $f(1)=f(5)=f(6)$ , and $f(2)=f(3)=f(7)$ . By symmetry, $f(4)=0$ . Now, WLOG let $f(1)=12$ , and $f(2)=f(3)=-12$ . Then, we can use finite differences to get that the third (constant) difference is $12$ , and therefore $f(0)=12+(24+(24+12))=\boxed{072}$ .

## Solution 7 (Like solution 1 without annoying systems)
We can rewrite our function as two different cubics, $f(x)=k(x-a)(x-b)(x-c)\pm12=k(x-d)(x-e)(x-f)\mp12$ . Note that $k$ is the same in both because they must be equal, so their leading terms must be. We must then, following Vieta's, choose our roots such that $a+b+c=d+e+f$ and verify that the other Vieta's formulas hold. Additionally, a cubic must only cross the x-axis thrice, restricting our choices for roots further. Choosing $a=1$ , $b=5$ , $c=6$ , $d=2$ , $e=3$ , $f=7$ yields: \[kx^3-12kx^2+41kx-30k\pm12=kx^3-12kx^2+41kx-42k\mp12\] For the constant terms to have a difference of 24 ( $|\pm12-\mp12|$ ), we must have $k=\pm2$ , so the constant term of our polynomial is $\pm72$ , the absolute value of which is $\boxed{072}$ . -- Solution by eiis1000

## Solution 8 (First few steps of solution 1)
We can rewrite the function as $f(x) - 12 = z(x-1)(x-5)(x-6)$ and $f(x) + 12 = z(x-2)(x-3)(x-7)$ . Since we need to find $|f(0)|$ , substitute 0 for x in these two equations.
\[f(0) - 12 = z(0-1)(0-5)(0-6), f(0) + 12 = z(0-2)(0-3)(0-7)\] \[f(0) - 12 = z\cdot -30, f(0) + 12 = z\cdot -42\] Isolating $z$ in both of the equations, \[z = \frac{f(0)-12}{-30}, z = \frac{f(0) + 12}{-42}\] Equating the two and solving for $f(0)$ , we see $|f(0)| = 72$ .
~YBSuburbanTea

## Solution 9 (Cheese Solution)
Let the leading coefficient of $f(x)$ be $a$ . Then, it is obvious that $(f(x) - 12)(f(x) + 12) = a^2(x - 1)(x - 2)(x - 3)(x - 5)(x - 6)(x - 7)$ . Let us now, let $x = 0$ . We then have, after cleaning it up nicely, $[f(0)]^2 = 2^2 * 3^2 * (35a^2 + 4)$ . We now take the square root of both sides, to obtain $|f(0)|$ . So, $|f(0)| = 6 * \sqrt{35a^2 + 4}$ . Now, this is the cheese part. Since this is aime, we know that the answer must be an integer, so we assume $a = 2$ . Thus, we get $|f(0)| = 6 * \sqrt{144} = 6 * 12 = 072$ .
~~triggod
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .