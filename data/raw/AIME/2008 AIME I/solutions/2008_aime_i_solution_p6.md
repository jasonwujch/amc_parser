# 2008 AIME I Problem 6

## Problem

A triangular array of numbers has a first row consisting of the odd integers $1,3,5,\ldots,99$ in increasing order. Each row below the first has one fewer entry than the row above it, and the bottom row has a single entry. Each entry in any row after the top row equals the sum of the two entries diagonally above it in the row immediately above it. How many entries in the array are multiples of $67$ ?

## Solution 1
Let the $k$ th number in the $n$ th row be $a(n,k)$ . Writing out some numbers, we find that $a(n,k) = 2^{n-1}(n+2k-2)$ . [1]
We wish to find all $(n,k)$ such that $67| a(n,k) = 2^{n-1} (n+2k-2)$ . Since $2^{n-1}$ and $67$ are relatively prime , it follows that $67|n+2k-2$ . Since every row has one less element than the previous row, $1 \le k \le 51-n$ (the first row has $50$ elements, the second $49$ , and so forth; so $k$ can range from $1$ to $50$ in the first row, and so forth). Hence
it follows that $67| n - 2k + 2$ implies that $n-2k+2 = 67$ itself.
Now, note that we need $n$ to be odd, and also that $n+2k-2 = 67 \le 100-n \Longrightarrow n \le 33$ .
We can check that all rows with odd $n$ satisfying $1 \le n \le 33$ indeed contains one entry that is a multiple of $67$ , and so the answer is $\frac{33+1}{2} = \boxed{017}$ .
^ Proof: Indeed, note that $a(1,k) = 2^{1-1}(1+2k-2)=2k-1$ , which is the correct formula for the first row. We claim the result by induction on $n$ . By definition of the array, $a(n,k) = a(n-1,k)+a(n-1,k+1)$ , and by our inductive hypothesis, \begin{align*}a(n,k) &= a(n-1,k)+a(n-1,k+1)\\ &= 2^{n-2}(n-1+2k-2)+2^{n-2}(n-1+2(k+1)-2)\\&=2^{n-2}(2n+4k-4)\\&=2^{n-1}(n+2k-2)\end{align*} thereby completing our induction.

## Solution 2
The result above is fairly intuitive if we write out several rows and then divide all numbers in row $r$ by $2^{r-1}$ (we can do this because dividing by a power of 2 doesn't affect divisibility by $67$ ). The second row will be $2, 4, 6, \cdots , 98$ , the third row will be $3, 5, \cdots, 97$ , and so forth. Clearly, only the odd-numbered rows can have a term divisible by $67$ . However, with each row the row will have one less element, and the $99-67+1 = 33$ rd row is the last time $67$ will appear. Therefore the number of multiples of 67 in the entire array is $\frac{33+1}{2} = \boxed{017}$ .

## Video Solution
2008 AIME I #6
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.