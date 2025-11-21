# 2002 AIME I Problem 1

## Problem

Many states use a sequence of three letters followed by a sequence of three digits as their standard license-plate pattern. Given that each three-letter three-digit arrangement is equally likely, the probability that such a license plate will contain at least one palindrome (a three-letter arrangement or a three-digit arrangement that reads the same left-to-right as it does right-to-left) is $\dfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1
Consider the three-digit arrangement, $\overline{aba}$ . There are $10$ choices for $a$ and $10$ choices for $b$ (since it is possible for $a=b$ ), and so the probability of picking the palindrome is $\frac{10 \times 10}{10^3} = \frac 1{10}$ . Similarly, there is a $\frac 1{26}$ probability of picking the three-letter palindrome.
By the Principle of Inclusion-Exclusion , the total probability is

## Solution 2
Using complementary counting, we count all of the license plates that do not have the desired property. To not be a palindrome, the first and third characters of each string must be different. Therefore, there are $10\cdot 10\cdot 9$ three-digit non-palindromes, and there are $26\cdot 26\cdot 25$ three-letter non-palindromes. As there are $10^3\cdot 26^3$ total three-letter three-digit arrangements, the probability that a license plate does not have the desired property is $\frac{10\cdot 10\cdot 9\cdot 26\cdot 26\cdot 25}{10^3\cdot 26^3}=\frac{45}{52}$ . We subtract this from 1 to get $1-\frac{45}{52}=\frac{7}{52}$ as our probability. Therefore, our answer is $7+52=\boxed{59}$ .
~minor edit by Yiyj1

## Solution 3
Note that we can pick the first and second letters/numbers freely with one choice left for the last letter/number for there to be a palindrome. Thus, the probability of no palindrome is \[\frac{25}{26}\cdot \frac{9}{10}=\frac{45}{52}\] thus we have $1-\frac{45}{52}=\frac{7}{52}$ so our answer is $7+52 = \boxed{59}.$
~Dhillonr25

## Solution 4
We can find the probability of getting a letter and number palindrome through Solution One, which gives us $\frac{1}{26},$ and $\frac{1}{10},$ respectively. Then, we can use casework to solve the question. We begin by creating the cases:
\begin{align*} \bullet\ \text{Case 1: The license plate includes only a letter palindrome, and no number palindrome} \\ \bullet\ \text{Case 2: The license plate includes only a number palindrome, and no letter palindrome} \\ \bullet\ \text{Case 3: The license plate includes both a number palindrome, and a letter palindrome} \end{align*}
We know that the complement of these probabilities gives us the probability that the numbers and letters are NOT palindromes, so we can use that in our cases to get:
\begin{align} \frac{1}{26} \cdot \frac{9}{10} &= \frac{9}{260} & \text{Case 1}\\ \frac{25}{26} \cdot \frac{1}{10} &= \frac{25}{260} & \text{Case 2}\\ \frac{1}{26} \cdot \frac{1}{10} &= \frac{1}{260} & \text{Case 3} \end{align}
Finally, we can add them all together to get: $\frac{9 + 25 + 1}{260} = \frac{35}{260} = \frac{7}{52} = \frac{m}{n}.$ Thus, we have $m + n = \boxed{059}.$
~ Cheetahboy93

## Video Solution by OmegaLearn
https://youtu.be/jRZQUv4hY_k?t=98
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.