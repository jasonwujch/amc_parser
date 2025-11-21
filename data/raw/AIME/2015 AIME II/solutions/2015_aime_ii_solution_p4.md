# 2015 AIME II Problem 4

## Problem

In an isosceles trapezoid, the parallel bases have lengths $\log 3$ and $\log 192$ , and the altitude to these bases has length $\log 16$ . The perimeter of the trapezoid can be written in the form $\log 2^p 3^q$ , where $p$ and $q$ are positive integers. Find $p + q$ .

## Solution
Call the trapezoid $ABCD$ with $AB$ as the smaller base and $CD$ as the longer. Let the point where an altitude intersects the larger base be $E$ , where $E$ is closer to $D$ .
Subtract the two bases and divide to find that $ED$ is $\log 8$ . The altitude can be expressed as $\frac{4}{3} \log 8$ . Therefore, the two legs are $\frac{5}{3} \log 8$ , or $\log 32$ .
The perimeter is thus $\log 32 + \log 32 + \log 192 + \log 3$ which is $\log 2^{16} 3^2$ . So $p + q = \boxed{018}$

## Solution 2 (gratuitous wishful thinking)
Set the base of the log as 2. Then call the trapezoid $ABCD$ with $CD$ as the longer base. Then have the two feet of the altitudes be $E$ and $F$ , with $E$ and $F$ in position from left to right respectively. Then, $CF$ and $ED$ are $\log 192 - \log 3 = \log 64$ (from the log subtraction identity. Then $CF=EF=3$ (isosceles trapezoid and $\log 64$ being 6. Then the 2 legs of the trapezoid is $\sqrt{3^2+4^2}=5=\log 32$ .
And we have the answer:
$\log 192 + \log 32 + \log 32 + \log 3 = \log(192 \cdot 32 \cdot 32 \cdot 3) = \log(2^6 \cdot 3 \cdot 2^5 \cdot 2^5 \cdot 3) = \log(2^{16} \cdot 3^2) \Rightarrow 16+2 = \boxed{18}$
-dragoon

## Solution 3
Let $ABCD$ be the trapezoid, where $\overline{AB} || \overline{CD}$ and $AB = \log 3$ and $CD = \log 192$ . Draw altitudes from $A$ and $B$ to $\overline{CD}$ with feet at $E$ and $F$ , respectively. $AB = \log 3$ , so $EF = \log 3$ . Now, we attempt to find $DE + FC$ , or what's left of $CD$ after we take out $EF$ . We make use of the two logarithmic rules:
\[\log(xy) = \log x + \log y\]
\[\log(x^a) = a\log(x)\]
\[CD = \log 192 = \log (3 \cdot 2^6) = \log 3 + \log(2^6) = \log 3 + 6\log 2\]
Thus, since $CD = DE + EF + FC = \log 3 + 6\log 2$ , $CD - EF = \log 3 + 6\log 2 - \log 3 = 6\log 2 = DE + FC$ .
Now, why was finding $DE + FC$ important? Absolutely no reason! Just kidding, lol 🤣 Now, we essentially "glue" triangles $\triangle DAE$ and $\triangle BFC$ together to get $\triangle XC'D'$ , where $X$ is the point where $A$ and $B$ became one. Note we can do this because $\triangle DAE$ and $\triangle BFC$ are both right triangles with a common leg length (the altitude of trapezoid $ABCD$ ).
Triangle $XC'D'$ has a base of $C'D'$ , which is just equal to $DE + FC = 6\log 2$ . It is equal to $DE + FC$ because when we brought triangles $\triangle DAE$ and $\triangle BFC$ together, the length of $CD$ was not changed except for taking out $EF$ .
$XC' = XD'$ since $AD = BC$ because the problem tells us we have an isosceles trapezoid. Drop and altitude from $X$ to $C'D'$ The altitude has length $\log 16 = 4\log 2$ . The altitude also bisects $C'D'$ since $\triangle XC'D'$ is isosceles. Let the foot of the altitude be $M$ . Then $MD' = 3\log 2$ (Remember that C'D' was $6\log 2$ , and then it got bisected by the altitude). Thus, the hypotenuse, $XD'$ must be $5\log 2$ from the Pythagorean Theorem or by noticing that you have a 3-4-5 right triangle with a similarity ratio of $\log 2$ . Since $XD' = XC' = BC = AD$ , $BC = AD = 5\log 2 = \log 2^5$ .
Now, we have $CD = \log (3 \cdot 2^6)$ , $AB = \log 3$ , and $BC = AD = \log 2^5$ . Thus, their sum is
\[\log (3 \cdot 2^6) + \log 3 + \log 2^5 + \log 2^5 = \log (2^16 \cdot 3^2)\]
Thus, $p + q = 16 + 2 = \boxed{18}$ . ~Extremelysupercooldude

## Solution 4
Let $a=\log2$ and $b=\log3$ so that the base lengths are $\log3=b$ and $\log192=\log(3\cdot64)=\log3+\log\left(2^6\right)=6a+b$ and the altitudes are $\log16=4a$ . Then we have the following picture:
[asy] import graph; unitsize(1cm); draw((0,0)--(3,4)--(9,4)--(12,0)--cycle); draw((3,4)--(3,0));draw((9,4)--(9,0)); label("$b$",(3,4)--(9,4),N); label("$6a+b$",(0,0)--(12,0),S); label("$b$",(0,0)--(12,0),N); label("$4a$", (3,0)--(3,4),W); label("$4a$", (9,0)--(9,4),E); [/asy]
Note that we have the two right triangles to the side; one of each of their bases is an altitude, which we know the length to be $4a$ . The length of the other base can be calculated as $\dfrac{(6a+b)-b}2=3a$ via simple isosceles trapezoid geometry; it is clear that each right triangle is actually a $3-4-5$ triangle, so we know their hypotenuses (and the remaining unknown sides of our original trapezoid) have length $5a$ (because of the $3a$ and $4a$ bases). Our answer is therefore $5a+5a+b+6a+b=16a+2b=16\log2+2\log3=\log\left(2^{16}3^2\right)$ ; $p+q=16+2=\boxed{018}$ . QED.
~Technodoggo

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=226s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .