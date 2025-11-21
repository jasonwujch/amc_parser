# 2019 AMC 8 Problem 12

## Problem

The faces of a cube are painted in six different colors: red $(R)$ , white $(W)$ , green $(G)$ , brown $(B)$ , aqua $(A)$ , and purple $(P)$ . Three views of the cube are shown below. What is the color of the face opposite the aqua face?

[asy] unitsize(2cm); pair x, y, z, trans; int i; x = dir(-5); y = (0.6,0.5); z = (0,1); trans = (2,0); for (i = 0; i <= 2; ++i) { draw(shift(i*trans)*((0,0)--x--(x + y)--(x + y + z)--(y + z)--z--cycle)); draw(shift(i*trans)*((x + z)--x)); draw(shift(i*trans)*((x + z)--(x + y + z))); draw(shift(i*trans)*((x + z)--z)); } label(rotate(-3)*"$R$", (x + z)/2); label(rotate(-5)*slant(0.5)*"$B$", ((x + z) + (y + z))/2); label(rotate(35)*slant(0.5)*"$G$", ((x + z) + (x + y))/2); label(rotate(-3)*"$W$", (x + z)/2 + trans); label(rotate(50)*slant(-1)*"$B$", ((x + z) + (y + z))/2 + trans); label(rotate(35)*slant(0.5)*"$R$", ((x + z) + (x + y))/2 + trans); label(rotate(-3)*"$P$", (x + z)/2 + 2*trans); label(rotate(-5)*slant(0.5)*"$R$", ((x + z) + (y + z))/2 + 2*trans); label(rotate(-85)*slant(-1)*"$G$", ((x + z) + (x + y))/2 + 2*trans); [/asy]

$\textbf{(A)} \text{ red}\qquad\textbf{(B)} \text{ white}\qquad\textbf{(C)} \text{ green}\qquad\textbf{(D)} \text{ brown}\qquad\textbf{(E)} \text{ purple}$

## Solution 1
$B$ is on the top, and $R$ is on the side, and $G$ is on the right side. That means that (image $2$ ) $W$ is on the left side. From the third image, you know that $P$ must be on the bottom since $G$ is sideways. That leaves us with the back, so the back must be $A$ . The front is opposite of the back, so the answer is $\boxed{\textbf{(A)}\ R}$ .

## Solution 2
Looking closely, we can see that all faces are connected with $R$ except for $A$ . Thus, the answer is $\boxed{\textbf{(A)}\ R}$ .
It is A, just draw it out! ~phoenixfire

## Solution 3
From pic 1 and 2, we know that the G's opposite is W. From pic 1 and 3, the B's opposite is P. So the $A$ 's opposite is $\boxed{\textbf{(A)}\ R}$ .

## Video Solution by Math-X (Simple Visualization!!!)
https://youtu.be/IgpayYB48C4?si=uPWa04P5Bi6wEZB-&t=3752
~Math-X

## Solution Explained
https://youtu.be/gOZOCFNXMhE ~ The Learning Royal

## Solution 3
Associated video - https://www.youtube.com/watch?v=K5vaX_EzjEM

## Video Solution
Solution detailing how to solve the problem: https://www.youtube.com/watch?v=VXBqE-jh2WA&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=13

## Video Solution
https://youtu.be/dru7MQO6jqs
~savannahsolver

## Video Solution (CREATIVE ANALYSIS!!!)
https://youtu.be/kD4V_InGI_g
~Education, the Study of Everything

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1