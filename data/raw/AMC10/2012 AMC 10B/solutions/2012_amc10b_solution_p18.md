# 2012 AMC 10B Problem 18

## Problem

Suppose that one of every 500 people in a certain population has a particular disease, which displays no symptoms. A blood test is available for screening for this disease. For a person who has this disease, the test always turns out positive. For a person who does not have the disease, however, there is a $2\%$ false positive rate--in other words, for such people, $98\%$ of the time the test will turn out negative, but $2\%$ of the time the test will turn out positive and will incorrectly indicate that the person has the disease. Let $p$ be the probability that a person who is chosen at random from this population and gets a positive test result actually has the disease. Which of the following is closest to $p$ ?

$\textbf{(A)}\ \frac{1}{98}\qquad\textbf{(B)}\ \frac{1}{9}\qquad\textbf{(C)}\ \frac{1}{11}\qquad\textbf{(D)}\ \frac{49}{99}\qquad\textbf{(E)}\ \frac{98}{99}$

## Solution 1
This question can be solved by considering all the possibilities:
$1$ out of $500$ people will have the disease and will be tested positive for the disease.
Out of the remaining $499$ people, $\frac{1}{50}$ , or about $10$ people, will be tested positive for the disease incorrectly.
Therefore, an approximation of $p$ can be found by taking $\dfrac{1}{1 +10}$ , which is $\dfrac{1}{11}$ , or $\boxed{\textbf{(C)}}$

## Solution 2
This question can also be solved by using a $\dfrac{probability1}{probability2}$ solution.
If the test is positive there are two cases: (1) The person was true-positive (2) The person was false-positive
For the first case, the probability of the person being true-positive is $\dfrac{1}{500}$ .
For the second case, the probability of the person being false-positive is $\dfrac{499}{500}\cdot\dfrac{1}{50}$
The probability of the test being positive is the sum of these values, $\dfrac{549}{25000}$
The final probability will be in the form: $\dfrac{P(true positive)}{P(positive)}$ .
Plugging in the values we get: $\dfrac{\dfrac{1}{500}}{\dfrac{549}{25000}}=\dfrac{50}{549}$ This fraction is clearly closest to $\dfrac{1}{11}$ , or $\boxed{\textbf{(C)}}$

## Solution 3
To solve this problem, you need to find the probability of a correctly identified positive and divided by the total probability of a positive.
The probability of obtaining a correctly identified positive is $\dfrac{1}{500}$ .
The probability of obtaining an incorrectly identified positive is $\dfrac{2}{100}$ = $\dfrac{10}{500}$ .
$\dfrac{1}{500}$ + $\dfrac{10}{500}$ = $\dfrac{11}{500}$ = the probability of obtaining a positive.
Correctly identifed positive / positive = $\dfrac{1}{500}$ / $\dfrac{11}{500}$ = $\dfrac{1}{11}$ or $\boxed{\textbf{(C)}}$

## Video Solution
https://youtu.be/igGLCogR-dk
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .