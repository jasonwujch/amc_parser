# 2020 AIME I Problem 12

## Problem

Let $n$ be the least positive integer for which $149^n-2^n$ is divisible by $3^3\cdot5^5\cdot7^7.$ Find the number of positive integer divisors of $n.$

## Solution 1.1
As usual, denote $v_p(n)$ the highest power of prime $p$ that divides $n$ . Lifting the Exponent shows that \[3=v_3(149^n-2^n) = v_3(n) + v_3(147) = v_3(n)+1\] so thus, $3^2$ divides $n$ . It also shows that \[7=v_7(149^n-2^n) = v_7(n) + v_7(147) = v_7(n)+2\] so thus, $7^5$ divides $n$ .
Now, setting $n = 4c$ (necessitated by $149^n \equiv 2^n \pmod 5$ in order to set up LTE), we see \[v_5(149^{4c}-2^{4c}) = v_5(149^{4c}-16^{c})\] and since $149^{4} \equiv 1 \pmod{25}$ and $16^1 \equiv 16 \pmod{25}$ then $v_5(149^{4c}-2^{4c})=v_5(149^4-16)+v_5(c)=1+v_5(c)$ meaning that we have that by LTE, $5^4 | c$ and $4 \cdot 5^4$ divides $n$ .
Since $3^2$ , $7^5$ and $4\cdot 5^4$ all divide $n$ , the smallest value of $n$ working is their LCM, also $3^2 \cdot 7^5 \cdot 4 \cdot 5^4 = 2^2 \cdot 3^2 \cdot 5^4 \cdot 7^5$ . Thus the number of divisors is $(2+1)(2+1)(4+1)(5+1) = \boxed{270}$ .
~kevinmathz
clarified by another user
notation note from another user
### Note
We were able to use LTE with 3 and 7 but not 5 because in order to use LTE, we need \( p \mid x-y \).
Obviously, \( 149^n \equiv 2^n \pmod{3} \) implies \( 149^n - 2^n \equiv 0 \pmod{3} \), so LTE works here.
Furthermore, \( 149^n \equiv 2^n \pmod{7} \) implies \( 149^n - 2^n \equiv 0 \pmod{7} \), so LTE works here.
However, when we get to the case of 5, we see that \( 149^n \equiv 2^n \pmod{5} \) doesn't always hold; specifically, this is only valid when \( n \) is a multiple of \( 4 \), which is why we let \( n = 4c \) in the solution.
mathboy282

## Solution 1.2 (LTE + Binomial)
Follow solution 1 to get that $3^2 \cdot 7^5$ is a divisor of $n$ . We now take care of the $5^5$ part. Rewrite $149^n-2^n$ as $(150-1)^n-2^n$ and assume $n$ is even. Since this expression is divisible by $5^5$ , we expand and get \[\binom n0(1^n)-\binom n1(1^{n-1}150^1)+\binom n2(1^{n-2}150^2)\cdot\cdot\cdot+\binom nn(150^n)-2^n \equiv 0 \pmod {5^5}.\] Everything except the first three terms and the $2^n$ term is divisible by $5^5$ , so we can rewrite this as \[1-150n+\frac{n(n-1)}{2}150^2-2^n \equiv 0 \pmod {5^5},\] And the following must be true: \[1-150n+\frac{n(n-1)}{2}150^2-2^n \equiv 0 \pmod {5^2}.\] Since $150n+\frac{n(n-1)}{2}150^2$ divides $5^2$ , we can now see that \[1-2^n \equiv 0 \pmod {5^2}.\] Solving for $n$ , $n \equiv 0 \pmod {2^2 \cdot 5}$ . We also know this is true: \[1-150n+\frac{n(n-1)}{2}150^2-2^n \equiv 0 \pmod {5^3}.\] We know $n$ is divisible by $5$ , so $150n+\frac{n(n-1)}{2}150^2$ divides $5^3$ . And now, \[1-2^n \equiv 0 \pmod {5^3}\] gives \[n \equiv 0 \pmod {2^2 \cdot 5^2}.\] This process can be repeated until we obtain $n \equiv 0 \pmod {2^2 \cdot 5^4}$ . The desired solution is then simply $\text{lcm} (3^2 \cdot 7^5, 2^2 \cdot 5^4)$ which yields an answer of $(2+1)(5+1)(2+1)(4+1)=\boxed{270}$ .
~Marchk26

## Solution 2 (Simpler, just basic mods and Fermat's theorem)
Note that for all $n$ , $149^n - 2^n$ is divisible by $149-2 = 147$ by difference of $n$ th powers. That is $3\cdot7^2$ , so now we can clearly see that the smallest $n$ to make the expression divisible by $3^3$ is just $3^2$ . Similarly, we can reason that the smallest $n$ to make the expression divisible by $7^7$ is just $7^5$ .
Finally, for $5^5$ , take $\pmod {5}$ and $\pmod {25}$ of each quantity (They happen to both be $-1$ and $2$ respectively, so you only need to compute once). One knows from Fermat's theorem that the maximum possible minimum $n$ for divisibility by $5$ is $4$ , and other values are factors of $4$ . Testing all of them(just $1$ , $2$ , $4$ using mods-not too bad), $4$ is indeed the smallest value to make the expression divisible by $5$ , and this clearly is NOT divisible by $25$ . Therefore, the smallest $n$ to make this expression divisible by $5^5$ is $2^2 \cdot 5^4$ .
Calculating the LCM of all these, one gets $2^2 \cdot 3^2 \cdot 5^4 \cdot 7^5$ . Using the factor counting formula, the answer is $3\cdot3\cdot5\cdot6$ = $\boxed{270}$ .
~Solution by thanosaops
~formatted by MY-2 and pandyhu2001

## Solution 3 (Using Totient Theorem for upper bound)
For the $5^5$ case, we can see that the problem implies $149^n \equiv 2^n \pmod{5^5}.$
The modular inverse of $2 \pmod{3125}$ is the least positive integer $x$ such that $2x \equiv 1 \pmod{3125}.$ \[x = \frac{3125 + 1}{2} = 1563 \implies (149\cdot1563)^n \equiv 1 \pmod{5^5}.\]
Now we can use Euler's Totient Theorem to get an upper bound for n, which states that if $\gcd(a,b) = 1,$ then $a^{\phi(b)} \equiv 1 \pmod{b}.$ $\phi(5^5) = 3125 \cdot (1 - \frac{1}{5}) = 2500,$ so $(149\cdot1563)^{2500} \equiv (1137)^{2500} \equiv 1 \pmod{5^5}.$
For the number to end with $1,$ $n$ also needs to be a multiple of $4.$ So it's a factor of $2500$ that's also divisible by 4. We bash out the factors of $625.$ Through repeated squaring we see none of the factors work, so $2500$ must be the minimum. Therefore, n must be a multiple of $2500.$
Next, we consider modulo $27$ : \[149^n - 2^n \equiv 14^n - 2^n \pmod{27} \equiv 0 \pmod{27}.\] \[14^n \equiv 2^n \pmod{27}\] \[7^n \equiv 1 \pmod{27}\] Apply Euler's Totient Theorem again to get $7^{18} \equiv 1 \pmod{27}.$
Bashing the factors of 18, we find $18$ is the smallest value that works, so $n$ needs to be a multiple of $18.$
For the $7^7$ case we can set up another congruence: \[149^n - 2^n \equiv 0 \pmod{7^7} \implies (2 + 7 \cdot 21)^n - 2^n \equiv 0 \pmod{7^7}\]
To continue evaluating we use the Binomial Theorem: \[\sum_{k=0}^{n} \binom{n}{k} 2^{n-k} (7 \cdot 21)^k - 2^n \equiv 0 \pmod{7^7}\] \[\cancel{2^n} + \binom{n}{1} 2^{n-1} (7 \cdot 21) + \binom{n}{2} 2^{n-2} (7 \cdot 21)^2 + \dots \cancel{- 2^n} \equiv 0 \pmod{7^7}\] \[\binom{n}{1} \cdot 2^{n-1} \cdot 147 + \binom{n}{2} 2^{n-2} \cdot 147^2 + \binom{n}{3} 2^{n-3} \cdot 147^3 + \binom{n}{4} 2^{n-4} \cdot 147^4 \dots \equiv 0 \pmod{7^7}.\]
Since $147 = 3 \cdot 7^2,$ the first term is a multiple of $7^2,$ the second is a multiple of $7^4,$ and the third is a multiple of $7^6.$ Everything after is a multiple of $7^7.$
So $n$ must be a multiple of $7^5$ at the minimum for these three terms to also be multiples of $7^7.$
Putting everything together we find the smallest value of $n$ to be $n = 2^2 \cdot 3^2 \cdot 5^4 \cdot 7^5,$ so the answer is $(2+1)(2+1)(4+1)(5+1) = \boxed{270}.$
~ grogg007

## Solution 4 (Elementary and Thorough)
As usual, denote $v_p(n)$ the highest power of prime $p$ that divides $n$ . For divisibility by $3^3$ , notice that $v_3(149^3 - 2^3) = 2$ as $149^3 - 2^3 =$ $(147)(149^2 + 2\cdot149 + 2^2)$ , and upon checking mods, $149^2 + 2\cdot149 + 2^2$ is divisible by $3$ but not $9$ . In addition, $149^9 - 2^9$ is divisible by $3^3$ because $149^9 - 2^9 = (149^3 - 2^3)(149^6 + 149^3\cdot2^3 + 2^6)$ , and the rightmost factor equates to $1 + 1 + 1 \pmod{3} \equiv 0 \pmod{3}$ . In fact, $n = 9 = 3^2$ is the least possible choice to ensure divisibility by $3^3$ because if $n = a \cdot 3^b$ , with $3 \nmid a$ and $b < 2$ , we write \[149^{a \cdot 3^b} - 2^{a \cdot 3^b} = (149^{3^b} - 2^{3^b})(149^{3^b(a - 1)} + 149^{3^b(a - 2)}\cdot2^{3^b}+\cdots2^{3^b(a - 1)}).\] Then, the rightmost factor is equivalent to $\pm a \pmod{3} \not\equiv 0 \pmod{3}$ , and $v_3(149^{3^b} - 2^{3^b}) = b + 1 < 3$ .
For divisibility by $7^7$ , we'll induct, claiming that $v_7(149^{7^k} - 2^{7^k}) = k + 2$ for whole numbers $k$ . The base case is clear. Then, \[v_7(149^{7^{k+1}} - 2^{7^{k+1}}) = v_7(149^{7^k} - 2^{7^k}) + v_7(149^{6\cdot7^k} + 2^{7^k}\cdot149^{5\cdot7^k} + \cdots + 2^{5\cdot7^k}\cdot149^{7^k} + 2^{6\cdot7^k}).\] By the induction hypothesis, $v_7(149^{7^k} - 2^{7^k}) = k + 2$ . Then, notice that \[S(k) = 149^{6\cdot7^k} + 2^{7^k}\cdot149^{5\cdot7^k} + \cdots + 2^{5\cdot7^k}\cdot149^{7^k} + 2^{6\cdot7^k} \equiv 7 \cdot 2^{6\cdot7^k}\pmod{7} \equiv 7 \cdot 2^{6\cdot7^k}\pmod{49}.\] This tells us that $S(k)$ is divisible by $7$ , but not $49$ so that $v_7\left(S(k)\right) = 1$ , completing our induction. We can verify that $7^5$ is the least choice of $n$ to ensure divisibility by $7^7$ by arguing similarly to the $3^3$ case.
Finally, for $5^5$ , we take the powers of $149$ and $2$ in mod $5$ and mod $25$ . Writing out these mods, we have that $149^n \equiv 2^n \pmod{5}$ if and only if $4 | n$ , in which $149^n \equiv 2^n \equiv 1 \pmod{5}$ . So here we claim that $v_5(149^{4\cdot5^k} - 2^{4\cdot5^k}) = k + 1$ and perform yet another induction. The base case is true: $5 | 149^4 - 2^4$ , but $149^4 - 2^4 \equiv 1 - 16 \pmod{25}$ . Now then, assuming the induction statement to hold for some $k$ , \[v_5(149^{4\cdot5^{k+1}} - 2^{4\cdot5^{k+1}}) = (k+1) + v_5(149^{4\cdot4\cdot5^k}+2^{4\cdot5^k}\cdot149^{3\cdot4\cdot5^k}+\cdots+2^{3\cdot4\cdot5^k}\cdot149^{4\cdot5^k}+2^{4\cdot4\cdot5^k}).\] Note that $S'(k) = 149^{4\cdot4\cdot5^k}+2^{4\cdot5^k}\cdot149^{3\cdot4\cdot5^k}+\cdots+2^{3\cdot4\cdot5^k}\cdot149^{4\cdot5^k}+2^{4\cdot4\cdot5^k}$ equates to $S''(k) = 1 + 2^{4\cdot5^k} + \cdots + 2^{16\cdot5^k}$ in both mod $5$ and mod $25$ . We notice that $S''(k) \equiv 0 \pmod{5}$ . Writing out the powers of $2$ mod $25$ , we have $S''(0) \equiv 5 \pmod{25}$ . Also $2^n \equiv 1 \pmod{25}$ when $n$ is a multiple of $20$ . Hence for $k > 0$ , $S''(k) \equiv 5 \mod{25}$ . Thus, $v_5\left(S'(k)\right) = 1$ , completing our induction. Applying the same argument from the previous two cases, $4\cdot5^4$ is the least choice to ensure divisibility by $5^5$ .
Our answer is the number of divisors of $\text{lcm}(3^2, 7^5, 2^2\cdot5^4) = 2^2 \cdot 3^2 \cdot 5^4 \cdot 7^5$ . It is $(2 + 1)(2 + 1)(4 + 1)(5 + 1) = \boxed{270}$ .
~hnkevin42

## Solution 5 (Official MAA)
Analyze each prime power separately. Start with the case of $3^3$ . By the Binomial Theorem, \begin{align*} 149^n - 2^n &= (147+2)^n - 2^n \\ &= \binom n1 \cdot 147 \cdot 2^{n-1} + \binom n2 \cdot 147^2 \cdot 2^{n-2}\\ &\qquad+ \binom n3 \cdot 147^3 \cdot 2^{n-3} + \cdots. \end{align*} Because $147$ is divisible by $3$ , all terms after the first two are divisible by $3^3$ , and the exponent of $3$ in the first term is less than that in the second term. Hence it is necessary and sufficient that $3^3 \mid 147n$ , that is, $3^2 \mid n$ . For the $7^7$ case, consider the same expansion as in the previous case. Because $147$ is divisible by $49 = 7^2$ , all terms after the first three are divisible by $7^7$ , and the exponent of $7$ in the first term is less than that in the second and third term. Hence it is necessary and sufficient that $7^7 \mid 147n$ , that is, $7^5 \mid n$ . For the $5^5$ case, working modulo $5$ gives $149^n - 2^n \equiv 4^n - 2^n = 2^n(2^n-1) \pmod 5$ , so it must be that $4 \mid n$ . Let $n = 4m$ , and let $c = 149^4 - 2^4 = (149^2-2^2)(149^2+2^2) = 147 \cdot 151 \cdot 22205$ . Note that $\frac c5$ is an integer not divisible by $5$ . Expand by the Binomial Theorem again to get \begin{align*} (149^4)^m - (2^4)^m &= (c+16)^m - (16)^m \\ &= \binom m1 \cdot c \cdot 16^{m-1} + \binom m2 \cdot c^2 \cdot 16^{m-2} \\ &\qquad+ \binom m3 \cdot c^3 \cdot 16^{m-3} + \binom m4 \cdot c^4 \cdot 16^{m-4} + \cdots. \end{align*} All terms after the first four are divisible by $5^5$ , and the exponent of $5$ in the first term is less than that in the second, third, or fourth term. Hence it is necessary and sufficient that $5^5 \mid cm$ . Thus $5^4 \mid m$ , and it follows that $4 \cdot 5^4 \mid n$ . Therefore the least $n$ is $3^2 \cdot (2^2 \cdot 5^4) \cdot 7^5$ . The requested number of divisors is $(1+2)(1+2)(1+4)(1+5) = 270$ .
The results of the above cases can be generalized using the following lemma.
Lifting the Exponent Lemma: Let $p$ be an odd prime, and let $a$ and $b$ be integers relatively prime to $p$ such that $p \mid (a-b)$ . Let $n$ be a positive integer. Then the number of factors of $p$ that divide $a^n - b^n$ is equal to the number of factors of $p$ that divide $a-b$ plus the number of factors of $p$ that divide $n$ .

## Video Solution
https://www.youtube.com/watch?v=O0BprEOVkjo ~ Math Gold Medalist
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .