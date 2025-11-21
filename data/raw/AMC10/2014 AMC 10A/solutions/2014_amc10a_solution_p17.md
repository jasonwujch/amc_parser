# 2014 AMC 10A Problem 17

## Problem

Three fair six-sided dice are rolled. What is the probability that the values shown on two of the dice sum to the value shown on the remaining die?

$\textbf{(A)}\ \dfrac16\qquad\textbf{(B)}\ \dfrac{13}{72}\qquad\textbf{(C)}\ \dfrac7{36}\qquad\textbf{(D)}\ \dfrac5{24}\qquad\textbf{(E)}\ \dfrac29$

## Solution 1
First, we note that there are $1, 2, 3, 4,$ and $5$ ways to get sums of $2, 3, 4, 5, 6$ respectively--this is not too hard to see. With any specific sum, there is exactly one way to attain it on the other die. This means that the probability that two specific dice have the same sum as the other is \[\dfrac16 \left( \dfrac{1+2+3+4+5}{36}\right) = \dfrac{5}{72}.\] Since there are $\dbinom31$ ways to choose which die will be the one with the sum of the other two, our answer is $3 \cdot \dfrac{5}{72} = \boxed{\textbf{(D)} \: \dfrac{5}{24}}$ .

## Solution 2 (Bashy)
$(1, 2, 3); (1, 3, 4); (1, 4, 5); (1, 5, 6); (2, 3, 5); (2, 4, 6)$ have $6$ ways to rearrange them for a total of $36$ ways. $(1, 1, 2); (2, 2, 4); (3, 3, 6)$ have $3$ ways to rearrange them for a total of $9$ ways. Adding them up, we get $45$ ways. We have to divide this values by $6^3$ because there are 3 dice. $\dfrac{45}{216}=\boxed{\dfrac{5}{24}}$ .
~MathFun1000

## Solution 3 (Summary of Solution 2)
Start by listing all possible sums. Then find the ways to arrange them and sum them up and divide by $6^3$ for 3 dice. $\dfrac{45}{216}$ is $\boxed{\textbf{(D)} \: \dfrac{5}{24}}$ .
-aopspandy

## Solution 4 (enumeration and casework)
There are $3$ ways to pick the dice which is the sum. From here proceed with "casework":
- If the sum is 1, there are $0$ ways because the minimum sum is $2$ .
- If the sum is 2, there is $1$ way (namely $(1, 1)$ ).
- If the sum is 3, there are $2$ ways (namely $(1, 2)$ and $(2, 1)$ ).
- If the sum is 4, there are $3$ ways (namely $(1, 3)$ , $(3, 1)$ , and $(2, 2)$ ).
We start noticing that for a sum of $n$ there are $n-1$ cases, but let's keep going to verify.
- If the sum is 5, there are $4$ ways (namely $(1, 4)$ , $(4, 1)$ , $(2, 3)$ , and $(3, 2)$ ).
- If the sum is 6, there are $5$ ways (namely $(1, 5)$ , $(5, 1)$ , $(2, 4)$ , $(4, 2)$ , and $(3, 3)$ ).
We have exhausted all cases because there is no way a dice can roll a $7$ . Summing, there are 15 ways here. To summarize: there are $3$ ways to pick the dice that is the sum, and $15$ ways to achieve the sum, for a total of $45$ configurations. There are $6\cdot6\cdot6=216$ total configurations, and the probability is $\frac{45}{216}=\frac{5}{24} \Longrightarrow \boxed{\textbf{(D)} \frac{5}{24}}$ .
~JH. L

## Video Solution by OmegaLearn
https://youtu.be/5UojVH4Cqqs?t=702
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .