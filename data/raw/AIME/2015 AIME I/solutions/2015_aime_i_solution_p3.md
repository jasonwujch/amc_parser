# 2015 AIME I Problem 3

## Problem

There is a prime number $p$ such that $16p+1$ is the cube of a positive integer. Find $p$ .

## Video Solution For Problems 1-3
https://www.youtube.com/watch?v=5HAk-6qlOH0

## Video Solution by OmegaLearn
https://youtu.be/3bRjcrkd5mQ?t=1096
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/vajttONefxs
~savannahsolver

## Solution 1
Let the positive integer mentioned be $a$ , so that $a^3 = 16p+1$ . Note that $a$ must be odd, because $16p+1$ is odd.
Rearrange this expression and factor the left side (this factoring can be done using $(a^3-b^3) = (a-b)(a^2+a b+b^2)$ or synthetic divison once it is realized that $a = 1$ is a root):
\begin{align*} a^3-1 &= 16p\\ (a-1)(a^2+a+1) &= 16p\\ \end{align*}
Because $a$ is odd, $a-1$ is even and $a^2+a+1$ is odd. If $a^2+a+1$ is odd, $a-1$ must be some multiple of $16$ . However, for $a-1$ to be any multiple of $16$ other than $16$ would mean $p$ is not a prime. Therefore, $a-1 = 16$ and $a = 17$ .
Then our other factor, $a^2+a+1$ , is the prime $p$ :
\begin{align*} (a-1)(a^2+a+1) &= 16p\\ (17-1)(17^2+17+1) &=16p\\ p = 289+17+1 &= \boxed{307} \end{align*}

## Solution 2 (Similar to 1)
Observe that this is the same as $16p+1=n^3$ for some integer $n$ . So:
\begin{align*} 16p &= n^3-1\\ 16p &= n^3-1^3\\ 16p &= (n-1)(n^2+n+1)\\ \end{align*}
Observe that either $p=n-1$ or $p=n^2+n+1$ because $p$ and $16$ share no factors ( $p$ can't be $2$ ). Let $p=n-1$ . Then:
\begin{align*} p &= n-1\\ 16 &= n^2+n+1\\ n^2+n &= 15\\ n(n+1) &= 15\\ \end{align*}
Which is impossible for integer n. So $p=n^2+n+1$ and
\begin{align*} 16 &= n-1\\ n &= 17\\ p &= 17^2+17+1\\ p = 289+17+1 &= \boxed{307}\\ \end{align*} - firebolt360

## Solution 3
Since $16p+1$ is odd, let $16p+1 = (2a+1)^3$ . Therefore, $16p+1 = (2a+1)^3 = 8a^3+12a^2+6a+1$ . From this, we get $8p=a(4a^2+6a+3)$ . We know $p$ is a prime number and it is not an even number. Since $4a^2+6a+3$ is an odd number, we know that $a=8$ .
Therefore, $p=4a^2+6a+3=4*8^2+6*8+3=\boxed{307}$ .

## Solution 4
Let $16p+1=a^3$ . Realize that $a$ congruent to $1\mod 4$ , so let $a=4n+1$ . Expansion, then division by 4, gets $16n^3+12n^2+3n=4p$ . Clearly $n=4m$ for some $m$ . Substitution and another division by 4 gets $256m^3+48m^4+3m=p$ . Since $p$ is prime and there is a factor of $m$ in the LHS, $m=1$ . Therefore, $p=\boxed{307}$ .

## Solution 5
Notice that $16p+1$ must be in the form $(a+1)^3 = a^3 + 3a^2 + 3a + 1$ . Thus $16p = a^3 + 3a^2 + 3a$ , or $16p = a\cdot (a^2 + 3a + 3)$ . Since $p$ must be prime, we either have $p = a$ or $a = 16$ . Upon further inspection and/or using the quadratic formula, we can deduce $p \neq a$ . Thus we have $a = 16$ , and $p = 16^2 + 3\cdot 16 + 3 = \boxed{307}$ .

## Solution 6
Notice that the cube 16p+1 is congruent to 1 mod 16. The only cubic numbers that leave a residue of 1 mod 16 are 1 and 15. Case one: The cube is of the form 16k+1-->Plugging this in, and taking note that p is prime and has only 1 factor gives p=307 Case two: The cube is of the form 16k+15--> Plugging this in, we quickly realize that this case is invalid, as that implies p is even, and p=2 doesn't work here
Hence, $p=\boxed{307}$ is our only answer
pi_is_3.141

## Solution 7
If $16p+1 =k$ , we have $k \equiv 1 \mod 16$ , so $k^3 \equiv 1 \mod 16$ . If $k=1$ we have $p=0$ , which is not prime. If $k=17$ we have $16p+1=4913$ , or $p=\boxed{307}$

## Solution 8 (Pattern Recognition)
Notice that: \begin{align*} 1^3 &= 0 +1\\ 2^3 &= 1*7+1 \\ 3^3 &= 2*13+1\\ 4^3 &= 3*21+1\\ 5^3 &= 4*31+1\\ 6^3 &= 5*43+1 \end{align*}
Here, we can see a clear pattern that $n^3=(n-1)p+1$ , where $p$ is some positive (not necessarily prime) integer. Hence, the equation $16p+1=a^3$ can interpret as $17^3 = 16p+1$ . Solving it, we got $p=307$ . After checking all possible divisors, we will find that $307$ is prime. Hence, we got $p=\boxed{307}$ .

## Solution 9 (Slightly Different Modular Arithmetic)
We see that $16p+1=n^3$ for a positive integer $n$ . Subtracting $1$ , we can turn this equation into a modular congruence, since $n^3-1$ must be a multiple of $16$ .
Since $n^3-1\equiv0\pmod{16}$ , $n^3\equiv1\pmod{16}$ . We observe that $n=1$ is a solution to this congruence, which doesn't work. The next, or most obvious number to try is $n=17$ . Plugging this in to our original equation, we get
$17^3=16p+1$ , yielding $p=\boxed{307}$ , which is prime.
-among us (countmath1)

## Solution 10 (Lengthy Brute Force)
Recognizing that AIME answers are $0$ through $999$ , the numbers whose cube could even be in contention to be equal to $16p + 1$ are $4-25$ . The cubes of $1-3$ are all below $17$ . We might consider $1$ , but that would result in a $p$ of $0$ , which is not prime and does not follow our given conditions. We can also see that $16p + 1$ must be an odd number. Hence, we brute force by looking at all cubes of odd numbers in $5-25$ until we get that the cube of $17$ , $4913$ , works when $p=\boxed{307}$
Solution by: armang32324
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .