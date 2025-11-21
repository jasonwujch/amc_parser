# 2022 AMC 10B Problem 13

## Problem

The positive difference between a pair of primes is equal to $2$ , and the positive difference between the cubes of the two primes is $31106$ . What is the sum of the digits of the least prime that is greater than those two primes?

$\textbf{(A)}\ 8 \qquad\textbf{(B)}\ 10 \qquad\textbf{(C)}\ 11 \qquad\textbf{(D)}\ 13 \qquad\textbf{(E)}\ 16$

## Solution 1 (Simplest)
Denote the two primes as \( a \) and \( b \). Then,
\( a - b = 2 \)
\( a^3 - b^3 = 31106 \)
We see that \( a = 2 + b \)
Now, we have \( (2+b)^3 - b^3 = 31106 \)
We apply the binomial theorem (or just expand) to \( (2+b)^3 \), getting
\( 8 + 12b + 6b^2 + b^3 - b^3 = 31106 \)
\( \Rightarrow 8 + 12b + 6b^2 = 31106 \)
Subtracting by 8 on both sides results in
\( 6b^2 + 12b = 31098 \)
\( b^2 + 2b - 5183 \)
\( (b-71)(b+73) \)
We see that \( b \in \{-73, 71\} \). We negate all negative values, and see that \( b = 71 \).
Therefore \( a - b = 2 \), \( a = 2 + b \), \( a = 2 + 71 = 73 \).
The next prime number greater than both of these is $79$ , and therefore our answer is \( 7 + 9 = \) $\boxed{\textbf{(E) }16}$ .
~Pinotation

## Solution 2
Let the two primes be $a$ and $b$ with $a>b$ . We would have $a-b=2$ and $a^{3}-b^{3}=31106$ . Using difference of cubes, we would have $(a-b)(a^{2}+ab+b^{2})=31106$ . Since we know $a-b$ is equal to $2$ , $(a-b)(a^{2}+ab+b^{2})$ would become $2(a^{2}+ab+b^{2})=31106$ . Simplifying more, we would get $a^{2}+ab+b^{2}=15553$ .
Now let's introduce another variable. Instead of using $a$ and $b$ , we can express the primes as $x+2$ and $x$ where $a$ is $x+2$ and b is $x$ . Plugging $x$ and $x+2$ in, we would have $(x+2)^{2}+x(x+2)+x^{2}$ . When we expand the parenthesis, it would become $x^{2}+4x+4+x^{2}+2x+x^{2}$ . Then we combine like terms to get $3x^{2}+6x+4$ which equals $15553$ . Then we subtract 4 from both sides to get $3x^{2}+6x=15549$ . Since all three numbers are divisible by 3, we can divide by 3 to get $x^{2}+2x=5183$ .
Notice how if we add 1 to both sides, the left side would become a perfect square trinomial: $x^{2}+2x+1=5184$ which is $(x+1)^{2}=5184$ . Since $2$ is too small to be a valid number, the two primes must be odd, therefore $x+1$ is the number in the middle of them. Conveniently enough, $5184=72^{2}$ so the two numbers are $71$ and $73$ . The next prime number is $79$ , and $7+9=16$ so the answer is $\boxed{\textbf{(E) }16}$ .
~Trex226
A note: If you aren't entirely familiar with square trinomials, after we have $x^{2}+2x=5183$ , we can simply guess and check from here. We know that $70^{2} = 4900$ , and we notice that for $x^{2}+2x=5183$ , $x$ must be a odd number. Thus we can guess that $x$ =71, which proves to be right. Continuing, we then know the larger prime is 73, and we know that 75 and 77 aren't primes, so thus our next bigger prime is 79, and 7+9=16. Thus the answer is $\boxed{\textbf{(E) }16}$ .
~Rhx
Understanding the "Completing a Square" formula: Adding $1$ to $x^{2}+2x$ is called completing a square. In the expression $x^{2}+bx$ , where $b$ is a constant, you can add $b/{2}$ to make the square $(x+b/{2})^{2}$ .
~NXC

## Solution 3
Let the two primes be $a$ and $b$ , with $a$ being the larger prime. We have $a - b = 2$ , and $a^3 - b^3 = 31106$ . Using difference of cubes, we obtain $a^2 + ab + b^2 = 15553$ . Now, we use the equation $a - b = 2$ to obtain $a^2 - 2ab + b^2 = 4$ . Hence, \[a^2 + ab + b^2 - (a^2 - 2ab + b^2) = 3ab = 15553 - 4 = 15549\] \[ab = 5183.\] Because we have $a = b+2$ , $ab = (b+1)^2 - (1)^2$ . Thus, $(b+1)^2 = 5183 + 1 = 5184$ , so $b+1 = 72$ . This implies $a = 73$ , $b = 71$ , and thus the next biggest prime is $79$ , so our answer is $7 + 9 = \boxed{\textbf{(E) }16}$
~mathboy100 ~ minor edits by AnubhavDey

## Solution 4 (Estimation)
Let the two primes be $p$ and $q$ such that $p-q=2$ and $p^{3}-q^{3}=31106$
By the difference of cubes formula, $p^{3}-q^{3}=(p-q)(p^{2}+pq+q^{2})$
Plugging in $p-q=2$ and $p^{3}-q^{3}=31106$ ,
$31106=2(p^{2}+pq+q^{2})$
Through the givens, we can see that $p \approx q$ .
Thus, $31106=2(p^{2}+pq+q^{2})\approx 6p^{2}\\p^2\approx \tfrac{31106}{6}\approx 5200$
Recall that $70^2=4900$ and $80^2=6400$ . It follows that our primes must be only marginally larger than $70$ , where we conveniently find $p=73, q=71$
The least prime greater than these two primes is $79 \implies 7 + 9 \implies \boxed{\textbf{(E) }16}$
~BrandonZhang202415 ~SwordOfJustice (small edits)

## Solution 5
Let the two primes be $x + 1$ and $x - 1$ . Then, plugging it into the second condition, we get $(x + 1)^3 - (x - 1)^3 = 31106.$ Expanding the left side, \[6x^2 + 2 = 31106 \implies x^2 = 5184.\] Taking the square root of both sides, we get that $x = 72$ and the larger prime is $73$ . The smallest prime larger than $73$ is $79$ , which has a digit sum of $7 + 9 = \boxed{16}.$
- NL008

## Video Solution (⚡️Lightning Fast⚡️)
https://youtu.be/FQn9XOPKlbw
~Education, the Study of Everything

## Video Solution by Interstigation
https://youtu.be/yLFiSmLJJ5A

## Video Solution by TheBeautyofMath
https://youtu.be/Mi2AxPhnRno?t=626
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .