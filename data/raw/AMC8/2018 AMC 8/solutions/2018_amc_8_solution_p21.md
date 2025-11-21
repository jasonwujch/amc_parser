# 2018 AMC 8 Problem 21

## Problem

How many positive three-digit integers have a remainder of 2 when divided by 6, a remainder of 5 when divided by 9, and a remainder of 7 when divided by 11?

$\textbf{(A) }1\qquad\textbf{(B) }2\qquad\textbf{(C) }3\qquad\textbf{(D) }4\qquad \textbf{(E) }5$

## Solution 1
Looking at the values, we notice that $11-7=4$ , $9-5=4$ and $6-2=4$ . This means we are looking for a value that is four less than a multiple of $11$ , $9$ , and $6$ . The least common multiple of these numbers is $11\cdot3^{2}\cdot2=198$ , so the numbers that fulfill this can be written as $198k-4$ , where $k$ is a positive integer. This value is only a three-digit integer when $k$ is $1, 2, 3, 4$ or $5$ , which gives $194, 392, 590, 788,$ and $986$ respectively. Thus, we have $5$ values, so our answer is $\boxed{\textbf{(E) }5}$ .

## Solution 2
Let us create the equations: $6x+2 = 9y+5 = 11z+7$ , and we know $100 \leq 11z+7 <1000$ , it gives us $9 \leq z \leq 90$ , which is the range of the value of z. Because of $6x+2=11z+7$ , then $6x=11z+5=6z+5(z+1)$ , so $(z+1)$ must be a multiple of 6. Because of $9y+5=11z+7$ , then $9y=11z+2=9z+2(z+1)$ , so $(z+1)$ must also be a multiple of $9$ . Hence, the value of $(z+1)$ must be a common multiple of $6$ and $9$ , which means multiples of $18 (LCM \text{ of }\ 6, 9)$ . So, let's say $z+1 = 18p$ ; then, $9 \leq z = 18p-1 \leq 90$ , so $1 \leq p \leq 91/18\ or \ 1 \leq p \leq 5$ . Thus, the answer is $\boxed{\textbf{(E) }5}$ .
~LarryFlora

## Solution 3
By the Chinese Remainder Theorem , we have that all solutions are in the form $x=198k+194$ where $k\in \mathbb{Z}.$ Counting the number of values, we get $\boxed{\textbf{(E) }5}.$
~mathboy282

## Solution 4
We can use modular arithmetic. Set up the equations: $x \equiv 2 \mod 6,$ $x \equiv 5 \mod 9,$ and $x \equiv 7 \mod 11.$ These equations can also be written as $x+4 \equiv 0 \mod 6,$ $x+4 \equiv 0 \mod 9,$ and $x+4 \equiv 0 \mod 11.$ Since $x+4$ is congruent to numbers $6, 9,$ and $11,$ then it must also be congruent to their LCM. Thus, $x+4 \equiv 0 \mod 198,$ since 198 is the LCM of $6, 9,$ and $11.$ Since these numbers have to be three digits, they can only be $194, 392, 590, 788,$ and $986.$ This gives us the answer of $\boxed{\textbf{(E) }5}.$
~ethancui0529

## Solution 5
Let $N$ be the three digit positive integer. $N = 6a + 2 = 9b + 5 = 11c + 7$ . Then, we add four to all sides and write $N + 4 = 6(a+1) = 9(b+1) = 11(c+1)$ . Now, we know that $N + 4$ is divisible by 6, 9, and 11. The LCM of 6, 9, and 11 is equal to 198, so $N = 198k - 4$ . From this, we can figure out that $N$ can be 5 different three digit numbers -- $194, 392, 590, 788,$ and $986$ . $\therefore$ , the answer is $\boxed{\textbf{(E) }5}.$
~DY

## Video Solution by Pi Academy (Fast and Easy)
https://youtu.be/7xlBdxcsP3I?si=lfZZBB7i_6tOlKr-

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/kb_0r9fEyEI
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/7an5wU9Q5hk?t=939
~ pi_is_3.14

## Video Solutions
https://youtu.be/CPQpkpnEuIc
~ Happytwin
https://youtu.be/hoCdk8AC-0c
~savannahsolver
https://www.youtube.com/watch?v=PjYwbGm_2aM ~David
### See Also