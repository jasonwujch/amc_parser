# 2018 AIME I Problem 11

## Problem

Find the least positive integer $n$ such that when $3^n$ is written in base $143$ , its two right-most digits in base $143$ are $01$ .

## Solution 1
Note that the given condition is equivalent to $3^n \equiv 1 \pmod{143^2}$ and $143=11\cdot 13$ . Because $\gcd(11^2, 13^2) = 1$ , the desired condition is equivalent to $3^n \equiv 1 \pmod{121}$ and $3^n \equiv 1 \pmod{169}$ .
If $3^n \equiv 1 \pmod{121}$ , one can see the sequence $1, 3, 9, 27, 81, 1, 3, 9...$ so $5|n$ .
Now if $3^n \equiv 1 \pmod{169}$ , it is harder. But we do observe that $3^3 \equiv 1 \pmod{13}$ , therefore $3^3 = 13a + 1$ for some integer $a$ . So our goal is to find the first number $p_1$ such that $(13a+1)^ {p_1} \equiv 1 \pmod{169}$ . Then, $p_1 \equiv 0 \pmod{13},$ which follows from the binomial theorem. It is not difficult to see that the smallest $p_1=13$ , so ultimately $3^{39} \equiv 1 \pmod{169}$ . Therefore, $39|n$ .
The first $n$ satisfying both criteria is thus $5\cdot 39=\boxed{195}$ .
-expiLnCalc

## Solution 2
Note that Euler's Totient Theorem would not necessarily lead to the smallest $n$ and that in this case that $n$ is greater than $1000$ .
We wish to find the least $n$ such that $3^n \equiv 1 \pmod{143^2}$ . This factors as $143^2=11^{2}*13^{2}$ . Because $\gcd(121, 169) = 1$ , we can simply find the least $n$ such that $3^n \equiv 1 \pmod{121}$ and $3^n \equiv 1 \pmod{169}$ .
Quick inspection yields $3^5 \equiv 1 \pmod{121}$ and $3^3 \equiv 1 \pmod{13}$ . Now we must find the smallest $k$ such that $3^{3k} \equiv 1 \pmod{169}$ . Euler's gives $3^{156} \equiv 1 \pmod{169}$ . So $3k$ is a factor of $156$ . This gives $k=1,2, 4, 13, 26, 52$ . Some more inspection yields $k=13$ is the smallest valid $k$ . So $3^5 \equiv 1 \pmod{121}$ and $3^{39} \equiv 1 \pmod{169}$ . The least $n$ satisfying both is $lcm(5, 39)=\boxed{195}$ . (RegularHexagon)

## Solution 3 (Big Bash)
Listing out the powers of $3$ , modulo $169$ and modulo $121$ , we have: \[\begin{array}{c|c|c} n & 3^n\mod{169} & 3^n\mod{121}\\ \hline 0 & 1 & 1\\ 1 & 3 & 3\\ 2 & 9 & 9\\ 3 & 27 & 27\\ 4 & 81 & 81\\ 5 & 74 & 1\\ 6 & 53\\ 7 & 159\\ 8 & 139\\ 9 & 79\\ 10 & 68\\ 11 & 35\\ 12 & 105\\ 13 & 146\\ 14 & 100\\ 15 & 131\\ 16 & 55\\ 17 & 165\\ 18 & 157\\ 19 & 133\\ 20 & 61\\ 21 & 14\\ 22 & 42\\ 23 & 126\\ 24 & 40\\ 25 & 120\\ 26 & 22\\ 27 & 66\\ 28 & 29\\ 29 & 87\\ 30 & 92\\ 31 & 107\\ 32 & 152\\ 33 & 118\\ 34 & 16\\ 35 & 48\\ 36 & 144\\ 37 & 94\\ 38 & 113\\ 39 & 1\\ \end{array}\]
The powers of $3$ repeat in cycles of $5$ and $39$ in modulo $121$ and modulo $169$ , respectively. The answer is $\text{lcm}(5, 39) = \boxed{195}$ .
~Minor edit by Yiyj1

## Solution 4 (Order+Bash)
We have that \[3^n \equiv 1 \pmod{143^2}.\] Now, $3^{110} \equiv 1 \pmod{11^2}$ so by the Fundamental Theorem of Orders, $\text{ord}_{11^2}(3)|110$ and with some bashing, we get that it is $5$ . Similarly, we get that $\text{ord}_{13^2}(3)=39$ . Now, $\text{lcm}(39,5)=\boxed{195}$ which is our desired solution.

## Solution 5 (Easy Binomial Theorem)
We wish to find the smallest $n$ such that $3^n\equiv 1\pmod{143^2}$ , so we want $n\equiv 1\pmod{121}$ and $n\equiv 1\pmod{169}$ . Note that $3^5\equiv 1\pmod{121}$ , so $3^n$ repeats $121$ with a period of $5$ , so $5|n$ . Now, in order for $n\equiv 1\pmod{169}$ , then $n\equiv 1\pmod{13}$ . Because $3^3\equiv 1\pmod{13}$ , $3^n$ repeats with a period of $3$ , so $3|n$ . Hence, we have that for some positive integer $p$ , $3^n\equiv (3^3)^p\equiv (26+1)^p\equiv \binom{p}{0}26^p+\binom{p}{1}26^{p-1}....+\binom{p}{p-2}26^2+\binom{p}{p-1}26+\binom{p}{p}\equiv 26p+1\equiv 1\pmod{169}$ , so $26p\equiv 0\pmod{169}$ and $p\equiv 0\pmod{13}$ . Thus, we have that $5|n$ , $3|n$ , and $13|n$ , so the smallest possible value of $n$ is $3\times5\times13=\boxed{195}$ . -Stormersyle

## Solution 6 (LTE)
We can see that $3^n-1 = 143^2*x$ , which means that $v_{11}(3^n-1) \geq 2$ , $v_{13}(3^n-1) \geq 2$ . $v_{11}(3^n-1) = v_{11}(242) + v_{11}(\frac{n}{5})$ , $v_{13}(3^n-1) = v_{13}(26) + v_{13}(\frac{n}{3})$ by the Lifting the Exponent lemma. From the first equation we gather that 5 divides n, while from the second equation we gather that both 13 and 3 divide n as $v_{13}(3^n-1) \geq 2$ . Therefore the minimum possible value of n is $3\times5\times13=\boxed{195}$ .
-bradleyguo

## Solution 7 (LTE, more in-depth)
As with the above solution, we are given $3^n \equiv 1 \pmod {143^2}.$ From CRT, we can separate these into. $3^n \equiv 1 \pmod {11^2}$ and $3^n \equiv 1 \pmod {13^2}.$
(1) $3^n \equiv 1 \pmod {11^2}$ Notice that for all $n \equiv 0 \pmod 5,$ the given equivalency holds. Hence, $5 \mid n.$
(2) $3^n \equiv 1 \pmod {13^2}.$ It is not exactly clear what $n$ would be here. We turn to LTE.
First, note that $3^3 \equiv 1 \pmod {13} \Rightarrow \nu_{13}(3^3-1)=1.$
For LTE, if we use $3^n-1^n,$ then we would need an odd prime to divide $3-1=2,$ absurd. If we instead use $3^{3n'}-1^{3n'}$ where $n=3n' \iff n \equiv 0 \pmod 3,$ then we can apply LTE.
We have $\nu_{13}((3^3)^{n'}-(1^3)^{n'})=\nu_{13}(n')+\nu_{13}(3^3-1^3)=\nu_{13}(n')+1.$
We need $\nu_{13}((3^3)^{n'}-(1^3)^{n'}) \geq 2 \Rightarrow \nu_{13}(n') \geq 1.$ Hence, $13 \mid n.$
All in all, we need $3, 5, 13 \mid n,$ and the minimum such value is $195.$
~mathboy282

## Solution 8
Note that the problem is basically asking for the least positive integer $n$ such that $11^2 \cdot 13^2 | 3^n - 1.$ It is easy to see that $n = \text{lcm } (a, b),$ where $a$ is the least positive integer satisfying $11^2 | 3^a - 1$ and $b$ the least positive integer satisfying $13^2 | 3^b - 1$ . Luckily, finding $a$ is a relatively trivial task, as one can simply notice that $3^5 = 243 \equiv 1 \mod 121$ . However, finding $b$ is slightly more nontrivial. The order of $3^k$ modulo $13$ (which is $3$ ) is trivial to find, as one can either bash out a pattern of remainders upon dividing powers of $3$ by $13$ , or one can notice that $3^3 = 27 \equiv 1 \mod 13$ (the latter which is the definition of period/orders by FLT). We can thus rewrite $3^3$ as $(2 \cdot 13 + 1) \mod 13^2$ . Now suppose that \[3^{3k} \equiv (13n + 1) \mod 13^2.\] I claim that $3^{3(k+1)} \equiv (13(n+2) + 1) \mod 13^2.$
Proof: To find $3^{3(k+1)},$ we can simply multiply $3^{3k}$ by $3^3,$ which is congruent to $2 \cdot 13 + 1$ modulo $13^2$ . By expanding the product out, we obtain \[3^{3(k+1)} \equiv (13n + 1)(2 \cdot 13 + 1) = 13^2 \cdot 2n + 13n + 2 \cdot 13 + 1 \mod 13^2,\] and since the $13^2$ on the LHS cancels out, we're left with \[13n + 2 \cdot 13 + 1 \mod 13^2 \implies 13(n+2) + 1 \mod 13^2\] . Thus, our claim is proven. Let $f(n)$ be the second to last digit when $3^{3k}$ is written in base $13^2$ . Using our proof, it is easy to see that $f(n)$ satisfies the recurrence $f(1) = 2$ and $f(n+1) = f(n) + 2$ . Since this implies $f(n) = 2n,$ we just have to find the least positive integer $n$ such that $2n$ is a multiple of $13$ , which is trivially obtained as $13$ . The least integer $n$ such that $3^n - 1$ is divisible by $13^2$ is $3 \cdot 13 = 39,$ so our final answer is $\text{lcm } (5, 39) = \boxed{195}.$
-fidgetboss_4000 -minor edits made by srisainandan6

## Solution 9 (Official MAA)
The requested positive integer is the least value of $n>0$ such that $3^n\equiv 1\pmod{143^2}.$ Note that $143=11\cdot 13.$ The least power of $3$ that is congruent to $1$ modulo $11^2$ is $3^5=243=2\cdot 11^2+1.$ It follows that. $3^n\equiv 1\pmod {11^2}$ if and only if $n=5j$ for some positive integer $j$ .
The least power of $3$ that is congruent to $1$ modulo $13$ is $3^3=27=2\cdot 13+1.$ It follows that $3^n\equiv 1\pmod{13}$ if and only if $n=3k$ for some positive integer $k$ . Additionally, for some positive integer $k$ , the Binomial Theorem shows that $3^{3k}=(26+1)^k=26\cdot k+1 \pmod{13^2}$ . In particular, $3^n=3^{3k}\equiv 1\pmod {13^2}$ if and only if $k=13m$ for some positive integer $m$ , that is, if and only if $n=39m.$
Because $11^2$ and $13^2$ are relatively prime, $3^n\equiv 1\pmod {143^2}$ if and only if $3^n\equiv 1\pmod{11^2}$ and $3^n \equiv 1\pmod {13^2}$ . This occurs if and only if $n$ is a multiple of both of the relatively prime integers $5$ and $39$ , so the least possible value of $n$ is $5\cdot 39=\boxed{195}.$

## Solution 10 (Motivation and LTE)
We first note that we wish to find $3^n \equiv 1 \pmod{11^2}$ and $3^n \equiv 1 \pmod{13^2}.$ Not thinking of anything else, we try a few numbers for the first condition to get that $5 \mid n.$ For the second condition, upon testing up to 729, we find that it doesn't yield a solution readily, so we use Lifting the Exponent from our toolkit to get that \[v_{13}(27^m-1^m)=v_{13}(26)+v(m)=1+v(m), 3m = n\] which clearly implies $m=13$ and $39 | n.$ Our answer is then obviously $39 \cdot 5 = \boxed{195}.$
~Dhillonr25
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .