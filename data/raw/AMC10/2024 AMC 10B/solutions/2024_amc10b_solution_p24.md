# 2024 AMC 10B Problem 24

## Problem

Let \[P(m)=\frac{m}{2}+\frac{m^2}{4}+\frac{m^4}{8}+\frac{m^8}{8}\] How many of the values $P(2022)$ , $P(2023)$ , $P(2024)$ , and $P(2025)$ are integers?

$\textbf{(A) } 0 \qquad\textbf{(B) } 1 \qquad\textbf{(C) } 2 \qquad\textbf{(D) } 3 \qquad\textbf{(E) } 4$

## Solution 1 (The simplest way)
First, we know that $P(2022)$ and $P(2024)$ must be integers since they are both divisible by $2$ .
Then let’s consider the remaining two numbers. Since they are not divisible by $2$ , the result of the first term must be a certain number $+\frac{1}{2}$ .
The divisibility rule for $4$ states that the last two digits of the number must be divisible by $4$ , and we know that the last two digits of ${2023}^2$ are the last two digits of ${23}^2$ , which is $29$ . And $29$ is $1$ greater than a multiple of $4$ . Therefore, the result of the second term must be $\frac{1}{4}$ . Similarly, the remaining two terms must each be $\frac{1}{8}$ .
Their sum is $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} = 1$ , so $P(2023)$ and $P(2025)$ are also integers.
Therefore, the answer is $\boxed{\textbf{(E) }4}$ .
~Athmyx & mayowl

## Solution 2 (Specific)
Take everything modulo 8 and re-write the entire fraction with denominator 8. This means that we're going to transform the fraction as follows : \[P(m)=\frac{m}{2}+\frac{m^2}{4}+\frac{m^4}{8}+\frac{m^8}{8}\] becomes \[P(m)=\frac{4m + 2m^2 + m^4 + m^8}{8}\] And in order for $P(m)$ to be an integer, it's important to note that $4m + 2m^2 + m^4 + m^8$ must be congruent to 0 modulo 8. Moreover, we know that $2022 \equiv 6 \pmod 8, 2023 \equiv 7 \pmod 8, 2024 \equiv 0 \pmod 8, 2025 \equiv 1 \pmod 8$ . We can verify it by taking everything modulo 8 :
If $m = 2022$ , then $4(6) + 2(4) + 0 + 0 = 24 + 8 = 32 \equiv 0 \pmod 8$ -> TRUE If $m = 2023$ , then $4(7) + 2(1) + 1 + 1 = 28 + 2 + 1 + 1 = 32 \equiv 0 \pmod 8$ -> TRUE If $m = 2024$ , then it is obvious that the entire expression is divisible by 8. Therefore, it is true. If $m = 2025$ , then $2025 \equiv 1 \pmod 8$ . Therefore, $4(1) + 2(1) + 1 + 1 = 8 \equiv 0 \pmod 8$ -> TRUE Therefore, there are $\boxed{\textbf{(E) }4}$ possible values.
Addendum for certain China test papers : Note that $2026 \equiv 2 \pmod 8$ . Therefore, taking everything modulo 8, whilst still maintaining the original expression, gives $4(2) + 2(4) + 0 + 0 = 16 \equiv 0 \pmod 8$ . This is true.
~elpianista227 ~ Major Edits by TrigoEinstein and Co.

## Solution 3 (Factoring)
We can rewrite the expression as \[\frac{1}{8}\cdot m \cdot (m^7+m^3+2m+4).\] If $m$ is even, then $m$ gives a factor of $2$ and $m^7+m^3+2m+4$ will give a factor of $4,$ so the result will be an integer. If $m$ is odd, then notice that for any $m$ we have $m^2\equiv 1 \pmod{8}.$ Then $m^7+m^3+2m+4\equiv m+m+2m+4 \equiv 4(m+1) \equiv 0 \pmod{8}.$ So any integer $m$ will result in an integer, meaning the answer is $\boxed{\textbf{(E) }4}$ .
-nevergonnagiveup
~flyingkinder123 (minor edits)

## Solution 4
Taking a closer look at the terms, we notice that each term builds off of the previous one. There is $\frac{m}{2}$ , $\frac{m^{2}}{4}$ , which is equal to $\left(\frac{m}{2}\right)^{2}$ , $\frac{m^{4}}{8}$ , which is equal to $2\left(\frac{m^{2}}{4}\right)^{2}$ , and $\frac{m^{8}}{8}$ , which is equal to $8\left(\frac{m^{4}}{8}\right)^{2}$ . Ultimately, this means that there are only two cases that we need to check for: the case in which $m$ is even and the case in which $m$ is odd.
If $m$ is even, $\frac{m}{2}$ will be an integer, which means the rest of the terms will be an integer. This means in the problem, $P(2022)$ and $P(2024)$ will yield an integer result. (For certain Chinese versions, this also proves that $P(2026)$ is an integer.)
If $m$ is odd, $\frac{m}{2}$ will result in $\frac{1}{2}$ . Building off of each term will give you $\frac{1}{4}$ , $\frac{1}{8}$ , and $\frac{1}{8}$ , and summing those up will grant $1$ , an integer. This means in the problem, $P(2023)$ and $P(2025)$ will also result in integer answers.
In general, all integer $m$ will make $P(m)$ give an integer answer, but for this question, this will get us to $\boxed{\textbf{(E) }4}$ integer values ( $\boxed{\textbf{(E) }5}$ for certain Chinese versions of the test).
~unpogged

## Solution 5 (sol 2 but fast)
Obviously $P(2022)$ and $P(2024)$ both work. $2023 \equiv -1 \pmod 8$ , and $2025 \equiv 1 \pmod 8$ . Restating the problem, we have the equation equivalent to $\frac{4m+2m^2 + m^4 + m^8}{8}$ . Plugging in $m=-1$ , we have $-4+2+1+1 \equiv 0 \pmod 8$ , so $P(2023)$ works. Plugging in $m=1$ , we have $4+2+1+1 \equiv 0 \pmod 8$ as well, so $P(2025)$ also works. Thus, the answer is $\boxed{E}$ .
~martianrunner
### Remark
On certain versions of the AMC in China, the problem was restated as follows:
Let \[P(m)=\frac{m}{2}+\frac{m^2}{4}+\frac{m^4}{8}+\frac{m^8}{8}\] How many of the values $P(2022)$ , $P(2023)$ , $P(2024)$ , $P(2025),$ and $P(2026)$ are integers? $\textbf{(A) } 1 \qquad\textbf{(B) } 2 \qquad\textbf{(C) } 3 \qquad\textbf{(D) } 4 \qquad\textbf{(E) } 5$
By identical reasoning, each term of $P$ is an integer, since $2026$ is even.
Therefore, the answer is $\boxed{\textbf{(E) }5}$ .
~IHateGeometry, countmath1

## Video Solution 1 by Pi Academy (Fast and Easy)
https://youtu.be/Xn1JLzT7mW4?si=borSg8xrYLAz7mNY

## Video Solution 2 by SpreadTheMathLove
https://youtu.be/DOm3Yc6I8sM?si=252mdbZelYqDYVbj

## Video Solution 3 by Steakmath (Simplest)
https://youtu.be/jWpCw9adStQ
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .