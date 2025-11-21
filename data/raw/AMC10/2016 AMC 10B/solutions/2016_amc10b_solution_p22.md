# 2016 AMC 10B Problem 22

## Problem

A set of teams held a round-robin tournament in which every team played every other team exactly once. Every team won $10$ games and lost $10$ games; there were no ties. How many sets of three teams $\{A, B, C\}$ were there in which $A$ beat $B$ , $B$ beat $C$ , and $C$ beat $A?$

$\textbf{(A)}\ 385 \qquad \textbf{(B)}\ 665 \qquad \textbf{(C)}\ 945 \qquad \textbf{(D)}\ 1140 \qquad \textbf{(E)}\ 1330$

## Solution 1
There are $10 \cdot 2+1=21$ teams. Any of the $\tbinom{21}3=1330$ sets of three teams must either be a fork (in which one team beat both the others) or a cycle:
[asy]size(7cm);label("A",(5,5));label("C",(10,0));label("B",(0,0));draw((4,4)--(1,1),EndArrow);draw((6,4)--(9,1),EndArrow); label("A",(20,5));label("C",(25,0));label("B",(15,0));draw((19,4)--(16,1),EndArrow);draw((16,0)--(24,0),EndArrow);draw((24,1)--(21,4),EndArrow); [/asy] But we know that every team beat exactly $10$ other teams, so for each possible $A$ at the head of a fork, there are always exactly $\tbinom{10}2$ choices for $B$ and $C$ as $A$ beat exactly 10 teams and we are choosing 2 of them. Therefore there are $21\cdot\tbinom{10}2=945$ forks, and all the rest must be cycles.
Thus the answer is $1330-945=385$ which is $\boxed{\textbf{(A)}}$ .

## Solution 2 (Cheap Solution)
Since there are $21$ teams and for each set of three teams there is a cycle, there are a total of $\tbinom{21}3=1330$ cycles of three teams. Because about $1/4$ of the cycles $\{A, B, C\}$ satisfy the conditions of the problems, our answer is close to $1/4 \cdot 1330=332.5$ . Looking at the answer choices, we find that $332.5$ is closer to $385$ than any other answer choices, and that the next closest is $665$ which is twice of $332.5$ , so our answer is $385$ which is $\boxed{\textbf{(A)}}$ .
Speaking of cheap solutions, you can let the teams be $1,2,3,..21$ and have $i$ beat $i+1,i+2, ... i+10 \pmod{21}$ and lose to $i+11,i+12, ... i+20 \pmod{21}.$ You can choose any random team as $A$ for $21$ ways but overcount since set, so divide by $3$ so multiply by $7.$ Now we can proceed w/casework (which isn't too hard). Eventually you realize the sum is $7(1+2+\cdots+10) = \boxed{\textbf{(A)}}$ .

## Solution 3 (Circle)
Let's arrange all the teams in a circle and assume that each team won against the first 10 teams clockwise of themselves, and lost against the first 10 teams counter-clockwise of themselves.
Consider a working set of $3$ teams: moving clockwise, we know that the first team beat the team clockwise of itself, that team beat the next team clockwise of itself, and the final team beat the first team, which would be clockwise of itself. However, we also must remember that if the first team beat the second team, moving clockwise, the second team cannot be more than $10$ teams away from the first team; the same applies to the second and third team, and the third and first team.
Let's say, WLOG, that the first team, team $A$ , is at position $0$ out of $20$ on the circle.
If team $A$ is to beat team $B$ , since we are assuming each team beats the 10 members clockwise of themselves, there are $10$ places on the circle that team $B$ could be: positions $1$ through $10$ . Also, if team $C$ is to beat team $A$ , team $C$ must be located from positions $11$ to $20$ .
If Team $B$ is in position $n$ , $C$ must be located from position $n+1$ to position $n+10$ , since $B$ beats $C$ . We also just found that $C$ 's position must be between $11$ and $20$ inclusive. So, when $B$ is in position $1$ , $C$ can only be in position $11$ . When $B$ is in position $2$ , $C$ can be in position $11$ or $12$ . In general, when $B$ is in position $n$ , there are $n$ choices for where $C$ can be. So, there are $1+2+3+ \dots + 10 = 55$ ways to place $B$ and $C$ . There are $21$ players to choose as player $A$ , and each working set will be counted $3$ times, so our final answer is $55 \cdot 21 \div 3 = \boxed{385, \textbf{(A)}}$ .

## Solution 4 (Aggregate Counting)
This is a Graph Theory problem with directed graph. There are $21$ teams in total. WLOG, pick team $A$ , there are $10$ teams that lost to $A$ and $10$ teams that won over $A$ . Call the group of teams that lost to $A$ group $L$ , and the group of teams that won over $A$ group $W$ .
[asy] size(7cm); label("A",(20,5)); label("Group W",(27,0)); label("Group L",(13,0)); draw((19,4)--(16,1),EndArrow); draw((16,0)--(24,0),EndArrow); draw((24,1)--(21,4),EndArrow); [/asy]
Any team from group $L$ that won a team from group $W$ will form a cycle with $A$ . Now we need to count how many teams in group $L$ won over a team from group $W$ . The total number of wins in group $L$ is $10 \cdot 10 =100$ . There are $\tbinom{10}2=45$ wins among the teams inside group $L$ . So group $L$ has $100-45=55$ wins over group $W$ .
\[\frac{21 \cdot 55}{3}=\boxed{385, \textbf{(A)}}\]
~ isabelchen

## Video Solution by Pi Academy
https://youtu.be/PeO-o9MOIYo?si=ZipIxXwzJPeTaEAP
~ Pi Academy
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .