# 2007 AIME II Problem 1

## Problem

A mathematical organization is producing a set of commemorative license plates. Each plate contains a sequence of five characters chosen from the four letters in AIME and the four digits in 2007. No character may appear in a sequence more times than it appears among the four letters in AIME or the four digits in 2007. A set of plates in which each possible sequence appears exactly once contains N license plates. Find $\frac{N}{10}$ .

## Solution
There are 7 different characters that can be picked, with 0 being the only number that can be repeated twice.
- If $0$ appears 0 or 1 times amongst the sequence, there are $\frac{7!}{(7-5)!} = 2520$ sequences possible.
- If $0$ appears twice in the sequence, there are ${5\choose2} = 10$ places to place the $0$ s. There are $\frac{6!}{(6-3)!} = 120$ ways to place the remaining three characters. In total, that gives us $10 \cdot 120 = 1200$ .
Thus, $N = 2520 + 1200 = 3720$ , and $\frac{N}{10} = \boxed{372}$ .
These problems are copyrighted © by the Mathematical Association of America.