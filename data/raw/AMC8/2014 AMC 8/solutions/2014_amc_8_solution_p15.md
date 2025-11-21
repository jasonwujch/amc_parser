# 2014 AMC 8 Problem 15

## Problem

The circumference of the circle with center $O$ is divided into $12$ equal arcs, marked the letters $A$ through $L$ as seen below. What is the number of degrees in the sum of the angles $x$ and $y$ ?

[asy] size(230); defaultpen(linewidth(0.65)); pair O=origin; pair[] circum = new pair[12]; string[] let = {"$A$","$B$","$C$","$D$","$E$","$F$","$G$","$H$","$I$","$J$","$K$","$L$"}; draw(unitcircle); for(int i=0;i<=11;i=i+1) { circum[i]=dir(120-30*i); dot(circum[i],linewidth(2.5)); label(let[i],circum[i],2*dir(circum[i])); } draw(O--circum[4]--circum[0]--circum[6]--circum[8]--cycle); label("$x$",circum[0],2.75*(dir(circum[0]--circum[4])+dir(circum[0]--circum[6]))); label("$y$",circum[6],1.75*(dir(circum[6]--circum[0])+dir(circum[6]--circum[8]))); label("$O$",O,dir(60)); [/asy]

$\textbf{(A) }75\qquad\textbf{(B) }80\qquad\textbf{(C) }90\qquad\textbf{(D) }120\qquad\textbf{(E) }150$

## Solution 1
The measure of an inscribed angle is half the measure of its corresponding central angle. Since each unit arc is $\frac{1}{12}$ of the circle's circumference, each unit central angle measures $\frac{360}{12}^{\circ}=30^{\circ}$ . From this, $\angle EOG = 60^{\circ}$ , so $x = 30^{\circ}$ . Also, $\angle AOI = 120^{\circ}$ , so $y = 60^{\circ}$ . The number of degrees in the sum of both angles is $30 + 60 = \boxed{(C)\ 90}.$

## Solution 2
Since $\triangle AOE$ is isosceles and $\angle AOE = \frac{4}{12} \cdot 360^{\circ} = 120^{\circ}$ , $x = 30^{\circ}$ . Since $\triangle GOI$ is isosceles and $\angle GOI = \frac{2}{12} \cdot 360^{\circ} = 60^{\circ}$ , $x = 60^{\circ}$ . The number of degrees in the sum of both angles is $30+60 = \boxed{(C)\ 90}$ .

## Video Solution 1
https://youtu.be/3QHH9xV-QDw
~Education, the Study of Everything

## Video Solution 2
https://www.youtube.com/watch?v=qseG63LK4AU ~David

## Video Solution 3
https://youtu.be/aZhjhb3mMfg ~savannahsolver

## Video Solution 4
https://youtu.be/abSgjn4Qs34?t=3242
### See Also