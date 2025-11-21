# 2013 AMC 8 Problem 10

## Problem

What is the ratio of the least common multiple of 180 and 594 to the greatest common factor of 180 and 594?

$\textbf{(A)}\ 110 \qquad \textbf{(B)}\ 165 \qquad \textbf{(C)}\ 330 \qquad \textbf{(D)}\ 625 \qquad \textbf{(E)}\ 660$

## Solution 1
To find either the LCM or the GCF of two numbers, always prime factorize first.
The prime factorization of $180 = 3^2 \times 5 \times 2^2$ .
The prime factorization of $594 = 3^3 \times 11 \times 2$ .
Then, to find the LCM, we have to find the greatest power of all the numbers there are; if one number is one but not the other, use it (this is $3^3, 5, 11, 2^2$ ). Multiply all of these to get 5940.
For the GCF of 180 and 594, use the least power of all of the numbers that are in both factorizations and multiply. $3^2 \times 2$ = 18.
Thus the answer = $\frac{5940}{18}$ = $\boxed{\textbf{(C)}\ 330}$ .

## Solution 2
We start off with a similar approach as the original solution. From the prime factorizations, the GCF is $18$ .
It is a well known fact that $\gcd(m,n)\times \operatorname{lcm}(m,n)=|mn|$ . So we have, $18\times \operatorname{lcm} (180,594)=594\times 180$ .
Dividing by $18$ yields $\operatorname{lcm} (180,594)=594\times 10=5940$ .
Therefore, $\frac{\operatorname{lcm} (180,594)}{\operatorname{gcf}(180,594)}=\frac{5940}{18}=\boxed{\textbf{(C)}\ 330}$ .

## Solution 3
From Solution 1, the prime factorization of $180 = 2^2 \cdot 3^2 \cdot 5$ . The prime factorization of $594 = 2 \cdot 3^3 \cdot 11$ . Hence, $\operatorname{lcm} (180,594) = 2^2 \cdot 3^3 \cdot 5 \cdot 11$ , and $\operatorname{gcf} (180,594) = 2 \cdot 3^2$ . Therefore, $\frac{\operatorname{lcm} (180,594)}{\operatorname{gcf} (180,594)} = \frac{2^2 \cdot 3^3 \cdot 5 \cdot 11}{2 \cdot 3^2} = 2 \cdot 3 \cdot 5 \cdot 11 = 330 \Longrightarrow \boxed{\textbf{(C)}\ 330}$

## Video Solution by OmegaLearn
https://youtu.be/CWZkTCNu42o?t=31
~ pi_is_3.14

## Video Solution
https://youtu.be/ZtjQTa2hWmw ~savannahsolver
### See Also