# 2020 AMC 10A Problem 22

## Problem

For how many positive integers $n \le 1000$ is \[\left\lfloor \dfrac{998}{n} \right\rfloor+\left\lfloor \dfrac{999}{n} \right\rfloor+\left\lfloor \dfrac{1000}{n}\right \rfloor\] not divisible by $3$ ? (Recall that $\lfloor x \rfloor$ is the greatest integer less than or equal to $x$ .)

$\textbf{(A) } 22 \qquad\textbf{(B) } 23 \qquad\textbf{(C) } 24 \qquad\textbf{(D) } 25 \qquad\textbf{(E) } 26$

## Solution 1
If $n$ is a factor of $999$ (and $n \neq 1$ ), then let $999 = an$ for some positive integer $a.$ Then we get $\lfloor 998/n \rfloor = a - 1$ , $\lfloor 999/n \rfloor =a$ , $\lfloor 1000/n \rfloor = a$ . The sum is $3a - 1,$ which isn't a multiple of 3. If $n$ is a factor of $1000$ (and $n \neq 1$ ), then let $1000 = an.$ Then we get $\lfloor 998/n \rfloor = a - 1$ , $\lfloor 999/n \rfloor = a - 1$ , and $\lfloor 1000/n \rfloor = a.$ The sum is $3a - 2,$ which also isn't a multiple of 3.
We find that the only way for the problem's condition to hold true is if $n$ is a factor of $999$ or $1000$ and $n \neq 1$ .
- $1000 = 5^3 \cdot 2^3 \implies (3+1)(3+1) = 16$ factors.
- $999 = 3^3 \cdot 37 \implies (3+1)(1+1) = 8$ factors.
We counted $1$ twice. So the answer is $16 + 8 - 2 = \boxed{22}.$
~ grogg007

## Solution 2
Clearly, $n=1$ fails. Except for the special case of $n=1$ , \[\left\lfloor \frac{1000}{n} \right\rfloor - \left\lfloor \frac{998}{n} \right\rfloor\] equals either $0$ or $1$ . If it equals $0$ , this implies that $\left\lfloor \frac{998}{n} \right\rfloor = \left\lfloor \frac{999}{n} \right\rfloor = \left\lfloor \frac{1000}{n} \right\rfloor$ , so their sum is clearly a multiple of $3$ , so this will always fail. If it equals $1$ , the sum of the three floor terms is $3 \left\lfloor \frac{999}{n} \right\rfloor \pm 1$ , so it is never a multiple of $3$ . Thus, we are looking for all $n \neq 1$ such that \[\left\lfloor \frac{1000}{n} \right\rfloor - \left\lfloor \frac{998}{n} \right\rfloor = 1.\] This implies that either \[\left\lfloor \frac{998}{n} \right\rfloor + 1 = \left\lfloor \frac{999}{n} \right\rfloor,\] or \[\left\lfloor \frac{999}{n} \right\rfloor + 1 = \left\lfloor \frac{1000}{n} \right\rfloor.\]
Let's analyze the first equation of these two. This equation is equivalent to the statement that there is a positive integer $a$ such that \[\frac{998}{n} < a \leq \frac{999}{n} \implies 998 < an \leq 999 \implies an = 999 \implies a = \frac{999}{n} \implies n | 999.*\] Analogously, the second equation implies that \[n | 1000.\] So our only $n$ that satisfy this condition are $n \neq 1$ that divide $999$ or $1000$ . Using the method to find the number of divisors of a number, we see that $999$ has $8$ divisors and $1000$ has $16$ divisors. Their only common factor is $1$ , so there are $8+16-1 = 23$ positive integers that divide either $999$ or $1000$ . Since the integer $1$ is a special case and does not count, we must subtract this from our $23$ , so our final answer is $23-1 = \boxed{\textbf{(A) } 22}.$
~ihatemath123

## Solution 3
Counting down $n$ from $1000$ , $999$ , $998$ ... we notice that $\left\lfloor \dfrac{998}{n} \right\rfloor+\left\lfloor \dfrac{999}{n} \right\rfloor+\left\lfloor \dfrac{1000}{n}\right \rfloor$ is only not divisible by $3$ when n is a divisor of only $1000$ or $999 (1000, 999, 500, 333$ ...). Notice how the factors of $998: 1, 2, 499$ , and $998$ , do not work.
The prime factorization of $999$ is $3^3\cdot37$ , so $4\cdot2=8$ factors in total.
The prime factorization of $1000$ is $2^3\cdot5^3$ , so $4\cdot4=16$ factors in total.
However, $1$ obviously does not work, so we have to subtract $2$ ( $1$ is counted twice) from the total. $8 + 16 - 2$ = $\boxed{\textbf{(A)}22}$ .
~BLOATED_BAGEL
~Typo fixed by evanhliu2009

## Solution 4
First, we notice the following lemma:
$\textbf{Lemma}$ : For $N, n \in \mathbb{N}$ , $\left\lfloor \frac{N}{n} \right\rfloor = \left\lfloor \frac{N-1}{n} \right\rfloor + 1$ if $n \mid N$ ; and $\left\lfloor \frac{N}{n} \right\rfloor = \left\lfloor \frac{N-1}{n} \right\rfloor$ if $n \nmid N.$
$\textbf{Proof}$ : Let $A = kn + r$ , with $0 \leq r < n$ . If $n \mid N$ , then $r = 0$ . Hence $\left\lfloor \frac{N}{n} \right\rfloor = k$ , $\left\lfloor \frac{N-1}{n} \right\rfloor = \left\lfloor \frac{(k-1)n+n-1}{n} \right\rfloor = k-1 + \left\lfloor \frac{n-1}{n} \right\rfloor = k-1$ , and $\left\lfloor \frac{N}{n} \right\rfloor = \left\lfloor \frac{N-1}{n} \right\rfloor + 1.$
If $n \nmid N$ , then $1 \leq r < n$ . Hence $\left\lfloor \frac{N}{n} \right\rfloor = k$ , $\left\lfloor \frac{N-1}{n} \right\rfloor = k + \left\lfloor \frac{r-1}{n} \right\rfloor = k$ , and $\left\lfloor \frac{N}{n} \right\rfloor = \left\lfloor \frac{N-1}{n} \right\rfloor.$
From the lemma and the given equation, we have four possible cases: \[\left\lfloor \frac{998}{n} \right\rfloor + 1 = \left\lfloor \frac{999}{n} \right\rfloor = \left\lfloor \frac{1000}{n} \right\rfloor - 1 \qquad (1)\] \[\left\lfloor \frac{998}{n} \right\rfloor + 1 = \left\lfloor \frac{999}{n} \right\rfloor + 1 = \left\lfloor \frac{1000}{n} \right\rfloor \qquad (2)\] \[\left\lfloor \frac{998}{n} \right\rfloor + 1 = \left\lfloor \frac{999}{n} \right\rfloor = \left\lfloor \frac{1000}{n} \right\rfloor \qquad (3)\] \[\left\lfloor \frac{998}{n} \right\rfloor = \left\lfloor \frac{999}{n} \right\rfloor = \left\lfloor \frac{1000}{n} \right\rfloor \qquad (4)\]
Note that cases (2) and (3) are the cases in which the term, $\left\lfloor \frac{998}{n} \right\rfloor + \left\lfloor \frac{999}{n} \right\rfloor + \left\lfloor \frac{1000}{n} \right\rfloor,$ is not divisible by $3$ . So we only need to count the number of $n$ 's for which cases (2) and (3) stand.
Case (2): By the lemma, we have $n \mid 1000$ and $n \nmid 999.$ Hence $n$ can be any factor of $1000$ except for $n = 1$ . Since $1000 = 2^3 * 5^3,$ there are $(3+1)(3+1) - 1 = 15$ possible values of $n$ for this case.
Case (3): By the lemma, we have $n \mid 999$ and $n \nmid 998.$ Hence $n$ can be any factor of $999$ except for $n = 1$ . Since $999 = 3^3 * 37^1,$ there are $(3+1)(1+1) - 1 = 7$ possible values of $n$ for this case.
So in total, we have total of $15+7=\boxed{\textbf{(A)}22}$ possible $n$ 's.
~mathboywannabe

## Solution 5 (Casework)
Note that $\left\lfloor \frac{998}{n} \right\rfloor + \left\lfloor \frac{999}{n} \right\rfloor + \left\lfloor \frac{1000}{n} \right\rfloor$ is a multiple of $3$ if $\left\lfloor \frac{998}{n} \right\rfloor + \left\lfloor \frac{999}{n} \right\rfloor + \left\lfloor \frac{1000}{n} \right\rfloor$ lies between two consecutive multiples of $n$ .
$\textbf{Explanation:}$
Let's assume that the above expression does indeed lie betweent two consecutive multiples of $n$ . This implies that $n$ does not divide either $998, 999$ or $1000$ , meaning that when divided by $n$ , none of the quotients are whole. In turn, this also means that they will all have the same whole number part.
If $\frac{998}{n}, \frac{999}{n},$ and $\frac{1000}{n}$ were to have a different whole number part, then $n$ would have to lie within $998$ and $1000$ . If this is confusing, think of why $\frac{6}{5}, \frac{7}{5}$ and $\frac{8}{5}$ have the same whole number part ( $1$ in this case). Here, $n=5$ . What happens to the whole number part when $n=7$ ?
Since $\frac{998}{n}, \frac{999}{n},$ and $\frac{1000}{n}$ have identical whole number parts, their floors are identical, since the floor of a number is equal to its whole number part, discarding its fractional component.
Let $k$ be the number we get when we floor $\frac{998}{n}, \frac{999}{n},$ or $\frac{1000}{n}$ if the three of those numbers lie between two consecutive multiples of $n$ . Adding them up, we get $3k$ (due to their floors being the same), which is a mulutiple of $3$ . So no matter what, we cannot have $\frac{998}{n}, \frac{999}{n},$ and $\frac{1000}{n}$ lie between two consecutive multiples of $n$ .
What does this mean? It means that there must be some multiple of $n$ within this expression (with some restrictions, as we'll see), in order to prevent the violation of the main restriction. We can proceed with casework now.
$\textbf{Case 1}$
Let's assume that the multiple of $n$ is located at $\frac{998}{n}$ . Luckily, the only prime factors of $998$ are $2$ and $499$ .
We can observe that $499$ doesn't work, since $\frac{998}{499}$ and $\frac{1000}{499}$ will both round down to $2$ when divided by it. However, $2$ does work, since it divides both $998$ and $1000$ . The floor of $\frac{999}{2}$ is $499$ , , meaning that when we evaluate the given expression for $n=2$ , we will get $2\cdot{499}+500$ which isn't a multiple of $3$ .
This case works because we have a multiple of $n$ at the end of the expression, as well as the beginning, so the whole number parts of $998, 999$ and $1000$ when divided by $n$ are not all the same, due to $n$ dividing two of these numbers.
The restriction of $n$ dividing more than one number within the expression is only valid when we're testing the first number in the given expression (otherwise, the other floors wouldn't round down to the same value as the first).
Case $1$ is complete, and we've found that only $2$ works.
$\textbf{Case 2}$
Now, let's assume that the multiple of $n$ is located at $\frac{999}{n}$ . In this case, if $n$ divides $999$ , it doesn't divide $998$ (since two multiples of a number greater than $1$ are never consecutive), nor does it divide $1000$ , for the same reason.
The prime factorization of $999$ is $3^3\cdot37$ , and thus has $(3+1)(1+1)=8$ divisors.
When testing a few values of $n$ initially, we observed that $n=1$ causes the expression to be divisible by $3$ . Subtracting $1$ , we see that there are $7$ values of $n$ that work for this case.
$\textbf{Case 3}$
Finally, let's assume that the multiple of $n$ is located at $\frac{1000}{n}.$
Our goal is to have the other multiple of $n$ below whatever $\frac{998}{n}$ is, so we won't have identical floors throughout the expression.
Once again, any factor of $1000$ , except for $2$ is relatively prime to both $998$ and $999$ , so when we floor those two numbers, we get an integer that isn't $500$ .
$1000$ factors as $2^3\cdot{5^3}$ , meaning that it has $(3+1)(3+1)=16$ divisors. $1$ and $2$ either don't work or have already been counted, so there are $14$ valid values of $n$ for this case.
$\textbf{Ending}$
Adding these three cases, we get $1+7+14= \boxed{\textbf{A) }22}$ values of $n$ .
-Benedict T (countmath1)

## Solution 6 (simple, fast)
Let $\lfloor \frac{998}{n} \rfloor + \lfloor \frac{999}{n} \rfloor + \lfloor \frac{1000}{n} \rfloor$ be (1). Claim : If $n$ is a factor of at least one of 998, 999, 1000, then (1) is NOT divisible by 3. Proof of the claim :
If you don't understand this, let's test out some possible values. Evaluating the expression using $n = 1, 2, 3, 4, 5$ show that the expression isn't divisible by 3. And when $n = 6$ , we have \[\lfloor \frac{998}{6} \rfloor = \lfloor \frac{999}{6} \rfloor = \lfloor \frac{1000}{6} \rfloor = 166\] This justifies that the expression is divisible by 3.
Therefore, let $S$ be the set of numbers (not incl. 1) for which this is divisible by 3, which is $S = \{2, 3, 4, 5, 8, 9, 10, 20, 27, 37, 40, 50, 100, 111, 200, 333, 400, 499, 500, 999, 1000\}$ . Adding 1 to this gives $21 + 1 = 22$ values. $\boxed{\textbf{(A) }22}$ Q. E. D. ~elpianista227

## Video Solutions

## Video Solution 1 (Simple)
Education, The Study of Everything
https://youtu.be/LWAYKQQX6KI

## Video Solution 2
https://www.youtube.com/watch?v=_Ej9nnHS07s
~Snore

## Video Solution 3
https://www.youtube.com/watch?v=G5UVS5aM-CY&list=PLLCzevlMcsWNcTZEaxHe8VaccrhubDOlQ&index=4 ~ MathEx

## Video Solution 4 (Richard Rusczyk)
https://artofproblemsolving.com/videos/amc/2020amc10a/517
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .