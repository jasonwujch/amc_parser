# 2019 AMC 10B Problem 21

## Problem

Debra flips a fair coin repeatedly, keeping track of how many heads and how many tails she has seen in total, until she gets either two heads in a row or two tails in a row, at which point she stops flipping. What is the probability that she gets two heads in a row but she sees a second tail before she sees a second head？

$\textbf{(A) } \frac{1}{36} \qquad \textbf{(B) } \frac{1}{24} \qquad \textbf{(C) } \frac{1}{18} \qquad \textbf{(D) } \frac{1}{12} \qquad \textbf{(E) } \frac{1}{6}$

## Solution 1
We first want to find out which sequences of coin flips satisfy the given condition. For Debra to see the second tail before the second head, her first flip can't be heads, as that would mean she would either end with double tails before seeing the second head, or would see two heads before she sees two tails. Therefore, her first flip must be tails. The shortest sequence of flips by which she can get two heads in a row and see the second tail before she sees the second head is $THTHH$ , which has a probability of $\frac{1}{2^5} = \frac{1}{32}$ . Furthermore, she can prolong her coin flipping by adding an extra $TH$ , which itself has a probability of $\frac{1}{2^2} = \frac{1}{4}$ . Since she can do this indefinitely, this gives an infinite geometric series with a first term of $\frac{1}{32}$ and a common ratio of $\frac{1}{4}$ , which means the answer (by the infinite geometric series sum formula) is $\frac{\frac{1}{32}}{1-\frac{1}{4}} = \boxed{\textbf{(B) }\frac{1}{24}}$ .
### Alternative finish
You have $THT$ ...(insert any # of pairs of HT)...HH. You could have $0$ pairs, $1$ pair, $2$ pairs, etc. of HT. Thus the probability is $(\frac{1}{2})^0+(\frac{1}{2})^2+(\frac{1}{2})^4+...=\frac{1}{(1-(\frac{1}{2})^2)}=4/3$ . number of ways to get $THT...HH$ in that order is $\frac{1}{8} * \frac{1}{4}$ . Thus your probability is $\frac{1}{8} * \frac{4}{3} * \frac{1}{4} = \frac{1}{24}$ as desired
~mathboy282
~minor LaTeX edits by turttheturtlez

## Solution 2 (Easier)
Note that the sequence must start in $THT$ , which happens with $\frac{1}{8}$ probability. Now, let $P$ be the probability that Debra will get two heads in a row after flipping $THT$ . Either Debra flips two heads in a row immediately (probability $\frac{1}{4}$ ), or flips a head and then a tail and reverts back to the "original position" (probability $\frac{1}{4}P$ ). Therefore, $P=\frac{1}{4}+\frac{1}{4}P$ , so $P=\frac{1}{3}$ , so our final answer is $\frac{1}{8}\times\frac{1}{3}=\boxed{\textbf{(B) }\frac{1}{24}}$ .
~Stormersyle

## Solution 3 (Even Easier)
Since the sequence must start with $THT$ and end with $HH$ and only have $HT$ in between, we use the infinite geometric series formula to get $\frac{1}{2^5}$ which is the smallest option, $THTHH$ , $+\frac{1}{2^7}$ , the next best option, and so on and so forth until we have an infinite geometric series increasing at a rate of $X\frac{1}{2^2}$ so it is equivalent to $\frac{\frac{1}{2^5}}{1-\frac{1}{2^2}}=\frac{1}{2^6}\cdot\frac{2^2}{3}=\frac{1}{3\cdot2^3}=\frac{1}{8\cdot3}=\boxed{\textbf{(B) }\frac{1}{24}}$
~<B+

## Video Solution by OmegaLearn
https://youtu.be/wopflrvUN2c?t=993

## Video Solution by OnTheSpotSTEM
https://www.youtube.com/watch?v=2f1zEvfUe9o
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .