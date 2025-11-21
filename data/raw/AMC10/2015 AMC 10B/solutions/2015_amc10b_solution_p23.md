# 2015 AMC 10B Problem 23

## Problem

Let $n$ be a positive integer greater than $4$ such that the decimal representation of $n!$ ends in $k$ zeros and the decimal representation of $(2n)!$ ends in $3k$ zeros. Let $s$ denote the sum of the four least possible values of $n$ . What is the sum of the digits of $s$ ?

$\textbf{(A) }7\qquad\textbf{(B) }8\qquad\textbf{(C) }9\qquad\textbf{(D) }10\qquad\textbf{(E) }11$

## Solution 1
A trailing zero requires a factor of two and a factor of five. Since factors of two occur more often than factors of five, we can focus on the factors of five. We make a chart of how many trailing zeros factorials have:
\[\begin{array}{c|c|c|c|c|c|c} \mathrm{Factorial}&0!-4!&5!-9!&10!-14!&15!-19!&20!-24!&25!-29!\\\hline \mathrm{Zeros}&0&1&2&3&4&6 \end{array}\]
We first look at the case when $n!$ has $1$ zero and $(2n)!$ has $3$ zeros. If $n=5,6,7$ , $(2n)!$ has only $2$ zeros. But for $n=8,9$ , $(2n)!$ has $3$ zeros. Thus, $n=8$ and $n=9$ work.
Secondly, we look at the case when $n!$ has $2$ zeros and $(2n)!$ has $6$ zeros. If $n=10,11,12$ , $(2n)!$ has only $4$ zeros. But for $n=13,14$ , $(2n)!$ has $6$ zeros. Thus, the smallest four values of $n$ that work are $n=8,9,13,14$ , which sum to $44$ . The sum of the digits of $44$ is $\boxed{\mathbf{(B)\ }8}$

## Solution 2
By Legendre's Formula and the information given, we have that $3\left(\left\lfloor{\frac{n}{5}}\right\rfloor+\left\lfloor{\frac{n}{25}}\right\rfloor\right)=\left\lfloor{\frac{2n}{5}}\right\rfloor+\left\lfloor{\frac{2n}{25}}\right\rfloor$ .
We have $n<100$ as there is no way that if $n>100$ , $(2n)!$ would have $3$ times as many zeroes as $n!$ .
First, let's plug in the number $5$ . We get that $3(1)=1$ , which is obviously not true. Hence, $n>5$
After several attempts, we realize that the RHS needs $1$ to $2$ more "extra" zeroes than the LHS. Hence, $n$ is greater than a multiple of $5$ .
We find that the least four possible $n$ are $8,9,13,14$ .
$8+9+13+14=17+27=44\implies 4+4=8\implies\boxed{B}$ .

## Solution 3
Let $n=5m+k$ for some natural numbers $m$ , $k$ such that $k\in\{0,1,2,3,4\}$ . Notice that $n<5^3=125$ . Thus \[3(\left\lfloor\frac{n}{5}\right\rfloor+\left\lfloor\frac{n}{25}\right\rfloor)=\left\lfloor\frac{2n}{5}\right\rfloor+\left\lfloor\frac{2n}{25}\right\rfloor+\left\lfloor\frac{2n}{125}\right\rfloor\] For smaller $n$ , we temporarily let $\left\lfloor\frac{2n}{125}\right\rfloor=0$ \[3(\left\lfloor\frac{n}{5}\right\rfloor+\left\lfloor\frac{n}{25}\right\rfloor)=\left\lfloor\frac{2n}{5}\right\rfloor+\left\lfloor\frac{2n}{25}\right\rfloor\] \[3(\left\lfloor\frac{5m+k}{5}\right\rfloor+\left\lfloor\frac{5m+k}{25}\right\rfloor)=\left\lfloor\frac{2(5m+k)}{5}\right\rfloor+\left\lfloor\frac{2(5m+k)}{25}\right\rfloor\] \[3(\left\lfloor\frac{5m+k}{5}\right\rfloor+\left\lfloor\frac{5m+k}{25}\right\rfloor)=\left\lfloor\frac{10m+2k}{5}\right\rfloor+\left\lfloor\frac{10m+2k}{25}\right\rfloor\] \[3m+3\left\lfloor\frac{5m+k}{25}\right\rfloor=2m+\left\lfloor\frac{2k}{5}\right\rfloor+\left\lfloor\frac{10m+2k}{25}\right\rfloor\] \[m+3\left\lfloor\frac{5m+k}{25}\right\rfloor=\left\lfloor\frac{2k}{5}\right\rfloor+\left\lfloor\frac{10m+2k}{25}\right\rfloor\] To minimize $n$ , we let $\left\lfloor\frac{5m+k}{25}\right\rfloor=\left\lfloor\frac{10m+2k}{25}\right\rfloor=0$ , then \[m=\left\lfloor\frac{2k}{5}\right\rfloor\] Since $k<5$ , $m>0$ , the only integral value of $m$ is $1$ , from which we have $k=3,4\Longrightarrow n=8,9$ .
Now we let $\left\lfloor\frac{5m+k}{25}\right\rfloor=0$ and $\left\lfloor\frac{10m+2k}{25}\right\rfloor=1$ , then \[m=\left\lfloor\frac{2k}{5}\right\rfloor+\left\lfloor\frac{10m+2k}{25}\right\rfloor\] Since $k<5$ , $10m>15\Longrightarrow m\ge2$ .
If $m>2$ , then \[m>\left\lfloor\frac{2k}{5}\right\rfloor+\left\lfloor\frac{10m+2k}{25}\right\rfloor\] which is a contradiction.
Thus $m=2\Longrightarrow\left\lfloor\frac{2k}{5}\right\rfloor=1\Longrightarrow n=13,14$
Finally, the sum of the four smallest possible $n=8+9+13+14=44$ and $4+4=8$ . $\boxed{\mathrm{(B)}}$
~ Nafer

## Solution 4
We first note that the number of 0's in $n!$ is determined by how many 5's are in the prime factorization. We use Legendre's Formula and split up into two cases:
$\textbf{CASE ONE: } 5\leq 2n < 25.$
The only way we can fulfill the requirements is if $\lfloor{\dfrac{n}{5}}\rfloor = 1$ and $\lfloor{\dfrac{2n}{5}}\rfloor=3$ which means that $5\leq n <10$ and $15\leq 2n < 20$ . The only way this works is if $n = 8 \text{ or } 9.$
$\textbf{CASE TWO: } 25 \leq 2n$ .
Since we want the smallest values of $n$ , we first try it when $2n<30.$ Thus $(2n)!$ has 6 zeros, which implies that $n!$ must have 2. The only way to do this while maintaining our restrictions for $2n$ is if $n = 13 \text{ or } 14.$
So the sum of the four values is $8+9+13+14=44$ so the digit is sum is $\boxed{\mathbf{(B)\ }8}.$
-ConfidentKoala4

## Solution 5
We will use trial and error to determine the answer to this problem. If $n = 5$ , then $n!$ has $1$ zero, and $2n!$ will have $2$ zeros. But $3 \cdot 1 \neq 2$ so $n = 5$ does not work. Similarly $n = 6, 7$ do not work either. But $n = 8$ works because $8!$ has $1$ zero and $16!$ has $3$ zeros. Note that $n = 9$ also works because $9!$ has $1$ zero and $18!$ has $3$ zeros. After performing trial and error several times, we find that $n = 10, 11, 12$ do not work but $n = 13, 14$ do work. Therefore, the four smallest values of $n$ are $8, 9, 13, 14$ . Therefore adding them together gives $44$ and our answer is $\boxed{\mathbf{(B)\ }8}.$
- Yiyj1
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .