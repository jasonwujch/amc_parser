# 2009 AMC 8 Problem 22

## Problem

How many whole numbers between 1 and 1000 do not contain the digit 1?

$\textbf{(A)}\ 512 \qquad \textbf{(B)}\ 648 \qquad \textbf{(C)}\ 720 \qquad \textbf{(D)}\ 728 \qquad \textbf{(E)}\ 800$

## Solution (Super Fast!)
Note that this is the same as finding how many numbers with up to three digits do not contain 1.
Since there are 10 total possible digits, and only one of them is not allowed (1), each place value has its choice of 9 digits, for a total of $9*9*9=729$ such numbers. However, we overcounted by one; 0 is not between 1 and 1000, so there are $\boxed{\textbf{(D)}\ 728}$ numbers.
Note: As stated above, 020 is equivalent to 20, but 000 is not between 1 and 1000.

## Solution 2 (Easy Casework)
We consider the 3 cases, where the number is 1,2 or 3 digits.
Case 1 : The number has a $1$ digit. Well, 1-9 all work except for $1$ , so $9-1=8$ numbers, for numbers that are 1 digit.
Case 2 : The number is has $2$ digits. Consider the two digit number. Since the tens digit can't be 0 or 1, we have 8 choices for the tens digit. For the ones digit, we have 9, since the ones digit can't be a 1. This gives us a total of $8*9=72$ two-digit numbers.
Case 3 : The number has $3$ digits. Using similar logic to Case 2, we have 8*9*9 choices for the third number.
We add the cases up getting $648+72+8$ which gives us $\framebox{(D) 728}$ numbers total.
### See Also