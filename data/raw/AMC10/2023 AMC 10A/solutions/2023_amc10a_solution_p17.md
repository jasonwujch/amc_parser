# 2023 AMC 10A Problem 17

## Problem

Let $ABCD$ be a rectangle with $AB = 30$ and $BC = 28$ . Point $P$ and $Q$ lie on $\overline{BC}$ and $\overline{CD}$ respectively so that all sides of $\triangle{ABP}, \triangle{PCQ},$ and $\triangle{QDA}$ have integer lengths. What is the perimeter of $\triangle{APQ}$ ?

$\textbf{(A) } 84 \qquad \textbf{(B) } 86 \qquad \textbf{(C) } 88 \qquad \textbf{(D) } 90 \qquad \textbf{(E) } 92$

## Solution 1 (Testing Pythagorean Triples)
[asy] /* ~ItsMeNoobieboy */ size(200); pair A, B, C, D, P, Q; A = (0,28/30); B = (1,28/30); C = (1,0); D = (0,0); P = (1,12/30); Q = (21/30,0); draw(A--B--C--D--cycle); draw(A--P--Q--cycle); dot("$A$",A,NW,linewidth(4)); dot("$B$",B,NE,linewidth(4)); dot("$C$",C,SE,linewidth(4)); dot("$D$",D,SW,linewidth(4)); dot("$P$",P,E,linewidth(4)); dot("$Q$",Q,S,linewidth(4)); label("$30$",midpoint(A--B),N); label("$16$",midpoint(B--P),E); label("$34$",midpoint(A--P),NE, red); label("$28$",midpoint(A--D),W); label("$21$",midpoint(D--Q),S); label("$35$",midpoint(A--Q),SW, red); label("$9$",midpoint(Q--C),S); label("$12$",midpoint(C--P),E); label("$15$",midpoint(Q--P),SE, red); [/asy]
We know that all side lengths are integers, so we can test Pythagorean triples for all triangles.
First, we focus on $\triangle{ABP}$ . The length of $AB$ is $30$ , and the possible (small enough) Pythagorean triples $\triangle{ABP}$ can be are $(3, 4, 5), (5, 12, 13), (8, 15, 17),$ where the length of the longer leg is a factor of $30$ . Testing these, we get that only $(8, 15, 17)$ is a valid solution. Thus, we know that $BP = 16$ and $AP = 34$ .
Next, we move on to $\triangle{QDA}$ . The length of $AD$ is $28$ , and the small enough triples are $(3, 4, 5)$ and $(7, 24, 25)$ . Testing again, we get that $(3, 4, 5)$ is our triple. We get the value of $DQ = 21$ , and $AQ = 35$ .
We know that $CQ = CD - DQ$ which is $9$ , and $CP = BC - BP$ which is $12$ . $\triangle{CPQ}$ is therefore a right triangle with side length ratios ${3, 4, 5}$ , and the hypotenuse is equal to $15$ . $\triangle{APQ}$ has side lengths $34, 35,$ and $15,$ so the perimeter is equal to $34 + 35 + 15 = \boxed{\textbf{(A) } 84}.$
~Gabe Horn ~ItsMeNoobieboy ~oinava

## Solution 2
Let $BP=y$ and $AP=z$ . We get $30^{2}+y^{2}=z^{2}$ . Subtracting $y^{2}$ on both sides, we get $30^{2}=z^{2}-y^{2}$ . Factoring, we get $30^{2}=(z-y)(z+y)$ . Since $y$ and $z$ are integers, both $z-y$ and $z+y$ have to be even or both have to be odd. We also have $y<31$ . We can pretty easily see now that $z-y=18$ and $z+y=50$ . Thus, $y=16$ and $z=34$ . We now get $CP=12$ . We do the same trick again. Let $DQ=a$ and $AQ=b$ . Thus, $28^{2}=(b+a)(b-a)$ . We can get $b+a=56$ and $b-a=14$ . Thus, $b=35$ and $a=21$ . We get $CQ=9$ and by the Pythagorean Theorem, we have $PQ=15$ . We get $AP+PQ+AQ=34+15+35=84$ . Our answer is $\boxed{\textbf{(A) } 84}.$
If you want to see a video solution on this solution, look at Video Solution 1.
-paixiao (minor edits-HW73)

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=FPZ1D4hdcd1QGUK2&t=3834 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=KfPIbpJjHwZQTyH4&t=4479
~Math-X

## Video Solution 🚀 2 min solve 🚀
https://youtu.be/HVMlhdSurPw
~Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=bN7Ly70nw_M

## Video Solution by OmegaLearn
https://youtu.be/xlFDMuoOd5Q?si=nCVTriSViqfHA2ju

## Video Solution
https://www.youtube.com/watch?v=RiUlGz-p-LU&t=71s

## Video Solution by CosineMethod
https://www.youtube.com/watch?v=r8Wa8OrKiZI

## VIdeo Solution 2
https://youtu.be/yxfRjwQ8_KM
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .