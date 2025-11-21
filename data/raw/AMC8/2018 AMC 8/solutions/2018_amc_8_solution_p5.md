# 2018 AMC 8 Problem 5

## Problem

What is the value of $1+3+5+\cdots+2017+2019-2-4-6-\cdots-2016-2018$ ?

$\textbf{(A) }-1010\qquad\textbf{(B) }-1009\qquad\textbf{(C) }1008\qquad\textbf{(D) }1009\qquad \textbf{(E) }1010$

## Solution 1
Rearranging the terms, we get $(1-2)+(3-4)+(5-6)+...(2017-2018)+2019$ , and our answer is $-1009+2019=\boxed{\textbf{(E) }1010}$ .
If you were stuck on this problem, refer to AOPS arithmetic lessons.
~Nivaar

## Solution 2
We can see that the last numbers of each of the sets (even numbers and odd numbers) have a difference of two. So, do the second last ones and so on. Now, all we need to find is the number of integers in any of the sets (I chose even) to get $\boxed{\textbf{(E) }1010}$ .
~avamarora

## Solution 3
It is similar to the Solution 1: Rearranging the terms, we get $1+(3-2)+(5-4)+(6-5)...(2017-2016)+(2019-2018)$ , and our answer is $1+1009=\boxed{\textbf{(E) }1010}$ .
~LarryFlora

## Solution 4
Note that the sum of consecutive odd numbers can be expressed as a square, namely $1+3+5+7+...+2017+2019 = 1010^2$ . We can modify the negative numbers in the same way by adding 1 to each negative term, factoring a negative sign, and accounting for the extra 1's by subtracting 1009. We then have $1010^2-1009^2-1009$ . Using difference of squares, we obtain $(1010+1009)(1010-1009)-1009 = 2019-1009 = \boxed{1010}$ .
~SigmaPiE

## Solution 5
The sum of odd numbers can be represented as the number of consecutive odds starting from one, squared. Since 2019 is (2019+1)/2, there are 1010 odd numbers. Therefore, the sum of the odd numbers is \[1010^2 \quad \text{or} \quad 1010 \times 1010.\]
The sum of even numbers up to 2018 is calculated by noting that there are 2018/2 = 1009 even numbers. Using the formula for the sum of the first n even numbers, n(n+1), we get \[1009 \times (1009+1) \quad \text{or} \quad 1009 \times 1010.\]
The difference between these two sums is \[1010 \times 1010 - 1009 \times 1010 = 1010.\]
Thus, the correct answer is $-1009+2019=\boxed{\textbf{(E) }1010}$ .

## Video Solution (CRITICAL THINKING!!!)
https://youtu.be/uMo2Jlbm7WY
~Education, the Study of Everything

## Video Solution
https://youtu.be/ykNMFdRMd0o
~savannahsolver
==See Also== y