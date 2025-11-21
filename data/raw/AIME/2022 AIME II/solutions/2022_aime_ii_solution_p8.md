# 2022 AIME II Problem 8

## Problem

Find the number of positive integers $n \le 600$ whose value can be uniquely determined when the values of $\left\lfloor \frac n4\right\rfloor$ , $\left\lfloor\frac n5\right\rfloor$ , and $\left\lfloor\frac n6\right\rfloor$ are given, where $\lfloor x \rfloor$ denotes the greatest integer less than or equal to the real number $x$ .

## Solution 1
We need to find all numbers between $1$ and $600$ inclusive that are multiples of $4$ , $5$ , and/or $6$ which are also multiples of $4$ , $5$ , and/or $6$ when $1$ is added to them.
We begin by noting that the LCM of $4$ , $5$ , and $6$ is $60$ . We can therefore simplify the problem by finding all such numbers described above between $1$ and $60$ and multiplying the quantity of such numbers by $10$ ( $600$ / $60$ = $10$ ).
After making a simple list of the numbers between $1$ and $60$ and going through it, we see that the numbers meeting this condition are $4$ , $5$ , $15$ , $24$ , $35$ , $44$ , $54$ , and $55$ . This gives us $8$ numbers. $8$ * $10$ = $\boxed{080}$ .

## Solution 1.5
This is Solution 1 with a slick element included. Solution 1 uses the concept that $60k+l$ is a solution for $n$ if $60k+l$ is a multiple of $3$ , $4$ , and/or $5$ and $60k+l+1$ is a multiple of $3$ , $4$ , and/or $5$ for positive integer values of $l$ and essentially any integer value of $k$ . But keeping the same conditions in mind for $k$ and $l$ , we can also say that if $60k+l$ is a solution, then $60k-l-1$ is a solution! Therefore, one doesn't have to go as far as determining the number of values between $1$ and $60$ and then multiplying by $10$ . One only has to determine the number of values between $1$ and $30$ and then multiply by $20$ . The values of $n$ that work between $1$ and $30$ are $4$ , $5$ , $15$ , and $24$ . This gives us $4$ numbers. $4$ * $20$ = $\boxed{080}$ .
### Note
Soon after the test was administered, a formal request was made to also accept $\boxed{081}$ as an answer and MAA decided to honor this request. The gist of this request stated that the phrasing of the first part of the question could reasonably be interpreted to mean that one is given the condition to begin with that the integer is less than or equal to $600$ . In this case, if one was told that the values of $\left\lfloor \frac n4\right\rfloor$ , $\left\lfloor\frac n5\right\rfloor$ , and $\left\lfloor\frac n6\right\rfloor$ were $150$ , $120$ , and $100$ respectively, then the only possible choice for $n$ would be $600$ as $601$ , $602$ , and $603$ do not meet the condition as stated in the first part of the problem. If instead the problem asked for the numbers less than $600$ that met the second condition in the problem, the answer would be $\boxed{080}$ . ~burkinafaso ~sethl
Here are two interpretations of the problem: 1) If $n$ is a positive integer, how many numbers less than or equal to $600$ are determinable? Answer: $\boxed{080}$ . 2) If $n$ is a positive integer and $n \leq 600$ , then how many different $n$ are determinable? Answer: $\boxed{081}$ . ~epiconan

## Solution 2
1. For $n$ to be uniquely determined, $n$ AND $n + 1$ both need to be a multiple of $4, 5,$ or $6.$ Since either $n$ or $n + 1$ is odd, we know that either $n$ or $n + 1$ has to be a multiple of $5.$ We can state the following cases:
1. $n$ is a multiple of $4$ and $n+1$ is a multiple of $5$
2. $n$ is a multiple of $6$ and $n+1$ is a multiple of $5$
3. $n$ is a multiple of $5$ and $n+1$ is a multiple of $4$
4. $n$ is a multiple of $5$ and $n+1$ is a multiple of $6$
Solving for each case, we see that there are $30$ possibilities for cases 1 and 3 each, and $20$ possibilities for cases 2 and 4 each. However, we over-counted the cases where
1. $n$ is a multiple of $24$ and $n+1$ is a multiple of $5$
2. $n$ is a multiple of $5$ and $n+1$ is a multiple of $24$
Each case has $10$ possibilities.
Adding all the cases and correcting for over-counting, we get $30 + 20 + 30 + 20 - 10 - 10 = \boxed {080}.$
~Lucasfunnyface

## Solution 2 Supplement
Here is a detailed solution for Solution 2.
Over-counted cases:
$30 + 20 + 30 + 20 - 10 - 10 = \boxed{\textbf{080}}$
~ isabelchen

## Solution 3
The problem is the same as asking how many unique sets of values of $\lfloor\frac{n}{4}\rfloor$ , $\lfloor\frac{n}{5}\rfloor$ , and $\lfloor\frac{n}{6}\rfloor$ can be produced by one and only one value of $n$ for positive integers $n$ less than or equal to 600.
Seeing that we are dealing with the unique values of the floor function, we ought to examine when it is about to change values, for instance, when $n$ is close to a multiple of 4 in $\lfloor\frac{n}{4}\rfloor$ .
For a particular value of $n$ , let $a$ , $b$ , and $c$ be the original values of $\lfloor\frac{n}{4}\rfloor$ , $\lfloor\frac{n}{5}\rfloor$ , and $\lfloor\frac{n}{6}\rfloor$ , respectively.
Notice when $n$ $\equiv0\mod4$ and $n$ $\equiv4\mod5$ , the value of $\lfloor\frac{n-1}{4}\rfloor$ will be 1 less than the original $a$ . The value of $\lfloor\frac{n+1}{5}\rfloor$ will be 1 greater than the original value of $b$ .
More importantly, this means that no other value less than or greater than $n$ will be able to produce the set of original values of $a$ , $b$ , and $c$ , since they make either $a$ or $b$ differ by at least 1.
Generalizing, we find that $n$ must satisfy:
Where $j$ and $k$ are pairs of distinct values of 4, 5, and 6.
Plugging in the values of $j$ and $k$ , finding the solutions to the 6 systems of linear congruences, and correcting for the repeated values, we find that there are $\boxed{080}$ solutions of $n$ .

## Solution 3 Supplement
By Chinese Remainder Theorem , the general solution of systems of $2$ linear congruences is:
$\operatorname{lcm}[4, 5, 6] = 60$ , we solve the number of values for $n \le 60$ , then multiply by $10$ to get the number of values for $n \le 600$ . We are going to solve the following $6$ systems of linear congruences:
$n \in \{ 4, 5, 15, 24, 35, 44, 54, 55 \}$ , there are $8$ values for $n \le 60$ . For $n \le 600$ , the answer is $8 \cdot 10 = \boxed{\textbf{080}}$ .
~ isabelchen

## Solution 4
Observe that if $1 \le n \le 60$ such that n is a solution to the desired equation, so is $n + 60\cdot m$ , where m is an integer, $0 \le m \le 9$ . So we only need to consider n from 1 to 60. As shown in Solution 2, there are 4 cases which we will split into 2 main cases:
- Case 1: $4 \mid n$ or $6 \mid n$ , $5 \mid (n+1)$
- Case 2: $4 \mid (n+1)$ or $6 \mid (n+1)$ , $5 \mid n$
There are 4 values of n where $1 \le n \le 12$ satisfying $4 \mid n$ or $6 \mid n$ .
I claim that there are 4 values of $n \le 60$ satisfying Case 1. Suppose x is one value of n satisfying $4 \mid n$ or $6 \mid n$ , and $n \le 12$ . Hence the solutions satisfying $4 \mid n$ or $6 \mid n$ , $n \le 60$ are of the form $x + 12m$ , so the values of $n + 1$ are $x + 12m + 1 \equiv x + 2m + 1 \equiv 0$ (mod 5), so $2m \equiv 4 + 4x$ (mod 5) and hence the value of m is unique since $0 \le m \le 4$ to satisfy $1 \le n \le 60$ and 2 and 5 are relatively prime.
A similar approach can be used to show the same for Case 2, that there are 4 values of $n \le 60$ .
Hence our answer is $(4+4)*10 = \fbox{080}$ .
~ Bxiao31415

## Solution 5
$n$ and $n + 1$ must be multiples of $4, 5,$ or $6.$ Note that multiples of $4$ and $6$ cannot be consecutive since they're both even.
Case 1: $n \equiv 0 \pmod{4}$ and $n + 1 \equiv 0 \pmod{5}$ \[n = 4x \implies 4x + 1 \equiv 0 \pmod{5} \implies x \equiv 1\pmod{5}.\]
\[x = 5a_1 + 1 \implies n = 20a_1 + 4.\]
$0 \leq a_1 \leq 29 \implies 30$ values for $n$
Case 2: $n \equiv 0 \pmod{5}$ and $n + 1 \equiv 0 \pmod{4}$ \[n = 5x \implies 5x + 1 \equiv 3 \pmod{4} \implies x \equiv 3\pmod{4}.\]
\[x = 4a_2 + 3 \implies n = 20a_2 + 15.\]
$0 \leq a_2 \leq 29 \implies 30$ values for $n$
Case 3: $n \equiv 0 \pmod{6}$ and $n + 1 \equiv 0 \pmod{5}$ \[n = 6x \implies 6x \equiv 4 \pmod{5} \implies x \equiv 4\pmod{5}.\]
\[x = 5a_3 + 4 \implies n = 30a_3 + 24.\]
$0 \leq a_3 \leq 19 \implies 20$ values for $n$
Case 4: $n \equiv 0 \pmod{5}$ and $n + 1 \equiv 0 \pmod{6}$
\[n = 5x \implies 5x \equiv 5 \pmod{6} \implies x \equiv 1\pmod{6}.\]
\[x = 6a_4 + 1 \implies n = 30a_4 + 5.\]
$0 \leq a_4 \leq 19 \implies 20$ values for $n$
Case 1 and Case 3 overcount:
$n \equiv 0 \pmod{24}$ and $n + 1 \equiv 0 \pmod{5}$ \[20a_1 + 4 = 30a_3 + 24 \implies 20a_1 = 30a_3 + 20\] $a_1 = 1,4,7 \dots 28 \implies 10$ overcounted values for these cases.
Case 2 and Case 4 overcount:
$n \equiv 0 \pmod{5}$ and $n + 1 \equiv 0 \pmod{24}$ \[20a_2 + 15 = 30a_4 + 5 \implies 20a_2 = 30a_4 -10\] $a_2 = 1,4,7 \dots 28 \implies 10$ overcounted values for these cases.
The answer is $30 + 30 + 20 + 20 - 10 - 10 = \boxed{80}.$
~ grogg007

## Solution 6(Recursive Way)
Let $n = 60x + y$ . Let $\lfloor \frac{n}{4} \rfloor = a$ and define the others analogously. Then we see that $15x + \lfloor \frac{y}{4} \rfloor = a$ . We let $y = 60x_1 + y_1$ and we proceed. Eventually, we note that any $y_i$ must be in the range $0$ to $60$ since it can't be greater than $60$ . We get the recursive definition of $y_i = 60x_{i + 1} + y_{i + 1}$ . Simplifying the series, we would get $15x_1 + 15x_2 + .... + 15x_n = a$ . Now note that $\lfloor \frac{n}{4} \rfloor$ has a maximum of $n = 600$ and a minimum of $n = 1$ hence $0 \leq a \leq 150$ . Therefore, plugging this in, we have $0 \leq x_1 + ... + x_n \leq 10$ . From $y_i = 60x_{i + 1} + y_{i + 1}$ , we can deduce $x_{i + 1} = \frac{y_i - y_{i + 1}}{60}$ . Plugging this in, we get $0 \leq \frac{y_1 - y_2}{60} + \frac{y_2 - y_3}{60} + ... + \frac{y_{n - 1} - y_n}{60} \leq 10$ . This is telescoping series which simplifies to $0 \leq y - y_n \leq 600$ . Now this looks almost identical to the original condition which stated $0 \leq n \leq 600$ . In fact, we note that any $y_i < 60$ from the floor function condition. Hence, the number of solutions we would have in the range of $0$ to $60$ is proportional to the number of solutions we would have from $0$ to $600$ . Since the first set is $60$ units long and the second set is $600$ units long, we note that $\frac{600}{60} = 10$ so when we find the number of solutions between $0$ and $60$ , we can just multiply that by $10$ to get our answer.
The problem reduces to stating:
How many possible positive integer $n$ less than or equal to $60$ are there such that when given the values of $\lfloor \frac{n}{4} \rfloor, \lfloor \frac{n}{5} \rfloor, \lfloor \frac{n}{6} \rfloor$ , we can uniquely find the value of $n$ ?
We'll solve this by noting ranges of $4$ . Let's first look at $n$ being in the range $[1, 3]$ . All the floor values will be $0$ for each of them so no value here is unique. From $[4, 7]$ , $n = 4$ will lead values of $1, 0, 0$ respectively. $n = 5$ will lead values of $1, 1, 0$ respectively. And both $n = 6$ and $n = 7$ will lead values of $1, 1, 1$ respectively. So only $n = 4$ and $n = 5$ are unique so we have $2$ cases here. We can perform similar analysis to the range of $[8, 11]$ and find none are unique. We will then do the same for $[12, 15]$ . We will see only $n = 15$ gives a unique solution so we have $1$ solution. Nothing will work for $[16, 19]$ . Nothing will work for $[20, 23]$ . Only $n = 24$ will work for $[24, 27]$ . So far the only ones that have worked so far are $n = 4, 5, 15, 24$ out of the first $27$ numbers. We will continue up until the first $30$ numbers then double the ones that have worked so far by symmetry. In the next range, $[28, 31]$ nothing works. Hence, as this range includes the first $30$ numbers, only $4$ have worked so far. If you are in contest, you should be pretty safe assuming the symmetry for the rest of the $30$ numbers. Assuming that is true, we conclude the total numbers that will work is $4 \cdot 2 = 8$ .
Hence, only $8$ numbers will give a unique solution out of the first $60$ numbers. By our claim using recursion above, we have to multiply this by $10$ to get the actual answer. Hence $8 \cdot 10 = \boxed{80}$ .
~ilikemath247365
### Note
Important observation is that a multiple of 4 and multiple of 6 cannot be consecutive.
~zephy

## Video Solution
https://youtu.be/mW9YQPNZqQg
~MathProblemSolvingSkills.com

## Video Solution by The Power of Logic
https://youtu.be/oudK3mfIFso
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .