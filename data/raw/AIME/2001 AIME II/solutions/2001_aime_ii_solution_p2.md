# 2001 AIME II Problem 2

## Problem

Each of the $2001$ students at a high school studies either Spanish or French, and some study both. The number who study Spanish is between $80$ percent and $85$ percent of the school population, and the number who study French is between $30$ percent and $40$ percent. Let $m$ be the smallest number of students who could study both languages, and let $M$ be the largest number of students who could study both languages. Find $M-m$ .

## Solution
Let $S$ be the percent of people who study Spanish, $F$ be the number of people who study French, and let $S \cap F$ be the number of students who study both. Then $\left\lceil 80\% \cdot 2001 \right\rceil = 1601 \le S \le \left\lfloor 85\% \cdot 2001 \right\rfloor = 1700$ , and $\left\lceil 30\% \cdot 2001 \right\rceil = 601 \le F \le \left\lfloor 40\% \cdot 2001 \right\rfloor = 800$ . By the Principle of Inclusion-Exclusion ,
\[S+F- S \cap F = S \cup F = 2001\]
For $m = S \cap F$ to be smallest, $S$ and $F$ must be minimized.
\[1601 + 601 - m = 2001 \Longrightarrow m = 201\]
For $M = S \cap F$ to be largest, $S$ and $F$ must be maximized.
\[1700 + 800 - M = 2001 \Longrightarrow M = 499\]
Therefore, the answer is $M - m = 499 - 201 = \boxed{298}$ .

## Solution 2 (What?)
I have no clue what is going on here. Let $x$ percentage study only Spanish, $y$ study only French and $z$ study both. We have: \[80 \leq x + z \leq 85\] \[30 \leq y + z \leq 40\] \[x + y + z = 100\] \[\implies 10 \leq z \leq 25\] Thus the desired answer should be $2001 \cdot (\frac{25}{100} - \frac{10}{100}) = 300.15$ . That's a decimal, and this is an integer type contest. In search of an answer, the individual above has rounded upwards. I do not know if that was specified in the contest, because it was not specified in the problem.
These problems are copyrighted © by the Mathematical Association of America.