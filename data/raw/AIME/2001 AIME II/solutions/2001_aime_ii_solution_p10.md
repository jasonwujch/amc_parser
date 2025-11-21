# 2001 AIME II Problem 10

## Problem

How many positive integer multiples of $1001$ can be expressed in the form $10^{j} - 10^{i}$ , where $i$ and $j$ are integers and $0\leq i < j \leq 99$ ?

## Solution 1
The prime factorization of $1001 = 7\times 11\times 13$ . We have $7\times 11\times 13\times k = 10^j - 10^i = 10^i(10^{j - i} - 1)$ . Since $\text{gcd}\,(10^i = 2^i \times 5^i, 7 \times 11 \times 13) = 1$ , we require that $1001 = 10^3 + 1 | 10^{j-i} - 1$ . From the factorization $10^6 - 1 = (10^3 + 1)(10^{3} - 1)$ , we see that $j-i = 6$ works; also, $a-b | a^n - b^n$ implies that $10^{6} - 1 | 10^{6k} - 1$ , and so any $\boxed{j-i \equiv 0 \pmod{6}}$ will work.
To show that no other possibilities work, suppose $j-i \equiv a \pmod{6},\ 1 \le a \le 5$ , and let $j-i-a = 6k$ . Then we can write $10^{j-i} - 1 = 10^{a} \left(10^{6k} - 1\right) + \left(10^{a} - 1\right)$ , and we observe that $10^{6k}-1 = \left(10^6\right)^k-1^k$ , which is divisible by $10^6-1$ , and thus by $10^3+1$ (as $10^6-1 = \left(10^3\right)^2-1^2 = \left(10^3+1\right)\left(10^3-1\right)$ ). It follows that the first term is divisible by $1001$ , whereas we can easily verify that the second term, $10^a-1$ , is not divisible by $1001$ for $1 \le a \le 5$ , so $10^{j-i}$ is not divisible by $1001$ for such $a$ .
If $j - i = 6, j\leq 99$ , then we can have solutions of $10^6 - 10^0, 10^7 - 10^1, \dots\implies 94$ ways. If $j - i = 12$ , we can have the solutions of $10^{12} - 10^{0},\dots\implies 94 - 6 = 88$ , and so forth. Therefore, the answer is $94 + 88 + 82 + \dots + 4\implies 16\left(\dfrac{98}{2}\right) = \boxed{784}$ .

## Solution 2
Observation: We see that there is a pattern with $10^k \pmod{1001}$ . \[10^0 \equiv 1 \pmod{1001}\] \[10^1 \equiv 10 \pmod{1001}\] \[10^2 \equiv 100 \pmod{1001}\] \[10^3 \equiv -1 \pmod{1001}\] \[10^4 \equiv -10 \pmod{1001}\] \[10^5 \equiv -100 \pmod{1001}\] \[10^6 \equiv 1 \pmod{1001}\] \[10^7 \equiv 10 \pmod{1001}\] \[10^8 \equiv 100 \pmod{1001}\]
So, this pattern repeats every 6.
Also, $10^j-10^i \equiv 0 \pmod{1001}$ , so $10^j \equiv 10^i \pmod{1001}$ , and thus, \[j \equiv i \pmod{6}\] . Continue with the 2nd paragraph of solution 1, and we get the answer of $\boxed{784}$ .
-AlexLikeMath

## Solution 3
Note that $1001=7\cdot 11\cdot 13,$ and note that $10^6 \equiv 1 \pmod{p}$ for prime $p \mid 1001$ ; therefore, the order of 10 modulo $7,11$ , and $13$ must divide 6. A quick check on 7 reveals that it is indeed 6. Therefore we note that $i-j=6k$ for some natural number k. From here, we note that for $j=0,1,2,3,$ we have 16 options and we have 15,14,...,1 option(s) for the next 90 numbers (6 each), so our total is $4\cdot 16 + 6 \cdot \frac{15 \cdot 16}{2} = \boxed{784}$ .
~Dhillonr25

## Solution 4
$10^j - 10^i \equiv 0 \pmod{1001} \iff 10^{j - i} - 1 \equiv 0 \pmod{1001} \iff 10^{j - i} \equiv 1 \pmod{1001} \iff j \equiv i \pmod 6$ , by the same argument as in all the solutions above. If $j \equiv i \equiv n \pmod 6$ for $n = 0, 1, 2, 3$ , there are $17$ choices for each value of $n$ , yielding $4 \cdot \dbinom{17}{2} = 544$ . However, if $n = 4, 5$ , there are only $16$ choices, giving us $2 \cdot \dbinom{16}{2} = 240$ . So, our final answer is $544 + 240 = \boxed{784}$ . ~Puck_0
These problems are copyrighted © by the Mathematical Association of America.