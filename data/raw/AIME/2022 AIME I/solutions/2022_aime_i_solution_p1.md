# 2022 AIME I Problem 1

## Problem

Quadratic polynomials $P(x)$ and $Q(x)$ have leading coefficients $2$ and $-2,$ respectively. The graphs of both polynomials pass through the two points $(16,54)$ and $(20,53).$ Find $P(0) + Q(0).$

## Solution 1 (Linear Polynomials)
Let $R(x)=P(x)+Q(x).$ Since the $x^2$ -terms of $P(x)$ and $Q(x)$ cancel, we conclude that $R(x)$ is a linear polynomial.
Note that \begin{alignat*}{8} R(16) &= P(16)+Q(16) &&= 54+54 &&= 108, \\ R(20) &= P(20)+Q(20) &&= 53+53 &&= 106, \end{alignat*} so the slope of $R(x)$ is $\frac{106-108}{20-16}=-\frac12.$
It follows that the equation of $R(x)$ is \[R(x)=-\frac12x+c\] for some constant $c,$ and we wish to find $R(0)=c.$
We substitute $x=20$ into this equation to get $106=-\frac12\cdot20+c,$ from which $c=\boxed{116}.$
~MRENTHUSIASM

## Solution 2 (Quadratic Polynomials)
Let \begin{alignat*}{8} P(x) &= &2x^2 + ax + b, \\ Q(x) &= &\hspace{1mm}-2x^2 + cx + d, \end{alignat*} for some constants $a,b,c$ and $d.$
We are given that \begin{alignat*}{8} P(16) &= &512 + 16a + b &= 54, \hspace{20mm}&&(1) \\ Q(16) &= &\hspace{1mm}-512 + 16c + d &= 54, &&(2) \\ P(20) &= &800 + 20a + b &= 53, &&(3) \\ Q(20) &= &\hspace{1mm}-800 + 20c + d &= 53, &&(4) \end{alignat*} and we wish to find \[P(0)+Q(0)=b+d.\] We need to cancel $a$ and $c.$ Since $\operatorname{lcm}(16,20)=80,$ we subtract $4\cdot[(3)+(4)]$ from $5\cdot[(1)+(2)]$ to get \[b+d=5\cdot(54+54)-4\cdot(53+53)=\boxed{116}.\] ~MRENTHUSIASM

## Solution 3 (Similar to Solution 2)
Like Solution 2, we can begin by setting $P$ and $Q$ to the quadratic above, giving us \begin{alignat*}{8} P(16) &= &512 + 16a + b &= 54, \hspace{20mm}&&(1) \\ Q(16) &= &\hspace{1mm}-512 + 16c + d &= 54, &&(2) \\ P(20) &= &800 + 20a + b &= 53, &&(3) \\ Q(20) &= &\hspace{1mm}-800 + 20c + d &= 53, &&(4) \end{alignat*} We can first add $(1)$ and $(2)$ to obtain $16(a-c) + (b+d) = 108.$
Next, we can add $(3)$ and $(4)$ to obtain $20(a-c) + (b+d) = 106.$ By subtracting these two equations, we find that $4(a-c) = -2,$ so substituting this into equation $[(1) + (2)],$ we know that $4 \cdot (-2) + (b+d) = 108,$ so therefore $b+d = \boxed{116}.$
~jessiewang28

## Solution 4 (Brute Force)
Let \begin{alignat*}{8} P(x) &= &2x^2 + ax + b, \\ Q(x) &= &\hspace{1mm}-2x^2 + cx + d, \end{alignat*} By substituting $(16, 54)$ and $(20, 53)$ into these equations, we can get: \begin{align*} 2(16)^2 + 16a + b &= 54, \\ 2(20)^2 + 20a + b &= 53. \end{align*} Hence, $a = -72.25$ and $b = 698.$
Similarly, \begin{align*} -2(16)^2 + 16c + d &= 54, \\ -2(20)^2 + 20c + d &= 53. \end{align*} Hence, $c = 71.75$ and $d = -582.$
Notice that $b = P(0)$ and $d = Q(0).$ Therefore \[P(0) + Q(0) = 698 + (-582) = \boxed{116}.\] ~Littlemouse

## Solution 5
Add the equations of the polynomials $y=2x^2+ax+b$ and $y=-2x^2+cx+d$ to get $2y=(a+c)x+(b+d)$ . This equation must also pass through the two points $(16,54)$ and $(20,53)$ .
Let $m=a+c$ and $n=b+d$ . We then have two equations: \begin{align*} 108&=16m+n, \\ 106&=20m+n. \end{align*} We are trying to solve for $n=P(0)$ . Using elimination: \begin{align*} 540&=80m+5n, \\ 424&=80m+4n. \end{align*} Subtracting both equations, we find that $n=\boxed{116}$ .
~eevee9406

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=sUfbEBCQ6RY

## Video Solution by MRENTHUSIASM (English & Chinese)
https://www.youtube.com/watch?v=XcS5qcqsRyw&ab_channel=MRENTHUSIASM
~MRENTHUSIASM

## Video Solution
https://youtu.be/MJ_M-xvwHLk?t=7
~ThePuzzlr

## Video Solution
https://youtu.be/eDZUzvwt4SE
~savannahsolver

## Video Solution
https://youtu.be/D3sSHlZQIlE
~AMC & AIME Training
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .