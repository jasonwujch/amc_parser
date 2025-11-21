# 2024 AMC 8 Problem 20

## Problem

Any three vertices of the cube $PQRSTUVW$ , shown in the figure below, can be connected to form a triangle. (For example, vertices $P$ , $Q$ , and $R$ can be connected to form isosceles $\triangle PQR$ .) How many of these triangles are equilateral and contain $P$ as a vertex?

[asy] unitsize(4); pair P,Q,R,S,T,U,V,W; P=(0,30); Q=(30,30); R=(40,40); S=(10,40); T=(10,10); U=(40,10); V=(30,0); W=(0,0); draw(W--V); draw(V--Q); draw(Q--P); draw(P--W); draw(T--U); draw(U--R); draw(R--S); draw(S--T); draw(W--T); draw(P--S); draw(V--U); draw(Q--R); dot(P); dot(Q); dot(R); dot(S); dot(T); dot(U); dot(V); dot(W); label("$P$",P,NW); label("$Q$",Q,NW); label("$R$",R,NE); label("$S$",S,N); label("$T$",T,NE); label("$U$",U,NE); label("$V$",V,SE); label("$W$",W,SW); [/asy]

$\textbf{(A)}0 \qquad \textbf{(B) }1 \qquad \textbf{(C) }2 \qquad \textbf{(D) }3 \qquad \textbf{(E) }6$

## Solution 1
The only equilateral triangles that can be formed are through the diagonals of the faces of the square. From P you have $3$ possible vertices that are possible to form a diagonal through one of the faces. Therefore, there are $3$ possible triangles. So the answer is $\boxed{\textbf{(D) }3}$ ~Math645, andliu766, e___

## Solution 2
Each other compatible point must be an even number of edges away from P, so the compatible points are R, V, and T. Therefore, we must choose two of the three points, because P must be a point in the triangle. So, the answer is ${3 \choose 2} = \boxed{\textbf{(D) }3}$
-ILoveMath31415926535

## Solution 3 (arduous and not recommended)
List them out- you get $PRV$ , $PRT$ , and $PVT$ . Therefore, the answer is $\boxed{\textbf{(D) 3}}$
-Anonymussrvusdmathstudent234234

## Solution 4 (Easy)
After looking at the cube, we realize that an equilateral triangle can only be formed by three lines that form a diagonal along a face of the cube (such as $PV$ ). Because the problem has a condition that one of the triangle's vertex must be on $P$ , the three diagonals that can be formed are $PT, PR$ , and $PV$ .
Now, we can choose any of 2 out of the 3 lines we have listed, and connect any of them with another line (for example, if we choose $PT$ and $PR$ , the third diagonal is $RT$ ). Thus, there are 3 ways to choose the 3 diagonals, so the answer is $3$ , or $\boxed{\textbf{(D) }3}$
~TechnoDragon

## Video Solution 1 by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/JVPNQJL1Cqc
~mr_mathman

## Video Solution 2 by Math-X (First understand the problem)
https://youtu.be/BaE00H2SHQM?si=QSxNpXGLosdIpffx&t=5954

## Video Solution 3 (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=_-gBZbXx4rn3nLnx&t=2912 ~hsnacademy

## Video Solution 4 (Under 3 minutes)
https://youtu.be/8X3Fwhp5-d8

## Video Solution 5 by Power Solve
https://www.youtube.com/watch?v=7_reHSQhXv8

## Video Solution 6 by NiuniuMaths (Easy to understand)
https://www.youtube.com/watch?v=V-xN8Njd_Lc

## Video Solution 7 by OmegaLearn.org
https://youtu.be/m1iXVOLNdlY

## Video Solution 8 by SpreadTheMathLove
https://www.youtube.com/watch?v=Svibu3nKB7E

## Video Solution 9 by CosineMethod [Fast and Easy]
https://www.youtube.com/watch?v=Xg-1CWhraIM

## Video Solution 10 by Interstigation
https://youtu.be/ktzijuZtDas&t=2353

## Video Solution 11 by Dr. David
https://youtu.be/yDM_2aGYRZU

## Video Solution by 12 WhyMath
https://youtu.be/XsC-x3b4mxE

## Video Solution (Effective, easy and simple)
https://www.youtube.com/watch?v=UwicmTsBvuU ~TheMathGeek

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also