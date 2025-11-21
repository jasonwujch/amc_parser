# 2005 AMC 10A Problem 25

## Problem

In $\triangle ABC$ we have $AB = 25$ , $BC = 39$ , and $AC = 42$ . Points $D$ and $E$ are on $\overline{AB}$ and $\overline{AC}$ respectively, with $AD = 19$ and $AE = 14$ . What is the ratio of the area of triangle $ADE$ to the area of the quadrilateral $BCED$ ?

$\textbf{(A) } \frac{266}{1521}\qquad \textbf{(B) } \frac{19}{75}\qquad \textbf{(C) } \frac{1}{3}\qquad \textbf{(D) } \frac{19}{56}\qquad \textbf{(E) } 1$

## Solution 1
We have \[\frac{[ADE]}{[ABC]} = \frac{AD}{AB} \cdot \frac{AE}{AC} = \frac{19}{25} \cdot \frac{14}{42} = \frac{19}{75}.\]
(Area of a triangle is base times height, so the area ratio of triangles, that have a common vertex (height) and bases on a common line, is the base length ratio. This is applied twice, using different pairs of bases, and corresponding altitudes for height.).
[asy] unitsize(0.15 cm); pair A, B, C, D, E; A = (191/39,28*sqrt(1166)/39); B = (0,0); C = (39,0); D = (6*A + 19*B)/25; E = (28*A + 14*C)/42; draw(A--B--C--cycle); draw(D--E); label("$A$", A, N); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, W); label("$E$", E, NE); label("$19$", (A + D)/2, W); label("$6$", (B + D)/2, W); label("$14$", (A + E)/2, NE); label("$28$", (C + E)/2, NE); [/asy]
$[BCED] = [ABC] - [ADE]$ , so \begin{align*} \frac{[ADE]}{[BCED]} &= \frac{[ADE]}{[ABC] - [ADE]} \\ &= \frac{1}{\frac{ABC}{ADE} - 1} \\ &= \frac{1}{\frac{75}{19} - 1} \\ &= \boxed{\textbf{(D) }\frac{19}{56}}. \end{align*}
Note: If it is hard to understand why \[\frac{[ADE]}{[ABC]} = \frac{AD}{AB} \cdot \frac{AE}{AC}\] , you can use the fact that the area of a triangle equals $\frac{1}{2} \cdot ab \cdot \sin(C)$ . If angle $DAE = Z$ , we have that \[\frac{[ADE]}{[ABC]} = \frac{\frac{1}{2} \cdot 19 \cdot 14 \cdot \sin(Z)}{\frac{1}{2} \cdot 25 \cdot 42 \cdot \sin(Z)} = \frac{19 \cdot 14}{25 \cdot 42} = \frac{ab}{cd}\] .

## Video Solution
https://youtu.be/VXyOJWcpi00

## Solution 2
[asy] unitsize(0.15 cm); pair A, B, C, D, E; A = (191/39,28*sqrt(1166)/39); B = (0,0); C = (39,0); D = (6*A + 19*B)/25; E = (28*A + 14*C)/42; draw(A--B--C--cycle); draw(D--E); label("$A$", A, N); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, W); label("$E$", E, NE); label("$19$", (A + D)/2, W); label("$6$", (B + D)/2, W); label("$14$", (A + E)/2, NE); label("$28$", (C + E)/2, NE); [/asy]
We can let $[ADE]=x$ . Since $EC=2 \cdot EA$ , $[DEC]=2x$ . So, $[ADC]=3x$ . This means that $[BDC]=\frac{6}{19}\cdot3x=\frac{18x}{19}$ . Thus, $\frac{[ADE]}{[BCED]} = \frac{x}{\frac{18x}{19}+2x}= \boxed{\textbf{(D) }\frac{19}{56}}.$
-Conantwiz2023

## Solution 3 (trig)
The area of a triangle is $\frac{1}{2} bc\sin A$ .
Using this formula:
$[ADE]=\frac{1}{2}\cdot19\cdot14\cdot\sin A = 133\sin A$
$[ABC]=\frac{1}{2}\cdot25\cdot42\cdot\sin A = 525\sin A$
Since the area of $BCED$ is equal to the area of $ABC$ minus the area of $ADE$ ,
$[BCED] = 525\sin A - 133\sin A = 392\sin A$ .
Therefore, the desired ratio is $\frac{133\sin A}{392\sin A}=\boxed{\textbf{(D) }\frac{19}{56}}$
Note: $BC=39$ was not used in this solution.

## Solution 4
Let $F$ be on $AC$ such that $DE\parallel BF$ then we have \[\frac{[ADE]}{[ABF]}=\left(\frac{AD}{AB}\right)^2=\left(\frac{19}{25}\right)^2=\frac{361}{625}\] \[\frac{[ADE]}{[DEFB]}=\frac{361}{625-361}=\frac{361}{364}\] Since $\bigtriangleup ADE\sim\bigtriangleup ABF$ we have \[\frac{AD}{AE}=\frac{DB}{EF}\Longrightarrow EF=\frac{84}{19}\] Thus $FC=EC-EF=\frac{448}{19}$ and \[\frac{[ABF]}{[BFC]}=\frac{AF}{FC}=\frac{350}{448}\] \[\frac{[ADE]}{[BFC]}=\left(\frac{[ADE]}{[ABF]}\right)\left(\frac{[ABF]}{[BFC]}\right)=\left(\frac{361}{625}\right)\left(\frac{350}{448}\right)=\frac{126350}{280000}\] Finally, after some calculations, \[\frac{[ADE]}{[DECB]}=\frac{[ADE]}{[BFC]+[DECB]}=\boxed{\textbf{(D) \ } \frac{19}{56}}\] .
~ Nafer
~ LaTeX changes by tkfun

## Solution 5
Let the area of triangle ABC be denoted by [ABC] and the area of quadrilateral ABCD be denoted by [ABCD].
\[\text{Diagram:}\] [asy] unitsize(0.15 cm); pair A, B, C, D, E; A = (191/39,28*sqrt(1166)/39); B = (0,0); C = (39,0); D = (6*A + 19*B)/25; E = (28*A + 14*C)/42; draw(A--B--C--cycle); draw(D--E); label("$A$", A, N); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, W); label("$E$", E, NE); label("$19$", (A + D)/2, W); label("$6$", (B + D)/2, W); label("$14$", (A + E)/2, NE); label("$28$", (C + E)/2, NE); [/asy]
Let the area of $\triangle ABC$ be $x$ . $\triangle ABE$ and $\triangle BEC$ share a height, and the ratio of their bases are $1:2$ , so the area of $\triangle ABE$ is $\frac{x}{3}$ .
Similarly, $\triangle AED$ and $\triangle DEB$ share a height, and the ratio of their bases is $19:6$ , so the ratio of $\frac{[AED]}{[AEB]}=\frac{19}{25}$ . Therefore, \[[AED]=\frac{19}{25}\cdot\left[AEB\right]=\frac{19}{25}\cdot\frac{1}{3}\cdot\left[ABC\right]=\frac{19}{25}\cdot\frac{1}{3}\cdot x=\frac{19}{75}x\] \[[DECB]=[ABC]-[AED]=x-\frac{19}{75}x=\frac{56}{75}x\] The ratio $\frac{[AED]}{[DECB]}=\frac{\frac{19}{75}}{\frac{56}{75}}=\frac{19}{56}$ which is answer choice $\boxed{\textbf{(D) } \frac{19}{56}}$ .
~JH. L
These problems are copyrighted © by the Mathematical Association of America. https://ivyleaguecenter.files.wordpress.com/2017/11/amc-10-picture.jpg
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
https://ivyleaguecenter.files.wordpress.com/2017/11/amc-10-picture.jpg