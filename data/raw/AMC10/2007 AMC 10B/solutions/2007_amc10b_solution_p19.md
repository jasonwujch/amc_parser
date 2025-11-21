# 2007 AMC 10B Problem 19

## Problem

The wheel shown is spun twice, and the randomly determined numbers opposite the pointer are recorded. The first number is divided by $4,$ and the second number is divided by $5.$ The first remainder designates a column, and the second remainder designates a row on the checkerboard shown. What is the probability that the pair of numbers designates a shaded square?

$\textbf{(A) } \frac{1}{3} \qquad\textbf{(B) } \frac{4}{9} \qquad\textbf{(C) } \frac{1}{2} \qquad\textbf{(D) } \frac{5}{9} \qquad\textbf{(E) } \frac{2}{3}$

## Solutions

## Solution 1
When dividing each number on the wheel by $4,$ the remainders are $1, 1, 2, 2, 3,$ and $3.$ Each column on the checkerboard is equally likely to be chosen.
When dividing each number on the wheel by $5,$ the remainders are $1, 1, 2, 2, 3,$ and $4.$
The probability that a shaded square in the $1$ st or $3$ rd row of the $1$ st or $3$ rd column is chosen is \[\frac{2}{3} \times \frac{3}{6} = \frac{1}{3}\]
The probability that a shaded square in the $2$ nd or $4$ th row of the $2$ nd column is chosen is \[\frac{1}{3} \times \frac{3}{6} = \frac{1}{6}\]
Add those two together to get \[\frac{1}{3} + \frac{1}{6} = \frac{2}{6} + \frac{1}{6} = \frac{3}{6} = \boxed{\textbf{(C)} \frac{1}{2}}\]

## Solution 2
Alternatively, we may analyze this problem a little further.
First, we isolate the case where the rows are numbered 1 or 2. Notice that as listed before, the probability for picking a shaded square here is \[\frac{1}{2}\] because the column/row probabilities are the same, with the same number of shaded and non-shaded squares
Next we isolate the rows numbered 3 or 4. Note that the probability of picking the rows is same, because of our list up above. The columns, of course, still have the same probability. Because the number of shaded and non-shaded squares are equal, we have \[\frac{1}{2}\] Combining these we have a general probability of \[\boxed{\textbf{(C)} \frac{1}{2}}\]

## Solution 3
Similarly to Solution 1, we create two lists, one for $mod$ $4$ and one for $mod$ $5$ : ( $1, 2, 3, 2, 3, 1$ ) and ( $1, 2, 3, 1, 2, 4$ ). Next, we make a list of the coordinates we want for the shaded boxes. ( $1,1$ ), ( $1,3$ ), ( $2,2$ ), ( $3,1$ ), ( $3,3$ ), ( $2,4$ ). For each coordinate pair, we find the probability for it to occur. In order, we get $\frac{1}{9}, \frac{1}{18}, \frac{1}{9}, \frac{1}{9}, \frac{1}{18}, \frac{1}{18}$ . Sum these to get the answer of $\boxed{\textbf{(C)} \frac{1}{2}}$
~Dynosol

## Solution 4
We take everything modulo $4$ first. We get $1$ mod $4$ , $2$ mod $4$ , $3$ mod $4$ , twice. Therefore, the probability of any given column is equal. We take everything modulo $5$ now. We have $1, 2, 3, 1, 2, 4$ mod $5$ . $1$ and $2$ are different colored squares, and $3$ and $4$ are also different colored squares. Therefore, every single one of them has the same probability.
Therefore, our probability for a white square or a shaded square is equal, and therefore, the probability the square is shaded $\boxed {(C)\frac {1}{2}}$
~Arcticturn
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .