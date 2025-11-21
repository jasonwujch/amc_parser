# 2018 AIME I Problem 2

## Problem

The number $n$ can be written in base $14$ as $\underline{a}\text{ }\underline{b}\text{ }\underline{c}$ , can be written in base $15$ as $\underline{a}\text{ }\underline{c}\text{ }\underline{b}$ , and can be written in base $6$ as $\underline{a}\text{ }\underline{c}\text{ }\underline{a}\text{ }\underline{c}\text{ }$ , where $a > 0$ . Find the base- $10$ representation of $n$ .

## Solution 1
We have these equations: $196a+14b+c=225a+15c+b=222a+37c$ . Taking the last two we get $3a+b=22c$ . Because $c \neq 0$ otherwise $a \ngtr 0$ , and $a \leq 5$ , $c=1$ .
Then we know $3a+b=22$ . Taking the first two equations we see that $29a+14c=13b$ . Combining the two gives $a=4, b=10, c=1$ . Then we see that $222 \times 4+37 \times1=\boxed{925}$ .

## Solution 2
We know that $196a+14b+c=225a+15c+b=222a+37c$ . Combining the first and third equations give that $196a+14b+c=222a+37c$ , or \[7b=13a+18c\] The second and third gives $222a+37c=225a+15c+b$ , or \[22c-3a=b\] \[154c-21a=7b=13a+18c\] \[4c=a\] We can have $a=4,8,12,16,20$ , but only $a=4$ falls within the possible digits of base $6$ . Thus $a=4$ , $c=1$ , and thus you can find $b$ which equals $10$ . Thus, our answer is $4\cdot225+1\cdot15+10=\boxed{925}$ . ~SHEN KISLAY KAI 2023

## Solution 3 (Official MAA)
The problem is equivalent to finding a solution to the system of Diophantine equations $196a+14b+c=225a+15c+b$ and $225a+15c+b=216a+36c+6a+c,$ where $1\le a\le 5,\,0\le b\le 13,$ and $0\le c\le 5.$ Simplifying the second equation gives $b=22c-3a.$ Substituting for $b$ in the first equation and simplifying then gives $a=4c,$ so $a = 4$ and $c = 1,$ and the base- $10$ representation of $n$ is $222 \cdot 4 + 37 \cdot 1 = 925.$ It may be verified that $b=10\le 13.$

## Solution 4 (Simple Modular Arithmetic)
We're given that $196a+14b+c=225a+15c+b=222a+37c.$ By taking the difference of the first $2$ equalities, we receive $29a+14c=13b.$ Taking $\pmod{13}$ , we receive $3a+c \equiv 0 \pmod{13}.$ We receive the following cases: $(a,c)=(4,1)$ or $(3,4).$ (Note that $(2,7)$ doesn't work since $a,c<6$ by third condition). We can just check these two, and find that $(a,b,c)=(4,10,1),$ and just plugging in $(a,c)$ into the third expression we receive $888+37=\boxed{925}.$
~SirAppel

## Video Solution
https://www.youtube.com/watch?v=WVtbD8x9fCM ~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .