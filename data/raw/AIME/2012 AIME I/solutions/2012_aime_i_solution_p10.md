# 2012 AIME I Problem 10

## Problem

Let $\mathcal{S}$ be the set of all perfect squares whose rightmost three digits in base $10$ are $256$ . Let $\mathcal{T}$ be the set of all numbers of the form $\frac{x-256}{1000}$ , where $x$ is in $\mathcal{S}$ . In other words, $\mathcal{T}$ is the set of numbers that result when the last three digits of each number in $\mathcal{S}$ are truncated. Find the remainder when the tenth smallest element of $\mathcal{T}$ is divided by $1000$ .

## Solution 1
It is apparent that for a perfect square $s^2$ to satisfy the constraints, we must have $s^2 - 256 = 1000n$ or $(s+16)(s-16) = 1000n.$ Now in order for $(s+16)(s-16)$ to be a multiple of $1000,$ at least one of $s+16$ and $s-16$ must be a multiple of $5,$ and since $s+16 \not\equiv s-16 \pmod{5},$ one term must have all the factors of $5$ and thus must be a multiple of $125.$ Furthermore, each of $s+16$ and $s-16$ must have at least two factors of $2,$ since otherwise $(s+16)(s-16)$ could not possibly be divisible by $8.$ So therefore the conditions are satisfied if either $s+16$ or $s-16$ is divisible by $500,$ or equivalently if $s = 500n \pm 16.$ Counting up from $n=0$ to $n=5,$ we see that the tenth value of $s$ is $500 \cdot 5 - 16 = 2484$ and thus the corresponding element in $\mathcal{T}$ is $\frac{2484^2 - 256}{1000} = 6170 \rightarrow \boxed{170.}$

## Solution 2
Notice that is $16^2=256$ , $1016^2$ ends in $256$ . In general, if $x^2$ ends in $256$ , $(x+1000)^2=x^2+2000x+1000000$ ends in 256 because $1000|2000x$ and $1000|2000000$ . It is clear that we want all numbers whose squares end in $256$ that are less than $1000$ .
Firstly, we know the number has to end in a $4$ or a $6$ . Let's look at the ones ending in $6$ .
Assume that the second digit of the three digit number is $0$ . We find that the last $3$ digits of $\overline{a06}^2$ is in the form $12a \cdot 100 + 3 \cdot 10 + 6$ . However, the last two digits need to be a $56$ . Thus, similarly trying all numbers from $0$ to $10$ , we see that only 1 for the middle digit works. Carrying out the multiplication, we see that the last $3$ digits of $\overline{a16}^2$ is in the form $(12a + 2) \cdot 100 + 5 \cdot 10 + 6$ . We want $(12a + 2)\pmod{10}$ to be equal to $2$ . Thus, we see that a is $0$ or $5$ . Thus, the numbers that work in this case are $016$ and $516$ .
Next, let's look at the ones ending in $4$ . Carrying out a similar technique as above, we see that the last $3$ digits of $\overline{a84}^2$ is in the form $((8a+10) \cdot 100+ 5 \cdot 10 + 6$ . We want $(8a + 10)\pmod{10}$ to be equal to $2$ . We see that only $4$ and $9$ work. Thus, we see that only $484$ and $984$ work.
We order these numbers to get $16$ , $484$ , $516$ , $984$ ... We want the $10th$ number in order which is $2484^2 = 6\boxed{170}256$ .

## Solution 3
The condition implies $x^2\equiv 256 \pmod{1000}$ . Rearranging and factoring, \[(x-16)(x+16)\equiv 0\pmod {1000}.\] This can be expressed with the system of congruences \[\begin{cases} (x-16)(x+16)\equiv 0\pmod{125} \\ (x-16)(x+16)\equiv 0\pmod{8} \end{cases}\] Observe that $x\equiv {109} \pmod {125}$ or $x\equiv{16}\pmod {125}$ . Similarly, it can be seen that $x\equiv{0}\pmod{8}$ or $x\equiv{4}\pmod{8}$ . By CRT, there are four solutions to this modulo $1000$ (one for each case e.g. $x\equiv{109}$ and $x\equiv{0}$ or $x\equiv{125}$ and $x\equiv{4}$ . These solutions are (working modulo $1000$ ) \[\begin{cases} x=16 \\ x=484 \\ x= 516 \\ x=984 \end{cases}\] The tenth solution is $x=2484,$ which gives an answer of $\boxed{170}$ .

## Solution 4
An element in S can be represented by $y^2 = 1000a + 256$ , where $y^2$ is the element in S. Since the right hand side must be even, we let $y = 2y_1$ and substitute to get $y_1^2 = 250a + 64$ . However, the right hand side is still even, so we make the substitution $y_1 = 2y_2$ to get $y_2^2 = 125a/2 + 16$ . Because both sides must be an integer, we know that $a = 2a_1$ for some integer $a_1$ . Our equation then becomes $y_2^2 = 125a_1 + 16$ , and we can simplify no further.
Rearranging terms, we get $y_2^2 - 16 = 125a_1$ , whence difference of squares gives $(y_2 + 4)(y_2 - 4) = 125a_1$ . Note that this equation tells us that one of $y_2 + 4$ and $y_2 - 4$ contains a nonnegative multiple of $125$ . Hence, listing out the smallest possible values of $y_2$ , we have $y_2 = 4, 121, 129, \cdots, 621$ . The tenth term is $621$ , whence $y = 4y_2 = 2484$ . The desired result can then be calculated to be $\boxed{170}$ . - Spacesam

## Solution 5 (Similar to Solution 4)
From the conditions, we can let every element in $\mathcal{S}$ be written as $y^2=1000x+256$ , where $x$ and $y$ are integers. Since there are no restrictions on $y$ , we let $y_1$ be equal to $y+16$ ( $y-16$ works as well). Then the $256$ cancels out and we're left with \[y_1^2+32y_1=1000x\] which can be factored as \[y_1(y_1+32)=1000x\] Since the RHS is even, $y_1$ must be even, so we let $y_1=2y_2$ , to get \[y_2(y_2+16)=250x\] Again, because the RHS is even, the LHS must be even too, so substituting $y_3=\frac{1}{2}y_2$ we have \[y_3(y_3+8)=125\cdot\frac{1}{2}x\] Since the LHS is an integer, the RHS must thus be an integer, so substituting $x=2x_1$ we get \[y_3(y_3+8)=125x_1\] Then we can do casework on the values of $y_3$ , as only one of $y_3$ and $y_3+8$ can be multiples of $125$
Case 1 : $125|y_3$
Since we're trying to find the values of $x_1$ , we can let $y_4=\frac{1}{125}y_3$ , to get \[x_1=y_4(125y_4+8)\] or \[x=2y_4(125y_4+8)\]
Case 2 : $125|y_3+8$
Similar to Case 1, only the equation is \[x=2y_4(125y_4-8)\]
In whole, the values of $x$ (i.e. the elements in $\mathcal{T}$ ) are of the form \[x=2k(125k\pm8)\] where $k$ is any integer. It can easily be seen that if $k<0$ , then $x$ is negative, thus $k\geq0$ . Also, note that when $k=0$ , there is only one value, because one of the factors is $0$ ( $k$ ). Thus the $10^{th}$ smallest number in the set $\mathcal{T}$ is when the $\pm$ sign takes the minus side and $k=5$ , giving $6170$ , so the answer is $\boxed{170}$

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/349
~ dolphin7

## Video Solution
https://www.youtube.com/watch?v=caCELHibbIE&list=PLOaAlyCEsUTbA2v1gRyEAB_gxk7NiWG3v&index=6&t=0s
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .