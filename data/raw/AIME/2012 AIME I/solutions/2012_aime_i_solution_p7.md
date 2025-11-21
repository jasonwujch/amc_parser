# 2012 AIME I Problem 7

## Problem

At each of the sixteen circles in the network below stands a student. A total of $3360$ coins are distributed among the sixteen students. All at once, all students give away all their coins by passing an equal number of coins to each of their neighbors in the network. After the trade, all students have the same number of coins as they started with. Find the number of coins the student standing at the center circle had originally.

## Solution 1
Say the student in the center starts out with $a$ coins, the students neighboring the center student each start with $b$ coins, and all other students start out with $c$ coins. Then the $a$ -coin student has five neighbors, all the $b$ -coin students have three neighbors, and all the $c$ -coin students have four neighbors.
Now in order for each student's number of coins to remain equal after the trade, the number of coins given by each student must be equal to the number received, and thus
\begin{align*} a &= 5 \cdot \frac{b}{3}\\ b &= \frac{a}{5} + 2 \cdot \frac{c}{4}\\ c &= 2 \cdot \frac{c}{4} + 2 \cdot \frac{b}{3}. \end{align*}
Solving these equations, we see that $\frac{a}{5} = \frac{b}{3} = \frac{c}{4}.$ Also, the total number of coins is $a + 5b + 10c = 3360,$ so $a + 5 \cdot \frac{3a}{5} + 10 \cdot \frac{4a}{5} = 3360 \rightarrow a = \frac{3360}{12} = \boxed{280}.$
- One way to make this more rigorous (answering the concern in Solution 3) is to let $a$ , $b$ , and $c$ represent the $total$ number of coins in the rings. Then, you don't care about individual people in the passing, you just know that each ring gets some coins and loses some coins, which must cancel each other out.

## Solution 2
Since the students give the same number of gifts of coins as they receive and still end up the same number of coins, we can assume that every gift of coins has the same number of coins. Let $x$ be the number of coins in each gift of coins. There $10$ people who give $4$ gifts of coins, $5$ people who give $3$ gifts of coins, and $1$ person who gives $5$ gifts of coins. Thus,
\begin{align*} 10(4x)+5(3x)+5x &= 3360\\ 40x+15x+5x &= 3360\\ 60x &= 3360\\ x &= 56 \end{align*} Therefore the answer is $5(56) = \boxed{280}.$

## Solution 3
Mark the number of coins from inside to outside as $a$ , $b_1$ , $b_2$ , $b_3$ , $b_4$ , $b_5$ , $c_1$ , $c_2$ , $c_3$ , $c_4$ , $c_5$ , $d_1$ , $d_2$ , $d_3$ , $d_4$ , $d_5$ . Then, we obtain \begin{align*} d_1 &= \frac{d_5}{4} + \frac{d_2}{4} + \frac{c_1}{4} + \frac{c_2}{4}\\ d_2 &= \frac{d_1}{4} + \frac{d_3}{4} + \frac{c_2}{4} + \frac{c_3}{4}\\ d_3 &= \frac{d_2}{4} + \frac{d_4}{4} + \frac{c_3}{4} + \frac{c_4}{4}\\ d_4 &= \frac{d_3}{4} + \frac{d_5}{4} + \frac{c_4}{4} + \frac{c_5}{4}\\ d_5 &= \frac{d_4}{4} + \frac{d_1}{4} + \frac{c_5}{4} + \frac{c_1}{4}\\ \end{align*} Letting $D = d_1 + d_2 + d_3 + d_4 + d_5$ , $C = c_1 + c_2 + c_3 + c_4 + c_5$ gets us $D = \frac{D}{4} + \frac{D}{4} + \frac{C}{4} + \frac{C}{4}$ and $D = C$ . In the same way, $C = \frac{D}{4} + \frac{D}{4} + \frac{B}{3} + \frac{B}{3}$ , $B = \frac{3D}{4}$ , $B = \frac{C}{4} + \frac{C}{4} + a$ , $a = \frac{D}{4}$ . Then, with $a + B + C + D = 3360$ , $D = 1120$ , $a = \boxed{280}$ .

## Solution 4
Define $x$ as the number of coins the student in the middle has. Since this student connects to $5$ other students, each of those students must have passed $\dfrac15 x$ coins to the center to maintain the same number of coins.
Each of these students connect to $3$ other students, passing $\dfrac15 x$ coins to each, so they must have $\dfrac35 x$ coins. These students must then recieve $\dfrac35 x$ coins, $\dfrac 15 x$ of which were given to by the center student. Thus, they must also have received $\dfrac25 x$ coins from the outer layer, and since this figure has symmetry, these must be the same.
Each of the next layer of students must have given $\dfrac15 x$ coins. Since they gave $4$ people coins, they must have started with $\dfrac45 x$ coins. They received $\dfrac25 x$ of them from the inner layer, making the two other connections have given them the same amount. By a similar argument, they recieved $\dfrac15 x$ from each of them.
By a similar argument, the outermost hexagon of students must have had $\dfrac45 x$ coins each. Summing this all up, we get the number of total coins passed out as a function of $x$ . This ends up to be \begin{align*} \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac45 x + \dfrac35 x + \dfrac35 x + \dfrac35 x + \dfrac35 x + \dfrac35 x + x &= 10 \cdot \dfrac45 x + 5 \cdot \dfrac35 x + x \\ &= 8x + 3x + x \\ &= 12 x. \end{align*}
Since this all sums up to $3360$ , which is given, we find that \begin{align*} 12x &= 3360 \\ x &= 280 \end{align*}
We defined $x$ to be the number of coins that the center person has, so the answer is $x$ , which is $\boxed{280}$

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/343
~ dolphin7
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .