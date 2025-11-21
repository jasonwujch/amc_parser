# 2007 AIME I Problem 6

## Problem

A frog is placed at the origin on the number line , and moves according to the following rule: in a given move, the frog advances to either the closest point with a greater integer coordinate that is a multiple of 3, or to the closest point with a greater integer coordinate that is a multiple of 13. A move sequence is a sequence of coordinates that correspond to valid moves, beginning with 0 and ending with 39. For example, $0,\ 3,\ 6,\ 13,\ 15,\ 26,\ 39$ is a move sequence. How many move sequences are possible for the frog?

## Solution

## Solution 1
Let us keep a careful tree of the possible number of paths around every multiple of $13$ .
From $0 \Rightarrow 13$ , we can end at either $12$ (mult. of 3) or $13$ (mult. of 13).
- Only $1$ path leads to $12$ Continuing from , there is way to continue to There are ways to reach .
- There are $\frac{12 - 0}{3} + 1 = 5$ ways to reach $13$ . Continuing from , there are ways to get to There are ways (the first 1 to make it inclusive, the second to also jump from ) to get to .
- Continuing from $12$ , there is $1 \cdot 1 = 1$ way to continue to $24$
- There are $1 \cdot \left(\frac{24-15}{3} + 1\right) = 4$ ways to reach $26$ .
- Continuing from $13$ , there are $5 \cdot 1 = 5$ ways to get to $24$
- There are $5 \cdot \left(\frac{24-15}{3} + 1 + 1\right) = 25$ ways (the first 1 to make it inclusive, the second to also jump from $13 \Rightarrow 26$ ) to get to $26$ .
Regrouping, work from $24 | 26\Rightarrow 39$
- There are $1 + 5 = 6$ ways to get to $24$ Continuing from , there are ways to continue to .
- There are $4 + 25 = 29$ ways to reach $26$ . Continuing from , there are (note that the 1 is not to inclusive, but to count ).
- Continuing from $24$ , there are $6 \cdot \left(\frac{39 - 27}{3}\right) = 24$ ways to continue to $39$ .
- Continuing from $26$ , there are $29 \cdot \left(\frac{39-27}{3} + 1\right) = 145$ (note that the 1 is not to inclusive, but to count $26 \Rightarrow 39$ ).
In total, we get $145 + 24 = 169$ .
In summary, we can draw the following tree, where in $(x,y)$ , $x$ represents the current position on the number line, and $y$ represents the number of paths to get there:
- $(12,1)$
- $(24,1)$
- $(26,4)$
- $(39,4)$
- $(39,20)$
- $(13,5)$
- $(24,5)$
- $(26,25)$
- $(39,20)$
- $(39,125)$
Again, this totals $4 + 20 + 20 + 125 = 169$ .

## Solution 2
We divide it into 3 stages. The first occurs before the frog moves past 13. The second occurs before it moves past 26, and the last is everything else.
For the first stage the possible paths are $(0,13)$ , $(0,3,13)$ , $(0,3,6,13)$ , $(0,3,6,9,13)$ , $(0,3,6,9,12,13)$ , and $(0,3,6,9,12)$ . That is a total of 6.
For the second stage the possible paths are $(26)$ , $(15,26)$ , $(15,18,26)$ , $(15,18,21,26)$ , $(15,18,21,24,26)$ , and $(15,18,21,24)$ . That is a total of 6.
For the third stage the possible paths are $(39)$ , $(27,39)$ , $(27,30,39)$ , $(27,30,33,39)$ , and $(27,30,33,36,39)$ . That is a total of 5.
However, we cannot jump from $12 \Rightarrow 26$ (this eliminates 5 paths) or $24 \Rightarrow 39$ (this eliminates 6 paths), so we must subtract $6 + 5 = 11$ .
The answer is $6*6*5 - 11=169$

## Solution 3
Another way would be to use a table representing the number of ways to reach a certain number
$\begin{tabular}{c|c|c|c|c|c|c|c|c|c|c|c|c|c|c} 0 & 3 & 6 & 9 & 12 & 13 & 15 & 18 & 21 & 24 & 26 & 27 & 30 & 33 & 36 \\ \hline 1 & 1 & 1 & 1 & 1 & 5 & 6 & 6 & 6 & 6 & 29 & 35 & 35 & 35 & 35 \\ \end{tabular}$
How we came with each value is to just add in the number of ways that we can reach that number from previous numbers. For example, for $26$ , we can reach it from $13, 15, 18, 21, 24$ , so we add all those values to get the value for $26$ . For $27$ , it is only reachable from $24$ or $26$ , so we have $29 + 6 = 35$ .
The answer for $39$ can be computed in a similar way to get $35 * 4 + 29 = \boxed{169}$ .

## Solution 4
I believe this is an easier way of organizing the solution to reduce the possibility of mistakes. This is a highly visual solution, so it's much easier to record than a tree or table.
Here is my diagram to help you see what I did: https://drive.google.com/file/d/1Gk_cziYvoeg--uVTap5FGOds3SEfiDAW/view?usp=sharing
Using graph paper, draw a number line from 0-39. On one line, dot every multiple of 3. Then on a line below it, dot every multiple of 13. This way you can clearly see which goes before or after which.
To make it easier to understand, I'll compare these jumps to a train system. Imagine that every multiple of 3 is a short transit, while the multiples of 13 are long transits; because of the possibility to skip a large section in one move. As we continue, picture each "transit" of 13 to be an option, like a switch. If you are the frog that are riding these trains, you would probably think like this: "I could use the first long transit, skip the second, and use the third. Or, I could skip both first and second and use only the third. etc.) From now on I'll be calling the multiples of 13: 13, 26, and 39, as stations 1, 2, and 3 for clarity.
Thinking like this organizes the problem efficiently into $2^3$ cases, where you could choose which "long transits" to ride. We will start with the harder cases and move downwards. Write out each of the 8 cases to record each one. Once we do the hardest case, which is the first one, every preceding one will be easier with the knowledge we gather.
Case #1: 111
You have 5 locations to choose to jump to station 1. From the start (0), 3, 6, 9, or 12. The same goes for station #2, with 13, 15, 18, 21, or 24. However, station #3 is tricky. You can jump from 26, 27, 30, or 33, but if you jumped from 36, then that could qualify as skipping jumping station #3, because station #3 is both a multiple of 3 and a multiple of 13. For example, if you jumped from 36 as your last move, then those moves are essentially the same as case 110.
So, $5*5*4=100$ .
Case #2: 110
Start with what you did on case #1, but when you reach station 2 continue only jumping multiples of 3 to 39.
$5*5=25$
Case #3: 101
We have the 5 original choices, and when you reach station #1, move to 27 on the number line, slightly ahead of station #2. Here is another tricky part. Since we did not start on station 2 like we did in case #1, there are only 3 cases instead of 4.
$5*3=15$
Case #4: 100
This one is simple.
$5$
Case #5: 011
Jump multiples of 3 to get to 15, where you will have 4 locations to jump to station 2, and another 4 choices to reach station 3.
$4*4=16$
Case #6: 010
This one is also simple. Once you reach 15 there are only 4 choices.
$4$
Case #7: 001
It only gets simpler. You can only jump at 27, 30, or 33.
$3$
Case #8: 000
Simple jumps.
$1$
You have reached the end! $100+25+15+5+16+4+3+1=\boxed{169}$ .
-jackshi2006

## Solution 5 (Recursionish)
Let $f(n)$ be the number of ways one can get to $39$ starting at position $n.$ We wish to compute $f(0).$ Now it's just a long simplifications until you get to $f(36) = 1.$ We have \[f(0) = f(3) + f(13) = f(6) +2f(13) + f(9) + 3f(12) + f(12) + 4f(12) + f(15) + 5f(12).\]
Most of these steps are valid since at any $n$ that is a multiple of $3$ we can either go to the next multiple of $3$ or we can skip to the next multiple of $13$ which is simply $13.$
From these equations we have deduced $f(0) = f(15) + 5f(12).$ Continuing we have \[f(15) + 5f(12) = f(15) + 5(f(26) +f(15) = 5f(26) + 6f(15) = 5f(26)+ 6f(26) + 6f(18) = 5f(26) + 12f(26) + 6f(21) = 5f(26) + 18f(26) + 6f(24) = 5f(26) + 24f(26) + 6f(27) = 29f(26) + 6f(27).\]
Finally, note that $f(26) = 1 + f(27) = 2 + f(30) = 3+f(33) = 4+f(36) = 5$ since at any point we can either go to the next multiple of $3$ or go to the next multiple of $13$ which happens to be $39.$ Therefore $f(26) = 5.$ Similarly we find $f(27) = 1+f(30) = 2 + f(33) = 3+f(36) = 4$ so the end answer is $5 \cdot 29 + 6 \cdot 4 = \boxed{169}.$

## Solution 6(Star Wars Solution)
Another way you can visualize the problem is by thinking of points $13$ , $26$ , and $39$ as planets and all multiples of 3 as points at which your spaceship can jump to hyperspace. Given that you wish to visit planet $39$ , you can choose to visit planets $13$ or $26$ along the way.
Case 1: Neither
There are $4$ ways to jump to $39$ from hyperspace.
Case 2: Only planet $13$
There are $5$ ways to jump to planet $13$ and $4$ ways to jump to planet $39$ . $20$ ways total.
Case 3: Only planet $26$ .
There are $4$ ways to jump to planet $26$ and $5$ ways to jump to planet $39$ . $20$ ways total.
Case 4: Both
There are $5$ ways to jump to $13$ , $5$ ways to jump to $26$ , and $5$ ways to jump to $39$ . $125$ ways total.
Therefore, there are $4+20+20+125=\boxed{169}$ ways to jump to 39 through various journeys in hyperspace.
-alanisawesome2018
These problems are copyrighted © by the Mathematical Association of America.