# 2017 AMC 10A Problem 20

## Problem

Let $S(n)$ equal the sum of the digits of positive integer $n$ . For example, $S(1507) = 13$ . For a particular positive integer $n$ , $S(n) = 1274$ . Which of the following could be the value of $S(n+1)$ ?

$\textbf{(A)}\ 1 \qquad\textbf{(B)}\ 3\qquad\textbf{(C)}\ 12\qquad\textbf{(D)}\ 1239\qquad\textbf{(E)}\ 1265$

## Solution 1
Note that $n \equiv S(n) \pmod{9}$ . This can be seen from the fact that $\sum_{k=0}^{n}10^{k}a_k \equiv \sum_{k=0}^{n}a_k \pmod{9}$ . Thus, if $S(n) = 1274$ , then $n \equiv 5 \pmod{9}$ , and thus $n+1 \equiv S(n+1) \equiv 6 \pmod{9}$ . The only answer choice that satisfies $n+1 \equiv 6 \pmod{9}$ is $\boxed{\textbf{(D)} 1239}$ .

## Solution 2 (Sol. 1 but more detail)
We disregard the case that the sum of $S(N)$ is $0$ because that would indicate that the number must be $0$ itself, which is not allowed. Therefore, every positive integer $N \ge 1$ can be denoted in the modular 9 format with $N \bmod 9$ . Thus we have $S(N) \bmod 9 \). In this case, we have \( S(n) = 1274$ , and therefore we have $S(n) \bmod 9 \equiv 1274 \bmod 9 \equiv 5 \bmod 9$ . Thus, \( S(n+1) \) must be congruent to $6 \bmod 9$ , and the only value that satisfies this is $\boxed{\textbf{(D)}\ 1239}$
~Pinotation

## Solution 3
One divisibility rule that we can use for this problem is that a multiple of $9$ will always have its digits sum to a multiple of $9$ . We can find out that the least number of digits the number $n$ has is $142$ , with $141$ $9$ 's and $1$ $5$ , assuming the rule above. No matter what arrangement or different digits we use, the divisibility rule stays the same. To make the problem simpler, we can just use the $141$ $9$ 's and $1$ $5$ . By randomly mixing the digits up, we are likely to get: $9999$ ... $9995999$ ... $9999$ . By adding $1$ to this number, we get: $9999$ ... $9996000$ ... $0000$ . Knowing that $n+1$ is divisible by $9$ when $6$ , we can subtract $6$ from every available choice, and see if the number is divisible by $9$ afterwards. After subtracting $6$ from every number, we can conclude that $1233$ (originally $1239$ ) is the only number divisible by $9$ . So our answer is $\boxed{\textbf{(D)}\ 1239}$ .

## Solution 4
The number $n$ can be viewed as having some unique digits in the front, following by a certain number of nines. We can then evaluate each potential answer choice.
If $A$ is correct, then $n$ must be some number $99999999...9$ , because when we add one to $99999999...9$ we get $10000000...00$ . Thus, if $1$ is the correct answer, then the equation $9x=1274$ must have an integer solution (i.e. $1274$ must be divisible by $9$ ). But since it does not, $1$ is not the correct answer.
If $B$ is correct, then $n$ must be some number $29999999...9$ , because when we add one to $29999999...9$ , we get $30000000...00$ . Thus, if $3$ is the correct answer, then the equation $2+9x=1274$ must have an integer solution. But since it does not, $3$ is not the correct answer.
Based on what we have done for evaluating the previous two answer choices, we can create an equation we can use to evaluate the final three possibilities. Notice that if $S(n+1)=N$ , then $n$ must be a number whose initial digits sum to $N-1$ , and whose other, terminating digits, are all $9$ . Thus, we can evaluate the three final possibilities by seeing if the equation $(N-1)+9x=1274$ has an integer solution.
The equation does not have an integer solution for $N=12$ , so $C$ is not correct. However, the equation does have an integer solution for $N=1239$ ( $x=4$ ), so $\boxed{\textbf{(D)} ~1239}$ is the answer.

## Solution 5 (Intuition)
If adding $1$ to $n$ does not carry any of its digits, then $S(n+1)=S(n)+1$ (ex: $25+1=26$ . Sum of digits $7 \rightarrow 8$ ). But since no answer choice is $1275$ , that means $n$ has some amount of $9$ 's from right to left.
When $n+1$ , some $9$ 's will bump to 0, not affected its $\pmod 9$ . But the first non-9 digit (from right to left) will be bumped up by 1. So $S(n) + 1 \pmod {9} \equiv S(n+1) \pmod{9}$ . For example, $34999+1=35000$ , and the sum of digits $7+27 \rightarrow 8+0$ .
Since $S(n) \equiv 5 \pmod{9}$ , that means $S(n+1) \equiv 6 \pmod{9}$ . The only answer choice that meets this requirement is $\boxed{\textbf{(D) } 1239}.$

## Solution 6 (Answer choices and luck)
We note quickly from the given value of $S(n)$ that the form of n is likely going to be of the form $999999999...X9...9999$ where X is a natural number between 1 and 9 inclusive
This allows us to create the following equation
$S(n+1)=1275 - 9y= A$
where $A$ is an answer choice and $y$ is any natural number
Plugging in answer choices for $A$ we quickly see that $\boxed{\textbf{(D) } 1239}.$ is our answer
$\textbf{Note}$ : we do have a second possible form for $n$ which is
$99999...993$
and thus $n+1 = 99999...994$ and $S(n+1)=1273$
but since $1273$ is not an answer choice we can disregard this case
~BakedPotato66

## Solution 7 (Answer choices but what's luck?)
This is a very complex solution so I recommend you read the previous ones before this.
Looking at the answer choices we first take A.
We see that A cannot work as if it was 1, that means that the number must be 1 followed by \( n \) amounts of zero's, and this cannot work as \( S(n) \) itself is not divisible by 9.
We look at 3 and notice that we have two cases. Either it is \( 1 + 2 + n \) zero's or it is 3 followed by \( n \) zero's. Case 2 is obviously false as subtracting 2 still doesn't make \( S(n) \) divisible by 9, and \( 1 + 2 + n \) zero's also doesn't work as even when we subtract 3 from the total, \( S(n) \) proceeds to still not be divisible by 9.
We look at 12 an immediately notice this can't be true as it needs to be divisible by 3 and 4 and the number itself cannot be both divisible by 3 and by 2 as when adding 1 to \( S(n) \) gives 1275, which is odd.
We look at 1239 and see that the sum of the digits is exactly 1 greater than \( S(n) \), making it a possibility.
We see that 1265 has a sum that is exactly the same as \( S(n) \). This means that the subaverage of the number lies between an interval of 9. But the sum \( S(n) \) itself is not divisible by 9, proving that the subaverage is false.
Our only answer is $\boxed{\textbf{(D) } 1239}.$
~Pinotation

## Video Solution
https://youtu.be/zfChnbMGLVQ?t=3996
~ pi_is_3.14

## Video Solution
https://youtu.be/pbt6p5s8J50
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .