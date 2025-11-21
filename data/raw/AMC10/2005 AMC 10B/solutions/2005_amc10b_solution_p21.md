# 2005 AMC 10B Problem 21

## Problem

Forty slips are placed into a hat, each bearing a number $1$ , $2$ , $3$ , $4$ , $5$ , $6$ , $7$ , $8$ , $9$ , or $10$ , with each number entered on four slips. Four slips are drawn from the hat at random and without replacement. Let $p$ be the probability that all four slips bear the same number. Let $q$ be the probability that two of the slips bear a number $a$ and the other two bear a number $b \neq a$ . What is the value of $q/p$ ?

$\textbf{(A) } 162 \qquad \textbf{(B) } 180 \qquad \textbf{(C) } 324 \qquad \textbf{(D) } 360 \qquad \textbf{(E) } 720$

## Solution 1 (where the order of drawing slips matters)
There are $10$ ways to determine which number to pick. There are $4!$ ways to then draw those four slips with that number, and $40 \cdot 39 \cdot 38 \cdot 37$ total ways to draw four slips. Thus $p = \frac{10\cdot 4!}{40 \cdot 39 \cdot 38 \cdot 37}$ .
There are ${10 \choose 2} = 45$ ways to determine which two numbers to pick for the second probability. There are ${4 \choose 2} = 6$ ways to arrange the order which we draw the non-equal slips, and in each order there are $4 \times 3 \times 4 \times 3$ ways to pick the slips, so $q = \frac{45 \cdot 6 \cdot 4^2 \cdot 3^2}{40 \cdot 39 \cdot 38 \cdot 37}$ .
Hence, the answer is $\frac{q}{p} = \frac{45 \cdot 6 \cdot 4^2 \cdot 3^2}{10\cdot 4!} = \boxed{\textbf{(A) }162}$ .

## Solution 2 (where the order does not matter)
For probability $p$ , there are $\binom{10}{1}=10$ ways to choose the number you want to show up $4$ times.
Hence, the probability is $\frac{10}{\binom{40}{4}}$ .
For probability $q$ , there are $\binom{10}{2}=45$ ways to choose the $2$ numbers you want to show up twice. There are $\binom{4}{2}\cdot\binom{4}{2}$ ways to pick which slips you want out of the $4$ of each.
Hence, the probability is $\frac{45\cdot6\cdot6}{\binom{40}{4}}$
Hence, $\frac{q}{p}=\frac{45\cdot6\cdot6}{10}=9\cdot6\cdot3=\boxed{\textbf{(A) }162}$ .

## Video Solution by OmegaLearn
https://youtu.be/wopflrvUN2c?t=252
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=HVUV6NgH3wU ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .