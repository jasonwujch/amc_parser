# 2007 AMC 10B Problem 9

## Problem

A cryptographic code is designed as follows. The first time a letter appears in a given message it is replaced by the letter that is $1$ place to its right in the alphabet (asumming that the letter $A$ is one place to the right of the letter $Z$ ). The second time this same letter appears in the given message, it is replaced by the letter that is $1+2$ places to the right, the third time it is replaced by the letter that is $1+2+3$ places to the right, and so on. For example, with this code the word "banana" becomes "cbodqg". What letter will replace the last letter $s$ in the message \[\text{"Lee's sis is a Mississippi miss, Chriss!"?}\]

$\textbf{(A) } g \qquad\textbf{(B) } h \qquad\textbf{(C) } o \qquad\textbf{(D) } s \qquad\textbf{(E) } t$

## Solution
Since the letter that will replace the last $s$ does not depend on any letter except the other $s$ 's, you can disregard anything else. There are $12$ $s$ 's, so the last $s$ will be replaced by the letter $1+2+3+\cdots+12$ places to the right of $s$ . \[1+2+3+\cdots+12=12 \times \frac{1+12}{2} = 78\] Every $26$ places, you will end up with the same letter so you can just take the remainder of $78$ when you divide by $26,$ which is $0.$ Therefore, the letter that will replace the last $s$ is $\boxed{\textbf{(D) } s}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .