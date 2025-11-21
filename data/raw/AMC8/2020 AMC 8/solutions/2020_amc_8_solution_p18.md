# 2020 AMC 8 Problem 18

## Problem

Rectangle $ABCD$ is inscribed in a semicircle with diameter $\overline{FE},$ as shown in the figure. Let $DA=16,$ and let $FD=AE=9.$ What is the area of $ABCD?$

[asy] draw(arc((0,0),17,180,0)); draw((-17,0)--(17,0)); fill((-8,0)--(-8,15)--(8,15)--(8,0)--cycle, 1.5*grey); draw((-8,0)--(-8,15)--(8,15)--(8,0)--cycle); dot("$A$",(8,0), 1.25*S); dot("$B$",(8,15), 1.25*N); dot("$C$",(-8,15), 1.25*N); dot("$D$",(-8,0), 1.25*S); dot("$E$",(17,0), 1.25*S); dot("$F$",(-17,0), 1.25*S); label("$16$",(0,0),N); label("$9$",(12.5,0),N); label("$9$",(-12.5,0),N); [/asy] $\textbf{(A) }240 \qquad \textbf{(B) }248 \qquad \textbf{(C) }256 \qquad \textbf{(D) }264 \qquad \textbf{(E) }272$

## Solution 1 (Pythagorean Theorem)
[asy] draw(arc((0,0),17,180,0)); draw((-17,0)--(17,0)); fill((-8,0)--(-8,15)--(8,15)--(8,0)--cycle, 1.5*grey); draw((-8,0)--(-8,15)--(8,15)--(8,0)--cycle); dot("$A$",(8,0), 1.25*S); dot("$B$",(8,15), 1.25*N); dot("$C$",(-8,15), 1.25*N); dot("$D$",(-8,0), 1.25*S); dot("$E$",(17,0), 1.25*S); dot("$F$",(-17,0), 1.25*S); label("$16$",(0,0),N); label("$9$",(12.5,0),N); label("$9$",(-12.5,0),N); dot("$O$", (0,0), 1.25*S); draw((0,0)--(-8,15));[/asy]
Let $O$ be the center of the semicircle. The diameter of the semicircle is $9+16+9=34$ , so $OC = 17$ . By symmetry, $O$ is the midpoint of $DA$ , so $OD=OA=\frac{16}{2}= 8$ . By the Pythagorean theorem in right-angled triangle $ODC$ (or $OBA$ ), we have that $CD$ (or $AB$ ) is $\sqrt{17^2-8^2}=15$ . Accordingly, the area of $ABCD$ is $16\cdot 15=\boxed{\textbf{(A) }240}$ .

## Solution 2 (Coordinate Geometry)
Let the midpoint of segment $FE$ be the origin. Evidently, point $D=(-8,0)$ and $A=(8,0)$ . Since points $C$ and $B$ share $x$ -coordinates with $D$ and $A$ respectively, it suffices to find the $y$ -coordinate of $B$ (which will be the height of the rectangle) and multiply this by $DA$ (which we know is $16$ ). The radius of the semicircle is $\frac{9+16+9}{2} = 17$ , so the whole circle has equation $x^2+y^2=289$ ; as already stated, $B$ has the same $x$ -coordinate as $A$ , i.e. $8$ , so substituting this into the equation shows that $y=\pm15$ . Since $y>0$ at $B$ , the y-coordinate of $B$ is $15$ . Therefore, the answer is $16\cdot 15 = \boxed{\textbf{(A) }240}$ .
(Note that the synthetic solution (Solution 1) is definitely faster and more elegant. However, this is the solution that you should use if you can't see any other easier strategy.)

## Solution 3
We can use a result from the Art of Problem Solving Introduction to Algebra book Sidenote: for a semicircle with diameter $(1+n)$ , such that the $1$ part is on one side and the $n$ part is on the other side, the height from the end of the $1$ side (or the start of the $n$ side) is $\sqrt{n}$ . To use this formula, we scale the figure down by $9$ ; this will give the height a length of $\sqrt{\frac{16+9}{9}} = \sqrt{\frac{25}{9}} = \frac{5}{3}$ . Now, scaling back up by $9$ , the height $DC$ is $9 \cdot \frac{5}{3} = 15$ . The answer is then $15 \cdot 16 = \boxed{\textbf{(A) }240}$ . - SweetMango77

## Solution 4 (Power of a Point Theorem)
Draw the other half of the circle as follows: [asy] draw(arc((0,0),17,360,0)); draw((-17,0)--(17,0)); fill((-8,0)--(-8,15)--(8,15)--(8,0)--cycle, 1.5*grey); draw((-8,0)--(-8,15)--(8,15)--(8,0)--cycle); dot("$A$",(8,0), 1.25*SE); dot("$B$",(8,15), 1.25*N); dot("$C$",(-8,15), 1.25*N); dot("$D$",(-8,0), 1.25*SW); dot("$E$",(17,0), 1.25*E); dot("$F$",(-17,0), 1.25*W); label("$16$",(0,0),N); label("$9$",(12.5,0),N); label("$9$",(-12.5,0),N); draw((-8,-15)--(-8,0)--(8,0)--(8,-15)--cycle); dot("$B'$",(8,-15), 1.25*S); dot("$C'$",(-8,-15), 1.25*S); [/asy] By the Power of a Point Theorem , $FD\cdot DE = CD\cdot C'D$ . By symmetry, $CD = C'D$ . We see that $FD = 9$ and $DE = 16 + 9 = 25$ . Substituting in these values, $9\cdot 25 = CD^2$ , giving $CD^2 = 225$ and $CD = 15$ . The area of the rectangle is therefore $15\cdot 16 = \boxed{\textbf{(A) }240}$ .

## Solution 5 (Vertical Theorem)
[asy] draw(arc((0,0),17,180,0)); draw((-17,0)--(17,0)); fill((-8,0)--(-8,15)--(8,15)--(8,0)--cycle, 1.5*grey); draw((-8,0)--(-8,15)--(8,15)--(8,0)--cycle); dot("$A$",(8,0), 1.25*S); dot("$B$",(8,15), 1.25*N); dot("$C$",(-8,15), 1.25*N); dot("$D$",(-8,0), 1.25*S); dot("$E$",(17,0), 1.25*S); dot("$F$",(-17,0), 1.25*S); label("$16$",(0,0),S); label("$9$",(12.5,0),N); label("$9$",(-12.5,0),N); dot("$G$", (0,15), SE); dot("$O$", (0,0), NE); draw((0,0)--(0, 15)); draw((-7.5,15)--(0,0)); [/asy]
According to the Pythagorean Theorem and the Vertical Theorem, we can find out that $OG=\sqrt{\left(\frac{2\times9+16}{2}\right)^2 - \left(\frac{16}{2}\right)^2}=15$ . Therefore, the answer is $15\times16=\boxed{\textbf{(A) }240}$ ;
~ Bloggish

## Video Solution by Mathionaire (Clear and fast explanation)
https://www.youtube.com/watch?v=P1xjpqm9_DQ
~Mathionaire

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=bHNrBwwUCMI
~NiuniuMaths

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=_0fveg1r3WFmwmpw&t=3334
~Math-X

## Video Solution (🚀 Quick 🚀)
https://youtu.be/pA6Smw91Bc0
~Education, the Study of Everything

## Video Solution by North America Math Contest Go Go Go
https://www.youtube.com/watch?v=5Qo4pG3Uk_U
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/l9wZS3qGSCg
~savannahsolver

## Video Solution
https://youtu.be/VnOecUiP-SA

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=852
~Interstigation

## Video Solution by OmegaLearn
https://youtu.be/7SwJdAEOeAg?t=23
~ pi_is_3.14

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=S_CnKCuOA_w
### See Also