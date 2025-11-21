# 2020 AMC 8 Problem 16

## Problem

Each of the points $A,B,C,D,E,$ and $F$ in the figure below represents a different digit from $1$ to $6.$ Each of the five lines shown passes through some of these points. The digits along each line are added to produce five sums, one for each line. The total of the five sums is $47.$ What is the digit represented by $B?$

[asy] size(200); dotfactor = 10; pair p1 = (-28,0); pair p2 = (-111,213); draw(p1--p2,linewidth(1)); pair p3 = (-160,0); pair p4 = (-244,213); draw(p3--p4,linewidth(1)); pair p5 = (-316,0); pair p6 = (-67,213); draw(p5--p6,linewidth(1)); pair p7 = (0, 68); pair p8 = (-350,10); draw(p7--p8,linewidth(1)); pair p9 = (0, 150); pair p10 = (-350, 62); draw(p9--p10,linewidth(1)); pair A = intersectionpoint(p1--p2, p5--p6); dot("$A$", A, 2*W); pair B = intersectionpoint(p5--p6, p3--p4); dot("$B$", B, 2*WNW); pair C = intersectionpoint(p7--p8, p5--p6); dot("$C$", C, 1.5*NW); pair D = intersectionpoint(p3--p4, p7--p8); dot("$D$", D, 2*NNE); pair EE = intersectionpoint(p1--p2, p7--p8); dot("$E$", EE, 2*NNE); pair F = intersectionpoint(p1--p2, p9--p10); dot("$F$", F, 2*NNE); [/asy]

$\textbf{(A) }1 \qquad \textbf{(B) }2 \qquad \textbf{(C) }3 \qquad \textbf{(D) }4 \qquad \textbf{(E) }5$

## Solution 1
We can form the following expressions for the sum along each line: \[\begin{dcases}A+B+C\\A+E+F\\C+D+E\\B+D\\B+F\end{dcases}\] Adding these together, we must have $2A+3B+2C+2D+2E+2F=47$ , i.e. $2(A+B+C+D+E+F)+B=47$ . Since $A,B,C,D,E,F$ are unique integers between $1$ and $6$ , we obtain $A+B+C+D+E+F=1+2+3+4+5+6=21$ (where the order doesn't matter as addition is commutative), so our equation simplifies to $42 + B = 47$ . This means $B = \boxed{\textbf{(E) }5}$ . ~RJ5303707

## Solution 2
Following the first few steps of Solution 1, we have $2(A+C+D+E+F)+3B=47$ . Because an even number $2(A+C+D+E+F)$ subtracted from an odd number (47) is always odd, we know that $3B$ is odd, showing that $B$ is odd. Now we know that $B$ is 1, 3, or 5. If we try $B=1$ , we get $43=47$ , which is false. Testing $B=3$ , we get $45=47$ , which is also false. Therefore, we have $B = \boxed{\textbf{(E) }5}$ . -minor edit by tonykuncheng

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=bHNrBwwUCMI
~NiuniuMaths

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=n-vOSvxYPmuhVmaq&t=2574
~Math-X

## Video Solution (CLEVER MANIPULATIONS!!!)
https://youtu.be/W8pib6O_6xA
~ Education, the Study of Everything

## Video Solution by North America Math Contest Go Go Go
https://www.youtube.com/watch?v=hwCb64F34XE
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/1ldTmo4J7Es
~savannahsolver

## Video Solution
https://www.youtube.com/watch?v=a3Z7zEc7AXQ -LOUISGENIUS

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=728
~Interstigation

## Video Solution by OmegaLearn
https://youtu.be/sZfOjGtEtEY?t=604
~ pi_is_3.14