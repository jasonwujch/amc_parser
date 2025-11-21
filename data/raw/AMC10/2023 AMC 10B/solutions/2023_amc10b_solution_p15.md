# 2023 AMC 10B Problem 15

## Problem

What is the least positive integer $m$ such that $m\cdot2!\cdot3!\cdot4!\cdot5!...16!$ is a perfect square?

$\textbf{(A) }30\qquad\textbf{(B) }30030\qquad\textbf{(C) }70\qquad\textbf{(D) }1430\qquad\textbf{(E) }1001$

## Solution 1
We want $m\cdot2!\cdot3!\cdot4!\cdot\dots\cdot16!$ to be a perfect square. Notice that we can rewrite and pair up certain elements:
\[m\cdot2\cdot3!\cdot(4\cdot3!)\cdot5!\cdot(6\cdot5!)\cdot\dots\cdot15!\cdot(16\cdot15!)=m\cdot2\cdot4\cdot6\cdot\dots\cdot16\cdot(3!)^2(5!)^2\cdot\dots\cdot(15!)^2.\]
Note here that this is equivalent to simply $m\cdot2\cdot4\cdot\dots\cdot16$ being a perfect square (this is intuitively obvious: i.e. if $a=bc$ is a perfect square and so is $b$ , then of course $c$ must be a perfect square too). We can rewrite this as the following:
\[m\cdot2^8\cdot(1\cdot2\cdot3\cdot\dots\cdot8)\equiv m\cdot2\cdot3\cdot4\cdot5\cdot6\cdot7\cdot8\equiv m\cdot70.\]
The smallest $m$ s.t. $70m$ is a perfect square is, of course, $70$ itself. QED.
~Technodoggo (rewritten as of 2024)

## Solution 2
Perfect squares have all of the powers in their prime factorization even. To evaluate $2!\cdot3!\cdot4!\cdot5!...16!$ we get the following:
$(2^{15}) \times (3^{14}) \times ((2^2)^{13}) \times (5^{12}) \times ((2 \times 3)^{11}) \times (7^{10}) \times ((2^3)^{9}) \times ((3^2)^8) \times \\ ((5 \times 2)^7) \times (11^6) \times (((2^2) \times 3)^5) \times (13^4) \times ((7 \times 2)^3) \times ((3 \times 5)^2) \times ((2^4)^1)$ .
Taking all powers $\mod 2$ we get:
$(2^1) \times ((2 \times 3)^1) \times (2^1) \times ((5 \times 2)^1) \times (3^1) \times ((7 \times 2)^1)$
Simplifying again, we finally get:
$(2^1) \times (5^1) \times (7^1)$
To make all the powers left even, we need to multiply by $(2 \times 5 \times 7)$ which is $\boxed{\text{(C) } 70}$ .
~darrenn.cp

## Solution 3
We can prime factorize the solutions: A = $2 \cdot 3 \cdot 5,$ B = $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13,$ C = $2 \cdot 5 \cdot 7,$ D = $2 \cdot 5 \cdot 11 \cdot 13,$ E = $7 \cdot 11 \cdot 13,$
We can immediately eliminate B, D, and E since 13 only appears in $13!, 14!, 15, 16!$ , so $13\cdot 13\cdot 13\cdot 13$ is a perfect square. Next, we can test if 7 is possible (and if it is not we can use process of elimination). 7 appears in $7!$ to $16!$ and 14 appears in $14!$ to $16!$ . So, there is an odd amount of 7's since there are 10 7's from $7!$ to $16!$ and 3 7's from $14!$ to $16!$ since 7 appears in 14 once, and $10+3=13$ which is odd. So we need to multiply by 7 to get a perfect square. Since 30 is not a divisor of 7, our answer is 70 which is $\boxed{\text{C}}$ .
~aleyang

## Solution 4
First, we note that $3! = 2! \cdot 3$ , $5! = 4! \cdot 5, ... 15! = 14! \cdot 15$ . So, $2!\cdot3! ={2!}^2\cdot3 \equiv 3, 4!\cdot5!={4!}^2\cdot5 \equiv 5, ... 14!\cdot15!={14!}^2\cdot15\equiv15$ . Simplifying the whole sequence and cancelling out the squares, we get $3 \cdot 5 \cdot 7 \cdot 9 \cdot 11 \cdot 13 \cdot 15 \cdot 16!$ . Prime factoring $16!$ and cancelling out the squares, the only numbers that remain are $2, 5,$ and $7$ . Since we need to make this a perfect square, $m = 2 \cdot 5 \cdot 7$ . Multiplying this out, we get $\boxed{\text{(C) } 70}$ .
~Stead (a.k.a. Aaron) & ~Technodoggo (add more examples)

## Solution 5 (Legendre's Formula)
We need to find the prime factorization of $16! \cdot 15! \cdot 14! ... \cdot 1!$ and check whether the exponents of each prime are odd or even.
Using Legendre's Formula on each of the factorials and adding the powers of each prime we get:
Powers of 2:
\[15 + 11 + 11 + 10 + 10 + 8 +8 + 7 + 7 + 4 + 4 + 3 + 3 + 1 + 1 + 0 = 103\]
Powers of 3: \[6 + 6 + 5 + 5 + 5 + 3 + 3 + 4 + 2 + 2 + 2 + 1 + 1 + 1 + 0 + 0 = 46\]
Powers of 5: \[3 + 3 + 2 + 2 + 2 + 2 + 2 + 1 + 1 + 1 + 1 + 1 + 0 + 0 + 0 + 0 = 23\]
Powers of 7: \[2 + 2 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 13\]
Powers of 11: \[1 + 1 + 1 + 1 + 1 + 1 = 6\]
Powers of 13: \[1 + 1 + 1 + 1 = 4\]
$2, 5,$ and $7$ have odd exponents, so the answer is $2\cdot 5 \cdot 7 = \boxed{\text{ (C) }70}$ .
~ grogg007

## Solution 6 (Bashy method)
We know that a perfect square must be in the form $2^{2a_1}\cdot3^{2a_2}\cdot5^{2a_3}...p^{2a_n}$ where $a_1, a_2, a_3, ..., a_n$ are nonnegative integers, and $p$ is the largest and $nth$ prime factor of our square number.
Let's assume $r=m\cdot2!\cdot3!\cdot4!\cdot5!...16!$ . We need to prime factorize $r$ and see which prime factors are raised to an odd power. Then, we can multiply one factor each of prime number with an odd number of factors to $m$ . We can do this by finding the number of factors of $2$ , $3$ , $5$ , $7$ , $11$ , and $13$ .
Case 1: Factors of $2$
We first count factors of $2^1$ in each of the factorials. We know there is one factor of $2^1$ each in $2!$ and $3!$ , two in $4!$ and $5!$ , and so on until we have $8$ factors of $2^1$ in $16!$ . Adding them all up, we have $1+1+2+2+...7+7+8=64$ .
Now, we count factors of $2^2$ in each of the factorials. We know there is one factor of $2^2$ each in $4!$ , $5!$ , $6!$ , and $7!$ , two in $8!$ , $9!$ , $10$ , and $11!$ , and so on until we have $4$ factors of $2^1$ in $16!$ . Adding them all up, we have $1+1+1+1+2+2+2+2+3+3+3+3+4=28$ .
Now we count factors of $2^3$ in each of the factorials. Using a similar method as above, we have a sum of $1+1+1+1+1+1+1+1+2=10$ .
Now we count factors of $2^4$ in each of the factorials. Using a similar method as above, we have a factor of $2^4$ in $16$ , so there is $1$ factor of $2^4$ .
Adding all the factors of $2$ , we have $103$ . Since $103$ is odd, $m$ has one factor of $2$ .
Case 2: Factors of $3$
We use a similar method as in case 1. We first count factors of $3^1$ . We obtain the sum $1+1+1+2+2+2+...4+4+4+5+5=50$ .
We count factors of $3^2$ . We obtain the sum $1+1+1+1+1+1+1+1=8$ .
Adding all the factors of $3$ , we have $58$ . Since $58$ is even, $m$ has $0$ factors of $3$ .
Case 3: Factors of $5$
We count the factors of $5^1$ : $1+1+1+1+1+2+2+2+2+2+3+3=21$ . Since $21$ is odd, $m$ has one factor of $5$ .
Case 4: Factors of $7$
We count the factors of $7^1$ : $1+1+1+1+1+1+1+2+2+2=13$ . Since $13$ is odd, $m$ has one factor of $7$ .
Case 5: Factors of $11$
We count the factors of $11^1$ : $1+1+1+1+1+1=6$ . Since $6$ is even, $m$ has $0$ factors of $11$ .
Case 6: Factors of $13$
We count the factors of $13^1$ : $1+1+1+1=4$ . Since $4$ is even, $m$ has $0$ factors of $13$ .
Multiplying out all our factors for $m$ , we obtain $2\cdot5\cdot7=\boxed{\text{ (C) }70}$ .
~arjken

## Solution 7 (Answer Choices)
We see that all the answer choices are divisible by $10$ except for $1001$ , and we also notice that the answer choices have $3$ , $7$ , $11$ , or $13$ as a prime factor.
Testing, we see that $3$ , $11$ , $13$ have an even power in the product, so we have that all the other answer choices will not work.
Therefore we just have $\boxed{\text{ (C) }70}$ .

## Solution 8 (Fastest Intuition)
Notice that you can add the factor $1!$ to the expression to make it $m\cdot1!\cdot2!\cdot3!\cdot4!\cdot5!\cdot6!\cdot7!\cdot8!\cdot9!\cdot10!\cdot11!\cdot12!\cdot13!\cdot14!\cdot15!\cdot16!$
Every consecutive pair $n!\cdot(n+1)!$ can be simplified to $n+1$ (divide out $n!^2$ ).
Resulting is the product $m\cdot2\cdot4\cdot6\cdot8\cdot10\cdot12\cdot14\cdot16 = m\cdot2^8\cdot8!$
This is easily simplified to $m\cdot2\cdot5\cdot7 = m\cdot70$ when dividing out perfect squares.
This means that $m$ must have a minimum factor of $70$ which gives answer choice $\boxed{\text{ (C) }70}$ .
~coolishu

## Solution 9(Pretty Quick similar to solution 8)
$16!\left(15!\right)$ this can be written as $16\left(15!\right)\left(15!\right)$
Thus
$16\left(15!\right)^{2}$
Now lets try
$16!15!14!$
$16\left(15\right)\left(14!\right)15\left(14!\right)\left(14!\right)$
thus $16\left(15\right)^{2}\left(14\right)^{3}$
we can continue this pattern until one to get $m\cdot2!\cdot3!\cdot4!\cdot5!...16! = 16\left(15\right)^{2}\left(14\right)^{3}\left(13\right)^{4}\left(12\right)^{5}\left(11\right)^{6}....\left(1\right)^{15}$
we can remove all the even powers of expression above to get
$16\left(14\right)^{3}\left(12\right)^{5}\left(10\right)^{7}\left(8\right)^{9}\left(6\right)^{11}\left(4\right)^{13}\left(2\right)^{15}$
we can see that all off the numbers are even and multiples of 2,3,5,7
the biggest possible number we should get is 2 times 3 times 5 times 7 which is 210 which means out anwer should be A or C 30 or 70.
Then look all the stuff with 7 which would only consist of ${14}^3$
which needs an extra 7 to give it company, so put answer must be divisble by 7 and less than 210
which leaves 70 or C as our answer
$\boxed{\text{ (C) }70}$ .
Note: you can also just remove all pairs of two to get $16\left(14\right)\left(12\right)\left(10\right)\left(8\right)\left(6\right)\left(4\right)\left(2\right)$

## Solution 10 (Braindead solution)
List out 1 to 16:
\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16.\]
First, we remove all numbers that appear an even amount of times in the product:
\[2, 4, 6, 8, 10, 12, 14, 16.\]
Next, we remove all perfect squares:
\[2, 6, 8, 10, 12, 14.\]
Factoring each term gives:
\[2^1, 2^1\cdot 3^1, 2^3, 2^1 \cdot 5^1, 2^2 \cdot 3^1, 2^1 \cdot 7^1.\]
We multiply all the terms together and remove perfect squares to get $2^1 \cdot 5^1 \cdot 7^1 = \boxed{\text{ (C) }70}$ .

## Solution 11
Note that all prime factors must have an even exponent, and that m must be the multiplied equivalent of all odd-exponent prime factors. The only prime numbers appearing are 2, 3, 5, 7, 11, and 13. We can quickly rule out 11 and 13 since they appear 6 and 4 times, respectively. That leaves 2, 3, 5, and 7. We can see that 2 numbers are multiples: 30 and 70. 30 is 2*5*3, 70 is 2*5*7. If we double-check, 3 comes up an even number of times, so our answer is 70. If there is no time left, this method quickly eliminates enough solutions so that guessing could be preferable to leaving it blank.
~Bjartskular457
~Zzzzzzzzzzzzz

## Video Solution 2 by OmegaLearn
https://youtu.be/fB81j1vbwdM

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=sqVY5-h4vfo

## Video Solution 4 by paixiao
https://www.youtube.com/watch?v=EvA2Nlb7gi4&t=238s This video link is invalid now.

## Video Solution
https://youtu.be/eW9eBpalm7I
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by MegaMath
### https://www.youtube.com/watch?v=le0KSx3Cy-gt=28s
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .