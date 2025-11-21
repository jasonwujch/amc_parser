# 2005 AMC 8 Problem 24

## Problem

A certain calculator has only two keys [+1] and [x2]. When you press one of the keys, the calculator automatically displays the result. For instance, if the calculator originally displayed "9" and you pressed [+1], it would display "10." If you then pressed [x2], it would display "20." Starting with the display "1," what is the fewest number of keystrokes you would need to reach "200"?

$\textbf{(A)}\ 8\qquad\textbf{(B)}\ 9\qquad\textbf{(C)}\ 10\qquad\textbf{(D)}\ 11\qquad\textbf{(E)}\ 12$

## Solution 1 (Now rigorous)
We can start at $200$ and work our way down to $1$ . We want to press the button that multiplies by $2$ the most, but since we are going down instead of up, we divide by $2$ instead. If we come across an odd number, then we will subtract that number by $1$ . Notice
Since we've reached $1$ , it's clear that the answer should be $\boxed{\textbf{(B)}\ 9}$ - $\boxed{\textbf{Javapost}}$ . Because we only subtracted $1$ when we had to, this is optimal. ~Roy2020

## Solution 2 (Binary)
We make two key observations. First, pressing [x2] appends a $0$ to the end of a number's binary representation. Second, pressing [x2] and then pressing [+1] appends $1$ to the end of a number's binary representation.
The base-ten number $200$ is represented as $11001000_2$ in binary. Therefore, the five $0$ s contribute $5$ button presses. Similarly, each of the three $1$ s each contribute $2$ button presses, although we do not count one of them as the calculator initially starts with the number $1.$ Thus, the answer is $5 + 2 \cdot 2 = \boxed{\textbf{(B)}\ 9}$
### See Also