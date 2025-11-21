# 2021 Fall AMC 10B Problem 19

## Problem

Let $N$ be the positive integer $7777\ldots777$ , a $313$ -digit number where each digit is a $7$ . Let $f(r)$ be the leading digit of the $r{ }$ th root of $N$ . What is \[f(2) + f(3) + f(4) + f(5)+ f(6)?\] $(\textbf{A})\: 8\qquad(\textbf{B}) \: 9\qquad(\textbf{C}) \: 11\qquad(\textbf{D}) \: 22\qquad(\textbf{E}) \: 29$

## Solution 1
We can rewrite $N$ as $\frac{7}{9}\cdot 9999\ldots999 = \frac{7}{9}\cdot(10^{313}-1)$ . When approximating values, as we will shortly do, the minus one will become negligible so we can ignore it. When we take the power of ten out of the square root, we’ll be multiplying by another power of ten, so the leading digit will not change. Thus the leading digit of $f(r)$ will be equal to the leading digit of $\sqrt[r]{\frac{7}{9} \cdot 10^{313(\mod r)}}$ .
Then $f(2)$ is the first digit of $\sqrt{\frac{7}{9}\cdot(10)} = \sqrt{\frac{70}{9}} = \sqrt{7. \ldots} \approx 2$
$f(3) = \sqrt[3]{\frac{7}{9} \cdot 10} = \sqrt[3]{\frac{70}{9}} = \sqrt[3]{7.\ldots} \approx 1$ .
$f(4) = \sqrt[4]{\frac{7}{9} \cdot 10} = \sqrt[4]{\frac{70}{9}} = \sqrt[4]{7.\ldots} \approx 1$ .
$f(5) = \sqrt[5]{\frac{7}{9} \cdot 1000} = \sqrt[5]{\frac{7000}{9}} = \sqrt[5]{777.\ldots} \approx 3$ .
$f(6) = \sqrt[6]{\frac{7}{9} \cdot 10} = \sqrt[6]{\frac{70}{9}} = \sqrt[6]{7.\ldots} \approx 1$ .
The final answer is therefore $2+1+1+3+1 = \boxed{\textbf{(A) }8}$ .
Note: in all of the divisions, we omitted the decimal places, because they are irrelevant to finding the leading digit.
~KingRavi, mathboy282, trevian1

## Solution 2
For notation purposes, let $x$ be the number $777 \ldots 777$ with $313$ digits, and let $B(n)$ be the leading digit of $n$ . As an example, $B(x) = 7$ , because $x = 777 \ldots 777$ , and the first digit of that is $7$ .
Notice that \[B(\sqrt{\frac{n}{100}}) = B(\sqrt{n})\] ​for all numbers $n \geq 100$ ; this is because $\sqrt{\frac{n}{100}} = \frac{\sqrt{n}}{10}$ , and dividing by $10$ does not affect the leading digit of a number. Similarly, \[B(\sqrt[3]{\frac{n}{1000}}) = B(\sqrt[3]{n}).\] In general, for positive integers $k$ and real numbers $n > 10^{k}$ , it is true that \[B(\sqrt[k]{\frac{n}{10^{k}}}) = B(\sqrt[k]{n}).\] Behind all this complex notation, all that we're really saying is that the first digit of something like $\sqrt[3]{123456789}$ has the same first digit as $\sqrt[3]{123456.789}$ and $\sqrt[3]{123.456789}$ .
The problem asks for \[B(\sqrt[2]{x}) + B(\sqrt[3]{x}) + B(\sqrt[4]{x}) + B(\sqrt[5]{x}) + B(\sqrt[6]{x}).\]
From our previous observation, we know that \[B(\sqrt[2]{x}) = B(\sqrt[2]{\frac{x}{100}} = B(\sqrt[2]{\frac{x}{10,000}} = B(\sqrt[2]{\frac{x}{1,000,000}} = \ldots .\] Therefore, $B(\sqrt[2]{x}) = B(\sqrt[2]{7.777 \dots})$ . We can evaluate $B(\sqrt[2]{7.777 \dots})$ , the leading digit of $\sqrt[2]{7.777 \dots}$ , to be $2$ . Therefore, $f(2) = 2$ .
Similarly, we have \[B(\sqrt[3]{x}) = B(\sqrt[3]{\frac{x}{1,000}} = B(\sqrt[3]{\frac{x}{1,000,000}} = B(\sqrt[3]{\frac{x}{1,000,000,000}} = \ldots .\] Therefore, $B(\sqrt[3]{x}) = B(\sqrt[3]{7.777 \ldots})$ . We know $B(\sqrt[3]{7.777 \ldots}) = 1$ , so $f(3) = 1$ .
Next, \[B(\sqrt[4]{x}) = B(\sqrt[4]{7.777 \ldots})\] and $B(\sqrt[4]{7.777 \ldots}) = 1$ , so $f(4) = 1$ .
We also have \[B(\sqrt[5]{x}) = B(\sqrt[5]{777.777 \ldots})\] and $B(\sqrt[5]{777.777 \ldots}) = 3$ , so $f(5) = 3$ .
Finally, \[B(\sqrt[6]{x}) = B(\sqrt[6]{7.777 \ldots})\] and $B(\sqrt[4]{7.777 \ldots}) = 1$ , so $f(6) = 1$ .
We have that $f(2)+f(3)+f(4)+f(5)+f(6) = 2+1+1+3+1 = \boxed{\textbf{(A) } 8}$ .
~ihatemath123

## Solution 3 (Condensed Solution 1)
Since $7777..7$ is a $313$ digit number and $\sqrt {7}$ is around $2.5$ , we have $f(2)$ is $2$ . $f(3)$ is the same story, so $f(3)$ is $1$ . It is the same as $f(4)$ as well, so $f(4)$ is also $1$ . However, $313$ is $3$ mod $5$ , so we need to take the 5th root of $777$ , which is between $3$ and $4$ , and therefore, $f(5)$ is $3$ . $f(6)$ is the same as $f(4)$ , since it is $1$ more than a multiple of $6$ . Therefore, we have $2+1+1+3+1$ which is $\boxed {\textbf{(A)8}}$ .
~Arcticturn

## Solution 4
First, we compute $f \left( 2 \right)$ .
Because $N > 4 \cdot 10^{312}$ , $\sqrt{N} > 2 \cdot 10^{156}$ . Because $N < 9 \cdot 10^{312}$ , $\sqrt{N} < 3 \cdot 10^{156}$ .
Therefore, $f \left( 2 \right) = 2$ .
Second, we compute $f \left( 3 \right)$ .
Because $N > 1 \cdot 10^{312}$ , $\sqrt[3]{N} > 1 \cdot 10^{104}$ . Because $N < 8 \cdot 10^{312}$ , $\sqrt[3]{N} < 2 \cdot 10^{104}$ .
Therefore, $f \left( 3 \right) = 1$ .
Third, we compute $f \left( 4 \right)$ .
Because $N > 1 \cdot 10^{312}$ , $\sqrt[4]{N} > 1 \cdot 10^{78}$ . Because $N < 16 \cdot 10^{312}$ , $\sqrt[4]{N} < 2 \cdot 10^{78}$ .
Therefore, $f \left( 4 \right) = 1$ .
Fourth, we compute $f \left( 5 \right)$ .
Because $N > 3^5 \cdot 10^{310}$ , $\sqrt[5]{N} > 3 \cdot 10^{62}$ . Because $N < 4^5 \cdot 10^{310}$ , $\sqrt[5]{N} < 4 \cdot 10^{62}$ .
Therefore, $f \left( 5 \right) = 3$ .
Fifth, we compute $f \left( 6 \right)$ .
Because $N > 1 \cdot 10^{312}$ , $\sqrt[6]{N} > 1 \cdot 10^{52}$ . Because $N < 2^6 \cdot 10^{312}$ , $\sqrt[6]{N} < 2 \cdot 10^{52}$ .
Therefore, $f \left( 6 \right) = 1$ .
Therefore, \begin{align*} f \left( 2 \right) + f \left( 3 \right) + f \left( 4 \right) + f \left( 5 \right) + f \left( 6 \right) & = 2 + 1 + 1 + 3 + 1 \\ & = 8 . \end{align*}
Therefore, the answer is $\boxed{\textbf{(A) }8}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 5 (Guessing)
Benford's Law states that in random numbers, the leading digit is more likely to be $1,2,$ or $3$ rather than $8$ or $9$ . From here, we can eliminate C, D, E. It is better to guess between A and B than not guess at all since your expected score from doing this is $3$ points.
~MathFun1000

## Solution 6 (Intuition)
To begin with, you can test some numbers and find a pattern. For $f(2)$ , we get the leading digit of $\sqrt{7}$ is 2, and the leading digit of $\sqrt{77}$ is 8. With each $7$ afterward, it repeats in a loop: $2$ for $7$ , $8$ for $77$ , $2$ for $777$ , $8$ for $777$ , and so on. Since the problem states that $N$ is a $313$ -digit number, we get the leading digit as $2$ for $f(2)$ . For $f(3)$ , it repeats in a loop of $3$ ( $\text{3rd}$ root means it repeats every $3$ times). In this case, you would get the leading digit for the $\text{3rd}$ root of $7$ to be 1, $77$ it will be 4, and for $777$ it will be 9. Since $N$ is $1$ more than a multiple of 3, the leading digit for $f(3)$ is $1$ . Likewise, we can find the leading digits for $f(4)$ to be $1$ , $f(5)$ to be $3$ , and $f(6)$ to be $1$ :
For $f(2)$ : $7: \boxed{2},\hspace{0.085in} 77: 8 ...$
For $f(3)$ : $7: \boxed{1},\hspace{0.085in} 77: 4,\hspace{0.085in} 777: 9 ...$
For $f(4)$ : $7: \boxed{1},\hspace{0.085in} 77: 2,\hspace{0.085in} 777: 5,\hspace{0.085in} 7777: 9 ...$
For $f(5)$ : $7: 1,\hspace{0.085in} 77: 2,\hspace{0.085in} 777: \boxed{3},\hspace{0.085in} 7777: 6,\hspace{0.085in} 77777: 9 ...$
For $f(6)$ : $7: \boxed{1},\hspace{0.085in} 77: 2,\hspace{0.085in} 777: 3,\hspace{0.085in} 7777: 4,\hspace{0.085in} 77777: 6,\hspace{0.085in} 777777: 9 ...$
Remember that it loops every $r$ times; the boxed numbers are where $N$ falls. Thus, the desired sum is $2+1+1+3+1 = \boxed{\textbf{(A) }8}$
~ cyberhacker

## Video Solution by Interstigation
https://youtu.be/CqyVowe6qN4
~Interstigation

## Video Solution 2 by WhyMath
https://youtu.be/QEc1GhZnDuo
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .