# 2010 AIME I Problem 1

## Problem

Maya lists all the positive divisors of $2010^2$ . She then randomly selects two distinct divisors from this list. Let $p$ be the probability that exactly one of the selected divisors is a perfect square . The probability $p$ can be expressed in the form $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
$2010^2 = 2^2\cdot3^2\cdot5^2\cdot67^2$ . Thus there are $(2+1)^4$ divisors, $(1+1)^4$ of which are squares (the exponent of each prime factor must either be $0$ or $2$ ). Therefore the probability is \[\frac {2\cdot2^4\cdot(3^4 - 2^4)}{3^4(3^4 - 1)} = \frac {26}{81} \Longrightarrow 26+ 81 = \boxed{107}.\]

## Solution 2 (Using a Bit More Counting)
The prime factorization of $2010^2$ is $67^2\cdot3^2\cdot2^2\cdot5^2$ . Therefore, the number of divisors of $2010^2$ is $3^4$ or $81$ , $16$ of which are perfect squares. The number of ways we can choose $1$ perfect square from the two distinct divisors is $\binom{16}{1}\binom{81-16}{1}$ . The total number of ways to pick two divisors is $\binom{81}{2}$
Thus, the probability is \[\frac {\binom{16}{1}\binom{81-16}{1}}{\binom{81}{2}} = \frac {16\cdot65}{81\cdot40} = \frac {26}{81} \Longrightarrow 26+ 81 = \boxed{107}.\]

## Video Solution
https://www.youtube.com/watch?v=YJeF9dLJZuw (Osman Nal)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .