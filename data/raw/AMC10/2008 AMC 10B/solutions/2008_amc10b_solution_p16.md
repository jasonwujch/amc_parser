# 2008 AMC 10B Problem 16

## Problem

Two fair coins are to be tossed once. For each head that results, one fair die is to be rolled. What is the probability that the sum of the die rolls is odd? (Note that if no die is rolled, the sum is 0.)

$\mathrm{(A)}\ {{{\frac{3} {8}}}} \qquad \mathrm{(B)}\ {{{\frac{1} {2}}}} \qquad \mathrm{(C)}\ {{{\frac{43} {72}}}} \qquad \mathrm{(D)}\ {{{\frac{5} {8}}}} \qquad \mathrm{(E)}\ {{{\frac{2} {3}}}}$

## Solution 1 (Casework)
We consider 3 cases based on the outcome of the coin:
Case 1, 0 heads: The probability of this occurring on the coin flip is $\frac{1} {4}$ . The probability that 0 rolls of a die will result in an odd sum is $0$ .
Case 2, 1 head: The probability of this case occurring is $\frac{1} {2} \cdot \frac {1} {2} \cdot 2 = \frac {1} {2}.$ The probability that 1 die results in an odd number is $\frac{1} {2}$ .
Case 3, 2 heads: The probability of this occurring is $\frac{1} {4}$ . The probability that 2 dice result in an odd sum is $\frac{1} {2}$ , because regardless of what we throw on the first die, we have $\frac{1} {2}$ probability that the second die will have the opposite parity.
Thus, the probability of having an odd sum rolled is $\frac{1} {4} \cdot 0 + \frac{1} {2} \cdot \frac{1} {2} + \frac{1} {4} \cdot \frac{1} {2}=\frac{3} {8}\Rightarrow \boxed{A}$

## Solution 2 (possibly slightly faster)
We use complementary counting or subtracting $P(\text{Even})$ from $1$ . We use casework now.
Case $1$ : $2$ Tails. $2$ tails occur with probability $\frac{1}{4}$ , but we will always get an even number, so the overall probability to get an even sum is $\frac{1}{4}$ .
Case $2$ : $1$ Tail: This event occurs with probability $\frac{1}{2}$ and the probability we get an even is $\frac{1}{2}$ , so the overall probability to get an even, in this case, is also $\frac{1}{4}$ .
We know $P\text{(Even)}$ is greater than $\frac{1}{2}$ , so $P\text{(Odd)}$ is less than $\frac{1}{2}$ .
Only $\boxed{\text{(A)}\frac{3}{8}}$ is less than $\frac{1}{2}$ .

## Solution 3
When rolling one or two dice, the probability of the sum being odd is equivalent to the probability of the sum being even. However, if we flip no heads, meaning we roll no dice, the sum is always even. Hence, the probability that the sum of the dice is even is ( 1 - the probability of flipping no heads ) / 2. Solving, we get that the answer is (1 - $\frac{1}{4}$ ) / 2 = $\frac{3}{8}$ .

## Solution 4 (Very Fast)
0 heads: If you are not rolling the dice, then it is an even number (0). 1 heads: If you are rolling 1 dice, the probability is 1/2, the same as odd. 2 heads: When you are rolling 2 dices, there are 2 choices for odd (O,E) (E,O) while there are also 2 choices for even (E,E) (O,O). In total, the chances of rolling an even is more than rolling an odd (More, Same, Same). So, the answer must be less than half and the only answer choice that satisfies this is answer choice (A).
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .