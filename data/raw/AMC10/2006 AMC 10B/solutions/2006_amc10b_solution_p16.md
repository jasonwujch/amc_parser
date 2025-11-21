# 2006 AMC 10B Problem 16

## Problem

Leap Day, February $29$

$\textbf{(A) } \textrm{Tuesday} \qquad \textbf{(B) } \textrm{Wednesday} \qquad \textbf{(C) } \textrm{Thursday} \qquad \textbf{(D) } \textrm{Friday} \qquad \textbf{(E) } \textrm{Saturday}$

## Solution
There are $365$ days in a year, plus $1$ extra day if there is a Leap Day, which occurs on years that are multiples of $4$ (with a few exceptions that don't affect this problem).
Therefore, the number of days between Leap Day $2004$ and Leap Day $2020$ is:
$16 \cdot 365 + 4 \cdot 1 = 5844$
Since the days of the week repeat every $7$ days and $5844 \equiv -1 \bmod{7}$ , the day of the week Leap Day $2020$ occurs is the day of the week the day before Leap Day $2004$ occurs, which is $\boxed{\textbf{(E) }\textrm{Saturday}}$ .

## Solution 2 (Feasible Shortcuts)
Since every non-leap year there is one day extra after the $52$ weeks, we can deduce that if we were to travel forward $x$ amount of non-leap years, then the answer would be "Sunday + $x$ " days.
However, we also have leap-years in our pool of years traveled forward, and for every leap-year that passes, we have two extra days after the 52 weeks. So we would travel "Sunday + $2x$ " days.
Mixing these two together, we get $4$ leap years $(2008, 2012, 2016, 2020)$ , and $12$ non-leap years. We thus get $12 + 2\cdot 4 = 20$ "extra days" after Sunday. Since seven days are in a week, we can get $20 \bmod{7} \equiv 6$ , and six days after Sunday is $\boxed{\textbf{(E) }\textrm{Saturday}}$ .
- Note how we did not require any complex or time-consuming computation, and thus it will save crucial time, especially during a test like the AMC 10.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .