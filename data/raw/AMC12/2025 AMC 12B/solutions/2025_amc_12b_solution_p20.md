# 2025 AMC 12B Problem 20

## Problem

A frog hops along the number line according to the following rules:

- It starts at $0$ .

- If it is at $0$ , then it moves to $1$ with probability $\frac 12$ and disappears with probability $\frac 12$ .

- For $n=1,2,3,$ if it is at $n$ , then it moves to $n+1$ with probability $\frac 14,$ to $n-1$ with probability $\frac 14,$ and disappears with probability $\frac 12$ .

What is the probability that the frog reaches $4?$

$\textbf{(A) } \frac1{101} \qquad \textbf{(B) } \frac 1{100} \qquad \textbf{(C) } \frac1{99} \qquad \textbf{(D) } \frac1{98} \qquad \textbf{(E) } \frac1{97}$

## Solution 1
We will solve this using states. Let $P_n$ be the probability of reaching $4$ , given that you start from $n$ . We want to find $P_0$ . Of course, $P_4 = 1$ . We also know that \[P_3 = \frac{1}{4}P_4 + \frac{1}{4}P_2\] \[P_2 = \frac{1}{4}P_3 + \frac{1}{4}P_1\] \[P_1 = \frac{1}{4}P_2 + \frac{1}{4}P_0\] \[P_0 = \frac{1}{2}P_1.\] Solving the system, we find that $P_1 = \frac{2}{97}$ and $P_0 = \boxed{\frac{1}{97}}.$
~lprado
Solution for certain China testpapers: (Pretty sure it also got moved to Problem 22) The problem was instead of a line it was a circle with points A,B,C,D,E in a circle, the frog started at A and was needed to figure out the probability of going to E. Using symmetry it was possible to deduce that P(A)=P(D) and P(B)=P(C), if we let them be equal to x and y respectively, then you got x=1/4+y/4 and y=y/4+x/4. Solving yielded x=3/11 and y=1/11, and since P(A)=x then the probability of reaching E from A was 3/11. (~iHateGeometry)

## Solution 2 (Characteristic Polynomial of Recurrence Relation)
For $n=1,2,3$ , we have the recurrence relation $p_{n}=\frac{1}{4}(p_{n-1}+p_{n+1})\iff 0=p_{n+1}-4p_{n}+p_{n-1}$ . This gives the characteristic polynomial $r^2-4r+1=0$ , so let $r,s=\frac{4\pm \sqrt{ 16-4 }}{2}=2\pm \sqrt{ 3 }$ , so $p_{n}=A(2-\sqrt{ 3 })^n+B(2+\sqrt{ 3 })^n$ . We plug in the boundary conditions $2p_{0}=p_{1}$ and $p_{4}=1$ . \[2p_{0}=2(Ar^0+Bs^0)=2A+2B=p_{1}=A(2-\sqrt{ 3 })+B(2+\sqrt{ 3 })\] Canceling the $2A$ and $2B$ , it remains that $A=B$ . Now, take $p_{4}=1$ . Using the property of rational conjugation $\overline{z^n}=\overline{z}^n$ for $\overline{a+\sqrt{ b }}=a-\sqrt{ b }$ , we compute \[1=A(r^4+\overline{r}^4)=2A\cdot\mathrm{Ra}(r^4)\] Now $r^4=(2+\sqrt{ 3 })^4=(7+4\sqrt{ 3 })^2=97+(\dots) \sqrt{ 3 }$ , giving $\mathrm{Ra}(r^4)=97$ , so $p_{0}=2A=\frac{1}{\mathrm{Ra}(r^4)}=\boxed{ \textbf{(E) } \frac1{97} }$ .
~imosilver

## Solution 3
Let $P_n$ be the probability that the frog eventually reaches position $n$ , given that it is at position $n-1$ .
From position 1, the frog moves to 2 with probability $\frac{1}{2}$ , or disappears with probability $\frac{1}{2}$ . Hence $P_1 = \frac{1}{2}$ .
From position 2, the frog moves to 3 with probability $\frac{1}{4}$ , back to 1 with probability $\frac{1}{4}$ , or disappears with probability $\frac{1}{2}$ . Using $P_1 = \frac{1}{2}$ , we have $P_2 = \frac{1}{4} + \frac{1}{4} \cdot \frac{1}{2} P_2 = \frac{1}{4} + \frac{1}{8} P_2 \implies \frac{7}{8} P_2 = \frac{1}{4} \implies P_2 = \frac{2}{7}$ .
From position 3, similarly, $P_3 = \frac{1}{4} + \frac{1}{4} \cdot \frac{2}{7} P_3 = \frac{1}{4} + \frac{1}{14} P_3 \implies \frac{13}{14} P_3 = \frac{1}{4} \implies P_3 = \frac{7}{26}$ .
From position 4, $P_4 = \frac{1}{4} + \frac{1}{4} \cdot \frac{7}{26} P_4 \implies \frac{97}{104} P_4 = \frac{1}{4} \implies P_4 = \frac{26}{97}$ .
Finally, multiplying the probabilities along the path from 1 to 4 (including the initial step from 0 to 1): $\frac{1}{2} \cdot \frac{2}{7} \cdot \frac{7}{26} \cdot \frac{26}{97} = \boxed{ \textbf{(E) } \frac1{97} }$ ~MathKing555
Video Solution (Fast and Easy) https://www.youtube.com/watch?v=e6Yyk8C_TQc ~ Pi Academy Video Solution 1 by SpreadTheMathLove https://www.youtube.com/watch?v=KYmc2m_WcP8 Video Solution 2 by OmegaLearn.org https://youtu.be/wBBlErp40Xc

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=e6Yyk8C_TQc ~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=KYmc2m_WcP8

## Video Solution 2 by OmegaLearn.org
https://youtu.be/wBBlErp40Xc

## Video Solution 3 (Fast and Easy)
https://www.youtube.com/watch?v=xh3-R0Q_7Gg ~ Pi Academy
See Also 2025 AMC 10B (Problems • Answer Key • Resources) Preceded byProblem 23 Followed byProblem 25 1 • 2 • 3 • 4 • 5 • 6 • 7 • 8 • 9 • 10 • 11 • 12 • 13 • 14 • 15 • 16 • 17 • 18 • 19 • 20 • 21 • 22 • 23 • 24 • 25 All AMC 10 Problems and Solutions 2025 AMC 12B (Problems • Answer Key • Resources) Preceded byProblem 19 Followed byProblem 21 1 • 2 • 3 • 4 • 5 • 6 • 7 • 8 • 9 • 10 • 11 • 12 • 13 • 14 • 15 • 16 • 17 • 18 • 19 • 20 • 21 • 22 • 23 • 24 • 25 All AMC 12 Problems and Solutions
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .