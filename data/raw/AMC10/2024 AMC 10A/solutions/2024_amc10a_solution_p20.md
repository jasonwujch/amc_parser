# 2024 AMC 10A Problem 20

## Problem

Let $S$ be a subset of $\{1, 2, 3, \dots, 2024\}$ such that the following two conditions hold:

- If $x$ and $y$ are distinct elements of $S$ , then $|x-y| > 2.$

- If $x$ and $y$ are distinct odd elements of $S$ , then $|x-y| > 6.$

What is the maximum possible number of elements in $S$ ?

$\textbf{(A) }436 \qquad \textbf{(B) }506 \qquad \textbf{(C) }608 \qquad \textbf{(D) }654 \qquad \textbf{(E) }675$

## Solution 1
All lists are organized in ascending order:
By listing out the smallest possible elements of subset $S,$ we can find that subset $S$ starts with $\{1, 4, 8, 11, 14, 18, 21, 24, 28, 31, \dots\}.$ It is easily noticed that the elements of the subset "loop around" every 3 elements, specifically adding 10 each time. This means that there will be $2024/10$ or $202R4$ whole loops in the subset $S,$ implying that there will be $202*3 = 606$ elements in S. However, we have undercounted, as we did not count the remainder that resulted from $2024/10$ $.$ With a remainder of $4,$ we can fit $2$ more elements into the subset $S,$ namely $2021$ and $2024,$ resulting in a total of $606+2$ or $\boxed{\textbf{(C) }608}$ elements in subset $S$ .
NOTE:
To prove that this is the best we can do, consider adding each element one by one, for the first element, say n. If $n>2$ , we can choose $n - 2$ which is always better. Therefore, $n = 1$ or $n = 2.$
If $n = 2$ was optimal, then choose it, then the set of usable numbers in $S$ becomes 5 through 2024. We can transform the usable set of $S$ to $Q$ where $Q$ contains the numbers 1 through 2020. Because we assumed $n = 2$ was optimal, we can choose $n = 2$ for the set $Q$ too. Because every element in $Q$ is 4 below the elements of $S$ , choosing 2 in $Q$ would mean choosing 6 in set $S$ . By induction we see that our list would be $\{2,6,10,14,18,.....2022\}$ which only gives $506$ elements which is sub-optimal. Therefore, we can conclude that $n = 1$ is optimal, and we proceed as the solution above.
-weihou0
- minor latex edits by eqb5000

## Solution 2
Notice that we can first place odd numbers, then place even numbers between each pair. We can start at $1$ and continue from there. Realize that the smallest number $k$ such that $kx+1$ reproduces odd number is $8$ . The next ones are $10, 12, 14$ . We can proceed to find the number of numbers in this particular sequence. From the equation $8x+1=2023$ , we get that $x \leq 252.875$ works, so this means there is 253 solutions. Looking at $1,2,3,4,5,6,7,9$ we can see that there could only be 1 possible number between each pair, yielding $252+253=505$ . Then see that we can fit two more into the number count since the set $2017$ to $2024$ can fit two evens. Now this means $A$ and $B$ don’t work. Now test out $10x+1$ . Using the same method, we get that $608$ is the maximum number in the set. Everything above $x=10$ doesn’t work, as we can split it down into smaller subgroups, so the answer is $\boxed{\textbf{(C) }608}$ .
~EaZ_Shadow

## Solution 3
We find the following pairs of numbers work:
\[(1,4), (4,8), (8,11), (11,14), (14, 18), (18, 21), (21, 24) \dots\]
Call a number an OE (odd-even) pair if the first number in the pair is odd and the second is even. Do the same for EE (even-even) and EO (even-odd) pairs. Notice that we're adding 10 to the pairs in each set, so there are 404 numbers in each set of pairs excluding 1 and 2024:
OE pairs: \[(1,4), (11,14), ... , (2021,2024) \implies (202 + 1) \cdot 2 - 2 = 404\]
EE pairs: \[(4,8), (14,18), ..., (2014,2018) \implies (201 + 1) \cdot 2 = 404\]
EO pairs: \[(8,11), (18,21), ..., (2018, 2021) \implies (201 + 1) \cdot 2 = 404\]
Every number besides $1$ and $2024$ is being overcounted twice (for example, $4$ is counted twice in the EE and OE pairs), so we have $404 \cdot \frac{3}{2} = 606.$ Finally, we add $2$ (adding back $1$ and $2024$ ) to get $\boxed{\textbf{(C) }608}$ .
~ grogg007

## Video Solution by Power Solve
https://www.youtube.com/watch?v=NZ0SBMqeAfg

## Video Solution by Pi Academy
https://youtu.be/fW7OGWee31c?si=oq7toGPh2QaksLHE

## Video Solution by SpreadTheMathLove
https://youtu.be/BhiczrT7Sg0?si=XnkHOJl5n9SWHsfc

## Video Solution 3 by grogg007 (5 mins ⏩)
https://youtu.be/rFU5EW9VOq8

## Video Solution by Scholars Foundation
https://www.youtube.com/watch?v=FKOqZau--5w&t=1s

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=4268s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .