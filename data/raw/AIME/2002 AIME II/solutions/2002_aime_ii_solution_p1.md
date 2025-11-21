# 2002 AIME II Problem 1

## Problem

Given that \begin{eqnarray*}&(1)& x\text{ and }y\text{ are both integers between 100 and 999, inclusive;}\qquad \qquad \qquad \qquad \qquad \\ &(2)& y\text{ is the number formed by reversing the digits of }x\text{; and}\\ &(3)& z=|x-y|. \end{eqnarray*}

How many distinct values of $z$ are possible?

## Solution
We express the numbers as $x=100a+10b+c$ and $y=100c+10b+a$ . From this, we have \begin{eqnarray*}z&=&|100a+10b+c-100c-10b-a|\\&=&|99a-99c|\\&=&99|a-c|\\ \end{eqnarray*} Because $a$ and $c$ are digits, and $a$ and $c$ are both between 1 and 9 (from condition 1), there are $\boxed{009}$ possible values (since all digits except $9$ can be expressed this way).
These problems are copyrighted © by the Mathematical Association of America.