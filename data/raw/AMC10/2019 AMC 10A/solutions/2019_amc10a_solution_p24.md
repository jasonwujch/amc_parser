# 2019 AMC 10A Problem 24

## Problem

Let $p$ , $q$ , and $r$ be the distinct roots of the polynomial $x^3 - 22x^2 + 80x - 67$ . It is given that there exist real numbers $A$ , $B$ , and $C$ such that \[\dfrac{1}{s^3 - 22s^2 + 80s - 67} = \dfrac{A}{s-p} + \dfrac{B}{s-q} + \frac{C}{s-r}\] for all $s\not\in\{p,q,r\}$ . What is $\tfrac1A+\tfrac1B+\tfrac1C$ ?

$\textbf{(A) }243\qquad\textbf{(B) }244\qquad\textbf{(C) }245\qquad\textbf{(D) }246\qquad\textbf{(E) } 247$

## Solution 1
Multiplying both sides by $(s-p)(s-q)(s-r)$ yields \[1 = A(s-q)(s-r) + B(s-p)(s-r) + C(s-p)(s-q)\] As this is a polynomial identity, and it is true for infinitely many $s$ , it must be true for all $s$ (since a polynomial with infinitely many roots must in fact be the constant polynomial $0$ ). This means we can plug in $s = p$ to find that $\frac1A = (p-q)(p-r)$ . Similarly, we can find $\frac1B = (q-p)(q-r)$ and $\frac1C = (r-p)(r-q)$ . Summing them up, we get that \[\frac1A + \frac1B + \frac1C = p^2 + q^2 + r^2 - pq - qr - pr\] We can express $p^2 + q^2 + r^2 = (p+q+r)^2 - 2(pq + qr + pr)$ , and by Vieta's Formulas, we know that this expression is equal to $484$ . Vieta's also gives $pq + qr + pr = 80$ (which we also used to find $p^2+q^2+r^2$ ), so the answer is $484 -240 = \boxed{\textbf{(B) } 244}$ .
Note : this process of substituting in the 'forbidden' values in the original identity is a standard technique for partial fraction decomposition, as taught in calculus classes.
-very small latex edit from countmath1 :)
Minor rephrasing for correctness and clarity ~ Technodoggo

## Solution 2 (Pure Elementary Algebra)
Solution 1 uses a trick from Calculus that seemingly contradicts the restriction $s\not\in\{p,q,r\}$ . Here is a solution with pure elementary algebra. \[A(s-q)(s-r) + B(s-p)(s-r) + C(s-p)(s-q)=1\] \[s^2(A+B+C)-s(Aq+Ar+Bp+Br+Cp+Cq)+(Aqr+Bpr+Cpq-1)=0\] \[\begin{cases} A+B+C=0 & (1)\\ Aq+Ar+Bp+Br+Cp+Cq=0 & (2)\\ Aqr+Bpr+Cpq=1 & (3) \end{cases}\] From $(1)$ we get $A=-(B+C)$ , $B=-(A+C)$ , $C=-(A+B)$ , substituting them in $(2)$ , we get $Ap + Bq + Cr=0$ $(4)$
$(4)- (1) \cdot r$ , $A(p-r)+B(q-r)=0$ $(5)$
$(3) - (1) \cdot pq$ , $Aq(r-p)+Bp(r-q)=1$ $(6)$
$(6) + (5) \cdot p$ , $A(r-p)(q-p)=1$
$A = \frac{1}{(r-p)(q-p)}$ , by symmetry, $B = \frac{1}{(r-q)(p-q)}$ , $C = \frac{1}{(q-r)(p-r)}$
The rest is similar to solution 1, we get $\boxed{\textbf{(B) } 244}$
~Mathman645: Honestly. this solution isn't even that hard to understand, but the way you factored the initial expression is kinda weird and misleading.
~ isabelchen

## Video Solution by Richard Rusczyk
https://www.youtube.com/watch?v=GI5d2ZN8gXY

## Video Solution by TheBeautyofMath
https://youtu.be/zw5CCPcT5IU
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .