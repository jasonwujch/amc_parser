# 2020 AMC 10B Problem 13

## Problem

Andy the Ant lives on a coordinate plane and is currently at $(-20, 20)$ facing east (that is, in the positive $x$ -direction). Andy moves $1$ unit and then turns $90^{\circ}$ left. From there, Andy moves $2$ units (north) and then turns $90^{\circ}$ left. He then moves $3$ units (west) and again turns $90^{\circ}$ left. Andy continues his progress, increasing his distance each time by $1$ unit and always turning left. What is the location of the point at which Andy makes the $2020$ th left turn?

$\textbf{(A)}\ (-1030, -994)\qquad\textbf{(B)}\ (-1030, -990)\qquad\textbf{(C)}\ (-1026, -994)\qquad\textbf{(D)}\ (-1026, -990)\qquad\textbf{(E)}\ (-1022, -994)$

## Solution 1 (Associative Property)
Andy makes a total of $2020$ moves: $1010$ horizontal ( $505$ left and $505$ right) and $1010$ vertical ( $505$ up and $505$ down).
The $x$ -coordinate of Andy's final position is \[-20+\overbrace{\underbrace{1-3}_{-2}+\underbrace{5-7}_{-2}+\underbrace{9-11}_{-2}+\cdots+\underbrace{2017-2019}_{-2}}^{\text{1010 terms, 505 pairs}}=-20-2\cdot505=-1030.\] The $y$ -coordinate of Andy's final position is \[20+\overbrace{\underbrace{2-4}_{-2}+\underbrace{6-8}_{-2}+\underbrace{10-12}_{-2}+\cdots+\underbrace{2018-2020}_{-2}}^{\text{1010 terms, 505 pairs}}=20-2\cdot505=-990.\] Together, we have $(x,y)=\boxed{\textbf{(B)}\ (-1030, -990)}.$
~MRENTHUSIASM

## Solution 2 (Pattern)
You can find that every four moves both coordinates decrease by $2.$ Therefore, both coordinates need to decrease by two $505$ times. You subtract, giving you the answer of $\boxed{\textbf{(B)}\ (-1030, -990)}.$
~happykeeper

## Solution 3 (Pattern)
Let's first mark the first few points Andy will arrive at:
Starting Point ( $0^{\text{th}}$ move): $(-20,20)$
$1^{\text{st}}$ move: $(-19,20)$
$2^{\text{nd}}$ move: $(-19,22)$
$3^{\text{rd}}$ move: $(-22,22)$
$4^{\text{th}}$ move: $(-22,18)$
$5^{\text{th}}$ move: $(-17,18)$
$6^{\text{th}}$ move: $(-17,24)$
$7^{\text{th}}$ move: $(-24, 24)$
In the $3^{\text{rd}}$ move Andy lands on $(-22,22)$ , in the $7^{\text{th}}$ move, Andy lands on $(-24, 24)$ .
There is a pattern, for every $4$ moves (starting from the $3^{\text{rd}}$ move), Andy will arrive on a coordinate in the form of $(-2n, 2n)$ . From this we can deduce:
$(1) \ 3^{\text{rd}}$ move: $(-22,22)$
$(2) \ 7^{\text{th}}$ move: $(-24, 24)$
$(3) \ 11^{\text{th}}$ move: $(-26, 26)$
$(4) \ 15^{\text{th}}$ move: $(-28, 28)$
$(n) \ (4n-1)^{\text{th}}$ move: $(-20-2n, 20+2n)$
We have $2019 = 4 \cdot 505 -1$ , for which $n = 505$ and $20 + 2 \cdot 505 = 1030$ . So, on the $2019^{\text{th}}$ move Andy is at $(-1030, 1030)$ .
Because the problem asks for the $2020^{\text{th}}$ move, $1030-2020=-990$ , on the $2020^{\text{th}}$ move, Andy will be on $\boxed{\textbf{(B)}\ (-1030, -990)}$ .
~ isabelchen

## Solution 4 (Answer Choices)
Drawing the spiral out, you obtain that every 4th turn occurs on the bottom left corner, whose coordinates difference stay the same(40):
(-20, 20) (-22, 18) (-24, 16) ...
So the X and Y coordinates will always have a difference of 40.
Now looking at the answer choices, only answer choice B's X and Y coordinates have a difference of 40, there (B) is the answer. :)
~Alan

## Video Solution (HOW TO CRITICALLY THINK!!!)
https://youtu.be/gbnWUskoOuU
~Education, the Study of Everything

## Video Solution
https://youtu.be/t6yjfKXpwDs?t=413
### Similar Problem
2015 AMC 10B Problem 24 https://artofproblemsolving.com/wiki/index.php/2015_AMC_10B_Problems/Problem_24
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .