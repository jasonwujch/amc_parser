# 2024 AMC 8 Problem 16

## Problem

Minh enters the numbers $1$ through $81$ into the cells of a $9 \times 9$ grid in some order. She calculates the product of the numbers in each row and column. What is the least number of rows and columns that could have a product divisible by $3$ ?

$\textbf{(A) } 8\qquad\textbf{(B) } 9\qquad\textbf{(C) } 10\qquad\textbf{(D) } 11\qquad\textbf{(E) } 12$

## Solution 1
Note you can swap/rotate any configuration of rows, such that all the rows and columns that have a product of 3 are in the top left. Hence the points are bounded by a $a \times b$ rectangle. This has $ab$ area and $a+b$ rows and columns divisible by $3$ . We want $ab\ge 27$ and $a+b$ minimized.
If $ab=27$ , we achieve minimum with $a+b=9+3=12$ .
If $ab=28$ ,our best is $a+b=7+4=11$ . Note if $a+b=10$ , $ab=25$ . Because $25<27$ , there is no smaller answer, and we get $\boxed{\textbf{(D)} 11}$ .
- SahanWijetunga ~vockey(minor edits) ~phy6(minor edits)

## Solution 2
For a row or column to have a product divisible by $3$ , there must be a multiple of $3$ in the row or column. To create the least amount of rows and columns with multiples of $3$ , we must find a way to keep them all together, to minimize the total number of rows and columns with multiples of threes in it. From $1$ to $81$ , there are $27$ multiples of $3$ $(81/3 = 27)$ . So we have to fill $27$ cells with numbers that are multiples of $3$ . If we put $25$ of these numbers in a $5 * 5$ grid, there would be $5$ rows and $5$ columns ( $10$ in total), with products divisible by $3$ . However, we have $27$ numbers, so $2$ numbers still need to be put in the $9 * 9$ grid. If we put both numbers in the $6$ th column, but one in the first row, and one in the second row, (next to the $5$ by $5$ grid already filled), we would have a total of $6$ columns now, and still $5$ rows with products that are multiples of $3$ . Since $6 + 5 = 11$ , the answer is $\boxed{\textbf{(D)} 11}$
~goofytaipan (minor edit) DehnTwistNil ~car0t (a few minor edits)

## Solution 3
In the numbers $1$ to $81$ , there are 27 multiples of three. In order to minimize the rows and columns, the best way is to make a square. However, the closest square is $25$ , meaning there are two multiples of three remaining. However, you can place these multiples right above the 5x5 square, meaning the answer is $\boxed{\textbf {(D)} 11}$ ~e Just be better ~Shriyans Chowdhury (minor configuration error)

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/ppeyfN3Fqnw
~mr_mathman

## Video Solution by Math-X (Apply this simple strategy that works every time!!!)
https://youtu.be/BaE00H2SHQM?si=Z4Y7xHZEdRfDR-Bb&t=3952

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=EKPTJZxRQUL6PAoS&t=2017
~hsnacademy
~Math-X

## Video Solution 1 (easy to digest) by Power Solve
https://youtu.be/zxkL4c316vg

## Video Solution 2 by OmegaLearn.org
https://youtu.be/xfiPVmuMiXs ~ Sohil Rathi

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=Svibu3nKB7E

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc
~NiuniuMaths

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=DLzFB4EplKk

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=1709

## Video Solution by Dr. David
https://youtu.be/0kp2LdaCWYw

## Video Solution by WhyMath
https://youtu.be/xtiBWCVHIHY

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also