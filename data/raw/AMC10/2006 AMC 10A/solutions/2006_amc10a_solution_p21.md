# 2006 AMC 10A Problem 21

## Problem

How many four-digit positive integers have at least one digit that is a $2$ or a $3$ ?

$\textbf{(A) } 2439\qquad\textbf{(B) } 4096\qquad\textbf{(C) } 4903\qquad\textbf{(D) } 4904\qquad\textbf{(E) } 5416$

## Video Solution
https://youtu.be/0W3VmFp55cM?t=3291
~ pi_is_3.14

## Solution 1 (Complementary Counting)
Since we are asked for the number of positive $4$ -digit integers with at least $2$ or $3$ in it, we can find this by finding the total number of $4$ -digit integers and subtracting off those which do not have any $2$ s or $3$ s as digits.
The total number of $4$ -digit integers is $9 \cdot 10 \cdot 10 \cdot 10 = 9000$ , since we have $10$ choices for each digit except the first (which can't be $0$ ).
Similarly, the total number of $4$ -digit integers without any $2$ or $3$ is $7 \cdot 8 \cdot 8 \cdot 8 ={3584}$ .
Therefore, the total number of positive $4$ -digit integers that have at least one $2$ or $3$ is $9000-3584=\boxed{\textbf{(E) }5416}.$

## Solution 2 (Casework)
We proceed to every case.
Case $1$ : There is ONLY one $2$ or $3$ . If the $2$ or $3$ is occupying the first digit, we have $512$ arrangements. If the $2$ or $3$ is not occupying the first digit, there are $7 \cdot 8^2$ = $448$ arrangements. Therefore, we have $2(448 \cdot 3 + 512) = 3712$ arrangements.
Case $2$ : There are two $2$ s OR two $3$ s. If the $2$ or $3$ is occupying the first digit, we have $64$ arrangements. If the $2$ or $3$ is not occupying the first digit, there are $56$ arrangements. There are $3$ ways for the $2$ or the $3$ to be occupying the first digit and $3$ ways for the first digit to be unoccupied. There are $2(3 \cdot (56+64))$ = $720$ arrangements.
Case $3$ : There is ONLY one $2$ and one $3$ . If the $2$ or the $3$ is occupying the first digit, we have $6$ types of arrangements of where the $2$ or $3$ is. We also have $64$ different arrangements for the non- $2$ or $3$ digits. We have $6 \cdot 64$ = $384$ arrangements. If the $2$ or the $3$ isn't occupying the first digit, we have $6$ types of arrangements of where the $2$ or $3$ is. We also have $56$ different arrangements for the non- $2$ or $3$ digits. We have $6 \cdot 56$ = $336$ arrangements for this case. We have $336 + 384$ = $720$ total arrangements for this case.
Notice that we already counted $3712 + 720 + 720 = 5152$ cases and we still have a lot of cases left over to count. This is already larger than the second largest answer choice, and therefore, our answer is $\boxed{\textbf{(E) }5416}$ .
~Arcticturn
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .