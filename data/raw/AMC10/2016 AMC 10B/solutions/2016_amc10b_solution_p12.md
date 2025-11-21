# 2016 AMC 10B Problem 12

## Problem

Two different numbers are selected at random from $\{1, 2, 3, 4, 5\}$ and multiplied together. What is the probability that the product is even?

$\textbf{(A)}\ 0.2\qquad\textbf{(B)}\ 0.4\qquad\textbf{(C)}\ 0.5\qquad\textbf{(D)}\ 0.7\qquad\textbf{(E)}\ 0.8$

## Solution 1
The product will be even if at least one selected number is even, and odd if none are. Using complementary counting, the chance that both numbers are odd is $\frac{\tbinom32}{\tbinom52}=\frac3{10}$ , so the answer is $1-0.3$ which is $\boxed{\textbf{(D) }0.7}$ .
An alternate way to finish: Since it is odd if none are even, the probability is $1-(\frac{3}{5} \cdot \frac{2}{4})=1-\frac{3}{10}=0.7 \Longrightarrow \boxed{\textbf{(D) }0.7}$ . ~Alternate solve by JH. L

## Solution 2
There are $2$ cases to get an even number. Case 1: $\text{Even} \times \text{Even}$ and Case 2: $\text{Odd} \times \text{Even}$ . Thus, to get an $\text{Even} \times \text{Even}$ , you get $\frac {\binom {2}{2}}{\binom {5}{2}}= \frac {1}{10}$ . And to get $\text{Odd} \times \text{Even}$ , you get $\frac {\binom {3}{1} \binom {2}{1}}{\binom {5}{2}}= \frac {6}{10}$ . $\frac {1}{10}+\frac {6}{10}=\frac {7}{10}$ which is $0.7$ and the answer is $\boxed{\textbf{(D) }0.7}$ .

## Solution 3
Note that we have three cases to get an even number: even $\times$ even, odd $\times$ even and even $\times$ odd. The probability of case 1 is $\dfrac{2}{5}\cdot\dfrac{1}{4}$ , the probability of case 2 is $\dfrac{2}{5}\cdot\dfrac{3}{4}$ and the probability of case 3 is $\dfrac{3}{5}\cdot\dfrac12$ .
Adding these up we get $\dfrac{1}{10}+\dfrac{3}{10}+\dfrac{3}{10} = \boxed{\textbf{(D) }0.7}.$
-ConfidentKoala4

## Video Solution by OmegaLearn
https://youtu.be/IRyWOZQMTV8?t=933
~ pi_is_3.14

## Video Solution
https://youtu.be/tUpKpGmOwDQ - savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .