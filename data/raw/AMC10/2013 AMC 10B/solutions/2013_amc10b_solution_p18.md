# 2013 AMC 10B Problem 18

## Problem

The number $2013$ has the property that its units digit is the sum of its other digits, that is $2+0+1=3$ . How many integers less than $2013$ but greater than $1000$ have this property?

$\textbf{(A)}\ 33\qquad\textbf{(B)}\ 34\qquad\textbf{(C)}\ 45\qquad\textbf{(D)}\ 46\qquad\textbf{(E)}\ 58$

## Solution 1
We take cases on the thousands digit, which must be either $1$ or $2$ : If the number is of the form $\overline{1bcd},$ where $b, c, d$ are digits, then we must have $d = 1 + b + c.$ Since $d \le 9,$ we must have $b + c \le 9 - 1 = 8.$ By casework on the value of $b$ , we find that there are $1 + 2 + \dots + 9 = 45$ possible pairs $(b, c)$ , and each pair uniquely determines the value of $d$ , so we get $45$ numbers with the given property.
If the number is of the form $\overline{2bcd},$ then it must be one of the numbers $2000, 2001, \dots, 2012.$ Checking all these numbers, we find that only $2002$ has the given property. Therefore, the number of numbers with the property is $45 + 1 = \boxed{\textbf{(D)}46}$ .

## Solution 2
This solution picks up from finding that $b + c \le 8$ in solution 1. Instead of using casework to find all possible pairs, $(b, c)$ , let's introduce a dummy variable, $z$ . Let us now have that $b + c + z = 8$ , where $b, c, z$ are all nonnegative.
We may now use stars and bars to distribute units between $b, c$ and $z$ . Any units that $z$ is given will essentially be discarded - this is how we get the 'less than' in the 'less than or equal to $8$ ' relation we found earlier.
Using two dividers, we find that the number of distributions is $\binom{10}{2},$ which is $45$ . We proceed from here as above.

## Solution 3 (Casework)
Let's start with the case that starts with $200$ . We have only one number, which is $2002$ . If we look at the $1900s$ , we have no solutions because $1+9 = 10$ , and because we can only use digits from $1$ through $9$ , it is impossible. If we looks at the $1800s$ , we do have one solution, which is $1809$ . If we look a the $1700s$ , we have $2$ solutions, namely, $1708$ and $1719$ .
We can see a pattern here. The pattern is every hundred you go down, you have $1$ more solution. Therefore, we have $1+0+1+2+3+4+5+6+7+8+9$ which is = $\boxed{\textbf{(D)}46}$ .
~Arcticturn

## Video Solution
https://youtu.be/2jNuQEfo1Rc
~savannahsolver
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .