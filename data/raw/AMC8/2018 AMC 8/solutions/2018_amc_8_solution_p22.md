# 2018 AMC 8 Problem 22

## Problem

Point $E$ is the midpoint of side $\overline{CD}$ in square $ABCD,$ and $\overline{BE}$ meets diagonal $\overline{AC}$ at $F.$ The area of quadrilateral $AFED$ is $45.$ What is the area of $ABCD?$

[asy] size(5cm); draw((0,0)--(6,0)--(6,6)--(0,6)--cycle); draw((0,6)--(6,0)); draw((3,0)--(6,6)); label("$A$",(0,6),NW); label("$B$",(6,6),NE); label("$C$",(6,0),SE); label("$D$",(0,0),SW); label("$E$",(3,0),S); label("$F$",(4,2),E); [/asy]

$\textbf{(A) } 100 \qquad \textbf{(B) } 108 \qquad \textbf{(C) } 120 \qquad \textbf{(D) } 135 \qquad \textbf{(E) } 144$

## Solution 1
We can use analytic geometry for this problem.
Let us start by giving $D$ the coordinate $(0,0)$ , $A$ the coordinate $(0,1)$ , and so forth. $\overline{AC}$ and $\overline{EB}$ can be represented by the equations $y=-x+1$ and $y=2x-1$ , respectively. Solving for their intersection gives point $F$ coordinates $\left(\frac{2}{3},\frac{1}{3}\right)$ .
Now, we can see that $\triangle$ $EFC$ ’s area is simply $\frac{\frac{1}{2}\cdot\frac{1}{3}}{2}$ or $\frac{1}{12}$ . This means that pentagon $ABCEF$ ’s area is $\frac{1}{2}+\frac{1}{12}=\frac{7}{12}$ of the entire square, and it follows that quadrilateral $AFED$ ’s area is $\frac{5}{12}$ of the square.
The area of the square is then $\frac{45}{\frac{5}{12}}=9\cdot12=\boxed{\textbf{(B) } 108}$ .

## Solution 2
$\triangle ABC$ has half the area of the square. $\triangle FEC$ has base equal to half the square side length, and by AA Similarity with $\triangle FBA$ , it has $\frac{1}{1+2}= \frac{1}{3}$ the height, so has $\dfrac1{12}$ th of the area of square( $\dfrac1{2}$ * $\dfrac1{2}$ * $\dfrac1{3}$ ). Thus, the area of the quadrilateral is $1-\frac{1}{2}-\frac{1}{12}=\frac{5}{12}$ of the area of the square. The area of the square is then $45\cdot\dfrac{12}{5}=\boxed{\textbf{(B) } 108}$ .
~minor edit by abirgh

## Solution 3
Extend $\overline{AD}$ and $\overline{BE}$ to meet at $X$ . Drop an altitude from $F$ to $\overline{CE}$ and call it $h$ . Also, call $\overline{CE}$ $x$ . As stated before, we have $\triangle ABF \sim \triangle CEF$ , so the ratio of their heights is in a $1:2$ ratio, making the altitude from $F$ to $\overline{AB}$ $2h$ . Note that this means that the side of the square is $3h$ . In addition, $\triangle XDE \sim \triangle XAB$ by AA Similarity in a $1:2$ ratio. This means that the square's side length is $2x$ , making $3h=2x$ .
Now, note that $[ADEF]=[XAB]-[XDE]-[ABF]$ . We have $[\triangle XAB]=(4x)(2x)/2=4x^2,$ $[\triangle XDE]=(x)(2x)/2=x^2,$ and $[\triangle ABF]=(2x)(2h)/2=(2x)(4x/3)/2=4x^2/3.$ Subtracting makes $[ADEF]=4x^2-x^2-4x^2/3=5x^2/3.$ We are given that $[ADEF]=45,$ so $5x^2/3=45 \Rightarrow x^2=27.$ Therefore, $x= 3 \sqrt{3},$ so our answer is $(2x)^2=4x^2=4(27)=\boxed{\textbf{(B) }108}.$
~ moony_eyed
~ Minor Edits by WrenMath

## Solution 4
Solution with Cartesian and Barycentric Coordinates:
We start with the following:
Claim: Given a square $ABCD$ , let $E$ be the midpoint of $\overline{DC}$ and let $BE\cap AC = F$ . Then $\frac {AF}{FC}=2$ .
Proof: We use Cartesian coordinates. Let $D$ be the origin, $A=(0,1),C=(0,1),B=(1,1)$ . We have that $\overline{AC}$ and $\overline{EB}$ are governed by the equations $y=-x+1$ and $y=2x-1$ , respectively. Solving, $F=\left(\frac{2}{3},\frac{1}{3}\right)$ . The result follows. $\square$
Now, we apply Barycentric Coordinates w.r.t. $\triangle ACD$ . We let $A=(1,0,0),D=(0,1,0),C=(0,0,1)$ . Then $E=(0,\tfrac 12,\tfrac 12),F=(\tfrac 13,0,\tfrac 23)$ .
In the barycentric coordinate system, the area formula is $[XYZ]=\begin{vmatrix} x_{1} &y_{1} &z_{1} \\ x_{2} &y_{2} &z_{2} \\ x_{3}& y_{3} & z_{3} \end{vmatrix}\cdot [ABC]$ where $\triangle XYZ$ is a random triangle and $\triangle ABC$ is the reference triangle. Using this, we find that \[\frac{[FEC]}{[ACD]}=\begin{vmatrix} 0&0&1\\ 0&\tfrac 12&\tfrac 12\\ \tfrac 13&0&\tfrac 23 \end{vmatrix}=\frac16.\] Let $[FEC]=x$ so that $[ACD]=45+x$ . Then, we have $\frac{x}{x+45}=\frac 16 \Rightarrow x=9$ , so the answer is $2(45+9)=\boxed{108}$ .
Note: Please do not learn Barycentric Coordinates for the AMC 8.

## Solution 5 (easier)
$\triangle ABF \sim \triangle FEC$ , and the bases $AB$ and $EC$ are in the ratio $2:1$ , so $\frac{[\triangle ABF]}{[\triangle FEC]}=\left(\frac{2}{1}\right)^2=\frac{4}{1}$ , and $[\triangle ABF]=4\cdot[\triangle FEC]$
It is obvious that $[AFED]+[\triangle FEC]=45+[\triangle FEC]=\frac{1}{2}\cdot[ABCD]$
and $[AFED]+[\triangle ABF]=45+4\cdot[\triangle FEC]=\frac{3}{4}\cdot[ABCD]$
Solving the two equations we get $[ABCD]=\boxed{\textbf{(B)}108}$
- bbidev

## Video Solution by OmegaLearn
https://youtu.be/FDgcLW4frg8?t=4038
- pi_is_3.14

## Video Solutions
https://youtu.be/c4_-h7DsZFg
- Happytwin
https://youtu.be/EJ-eFP3KHWg
~savannahsolver

## Video Solution only problem 22's by SpreadTheMathLove
https://www.youtube.com/watch?v=sOF1Okc0jMc
### Note
Set s to be the bottom left triangle.