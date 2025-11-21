# 2023 AMC 8 Problem 17

## Problem

A regular octahedron has eight equilateral triangle faces with four faces meeting at each vertex. Jun will make the regular octahedron shown on the right by folding the piece of paper shown on the left. Which numbered face will end up to the right of $Q$ ?

[asy] // Diagram by TheMathGuyd import graph; // The Solid // To save processing time, do not use three (dimensions) // Project (roughly) to two size(15cm); pair Fr, Lf, Rt, Tp, Bt, Bk; Lf=(0,0); Rt=(12,1); Fr=(7,-1); Bk=(5,2); Tp=(6,6.7); Bt=(6,-5.2); draw(Lf--Fr--Rt); draw(Lf--Tp--Rt); draw(Lf--Bt--Rt); draw(Tp--Fr--Bt); draw(Lf--Bk--Rt,dashed); draw(Tp--Bk--Bt,dashed); label(rotate(-8.13010235)*slant(0.1)*"$Q$", (4.2,1.6)); label(rotate(21.8014095)*slant(-0.2)*"$?$", (8.5,2.05)); pair g = (-8,0); // Define Gap transform real a = 8; draw(g+(-a/2,1)--g+(a/2,1), Arrow()); // Make arrow // Time for the NET pair DA,DB,DC,CD,O; DA = (4*sqrt(3),0); DB = (2*sqrt(3),6); DC = (DA+DB)/3; CD = conj(DC); O=(0,0); transform trf=shift(3g+(0,3)); path NET = O--(-2*DA)--(-2DB)--(-DB)--(2DA-DB)--DB--O--DA--(DA-DB)--O--(-DB)--(-DA)--(-DA-DB)--(-DB); draw(trf*NET); label("$7$",trf*DC); label("$Q$",trf*DC+DA-DB); label("$5$",trf*DC-DB); label("$3$",trf*DC-DA-DB); label("$6$",trf*CD); label("$4$",trf*CD-DA); label("$2$",trf*CD-DA-DB); label("$1$",trf*CD-2DA); [/asy]

$\textbf{(A)}\ 1 \qquad \textbf{(B)}\ 2 \qquad \textbf{(C)}\ 3 \qquad \textbf{(D)}\ 4 \qquad \textbf{(E)}\ 5$

## Solution 1
We color face $6$ red and face $5$ yellow. Note that from the octahedron, face $5$ and face $?$ do not share anything in common. From the net, face $5$ shares at least one vertex with all other faces except face $1,$ which is shown in green: [asy] /* Diagram by TheMathGuyd Edited by MRENTHUSIASM */ import graph; // The Solid // To save processing time, do not use three (dimensions) // Project (roughly) to two size(15cm); pair Fr, Lf, Rt, Tp, Bt, Bk; Lf=(0,0); Rt=(12,1); Fr=(7,-1); Bk=(5,2); Tp=(6,6.7); Bt=(6,-5.2); fill(Tp--Bk--Lf--cycle,red); fill(Bt--Bk--Lf--cycle,yellow); fill(Fr--Rt--Tp--cycle,green); draw(Lf--Fr--Rt); draw(Lf--Tp--Rt); draw(Lf--Bt--Rt); draw(Tp--Fr--Bt); draw(Lf--Bk--Rt,dashed); draw(Tp--Bk--Bt,dashed); label(rotate(-8.13010235)*slant(0.1)*"$Q$", (4.2,1.6)); label(rotate(21.8014095)*slant(-0.2)*"$?$", (8.5,2.05)); pair g = (-8,0); // Define Gap transform real a = 8; draw(g+(-a/2,1)--g+(a/2,1), Arrow()); // Make arrow // Time for the NET pair DA,DB,DC,CD,O; DA = (4*sqrt(3),0); DB = (2*sqrt(3),6); DC = (DA+DB)/3; CD = conj(DC); O=(0,0); transform trf=shift(3g+(0,3)); path NET = O--(-2*DA)--(-2DB)--(-DB)--(2DA-DB)--DB--O--DA--(DA-DB)--O--(-DB)--(-DA)--(-DA-DB)--(-DB); fill(trf*((DA-DB)--O--DA--cycle),red); fill(trf*((DA-DB)--O--(-DB)--cycle),yellow); fill(trf*((-2*DA)--(-DA-DB)--(-DA)--cycle),green); draw(trf*NET); label("$7$",trf*DC); label("$Q$",trf*DC+DA-DB); label("$5$",trf*DC-DB); label("$3$",trf*DC-DA-DB); label("$6$",trf*CD); label("$4$",trf*CD-DA); label("$2$",trf*CD-DA-DB); label("$1$",trf*CD-2DA); [/asy] Therefore, the answer is $\boxed{\textbf{(A)}\ 1}.$
~UnknownMonkey, apex304, MRENTHUSIASM

## Solution 2
We label the octohedron going triangle by triangle until we reach the $?$ triangle. The triangle to the left of the $Q$ should be labeled with a $6$ . Underneath triangle $6$ is triangle $5$ . The triangle to the right of triangle $5$ is triangle $4$ and further to the right is triangle $3$ . Finally, the side of triangle $3$ under triangle $Q$ is $2$ , so the triangle to the right of $Q$ is $\boxed{\textbf{(A)}\ 1}$ .
~hdanger

## Solution 3 (Fast and Cheap)
Notice that the triangles labeled $2, 3, 4,$ and $5$ make the bottom half of the octahedron, as shown below: [asy] /* Diagram by TheMathGuyd Edited by MRENTHUSIASM */ import graph; // The Solid // To save processing time, do not use three (dimensions) // Project (roughly) to two size(15cm); pair Fr, Lf, Rt, Tp, Bt, Bk; Lf=(0,0); Rt=(12,1); Fr=(7,-1); Bk=(5,2); Tp=(6,6.7); Bt=(6,-5.2); dot(Bt,linewidth(5)); draw(Lf--Fr--Rt); draw(Lf--Tp--Rt); draw(Lf--Bt--Rt); draw(Tp--Fr--Bt); draw(Lf--Bk--Rt,dashed); draw(Tp--Bk--Bt,dashed); label(rotate(-8.13010235)*slant(0.1)*"$Q$", (4.2,1.6)); label(rotate(21.8014095)*slant(-0.2)*"$?$", (8.5,2.05)); pair g = (-8,0); // Define Gap transform real a = 8; draw(g+(-a/2,1)--g+(a/2,1), Arrow()); // Make arrow // Time for the NET pair DA,DB,DC,CD,O; DA = (4*sqrt(3),0); DB = (2*sqrt(3),6); DC = (DA+DB)/3; CD = conj(DC); O=(0,0); transform trf=shift(3g+(0,3)); path NET = O--(-2*DA)--(-2DB)--(-DB)--(2DA-DB)--DB--O--DA--(DA-DB)--O--(-DB)--(-DA)--(-DA-DB)--(-DB); dot(trf*(-DB),linewidth(5)); draw(trf*NET); label("$7$",trf*DC); label("$Q$",trf*DC+DA-DB); label("$5$",trf*DC-DB); label("$3$",trf*DC-DA-DB); label("$6$",trf*CD); label("$4$",trf*CD-DA); label("$2$",trf*CD-DA-DB); label("$1$",trf*CD-2DA); [/asy] Therefore, $\textbf{(B)}, \textbf{(C)}, \textbf{(D)},$ and $\textbf{(E)}$ are clearly not the correct answer. Thus, the only choice left is $\boxed{\textbf{(A)}\ 1}$ .
~andy_lee

## Solution 4 (Really Simple Reasoning)
The first half of the octahedron will need $4$ triangles connected to one another to form it. We can choose the triangles $4$ , $5$ , $6$ , and $7$ and form the half around the vertex they all share. That leaves triangles $1$ , $3$ , $2$ , and $Q$ to form the second half. Triangle $3$ will definitely share its sides with triangles $1$ and $2$ , leaving them to share their second side with triangle $Q$ . Since triangle $Q$ will certainly share its left side with triangle $2$ , the only triangle left to share its right side is triangle $\boxed{\textbf{(A)}\ 1}$
~mihikamishra

## Video Solution by Math-X (Simple Visualization)
https://youtu.be/Ku_c1YHnLt0?si=XilaQFDcnGR8ak7W&t=3364
~Math-X

## Video Solution by CoolMathProblems
https://youtu.be/t72hL_LiqIM

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=1699 ~hsnacademy

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/tcGcqm5RHiY
~Education, the Study of Everything

## Animated Video Solution
https://youtu.be/ECqljkDeA5o
~Star League ( https://starleague.us )

## Video Solution by OmegaLearn (Using 3D Visualization)
https://www.youtube.com/watch?v=nVSF2ujZkPE&ab_channel=SohilRathi

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=3789

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=2195

## Video Solution by Dr. David
https://youtu.be/RKPKuD-fqLg
### A Correction and Concise, Thorough Discussion of This Problem by Dr. Xue's Math School
https://youtu.be/aIdo4HQL9O4
### See Also