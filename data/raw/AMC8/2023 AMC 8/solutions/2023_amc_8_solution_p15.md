# 2023 AMC 8 Problem 15

## Problem

Viswam walks half a mile to get to school each day. His route consists of $10$ city blocks of equal length and he takes $1$ minute to walk each block. Today, after walking $5$ blocks, Viswam discovers he has to make a detour, walking $3$ blocks of equal length instead of $1$ block to reach the next corner. From the time he starts his detour, at what speed, in mph, must he walk, in order to get to school at his usual time? [asy] // Diagram by TheMathGuyd size(13cm); // this is an important stickman to the left of the origin pair C=midpoint((-0.5,0.5)--(-0.6,0.05)); draw((-0.5,0.5)--(-0.6,0.05)); // Head to butt draw((-0.64,0.16)--(-0.7,0.2)--C--(-0.47,0.2)--(-0.4,0.22)); // LH-C-RH draw((-0.6,0.05)--(-0.55,-0.1)--(-0.57,-0.25)); draw((-0.6,0.05)--(-0.68,-0.12)--(-0.8,-0.20)); filldraw(circle((-0.5,0.5),0.1),white,black); int i; real d,s; // gap and side d=0.2; s=1-2*d; for(i=0; i<10; i=i+1) { //dot((i,0), red); //marks to start filldraw((i+d,d)--(i+1-d,d)--(i+1-d,1-d)--(i+d,1-d)--cycle, lightgrey, black); filldraw(conj((i+d,d))--conj((i+1-d,d))--conj((i+1-d,1-d))--conj((i+d,1-d))--cycle,lightgrey,black); } fill((5+d,-d/2)--(6-d,-d/2)--(6-d,d/2)--(5+d,d/2)--cycle,lightred); draw((0,0)--(5,0)--(5,1)--(6,1)--(6,0)--(10.1,0),deepblue+linewidth(1.25)); //Who even noticed label("School", (10,0),E, Draw()); [/asy] $\textbf{(A)}\ 4 \qquad \textbf{(B)}\ 4.2 \qquad \textbf{(C)}\ 4.5 \qquad \textbf{(D)}\ 4.8 \qquad \textbf{(E)}\ 5$

## Solution 1
Note that Viswam walks at a constant speed of $60$ blocks per hour as he takes $1$ minute to walk each block. After walking $5$ blocks, he has taken $5$ minutes and has $5$ minutes remaining to walk $7$ blocks. Therefore, he must walk at a speed of $7 \cdot 60 \div 5 = 84$ blocks per hour to get to school on time, from the time he starts his detour. Since he normally walks $\frac{1}{2}$ mile, which is equal to $10$ blocks, $1$ mile is equal to $20$ blocks. Therefore, he must walk at $84 \div 20 = 4.2$ mph from the time he starts his detour to get to school on time, so the answer is $\boxed{\textbf{(B)}\ 4.2}$ .
~pianoboy (Edits by ILoveMath31415926535 , apex304 and MrThinker)

## Solution 2
Viswam walks $10$ blocks, or half a mile, in $10$ minutes. Therefore, he walks at a rate of $3$ mph. When he takes his detour, he must travel $7$ blocks instead of $5$ . Our final equation is $\frac{7}{5} \times 3 = \frac{21}{5} = \boxed{\textbf{(B)}\ 4.2}$ .
- ILoveMath31415926535
Note: In the second half of his journey, he is travelling 7/5 as far as he originally expected to, so he needs to travel at 7/5 the speed to get there on time.
— wescarroll

## Solution 3
When calculating the speed of his normal route, we get:
$\frac{0.5 \mathrm{miles}}{10 \mathrm{minutes}}= \frac{3 \mathrm{miles}}{60 \mathrm{minutes}}$
Keep in mind that his route is $10$ blocks long. Since we count $7$ blocks when the detour starts, than this would mean that he has $\frac{7}{10}$ miles left to walk, considering the normal amount of blocks that he usually walks. Multiplying by $6$ to get the rate, we get, $\frac{42}{10}=4.2$
Therefore, the answer is $\boxed{\textbf{(B)}\ 4.2}$ .

## Video Solution by Math-X (Let's first Understand the question)
https://youtu.be/Ku_c1YHnLt0?si=sWlX8leEM3rALWLK&t=2686
~Math-X

## Video Solution by CoolMathProblems
https://youtu.be/9WP3LQaMIVg?feature=shared&t=510

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/3UrNUd-s59o
~Education, the Study of Everything

## Animated Video Solution
https://youtu.be/iSEwbNKrvWw
~Star League ( https://starleague.us )

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=4153

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=1626

## Video Solution by harungurcan
https://www.youtube.com/watch?v=otNV1MviJsA&t=20s
~harungurcan

## Video Solution (Solve under 60 seconds!!!)
https://youtu.be/6O5UXi-Jwv4?si=KvvABit-3-ZtX7Qa&t=681
~hsnacademy

## Video Solution by Dr. David
https://youtu.be/Ong72hi801E

## Video Solution by WhyMath
https://youtu.be/1kzJKe5_ekE
### See Also