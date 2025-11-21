# 2023 AIME II Problem 13

## Problem

Let $A$ be an acute angle such that $\tan A = 2 \cos A.$ Find the number of positive integers $n$ less than or equal to $1000$ such that $\sec^n A + \tan^n A$ is a positive integer whose units digit is $9.$

## Solution 1
Denote $a_n = \sec^n A + \tan^n A$ . For any $k$ , we have \begin{align*} a_n & = \sec^n A + \tan^n A \\ & = \left( \sec^{n-k} A + \tan^{n-k} A \right) \left( \sec^k A + \tan^k A \right) - \sec^{n-k} A \tan^k A - \tan^{n-k} A \sec^k A \\ & = a_{n-k} a_k - 2^k \sec^{n-k} A \cos^k A - 2^k \tan^{n-k} A \cot^k A \\ & = a_{n-k} a_k - 2^k a_{n-2k} . \end{align*}
Next, we compute the first several terms of $a_n$ .
By solving equation $\tan A = 2 \cos A$ , we get $\cos A = \frac{\sqrt{2 \sqrt{17} - 2}}{4}$ . Thus, $a_0 = 2$ , $a_1 = \sqrt{\sqrt{17} + 4}$ , $a_2 = \sqrt{17}$ , $a_3 = \sqrt{\sqrt{17} + 4} \left( \sqrt{17} - 2 \right)$ , $a_4 = 9$ .
In the rest of analysis, we set $k = 4$ . Thus, \begin{align*} a_n & = a_{n-4} a_4 - 2^4 a_{n-8} \\ & = 9 a_{n-4} - 16 a_{n-8} . \end{align*}
Thus, to get $a_n$ an integer, we have $4 | n$ . In the rest of analysis, we only consider such $n$ . Denote $n = 4 m$ and $b_m = a_{4n}$ . Thus, \begin{align*} b_m & = 9 b_{m-1} - 16 b_{m-2} \end{align*} with initial conditions $b_0 = 2$ , $b_1 = 9$ .
To get the units digit of $b_m$ to be 9, we have \begin{align*} b_m \equiv -1 & \pmod{2} \\ b_m \equiv -1 & \pmod{5} \end{align*}
Modulo 2, for $m \geq 2$ , we have \begin{align*} b_m & \equiv 9 b_{m-1} - 16 b_{m-2} \\ & \equiv b_{m-1} . \end{align*}
Because $b_1 \equiv -1 \pmod{2}$ , we always have $b_m \equiv -1 \pmod{2}$ for all $m \geq 2$ .
Modulo 5, for $m \geq 5$ , we have \begin{align*} b_m & \equiv 9 b_{m-1} - 16 b_{m-2} \\ & \equiv - b_{m-1} - b_{m-2} . \end{align*}
We have $b_0 \equiv 2 \pmod{5}$ , $b_1 \equiv -1 \pmod{5}$ , $b_2 \equiv -1 \pmod{5}$ , $b_3 \equiv 2 \pmod{5}$ , $b_4 \equiv -1 \pmod{5}$ , $b_5 \equiv -1 \pmod{5}$ , $b_6 \equiv 2 \pmod{5}$ . Therefore, the congruent values modulo 5 is cyclic with period 3. To get $b_m \equiv -1 \pmod{5}$ , we have $3 \nmid m \pmod{3}$ .
From the above analysis with modulus 2 and modulus 5, we require $3 \nmid m \pmod{3}$ .
For $n \leq 1000$ , because $n = 4m$ , we only need to count feasible $m$ with $m \leq 250$ . The number of feasible $m$ is \begin{align*} 250 - \left\lfloor \frac{250}{3} \right\rfloor & = 250 - 83 \\ & = \boxed{\textbf{(167) }} . \end{align*}
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 2 (Simple)
\[\tan A = 2 \cos A \implies \sin A = 2 \cos^2 A \implies \sin^2 A + \cos^2 A = 4 \cos^4 A + \cos^2 A = 1\] \[\implies \cos^2 A = \frac {\sqrt {17} - 1}{8}.\] \[c_n = \sec^n A + \tan^n A = \frac {1}{\cos^n A} + 2^n \cos^n A = (4\cos^2 A +1)^{\frac {n}{2}}+(4 \cos^2 A)^{\frac {n}{2}} =\] \[= \left(\frac {\sqrt {17} + 1}{2}\right)^{\frac {n}{2}}+ \left(\frac {\sqrt {17} - 1}{2}\right)^{\frac {n}{2}}.\]
It is clear, that $c_n$ is not integer if $n \ne 4k, k > 0.$
Denote $x = \frac {\sqrt {17} + 1}{2}, y = \frac {\sqrt {17} - 1}{2} \implies$ \[x \cdot y = 4, x + y = \sqrt{17}, x - y = 1 \implies x^2 + y^2 = (x - y)^2 + 2xy = 9 = c_4.\]
\[c_8 = x^4 + y^4 = (x^2 + y^2)^2 - 2x^2 y^2 = 9^2 - 2 \cdot 16 = 49.\] \[c_{4k+4} = x^{2k+2} + y^{2k+2} = (x^{2k} + y^{2k})(x^2+y^2)- (x^2 y^2)(x^{2k-2}+y^{2k-2}) = 9 c_{4k}- 16 c_{4k – 4} \implies\] \[c_{12} = 9 c_8 - 16 c_4 = 9 \cdot 49 - 16 \cdot 9 = 9 \cdot 33 = 297.\] \[c_{16} = 9 c_{12} - 16 c_8 = 9 \cdot 297 - 16 \cdot 49 = 1889.\] \[c_{12m + 4} \pmod{10} = 9 \cdot c_{12m} \pmod{10} - 16 \pmod{10} \cdot c_{12m - 4} \pmod{10} =\] \[= (9 \cdot 7 - 6 \cdot 9) \pmod{10} = (3 - 4) \pmod{10} = 9.\] \[c_{12m + 8}\pmod{10} = 9 \cdot c_{12m+4} \pmod{10} - 16 \pmod{10} \cdot c_{12m } \pmod{10} =\] \[= (9 \cdot 9 - 6 \cdot 7) \pmod{10} = (1 - 2)\pmod{10} = 9.\] \[c_{12m + 12} \pmod{10} = 9 \cdot c_{12m + 8} \pmod{10} - 16 \pmod{10} \cdot c_{12m + 4} \pmod{10} =\] \[= (9 \cdot 9 - 6 \cdot 9) \pmod{10} = (1 - 4) \pmod{10} = 7 \implies\]
The condition is satisfied iff $n = 12 k + 4$ or $n = 12k + 8.$
If $n \le N$ then the number of possible n is $\left\lfloor \frac{N}{4} \right\rfloor - \left\lfloor \frac{N}{12} \right\rfloor.$
For $N = 1000$ we get $\left\lfloor \frac{1000}{4} \right\rfloor - \left\lfloor \frac{1000}{12} \right\rfloor = 250 - 83 = \boxed{167}.$
vladimir.shelomovskii@gmail.com, vvsss
### Note
A key idea in this solution is realizing that to calculate values of $a^n+b^n$ is difficult directly, so we try to think about it recursively.
We then see how we can go from $a^n+b^n$ to $a^{n+1}+b^{n+1}$ , and learn that $(a^n+b^n)(a+b)-a^nb-ab^n=a^{n+1}b^{n+1}$ .
So, letting $a^i+b^i=s_i$ , $s_i=(a+b)s_{i-1}-(ab)s_{i-2}$ where we set $n+1$ as $i$ , and $(a^n+b^n)=s_{i-1}$ , as well as $(a^nb+ab^n)=(ab)(a^{n-1}+b^{n-1})=(ab)s_{i-2}$ .
~Bigbrain_2009

## Video Solution
https://youtu.be/5Dpdi8IiUiw
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .