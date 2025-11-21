# 2019 AIME I Problem 5

## Problem

A moving particle starts at the point $(4,4)$ and moves until it hits one of the coordinate axes for the first time. When the particle is at the point $(a,b)$ , it moves at random to one of the points $(a-1,b)$ , $(a,b-1)$ , or $(a-1,b-1)$ , each with probability $\frac{1}{3}$ , independently of its previous moves. The probability that it will hit the coordinate axes at $(0,0)$ is $\frac{m}{3^n}$ , where $m$ and $n$ are positive integers such that $m$ is not divisible by $3$ . Find $m + n$ .

## Solution 1
One could recursively compute the probabilities of reaching $(0,0)$ as the first axes point from any point $(x,y)$ as \[P(x,y) = \frac{1}{3} P(x-1,y) + \frac{1}{3} P(x,y-1) + \frac{1}{3} P(x-1,y-1)\] for $x,y \geq 1,$ and the base cases are $P(0,0) = 1, P(x,0) = P(y,0) = 0$ for any $x,y$ not equal to zero. We then recursively find $P(4,4) = \frac{245}{2187}$ so the answer is $245 + 7 = \boxed{252}$ .
If this algebra seems intimidating, you can watch a nice pictorial explanation of this by On The Spot Stem. https://www.youtube.com/watch?v=XBRuy3_TM9w

## Solution 2
Obviously, the only way to reach (0,0) is to get to (1,1) and then have a $\frac{1}{3}$ chance to get to (0,0). Let x denote a move left 1 unit, y denote a move down 1 unit, and z denote a move left and down one unit each. The possible cases for these moves are $(x,y,z)=(0,0,3),(1,1,2),(2,2,1)$ and $(3,3,0)$ . This gives a probability of $1 \cdot \frac{1}{27} + \frac{4!}{2!} \cdot \frac{1}{81} + \frac{5!}{2! \cdot 2!} \cdot \frac{1}{243} +\frac{6!}{3! \cdot 3!} \cdot \frac{1}{729}=\frac{245}{729}$ to get to $(1,1)$ . The probability of reaching $(0,0)$ is $\frac{245}{3^7}$ . This gives $245+7=\boxed{252}$ .

## Solution 3
Since the particle stops at one of the axes, we know that the particle must pass through $(1,1)$ . Thus, it suffices to consider the probability our particle will reach $(1,1)$ . Then the only ways to get to $(1,1)$ from $(4,4)$ are the following:
(1) 3 moves diagonally
(2) 2 moves diagonally, 1 move left, 1 move down
(3) 1 move diagonally, 2 moves left and 2 moves down.
(4) 3 moves left, 3 moves down.
The probability of (1) is $\frac{1}{3^3}$ . The probability of (2) is $\frac{\frac{4!}{2!}}{3^4} = \frac{12}{3^4}$ . The probability of (3) is $\frac{\frac{5!}{2!2!}}{3^5} = \frac{30}{3^5}$ . The probability of (4) is $\frac{\frac{6!}{3!3!}}{3^6} = \frac{20}{3^6}$ . Adding all of these together, we obtain a total probability of $\frac{245}{3^6}$ that our particle will hit $(1,1)$ . Trivially, there is a $\frac{1}{3}$ chance our particle will hit $(0,0)$ from $(1,1)$ . So our final probability will be $\frac{245}{3^6} \cdot \frac{1}{3} = \frac{245}{3^7} \implies m = 245, n = 7 \implies \boxed{252}$
~NotSoTrivial

## Solution 4 (Official MAA)
All paths that first hit the axes at the origin must pass through the point $(1,1)$ . There are $63$ paths from the point $(4,4)$ to the point $(1,1)$ : $\tbinom{6}{3}=20$ that take $3$ steps left and $3$ steps down, $\tbinom{5}{2\,2\,1}=30$ that take $2$ steps left, $2$ steps down, and $1$ diagonal step, $\tbinom{4}{1\,1\,2}=12$ steps that take $1$ step left, $1$ steps down, and $2$ diagonal steps, and $1$ that takes $3$ diagonal steps. The total probability of moving from $(4,4)$ to $(1,1)$ is therefore \[\frac{1}{3^6}\cdot20+\frac{1}{3^5}\cdot30+\frac{1}{3^4}\cdot12+\frac{1}{3^3}\cdot1=\frac{245}{3^6}.\] Multiplying by $\tfrac13$ gives $\tfrac{245}{3^7},$ the probability that the path first reaches the axes at the origin. The requested sum is $245+7=252$ .

## Video Solution #1(A nice visual explanation)
https://youtu.be/JQdad7APQG8?t=1340

## Video Solution
Unique solution: https://youtu.be/I-8xZGhoDUY
~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .