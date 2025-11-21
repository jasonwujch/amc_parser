# 2001 AIME II Problem 5

## Problem

A set of positive numbers has the triangle property if it has three distinct elements that are the lengths of the sides of a triangle whose area is positive. Consider sets $\{4, 5, 6, \ldots, n\}$ of consecutive positive integers, all of whose ten-element subsets have the triangle property. What is the largest possible value of $n$ ?

## Solution
Out of all ten-element subsets with distinct elements that do not possess the triangle property, we want to find the one with the smallest maximum element. Call this subset $\mathcal{S}$ . Without loss of generality, consider any $a, b, c \,\in \mathcal{S}$ with $a < b < c$ . $\,\mathcal{S}$ does not possess the triangle property , so $c \geq a + b$ . We use this property to build up $\mathcal{S}$ from the smallest possible $a$ and $b$ :
\[\mathcal{S} = \{\, 4,\, 5,\, 4+5, \,5+(4+5),\, \ldots\,\} = \{4, 5, 9, 14, 23, 37, 60, 97, 157, 254\}\]
$\mathcal{S}$ is the "smallest" ten-element subset without the triangle property, and since the set $\{4, 5, 6, \ldots, 253\}$ is the largest set of consecutive integers that does not contain this subset, it is also the largest set of consecutive integers in which all ten-element subsets possess the triangle property. Thus, our answer is $n = \fbox{253}$ .
### Note
If we wanted to find this for a much larger number (say 2001), we could have noted that this is a "quasi-Fibonacci" sequence with initial terms $4,5$ and built up an explicit function to find the $nth$ term. (The latter part is generally pretty annoying).
~Dhillonr25 ~Minor edit by Yiyj1
These problems are copyrighted © by the Mathematical Association of America.