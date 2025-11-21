# 2016 AIME I Problem 2

## Problem

Two dice appear to be normal dice with their faces numbered from $1$ to $6$ , but each die is weighted so that the probability of rolling the number $k$ is directly proportional to $k$ . The probability of rolling a $7$ with this pair of dice is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution
It is easier to think of the dice as $21$ sided dice with $6$ sixes, $5$ fives, etc. Then there are $21^2=441$ possible rolls. There are $2\cdot(1\cdot 6+2\cdot 5+3\cdot 4)=56$ rolls that will result in a seven. The odds are therefore $\frac{56}{441}=\frac{8}{63}$ . The answer is $8+63=\boxed{071}$
See also 2006 AMC 12B Problems/Problem 17

## Solution 2
Since the probability of rolling any number is 1, and the problem tells us the dice are unfair, we can assign probabilities to the individual faces. The probability of rolling $n$ is $\frac{n}{21}$ because $21=\frac{6 \cdot 7}{2}$ Next, we notice that 7 can be rolled by getting individual results of 1 and 6, 2 and 5, or 3 and 4 on the separate dice. The probability that 7 is rolled is now $2(\frac{1}{21} \cdot \frac{6}{21}+\frac{2}{21} \cdot \frac{5}{21} + \frac{3}{21} \cdot \frac{4}{21})$ which is equal to $\frac{56}{441}=\frac{8}{63}$ . Therefore the answer is $8+63=\boxed{071}$ ~PEKKA

## Solution 3
Since the probability of rolling a $1$ is $\frac{1}{21}$ , the probability of rolling a $2$ is $\frac{2}{21}$ the probability of rolling a $3$ is $\frac{3}{21}$ and so on, we can make a chart of probabilities and add them together. Note that we only need the probabilities of $1$ and $6$ , $2$ and $5$ , and $3$ and $4$ , and the rest is symmetry and the others are irrelevant.
We have: $2 \cdot (\frac{1}{21} \cdot \frac{2}{7}$ $+$ $\frac{2}{21} \cdot \frac{5}{21}$ $+$ $\frac{1}{7} \cdot \frac{4}{21})$ $=$ $2 \cdot (\frac{2}{147} + \frac{10}{441} + \frac{4}{147})$ = $2 \cdot \frac{4}{63} = \frac{8}{63}$ . Therefore, the answer is $8 + 63$ = $\boxed{071}$
~Arcticturn
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .