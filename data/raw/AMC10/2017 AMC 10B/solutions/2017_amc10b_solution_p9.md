# 2017 AMC 10B Problem 9

## Problem

A radio program has a quiz consisting of $3$ multiple-choice questions, each with $3$ choices. A contestant wins if he or she gets $2$ or more of the questions right. The contestant answers randomly to each question. What is the probability of winning?

$\textbf{(A)}\ \frac{1}{27}\qquad\textbf{(B)}\ \frac{1}{9}\qquad\textbf{(C)}\ \frac{2}{9}\qquad\textbf{(D)}\ \frac{7}{27}\qquad\textbf{(E)}\ \frac{1}{2}$

## Solution 1
There are two ways the contestant can win.
Case 1: The contestant guesses all three right. This can only happen $\frac{1}{3} * \frac{1}{3} * \frac{1}{3} = \frac{1}{27}$ of the time.
Case 2: The contestant guesses only two right. We pick one of the questions to get wrong, $3$ , and this can happen $\frac{1}{3} * \frac{1}{3} * \frac{2}{3}$ of the time. Thus, $\frac{2}{27} * 3$ = $\frac{6}{27}$ .
So, in total the two cases combined equals $\frac{1}{27} + \frac{6}{27}$ = $\boxed{\textbf{(D)}\ \frac{7}{27}}$ .
More detailed explanation: For case 1, the contestant must guess all three correctly. The probability of guessing one problem right is $\frac{1}{3}$ , so the probability of getting all three right is $\left(\frac{1}{3}\right)^{3}$ . For case 2: we must choose one of the problems to answer incorrectly and two to answer correctly. The probabilities for guessing correctly and incorrectly are $\frac{1}{3}$ and $\frac{2}{3}$ , respectively. So we have $\left(\frac{1}{3}\right)^{2}\cdot\frac{2}{3}\cdot3$ . The answer is the sum of probabilities of case 1 and 2, since there are no overcounts. $\frac{1}{27}+\frac{6}{27}=\frac{7}{27}$ .

## Solution 2 (complementary counting)
Complementary counting is good for solving the problem and checking work if you solved it using the method above.
There are two ways the contestant can lose.
Case 1: The contestant guesses zero questions correctly.
The probability of getting each question incorrect is $\frac{2}{3}$ . Thus, the probability of getting all questions incorrect is $\frac{2}{3} * \frac{2}{3} * \frac{2}{3} = \frac{8}{27}$ .
Case 2: The contestant gets one question right. There are 3 ways the contestant can get one question correct since there are 3 questions. The probability of guessing correctly is $\frac{1}{3}$ so the probability of guessing one correctly and two incorrectly is $\frac{1}{3} * \frac{2}{3} * \frac{2}{3} = \frac{4}{27}$ . Each of these 3 ways has a probability associated with it, so probability of getting 1 correct is $3 * \frac{4}{27} = \frac{4}{9}$
The sum of the two cases is $\frac{8}{27} + \frac{4}{9} = \frac{20}{27}$ . This is the complement of what we want so the answer is $1-\frac{20}{27} = \boxed{\textbf{(D)}\frac{7}{27}}$

## Video Solution
https://youtu.be/XYeexmAyVzQ
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/XRfOULUmWbY?t=482
~IceMatrix

## Video Solution
https://youtu.be/IRyWOZQMTV8?t=1029
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .