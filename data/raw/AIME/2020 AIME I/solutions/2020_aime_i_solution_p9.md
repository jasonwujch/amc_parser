# 2020 AIME I Problem 9

## Problem

Let $S$ be the set of positive integer divisors of $20^9.$ Three numbers are chosen independently and at random with replacement from the set $S$ and labeled $a_1,a_2,$ and $a_3$ in the order they are chosen. The probability that both $a_1$ divides $a_2$ and $a_2$ divides $a_3$ is $\tfrac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m.$

## Solution 1
[asy] size(12cm); for (int x = 1; x < 18; ++x) { draw((x, 0) -- (x, 9), dotted); } for (int y = 1; y < 9; ++y) { draw((0, y) -- (18, y), dotted); } draw((0, 0) -- (18, 0) -- (18, 9) -- (0, 9) -- cycle); pair b1, b2, b3; pair c1, c2, c3; pair a1, a2, a3; b1 = (3, 0); b2 = (12, 0); b3 = (16, 0); c1 = (0, 2); c2 = (0, 4); c3 = (0, 8); a1 = b1 + c1; a2 = b2 + c2; a3 = b3 + c3; draw(b1 -- a1 -- c1); draw(b2 -- a2 -- c2); draw(b3 -- a3 -- c3); dot(a1); dot(a2); dot(a3); label("$a_1$", a1, NE); label("$a_2$", a2, NE); label("$a_3$", a3, NE); label("$b_1$", b1, S); label("$b_2$", b2, S); label("$b_3$", b3, S); label("$c_1$", c1, W); label("$c_2$", c2, W); label("$c_3$", c3, W); [/asy]
First, prime factorize $20^9$ as $2^{18} \cdot 5^9$ . Denote $a_1$ as $2^{b_1} \cdot 5^{c_1}$ , $a_2$ as $2^{b_2} \cdot 5^{c_2}$ , and $a_3$ as $2^{b_3} \cdot 5^{c_3}$ .
In order for $a_1$ to divide $a_2$ , and for $a_2$ to divide $a_3$ , $b_1\le b_2\le b_3$ , and $c_1\le c_2\le c_3$ . We will consider each case separately. Note that the total amount of possibilities is $190^3$ , as there are $(18+1)(9+1)=190$ choices for each factor.
We notice that if we add $1$ to $b_2$ and $2$ to $b_3$ , then we can reach the stronger inequality $0\le b_1<b_2+1<b_3+2\le 20$ . Therefore, if we pick $3$ integers from $0$ to $20$ , they will correspond to a unique solution, forming a 1-1 correspondence between the numbers $b_1$ , $b_2+1$ , and $b_3+2$ . This is also equivalent to applying stars and bars on distributing the powers of 2 and 5 through differences. The amount of solutions to this inequality is $\dbinom{21}{3}$ .
The case for $c_1$ , $c_2$ , and $c_3$ proceeds similarly for a result of $\dbinom{12}{3}$ . Therefore, the probability of choosing three such factors is \[\frac{\dbinom{21}{3} \cdot \dbinom{12}{3}}{190^3}.\] Simplification gives $\frac{77}{1805}$ , and therefore the answer is $\boxed{077}$ .
-molocyxu

## Solution 2
Same as before, say the factors have powers of $b$ and $c$ . $b_1, b_2, b_3$ can either be all distinct, all equal, or two of the three are equal. As well, we must have $b_1 \leq b_2 \leq b_3$ . If they are all distinct, the number of cases is simply ${19 \choose 3}$ . If they are all equal, there are only $19$ cases for the general value. If we have a pair equal, then we have $2 \cdot {19\choose 2}$ . We need to multiply by $2$ because if we have two values $b_i < b_j$ , we can have either $(b_i, b_i, b_j)$ or $(b_i, b_j, b_j)$ .
\[{19 \choose 3} + 2 \cdot {19 \choose 2} + 19 = 1330\]
Likewise for $c$ , we get
\[{10 \choose 3} + 2 \cdot {10 \choose 2} + 10 = 220\]
The final probability is simply $\frac{1330 \cdot 220}{190^3}$ . Simplification gives $\frac{77}{1805}$ , and therefore the answer is $\boxed{077}$ .

## Solution 3
Similar to before, we calculate that there are $190^3$ ways to choose $3$ factors with replacement. Then, we figure out the number of triplets ${a,b,c}$ and ${d,f,g}$ , where $a$ , $b$ , and $c$ represent powers of $2$ and $d$ , $f$ , and $g$ represent powers of $5$ , such that the triplets are in non-descending order. The maximum power of $2$ is $18$ , and the maximum power of $5$ is $9$ . Using the Hockey Stick identity, we figure out that there are $\dbinom{12}{3}$ ways to choose $d$ , $f$ and $g$ , and $\dbinom{21}{3}$ ways to choose $a$ , $b$ , and $c$ . Therefore, the probability of choosing $3$ factors which satisfy the conditions is \[\frac{\dbinom{21}{3} \cdot \dbinom{12}{3}}{190^3}.\] This simplifies to $\frac{77}{1805}$ , therefore $m =$ $\boxed{077}$ .

## Solution 4 (Official MAA)
Note that the prime factorization of $20^9$ is $2^{18}\cdot5^{9}.$ The problem reduces to selecting independently the powers of $2$ and the powers of $5$ in the numbers $a_1$ , $a_2$ , and $a_3$ . This is equivalent to selecting $3$ exponents for the powers of $2$ and $3$ exponents for the powers of $5$ and determining in each case the probability that the 3 exponents are chosen in nondecreasing order. Given a positive integer $k$ , the probability that three integers $a$ , $b$ , and $c$ are chosen such that $0\le a \le b\le c \le k$ is the probability that $a$ , $b+1$ , and $c+2$ are chosen such that $0 \le a < b+1 < c+2 \le k+2$ . There are $\binom {k+3}3$ ways to choose $a$ , $b+1$ , and $c+2$ , so the probability that the integers are chosen in order is \[\frac{\binom{k+3}3}{(k+1)^3}.\] Thus the probability that three chosen divisors of $20^9$ satisfy the divisibility requirement is \[\frac{\binom{12}3}{10^3}\cdot\frac{\binom{21}3}{19^3}=\frac{12\cdot11\cdot10}{6\cdot10\cdot10\cdot10}\cdot\frac{21\cdot20\cdot19}{6\cdot19\cdot19\cdot19}=\frac{77}{1805}.\] The requested numerator is $77.$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .