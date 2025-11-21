# 2021 AIME I Problem 14

## Problem

For any positive integer $a, \sigma(a)$ denotes the sum of the positive integer divisors of $a$ . Let $n$ be the least positive integer such that $\sigma(a^n)-1$ is divisible by $2021$ for all positive integers $a$ . Find the sum of the prime factors in the prime factorization of $n$ .

## Solution 1
We first claim that $n$ must be divisible by $42$ . Since $\sigma(a^n)-1$ is divisible by $2021$ for all positive integers $a$ , we can first consider the special case where $a$ is prime and $a \neq 0,1 \pmod{43}$ . By Dirichlet's Theorem (Refer to the Remark section.), such $a$ always exists.
Then $\sigma(a^n)-1 = \sum_{i=1}^n a^i = a\left(\frac{a^n - 1}{a-1}\right)$ . In order for this expression to be divisible by $2021=43\cdot 47$ , a necessary condition is $a^n - 1 \equiv 0 \pmod{43}$ . By Fermat's Little Theorem , $a^{42} \equiv 1 \pmod{43}$ . Moreover, if $a$ is a primitive root modulo $43$ , then $\text{ord}_{43}(a) = 42$ , so $n$ must be divisible by $42$ .
By similar reasoning, $n$ must be divisible by $46$ , by considering $a \not\equiv 0,1 \pmod{47}$ .
We next claim that $n$ must be divisible by $43$ . By Dirichlet, let $a$ be a prime that is congruent to $1 \pmod{43}$ . Then $\sigma(a^n) \equiv n+1 \pmod{43}$ , so since $\sigma(a^n)-1$ is divisible by $43$ , $n$ is a multiple of $43$ .
Alternatively, since $\left(\frac{a(a^n - 1^n)}{a-1}\right)$ must be divisible by $43,$ by LTE, we have $v_{43}(a)+v_{43}{(a-1)}+v_{43}{(n)}-v_{43}{(a-1)} \geq 1,$ which simplifies to $v_{43}(n) \geq 1,$ which implies the desired result.
Similarly, $n$ is a multiple of $47$ .
Lastly, we claim that if $n = \text{lcm}(42, 46, 43, 47)$ , then $\sigma(a^n) - 1$ is divisible by $2021$ for all positive integers $a$ . The claim is trivially true for $a=1$ so suppose $a>1$ . Let $a = p_1^{e_1}\ldots p_k^{e_k}$ be the prime factorization of $a$ . Since $\sigma(n)$ is multiplicative , we have \[\sigma(a^n) - 1 = \prod_{i=1}^k \sigma(p_i^{e_in}) - 1.\] We can show that $\sigma(p_i^{e_in}) \equiv 1 \pmod{2021}$ for all primes $p_i$ and integers $e_i \ge 1$ , so \[\sigma(p_i^{e_in}) = 1 + (p_i + p_i^2 + \ldots + p_i^n) + (p_i^{n+1} + \ldots + p_i^{2n}) + \ldots + (p_i^{n(e_i-1)+1} + \ldots + p_i^{e_in}),\] where each expression in parentheses contains $n$ terms. It is easy to verify that if $p_i = 43$ or $p_i = 47$ then $\sigma(p_i^{e_in}) \equiv 1 \pmod{2021}$ for this choice of $n$ , so suppose $p_i \not\equiv 0 \pmod{43}$ and $p_i \not\equiv 0 \pmod{47}$ . Each expression in parentheses equals $\frac{p_i^n - 1}{p_i - 1}$ multiplied by some power of $p_i$ . If $p_i \not\equiv 1 \pmod{43}$ , then FLT implies $p_i^n - 1 \equiv 0 \pmod{43}$ , and if $p_i \equiv 1 \pmod{43}$ , then $p_i + p_i^2 + \ldots + p_i^n \equiv 1 + 1 + \ldots + 1 \equiv 0 \pmod{43}$ (since $n$ is also a multiple of $43$ , by definition). Similarly, we can show $\sigma(p_i^{e_in}) \equiv 1 \pmod{47}$ , and a simple CRT argument shows $\sigma(p_i^{e_in}) \equiv 1 \pmod{2021}$ . Then $\sigma(a^n) \equiv 1^k \equiv 1 \pmod{2021}$ .
Then the prime factors of $n$ are $2,3,7,23,43,$ and $47,$ and the answer is $2+3+7+23+43+47 = \boxed{125}$ .
~scrabbler94, Revised by wzs26843545602

## Solution 2 (Along the Lines of Solution 1)
$n$ only needs to satisfy $\sigma(a^n)\equiv 1 \pmod{43}$ and $\sigma(a^n)\equiv 1 \pmod{47}$ for all $a$ . Let's work on the first requirement (mod 43) first. All $n$ works for $a=1$ . If $a>1$ , let $a$ 's prime factorization be $a=p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}$ . The following three statements are the same:
1. For all $a$ , we have $\sigma(a^n)=\prod_{i=1}^k(1+p_i+\cdots+p_i^{ne_i})\equiv1\pmod{43}$ .
1. For all $e>0$ and prime $p$ , we have $1+p+\cdots+p^{ne}\equiv1\pmod{43}$ .
1. For all prime $p$ , we have $p+p^2+\cdots+p^n \equiv 0 \pmod{43}$ .
We can show this by casework on $p$ :
1. For $p\equiv0\pmod{43}$ , no matter what $n$ is, it is true that \[p+p^2+\cdots+p^n \equiv 0 \pmod{43}.\]
1. For all $p\equiv1\pmod{43}$ , it is true that \[p+p^2+\cdots+p^n \equiv n \equiv 0 \pmod{43}.\] One can either use brute force or Dirichlet's Theorem to show such $p$ exists. Therefore, $43|n$ .
1. For all $p\not\equiv0,1\pmod{43}$ , it is true that \[p+p^2+\cdots+p^n \equiv 0 \pmod{43} \Leftrightarrow p^n-1\equiv0\pmod{43}.\] According to Fermat's Little Theorem, $42|n$ is sufficient. To show it's necessary, we just need to show $43$ has a prime primitive root. This can be done either by brute force or as follows. $43$ is prime and it must have a primitive root $t\neq 1$ that's coprime to $43$ . All numbers of the form $43k+t$ are also primitive roots of $43$ . According to Dirichlet's Theorem there must be infinitely many primes among them.
Similar arguments for modulo $47$ lead to $46|n$ and $47|n$ . Therefore, we get $n=\operatorname{lcm}[42,43,46,47]$ . Following the last paragraph of Solution 1 gives the answer $\boxed{125}$ .
~Mryang6859 (Solution)
~MRENTHUSIASM (Reformatting)

## Solution 3 (Casework)
We perform casework on $a:$
1. $a=1.$ For all positive integers we have
1. $a$ is a prime number. For all prime numbers note that by geometric series. Recall that Applying the Chinese Remainder Theorem, we get the following system of congruences: We perform casework on We need If then this congruence is true for all positive integers If then this congruence becomes By Fermat's Little Theorem, we obtain We need to contain more factors of than does. More generally, for all positive integers if then Let for some positive integer such that We substitute this into and apply the Binomial Theorem: from which For $(1),$ we find that $n\equiv0\pmod{42}$ and $n\equiv0\pmod{43}.$ For we find that and by a similar argument. Together, we conclude that is the least such positive integer for this case.
1. $a$ is a composite number. Let be the prime factorization of Note that is a multiplicative function: as this product of geometric series spans all positive divisors of At it follows that
For all positive integers $n,$ we have $\sigma\left(a^n\right)-1=0.$
For all prime numbers $p,$ note that \[\sigma\left(p^n\right)-1=\left(\sum_{i=0}^{n}p^i\right)-1=\sum_{i=1}^{n}p^i=\frac{p^{n+1}-p}{p-1}=\frac{p\left(p^n-1\right)}{p-1}\] by geometric series.
Recall that $2021=43\cdot47.$ Applying the Chinese Remainder Theorem, we get the following system of congruences: \begin{align*} \frac{p\left(p^n-1\right)}{p-1}&\equiv0\pmod{43}, &(1)\\ \frac{p\left(p^n-1\right)}{p-1}&\equiv0\pmod{47}. &(2) \end{align*} We perform casework on $(1):$
1. $p-1\not\equiv0\pmod{43}.$ We need If then this congruence is true for all positive integers If then this congruence becomes By Fermat's Little Theorem, we obtain
1. $p-1\equiv0\pmod{43}.$ We need to contain more factors of than does. More generally, for all positive integers if then Let for some positive integer such that We substitute this into and apply the Binomial Theorem: from which
We need $p\left(p^n-1\right)\equiv0\pmod{43}.$
If $p=43,$ then this congruence is true for all positive integers $n.$
If $p\neq43,$ then this congruence becomes $p^n-1\equiv0\pmod{43}.$ By Fermat's Little Theorem, we obtain $n\equiv0\pmod{42}.$
We need $p^n-1$ to contain more factors of $43$ than $p-1$ does. More generally, for all positive integers $k,$ if $p-1\equiv0 \ \left(\operatorname{mod} \ 43^k\right),$ then $p^n-1\equiv0 \ \left(\operatorname{mod} \ 43^{k+1}\right).$
Let $p=43^km+1$ for some positive integer $m$ such that $m\not\equiv0\pmod{43}.$ We substitute this into $p^n-1\equiv0 \ \left(\operatorname{mod} \ 43^{k+1}\right)$ and apply the Binomial Theorem: \begin{align*} \left(43^km+1\right)^n-1&\equiv0 \ \left(\operatorname{mod} \ 43^{k+1}\right) \\ \Biggl[\binom{n}{0}\left(43^km\right)^0+\binom{n}{1}\left(43^km\right)^1+\phantom{ }\underbrace{\binom{n}{2}\left(43^km\right)^2+\cdots+\binom{n}{n}\left(43^km\right)^n}_{0 \ \left(\operatorname{mod} \ 43^{k+1}\right)}\phantom{ }\Biggr]-1 &\equiv0 \ \left(\operatorname{mod} \ 43^{k+1}\right) \\ \left[1+43^kmn\right]-1&\equiv0 \ \left(\operatorname{mod} \ 43^{k+1}\right) \\ 43^kmn&\equiv0 \ \left(\operatorname{mod} \ 43^{k+1}\right), \end{align*} from which $n\equiv0\pmod{43}.$
For $(2),$ we find that $n\equiv0\pmod{46}$ and $n\equiv0\pmod{47}$ by a similar argument.
Together, we conclude that $n=\operatorname{lcm}(42,43,46,47)$ is the least such positive integer $n$ for this case.
Let $a=\prod_{i=1}^{u}p_i^{e_i}$ be the prime factorization of $a.$ Note that $\sigma(a)$ is a multiplicative function: \[\sigma(a)=\sigma\left(\prod_{i=1}^{u}p_i^{e_i}\right)=\prod_{i=1}^{u}\sigma\left(p_i^{e_i}\right)=\prod_{i=1}^{u}\left(\sum_{j=0}^{e_i}p_i^j\right),\] as this product of geometric series spans all positive divisors of $a.$
At $n=\operatorname{lcm}(42,43,46,47),$ it follows that \begin{align*} \sigma\left(a^n\right)-1&=\left(\prod_{i=1}^{u}\sigma\left(p_i^{e_in}\right)\right)-1 \\ &\equiv\left(\prod_{i=1}^{u}1\right)-1 &&\pmod{2021} \\ &\equiv0 &&\pmod{2021}. \end{align*}
Finally, the least such positive integer $n$ for all cases is \begin{align*} n&=\operatorname{lcm}(42,43,46,47) \\ &=\operatorname{lcm}(2\cdot3\cdot7,43,2\cdot23,47) \\ &=2\cdot3\cdot7\cdot23\cdot43\cdot47, \end{align*} so the sum of its prime factors is $2+3+7+23+43+47=\boxed{125}.$
~MRENTHUSIASM (inspired by Math Jams's 2021 AIME I Discussion )

## Solution 4 (Cheap)
Since the problem works for all positive integers $a$ , let's plug in $a=2$ and see what we get. Since $\sigma({2^n}) = 2^{n+1}-1,$ we have $2^{n+1} \equiv 2 \pmod{2021}.$ Simplifying using CRT and Fermat's Little Theorem , we get that $n \equiv 0 \pmod{42}$ and $n \equiv 0 \pmod{46}.$ Then, we can look at $a$ being a $1\pmod{43}$ prime and a $1\pmod{47}$ prime, just like in Solution 1, to find that $43$ and $47$ also divide $n$ . There don't seem to be any other odd "numbers" to check, so we can hopefully assume that the answer is the sum of the prime factors of $\text{lcm(42, 43, 46, 47)}.$ From here, follow solution 1 to get the final answer $\boxed{125}$ .
~PureSwag

## Solution 5 (Similar to Solution 4 and USEMO 2019 Problem 4)
Warning: This solution doesn't explain why $43*47\mid n$ .
It says the problem implies that it works for all positive integers $a$ , we basically know that If $p \equiv 1 \pmod q$ , then from "USEMO 2019 Problem 4", if $p^n + p^{n-1} + \cdots + 1 \equiv 1 \pmod{q}$ , then \[\frac{p^{en+1}-1}{p-1} = p^{en} + p^{en-1} + \cdots + 1 \equiv 1 \pmod{q}.\] From here we can just let $\sigma(2^n)$ or be a power of $2$ which we can do \[\sigma(2^n)=1+2+2^2+2^3+2^4+\cdots+2^n=2^{n+1}-1,\] which is a geometric series. We can plug in $a=2$ like in Solution 4 and use CRT. We have the prime factorization $2021 = 43 \cdot 47$ . We use CRT to find that \begin{align*} 2^n &\equiv 1 \pmod{43}, \\ 2^n &\equiv 1 \pmod{47}. \end{align*} We see that this is just FLT which is $a^{p-1} \equiv 1 \pmod p$ we see that all multiples of $42$ will work for first and $46$ for the second. We can figure out that it is just $\text{lcm}(43-1,47-1)\cdot43\cdot47$ which when we add up we get that it's just the sum of the prime factors of $\text{lcm}(42,43,46,47)$ which you can just look at Solution 1 to find out the sum of the prime factors and get the answer $\boxed{125}$ .
### Remark (Dirichlet's Theorem)
All solutions require Dirichlet's Theorem, which states that for any coprime positive integers $k$ and $r$ , there are infinitely many primes $p$ congruent to $r\pmod{k}$ .

## Video Solution
https://youtu.be/q0zUFAyGN4s ~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .