# 2004 AIME I Problem 2

## Problem

Set $A$ consists of $m$ consecutive integers whose sum is $2m$ , and set $B$ consists of $2m$ consecutive integers whose sum is $m.$ The absolute value of the difference between the greatest element of $A$ and the greatest element of $B$ is $99$ . Find $m.$

## Solution 1
Note that since set $A$ has $m$ consecutive integers that sum to $2m$ , the middle integer (i.e., the median) must be $2$ . Therefore, the largest element in $A$ is $2 + \frac{m-1}{2}$ .
Further, we see that the median of set $B$ is $0.5$ , which means that the "middle two" integers of set $B$ are $0$ and $1$ . Therefore, the largest element in $B$ is $1 + \frac{2m-2}{2} = m$ . $2 + \frac{m-1}{2} > m$ if $m < 3$ , which is clearly not possible, thus $2 + \frac{m-1}{2} < m$ .
Solving, we get \begin{align*} m - 2 - \frac{m-1}{2} &= 99\\ m-\frac{m}{2}+\frac{1}{2}&=101\\ \frac{m}{2}&=100\frac{1}{2}.\\ m &= \boxed{201}\end{align*}

## Solution 2
Let us give the elements of our sets names: $A = \{x, x + 1, x + 2, \ldots, x + m - 1\}$ and $B = \{y, y + 1, \ldots, y + 2m - 1\}$ . So we are given that \[2m = x + (x + 1) + \ldots + (x + m - 1) = mx + (1 + 2 + \ldots + (m - 1)) = mx + \frac{m(m -1)}2,\] so $2 = x + \frac{m - 1}2$ and $x + (m - 1) = \frac{m + 3}2$ (this is because $x = 2 - \frac{m-1}{2}$ so plugging this into $x+(m-1)$ yields $\frac{m+3}{2}$ ). Also, \[m = y + (y + 1) + \ldots + (y + 2m - 1) = 2my + \frac{2m(2m - 1)}2,\] so $1 = 2y + (2m - 1)$ so $2m = 2(y + 2m - 1)$ and $m = y + 2m - 1$ .
Then by the given, $99 = |(x + m - 1) - (y + 2m - 1)| = \left|\frac{m + 3}2 - m\right| = \left|\frac{m - 3}2\right|$ . $m$ is a positive integer so we must have $99 = \frac{m - 3}2$ and so $m = \boxed{201}$ .

## Solution 3
The thing about this problem is, you have some "choices" that you can make freely when you get to a certain point, and these choices won't affect the accuracy of the solution, but will make things a lot easier for us.
First, we note that for set $A$
\[\frac{m(f + l)}{2} = 2m\]
Where $f$ and $l$ represent the first and last terms of $A$ . This comes from the sum of an arithmetic sequence.
Solving for $f+l$ , we find the sum of the two terms is $4$ .
Doing the same for set B, and setting up the equation with $b$ and $e$ being the first and last terms of set $B$ ,
\[m(b+e) = m\]
and so $b+e = 1$ .
Now we know, assume that both sequences are increasing sequences, for the sake of simplicity. Based on the fact that set $A$ has half the number of elements as set $B$ , and the difference between the greatest terms of the two two sequences is $99$ (forget about absolute value, it's insignificant here since we can just assume both sets end with positive last terms), you can set up an equation where $x$ is the last term of set A:
\[2(x-(-x+4)+1) = 1+(x+99)-(-x-99+1)\]
Note how i basically just counted the number of terms in each sequence here. It's made a lot simpler because we just assumed that the first term is negative and last is positive for each set, it has absolutely no effect on the end result! This is a great strategy that can help significantly simplify problems. Also note how exactly i used the fact that the first and last terms of each sequence sum to $4$ and $1$ respectively (add $x$ and $(-x+4)$ to see what i mean).
Solving this equation we find $x = 102$ . We know the first and last terms have to sum to $4$ so we find the first term of the sequence is $-98$ . Now, the solution is in clear sight, we just find the number of integers between $-98$ and $102$ , inclusive, and it is $m = \boxed{201}$ .
Note how this method is not very algebra heavy. It seems like a lot by the amount of text but really the first two steps are quite simple.

## Solution 4 (Sketchy Solution for Speedrunners)
First, calculate the average of set $A$ and set $B$ . It's obvious that they are $2$ and $1/2$ respectively. Let's look at both sets. Obviously, there is an odd number of integers in the set with $2$ being in the middle, which means that $m$ is an odd number and that the number of consecutive integers on each side of $2$ are equal. In set $B$ , it is clear that it contains an even number of integers, but since the number in the middle is $1/2$ , we know that the range of the consecutive numbers on both sides will be $(x$ to $0)$ and $(1$ to $-y)$ .
Nothing seems useful right now, but let's try plugging an odd number, $3$ , for $m$ in set $B$ . We see that there are $6$ consecutive integers and $3$ on both sides of $1/2$ . After plugging this into set $A$ , we find that the set equals \[{1,2,3}\] . From there, we find the absolute value of the difference of both of the greatest values, and get 0.
Let's try plugging in another odd number, $55$ . We see that the resulting set of numbers is $(-54$ to $0)$ , and $(1$ to $55)$ . We then plug this into set $A$ , and find that the set of numbers is $(-25$ to $-29)$ which indeed results in the average being $2$ . We then find the difference of the greatest values to be 26.
From here, we see a pattern that can be proven by more trial and error. When we make $m$ equal to $3$ , then the difference is $0$ whearas when we make it $55$ , then the difference is $26$ . $55-3$ equals to $52$ and $26-0$ is just $0$ . We then see that $m$ increases twice as fast as the difference. So when the difference is $99$ , it increased $99$ from when it was $0$ , which means that $m$ increased by $99*2$ which is $198$ . We then add this to our initial $m$ of $3$ , and get $\boxed{201}$ as our answer.

## Solution 5
Let the first term of $A$ be $a$ and the first term of $B$ be $b$ . There are $m$ elements in $A$ so $A$ is $a, a+1, a+2,...,a+m-1$ . Adding these up, we get $\frac{2a+m-1}{2}\cdot m = 2m \implies 2a+m=5$ . Set $B$ contains the numbers $b, b+1, b+2,...,b+2m-1$ . Summing these up, we get $\frac{2b+2m-1}{2}\cdot 2m =m \implies 2b+2m=2$ . The problem gives us that the absolute value of the difference of the largest terms in $A$ and $B$ is $99$ . The largest term in $A$ is $a+m-1$ and the largest term in $B$ is $b+2m-1$ so $|b-a+m|=99$ . From the first two equations we get, we can get that $2(b-a)+m=-3$ . Now, we make a guess and assume that $b-a+m=99$ (if we get a negative value for $m$ , we can try $b-a+m=-99$ ). From here we get that $b-a=-102$ . Solving for $m$ , we get that the answer is $\boxed{201}$
-Heavytoothpaste
These problems are copyrighted © by the Mathematical Association of America.