# 2016 AMC 8 Problem 21

## Problem

A top hat contains 3 red chips and 2 green chips. Chips are drawn randomly, one at a time without replacement, until all 3 of the reds are drawn or until both green chips are drawn. What is the probability that the 3 reds are drawn?

$\textbf{(A) }\dfrac{3}{10}\qquad\textbf{(B) }\dfrac{2}{5}\qquad\textbf{(C) }\dfrac{1}{2}\qquad\textbf{(D) }\dfrac{3}{5}\qquad \textbf{(E) }\dfrac{7}{10}$

## Solutions

## Solution 1
We put five chips randomly in order and then pick the chips from the left to the right. To find the number of ways to rearrange the three red chips and two green chips, we solve for $\binom{5}{2} = 10$ . However, we notice that whenever the last chip we draw is red, we pick both green chips before we pick the last red chip. Similarly, when the last chip is green, we pick all three red chips before the last green chip. This means that the last chip must be green in all the situations that work. This means we are left with finding the number of ways to rearrange three red chips and one green chip, which is $\binom{4}{3} = 4$ . Because a green chip will be last $4$ out of the $10$ situations, our answer is $\boxed{\textbf{(B) } \frac{2}{5}}$ .

## Solution 2
We can use basic probability to find the answer to this question. The probability of the first chip being red is $\frac{3}{5}$ because there are $3$ red chips and $5$ chips in total. The probability of the second chip being red is $\frac{2}{4}$ because there are now $2$ red chips and $4$ total chips. The probability of the third chip being red is $\frac{1}{3}$ because there are now $1$ red chips and $3$ total chips. If we multiply these fractions, we get $\frac{1}{10}$ . To get the answer of $\frac{2}{5}$ we need to multiply this product by $4$ because there are $4$ different draws that these red chips can be chosen on. They can be chosen on the $\text{1st 2nd, 3rd, or 4th}$ draws because if a red chip was chosen on the $\text{5th}$ draw, $2$ green chips would have already been chosen. So our answer is $\frac{1}{10}$ multiplied by $4$ which would leave us with the answer of $\boxed{\textbf{(B) } \frac{2}{5}}$ .
~ThatCarGuy3

## Faster Solution (Similar to Solution 1)
Arrange them in a row of 5. There is a 3/5 chance that the last one will be red. If the last one is red, 3 reds will not be drawn first, so there is a $\boxed{\textbf{(B) } \frac{2}{5}}$ chance that 3 reds will come out first.

## Video Solution
https://youtu.be/RK1lG84nr4w
~Education, the Study of Everything
### See Also