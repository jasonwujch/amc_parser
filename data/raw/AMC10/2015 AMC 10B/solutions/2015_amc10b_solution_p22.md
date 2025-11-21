# 2015 AMC 10B Problem 22

## Problem

In the figure shown below, $ABCDE$ is a regular pentagon and $AG=1$ . What is $FG + JH + CD$ ?

[asy] pair A=(cos(pi/5)-sin(pi/10),cos(pi/10)+sin(pi/5)), B=(2*cos(pi/5)-sin(pi/10),cos(pi/10)), C=(1,0), D=(0,0), E1=(-sin(pi/10),cos(pi/10)); pair F=intersectionpoints(D--A,E1--B)[0], G=intersectionpoints(A--C,E1--B)[0], H=intersectionpoints(B--D,A--C)[0], I=intersectionpoints(C--E1,D--B)[0], J=intersectionpoints(E1--C,D--A)[0]; draw(A--B--C--D--E1--A); draw(A--D--B--E1--C--A); draw(F--I--G--J--H--F); label("$A$",A,N); label("$B$",B,E); label("$C$",C,SE); label("$D$",D,SW); label("$E$",E1,W); label("$F$",F,NW); label("$G$",G,NE); label("$H$",H,E); label("$I$",I,S); label("$J$",J,W); [/asy]

$\textbf{(A) } 3 \qquad\textbf{(B) } 12-4\sqrt5 \qquad\textbf{(C) } \dfrac{5+2\sqrt5}{3} \qquad\textbf{(D) } 1+\sqrt5 \qquad\textbf{(E) } \dfrac{11+11\sqrt5}{10}$

## Solution 1
[asy] pair A=(cos(pi/5)-sin(pi/10),cos(pi/10)+sin(pi/5)), B=(2*cos(pi/5)-sin(pi/10),cos(pi/10)), C=(1,0), D=(0,0), E1=(-sin(pi/10),cos(pi/10)); //(0,0) is a convenient point //E1 to prevent conflict with direction E(ast) pair F=intersectionpoints(D--A,E1--B)[0], G=intersectionpoints(A--C,E1--B)[0], H=intersectionpoints(B--D,A--C)[0], I=intersectionpoints(C--E1,D--B)[0], J=intersectionpoints(E1--C,D--A)[0]; draw(A--B--C--D--E1--A); draw(A--D--B--E1--C--A); draw(F--I--G--J--H--F); label("$A$",A,N); label("$B$",B,E); label("$C$",C,SE); label("$D$",D,SW); label("$E$",E1,W); label("$F$",F,NW); label("$G$",G,NE); label("$H$",H,E); label("$I$",I,S); label("$J$",J,W); [/asy]
Triangle $AFG$ is isosceles, so $AG=AF=1$ . $FJ = FG$ since $\triangle FGJ$ is also isosceles. Using the symmetry of pentagon $FGHIJ$ , notice that $\triangle JHG \cong \triangle AFG$ . Therefore, $JH=AF=1$ .
Since $\triangle AJH \sim \triangle AFG$ , \[\frac{JH}{AF+FJ}=\frac{FG}{FA}\] \[\frac{1}{1+FG} = \frac{FG}1\] \[1 = FG^2 + FG\] \[FG^2+FG-1 = 0\] \[FG = \frac{-1 \pm \sqrt{5} }{2}\]
So, $FG=\frac{-1 + \sqrt{5}}{2}$ since $FG$ must be greater than 0.
Notice that $CD = AE = AJ = AF + FJ = 1 + \frac{-1 + \sqrt{5}}{2} = \frac{1 + \sqrt{5}}{2}$ .
Therefore, $FG+JH+CD=\frac{-1+\sqrt5}2+1+\frac{1+\sqrt5}2=\boxed{\mathbf{(D)}\ 1+\sqrt{5}\ }$
Note by Fasolinka: Alternatively, extend $FI$ and call its intersection with $DC$ $K$ . It is not hard to see that quadrilaterals $FGCK$ and $JHKD$ are parallelograms, so $DC=DK+KC=JH+FG=1+\frac{-1+\sqrt{5}}{2}$ , and the same result is achieved.

## Solution 1 alternative (No trig, only similar triangles :) )
Further insight: I didn't use the obvious similar triangles AFG and AJH, and then AJH and ADC as that would lead to a cubic for x.
~mathboy282

## Solution 2
Notice that $JH=BH=BG=AG=1$ . Since a $36-72-72$ triangle has the congruent sides equal to $\frac{\sqrt{5}+1}{2}$ times the short base side, we have $FG=\frac{2}{\sqrt{5}+1}=\frac{\sqrt{5}-1}{2}$ . Now notice that $CD=AB=AH$ , and that $\bigtriangleup AJH$ is $36-72-72$ . So, $CD=\frac{\sqrt{5}+1}{2}$ and adding gives $\boxed{1+\sqrt{5}}$ , or $\boxed{\textbf{(D)}}$ .

## Solution 3 (Trignometry)
When you first see this problem you can't help but see similar triangles. But this shape is filled with $36 - 72 - 72$ triangles throwing us off. First, let us write our answer in terms of one side length. I chose to write it in terms of $FG$ so we can apply similar triangles easily. To simplify the process lets write $FG$ as $x$ .
First what is $JH$ in terms of $x$ , also remember $AJ = 1+x$ : \[\frac{JH}{1+x}=\frac{x}{1}\] \[JH = {x}^2+x\]
Next, find $DC$ in terms of $x$ , also remember $AD = 2+x$ : \[\frac{DC}{2+x}=\frac{x}{1}\] \[DC = {x}^2+2x\]
So adding all the $FG + JH + CD$ we get $2{x}^2+4x$ . Now we have to find out what x is. For this, we break out a bit of trig. Let's look at $\triangle AFG$ . By the law of sines: \[\frac{x}{\sin(36)}=\frac{1}{\sin(72)}\] \[x=\frac{\sin(36)}{\sin(72)}\]
Now by the double angle identities in trig. $\sin(72) = 2\sin(36)\cos(36)$ substituting in \[x=\frac{1}{2\cos(36)}\]
A good thing to memorize for AMC and AIME is the exact values for all the nice sines and cosines. You would then know that: \[\cos(36)= \frac{1 + \sqrt{5}}{4}\]
so now we know: \[x = \frac{2}{1+\sqrt{5}} = \frac{-1+\sqrt{5}}{2}\]
Substituting back into $2{x}^2+4x$ we get $FG+JH+CD=\boxed{\mathbf{(D)}\ 1+\sqrt{5}\ }$

## Solution 4
Notice that $\angle AFG=\angle AFB$ and $\angle FAG=\angle ABF$ , so we have $\bigtriangleup AFG \sim \bigtriangleup BAF$ . Thus \[\frac{AF}{FG}=\frac{FB}{AF}\] \[\frac{AF}{FG}=\frac{FG+GB}{AF}\] \[\frac{1}{FG}=\frac{FG+1}{1}\] Solving the equation gets $FG=\frac{\sqrt{5}-1}{2}$ .
Since $\bigtriangleup AFG \sim \bigtriangleup AJH$ \[\frac{AF}{FG}=\frac{AJ}{JH}\] \[\frac{AF}{FG}=\frac{AF+FJ}{JH}\] \[\frac{AF}{FG}=\frac{AF+FG}{JH}\] \[\frac{1}{\frac{\sqrt{5}-1}{2}}=\frac{1+\frac{\sqrt{5}-1}{2}}{JH}\] Solving the equation gets $JH=1$ .
Since $\bigtriangleup AFG \sim \bigtriangleup ADC$ \[\frac{AF}{FG}=\frac{AD}{DC}\] \[\frac{AF}{FG}=\frac{AD+FJ+JD}{DC}\] \[\frac{AF}{FG}=\frac{2AF+FG}{DC}\] \[\frac{1}{\frac{\sqrt{5}-1}{2}}=\frac{2+\frac{\sqrt{5}-1}{2}}{DC}\] Solving the equation gets $DC=\frac{\sqrt{5}+1}{2}$
Finally adding them up gets $FG+JH+DC=\frac{\sqrt{5}-1}{2}+1+\frac{\sqrt{5}+1}{2}= \boxed{\mathbf{(D)}\ 1+\sqrt{5}\ }$
Note: this solution might be a bit complicated but it definitely works when none of the cleverer symmetries in Solution 1 is noticed.
~ Nafer

## Solution 5
Note that: \[\frac{FG}{DC}=\frac{AG}{AC}\] \[\frac{JH}{DC}=\frac{AH}{AC}\] Summing the equations, we have: \[\frac{FG + JH + CD}{CD} - 1 = \frac{2 + GH}{AC}\] We know that \[AC = 2 + GH\] So we have \[\frac{FG+JH+CD}{CD} - 1 = 1 \Rightarrow FG + JH + CD = 2 \cdot CD\] All that remains is to find $CD.$ By the law of cosines, we have \begin{align*} CD^2 &= 2 - 2 \cos 108\\ &= 2 - \frac{1 - \sqrt{5}}{2} \\ &= \frac{3 + \sqrt{5}}{2} \end{align*}
Thus, \begin{align*} 2 \cdot CD &= 2 \cdot \sqrt{\frac{3 + \sqrt{5}}{2}} \\ &= 2 \cdot \frac{1 + \sqrt{5}}{2} \\ &= \boxed{\mathbf{(D)}\ 1 + \sqrt{5}} \end{align*}
I'll leave you to convince yourself about certain facts that were deduced in order to obtain these equations.
~mathboy282

## Solution 6(Trignometry)
Let's denote the length FG $x$ . From similarity, GH, HI, JI, and JF are also x. Now, because $\triangle AFG \sim \triangle AJH \sim \triangle ACD$ by SAS similarity, we can write the lengths of FG + JH + CD as $2x^2+4x$ . We obtain this result by directly writing out the similarity statements and then multiplying.
So all we have to do is find x. Because a regular pentagon has angles of 108 degrees, with an easy angle chase we can find $\angle AGF = 72$ . Now drop the altitude from A, and call the point T. Since $\angle GAT = 18$ degrees, we can easily use sine18 deg to find TG = $\frac{\sqrt{5}-1}{4}$ and therefore x = $\frac{\sqrt{5}-1}{4}$ . Plugging this into $2x^2+4x$ , we obtain the result $\boxed{\mathbf{(D)}\ 1 + \sqrt{5}}$ .
~MathCosine

## Solution 7 (Knowledge of )
In a pentagon, FG:JH=JH:CD=CD:AB=1: $\varphi$ . Also, JH=AG. FG= $\frac{1}{\varphi}=\varphi-1$ , so FG+JH+CD= $\varphi-1+1+\varphi=2\varphi=\boxed{(\textbf{D})~1+\sqrt{5}}$

## Video Solution
https://www.youtube.com/watch?v=TpHZVbBGmVQ (Beauty of Math)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .