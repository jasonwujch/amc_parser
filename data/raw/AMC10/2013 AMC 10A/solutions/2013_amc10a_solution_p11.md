# 2013 AMC 10A Problem 11

## Problem

A student council must select a two-person welcoming committee and a three-person planning committee from among its members. There are exactly $10$ ways to select a two-person team for the welcoming committee. It is possible for students to serve on both committees. In how many different ways can a three-person planning committee be selected?

$\textbf{(A)}\ 10\qquad\textbf{(B)}\ 12\qquad\textbf{(C)}\ 15\qquad\textbf{(D)}\ 18\qquad\textbf{(E)}\ 25$

## Solution
Let the number of students on the council be $x$ . To select a two-person committee, we can select a "first person" and a "second person." There are $x$ choices to select a first person; subsequently, there are $x-1$ choices for the second person. This gives a preliminary count of $x(x-1)$ ways to choose a two-person committee. However, this accounts for the order of committees. To understand this, suppose that Alice and Bob are two students in the council. If we choose Alice and then Bob, that is the same as choosing Bob and then Alice and so latter and former arrangements would be considered the same. Therefore, we have to divide by $2$ to account for overcounting. Thus, there are $\dfrac{x(x-1)} 2=10$ ways to choose the two-person committee. Solving this equation, we find that $5$ and $-4$ are integer solutions. $-4$ is a ridiculous situation, so there are $5$ people on the student council. The solution is $\dbinom 5 3=10\implies \boxed{\textbf{A}}$ .

## Solution 2 (much faster)
To choose $2$ people from $n$ total people and get $10$ as a result, we can establish the equation $\binom{n}{2}=10$ which we can easily see $n=5$ , so there are $5$ people. The question asks how many ways to choose $3$ people from the $5$ , so there are $\binom{5}{3}=\boxed{\textbf{(A)}10}$ ways.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .