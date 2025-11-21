# 2022 AMC 8 Problem 25

## Problem

A cricket randomly hops between $4$ leaves, on each turn hopping to one of the other $3$ leaves with equal probability. After $4$ hops what is the probability that the cricket has returned to the leaf where it started?

$\textbf{(A) }\frac{2}{9}\qquad\textbf{(B) }\frac{19}{80}\qquad\textbf{(C) }\frac{20}{81}\qquad\textbf{(D) }\frac{1}{4}\qquad\textbf{(E) }\frac{7}{27}$

## Solution 1 (Casework)
Let $A$ denote the leaf where the cricket starts and $B$ denote one of the other $3$ leaves. Note that:
We apply casework to the possible paths of the cricket:
The probability for this case is $1\cdot\frac13\cdot1\cdot\frac13=\frac19.$
The probability for this case is $1\cdot\frac23\cdot\frac23\cdot\frac13=\frac{4}{27}.$
Together, the probability that the cricket returns to $A$ after $4$ hops is $\frac19+\frac{4}{27}=\boxed{\textbf{(E) }\frac{7}{27}}.$
~MRENTHUSIASM

## Solution 2 (Casework)
We can label the leaves as shown below:
Carefully counting cases, we see that there are $7$ ways for the cricket to return to leaf $A$ after four hops if its first hop was to leaf $B$ :
By symmetry, we know that there are $7$ ways if the cricket's first hop was to leaf $C$ , and there are $7$ ways if the cricket's first hop was to leaf $D$ . So, there are $21$ ways in total for the cricket to return to leaf $A$ after four hops.
Since there are $3^4 = 81$ possible ways altogether for the cricket to hop to any other leaf four times, the answer is $\frac{21}{81} = \boxed{\textbf{(E) }\frac{7}{27}}$ .
~mahaler

## Solution 3 (Complement)
There are always three possible leaves to jump to every time the cricket decides to jump, so there is a total number of $3^4$ routes. Let $A$ denote the leaf cricket starts at, and $B, C, D$ be the other leaves. If we want the cricket to move to leaf $A$ for its last jump, the cricket cannot jump to leaf $A$ for its third jump. Also, considering that the cricket starts at leaf $A$ , he cannot jump to leaf $A$ for its first jump. Note that there are $3\cdot2=6$ paths if the cricket moves to leaf $A$ for its third jump. Therefore, we can conclude that the total number of possible paths for the cricket to return to leaf $A$ after four jumps is $3^3 - 6 = 21$ , so the answer is $\frac{21}{3^4} = \frac{21}{81}=\boxed{\textbf{(E) }\frac{7}{27}}$ .
~ Bloggish

## Solution 4 (Recursion)
Denote $P_n$ to be the probability that the cricket would return back to the first point after $n$ hops. Then, we get the recursive formula \[P_n = \frac13(1-P_{n-1})\] because if the leaf is not on the target leaf, then there is a $\frac13$ probability that it will make it back.
With this formula and the fact that $P_1=0$ (After one hop, the cricket can never be back to the target leaf.), we have \[P_2 = \frac13, P_3 = \frac29, P_4 = \frac7{27},\] so our answer is $\boxed{\textbf{(E) }\frac{7}{27}}$ .
~wamofan

## Solution 5 (Dynamic Programming)
Let $A$ denote the leaf cricket starts at, and $B, C, D$ be the other leaves, similar to Solution 2.
Let $A(n)$ be the probability the cricket lands on $A$ after $n$ hops, $B(n)$ be the probability the cricket lands on $B$ after crawling $n$ hops, etc.
Note that $A(1)=0$ and $B(1)=C(1)=D(1)=\frac13.$ For $n\geq2,$ the probability that the cricket land on each leaf after $n$ hops is $\frac13$ the sum of the probability the cricket land on other leaves after $n-1$ hops. So, we have \begin{align*} A(n) &= \frac13 \cdot [B(n-1) + C(n-1) + D(n-1)], \\ B(n) &= \frac13 \cdot [A(n-1) + C(n-1) + D(n-1)], \\ C(n) &= \frac13 \cdot [A(n-1) + B(n-1) + D(n-1)], \\ D(n) &= \frac13 \cdot [A(n-1) + B(n-1) + C(n-1)]. \end{align*} It follows that $A(n) = B(n-1) = C(n-1) = D(n-1).$
We construct the following table: \[\begin{array}{c|cccc} & & & & \\ [-2ex] n & A(n) & B(n) & C(n) & D(n) \\ [1ex] \hline & & & & \\ [-1ex] 1 & 0 & \frac13 & \frac13 & \frac13 \\ & & & & \\ 2 & \frac13 & \frac29 & \frac29 & \frac29 \\ & & & & \\ 3 & \frac29 & \frac{7}{27} & \frac{7}{27} & \frac{7}{27} \\ & & & & \\ 4 & \frac{7}{27} & \frac{20}{81} & \frac{20}{81} & \frac{20}{81} \\ [1ex] \end{array}\] Therefore, the answer is $A(4)=\boxed{\textbf{(E) }\frac{7}{27}}$ .
~ isabelchen

## Solution 6 (Generating Function)
Assign the leaves to $0, 1, 2,$ and $3$ modulo $4,$ and let $0$ be the starting leaf. We then use generating functions with relation to the change of leaves. For example, from $3$ to $1$ would be a change of $2,$ and from $1$ to $2$ would be a change of $1.$ This generating function is equal to $(x+x^2+x^3)^4.$ It is clear that we want the coefficients in the form of $x^{4n},$ where $n$ is a positive integer. One application of roots of unity filter gives us a successful case count of $\frac{81+1+1+1}{4} = 21.$
Therefore, the answer is $\frac{21}{3^4}=\boxed{\textbf{(E) }\frac{7}{27}}.$
~sigma

## Solution 7 (Also Generating Functions)
Let the leaves be $(0,0), (0,1), (1,0),$ and $(1,1)$ on the coordinate plane, with the cricket starting at $(0,0)$ . Then we write a generating function. We denote $x$ a change in the x-value of the cricket, and similarly for $y$ . Then our generating function is $(x+y+xy)^4,$ and we wish to compute the number of terms in which the exponents of both x and y are even. To do this, we first square to get $(x^2 + y^2 + x^2y^2 + 2xy + 2x^2y + 2xy^2)^2$ . Note that every term squared will give even powers for x and y, so that gives us $3 + 4\cdot3 = 15.$ Then every combination of $x^2, y^2,$ and $x^2y^2$ will also give us even powers for x and y, so that yields $6$ more terms, for a total of $21.$ Now in total there $3^4 = 81$ possible sequences, so $21/81$ gives us the answer of $\boxed{\textbf{(E) }\frac{7}{27}}.$
~littlefox_amc
### Remark
This problem is a reduced version of 1985 AIME Problem 12 , changing $7$ steps into $4$ steps.
This problem is also similar to 2003 AIME II Problem 13 .
~ isabelchen

## Video Solution by Mathionaire (Clear and fast solution)
https://www.youtube.com/watch?v=0HNQQDwFUqU
~Mathionaire

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=3442 ~hsnacademy

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/oUEa7AjMF2A?si=n9aPrcW_qLqFC8IF&t=5261
~Math-X

## Video Solution(🚀Under 2 min🚀 Easy logic with all paths color-coded ✨)
https://youtu.be/YiI9szmMWX4
~Education, the Study of Everything

## Video Solution
https://youtu.be/GNFG4cmYDgw

## Video Solution by OmegaLearn
https://youtu.be/kE15Sy0B2Pk?t=633
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=85A6av3oqRo
~Mathematical Dexterity

## Video Solution
https://youtu.be/Ij9pAy6tQSg?t=2588
~Interstigation

## Video Solution
https://www.youtube.com/watch?v=H1zxrkq6DKg
~David

## Video Solution
https://youtu.be/0orAAUaLIO0?t=609
~STEMbreezy

## Video Solution
https://youtu.be/9SKUdTut3l4
~savannahsolver

## Video Solution Using States by SpreadTheMathLove
https://www.youtube.com/watch?v=740Z355PtWs&t=777s

## Video Solution by Dr. David
https://youtu.be/CqFjWscX_kw

## Official Video Solution (Simplified Casework in 2 min!)
https://www.youtube.com/watch?v=kK8YVX559Ko
~TheMathGeek(Plz sub)
### See Also