# 2008 AIME I Problem 9

## Problem

Ten identical crates each of dimensions $3\mathrm{ft}\times 4\mathrm{ft}\times 6\mathrm{ft}$ . The first crate is placed flat on the floor. Each of the remaining nine crates is placed, in turn, flat on top of the previous crate, and the orientation of each crate is chosen at random. Let $\frac {m}{n}$ be the probability that the stack of crates is exactly $41\mathrm{ft}$ tall, where $m$ and $n$ are relatively prime positive integers. Find $m$ .

## Solution
Only the heights matter, and each crate is either 3, 4, or 6 feet tall with equal probability. We have the following:
\begin{align*}3a + 4b + 6c &= 41\\ a + b + c &= 10\end{align*}
Subtracting 3 times the second from the first gives $b + 3c = 11$ , or $(b,c) = (2,3),(5,2),(8,1),(11,0)$ . The last doesn't work, obviously. This gives the three solutions $(a,b,c) = (5,2,3),(3,5,2),(1,8,1)$ . In terms of choosing which goes where, the first two solutions are analogous.
For $(5,2,3),(3,5,2)$ , we see that there are $2\cdot\dfrac{10!}{5!2!3!} = 10\cdot9\cdot8\cdot7$ ways to stack the crates. For $(1,8,1)$ , there are $\dfrac{10!}{8!1!1!} = 90$ . Also, there are $3^{10}$ total ways to stack the crates to any height.
Thus, our probability is $\dfrac{10\cdot9\cdot8\cdot7 + 90}{3^{10}} = \dfrac{10\cdot8\cdot7 + 10}{3^{8}} = \dfrac{570}{3^8} = \dfrac{190}{3^{7}}$ . Our answer is the numerator, $\boxed{190}$ .

## 1 Min Solution
It would be helpful for this solution to be reformatted. To start with, let us observe the three numbers. Note that $3$ and $6$ are both divisible by $3$ , so the number of $4$ -crates must be congruent to $41\bmod{3}$ , which is also congruent to $2\bmod{3}$ . Our solutions for the number of $4$ -crates will repeat mod $3$ , so if $x$ is a solution, so is $x+3$ . By inspection, we have that $2$ is solution, and so are $5$ and $8$ . Each solution splits into its own case.We must solve the equation $41-4z=6x+3y$ , simultaneously with $x+y=10-z$ . Note that we already know the possible values of $z$ . Solving these (it's AIME $9$ , you should be able to do this and if anyone feels like they want to write a rundown of this please go ahead), we get the solution sets $\{8,1,1\},\{5,2,3\},$ and $\{2,3,5\}$ . We can count the number of possible arrangements for each solution by taking $\dbinom{10}{z}$ and then multiplying by $\dbinom{10-z}{x}$ (the solution sets, for the sake of consistency, are in the form $z,x,y$ ). Summing the results for all the solutions gives us $5130$ . Finally, to calculate the probability we must determine our denominator. Since we have $3$ ways to arrange each block, our denominator is $3^{10}$ . $\frac{5130}{3^{10}}=\frac{190}{3^7}$ . The answer is $m=\boxed{190}$ .

## Solution 2 (a more direct approach)
Let's make two observations. We are trying to find the number of ways we can add $3\text{s}, 4\text{s}$ , and $6\text{s}$ to get $41$ , and the total number of (non-distinct) sums possible is $3^{10}$ . Then we just use casework to easily and directly solve for the number of ways to get $41$ . To begin, the minimum sum is produced with $10$ threes, so WLOG we can solve for the number of ways to get $11$ with $0\text{s}, 1\text{s}$ , and $3\text{s}$ .
Case I: $0$ zeroes, $0$ threes, $11$ ones Impossible, because there are only ten available spots.
Case II: $1$ zero, $1$ three, $8$ ones This is just $\frac{10!}{8!}$ , so there are $90$ possibilities.
Case III: $3$ zeroes, $2$ threes, $5$ ones This is just $\frac{10!}{3!2!5!}$ . This gives $2520$ possibilities.
Case IV: 5 zeroes, 3 threes, and 2 ones. This is the same as case $3$ , so also $2520$ possibilities.
$90+2520+2520=5130$
$5130$ has three powers of $3$ , so $5130$ divided by $27$ is $\boxed{190}$ .
-jackshi2006

## Solution 3 (Generating Functions)
Note we are placing 10 crates where each "height" is 3, 4, 6 and we want all the heights to sum to 41. We can model this as the generating function \[\left(x^3+x^4+x^6\right)^{10}\] where we want the coefficient of $x^{41}.$ First off, factor this to get \[{x^{30} \left(1 + x + x^3\right)^{10}}\] and then see that we want the coefficient of $x^{11}$ in $\left(1+x+x^3\right)^{10}.$ From multinomial theorem, this expansion is \[\sum_{a+b+c=10}\binom{10}{a,b,c}1^ax^bx^{3c}\] If we want the coefficient of $x^{11}$ then we need $b + 3c = 11.$ with $b + c \le 10$ (from the multinomial expansion). This has the solutions $(b, c) = \{8, 1\}, \{5, 2\}, \{2, 3\}.$ Note that the denominator of the answer is just $3^{10}$ since there are 3 ways to orientate every crate and there are 10 creates. Thus, our answer is \[\frac{\binom{10}{8,1,1} + \binom{10}{5,2,3} + \binom{10}{2,3,5}}{3^{10}} = \frac{190}{3^7} \rightarrow \boxed{190}\]

## Video Solution (Very fast)
https://www.youtube.com/watch?v=qeSY_ISSX6M&t=33s
~fidgetboss_4000
These problems are copyrighted © by the Mathematical Association of America.