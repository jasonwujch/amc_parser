# 2005 AMC 10B Problem 25

## Problem

A subset $B$ of the set of integers from $1$ to $100$ , inclusive, has the property that no two elements of $B$ sum to $125$ . What is the maximum possible number of elements in $B$ ?

$\textbf{(A) } 50 \qquad \textbf{(B) } 51 \qquad \textbf{(C) } 62 \qquad \textbf{(D) } 65 \qquad \textbf{(E) } 68$

## Solution 1
The question asks for the maximum possible number of elements. The integers from $1$ to $24$ can be included because you cannot make $125$ with integers from $1$ to $24$ without the other number being greater than $100$ . The integers from $25$ to $100$ are left. They can be paired so the sum is $125$ : $25+100$ , $26+99$ , $27+98$ , $\ldots$ , $62+63$ . That is $38$ pairs, and at most one number from each pair can be included in the set. The total is $24 + 38 = \boxed{\textbf{(C)}\ 62}$ .
Also, it is possible to see that since the numbers $1$ to $24$ are in the set there are only the numbers $25$ to $100$ to consider. As $62+63$ gives $125$ , the numbers $25$ to $62$ can be put in subset $B$ without having two numbers add up to $125$ . In this way, subset $B$ will have the numbers $1$ to $62$ , and so the answer is $\boxed{\textbf{(C)}\ 62}$ .

## Solution 1 Alternate Solution
Since there are $38$ numbers that sum to $125$ , there are $100-38=62$ numbers not summing to $125.$ ~mathboy282

## Solution 2 (If you have no time)
"Cut" $125$ into half. The maximum integer value in the smaller half is $62$ . Thus the answer is $\boxed{\textbf{(C)}\ 62}$ .

## Solution 3
The maximum possible number of elements includes the smallest numbers. So, subset $B = \{1,2,3....n-1,n\}$ where n is the maximum number of elements in subset $B$ . So, we have to find two consecutive numbers, $n$ and $n+1$ , whose sum is $125$ . Setting up our equation, we have $n+(n+1) = 2n+1 = 125$ . When we solve for $n$ , we get $n =\boxed{\textbf{(C)}\ 62}$ .
~GentleTiger

## Solution 4
We can put all odd numbers into subset B, or we can put all even numbers into subset B, so now there are 50 numbers in the set. I will use all even numbers in this solution. Now, we need to add other odd(or even!) numbers possible in this subset, which is all odd(or even) numbers that can be added so that the sum with 100(or 99) plus the biggest possible odd number(or even) to get 123. This will get us the numbers 1,3,5...21,23(or numbers 2,4,6...22,24), which gives us 12 more numbers, and adding that to the 50 original numbers, we get $B =\boxed{\textbf{(C)}\ 62}$ .

## Video Solution
https://www.youtube.com/watch?v=3fE_rveF_n0 ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .