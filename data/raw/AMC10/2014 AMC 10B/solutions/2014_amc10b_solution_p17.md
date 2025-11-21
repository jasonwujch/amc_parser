# 2014 AMC 10B Problem 17

## Problem

What is the greatest power of $2$ that is a factor of $10^{1002} - 4^{501}$ ?

$\textbf{(A) } 2^{1002} \qquad\textbf{(B) } 2^{1003} \qquad\textbf{(C) } 2^{1004} \qquad\textbf{(D) } 2^{1005} \qquad\textbf{(E) }2^{1006}$

## Solution 1
We begin by factoring the $2^{1002}$ out. This leaves us with $5^{1002} - 1$ .
We factor the difference of squares, leaving us with $(5^{501} - 1)(5^{501} + 1)$ . We note that all even powers of $5$ more than two end in ... $625$ . Also, all odd powers of five more than $2$ end in ... $125$ . Thus, $(5^{501} + 1)$ would end in ... $126$ and thus would contribute one power of two to the answer, but not more.
We can continue to factor $(5^{501} - 1)$ as a difference of cubes, leaving us with $(5^{167} - 1)$ times an odd number (Notice that the other number is $5^{334} + 5^{167} + 1$ . The powers of $5$ end in $5$ , so the two powers of $5$ will end with $0$ . Adding $1$ will make it end in $1$ . Thus, this is an odd number). $(5^{167} - 1)$ ends in ... $124$ , contributing two powers of two to the final result.
Or we can see that $(5^{501} - 1)$ ends in $124$ , and is divisible by $2$ only. Still that's $2$ powers of $2$ .
Adding these extra $3$ powers of two to the original $1002$ factored out, we obtain the final answer of $\textbf{(D) } 2^{1005}$ .

## Solution 2
First, we can write the expression in a more primitive form which will allow us to start factoring. \[10^{1002} - 4^{501} = 2^{1002} \cdot 5^{1002} - 2^{1002}\] Now, we can factor out $2^{1002}$ . This leaves us with $5^{1002} - 1$ . Call this number $N$ . Thus, our final answer will be $2^{1002+k}$ , where $k$ is the largest power of $2$ that divides $N$ . Now we can consider $N \pmod{16}$ , since $k \le 4$ by the answer choices.
Note that \begin{align*} 5^1 &\equiv 5 \pmod{16} \\ 5^2 &\equiv 9 \pmod{16} \\ 5^3 &\equiv 13 \pmod{16} \\ 5^4 &\equiv 1 \pmod{16} \\ 5^5 &\equiv 5 \pmod{16} \\ &\: \: \qquad \vdots \end{align*} The powers of $5$ cycle in $\mod{16}$ with a period of $4$ . Thus, \[5^{1002} \equiv 5^2 \equiv 9 \pmod{16} \implies 5^{1002} - 1 \equiv 8 \pmod{16}\] This means that $N$ is divisible by $8= 2^3$ but not $16 = 2^4$ , so $k = 3$ and our answer is $2^{1002 + 3} =\boxed{\textbf{(D)}\: 2^{1005}}$ .

## Solution 3
Convert $4^{501}=2^{1002}$ . We can factor out $2^{1002}$ to get that $\nu_2(10^{1002}-2^{1002})=1002+\nu_2(5^{1002}-1)$ . Using the adjusted Lifting The Exponent lemma ( $\nu_2(a^n-b^n)=\nu_2(n)+\nu_2(a^2-b^2)-1$ for all even $n$ and odd $a,b$ ), we get that the answer is $2^{1002+\nu_2(1002)+\nu_2(24)-1}=2^{1002+1+3-1}=\boxed{\textbf{(D)}2^{1005}}$

## Solution 4
Factor out $2^{1002}$ to get $2^{1002}(5^{1002} - 1)$ . Since $5^{1002}-1\equiv (-3)^{1002}-1\equiv (9)^{501}-1\equiv 1^{501}-1\equiv 0\pmod{8}$ , but $5^{1002}-1\equiv 11^{1002}-1\equiv 121\cdot (11^4)^{250} - 1\equiv 121 - 1\equiv 8 \pmod{16}$ , $5^{1002}-1$ has 3 factors of 2. Hence $2^{1002 + 3} =\boxed{2^{1005}}$ is the largest power of two which divides the given number

## Solution 5
Like Solution 1, factor out $2^{1002}$ to get $(2^{1002})(5^{501}-1)(5^{501}+1)$ . Using engineer's induction, we observe that for any positive integer $5^n$ (where $n$ is an odd positive integer), it appears that the least even numbers directly above and below $n$ in value must contain a maximum multiple of $4$ and a maximum multiple of $2$ . Hence, the answer is $2^{1002+2+1}$ which is $\boxed{\textbf{(D)} 2^{1005}}$ .
Proof;
For all integers $x$ where $x=5^{n}$ where n is an odd integer, $x$ must end in $125.$ Thus, we find that $x-1$ and $x+1$ respectively end in $124$ and $126.$
Case $1$ : $x-1$
We know that this number takes the form $abcde... 124$ where $abcde...$ is an integer that ends in $124$ . Because $abcde...$ is a multiple of $4$ times an even number $e$ while $124$ is $4(31)$ , we find that $X-1$ must be $4e + 4 \cdot 31 = 4(e+31) = 4o$ where $o$ is an odd number
Case $2$ : $x+1$
We know that this number $fghijk...126$ ends. Because it is $2$ more than the number $x-1$ , which is a multiple of $4$ , we find $x+1 = 4o + 2$ which is an even number that is not divisible by $4$ . Thus, it must have a maximum of $1$ multiple of $2$ .
This means that for any number $x$ being in the form $5^{n}$ where $n$ is an odd integer, $x-1$ must have a maximum of $2$ factors of $2$ while $x+1$ must have a maximum of $1$ factor of $2$ .
~ShangJ2

## Solution 6
Using difference of squares, we get $\left(10^{501}-2^{501}\right) \left(10^{501}+2^{501}\right)$ . Factoring a $2^{501}$ out, we get $\left(2^{501}\right) \left(5^{501}-1\right) \left(2^{501}\right) \left(5^{501}+1\right)$ , and grouping like terms give $\left(2^{1002}\right) \left(5^{501}-1\right) \left(5^{501}+1\right)$ .
Then, you would go ahead and innocently choose $\textbf{(A) } 2^{1002}$ , right? No! Note that $5^n$ , where $n$ is any odd integer greater than or equal to $3$ , it always ends in $125$ . So, $5^{501}+1$ ends in $126$ and $5^{501}-1$ ends in $124$ , so they add up to an extra three $2$ 's. Therefore, the answer is actually $2^{1002+3}=\boxed{\textbf{(D) } 2^{1005}}$ .
~MrThinker

## Solution 7
Note that we are trying to find the number of powers of $2$ in $(5^{1002}-1) \cdot 2^{1002}.$ Let's see how many $5^{1002}-1$ has.
Try the first 4 powers of 5, namely $5^1$ , $5^2$ , $5^3$ , and $5^4$ . Note that when taking $mod 4$ , all result in $1 mod 4$ . When taking $mod 8$ , even powers result in $1 mod 8$ . When taking $mod 16$ , every $4$ th power (i.e. $4,8,..$ ) will result in $1 mod 16$ .
Because $1002$ is even but $2 mod 4, 5^1002$ will be equivalent to $1 mod 8$ but not $1 mod 16$ . Hence $5^1002 - 1$ ≡ $0 mod 8$ , and so we have an extra power of $2^3$ , hence the result is $1002+3=1005 (D)$ .
~mathboy282 ~Minor Edits by L314159265358979323846264

## Video Solution
https://youtu.be/aCtvD8nitgg
~savannahsolver

## Video Solution (Simplified Explanation - Grade 7 Level)
https://youtu.be/6mkzhgRAx9Q
~Ace the olympiad
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .