# 2018 AMC 10A Problem 11

## Problem

When $7$ fair standard $6$ -sided dice are thrown, the probability that the sum of the numbers on the top faces is $10$ can be written as \[\frac{n}{6^{7}},\] where $n$ is a positive integer. What is $n$ ?

$\textbf{(A) }42\qquad \textbf{(B) }49\qquad \textbf{(C) }56\qquad \textbf{(D) }63\qquad \textbf{(E) }84\qquad$

## Solutions

## Solution 1
Add possibilities. There are $3$ ways to sum to $10$ , listed below.
\[4,1,1,1,1,1,1: \dbinom{7}{6} = 7\] \[3,2,1,1,1,1,1: \dbinom{7}{5}\dbinom{2}{1} = 42\] \[2,2,2,1,1,1,1: \dbinom{7}{4} = 35.\]
Add up the possibilities: $35+42+7=\boxed{\textbf{(E) } 84}$ .

## Solution 2
Rolling a sum of $10$ with 7 dice can be represented with stars and bars, with 10 stars and 6 bars. Each star represents one of the dots on the dices' faces and the bars represent separation between different dice. However, we must note that each die must have at least one dot on a face, so there must already be 7 stars predetermined. We are left with 3 stars and 6 bars, which we can rearrange in $\dbinom{9}{3}=\boxed{\textbf{(E) } 84}$

## Solution 3 (overkill)
We can use generating functions, where $(x+x^2+...+x^6)$ is the function for each die. We want to find the coefficient of $x^{10}$ in $(x+x^2+...+x^6)^7$ , which is the coefficient of $x^3$ in $\left(\frac{1-x^7}{1-x}\right)^7$ . This evaluates to $\dbinom{-7}{3} \cdot (-1)^3=\boxed{\textbf{(E) }84}$

## Solution 4 (Stars and Bars)
If we let each number take its minimum value of 1, we will get 7 as the minimum sum. So we can do $10$ - $7$ = $3$ to find the number of balls we need to distribute to get three more added to the minimum to get 10, so the problem is asking how many ways can you put $3$ balls into $7$ boxes. From there we get $\binom{7+3-1}{7-1}=\binom{9}{6}=\boxed{\textbf{(E) }84}$

## Solution 5 (Similar to above, using number separation)
We can use number separation for this problem. If we set each of the dice value to $D\{a, b, c, d, e, f, g, h\}$ , we can say $D = 10$ and each of $D$ 's elements are larger than $0$ . Using the positive number separation formula, which is $\dbinom{n-1}{r-1}$ , we can make the following equations. \begin{align*} D &= 10 \\ a+b+c+d+e+f+g &= 10 \\ \dbinom{10-1}{7-1} &= \\ \dbinom{9}{6} &= \\ \dbinom{9}{3} &= \\ \dfrac{9 \cdot 8 \cdot 7}{3 \cdot 2 \cdot 1} &= \\ 12 \cdot 7 &= \boxed{\textbf{(E) }84} \\ \end{align*}
Note: We are unable to use non-negative number separations due to the fact that the dice *must* be larger than $0$ or positive.
~ Wiselion =)

## Video Solution (HOW TO THINK CREATIVELY!)
https://youtu.be/gTpg8yInCCY
~Education, the Study of Everything

## Video Solution 1
https://youtu.be/HVn1WV80ZIU
~savannahsolver

## Video Solution by OmegaLearn
This video by OmegaLearn explains the solution using two methods: Casework and Stars & Bars .
https://www.youtube.com/watch?v=5UojVH4Cqqs&t=5381s
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .