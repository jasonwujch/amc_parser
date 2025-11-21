# 2025 AMC 10A Problem 19

## Problem

An array of numbers is constructed beginning with the numbers $-1$ , $3$ , and $1$ in the top row. Each adjacent pair of numbers is summed to produce a number in the next row. Each row begins and ends with $-1$ and $1,$ respectively.

\[\large{-1}\qquad\large{3}\qquad\large{1}\] \[\large{-1}\qquad\large{2}\qquad\large{4}\qquad\large{1}\] \[\large{-1}\qquad\large{1}\qquad\large{6}\qquad\large{5}\qquad\large{1}\] If the process continues, one of the rows will sum to $12{,}288$ . In that row, what is the third number from the left?

$\textbf{(A)} \: -29\qquad\textbf{(B)} \: -21\qquad\textbf{(C)} \: -14\qquad\textbf{(D)} \: -18\qquad\textbf{(E)} \: -3$

## Solution 1
Consider the polynomial $f(x) = -x^2+3x+1.$ When we multiply this polynomial by $x+1,$ we are essentially doing the operation given in the problem (When we multiply $p(x)$ by $x+1,$ a term of degree $d$ in the yielded expression is the sum of $1\cdot(\text{degree d})$ and $x\cdot(\text{degree d-1})$ in $p(x)$ This effect is visible in Pascal's Triangle). So, if we let the coefficients of $f(x)$ be the zero row of the array, then the $n^{th}$ row is just the coefficients of $f(x)(x+1)^n.$ The next thing to note is that the sum of the coefficients in any polynomial $p(x)$ is just $p(1).$ Therefore, the sum of the entries in the $n^{th}$ row of the array is $f(1)(1+1)^n=3\cdot2^n.$ Letting this equal $12288,$ we get $n=12.$ We are looking for the $3^{rd}$ term in the $12^{th}$ row. The $12^{th}$ row is given by the coefficients of $f(x)(x+1)^{12}=(-x^2+3x+1)(x+1)^{12}.$ Since the degree of the resulting expression is $14,$ the third term in the row is just the coefficient of $x^{12}$ in the expression, which is $-\dbinom{12}{10}+3\dbinom{12}{11}+1=\boxed{\textbf{(A) }-29}.$
~Tacos_are_yummy_1
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 09:26, 7 November 2025 (EST)saharshdevaraju)

## Solution 2
If we take a look at the first few rows, we notice that the sum of the terms in each row $n$ is equal to the twice the sum of row $n-1$ . We note the first row is $3$ so recognize $12,228$ must be equal to $3$ times a power of $2$ . $12,288=3\cdot 4096=3 \cdot 2^{12}$ . Therefore, we are looking for the $3$ rd term from the left in the $13$ th row. From here, we can take a look at the second number of each row, noting that it will always decrease by $1$ because it is being added to the $-1$ on its left. We can compute the $3$ rd term of each row by adding the $2$ nd and $3$ rd term of the previous row, which means that to find the $3$ rd term of the nth row, we simply have to add all of the 2nd terms of each row starting from the row with the first appearance of the $3$ rd term, which is $6$ . Using this, we get the expression $6+(1+0+(-1)+...+(-(n-5))$ , where $n$ is $13$ . Plugging it in, we get $6+(1+0+(-1)+...+(-8))$ , which tells us that the $3$ rd number from the left of the $13$ th row is $\boxed{\text{(A) -29}}$ .
~Squidget
~YTH
### Remark (Why each row is twice the previous row)
To prove that the sum of each row is $2$ times the previous row, use the equation ${(1+1)}^n$ with the normal Pascal's triangle and use the binomial theorem from there.
Example: In the fifth row of Pascal's triangle, the numbers are $1, 4, 6, 4, 1$ . The first number can be represented by ${4 \choose 0} = 1$ , the second by ${4 \choose 1} = 4$ , the third by ${4 \choose 2} = 6$ , the fourth by ${4 \choose 3} = 4$ , and the last by ${4 \choose 4} = 1$ . The sum of these five numbers is $16$ which is also $2^{4}$ . Using the binomial theorem with ${(1+1)}^4$ , we get $1 + 4 + 6 + 4 + 1 = 16$ , the same results in Pascal's triangle. We could also solve ${(1+1)}^4$ by converting it to $2^4 = 16$ , proving the identity that all rows in Pascal's triangle are exactly twice the previous row and can be represented by $2^{n}$ .
~Bros1 ~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 21:27, 7 November 2025 (EST)saharshdevaraju)

## Solution 3 - Fast and Effective!
\(\large \textbf{<3 minute solve!}\)
Add all the numbers up in the first row. You get $3.$ Now, add all the numbers up on the second row. You get $6.$ Notice that as the rows keep going, the sum of the numbers in the row keeps doubling. When you repeat this process, you realize that you reach $12288$ on the $13^{th}$ row.
Knowing this, we can use this pattern to find the solution quickly. We know that the first number will always be $-1$ , so we can ignore that. Knowing this, all you have to do now is to add up the second and third numbers $13$ times. This is already done for us three times, so we just have to do it ten more. Note that you do not have to do this process for all the numbers, only the second and third.
Doing this 13 times (since $\frac{12288}{3}=4096=2^{12}=2^{13-1}$ ), you get the following string of numbers (starting from the first one): $1, 4, 6, 7, 7, 6, 4, 1, -3, -8, -14, -21,$ and finally, $\boxed{\textbf{(A) }-29}.$
~i_am_not_suk_at_math (saharshdevaraju 21:19, 6 November 2025 (EST)saharshdevaraju)
~minor edits by iiiiiizh
~minor $\LaTeX$ edits by yogert2
~minor edit by Leong2023
~minor $\LaTeX$ edits by kfclover

## Solution 4
From adding the sum of all terms in the first few rows, we see that $S(r(1))=3, S(r(2))=6, S(r(3))=12, S(r(4))=24,...$ and so on. We can deduce that $S(r(n))=3 \cdot 2^{n-1}$ is the sum of all numbers in row $n$ . Now, set $3 \cdot 2^{n-1} = 12288$ so we have $2^{n-1} = 4096 = 2^{12}$ . It follows that $n=13$ . Now let $a_n$ be the 2nd number of each row, and $b_n$ be the 3rd number of each row. Since, the first number of each row is -1, $a_n=a_{n-1}-1$ . Additionally, $b_n = b_{n-1}+a_{n-1}$ .
\begin{array}{|c|c|} \hline a_n & b_n \\ \hline a_1 = 3 & b_1 = 1 \\ a_2 = 2 & b_2 = 4 \\ a_3 = 1 & b_3 = 6 \\ a_4 = 0 & b_4 = 7 \\ a_5 = -1 & b_5 = 7 \\ a_6 = -2 & b_6 = 6 \\ a_7 = -3 & b_7 = 4 \\ a_8 = -4 & b_8 = 1 \\ a_9 = -5 & b_9 = -3 \\ a_{10} = -6 & b_{10} = -8 \\ a_{11} = -7 & b_{11} = -14 \\ a_{12} = -8 & b_{12} = -21 \\ a_{13} = -9 & b_{13} = -29 \\ \hline \end{array}
We are asked to compute $b_{13} = \boxed{\textbf{(A) }-29}.$
~hxve
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 21:29, 6 November 2025 (EST)saharshdevaraju)

## Solution 5 (Wish I used this)
So the sum is doubling every time, starting with 3.
$12288 = 3 \cdot 2^{12}$
So in the 13th row we go, so we eventually get that the 3rd number is $\boxed{\text{(A)}-29}$
Go check out solution 1, looks interesting.
~Aarav22

## Solution 6
We firstly notice that the pattern for the sums of each row is $S_n$ $=$ $3 \cdot 2^n$ where n is the number of the row. Since the sum for the row we are looking for is $12288$ , We can write the equation $3 \cdot 2^n$ $=$ $12288$ which solving gives $n = 12$ .
Recognizing that the $n^{th}$ row term is basically a scaled version of the first row-term $(-1,3,1)$ , we can write a polynomial $f(x) = (-1x+3x+1x^2)(x+1)^n$ , where $(x+1)^n$ is kind of a "shifting step" to proceed down the triangle to the $n^{th}$ term.
-you can test for the different values like $(x+1)^1$ which results to coefficients $(-1,2,4,1)$ which matches the second row down
Now we recognize we can write the polynomial of the $12^{th}$ term in the form $(a_0 + a_1 x + a_2 x^2 + \dots + a_m x^m)(1+x)^n$ which we can simplify using the binomial theorem achieving this: $\sum_{i=0}^{m} a_i \binom{n}{k-i}$
Plugging the terms in we get: $(-1)\binom{n}{2} + 3\binom{n}{1} + 1\binom{n}{0}$ where $n = 12$ thus giving $\boxed{(A) -29}$
~LucasW
~Leong2023
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 22:01, 7 November 2025 (EST)saharshdevaraju)

## Solution 7
The first step is recognizing that you multiply the sum by two each row. This is because each number adds to the number down to the left and the number down to the right (this includes the -1 and 1 on the ends). Thus the sum in row $n$ is $3*2^{n-1}$ which means the question corresponds to row $13$ .
Now we can look at the trends in the terms of each row. The first term in each row is $-$ 1, which makes the second term in each row $3,2,1,0,-1...$
This leads us to finding the third term in each row has the pattern of $1, 1+3, 1+3+2, 1+3+2+1, 1+3+2+1+0, 1+3+2+1+0+-1...$
Therefore we just need to find $1$ plus the sum of $3$ through $-8$ inclusive which by any number of methods computes to $1-30=\boxed{\text{(A) }-29}$ .
~Ant_Eater

## Video Solution
https://youtu.be/sjeE987U_hU
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .