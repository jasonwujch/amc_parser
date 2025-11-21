# 2017 AMC 10B Problem 20

## Problem

The number $21!=51,090,942,171,709,440,000$ has over $60,000$ positive integer divisors. One of them is chosen at random. What is the probability that it is odd?

$\textbf{(A)}\ \frac{1}{21}\qquad\textbf{(B)}\ \frac{1}{19}\qquad\textbf{(C)}\ \frac{1}{18}\qquad\textbf{(D)}\ \frac{1}{2}\qquad\textbf{(E)}\ \frac{11}{21}$

## Solution 1
We note that the only thing that affects the parity of the factor are the powers of 2. There are $10+5+2+1 = 18$ factors of 2 in the number. Thus, there are $18$ cases in which a factor of $21!$ would be even (have a factor of $2$ in its prime factorization), and $1$ case in which a factor of $21!$ would be odd. Therefore, the answer is $\boxed{\textbf{(B)} \frac 1{19}}$ .
Note from Williamgolly: To see why symmetry occurs here, we group the factors of 21! into 2 groups, one with powers of 2 and the others odd factors. For each power of 2, the factors combine a certain number of 2's from the first group and numbers from the odd group. That is why symmetry occurs here.

## Solution 2 (Legendre's and Substitution)
Use Legendre's formula to derive the prime factorization of $21!$ .
How can this be done? The greatest prime factor before $21$ is $19$ , so use Legendre's formula for all prime numbers up until $19$ inclusive of $19$ . Then, if you do the steps correctly, your prime factorization should be \[2^{18} \times 3^9 \times 5^4 \times 7^3 \times 11 \times 13 \times 17 \times 19\]
We want \(\frac{P(\text{odd})}{P(\text{All})}\). To get \(P(\text{odd})\), we want all the factors of \[3^9 \times 5^4 \times 7^3 \times 11 \times 13 \times 17 \times 19\]
Why not $2^{18}$ ? Well, anything multiplied by 2 is going to be even, which we don't want.
Using the number of factors formula, the number of factors that divide $3^9 \times 5^4 \times 7^3 \times 11 \times 13 \times 17 \times 19$ including 1 and $3^9 \times 5^4 \times 7^3 \times 11 \times 13 \times 17 \times 19$ is $(9+1)(4+1)(3+1)(2^4)$ .
For simplicity, denote this product as \(\aleph\). Then, $\aleph$ is the number of odd factors in $21!$ .
We now want \(P(\text{all})\). This is just the number of factors in $2^{18} \times 3^9 \times 5^4 \times 7^3 \times 11 \times 13 \times 17 \times 19$ (While they do say this is $60,000$ in the problem, for the sake of substitution reasons let's ignore this fact). Then, the number of factors is \((18+1)(9+1)(4+1)(3+1)(2^4)\). We substitute $\aleph$ and see that $P(\text{all}) = 19\aleph$
The probability that we pick an odd divisor of $21!$ is $\frac{P(\text{odd})}{P(\text{All})}$ , or $\frac{P(\text{odd})}{P(\text{All})}$ , or $\boxed{\textbf{(B)} ~\frac{1}{19}}$ .
~Pinotation

## Solution 3 (Constructive Counting)
Consider how to construct any divisor $D$ of $21!$ . First by Legendre's theorem for the divisors of a factorial (see here: Legendre's Formula ), we have that there are a total of 18 factors of 2 in the number. $D$ can take up either 0, 1, 2, 3,..., or all 18 factors of 2, for a total of 19 possible cases. In order for $D$ to be odd, however, it must have 0 factors of 2, meaning that there is a probability of 1 case/19 cases = $\boxed{\textbf{(B)} \frac 1{19}}$

## Solution 4
We can find the prime factorization of $21!$ . We do this by finding the prime factorization of each of 21, 20, ..., 2, and 1 and multiplying them together. This gives us $2^{18} \cdot 3^{9} \cdot 5^{4} \cdot 7^{3} \cdot 11 \cdot 13 \cdot 17 \cdot 19$ . To find the number of odd divisors, we pretend as if the $2^{18}$ doesn't exist and count the other divisors: $10 \cdot 5 \cdot 4 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ . The total number of divisors are $19 \cdot 10 \cdot 5 \cdot 4 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ . Dividing gives $\boxed{\textbf{(B)} ~\frac{1}{19}}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .