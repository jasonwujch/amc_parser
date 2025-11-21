# 2024 AMC 8 Problem 13

## Problem

Buzz Bunny is hopping up and down a set of stairs, one step at a time. In how many ways can Buzz Bunny start on the ground, make a sequence of $6$ hops, and end up back on the ground? (For example, one sequence of hops is up-up-down-down-up-down.)

![](https://wiki-images.artofproblemsolving.com//f/f1/2024-AMC8-q13.png)

$\textbf{(A)}\ 4 \qquad \textbf{(B)}\ 5 \qquad \textbf{(C)}\ 6 \qquad \textbf{(D)}\ 8 \qquad \textbf{(E)}\ 12$

## Solution 1
Looking at the answer choices, you see that you can list them out. Doing this gets you:
$\mathit{UUDDUD}$
$\mathit{UDUDUD}$
$\mathit{UUUDDD}$
$\mathit{UDUUDD}$
$\mathit{UUDUDD}$
Counting all the paths listed above gets you $\boxed{\textbf{(B)} \ 5}$ .
~ALWAYSRIGHT11

## Solution 2
Any combination can be written as some re-arrangement of $\mathit{UUUDDD}$ . Clearly we must end going down, and start going up, so we need the number of ways to insert 2 $U$ 's and 2 $D$ 's into $U\, \_ \, \_ \, \_ \, \_ \, D$ . There are ${4\choose 2}=6$ ways, but we have to remove the case $\mathit{UDDUUD}$ , giving us $\boxed{\textbf{(B)}\ 5}$ .
- We know there are no more cases since there will be at least one $U$ before we have a $D$ (from the first $U$ ), at least two $U$ 'S before two $D$ 's (since we removed the one case), and at least three $U$ 's before three $D$ 's, as we end with the third $D$ .
~Sahan Wijetunga

## Solution 3
These numbers are clearly the Catalan numbers. Since we have $6$ steps, we need the third Catalan number, which is $\boxed{\textbf{(B)}\ 5}$ . ~andliu766

## Solution 4
The first step must be a U, last step must be a D. After the third step we can get only position 3 or position 1. In the first case there is only one way: UUUDDD. In the second case we have two way to get this position UDU and UUD. Similarly, we have two way return to position 0 (UDD and DUD). Therefore, we have $1 + 2 \cdot 2 = \boxed{\textbf{(B)}\ 5}$ .

## Solution 5 (Complementary Counting)
We can find the total cases then deduct the ones that don't work.
Let $U$ represent "Up" and $D$ represent "Down". We know that in order to land back at the bottom of the stairs, we must have an equal number of $U$ 's and $D$ 's, therefore six hops means $3$ of each.
The number of ways to arrange $3$ $U$ 's and $3$ $D$ 's is $\dfrac{6!}{(3!)^2}=\dfrac{720}{36}=20$ .
Case $1$ : Start with $\mathit D$
Case $2$ : Start with $\mathit{UDD}$
Case $3$ : Start with $\mathit{UUDDD}$
Case $4$ : Start with $\mathit{UDUDD}$
Case $1$ is asking us how many ways there are to arrange $3$ $U$ 's and $2$ $D$ 's, which is $\dfrac{5!}{3!2!}=\dfrac{120}{12}=10$ .
Case $2$ is asking us how many ways there are to arrange $2$ $U$ 's and $1$ $D$ , which is $\dfrac{3!}{2!1!}=\dfrac{6}{2}=3$ .
Case $3$ is asking us how many ways there are to arrange $1$ $U$ , which is $1$ .
Case $4$ is asking us the same thing as Case $3$ , giving us $1$ .
Therefore, deducting all cases from $20$ gives $20-10-3-1-1=\boxed{\textbf{(B)}\,5}$ .
~Tacos_are_yummy_1
### Video by MathTalks😉
https://youtu.be/qAwRUj2N46c?si=QDUY8ZUVFP29Eg4c

## Video Solution 1
https://youtu.be/BaE00H2SHQM?si=GTocuz7rsKFCrPn3&t=2986 ~Math-X

## Video Solution 2 by Central Valley Math Circle(Goes through the full thought process)
https://youtu.be/aMmHkyEOmAc ~mr_mathman

## Video Solution 3 (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=n9jyl0QHXLbaKz3I&t=1363
~hsnacademy

## Video Solution 4 by OmegaLearn.org
https://youtu.be/dM1wvr7mPQs

## Video Solution 5 (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc ~NiuniuMaths

## Video Solution 6 Interstigation
https://youtu.be/ktzijuZtDas&t=1238

## Video Solution 7 Dr. David
https://youtu.be/r3FtOOYEces

## Video Solution 8 WhyMath
https://youtu.be/6Bg0Z0jcInw

## Video Solution 9 (30-Second Rearrangement + 2 other methods)
https://www.youtube.com/watch?v=WhuMrsxkf70 ~TheMathGeek

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/qJqrFauo3lQ
~Thesmartgreekmathdude
### See Also