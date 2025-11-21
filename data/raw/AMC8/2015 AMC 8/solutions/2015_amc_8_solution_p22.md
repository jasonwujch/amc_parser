# 2015 AMC 8 Problem 22

## Problem

On June 1, a group of students is standing in rows, with 15 students in each row. On June 2, the same group is standing with all of the students in one long row. On June 3, the same group is standing with just one student in each row. On June 4, the same group is standing with 6 students in each row. This process continues through June 12 with a different number of students per row each day. However, on June 13, they cannot find a new way of organizing the students. What is the smallest possible number of students in the group?

$\textbf{(A) } 21 \qquad \textbf{(B) } 30 \qquad \textbf{(C) } 60 \qquad \textbf{(D) } 90 \qquad \textbf{(E) } 1080$

## Solution 1
Since we know the number must be a multiple of $15$ , we can eliminate $A$ . We also know that after $12$ days, the students can't find any more arrangements, meaning the number has $12$ factors. Now, we just list the factors of every number, starting with $30$ : \[30=1\cdot30, 2\cdot15, 3\cdot10, 5\cdot6\] \[60=1\cdot60, 2\cdot30, 3\cdot20, 4\cdot15, 5\cdot12, 6\cdot10\] $60$ has $12$ factors, so the answer is $\boxed{\textbf{(C) } 60}$ .
Note - A faster way to find the factors of a number is really helpful in competitions, as you don't want to waste time listing them all. What we can do is find the prime factorization of a number. We'll use $60$ as an example here, so we take $60 = 2 \cdot 2 \cdot 3 \cdot 5$ or $60 = 2^2 \cdot 3^1 \cdot 5^1$ . Now, we just add one to the power of each factor. So since we have powers of $2$ , $1$ , and $1$ , we turn those into $3$ , $2$ , and $2$ . Finally, we just multiply them together to get $3 \cdot 2 \cdot 2 = 12$ as the amount of factors in 60.

## Solution 2
We know that the number of students in the group has to be a multiple of 15, so we can eliminate A. However, on June 13, they cannot find a new way of organizing the students meaning that the number has only 12 factors. The prime factorization of 60 is equal to 2^2 x 3^1 x 5^1. Using the factor counting formula, we have the add one to each exponent and multiply them together to find the number of factors. $(2+1) \times (1+1) \times (1+1) = 3 \times 2 \times 2 = 12$ factors making $\boxed{\textbf{(C) } 60}$ the answer.
~ CHECKMATE2021
### See Also