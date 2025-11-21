# 2011 AMC 10B Problem 13

## Problem

Two real numbers are selected independently at random from the interval $[-20, 10]$ . What is the probability that the product of those numbers is greater than zero?

$\textbf{(A)}\ \frac{1}{9} \qquad\textbf{(B)}\ \frac{1}{3} \qquad\textbf{(C)}\ \frac{4}{9} \qquad\textbf{(D)}\ \frac{5}{9} \qquad\textbf{(E)}\ \frac{2}{3}$

## Solution
For the product of two numbers to be greater than zero, they either have to both be negative or both be positive. The interval for a positive number is $\frac{1}{3}$ of the total interval, and the interval for a negative number is $\frac{2}{3}$ . Therefore, the probability the product is greater than zero is \[\frac{1}{3} \times \frac{1}{3} + \frac{2}{3} \times \frac{2}{3} = \frac{1}{9} + \frac{4}{9} = \boxed{\textbf{(D)} \frac{5}{9}}\]

## Solution 2
We can plot this problem on the coordinate grid. First, plot the possible region [the square with endpoints $(10,10), (-20, 10), (-20, -20), (10, -20)$ ]. Including quadrant 3 and 4 allows for the second number selected to be negative. Then, we can find our possible region which is if both numbers are positive or if both numbers are negative. Lets take the first case in which both numbers are positive: The region which has these desired values is the square [ $(10,10) ,(0,0) ,(10,0) ,(0,10)$ ]. Similarly if both numbers are negative we get the square [ $(-20,-20), (0,0), (-20,0) ,(0,-20)$ ] Then we find the area of the possible region $30\cdot 30 = 900$ and then find the areas of our positive regions $10\cdot 10=100$ and $20\cdot 20 = 400$ . Adding and simplifying we get $\frac{100+400}{900}=\frac{5}{9}$ .

## Solution 3
We will use complementary counting. The probability that the product is negative can be found by finding the probability that one number is positive and the other number is negative. The probability of a positive number being selected is $\frac13$ , and the probability of a negative number being selected is $\frac23$ . So, we see that the probability of the product being negative is \[2 \cdot \frac23 \cdot \frac13 = \frac49.\]
We multiply by $2$ because you can either pick the negative or positive number first.
Thus, the probability of the product being positive is \[1-\frac49 = \boxed{\textbf{(D) }\frac59}\]

## Solution 4
We can simplify the problem down by dividing the boundary numbers by 10, which gives us $[-2,1]$ . Then, it is easier for us to come to Solution 2. The probability the product is greater than zero is \[\frac{1}{3} \times \frac{1}{3} + \frac{2}{3} \times \frac{2}{3} = \frac{1}{9} + \frac{4}{9} = \boxed{\textbf{(D)} \frac{5}{9}}\]
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .