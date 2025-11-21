# 2025 AMC 10B Problem 3

## Problem

A Pascal-like triangle has $10$ as the top row and $10$ followed by $1$ as the second row. In each subsequent row the first number is $10$ , the last number is $1$ , and, as in the standard Pascal Triangle, each other in the row is the sum of the two numbers directly above it. The first four rows are shown below. \[\large{10}\] \[\large{10}\qquad\large{1}\] \[\large{10}\qquad\large{11}\qquad\large{1}\] \[\large{10}\qquad\large{21}\qquad\large{12}\qquad\large{1}\] What is the sum of the digits of the sum of the numbers in the 11th row?

$\textbf{(A) } 11 \qquad\textbf{(B) } 13 \qquad\textbf{(C) } 14 \qquad\textbf{(D) } 16 \qquad\textbf{(E) } 17$

## Solution 1
If we find the sum for each rows, I'll only do the first 5, we find that row 1 has sum $10$ , row 2 has sum $11$ , row 3 has sum $22$ , row 4 has sum $44$ , and row 5 has sum $88$ . we can see that excluding the first row each row has sum $11*2^{n-2}$ where $n$ is the row. This means the 11th row will have sum $11*2^9=11*512=5632$ . The sum of the digits of $5632$ is $16$ , so the answer is $\boxed{\textbf{(D) }16}$ .
~ToxicWaste
### Why each row is twice the previous row
Notice that the sum of each row is the slightly different than the normal Pascal's triangle, so the sum of the numbers is similar. Here's a proof of why each number in the normal Pascal's triangle is twice the previous number. To prove that the sum of each row is $2$ times the previous row, use the equation ${(1+1)}^n$ with the normal Pascal's triangle and use the binomial theorem from there.
Example: In the fifth row of Pascal's triangle, the numbers are $1, 4, 6, 4, 1$ . The first number can be represented by ${4 \choose 0} = 1$ , the second by ${4 \choose 1} = 4$ , the third by ${4 \choose 2} = 6$ , the fourth by ${4 \choose 3} = 4$ , and the last by ${4 \choose 4} = 1$ . The sum of these five numbers is $16$ which is also $2^{4}$ . Using the binomial theorem with ${(1+1)}^4$ , we get $1 + 4 + 6 + 4 + 1 = 16$ , the same results in Pascal's triangle. We could also solve ${(1+1)}^4$ by converting it to $2^4 = 16$ , proving the identity that all rows in Pascal's triangle are exactly twice the previous row and can be represented by $2^{n}$ .
~Bros1 (original writer of this on AMC10B #19)

## Solution 2
In this Pascal's Triangle-like sequence, after row 2, each number in row $x$ applies twice to row $x+1$ . The numbers in row 2 are $10$ and $1$ , and these numbers each apply twice to the next row ( $10, 10+1$ , and $1$ are the numbers in row 3, which can be rewritten as $10*2+1*2$ .) With this pattern, we know that after row 2 the sum of the numbers doubles, and proceed with Solution 1's continuation to get $\boxed{\textbf{(D) }16}$ .
~Akang11

## Solution 3 (BRUTE FORCE!!!)
We can write out the first $11$ rows with direct computation. Since no calculators are allowed, you will spend at least 5 minutes on this problem, so I do not recommend this way. Here are the first $11$ rows.
\[10\] \[10\qquad 1\] \[10\qquad 11\qquad 1\] \[10\qquad 21\qquad 12\qquad 1\] \[10\qquad 31\qquad 33\qquad 13\qquad 1\] \[10\qquad 41\qquad 64\qquad 46\qquad 14\qquad 1\] \[10\qquad 51\qquad 105\qquad 110\qquad 60\qquad 15\qquad 1\] \[10\qquad 61\qquad 156\qquad 215\qquad 170\qquad 75\qquad 16\qquad 1\] \[10\qquad 71\qquad 217\qquad 371\qquad 385\qquad 245\qquad 91\qquad 17\qquad 1\] \[10\qquad 81\qquad 288\qquad 588\qquad 756\qquad 630\qquad 336\qquad 108\qquad 18\qquad 1\] \[10\qquad 91\qquad 369\qquad 876\qquad 1344\qquad 1386\qquad 966\qquad 444\qquad 126\qquad 19\qquad 1\]
Summing the last row gives $10+91+369+876+1344+1386+966+444+126+19+1 = 5632$ . Summing the digits of $5632$ gives $5+6+3+2 = \boxed{\textbf{(D) } 16}$ .
Edit: After brute forcing two or three lines, it is clear that the number doubles ( $11, 22, 44, 88$ ...), and you can use this to find $5632$ which gives $5+6+3+2 = \boxed{\textbf{(D) } 16}$ .
~JerryZYang
~Sumeete(Small edit)

## Solution 4 (Fast)
We can just take the entire triangle modulo $9$ since all the answer choices have different modulo $9$ and because a number is congruent to the sum of the digits of it mod $9$ . Thus, since $10\cong1$ (mod $9$ ) it just becomes Pascal's triangle, and the sum of the elements on the 11th row is $2^{11-1}=1024$ , and since $1024\cong7$ (mod $9$ ), the only feasible answer choice is $16$ since it is the only answer choice that is $7$ mod $9$ , thus the answer is $\boxed{\textbf{(D) } 16}$ ~Irfans123

## Solution 5 (Cheese, Gamble)
We can start brute forcing the first few rows and figure out the pattern that for row $n$ where $n$ is a natural number, the sum of the numbers in row $n$ is $11(2^{n-2})$ . Now we gamble on this pattern (which is mostly correct for AMC 10 problems) and plug in $11$ into $n$ which results in $5632$ as the sum of all the numbers in that row. Thus, the answer is $5 + 6 + 3 + 2 = \boxed{\textbf{D) }16}$
~ROGER8432V3

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=jNrsFzY3ndg
~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution by Daily Dose of Math
https://youtu.be/s-Wimgu9wto
~Thesmartgreekmathdude
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .