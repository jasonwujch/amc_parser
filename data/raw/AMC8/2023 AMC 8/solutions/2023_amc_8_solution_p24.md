# 2023 AMC 8 Problem 24

## Problem

Isosceles $\triangle ABC$ has equal side lengths $AB$ and $BC$ . In the figure below, segments are drawn parallel to $\overline{AC}$ so that the shaded portions of $\triangle ABC$ have the same area. The heights of the two unshaded portions are 11 and 5 units, respectively. What is the height of $h$ of $\triangle ABC$ ? (Diagram not drawn to scale.)

[asy] //Diagram by TheMathGuyd size(12cm); real h = 2.5; // height real g=4; //c2c space real s = 0.65; //Xcord of Hline real adj = 0.08; //adjust line diffs pair A,B,C; B=(0,h); C=(1,0); A=-conj(C); pair PONE=(s,h*(1-s)); //Endpoint of Hline ONE pair PTWO=(s+adj,h*(1-s-adj)); //Endpoint of Hline ONE path LONE=PONE--(-conj(PONE)); //Hline ONE path LTWO=PTWO--(-conj(PTWO)); path T=A--B--C--cycle; //Triangle fill (shift(g,0)*(LTWO--B--cycle),mediumgrey); fill (LONE--A--C--cycle,mediumgrey); draw(LONE); draw(T); label("$A$",A,SW); label("$B$",B,N); label("$C$",C,SE); draw(shift(g,0)*LTWO); draw(shift(g,0)*T); label("$A$",shift(g,0)*A,SW); label("$B$",shift(g,0)*B,N); label("$C$",shift(g,0)*C,SE); draw(B--shift(g,0)*B,dashed); draw(C--shift(g,0)*A,dashed); draw((g/2,0)--(g/2,h),dashed); draw((0,h*(1-s))--B,dashed); draw((g,h*(1-s-adj))--(g,0),dashed); label("$5$", midpoint((g,h*(1-s-adj))--(g,0)),UnFill); label("$h$", midpoint((g/2,0)--(g/2,h)),UnFill); label("$11$", midpoint((0,h*(1-s))--B),UnFill); [/asy]

$\textbf{(A) } 14.6 \qquad \textbf{(B) } 14.8 \qquad \textbf{(C) } 15 \qquad \textbf{(D) } 15.2 \qquad \textbf{(E) } 15.4$

## Solution 1
First, we notice that the smaller isosceles triangles are similar to the larger isosceles triangles. We can find that the area of the gray area in the first triangle is $[ABC]\cdot\left(1-\left(\tfrac{11}{h}\right)^2\right)$ . Similarly, we can find that the area of the gray part in the second triangle is $[ABC]\cdot\left(\tfrac{h-5}{h}\right)^2$ . These areas are equal, so $1-\left(\frac{11}{h}\right)^2=\left(\frac{h-5}{h}\right)^2$ . Simplifying yields $10h=146$ so $h=\boxed{\textbf{(A) }14.6}$ .
~MathFun1000 (~edits apex304)

## Solution 2
We can call the length of AC as $x$ . Therefore, the length of the base of the triangle with height $11$ is $11/h = a/x$ . Therefore, the base of the smaller triangle is $11x/h$ . We find that the area of the trapezoid is $(hx)/2 - 11^2x/2h$ .
Using similar triangles once again, we find that the base of the shaded triangle is $(h-5)/h = b/x$ . Therefore, the area is $(h-5)(hx-5x)/2h$ .
Since the areas are the same, we find that $(hx)/2 - 121x/2h = (h-5)(hx-5x)/2h$ . Multiplying each side by $2h$ , we get $h^2x - 121x = h^2x - 5hx - 5hx + 25x$ . Therefore, we can subtract $25x + h^2x$ from both sides, and get $-146x = -10hx$ . Finally, we divide both sides by $-x$ and get $10h = 146$ . $h$ is $\boxed{\textbf{(A)}14.6}$ .
Solution by CHECKMATE2021 (edits by Someone)

## Solution 3 (Faster)
Since the length of AC does not matter, we can assume the base of triangle ABC is $h$ . Therefore, the area of the trapezoid in the first diagram is $h^2/2 - \frac{11^2}{2}$ .
The area of the triangle in the second diagram is now $\frac{(h-5)^2}{2}$ .
Therefore, $\frac{h^2 - 11^2}{2} = \frac{(h-5)^2}{2}$ . Multiplying both sides by $2$ , we get $h^2 - 121 = h^2 - 10h + 25$ . Subtracting $h^2 + 25$ from both sides, we get $-146 = -10h$ and $h$ is $\boxed{\textbf{(A)}14.6}$ .
Solution by ILoveMath31415926535 , and CHECKMATE2021

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=2990 ~hsnacademy

## Video Solution by Math-X
https://youtu.be/Ku_c1YHnLt0?si=NHwA1x9STOJLG8IP&t=5349
~Math-X
https://youtu.be/uxyJGZ3ZYGE

## Video Solution (THINKING CREATIVELY!!!)
https://youtu.be/SVVSMcw1Xe8
~Education, the Study of Everything

## Video Solution 1 by OmegaLearn (Using Similar Triangles)
https://youtu.be/almtw4n-92A

## Video Solution 2 by SpreadTheMathLove(Using Area-Similarity Relaitionship)
https://www.youtube.com/watch?v=GTlkTwxSxgo

## Video Solution 3 by Magic Square (Using Similarity and Special Value)(best solution)
https://www.youtube.com/watch?v=-N46BeEKaCQ&t=1569s

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=3270

## Video Solution by WhyMath
https://youtu.be/roTSeCAehek
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=Ki4tPSGAapU&t=1593s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/GnlU-McyPXY
### See Also