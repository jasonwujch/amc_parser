# 2014 AMC 10A Problem 24

## Problem

A sequence of natural numbers is constructed by listing the first $4$ , then skipping one, listing the next $5$ , skipping $2$ , listing $6$ , skipping $3$ , and on the $n$ th iteration, listing $n+3$ and skipping $n$ . The sequence begins $1,2,3,4,6,7,8,9,10,13$ . What is the $500,\!000$ th number in the sequence?

$\textbf{(A)}\ 996,\!506\qquad\textbf{(B)}\ 996,\!507\qquad\textbf{(C)}\ 996,\!508\qquad\textbf{(D)}\ 996,\!509\qquad\textbf{(E)}\ 996,\!510$

## Solution 1
If we list the rows by iterations, then we get
$1,2,3,4$
$6,7,8,9,10$
$13,14,15,16,17,18$ etc.
so that the $500,000$ th number is the $506$ th number on the $997$ th row because $4+5+6+7......+999 = 499,494$ . The last number of the $996$ th row (when including the numbers skipped) is $499,494 + (1+2+3+4.....+996)= 996,000$ , (we add the $1-996$ because of the numbers we skip) so our answer is $996,000 + 506 = \boxed{\textbf{(A) }996,506}$ .
### Note
One may also note we simply need to add the number of skipped numbers to $500,000$ to get our answer. The number of skipped numbers is $\frac{996\cdot 997}{2}$ which has a units digit of $6$ . Looking at the answer choices, it becomes apparent that the answer is $\boxed{\textbf{(A) }996,506}$
~firebolt360

## Note 2 (A little bit of clarification if the solution wasn't entirely clear at the beginning)
Since it looks kind of weird to pick $999$ as the end of the sum, the intuition behind it is that the sum of $n$ terms is $4+5+6+7+...+n+3=\frac{n(n+7)}{2}$ , since \[4+5+6+7+...+n+3\] \[=(1+3)+(2+3)+(3+3)+(4+3)+...+(n-3+3)\] \[=(1+2+3+4+...+n)+3n\] \[=\frac{n(n+1)}{2}+3n\] \[=\frac{n(n+7)}{2}\] Since we want the $500,000$ th number, we can write our equation as an approximation. \[\frac{n(n+7)}{2} \approx 500,000\] \[n(n+7) \approx 1,000,000\] Since $n(n+7) \approx n^2$ , $n^2 \approx 1,000,000$ , meaning $n \approx 1,000$ . $n(n+7)=n^2+7n$ , so $n \approx 1,000$ yields $1,000,000+7,000 \approx 1,000,000$ , prompting us to lower the value of $n$ by around $3$ or $4$ since we want to lower our answer by $7,000$ and the term below $n^2$ is $(n-1)^2$ , which is $2n-1$ lower than $n^2$ . Thus, through a little bit of guess and checking, we get $4+5+6+7+...+999=499,494.$ This is also similar to the Solution 3, the AOPS video transcript.
~Wesserwes7254

## Solution 2
Let's start with natural numbers, with no skips in between.
$1,2,3,4,5,...,500000$
All we need to do is count how many numbers are skipped, $n$ , and "push" (add on to) $500,000$ according to however many numbers are skipped.
Clearly, $\frac{999(1000)}{2}<500,000<\frac{1000(1001)}{2}$ . This means that there are $999-3=996$ skipped number "blocks" in the sequence because we started counting from 4.
Therefore $n=\frac{996(997)}{2}=496,506$ , and the answer is $496,506+500000=\boxed{\textbf{(A) }996,506}$ .

## Solution 3 (AOPS Video Transcript)
First, we group the numbers together in the following way: ${1, 2, 3, 4, (5)}; {6, 7, 8, 9, 10, (11, 12)}; ...$ We quickly realize that the number of terms in the curly braces follow a pattern: $5, 7, 9, 11, ... , n$ (where $n$ is the $n^\text{th}$ block. Now, we can tell that the last number in a curly brace will be the number of terms in the set added to the number of terms in all the previous sets. Luckily for us, odd numbers are easy to add. If we pretend that there was a $1, 3$ at the beginning, then the sum of all of the numbers before and including $n$ is $(n+2)^2$ . However, we have to subtract $1+3$ which results in $n^2+4n$ . The amount of numbers in the parenthesis are the $n^\text{th}$ triangular number or $\frac{n(n+1)}{2}$ . Next, we want to find the greatest $n$ , where $(n^2+4n) - \frac{n(n+1)}{2}<500000$ . Simplifying, we get $n^2+7n<1000000$ . We realize that $n=1000$ results in a number just $7000$ greater than our target. Next, we square $999$ : $(1000 - 1)^2 = 1000000 - 2001$ . As we decrease $n$ by $1$ , we decrease the result of the equation by approximately $2000$ . In order to decrease by at least $7000$ , we have to decrease $4$ times leading to $n=1000-4=996$ . We plug it in to $n^2+4n$ getting $996\cdot1000=996000$ . This is the last number in the $996^\text{th}$ set. The number of terms used is $\frac{n\cdot(n+7)}{2}=\frac{996\cdot1003}{2}=498\cdot1003=498000+1494=499494$ . We need to add $500000-499494=506$ terms to get an answer of $\boxed{\textbf{(A) }996,506}$ .
~MathFun1000

## Solution 4(Answer choices)
We look at each option starting from $A$ . Clearly $500,000 + n(n+1)/2 = 996,506$ where $n$ is the number of the skipped numbers. So we have $n^2 + n - 987,012 = 0$ . This factors as $(n+997)(n-996)$ . Since $n$ is a positive integer the answer is $A$ .
~coolmath_2018, minor edits by Mathman645

## Solution 5 (fast)
We make a list:
$1,2,3,4$ ---> $4$ elements, $1$ st group
$6,7,8,9,10$ ---> $5$ elements, $2$ nd group
...
It becomes apparent that the amount of elements $n$ in the group that the $500,000$ th number is in is the smallest $n$ such that \[\frac{n(n+1)}{2} - 6 >= 500,000\] , which yields $n=1000$ .
This means that the group number $k$ of the $500,000$ th element is $1000-3=997$ (by looking at the pattern from our list).
Notice that the group number of every group is how many numbers will be skipped after the numbers from that group appear. This means that the numbers from $1$ to $996$ are skipped.
It follows that our answer is thus $\frac{996(997)}{2} + 500,000 = 996506$ , yielding $\boxed{A}$
~martianrunner

## Video Solution by Richard Rusczyk
https://www.youtube.com/watch?v=KfGtE4G6tBo
~ dolphin7
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .