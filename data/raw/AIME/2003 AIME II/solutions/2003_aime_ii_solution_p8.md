# 2003 AIME II Problem 8

## Problem

Find the eighth term of the sequence $1440,$ $1716,$ $1848,\ldots,$ whose terms are formed by multiplying the corresponding terms of two arithmetic sequences.

## Solution 0.67
If you multiply the corresponding terms of two arithmetic sequences, you get the terms of a quadratic function. Thus, we have a quadratic $ax^2+bx+c$ such that $f(1)=1440$ , $f(2)=1716$ , and $f(3)=1848$ . Plugging in the values for x gives us a system of three equations:
$a+b+c=1440$
$4a+2b+c=1716$
$9a+3b+c=1848$
Solving gives $a=-72, b=492,$ and $c=1020$ . Thus, the answer is $-72(8)^2+492\cdot8+1020= \boxed{348}.$

## Solution 1 (faster)
Use the same rationale as in solution 1; instead of using terms $1,2,3$ , we use $-1,0,1$ and solve the $6$ th term.
$a-b+c=1440$
$c=1716$
$a+b+c=1848$
Accordingly we will solve
$a=-72, b=204, c=1716$
$36a+6b+c= \boxed{348}.$
-maxamc

## Solution 2
Setting one of the sequences as $a+nr_1$ and the other as $b+nr_2$ , we can set up the following equalities
$ab = 1440$
$(a+r_1)(b+r_2)=1716$
$(a+2r_1)(b+2r_2)=1848$
We want to find $(a+7r_1)(b+7r_2)$
Foiling out the two above, we have
$ab + ar_2 + br_1 + r_1r_2 = 1716$ and $ab + 2ar_2 + 2br_1 + 4r_1r_2 = 1848$
Plugging in $ab=1440$ and bringing the constant over yields
$ar_2 + br_1 + r_1r_2 = 276$
$ar_2 + br_1 + 2r_1r_2 = 204$
Subtracting the two yields $r_1r_2 = -72$ and plugging that back in yields $ar_2 + br_1 = 348$
Now we find
$(a+7r_1)(b+7r_2) = ab + 7(ar_2 + br_1) + 49r_1r_2 = 1440 + 7(348) + 49(-72) = \boxed{348}$ .

## Solution 3
Let the first sequence be
$A={a+d_1, a + 2d_1, a + 3d_1, \cdots}$
and the second be
$B={b+d_2, b + 2d_2, b + 3d_2, \cdots}$ ,
with $(a+d_1)(b+d_2)=1440$ . Now, note that the $n^{\text{th}}$ term of sequence $A$ is $a+d_1 n$ and the $n^{\text{th}}$ term of $B$ is $b + d_2 n$ . Thus, the $n^{\text{th}}$ term of the given sequence is
$n^2(d_1 + d_2) + n(ad_2 + bd_1) + ab$ ,
a quadratic in $n$ . Now, letting the given sequence be $C$ , we see that
$C_n - C_{n-1} = n^2(d_1 + d_2) + n(ad_2 + bd_1) + ab - (n-1)^2(d_1 + d_2) - (n-1)(ad_2 + bd_1) - ab = n(2d_1 + 2d_2) + ad_2 + bd_1 - d_1 - d_2$ ,
a linear equation in $n$ . Since $C_2 - C_1 = 276$ and $C_3 - C_2 = 132$ , we can see that, in general, we have
$C_n - C_{n-1} = 420 - 144n$ .
Thus, we can easily find
$C_4 - C_3 = -12 \rightarrow C_4 = 1836$ ,
$C_5 - C_4 = -156 \rightarrow C_5 = 1680$ ,
$C_6 - C_5 = -300 \rightarrow C_6 = 1380$ ,
$C_7 - C_6 = -444 \rightarrow C_7 = 936$ , and finally
$C_8 - C_7 = -588 \rightarrow \boxed{C_8 = 348}$ .

## Solution 4(Tedious)
Start by labeling the two sequences:
Sequence 1: $a,a+d_1,a+2d_1,\dots a+(n-1)d_1$ ,
Sequence 2: $b,b+d_2,b+2d_2,\dots b+(n-1)d_2$ .
Additionally, label the sequence given in the problem the function $f$ , such that
$f(1)=1440,f(2)=1716,f(3)=1848$ .
Then,
$f(1)=ab,$
$f(2)=(a+d_1)(b+d_2)=a+ad_2+d_1b+d_1d_2,$
$f(3)=(a+2d_1)(b+2d_2)=ab+2ad_2+2bd_1+4d_1d_2,$
and $f(8)=(a+7d_1)(b+7d_2)=ab+7ad_2+7bd_1+49d_1d_2$ .
In order to find $f(8)$ add $f(3)$ enough times to get the difference between the $d_1d_2$ and $ad_2+bd_1$ terms, then add $f(2)$ and $f(1)$ to get the other terms:
$21f(3)=21ab+42ad_2+42bd_1+84d_1d_2$
$21f(3)-35f(2)=21ab+42ad_2+42bd_1+84d_1d_2-35a-35ad_2-35d_1b-35d_1d_2=-14ab+7ad_2+7bd_1+49d_1d_2$
$21f(3)-35f(2)+15f(1)=-14ab+7ad_2+7bd_1+49d_1d_2+15ab=ab+7ad_2+7bd_1+49d_1d_2$
Now that the expression is in terms of the given values, insert values and solve:
$21*1848-35*1716+15*1440=1848+20*132+(20*1716-35*1716+15*1716)+15*(-276)$
$=1848+5*132+15(132-276)$
$=1848+660+15(-144)$
$=348$

## Video Solution by Scholars Foundation
https://youtu.be/Kj0L8jMicOA?si=Dtj0kcosTtX2jki_
These problems are copyrighted © by the Mathematical Association of America.