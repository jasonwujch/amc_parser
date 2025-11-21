# 2023 AMC 10B Problem 6

## Problem

Let $L_{1}=1, L_{2}=3$ , and $L_{n+2}=L_{n+1}+L_{n}$ for $n\geq 1$ . How many terms in the sequence $L_{1}, L_{2}, L_{3},...,L_{2023}$ are even?

$\textbf{(A) }673\qquad\textbf{(B) }1011\qquad\textbf{(C) }675\qquad\textbf{(D) }1010\qquad\textbf{(E) }674$

## Solution 1
We calculate more terms: \[1,3,4,7,11,18,\ldots.\] We find a pattern: if $n+2$ is a multiple of $3$ , then the term is even, or else it is odd. There are $\left\lfloor \frac{2023}{3} \right\rfloor =\boxed{\textbf{(E) }674}$ multiples of $3$ from $1$ to $2023$ .
~Mintylemon66 ~minor edit by the_eaglercraft_grinder

## Solution 2
Like in the other solution, we find a pattern, except in a more rigorous way. Since we start with $1$ and $3$ , the next term is $4$ .
We start with odd, then odd, then (the sum of odd and odd) even, (the sum of odd and even) odd, and so on. Basically the pattern goes: odd, odd, even, odd odd, even, odd, odd even…
When we take $\frac{2023}{3}$ we get $674$ with a remainder of one. So we have $674$ full cycles, and an extra odd at the end.
Therefore, there are $\boxed{\textbf{(E) }674}$ evens.
~e_is_2.71828

## Solution 3
We know that \( L_1 = 1 \) and \( L_2 = 3 \).
To find \( L_3 \), we put \( n=1 \) into \( L_{n+1} = L_n + L_{n-1} \).
This gives \( L_3 = 4 \). Continuing for \( L_4 \), \( L_5 \), and \( L_6 \), we get
\( L_4 = 7 \)
\( L_5 = 11 \)
\( L_6 = 18 \).
We can now make an educated guess that this pattern will always remain the same, and evens will always appear on the \( L_{3n} \)th number. (Proof is below).
So, we take the \( \lfloor 2023/3 \rfloor \), which gives $\boxed{E. 674}$
Note that \( \lfloor x \rfloor \) = to the nearest rounded down whole number.
~Pinotation
### Proof that all \( L_{3n} \) is even
We have that \( L_1 \) is an odd number and \( L_2 \) is also an odd number. The sum of two odd numbers is even. Now \( L_3 = L_2 + L_1 \), so \( L_3 \) must be even. We continue with proof by contradiction. Say \( L_{3n} \), \( n \not\le 1 \) was not even. We take \( L_6 \), for instance, and this should be odd. This means that because \( L_6 = L_5 + L_4 \), either \( L_5 \) or \( L_4 \) must be even, or else the number will be odd.
So given that \( L_3 \) is even, then \( L_4 = L_3 + L_2 \), which is an even + odd, which is odd. So now \( L_5 \) must be even for this to not work.
We know that \( L_4 \) is odd, and \( L_3 \) is even.
We have \( L_5 = L_4 + L_3 \), and that is again an odd + even case, showing that \( L_5 \) is also odd. Therefore, if \( L_{3n} \), \( n \not\le 1 \) is not even, there lies a contradiction.
Therefore, each \( L_{3n} \) number is even, and that is why we do \( \lfloor 2023/3 \rfloor \) to get $\boxed{E. 674}$
~Proof By Pinotation

## Video Solutions

## Video Solution
https://youtu.be/EuLkw8HFdk4?si=iNQdS6bI38MUha1I&t=1174
~Math-X
https://www.youtube.com/watch?v=cT-0V4a3FYY ~SpreadTheMathLove
https://www.youtube.com/watch?v=wdNGZpTrjxY ~e_is_2.71828

## Video Solution
https://youtu.be/DmE9mmTx3Fw
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by Interstigation
https://youtu.be/gDnmvcOzxjg?si=cYB6uChy7Ue0UT4L
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .