# 2020 AIME II Problem 11

## Problem

Let $P(x) = x^2 - 3x - 7$ , and let $Q(x)$ and $R(x)$ be two quadratic polynomials also with the coefficient of $x^2$ equal to $1$ . David computes each of the three sums $P + Q$ , $P + R$ , and $Q + R$ and is surprised to find that each pair of these sums has a common root, and these three common roots are distinct. If $Q(0) = 2$ , then $R(0) = \frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Let $Q(x) = x^2 + ax + 2$ and $R(x) = x^2 + bx + c$ . We can write the following: \[P + Q = 2x^2 + (a - 3)x - 5\] \[P + R = 2x^2 + (b - 3)x + (c - 7)\] \[Q + R = 2x^2 + (a + b)x + (c + 2)\] Let the common root of $P+Q,P+R$ be $r$ ; $P+R,Q+R$ be $s$ ; and $P+Q,Q+R$ be $t$ . We then have that the roots of $P+Q$ are $r,t$ , the roots of $P + R$ are $r, s$ , and the roots of $Q + R$ are $s,t$ .
By Vieta's, we have: \[r + t = \dfrac{3 - a}{2}\tag{1}\] \[r + s = \dfrac{3 - b}{2}\tag{2}\] \[s + t = \dfrac{-a - b}{2}\tag{3}\] \[rt = \dfrac{-5}{2}\tag{4}\] \[rs = \dfrac{c - 7}{2}\tag{5}\] \[st = \dfrac{c + 2}{2}\tag{6}\]
Subtracting $(3)$ from $(1)$ , we get $r - s = \dfrac{3 + b}{2}$ . Adding this to $(2)$ , we get $2r = 3 \implies r = \dfrac{3}{2}$ . This gives us that $t = \dfrac{-5}{3}$ from $(4)$ . Substituting these values into $(5)$ and $(6)$ , we get $s = \dfrac{c-7}{3}$ and $s = \dfrac{-3c - 6}{10}$ . Equating these values, we get $\dfrac{c-7}{3} = \dfrac{-3c-6}{10} \implies c = \dfrac{52}{19} = R(0)$ . Thus, our answer is $52 + 19 = \boxed{071}$ . ~ TopNotchMath

## Solution 2
We know that $P(x)=x^2-3x-7$ .
Since $Q(0)=2$ , the constant term in $Q(x)$ is $2$ . Let $Q(x)=x^2+ax+2$ .
Finally, let $R(x)=x^2+bx+c$ .
$P(x)+Q(x)=2x^2+(a-3)x-5$ . Let its roots be $p$ and $q$ .
$P(x)+R(x)=2x^2+(b-3)x+(c-7)$ Let its roots be $p$ and $r$ .
$Q(x)+R(x)=2x^2+(a+b)x+(c+2)$ . Let its roots be $q$ and $r$ .
By vietas, $p+q=\frac{3-a}{2}, p+r=\frac{3-b}{2}, q+r=\frac{-(a+b)}{2}$
We could work out the system of equations, but it's pretty easy to see that $p=\frac32, q=-\frac{a}{2}, r=-\frac{b}{2}$ .
$\text{Again, by vietas, }pq=-\frac52\text{, } pr=\frac{c-7}{2}\text{, } qr=\frac{c+2}{2}\text{, } \text{multiplying everything together a}\text{nd taking the sqrt of both sides,}$ \[(pqr)^2=\left(-\frac52\right)\left(\frac{c-7}{2}\right)\left(\frac{c+2}{2}\right)\] \[pqr=\sqrt{\left(-\frac52\right)\left(\frac{c-7}{2}\right)\left(\frac{c+2}{2}\right)}\] $\text{Dividing this }\text{equation by }qr=\frac{c+2}{2}$ \[\frac{pqr}{qr}=\frac{\sqrt{\left(-\frac52\right)\left(\frac{c-7}{2}\right)\left(\frac{c+2}{2}\right)}}{\frac{c+2}{2}}\] \[p = \frac{\sqrt{\left(-\frac52\right)\left(\frac{c-7}{2}\right)}}{\sqrt{\frac{c+2}{2}}}\] $\text{Recall th}\text{at }p=\frac32 \text{ and square both sides}$ \[\frac94=\frac{\left(-\frac52\right)\left(\frac{c-7}{2}\right)}{\frac{c+2}{2}}\] $\text{Solving gives } c=\frac{52}{19}, \text{ so our answer is }\boxed{071}$
~quacker88

## Solution 3 (Official MAA)
Let the common root of $P+Q$ and $P+R$ be $p$ , the common root of $P+Q$ and $Q+R$ be $q$ , and the common root of $Q+R$ and $P+R$ be $r$ . Because $p$ and $q$ are both roots of $P+Q$ and $P+Q$ has leading coefficient $2$ , it follows that $P(x) + Q(x) = 2(x-p)(x-q).$ Similarly, $P(x) + R(x) = 2(x-p)(x-r)$ and $Q(x) + R(x) = 2(x-q)(x-r)$ . Adding these three equations together and dividing by $2$ yields \[P(x) + Q(x) + R(x) = (x-p)(x-q) + (x-p)(x-r) + (x-q)(x-r),\] so \[P(x) = (P(x) + Q(x) + R(x)) - (Q(x) + R(x))\] \[= (x-p)(x-q) + (x-p)(x-r) - (x-q)(x-r)\] \[= x^2 - 2px + (pq + pr - qr).\] Similarly, \[Q(x) = x^2 - 2qx + (pq + qr - pr) \text{~ and}\] \[R(x) = x^2 - 2rx + (pr + qr - pq).\] Comparing the $x$ coefficients yields $p = \tfrac32$ , and comparing the constant coefficients yields $-7 = pq + pr - qr = \tfrac32(q+r) - qr$ . The fact that $Q(0) = 2$ implies that $\tfrac32(q-r) + qr = 2$ . Adding these two equations yields $q = -\tfrac53$ , and so substituting back in to solve for $r$ gives $r=-\tfrac{27}{19}$ . Finally, \[R(0) = pr + qr - pq = \left(-\frac{27}{19}\right)\left(\frac32-\frac53\right) + \frac52 = \frac{9}{38} + \frac52 = \frac{52}{19}.\] The requested sum is $52 + 19 = 71$ . Note that $Q(x) = x^2 + \frac{10}3x + 2$ and $R(x) = x^2 + \frac{54}{19}x + \frac{52}{19}$ .

## Video Solution
https://youtu.be/BQlab3vjjxw ~ CNCM
Another one:
https://www.youtube.com/watch?v=AXN9x51KzNI
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .