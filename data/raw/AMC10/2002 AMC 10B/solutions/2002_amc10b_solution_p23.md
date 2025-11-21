# 2002 AMC 10B Problem 23

## Problem

Let $\{a_k\}$ be a sequence of integers such that $a_1=1$ and $a_{m+n}=a_m+a_n+mn,$ for all positive integers $m$ and $n.$ Then $a_{12}$ is

$\mathrm{(A) \ } 45\qquad \mathrm{(B) \ } 56\qquad \mathrm{(C) \ } 67\qquad \mathrm{(D) \ } 78\qquad \mathrm{(E) \ } 89$

## Solution 1
When $m=1$ , $a_{n+1}=1+a_n+n$ . Hence, \[a_{2}=1+a_1+1\] \[a_{3}=1+a_2+2\] \[a_{4}=1+a_3+3\] \[\dots\] \[a_{12}=1+a_{11}+11\] Adding these equations up, we have that $a_{12}=12+(1+2+3+...+11)=\boxed{\mathrm{(D) \ } 78}$
~AopsUser101

## Solution 2
Substituting $n=1$ into $a_{m+n}=a_m+a_n+mn$ : $a_{m+1}=a_m+a_{1}+m$ .
Since $a_1 = 1$ , $a_{m+1}=a_m+m+1$ .
Therefore, $a_m = a_{m-1} + m, a_{m-1}=a_{m-2}+(m-1), a_{m-2} = a_{m-3} + (m-2)$ , and so on until $a_2 = a_1 + 2$ .
Adding the Left Hand Sides of all of these equations gives $a_m + a_{m-1} + a_{m-2} + a_{m-3} + \cdots + a_2$ .
Adding the Right Hand Sides of these equations gives
$(a_{m-1} + a_{m-2} + a_{m-3} + \cdots + a_1) + (m + (m-1) + (m-2) + \cdots + 2)$ .
These two expressions must be equal; hence $a_m + a_{m-1} + a_{m-2} + a_{m-3} + \cdots + a_2 = (a_{m-1} + a_{m-2} + a_{m-3} + \cdots + a_1) + (m + (m-1) + (m-2) + \cdots + 2)$ and $a_m = a_1 + (m + (m-1) + (m-2) + \cdots + 2)$ .
Substituting $a_1 = 1$ : $a_m = 1 + (m + (m-1) + (m-2) + \cdots + 2) = 1+2+3+4+ \cdots +m = \frac{(m+1)(m)}{2}$ .
Thus we have a general formula for $a_m$ and substituting $m=12$ : $a_{12} = \frac{(13)(12)}{2} = (13)(6) = \boxed{\mathrm{(D)} 78}$ .

## Solution 3
We can literally just plug stuff in. No prerequisite is actually said in the sequence. Since $a_{m+n} = a_m+a_n +mn$ , we know $a_2=a_1+a_1+1\cdot1=1+1+1=3$ . After this, we can use $a_2$ to find $a_4$ . $a_4=a_2+a_2+2\cdot 2 = 3+3+4 = 10$ . Now, we can use $a_2$ and $a_4$ to find $a_6$ , or $a_6=a_4+a_2+4\cdot 2 = 10+3+8=21$ . Lastly, we can use $a_6$ to find $a_{12}$ . $a_{12} = a_6+a_6+6\cdot 6 = 21+21+36= \boxed{\mathrm{(D) \ } 78}$

## Solution 4
We can set $n$ equal to $m$ , so we can say that \[a_{m + m} = a_m + a_m + m*m\] \[a_{2m} = 2a_m + m^2\]
We set $2m = 12$ , we get $m = 6$ . \[a_{12} = 2a_6 + 36\]
We set $2m = 6$ m, we get $m = 3$ . \[a_6 = 2a_3 + 9\]
Solving for $a_3$ is easy, just direct substitution. \[a_2 = 1 + 1 + 1 = 3\] \[a_3 = a_{2 + 1} = 3 + 1 + 2 = 6\]
Substituting, we get \[a_6 = 2(6) + 9 = 21\] \[a_{12} = 2(21) + 36 = 78\]
Thus, the answer is $\boxed{D}$ .
~ euler123

## Solution 5
Note that the sequence of triangular numbers $T_n=1+2+3+...+n$ satisfies these conditions. It is immediately obvious that it satisfies $a_1=1$ , and $a_{m+n}=a_m+a_n+mn$ can be visually proven with the diagram below.
[asy] for(int i=5; i > 0; --i) { for(int j=0; j < i; ++j) { draw(circle((j+(5-i)/2,(5-i)*sqrt(3)/2),.2)); }; }; path m1 = brace((2,-.3),(0,-.3),.2); draw(m1); label("$m$",m1,S); path n1 = brace((4,-.3),(3,-.3),.2); draw(n1); label("$n$",n1,S); draw((-.2*sqrt(3),-.2)--(2+.2*sqrt(3),-.2)--(1,.4+sqrt(3))--cycle); label("$T_m$",(1,1/3*sqrt(3))); draw((3-.2*sqrt(3),-.2)--(4+.2*sqrt(3),-.2)--(3.5,.4+.5*sqrt(3))--cycle); label("$T_n$",(3.5,.5/3*sqrt(3))); path m2 = brace((2+.15*sqrt(3),.15+2*sqrt(3)),(3+.15*sqrt(3),.15+sqrt(3)),.2); draw(m2); label("$m$",m2,(.5*sqrt(3),.5)); path n2 = brace((1.5-.15*sqrt(3),.15+1.5*sqrt(3)),(2-.15*sqrt(3),.15+2*sqrt(3)),.2); draw(n2); label("$n$",n2,(-.5*sqrt(3),.5)); draw((2.5,-.4+.5*sqrt(3))--(3+.4/3*sqrt(3),sqrt(3))--(2,.4+2*sqrt(3))--(1.5-.4/3*sqrt(3),1.5*sqrt(3))--cycle); label("$mn$",(2.25,1.25*sqrt(3))); [/asy]
This means that we can use the triangular number formula $T_n = \frac{n(n+1)}{2}$ , so the answer is $T_{12} = \frac{12(12+1)}{2} = \boxed{\mathrm{(D) \ } 78}$ .
~ emerald_block

## Solution 6
Follow solution 4 with plugging in m=n, but for the last part since since the subscript is 2n, and we aren't given anything that has odd numbers ( without substitution into the original equation), we need to find two numbers that add up to 12, which result from the multiplication of two even numbers. We realize that 4+8 works, since 4=2x2 and 8=4x2. We then proceed in substituting n=2 and n=4 into the equation, then add to obtain 78. ~Charmainema07292010

## Solution 6 (Fast - Good for use in contest)
Find $a_2$ which is just \[a_2 = a_{1+1} = 1+1+1 = 3\] . Now, we can find $a_4$ and so on until $a_12$ . So here goes: \[a_4 = a_{2+2} = 3+3+4 = 10\] \[a_8 = a_{4+4} = 10+10+16 = 36\] \[a_{12} = a_{8+4} = 36+10+32 = \boxed{\mathrm{(D) \ } 78}\]
-jb2015007

## Video Solution
https://www.youtube.com/watch?v=zraGzYAh0uM ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .