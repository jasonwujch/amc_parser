# 2023 AMC 10B Problem 11

## Problem

Suzanne went to the bank and withdrew $\$800$ . The teller gave her this amount using $\$20$ bills, $\$50$ bills, and $\$100$ bills, with at least one of each denomination. How many different collections of bills could Suzanne have received?

$\textbf{(A) } 45 \qquad \textbf{(B) } 21 \qquad \text{(C) } 36 \qquad \text{(D) } 28 \qquad \text{(E) } 32$

## Solution 1
We let the number of $\$20$ , $\$50$ , and $\$100$ bills be $a,b,$ and $c,$ respectively.
We are given that $20a+50b+100c=800.$ Dividing both sides by $10$ , we see that $2a+5b+10c=80.$
We divide both sides of this equation by $5$ : $\dfrac25a+b+2c=16.$ Since $b+2c$ and $16$ are integers, $\dfrac25a$ must also be an integer, so $a$ must be divisible by $5$ . Let $a=5d,$ where $d$ is some positive integer.
We can then write $2\cdot5d+5b+10c=80.$ Dividing both sides by $5$ , we have $2d+b+2c=16.$ We divide by $2$ here to get $d+\dfrac b2+c=8.$ $d+c$ and $8$ are both integers, so $\dfrac b2$ is also an integer. $b$ must be divisible by $2$ , so we let $b=2e$ .
We now have $2d+2e+2c=16\implies d+e+c=8$ . Every substitution we made is part of a bijection (i.e. our choices were one-to-one); thus, the problem is now reduced to counting how many ways we can have $d,e,$ and $c$ such that they add to $8$ .
We still have another constraint left, that each of $d,e,$ and $c$ must be at least $1$ . For $n\in\{d,e,c\}$ , let $n'=n-1.$ We are now looking for how many ways we can have $d'+e'+c'=8-1-1-1=5.$
We use a classic technique for solving these sorts of problems: stars and bars. We have $5$ stars and $3$ groups, which implies $2$ bars. Thus, the total number of ways is $\dbinom{5+2}2=\dbinom72=21.$
~Technodoggo ~minor edits by lucaswujc

## Solution 2
Denote by $x$ , $y$ , $z$ the amount of \$20 bills, \$50 bills and \$100 bills, respectively. Thus, we need to find the number of tuples $\left( x , y, z \right)$ with $x, y, z \in \Bbb N$ that satisfy \[ 20 x + 50 y + 100 z = 800. \]
First, this equation can be simplified as \[ 2 x + 5 y + 10 z = 80. \]
Second, we must have $5 |x$ . Denote $x = 5 x'$ . The above equation can be converted to \[ 2 x' + y + 2 z = 16 . \]
Third, we must have $2 | y$ . Denote $y = 2 y'$ . The above equation can be converted to \[ x' + y' + z = 8 . \]
Denote $x'' = x' - 1$ , $y'' = y' - 1$ and $z'' = z - 1$ . Thus, the above equation can be written as \[ x'' + y'' + z'' = 5 . \]
Therefore, the number of non-negative integer solutions $\left( x'', y'', z'' \right)$ is $\binom{5 + 3 - 1}{3 - 1} = \boxed{\textbf{(B) 21}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3
To start, we simplify things by dividing everything by $10$ , the resulting equation is $2x+5y+10z=80$ , and since the problem states that we have at least one of each, we simplify this to $2x+5y+10z=63$ . Note that since the total is odd, we need an odd number of $5$ dollar bills. We proceed using casework.
Case 1: One $5$ dollar bill
$2x+10z=58$ , we see that $10z$ can be $0,10,20,30,40,50$ or $6$ ways
Case 2: Three $5$ dollar bills
$2x+10z=48$ , like before we see that $10z$ can be $0,10,20,30,40$ , so $5$ ways
Now we should start to see a pattern emerge, each case there is $1$ less way to sum to $80$ , so the answer is just $\frac{6(6+1)}{2}=\boxed{\textbf{(B)}~21}$ .
~andyluo

## Solution 4
We notice that each \$100 can be split 3 ways: 5 \$20 dollar bills, 2 \$50 dollar bills, or 1 \$100 dollar bill.
There are 8 of these \$100 chunks in total--take away 3 as each split must be used at least once.
Now there are five left--so we use stars and bars.
5 chunks, 3 categories or 2 bars. This gives us $\binom{5+2}{2}=\boxed{\textbf{(B) 21}}$
~not_slay

## Solution 5 (generating functions)
The problem is equivalent to the number of ways to make $\$80$ from $\$2$ bills, $\$5$ bills, and $\$10$ bills. We can use generating functions to find the coefficient of $x^{80}$ :
The $\$2$ bills provide $1+x^2+x^4+x^6 \cdots = \frac{1}{1-x^2},$
The $\$5$ bills provide $1+x^5+x^{10}+x^{15} \cdots = \frac{1}{1-x^5},$
The $\$10$ bills provide $1+x^{10}+x^{20}+x^{30} \cdots = \frac{1}{1-x^{10}}.$
Multiplying, we get $(1-x^{2})^{-1}(1-x^{5})^{-1}(1-x^{10})^{-1}.$

## Solution 6 (easy logic)
There aren't dollar signs because the $latex$ thinks they're latex symbols. If you find how to override this error, please edit this. There's no $latex$ here but feel free to add some! ~SwordAxe
We can see in the problem that the teller gave her at least one of $\$20$ , $\$50$ , and $\$100$ . Therefore, she has 800 - 20 - 50 - 100 = 630 "left over".
Since all bills and 630 are multiples of 10, we can divide by ten. ==> Question becomes: How many different collections of 2, 5, and 10 could she get if her total was 63?
We notice that because 63 is odd, we need an odd amount of 5 bills. (2 and 10 are both even, and 63 is not a multiple of 5, so we need 2 and/or 10 bills. PM SwordAxe if you don't get this.)
We can do casework.
1: She gets one 5 (50) dollar bill. She has 58 (580) left.
This looks very tedious, but draw a simple tree diagram, and you'll see that its very easy!
If she gets one 50, there are 6 ways If she gets three 50, there are 5 ways ... If she gets nine 50, there are 2 ways If she gets eleven 50, there is one way
We can add them all up, with a grand sum of 6+5+4+3+2+1 = 21.
Therefore, we get the answer (B) 21.
~SwordAxe (PM me if you have any questions! :)) EDIT: use /$ for the dollar signs
\documentclass{article} \usepackage{amsmath, amssymb} \usepackage{amsthm} \usepackage{enumitem} \usepackage{tcolorbox} % Package to box the final answer \begin{document}

## Solution 7
Because the problem states that at least one of each type of bill must be used, we can subtract 20,50, and 100 from 800, giving us 630. Let the new amount of 20 bills be x, 50 bills be y, and 100 bills be z. Notice that there must be more than one type of bill used, as 630 cannot be made from just 20, 50, or 100. Now, we can do the casework.
Case 1: Uses 20 and 50
Case 2: 50 and 100
Case 3: 20 and 100
Case 4: 20, 50, and 100
In total, for Case 4, there is 5+4+3+2+1 = 15 solutions. Thus, in total, there are 6 + 15 = $\boxed{\textbf{(B) 21}}$ solutions.
~DUODUOLUO

## Video Solution 1 by OmegaLearn
https://youtu.be/UeX3eEwRS9I

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=sfZRRsTimmE

## Video Solution 3 by paixiao
https://youtu.be/EvA2Nlb7gi4?si=fVLG8gMTIC5XkEwP&t=89s This video link is invalid now.

## Video Solution 4
https://youtu.be/D-ZvFBiZsaY
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution 5 by Lucas637
https://www.youtube.com/watch?v=kXLHjclTD44&t=27s