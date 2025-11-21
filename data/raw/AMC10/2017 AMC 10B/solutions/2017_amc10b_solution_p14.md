# 2017 AMC 10B Problem 14

## Problem

An integer $N$ is selected at random in the range $1\leq N \leq 2020$ . What is the probability that the remainder when $N^{16}$ is divided by $5$ is $1$ ?

$\textbf{(A)}\ \frac{1}{5}\qquad\textbf{(B)}\ \frac{2}{5}\qquad\textbf{(C)}\ \frac{3}{5}\qquad\textbf{(D)}\ \frac{4}{5}\qquad\textbf{(E)}\ 1$

## Solution 1
Notice that we can rewrite $N^{16}$ as $(N^{4})^4$ . By Fermat's Little Theorem , we know that $N^{(5-1)} \equiv 1 \pmod {5}$ if $N \not \equiv 0 \pmod {5}$ . Therefore for all $N \not \equiv 0 \pmod {5}$ we have $N^{16} \equiv (N^{4})^4 \equiv 1^4 \equiv 1 \pmod 5$ . Since $1\leq N \leq 2020$ , and $2020$ is divisible by $5$ , $\frac{1}{5}$ of the possible $N$ are divisible by $5$ . Therefore, $N^{16} \equiv 1 \pmod {5}$ with probability $1-\frac{1}{5},$ or $\boxed{\textbf{(D) } \frac 45}$ .

## Solution 2
Note that the patterns for the units digits repeat, so in a sense we only need to find the patterns for the digits $0-9$ . The pattern for $0$ is $0$ , no matter what power, so $0$ doesn't work. Likewise, the pattern for $5$ is always $5$ . Doing the same for the rest of the digits, we find that the units digits of $1^{16}$ , $2^{16}$ , $3^{16}$ , $4^{16}$ , $6^{16}$ , $7^{16}$ , $8^{16}$ and $9^{16}$ all have the remainder of $1$ when divided by $5$ , so $\boxed{\textbf{(D) } \frac 45}$ .
Explanation: Since the remainder is 1, the units digit is either 1 or 6. Since we only care about the units digits, we don't need to think about anything beyond units digits. We count in modulus ten (fancy word of saying ignore everything except the units digit) For 1: 1, 1, 1, 1... anything with a units digit one will always have powers that have a units digit one. For 2: 2, 4, 8, 6, 2, 4, 8, 6... we see that it repeats with a cycle of 4. Since we are looking for the 16th power, the units digit will be 6, and this works. For 3: 3, 9, 7, 1, 3, 9, 7, 1... similarly to 2, a cycle of 4 and the 16th power has a units digit of 1. This works. For 4: 4, 6, 4, 6... a cycle of 4, 16th power has a units digit of 6. This works. For 5: 5, 5, 5, 5... the units digit will always be 5, and this doesn't work. For 6: 6, 6, 6, 6... the units digit will always be 6, and this works. For 7: 7, 9, 3, 1, 7, 9, 3, 1... a cycle of 4, 16th power has a units digit of 1. This works. For 8: 8, 4, 2, 6, 8, 4, 2, 6... a cycle of 4, 16th power has a units digit of 6. This works. For 9: 9, 1, 9, 1... a cycle of 2, 16th power has a units digit of 1. This works. Last but not least, 0: 0, 0, 0... the units digit will always be 0, and this does not work. To sum up: There are ten choices for the units digit. Of these ten choices, 1, 2, 3, 4, 6, 7, 8, 9 all work, and the probability is therefore $\frac{8}{10}=\frac{4}{5}$ which is answer choice $\boxed{\textbf{(D)}\ \frac{4}{5}}$ . ~Explanation by JH. L

## Solution 3 (Casework)
We can use modular arithmetic for each residue of $n \pmod 5$
If $n \equiv 0 \pmod 5$ , then $n^{16} \equiv 0^{16} \equiv 0 \pmod 5$
If $n \equiv 1 \pmod 5$ , then $n^{16} \equiv 1^{16} \equiv 1 \pmod 5$
If $n \equiv 2 \pmod 5$ , then $n^{16} \equiv (n^2)^8 \equiv (2^2)^8 \equiv 4^8 \equiv (-1)^8 \equiv 1 \pmod 5$
If $n \equiv 3 \pmod 5$ , then $n^{16} \equiv (n^2)^8 \equiv (3^2)^8 \equiv 9^8 \equiv (-1)^8 \equiv 1 \pmod 5$
If $n \equiv 4 \pmod 5$ , then $n^{16} \equiv 4^{16} \equiv (-1)^{16} \equiv 1 \pmod 5$
In $4$ out of the $5$ cases, the result was $1 \pmod 5$ , and since each case occurs equally as $2020 \equiv 0 \pmod 5$ , the answer is $\boxed{\textbf{(D) }\frac{4}{5}}$

## Solution 4 (Good for use in actual contest)
Another phrasing for this question is: An integer $N$ is selected at random in the range $1\leq N \leq 2020$ . What is the probability that $N^{16}$ has a units digit of $1$ or $6$ ? The reason I say this is to make it simpler because now we can just test which numbers to the sixteenth power have units digit $1$ or $6$ . Now we test: \[1^{16} \equiv 1 \pmod 5\] , \[2^{16} \equiv 1 \pmod 5\] , \[3^{16} \equiv 1 \pmod 5\] , \[4^{16} \equiv 1 \pmod 5\] , \[6^{16} \equiv 1 \pmod 5\] , \[7^{16} \equiv 1 \pmod 5\] , \[8^{16} \equiv 1 \pmod 5\] , \[9^{16} \equiv 1 \pmod 5\] . We have $\dfrac{8}{10}$ digits work so simplifying gives us $\boxed{\textbf{(D) }\frac{4}{5}}$ -jb2015007

## Video Solution 1 by OmegaLearn
https://youtu.be/zfChnbMGLVQ?t=2410
~ pi_is_3.14

## Video Solution 2
https://youtu.be/Oj3Z1JhvoiE
~savannahsolver

## Video Solution 3
https://www.youtube.com/watch?v=PY_WugVa4cg
~Math4All999
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .