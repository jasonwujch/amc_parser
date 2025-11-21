# 2001 AMC 8 Problem 18

## Problem

Two dice are thrown. What is the probability that the product of the two numbers is a multiple of 5?

$\text{(A)}\ \dfrac{1}{36} \qquad \text{(B)}\ \dfrac{1}{18} \qquad \text{(C)}\ \dfrac{1}{6} \qquad \text{(D)}\ \dfrac{11}{36} \qquad \text{(E)}\ \dfrac{1}{3}$

## Solution 1
This is equivalent to asking for the probability that at least one of the numbers is a multiple of $5$ , since if one of the numbers is a multiple of $5$ , then the product with it and another integer is also a multiple of $5$ , and if a number is a multiple of $5$ , then since $5$ is prime, one of the factors must also have a factor of $5$ , and $5$ is the only multiple of $5$ on a die, so one of the numbers rolled must be a $5$ . To find the probability of rolling at least one $5$ , we can find the probability of not rolling a $5$ and subtract that from $1$ , since you either roll a $5$ or not roll a $5$ . The probability of not rolling a $5$ on either dice is $\left(\frac{5}{6} \right) \left(\frac{5}{6} \right)=\frac{25}{36}$ . Therefore, the probability of rolling at least one five, and thus rolling two numbers whose product is a multiple of $5$ , is $1-\frac{25}{36}=\frac{11}{36}, \boxed{\text{D}}$

## Solution 2 (quick & easy)
The only way to get a multiple of $5$ is to have at least one $5$ . If the first dice rolls a $5$ , there are $6$ ways to get a multiple of $5$ . If the second dice rolls a $5$ , there are also $6$ ways. However, one case is repeated: both dice roll a $5$ . Therefore, there are $6 + 6 - 1 = 11$ , and there is a total of $6 \times 6$ ways, so the probability is $\text{(D)}\ \dfrac{11}{36}$
Solution by ILoveMath31415926535

## Video Solution
https://youtu.be/4aX9-DZHgNw Soo, DRMS, NM
### See Also