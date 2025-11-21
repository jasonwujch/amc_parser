# 2019 AIME II Problem 2

## Problem

Lilypads $1,2,3,\ldots$ lie in a row on a pond. A frog makes a sequence of jumps starting on pad $1$ . From any pad $k$ the frog jumps to either pad $k+1$ or pad $k+2$ chosen randomly with probability $\tfrac{1}{2}$ and independently of other jumps. The probability that the frog visits pad $7$ is $\tfrac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution (Probability States)
Let $P_n$ be the probability the frog visits pad $7$ starting from pad $n$ . Then $P_7 = 1$ , $P_6 = \frac12$ , and $P_n = \frac12(P_{n + 1} + P_{n + 2})$ for all integers $1 \leq n \leq 5$ . Working our way down, we find \[P_5 = \frac{3}{4}\] \[P_4 = \frac{5}{8}\] \[P_3 = \frac{11}{16}\] \[P_2 = \frac{21}{32}\] \[P_1 = \frac{43}{64}\] $43 + 64 = \boxed{107}$ .

## Solution 2 (Casework)
Define a one jump to be a jump from $k$ to $k + 1$ and a two jump to be a jump from $k$ to $k + 2$ .
Case 1: (6 one jumps) $\left (\frac{1}{2} \right)^6 = \frac{1}{64}$
Case 2: (4 one jumps and 1 two jumps) $\binom{5}{1} \cdot \left(\frac{1}{2}\right)^5 = \frac{5}{32}$
Case 3: (2 one jumps and 2 two jumps) $\binom{4}{2} \cdot \left(\frac{1}{2}\right)^4 = \frac{3}{8}$
Case 4: (3 two jumps) $\left(\frac{1}{2}\right)^3 = \frac{1}{8}$
Summing the probabilities gives us $\frac{43}{64}$ so the answer is $\boxed{107}$ .
- pi_is_3.14

## Solution 3
Let $P_n$ be the probability that the frog lands on lily pad $n$ . The probability that the frog never lands on pad $n$ is $\frac{1}{2}P_{n-1}$ , so $1-P_n=\frac{1}{2}P_{n-1}$ . This rearranges to $P_n=1-\frac{1}{2}P_{n-1}$ , and we know that $P_1=1$ , so we can compute $P_7$ . \begin{align*} P_1&=1\\ P_2&=1-\dfrac{1}{2} \cdot 1=\dfrac{1}{2}\\ P_3&=1-\dfrac{1}{2} \cdot \dfrac{1}{2}=\dfrac{3}{4}\\ P_4&=\dfrac{5}{8}\\ P_5&=\dfrac{11}{16}\\ P_6&=\dfrac{21}{32}\\ P_7&=\dfrac{43}{64}\\ \end{align*} We calculate $P_7$ to be $\frac{43}{64}$ , meaning that our answer is $\boxed{107}$ .

## Solution 4
For any point $n$ , let the probability that the frog lands on lily pad $n$ be $P_n$ . The frog can land at lily pad $n$ with either a double jump from lily pad $n-2$ or a single jump from lily pad $n-1$ . Since the probability when the frog is at $n-2$ to make a double jump is $\frac{1}{2}$ and same for when it's at $n-1$ , the recursion is just $P_n = \frac{P_{n-2}+P_{n-1}}{2}$ . Using the fact that $P_1 = 1$ , and $P_2 = \frac{1}{2}$ , we find that $P_7 = \frac{43}{64}$ . $43 + 64 = \boxed{107}$
-bradleyguo

## Solution 5
Let $a$ represent the number of two-step jumps (hopping over two lily pads) and $b$ represent the number of one-step jumps (hopping over one lily pad). We get the equation $2a + b = 6$ , which has 4 integer solutions: $(3,0)$ , $(2,2)$ , $(1,4)$ , and $(0,6)$ . For $(2,2)$ , there are $\frac{4!}{2!2!} = 6$ ways to permute the jumps, and for $(1,4)$ there are $\frac{5!}{1!4!} = 5$ ways. So we get:
\[\frac{1}{2^{3+0}} + 6 \cdot \frac{1}{2^{2 + 2}} + 5 \cdot \frac{1}{2^{1 +4}} + \frac{1}{2^{0 + 6}} = \frac{43}{64}\]
$43 + 64 = \boxed{107}$
~ grogg007

## Video Solution (2 Solutions)
https://youtu.be/wopflrvUN2c?t=652
~ pi_is_3.14 aka the GOAT Sohil Rathi or Lebron James!!!! go king go!
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .