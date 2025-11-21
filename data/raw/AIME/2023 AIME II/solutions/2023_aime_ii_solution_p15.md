# 2023 AIME II Problem 15

## Problem

For each positive integer $n$ let $a_n$ be the least positive integer multiple of $23$ such that $a_n \equiv 1 \pmod{2^n}.$ Find the number of positive integers $n$ less than or equal to $1000$ that satisfy $a_n = a_{n+1}.$

## Solution 1
Denote $a_n = 23 b_n$ . Thus, for each $n$ , we need to find smallest positive integer $k_n$ , such that \[ 23 b_n = 2^n k_n + 1 . \]
Thus, we need to find smallest $k_n$ , such that \[ 2^n k_n \equiv - 1 \pmod{23} . \]
Now, we find the smallest $m$ , such that $2^m \equiv 1 \pmod{23}$ . By Fermat's Theorem, we must have $m | \phi \left( 23 \right)$ . That is, $m | 22$ . We find $m = 11$ .
Therefore, for each $n$ , we need to find smallest $k_n$ , such that \[ 2^{{\rm Rem} \left( n , 11 \right)} k_n \equiv - 1 \pmod{23} . \]
We have the following results:
If \({\rm Rem} \left( n , 11 \right) = 0\), then \(k_n = 22\) and \(b_n = 1\).
If \({\rm Rem} \left( n , 11 \right) = 1\), then \(k_n = 11\) and \(b_n = 1\).
If \({\rm Rem} \left( n , 11 \right) = 2\), then \(k_n = 17\) and \(b_n = 3\).
If \({\rm Rem} \left( n , 11 \right) = 3\), then \(k_n = 20\) and \(b_n = 7\).
If \({\rm Rem} \left( n , 11 \right) = 4\), then \(k_n = 10\) and \(b_n = 7\).
If \({\rm Rem} \left( n , 11 \right) = 5\), then \(k_n = 5\) and \(b_n = 7\).
If \({\rm Rem} \left( n , 11 \right) = 6\), then \(k_n = 14\) and \(b_n = 39\).
If \({\rm Rem} \left( n , 11 \right) = 7\), then \(k_n = 7\) and \(b_n = 39\).
If \({\rm Rem} \left( n , 11 \right) = 8\), then \(k_n = 15\) and \(b_n = 167\).
If \({\rm Rem} \left( n , 11 \right) = 9\), then \(k_n = 19\) and \(b_n = 423\).
If \({\rm Rem} \left( n , 11 \right) = 10\), then \(k_n = 21\) and \(b_n = 935\).
Therefore, in each cycle, $n \in \left\{ 11 l , 11l + 1 , \cdots , 11l + 10 \right\}$ , we have $n = 11l$ , $11l + 3$ , $11l + 4$ , $11l + 6$ , such that $b_n = b_{n+1}$ . That is, $a_n = a_{n+1}$ . At the boundary of two consecutive cycles, $b_{11L + 10} \neq b_{11 \left(l + 1 \right)}$ .
We have $1000 = 90 \cdot 11 + 10$ . Therefore, the number of feasible $n$ is $91 \cdot 4 - 1 = \boxed{\textbf{(363) }}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 2
Observe that if $a_{n-1} - 1$ is divisible by $2^n$ , $a_n = a_{n-1}$ . If not, $a_n = a_{n-1} + 23 \cdot 2^{n-1}$ .
This encourages us to let $b_n = \frac{a_n - 1}{2^n}$ . Rewriting the above equations, we have \[b_n = \begin{cases} \frac{b_{n-1}}{2} & \text{if } 2 \text{ } \vert \text{ } b_{n-1} \\ \frac{b_{n-1}+23}{2} &\text{if } 2 \not\vert \text{ } b_{n-1} \end{cases}\] The first few values of $b_n$ are $11, 17, 20, 10, 5, 14, 7, 15, 19, 21,$ and $22$ . We notice that $b_{12} = b_1 = 11$ , and thus the sequence is periodic with period $11$ .
Note that $a_n = a_{n+1}$ if and only if $b_n$ is even. This occurs when $n$ is congruent to $0, 3, 4$ or $6$ mod $11$ , giving four solutions for each period.
From $1$ to $1001$ (which is $91 \times 11$ ), there are $91 \times 4 = 364$ values of $n$ . We subtract $1$ from the total since $1001$ satisfies the criteria but is greater than $1000$ to get a final answer of $\fbox{363}$ . ~ Bxiao31415
(small changes by bobjoebilly and IraeVid13 )

## Solution 3 (Similar to solution 2 but more explanation)
Let $a_n = 23b_n$ . Note that if \[23 b_{n+1} \equiv 1 \pmod{2^{n+1}}\] Then \[23 b_{n+1} \equiv 1 \pmod{2^{n}}\] Also \[23 b_n \equiv 1 \pmod{2^n}\] Therefore \[b_n \equiv b_{n+1} \equiv 23^{-1} \pmod{2^n}\] Then \[b_{n+1} \equiv b_n, b_n + 2^n \pmod{2^{n+1}}\] So \[b_{n+1} = b_n, b_n + 2^n\] Since $0 \le b_n < 2^n$ and $0 \le b_{n+1} < 2^{n+1}$ as $a_n$ is the least positive integer multiple of 23.
Now suppose $b_{n+1} = b_n$ . Define $q_n$ to be the quotient of $23b_n$ divided by $2^n$ . Then \[23b_n = 2^n q_n + 1 \text{ and } 23b_{n+1} = 23b_n = 2^{n+1} q_{n+1} + 1 = 2^n q_n + 1 \implies q_{n+1} = \frac{q_n}{2}\] Furthermore if quotient $q_n$ is even then \[23b_n = 2^n q_n +1 = 2^{n+1} \frac{q_n}{2} +1\] Therefore $b_{n+1} = b_n$ if and only if $q_n$ is even. And, if this is true, then $q_{n+1} = \frac{q_n}{2}$ . Next, if $q_n$ is odd, we must have $b_{n+1} = b_n + 2^n$ . Solving for $q_{n+1}$ , we have \[23b_{n+1} = 2^{n+1} q_{n+1} + 1 \implies 23b_n + 23 \cdot 2^n = 2^{n+1} q_{n+1} + 1 \implies 2^n q_n + 1 + 23 = 2^{n+1} q_{n+1} + 1 \implies q_{n+1} = \frac{q_n + 1}{2} + 11\] Therefore, if $q_n$ is odd, $q_{n+1} = \frac{q_n + 1}{2} + 11$ . In sum, our recursion is \[q_n = \begin{cases} \frac{q_{n-1}}{2} & \text{if } 2 \text{ } \vert \text{ } q_{n-1} \\ \frac{q_{n-1}+1}{2} + 11 &\text{if } 2 \not\vert \text{ } q_{n-1} \end{cases}\] Finally, let us list out $q_n$ to find a pattern. Because $a_1 = 23$ , $q_1 = 11$ . Through our recursion, we continue like so: \[q_1 = 11, q_2 = 17, q_2 = 20, q_3 = 10, q_4 = 5, q_6 = 14, q_7 = 7, q_8 = 15, q_9 = 19, q_{10} = 21, q_{11} = 22, q_{12} = 11, \dots\] Therefore $q_n$ repeats with cycle length $11$ . Since $a_{n+1} = a_n$ if and only if $q_n$ is even, in each cycle, we have 4 satisfactory values of $n$ . There are $\frac{1000 - 10}{11} = 90$ complete cycles. There are 3 extra values in the last incomplete cycle. Therefore we obtain $90 \cdot 4 + 3 = \fbox{363}$ .
~ CrazyVideoGamez

## Solution 4 (Binary Interpretation, Computer Scientists' Playground)
We first check that $\gcd(23, 2^n) = 1$ hence we are always seeking a unique modular inverse of $23$ , $b_n$ , such that $a_n \equiv 23b_n \equiv 1 \mod{2^n}$ .
Now that we know that $b_n$ is unique, we proceed to recast this problem in binary. This is convenient because $x \mod{2^n}$ is simply the last $n$ -bits of $x$ in binary, and if $x \equiv 1 \mod{2^n}$ , it means that of the last $n$ bits of $x$ , only the rightmost bit (henceforth $0$ th bit) is $1$ .
Also, multiplication in binary can be thought of as adding shifted copies of the multiplicand. For example:
\begin{align} 10111_2 \times 1011_2 &= 10111_2 \times (1000_2 + 10_2 + 1_2) \\ &= 10111000_2 + 101110_2 + 10111_2 \\ &= 11111101_2 \end{align}
Now note $23 = 10111_2$ , and recall that our objective is to progressively zero out the $n$ leftmost bits of $a_n = 10111_2 \times b_n$ except for the $0$ th bit.
Write $b_n = \underline{c_{n-1}\cdots c_2c_1c_0}_2$ , we note that $c_0$ uniquely defines the $0$ th bit of $a_n$ , and once we determine $c_0$ , $c_1$ uniquely determines the $1$ st bit of $a_n$ , so on and so forth.
For example, $c_0 = 1$ satisfies $a_1 \equiv10111_2 \times 1_2 \equiv 1 \mod{10_2}$ Next, we note that the second bit of $a_1$ is $1$ , so we must also have $c_1 = 1$ in order to zero it out, giving
\[a_2 \equiv 10111_2 \times 11_2 \equiv 101110_2 + a_1 \equiv 1000101_2 \equiv 01_2 \mod{100_2}\]
$a_{n+1} = a_{n}$ happens precisely when $c_n = 0$ . In fact we can see this in action by working out $a_3$ . Note that $a_2$ has 1 on the $2$ nd bit, so we must choose $c_2 = 1$ . This gives
\[a_3 \equiv 10111_2 \times 111_2 \equiv 1011100_2 + a_2 \equiv 10100001_2 \equiv 001_2 \mod{1000_2}\]
Note that since the $3$ rd and $4$ th bit are $0$ , $c_3 = c_4 = 0$ , and this gives $a_3 = a_4 = a_5$ .
It may seem that this process will take forever, but note that $23 = 10111_2$ has $4$ bits behind the leading digit, and in the worst case, the leading digits of $a_n$ will have a cycle length of at most $16$ . In fact, we find that the cycle length is $11$ , and in the process found that $a_3 = a_4 = a_5$ , $a_6 = a_7$ , and $a_{11} = a_{12}$ .
Since we have $90$ complete cycles of length $11$ , and the last partial cycle yields $a_{993} = a_{994} = a_{995}$ and $a_{996} = a_{997}$ , we have a total of $90 \times 4 + 3 = \boxed{363}$ values of $n \le 1000$ such that $a_n = a_{n+1}$
~ cocoa @ https://www.corgillogical.com

## Video Solution
https://youtu.be/ujP-V170vvI
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .