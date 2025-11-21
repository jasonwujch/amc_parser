# 2012 AMC 10B Problem 22

## Problem

Let ( $a_1$ , $a_2$ , ... $a_{10}$ ) be a list of the first 10 positive integers such that for each $2\le$ $i$ $\le10$ either $a_i + 1$ or $a_i-1$ or both appear somewhere before $a_i$ in the list. How many such lists are there?

$\textbf{(A)}\ \ 120\qquad\textbf{(B)}\ 512\qquad\textbf{(C)}\ \ 1024\qquad\textbf{(D)}\ 181,440\qquad\textbf{(E)}\ \ 362,880$

## Solution 1
If we have 1 as the first number, then the only possible list is $(1,2,3,4,5,6,7,8,9,10)$ .
If we have 2 as the first number, then we have 9 ways to choose where the $1$ goes, and the numbers ascend from the first number, $2$ , with the exception of the $1$ . For example, $(2,3,1,4,5,6,7,8,9,10)$ , or $(2,3,4,1,5,6,7,8,9,10)$ . There are $\dbinom{9}{1}$ ways to do so.
If we use 3 as the first number, we need to choose 2 spaces to be 2 and 1, respectively. There are $\dbinom{9}{2}$ ways to do this.
In the same way, the total number of lists is: $\dbinom{9}{0} +\dbinom{9}{1} + \dbinom{9}{2} + \dbinom{9}{3} + \dbinom{9}{4}.....\dbinom{9}{9}$
By the binomial theorem , this is $2^{9}$ = $512$ , or $\boxed{\textbf{(B)}}$

## Solution 2
Arrange the spaces and put arrows pointing either up or down between them. Then for each arrangement of arrows there is one and only one list that corresponds to up. For example, all arrows pointing up is $(1,2,3,4,5...10)$ . There are 9 arrows, so the answer is $2^{9}$ = $512$ $\boxed{\textbf{(B)}}$
NOTE: Solution cited from: http://www.artofproblemsolving.com/Videos/external.php?video_id=269 .

## Solution 3
Notice that the answer to the problem is solely based on the length of the lists, i.e. 10. We can replace 10 with smaller values, such as 2 and 3, and try to find a pattern. If we replace it with 2, we can easily see that there are two possible lists, $(1, 2)$ and $(2, 1)$ . If we replace it with 3, there are four lists, $(1, 2, 3), (2, 1, 3), (2, 3, 1),$ and $(3, 2, 1)$ . Since 2 and 4 are both powers of 2, it is likely that the number of lists is $2^{n-1}$ , where $n$ is the length of the lists. $2^{10-1}=512=\boxed{\textbf{(B)}}$

## Solution 4 (Recursion)
If $a_1=10$ , the sequence must be $10, 9, 8,7,6,5,4,3,2,1$ . If $a_2=10$ , then $a_1=9$ , and the sequence is $9, 10, 8, 7, 6, 5,4,3,2,1$ . If $a_3=10$ , then the possible sequences are \[9,8,10,7,6,5,4,3,2,1 \text{ and}\] \[8,9,10,7,6,5,4,3,2,1.\] In general, for an $n$ -length sequence, if $a_i=n$ , then $a_1$ through $a_{i-1}$ can be filled in $f(i-1)$ ways with $n-i+1$ through $n-1$ , and $a_{i+1}$ through $a_{n}$ must be sorted in decreasing order with the remaining numbers ( $1$ through $n-i$ ), in one way. Thus $f(n) = \sum_{i=0}^{n-1} f(i)$ , where $f(0)=1$ .
We can see (or prove by induction) that $f(n)=2^{n-1} ~\forall~ n \ge 1$ . Hence, $f(10)=2^9=\boxed{\textbf{(B) }512}$ .
- ColtsFan10

## Solution 5
Solution 3 states that $f(n)=2^{n-1} ~\forall~ n \ge 1$ without formal proof. Solution 4 gives a formal proof. Here is another formal proof:
$f(1)=1$ . When the list goes from $n-1$ numbers to $n$ numbers, there are $2$ ways to make the new lists:
Case 1: append $n$ to the end of lists with $n-1$ numbers to make a new list, the number of the new lists is $f(n-1)$ ;
Case 2: put number $1$ at the end of the new lists, the way to arrange $(2,3,...,n-1,n)$ as the first $n-1$ items is the same as to arrange $(1,2,...,n-2,n-1)$ , by subtracting 1 from each of the elements, so the number of the new lists is also $f(n-1)$ .
So $f(n)=f(n-1)+f(n-1)=2f(n-1)=2^{n-1} ~\forall~ n \ge 1$
- junche

## Solution 6 (similar to solution 2, explained differently)
Lay out the numbers $(1,2,3,4,5,6,7,8,9,10)$ . Let's say each time a number is chosen, it is crossed out. Notice that for each new number we choose, it must be one that is next to one already chosen (if we have chosen numbers in the order $5$ , $6$ , $4$ , $7$ , $8$ then all the numbers from $4$ to $8$ are crossed out like a 'block' of crosses. our next number is either $3$ or $9$ .). We can imagine this as each time either choosing a higher number or a lower number (in the example either $3$ or $9$ ).
So when we start with $1$ , then at no point we are allowed to choose a lower number, giving us only higher numbers which is $\dbinom{9}{0}$ . Similarly for $2$ , we can only choose a lower number once (the only number lower than our starting is $1$ ), which is $\dbinom{9}{1}$ . Continue for when we start with $3$ , $4$ , $5$ and so on, so we have the sum $\dbinom{9}{0} +\dbinom{9}{1} + \dbinom{9}{2}.....\dbinom{9}{9}=2^9=512$ , so we choose $\boxed{\textbf{(B)}}$ .
-lisztepos

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012amc10b/269
~dolphin7

## Video Solution by TheBeautyofMath
https://youtu.be/bXPSv93GVbg
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .