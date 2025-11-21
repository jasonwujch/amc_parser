# 2003 AMC 10A Problem 16

## Problem

What is the units digit of $13^{2003}$ ?

$\mathrm{(A) \ } 1\qquad \mathrm{(B) \ } 3\qquad \mathrm{(C) \ } 7\qquad \mathrm{(D) \ } 8\qquad \mathrm{(E) \ } 9$

## Solution 1
$13^{2003}\equiv 3^{2003}\pmod{10}$
Since $3^4=81\equiv1\pmod{10}$ :
$3^{2003}=(3^{4})^{500}\cdot3^{3}\equiv1^{500}\cdot27\equiv7\pmod{10}$
Therefore, the units digit is $7 \Rightarrow\boxed{\mathrm{(C)}\ 7}$

## Solution 2 (Patterns)
Since we are looking for the units digit of $13^{2003}$ , we only have to focus on the units digit of the base (13) as none of the other digits of the base affect the units digit of the resulting value.
By testing the first few values or through previous knowledge, you might see that the units digit of exponents with base 3 follow this pattern: \[3^1=3\] \[3^2=9\] \[3^3=27\] \[3^4=81,\] giving us the rotation $3-9-7-1.$
As this cycle resets every time the index increases by 4, we know that this cycle ends on 2000, and starts once again on 2001. As our expression is raised to the power of 2003, we know that the units digit of our expression must end with the third term of our pattern: $7$ .
Therefore, the units digit of our expression is $7 \Rightarrow\boxed{\mathrm{(C)}\ 7}$
~ JinhoK
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .