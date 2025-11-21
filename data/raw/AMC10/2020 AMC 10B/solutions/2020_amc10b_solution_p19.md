# 2020 AMC 10B Problem 19

## Problem

In a certain card game, a player is dealt a hand of $10$ cards from a deck of $52$ distinct cards. The number of distinct (unordered) hands that can be dealt to the player can be written as $158A00A4AA0$ . What is the digit $A$ ?

$\textbf{(A) } 2 \qquad\textbf{(B) } 3 \qquad\textbf{(C) } 4 \qquad\textbf{(D) } 6 \qquad\textbf{(E) } 7$

## Solution 1
$158A00A4AA0 \equiv 1+5+8+A+0+0+A+4+A+A+0 \equiv 4A \pmod{9}$
We're looking for the amount of ways we can get $10$ cards from a deck of $52$ , which is represented by $\binom{52}{10}$ .
$\binom{52}{10}=\frac{52\cdot51\cdot50\cdot49\cdot48\cdot47\cdot46\cdot45\cdot44\cdot43}{10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}$
We need to get rid of the multiples of $3$ , which will subsequently get rid of the multiples of $9$ (if we didn't, the zeroes would mess with the equation since you can't divide by 0)
$9\cdot5=45$ , $8\cdot6=48$ , $\frac{51}{3}$ leaves us with 17.
$\frac{52\cdot\cancel{51}^{17}\cdot50\cdot49\cdot\cancel{48}\cdot47\cdot46\cdot\cancel{45}\cdot44\cdot43}{10\cdot\cancel{9}\cdot\cancel{8}\cdot7\cdot\cancel{6}\cdot\cancel{5}\cdot4\cdot\cancel{3}\cdot2\cdot1}$
Converting these into $\pmod{9}$ , we have
$\binom{52}{10}\equiv \frac{(-2)\cdot(-1)\cdot(-4)\cdot4\cdot2\cdot1\cdot(-1)\cdot(-2)}{1\cdot(-2)\cdot4\cdot2\cdot1} \equiv (-1)\cdot(-4)\cdot(-1)\cdot(-2) \equiv 8 \pmod{9}$
$4A\equiv8\pmod{9} \implies A=\boxed{\textbf{(A) }2}$ ~quacker88

## Solution 1 but easier
We're looking for the amount of ways we can get $10$ cards from a deck of $52$ , which is represented by $\binom{52}{10}$ .
$\binom{52}{10}=\frac{52\cdot51\cdot50\cdot49\cdot48\cdot47\cdot46\cdot45\cdot44\cdot43}{10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}$
And after simplifying, we get $26\cdot17\cdot7\cdot47\cdot46\cdot5\cdot11\cdot43$ . Now, if we examine the number $158A00A4AA0$ , we can notice that it is equal to some number $n$ times 10. Therefore, we can divide 10 from the aforementioned expression and find the units digit, which will be $A$ .
Now, after dividing ten, we will have $26\cdot17\cdot7\cdot47\cdot23\cdot11\cdot43$ . We can then use modulo 10 and find that the unit digit of the expression is $\boxed{\textbf{(A) }2}$ ~lucaswujc

## Solution 2
$\binom{52}{10}=\frac{52\cdot51\cdot50\cdot49\cdot48\cdot47\cdot46\cdot45\cdot44\cdot43}{10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}=26\cdot17\cdot5\cdot7\cdot47\cdot46\cdot11\cdot43$
Since this number is divisible by $4$ but not $8$ , the last $2$ digits must be divisible by $4$ but the last $3$ digits cannot be divisible by $8$ . This narrows the options down to $2$ and $6$ .
Also, the number cannot be divisible by $3$ . Adding up the digits, we get $18+4A$ . If $A=6$ , then the expression equals $42$ , a multiple of $3$ . This would mean that the entire number would be divisible by $3$ , which is not what we want. Therefore, the only option is $\boxed{\textbf{(A) }2}$ -PCChess

## Solution 3
It is not hard to check that $13$ divides the number, \[\binom{52}{10}=\frac{52\cdot51\cdot50\cdot49\cdot48\cdot47\cdot46\cdot45\cdot44\cdot43}{10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}=26\cdot17\cdot5\cdot7\cdot47\cdot46\cdot11\cdot43.\] As $10^3\equiv-1\pmod{13}$ , using $\pmod{13}$ we have $13|\overline{AA0}-\overline{0A4}+\overline{8A0}-\overline{15}=110A+781$ . Thus $6A+1\equiv0\pmod{13}$ , implying $A\equiv2\pmod{13}$ so the answer is $\boxed{\textbf{(A) }2}$ .
$\textbf{- Emathmaster}$

## Solution 4
As mentioned above, \[\binom{52}{10}=\frac{52 \cdot 51 \cdot 50 \cdot 49 \cdot 48 \cdot 47 \cdot 46 \cdot 45 \cdot 44 \cdot 43}{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = {10 \cdot 17 \cdot 13 \cdot 7 \cdot 47 \cdot 46 \cdot 11 \cdot 43} = 158A00A4AA0.\] We can divide both sides of $10 \cdot 17 \cdot 13 \cdot 7 \cdot 47 \cdot 46 \cdot 11 \cdot 43 = 158A00A4AA0$ by 10 to obtain \[17 \cdot 13 \cdot 7 \cdot 47 \cdot 46 \cdot 11 \cdot 43 = 158A00A4AA,\] which means $A$ is simply the units digit of the left-hand side. This value is \[7 \cdot 3 \cdot 7 \cdot 7 \cdot 6 \cdot 1 \cdot 3 \equiv \boxed{\textbf{(A) }2} \pmod{10}.\] ~ i_equal_tan_90 , revised by emerald_block

## Solution 5 (Very Factor Bashy CRT)
We note that: \[\frac{(52)(51)(50)(49)(48)(47)(46)(45)(44)(43)}{(10)(9)(8)(7)(6)(5)(4)(3)(2)(1)} = (13)(17)(7)(47)(46)(5)(22)(43).\] Let $K=(13)(17)(7)(47)(46)(5)(22)(43)$ . This will help us find the last two digits modulo $4$ and modulo $25$ . It is obvious that $K \equiv 0 \pmod{4}$ . Also (although this not so obvious), \[K \equiv (13)(17)(7)(47)(46)(5)(22)(43)\] \[\equiv (13)(-8)(7)(-3)(-4)(5)(-3)(-7)\] \[\equiv (13)(-96)(21)(35)\] \[\equiv (13)(4)(-4)(10)\] \[\equiv (13)(-16)(10)\] \[\equiv (13)(9)(10)\] \[\equiv (117)(10)\] \[\equiv (-8)(10)\] \[\equiv 20 \pmod{25}.\] Therefore, $K \equiv 20 \mod 100$ . Thus $K=20$ , implying that $\boxed{\textbf{(A) }2}$ .

## Solution 6
As in Solution 2, we see that
\[\binom{52}{10}=26\cdot17\cdot5\cdot7\cdot47\cdot46\cdot11\cdot43,\]
which contains no factors of $3.$ Therefore, the sum of the digits must not be a multiple of $3.$ This sum is
\[1+5+8+A+0+0+A+4+A+A+0=18+4A.\]
It follows that $4A$ cannot be a multiple of $3,$ ruling out choices $(B)$ and $(D).$ Therefore, our possibilities are $A=2,4,$ and $7.$ Now, notice that $\binom{52}{10}$ is divisible by $7.$ Therefore, we can plug each possible value of $A$ into $158A00A4AA0$ and test for divisibility by $7.$ Conveniently, we see that the first value, $A=2,$ works. Thus, the answer is $\boxed{\bold{(A)} 2}.$ (To make our argument more rigorous, we can also test divisibility by $7$ for $A=4$ and $7$ to show that these values do not work.)
--vaporwave

## Solution 7
The total number of ways to choose $10$ from $52$ is $\binom{52}{10}=\frac{52\cdot51\cdot50\cdot49\cdot48\cdot47\cdot46\cdot45\cdot44\cdot43}{10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}$
Using divisibility rules, we have that A is not a multiple of $3$ . Then, divide this equation by 10. This implies that the new number $158A00A4AA0$ is divisible by $2$ but not $4$ . This means that $A$ is either $2$ or $6$ . However, $6$ is a multiple of $3$ , meaning $A$ has to be $\boxed {\textbf{(A)2}}$
~Arcticturn

## Solution 8 (Very time consuming)
As stated in previous solutions, the number of ways to choose $10$ from $52$ is $\binom{52}{10}=\frac{52\cdot51\cdot50\cdot49\cdot48\cdot47\cdot46\cdot45\cdot44\cdot43}{10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}$
Canceling out common factors $\left(\dfrac{52}{2} = 26 \text{, } \dfrac{51}{3} = 17 \text{, } 5 \cdot 10 = 50 \text{, } \dfrac{49}{7} = 7 \text{, } 48 = 6 \cdot 8 \text{, } \dfrac{45}{9} = 5 \text{, } \dfrac{44}{4} = 11\right)$ , you get this - $\frac{\cancel{52}^{26}\cdot\cancel{51}^{17}\cdot\cancel{50}\cdot\cancel{49}^{7}\cdot\cancel{48}\cdot47\cdot46\cdot\cancel{45}^5\cdot\cancel{44}^{11}\cdot43}{\cancel{10}\cdot\cancel{9}\cdot\cancel{8}\cdot\cancel{7}\cdot\cancel{6}\cdot\cancel{5}\cdot\cancel{4}\cdot\cancel{3}\cdot\cancel{2}\cdot\cancel{1}}$
When you multiply the remaining numbers, you get the product as $15820024220$ . From this product, we can then determine that $A$ is equal to $\boxed {\textbf{(A)2}}$
~ KING.OF.MATH
~ Puck_0 (Minor LaTeX)

## Solution 9 (DO NOT DO THIS)
Compute $\frac{52!}{10!42!} = 15820024220.$ Therefore our answer is $\boxed {\textbf{(A)2}}.$
~ Sliced_Bread
Note: This is a very impractical solution for the AMC 10B. This is only put here for fun. ~Yvz2900

## Solution 10 (Solution 8 but better)
As in solution 8, you get $26\cdot17\cdot7\cdot47\cdot46\cdot5\cdot11\cdot43$ This ends in a 0, so let's divide by 10. $13\cdot17\cdot7\cdot47\cdot46\cdot11\cdot43$ We want the last digit of this:
$3\cdot7\cdot7\cdot7\cdot6\cdot1\cdot3$
$\equiv2\cdot(3\cdot2\cdot2\cdot2\cdot3\cdot1\cdot3)$
$\equiv2\cdot(1\cdot2\cdot2\cdot3\cdot3)$
$\equiv2\cdot(2\cdot2\cdot3\cdot3)$
$\equiv2\cdot(4\cdot3\cdot3)$
$\equiv2\cdot(2\cdot3)$
$\equiv2\cdot1$
$\equiv2$
so A=2

## Video Solutions

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/QNUzrwXWQ2A
~Education, the Study of Everything

## Video Solution
https://youtu.be/3BvJeZU3T-M

## Video Solution 2
https://www.youtube.com/watch?v=ApqZFuuQJ18&list=PLLCzevlMcsWNcTZEaxHe8VaccrhubDOlQ&index=6 ~ MathEx
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .