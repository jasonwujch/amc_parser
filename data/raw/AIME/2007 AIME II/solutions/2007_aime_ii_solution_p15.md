# 2007 AIME II Problem 15

## Problem

Four circles $\omega,$ $\omega_{A},$ $\omega_{B},$ and $\omega_{C}$ with the same radius are drawn in the interior of triangle $ABC$ such that $\omega_{A}$ is tangent to sides $AB$ and $AC$ , $\omega_{B}$ to $BC$ and $BA$ , $\omega_{C}$ to $CA$ and $CB$ , and $\omega$ is externally tangent to $\omega_{A},$ $\omega_{B},$ and $\omega_{C}$ . If the sides of triangle $ABC$ are $13,$ $14,$ and $15,$ the radius of $\omega$ can be represented in the form $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

1 Problem

- 1 Problem

- 2 Diagram

- 3 Solution 1 (Homothety)

- 4 Solution 2

- 5 Solution 3 (elementary)

- 6 Solution 4

- 7 Sidenote (Generalization)

- 8 Solution 5

- 9 Solution 6

- 10 Video Solution

- 11 See also

### Diagram

[asy] defaultpen(fontsize(12)+0.8); size(300); pair A,B,C,X,Y,Z,P,Q,R; B=origin; C=15*right; A=IP(CR(B,13),CR(C,14)); P=incenter(A,B,C); real r=260/129; Q=r*(rotate(-90)*A/length(A)); X=extension(A,P,Q,Q+A); Y=extension(B,P,Q,Q+A); R=rotate(90,C)*(C+r*(A-C)/length(A-C)); Z=extension(C,P,R,R+A-C); draw(A--B--C--A); draw(CR(X,r)^^CR(Y,r)^^CR(Z,r)^^A--P--B^^P--C, gray); draw(CR(circumcenter(X,Y,Z),r), gray); label("$A$",A,N); label("$B$",B,0.15*(B-P)); label("$C$",C,0.1*(C-P)); pen p=fontsize(10)+linewidth(3); dot("$O_A$",X,right,p); dot("$O_B$",Y,left+up,p); dot("$O_C$",Z,right+up,p); dot("$O$",circumcenter(X,Y,Z),right+down,p); dot("$I$",P,left+up,p); [/asy]

## Solution 1 (Homothety)
[asy] defaultpen(fontsize(12)+0.8); size(350); pair A,B,C,X,Y,Z,P,Q,R,Zp; B=origin; C=15*right; A=IP(CR(B,13),CR(C,14)); P=incenter(A,B,C); real r=260/129; Q=r*(rotate(-90)*A/length(A)); X=extension(A,P,Q,Q+A); Y=extension(B,P,Q,Q+A); R=rotate(90,C)*(C+r*(A-C)/length(A-C)); Z=extension(C,P,R,R+A-C); Zp=circumcenter(X,Y,Z); draw(A--B--C--A); draw(CR(X,r)^^CR(Y,r)^^CR(Z,r), gray); draw(A--P--B^^P--C^^X--Y--Z--X, royalblue); draw(X--foot(X,A,C)^^Z--foot(Z,A,C),royalblue); draw(CR(Zp,r), gray); draw(incircle(A,B,C)^^incircle(X,Y,Z)^^P--foot(P,A,C), heavygreen+0.6); draw(rightanglemark(X,foot(X,A,C),C,10),linewidth(0.6)); draw(rightanglemark(Z,foot(Z,A,C),A,10),linewidth(0.6)); label("$A$",A,N); label("$B$",B,0.15*(B-P)); label("$C$",C,0.1*(C-P)); pen p=fontsize(10)+linewidth(3); dot("$O_A$",X,right,p); dot("$O_B$",Y,left+up,p); dot("$O_C$",Z,down,p); dot("$O$",Zp,dir(-45),p+red); dot("$I$",P,left+up,p); [/asy]
First, apply Heron's formula to find that $[ABC] = \sqrt{21 \cdot 8 \cdot 7 \cdot 6} = 84$ . The semiperimeter is $21$ , so the inradius is $\frac{A}{s} = \frac{84}{21} = 4$ .
Now consider the incenter $I$ of $\triangle ABC$ . Let the radius of one of the small circles be $r$ . Let the centers of the three little circles tangent to the sides of $\triangle ABC$ be $O_A$ , $O_B$ , and $O_C$ . Let the center of the circle tangent to those three circles be $O$ . The homothety $\mathcal{H}\left(I, \frac{4-r}{4}\right)$ maps $\triangle ABC$ to $\triangle O_A O_B O_C$ since $OO_A = OO_B = OO_C = 2r$ , $O$ is the circumcenter of $\triangle O_A O_B O_C$ and $\mathcal{H}$ therefore maps the circumcenter of $\triangle ABC$ to $O$ . Thus, $2r = R \cdot \frac{4 - r}{4}$ , where $R$ is the circumradius of $\triangle ABC$ . Substituting $R = \frac{abc}{4[ABC]} = \frac{65}{8}$ , $r = \frac{260}{129}$ and the answer is $\boxed{389}$ .
https://latex.artofproblemsolving.com/9/4/7/947b7f06d947dbf8bc5d8f61cdd193c330377372.png

## Solution 2
Consider a 13-14-15 triangle. $A=84.$ (By Heron's Formula or by 5-12-13 and 9-12-15 right triangles.)
The inradius is $r=\frac{A}{s}=\frac{84}{21}=4$ , where $s$ is the semiperimeter. Scale the triangle with the inradius by a linear scale factor, $u.$
The circumradius is $R=\frac{abc}{4rs}=\frac{13\cdot 14\cdot 15}{4\cdot 4\cdot 21}=\frac{65}{8},$ where $a,$ $b,$ and $c$ are the side-lengths. Scale the triangle with the circumradius by a linear scale factor, $v$ .
Cut and combine the triangles, as shown. Then solve for $4u$ :
The solution is $260+129=\boxed{389}$ .

## Solution 3 (elementary)
Let $A'$ , $B'$ , $C'$ , and $O$ be the centers of circles $\omega_{A}$ , $\omega_{B}$ , $\omega_{C}$ , $\omega$ , respectively, and let $x$ be their radius.
Now, triangles $ABC$ and $A'B'C'$ are similar by parallel sides, so we can find ratios of two quantities in each triangle and set them equal to solve for $x$ .
Since $OA'=OB'=OC'=2x$ , $O$ is the circumcenter of triangle $A'B'C'$ and its circumradius is $2x$ . Let $I$ denote the incenter of triangle $ABC$ and $r$ the inradius of $ABC$ . Then the inradius of $A'B'C'=r-x$ , so now we compute r. Computing the inradius by $A=rs$ , we find that the inradius of $ABC$ is $4$ . Additionally, using the circumradius formula $R=\frac{abc}{4K}$ where $K$ is the area of $ABC$ and $R$ is the circumradius, we find $R=\frac{65}{8}$ . Now we can equate the ratio of circumradius to inradius in triangles $ABC$ and $A'B'C'$ .
\[\frac{\frac{65}{8}}{4}=\frac{2x}{4-x}\]
Solving, we get $x=\frac{260}{129}$ , so our answer is $260+129=\boxed{389}$ .

## Solution 4
According to the diagram, it is easily to see that there is a small triangle made by the center of three circles which aren't in the middle. The circumradius of them is $2r$ . Now denoting $AB=13;BC=14;AC=15$ , and centers of circles tangent to $AB,AC;AC,BC;AB,BC$ are relatively $M,N,O$ with $OJ,NK$ both perpendicular to $BC$ . It is easy to know that $tanB=\frac{12}{5}$ , so $tan\angle OBJ=\frac{2}{3}$ according to half angle formula. Similarly, we can find $tan\angle NCK=\frac{1}{2}$ . So we can see that $JK=ON=14-\frac{7x}{2}$ . Obviously, $\frac{2x}{14-\frac{7x}{2}}=\frac{65}{112}$ . After solving, we get $x=\frac{260}{129}$ , so our answer is $260+129=\boxed{389}$ . ~bluesoul
### Sidenote (Generalization)
If four circles $\omega,$ $\omega_{A},$ $\omega_{B},$ and $\omega_{C}$ with the same radius are drawn in the interior of triangle $ABC$ such that $\omega_{A}$ is tangent to sides $AB$ and $AC$ , $\omega_{B}$ to $BC$ and $BA$ , $\omega_{C}$ to $CA$ and $CB$ , and $\omega$ is externally tangent to $\omega_{A},$ $\omega_{B},$ and $\omega_{C}$ . If $ABC$ has side lengths $a,b,$ and $c$ , then the radius of $\omega$ can be written as \[\frac{abc\sqrt{2b^{2}c^{2}+2a^{2}b^{2}+2a^{2}c^{2}-a^{4}-b^{4}-c^{4}}}{4b^{2}c^{2}+4a^{2}b^{2}+4a^{2}c^{2}-2a^{4}-2b^{4}-2c^{4}+2a^{2}bc+2ab^{2}c+2abc^{2}},\] or, more simply as, \[\frac{abc\cdot K}{8K^{2}+sabc},\] where $K$ is the area of the triangle and $s$ is the semiperimeter
~pinkpig

## Solution 5
[asy] defaultpen(fontsize(12)+0.8); size(300); pair A,B,C,X,Y,Z,P,Q,R; B=origin; C=15*right; A=IP(CR(B,13),CR(C,14)); P=incenter(A,B,C); real r=260/129; Q=r*(rotate(-90)*A/length(A)); X=extension(A,P,Q,Q+A); Y=extension(B,P,Q,Q+A); R=rotate(90,C)*(C+r*(A-C)/length(A-C)); Z=extension(C,P,R,R+A-C); draw(A--B--C--A); draw(CR(X,r)^^CR(Y,r)^^CR(Z,r)^^A--P--B^^P--C, gray); draw(CR(circumcenter(X,Y,Z),r), gray); label("$A$",A,N); label("$B$",B,0.15*(B-P)); label("$C$",C,0.1*(C-P)); draw(X--Y--Z--cycle); draw(Y--(3.5,0),blue); draw(P--(7,0), blue); pen p=fontsize(10)+linewidth(3); dot("$O_A$",X,right,p); dot("$O_B$",Y,left+up,p); dot("$O_C$",Z,right+up,p); dot("$O$",circumcenter(X,Y,Z),right+down,p); dot("$I$",P,left+up,p); dot("$H$",(7,0),down,p); [/asy]
Let $O_A, O_B, O_C, O$ be the centers of $w_A, w_B, w_C, w$ , respectively. Also, let $I$ be the incenter of $ABC$ and $r$ be the radius of circle $w$ . Since $AB||O_AO_B$ , $BC||O_BO_C$ , and $CA||O_CO_A$ , we know that
\[\angle BAI = \angle O_BO_AI, \angle CBI = \angle O_CO_BI, \angle ACI = \angle O_AO_CI \text{ and }\angle CAI = \angle O_CO_AI, \angle ABI = \angle O_AO_BI, \angle BCI = \angle O_BO_CI.\]
That means $\angle ABC = \angle O_AO_BO_C$ , $\angle BAC = \angle O_BO_AO_C$ , and $\angle ACB = \angle O_AO_CO_B$ . Thus, $\triangle ABC \sim \triangle O_AO_BO_C$ . We also know that we are scaling each side of $\triangle ABC$ (from $AB$ to $O_AO_B$ for instance), about $I$ (since A,O_A,I are collinear ; same apply with $B$ and $C$ ).
Now, let the homothety $\mathcal{H} (I, x)$ map $\triangle ABC$ to $\triangle O_AO_BO_C$ . To start off, we know the circumradius of $O_AO_BO_C$ is $O$ , since $OO_A = OO_B = OO_C = 2r$ . Since $O_AO_B = 13x$ , $O_BO_C = 14x$ , $O_CO_A = 15x$ , we can get an relationship involving $x$ and $r$ via another way to find the circumradius:
\[[\triangle O_AO_BO_C ] =\frac{abc}{4R} \Longrightarrow 84x^2 =\frac{13x\cdot 14x\cdot 15x}{4\cdot 2r} \Longrightarrow r=\frac{65x}{16}\]
Take notice of the inradius of $ABC$ . We get the inradius to be $[\triangle ABC ] = sr_0 \Longrightarrow r_0=4$ . Let the tangency point of the incircle and side $BC$ be $H$ . We know $IH = 4$ . We also know that we can cut off the part of $IH$ that is outside of $\triangle O_AO_BO_C$ to get the inradius of $\triangle O_AO_BO_C$ . To part that is outside $\triangle O_AO_BO_C$ turns out just to be the radius of circle $w_B$ (as seen in the picture). That means the inradius of $\triangle O_AO_BO_C$ is just $4-r$ . We can calculate that incradius in another way, though. We know that the inradius of $\triangle ABC$ is $4$ , which means the inradius of $\triangle O_AO_BO_C$ is just $4x$ (by our homethety ratio).
Thus, we have $4x = 4-r = 4-\dfrac{65x}{16} \Longrightarrow x = \dfrac{64}{129} \Longrightarrow r = \dfrac{260}{129}$ . That gives $\boxed{389}$ as our final answer.
The homethety turned out to be $\mathcal{H} \left(I, \dfrac{64}{129}\right)$
~sml1809

## Solution 6
Let the radius of $\omega$ be $r$ , let the centers of $\omega_A$ , $\omega_B$ , and $\omega_C$ be $O_A$ , $O_B$ , and $O_C$ , respectively, and let the feet of the altitudes from $O_A$ and $O_C$ onto $AC$ be $X$ and $Y$ , respectively. Now, observe that $\triangle O_AO_BO_C$ has all its sides parallel to the sides of $\triangle ABC$ , so the two triangles are similar. Then, we get \begin{align*} AC&=AX+XY+YC,\\ 15&=r\cot\frac{\angle A}{2}+O_AO_C+r\cot\frac{\angle C}{2},\\ 15&=r\sqrt{\frac{1+\cos A}{1-\cos A}}+4r\sin\angle B+r\sqrt{\frac{1+\cos C}{1-\cos C}},\\ 15&=r\sqrt{\frac{65+33}{65-33}}+\frac{48}{13}r+r\sqrt{\frac{5+3}{5-3}},\\ r&=\frac{15}{\frac 74+\frac{48}{13}+2}\\ &=\boxed{\frac{260}{129}}.\,\square\\ \end{align*}
~pieMax2713

## Video Solution
2007 AIME II #15
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.