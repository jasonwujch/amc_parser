# 2020 AMC 8 Problem 25

## Problem

Rectangles $R_1$ and $R_2,$ and squares $S_1,\,S_2,\,$ and $S_3,$ shown below, combine to form a rectangle that is 3322 units wide and 2020 units high. What is the side length of $S_2$ in units?

[asy] draw((0,0)--(5,0)--(5,3)--(0,3)--(0,0)); draw((3,0)--(3,1)--(0,1)); draw((3,1)--(3,2)--(5,2)); draw((3,2)--(2,2)--(2,1)--(2,3)); label("$R_1$",(3/2,1/2)); label("$S_3$",(4,1)); label("$S_2$",(5/2,3/2)); label("$S_1$",(1,2)); label("$R_2$",(7/2,5/2)); [/asy]

$\textbf{(A) }651 \qquad \textbf{(B) }655 \qquad \textbf{(C) }656 \qquad \textbf{(D) }662 \qquad \textbf{(E) }666$

## Solution 1
Let the side length of each square $S_k$ be $s_k$ . Then, from the diagram, we can line up the top horizontal lengths of $S_1$ , $S_2$ , and $S_3$ to cover the top side of the large rectangle, so $s_{1}+s_{2}+s_{3}=3322$ . Similarly, the short side of $R_2$ will be $s_1-s_2$ , and lining this up with the left side of $S_3$ to cover the vertical side of the large rectangle gives $s_{1}-s_{2}+s_{3}=2020$ . We subtract the second equation from the first to obtain $2s_{2}=1302$ , and thus $s_{2}=\boxed{\textbf{(A) }651}$ .

## Solution 2
Assuming that the problem is well-posed, it should be true in the particular case where $S_1 \cong S_3$ and $R_1 \cong R_2$ . Let the sum of the side lengths of $S_1$ and $S_3$ be $x$ , and let the length of square $S_2$ be $y$ . We then have the system \[\begin{dcases}x+y =3322 \\x-y=2020\end{dcases}\] which we solve to determine $y=\boxed{\textbf{(A) }651}$ .

## Solution 3 (faster version of Solution 1)
Since, for each pair of rectangles, the side lengths have a sum of $3322$ or $2020$ and a difference of $S_2$ , the answer must be $\dfrac{3322 - 2020}{2} = \dfrac{1302}{2} = \boxed{\textbf{(A) }651}$ .

## Solution 4
Let the side length of $S_2$ be s, and the shorter side length of $R_1$ and $R_2$ be $r$ . We have
[asy] draw((0,0)--(5,0)--(5,3)--(0,3)--(0,0)); draw((3,0)--(3,1)--(0,1)); draw((3,1)--(3,2)--(5,2)); draw((3,2)--(2,2)--(2,1)--(2,3)); label("$R_1$",(3/2,1/2)); label("$S_3$",(4,1)); label("$S_2$",(5/2,3/2)); label("$S_1$",(1,2)); label("$R_2$",(7/2,5/2)); label("$r$",(5.2,5/2)); label("$r$",(3.2,1/2)); label("$s$",(3.2,3/2)); [/asy]
From this diagram, it is evident that $r+s+r=2020$ . Also, the side length of $S_1$ and $S_3$ is $r+s$ . Then, $r+s+s+r+s=3322$ . Now, we have 2 systems of equations.
\begin{align*}r+s+r &= 2020 \\ r+s+r+s+s &= 3322 \\ \end{align*}
We can see an $r+s+r$ in the 2nd equation, so substituting that in gives us $2020+2s=3322 \Rightarrow 2s= 1302 \Rightarrow s=\boxed{\textbf{(A) }651}$ .

## Solution 5 (Cheese)
Note that the problem is underspecified. We can modify the diagram in any way as long as the relative positioning of the internal rectangles and squares is maintained. Here's an animation describing all such possible configurations:
![](https://wiki-images.artofproblemsolving.com//thumb/c/c9/AMC8_2020_Problem_25_animation.gif/400px-AMC8_2020_Problem_25_animation.gif)
Let's pick the configuration where S1 is as large as possible and takes up the whole height of the rectangle. Then our diagram is just:
[asy] draw((0,0)--(5,0)--(5,3)--(0,3)--(0,0)); // Outer rectangle draw((3,0)--(3,3)); // Vertical line at x = 3 draw((3,0)--(3,1)--(4,1)--(4,0)--cycle); // Bottom-right square S_2 draw((4,0)--(4,1)--(5,1)--(5,0)--cycle); // Bottom-right square S_3 label("3322", (2.5,-0.3), S); // Width label("2020", (-0.3,1.5), W); // Height label("$S_1$", (1.5,1.5)); // Left region S_1 label("$S_2$", (3.5,0.5)); // Bottom-right square S_2 label("$S_3$", (4.5,0.5)); // Bottom-right square S_3 label("$R_2$", (4,2)); // Upper-right rectangle R_2 label("$x$", (3.5,1), N); // Label for x above S_2 [/asy]
For \( S_2 \) and \( S_3 \) to share a top edge, they must actually be congruent! Therefore, the width of the entire rectangle, being given as 3322, is also \( 2020 + 2x \). Solving for \( x \), we get $x = \boxed{\textbf{(A) } 651}$ .
~ proloto

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=ryNc6kwFiy7YkEbc&t=6127
~Math-X

## Video Solution(🚀Just 1 min🚀)
https://youtu.be/2yiZ1Mx2P1M
~ Education, the Study of Everything

## Video Solution
https://youtu.be/wAUam5A-jcA
https://www.youtube.com/watch?v=gJXMZq2Rbwg ~David

## Video Solution by OmegaLearn
https://youtu.be/jhJifWaoUI8?t=441
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/LebVAuPkpcg
~savannahsolver

## Video Solution by The Learning Royal
https://youtu.be/JAZXFv1fFGo

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=1639
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/wq8EUCe5oQU?t=588
~STEMbreezy