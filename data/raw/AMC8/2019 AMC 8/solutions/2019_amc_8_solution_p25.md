# 2019 AMC 8 Problem 25

## Problem

Alice has $24$ apples. In how many ways can she share them with Becky and Chris so that each of the three people has at least two apples?

$\textbf{(A) }105\qquad\textbf{(B) }114\qquad\textbf{(C) }190\qquad\textbf{(D) }210\qquad\textbf{(E) }380$

## Solution 1 (Stars and Bars/Sticks and Stones)
Note: This solution uses the non-negative version for stars and bars. A solution using the positive version of stars is similar (first removing an apple from each person instead of 2).
This method uses the counting method of stars and bars (non-negative version). Since each person must have at least $2$ apples, we can remove $2*3$ apples from the total that need to be sorted. With the remaining $18$ apples, we can use stars and bars to determine the number of possibilities. Assume there are $18$ stars in a row, and $2$ bars, which will be placed to separate the stars into groups of $3$ . In total, there are $18$ spaces for stars $+ 2$ spaces for bars, for a total of $20$ spaces. We can now do $20 \choose 2$ . This is because if we choose distinct $2$ spots for the bars to be placed, each combo of $3$ groups will be different, and all apples will add up to $18$ . We can also do this because the apples are indistinguishable. $20 \choose 2$ is $190$ , therefore the answer is $\boxed{\textbf{(C) }190}$ .
~goofytaipan91

## Solution 2 (Answer Choices)
Consider an unordered triple $(a,b,c)$ where $a+b+c=24$ and $a,b,c$ are not necessarily distinct. Then, we will either have $1$ , $3$ , or $6$ distinguishable ways to assign $a$ , $b$ , and $c$ to Alice, Becky, and Chris. Thus, our answer will be $x+3y+6z$ for some nonnegative integers $x,y,z$ . Notice that we only have $1$ way to assign the numbers $a,b,c$ to Alice, Becky, and Chris when $a=b=c$ . As this only happens $1$ way ( $a=b=c=8$ ), our answer is $1+3y+6z$ for some $y,z$ . Finally, notice that this implies the answer is $1$ mod $3$ . The only answer choice that satisfies this is $\boxed{\textbf{(C) }190}$ .
-BorealBear

## Solution 3
Since each person needs to have at least two apples, we can simply give each person two, leaving $24 - 2\times3=18$ apples. For the remaining apples, if Alice is going to have $a$ apples, Becky is going to have $b$ apples, and Chris is going to have $c$ apples, we have indeterminate equation $a+b+c=18$ . Currently, we can see that $0 \leq a\leq 18$ where $a$ is an integer, and when $a$ equals any number in the range, there will be $18-a+1=19-a$ sets of values for $b$ and $c$ . Thus, there are $19 + 18 + 17 + \cdots + 1 = \boxed{\textbf{(C) }190}$ possible sets of values in total.
~ Bloggish

## Video Solution by Math-X (Let's review stars and bars together first!!!)
https://youtu.be/IgpayYB48C4?si=SzBgzW4jHelkYwP1&t=8105
~Math-X

## Video Solution by OmegaLearn
https://youtu.be/5UojVH4Cqqs?t=5131
~ pi_is_3.14

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1

## Video Solutions
https://www.youtube.com/watch?v=EJzSOPXULBc
- Happytwin
https://www.youtube.com/watch?v=wJ7uvypbB28
https://www.youtube.com/watch?v=2dBUklyUaNI
https://www.youtube.com/watch?v=3qp0wTq-LI0&list=PLLCzevlMcsWNBsdpItBT4r7Pa8cZb6Viu&index=7
~ MathEx
https://youtu.be/8kzjB60pBrA
~savannahsolver