# 2018 AMC 10B Problem 9

## Problem

The faces of each of $7$ standard dice are labeled with the integers from $1$ to $6$ . Let $p$ be the probabilities that when all $7$ dice are rolled, the sum of the numbers on the top faces is $10$ . What other sum occurs with the same probability as $p$ ?

$\textbf{(A)} \text{ 13} \qquad \textbf{(B)} \text{ 26} \qquad \textbf{(C)} \text{ 32} \qquad \textbf{(D)} \text{ 39} \qquad \textbf{(E)} \text{ 42}$

## Solution 1
The number 10 can be achieved by \( 4+6 \), \( 5+5 \), \( 6+4 \), in which there must exist at least 5 number ones.
Thus, we can write an answer in the form \( 1 + 1 + 1 + 1 + 1 + x + y \), where \( x + y \) must sum to 5. We notice that \( x + y = 5 \) can be either \( 1 + 4 \), \( 2 + 3 \), \( 3 + 2 \), or \( 4 + 1 \). So \( x + y = 4\) cases.
The question now is which of the following answer choices can be written as a 5 term consecutive sum with the last two numbers \( x\) and \(y\) having exactly 4 cases.
We first take E. 42. We see that we can have 5 consecutive number 6's to get 30. We then have a remaining 12, which can be represented as 6 + 6 only, not giving us our wanted 4 cases.
We try D. 39. We see we can write this as 5 consecutive number 6's. This gives us a remainder of 9, which can be written as 6+3, 4+5, 5+4, or 3+6, giving us 4 cases, exactly like the cases we got for 10.
Our answer is therefore $\boxed{\textbf{(D)} \text{ 39}}$ .
~Pinotation

## Solution 1.1
If you wish to check your answer.
32 = a consecutive number 5's or 6's, gives a remainder of 7 and 2 respectively.
The consecutive number of 6's obviously doesn't work.
The consecutive number of 5's gives the remainder 7, which is \( 1+6 \), \( 2 + 5 \), \( 3+4 \), \( 4+3 \), \( 5+2 \), \( 6+1 \), which is 6 cases and not 4.
26 is either consecutive 5's or 4's.
This gives a remainder of 1 or 6. 1 obviously doesn't work. 6 is \( 1+5 \), \( 2+4 \), \( 3+3 \), \( 4+2 \), or \( 5+1 \), which is 5 cases, not 4.
13 is consecutive 2's or 1's, giving a remainder of 3 and 7 respectively.
We see that 3 doesn't work, and we already know that 7 doesn't work either.
~Pinotation

## Solution 2
It can be seen that the probability of rolling the smallest number possible is the same as the probability of rolling the largest number possible, the probability of rolling the second smallest number possible is the same as the probability of rolling the second largest number possible, and so on. This is because the number of ways to add a certain number of ones to an assortment of $7$ ones is the same as the number of ways to take away a certain number of ones from an assortment of $7$ $6$ s.
So, we can match up the values to find the sum with the same probability as $10$ . We can start by noticing that $7$ is the smallest possible roll and $42$ is the largest possible roll. The pairs with the same probability are as follows:
$(7, 42), (8, 41), (9, 40), (10, 39), (11, 38)...$
However, we need to find the number that matches up with $10$ . So, we can stop at $(10, 39)$ and deduce that the sum with equal probability as $10$ is $39$ . So, the correct answer is $\boxed{\textbf{(D)} \text{39}}$ , and we are done.
Written By: Archimedes15
Add-on by ike.chen: to see how the number of ways to roll $10$ and $39$ are the same, consider this argument:
Each of the $7$ dice needs to have a nonnegative value; it follows that the number of ways to roll $10$ is $\binom {10-1}{7-1}=84$ by stars and bars. $10-7=3$ , so there's no chance that any dice has a value $>6$ .
Now imagine $7$ piles with $6$ blocks each. The number of ways to take $3$ blocks away (making the sum $7\cdot 6-3=39$ ) is also $\binom {3+7-1}{7-1}=84$ .
correction to the add-on: the die need a positive value. We first give every die 1 so we have $10-7=3$ "balls" left to put into the 7 more bins/die. a dice can have a value of 0 for the # of added balls. Thus, from stars and bars it follows that there are $\binom{7+3-1}{7-1}=84$ ways
~mathboy282

## Solution 3
Let's call the unknown value $x$ . By symmetry, we realize that the difference between 10 and the minimum value of the rolls is equal to the difference between the maximum and $x$ . So,
$10 - 7 = 42- x$
$x = 39$ and our answer is $\boxed{\textbf{(D)} \text{ 39}}$ By: Soccer_JAMS

## Solution 4
For the sums to have equal probability, the average sum of both sets of $7$ dies has to be $(6+1)\cdot 7 = 49$ . Since having $10$ is similar to not having $10$ , you just subtract 10 from the expected total sum. $49 - 10 = 39$ so the answer is $\boxed{\textbf{(D)} \text{ 39}}$
By: epicmonster
Revised solution by Williamgolly (includes bijections): Notice that we first must have at least a 1 on each die. Now, we form the following bijection: biject each value on the original die, say $x$ to a value $7-x$ on the new die. Notice how now we need to 'take away' 3 from seven dies that all show 6. Therefore, the answer is 39.

## Solution 5
The expected value of the sums of the die rolls is $3.5\cdot7=24.5$ , and since the probabilities should be distributed symmetrically on both sides of $24.5$ , the answer is $24.5+(24.5-10)=39$ , which is $\boxed{\textbf{(D)} \text{ 39}}$ .
By: dajeff

## Solution 6
Another faster and easier way of doing this, without using almost any math at all, is realizing that the possible sums are ${7,8,9,10,...,39,40,41,42}$ . By symmetry, (and doing a few similar problems in the past), you can realize that the probability of obtaining $7$ is the same as the probability of obtaining $42$ , $P(8)=P(41)$ and on and on and on. This means that $P(10)=P(39)$ , and thus the correct answer is $\boxed{\textbf{(D)} \text{ 39}}$ .
By: fhdsaukfaioifk
### Note
Calculating the probability of getting a sum of $10$ is also easy. There are $3$ cases:
Case $1$ : $\{1,1,1,1,1,1,4\}$
${7 \choose 6}=7$ cases
Case $2$ : $\{1,1,1,1,1,2,3\}$
${7 \choose 5}=6 \cdot 7=42$ cases
Case $3$ : $\{1,1,1,1,2,2,2\}$
${7 \choose 4}=\frac {7 \cdot 6 \cdot 5}{3 \cdot 2}=35$ cases
The probability is ${84 \over 6^7} = \frac{14}{6^6}$ .
Calculating $6^6$ :
$6^6=(6^3)^2=216^2=46656$
Therefore, the probability is ${14 \over 46656} = \boxed{{7 \over 23328}}$
~Zeric Hang (Main writer) and fhdsaukfaioifk (Editor)
### Related Problems
There is similar to problem 11 of the AMC 10A in the same year, which is almost a replica of the problem mentioned by Zeric Hang in the Note section: https://artofproblemsolving.com/wiki/index.php/2018_AMC_10A_Problems/Problem_11

## Video Solution
https://youtu.be/odHniGWWLvw
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .