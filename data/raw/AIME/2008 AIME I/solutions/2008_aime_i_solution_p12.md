# 2008 AIME I Problem 12

## Problem

On a long straight stretch of one-way single-lane highway, cars all travel at the same speed and all obey the safety rule: the distance from the back of the car ahead to the front of the car behind is exactly one car length for each 15 kilometers per hour of speed or fraction thereof (Thus the front of a car traveling 52 kilometers per hour will be four car lengths behind the back of the car in front of it.) A photoelectric eye by the side of the road counts the number of cars that pass in one hour. Assuming that each car is 4 meters long and that the cars can travel at any speed, let $M$ be the maximum whole number of cars that can pass the photoelectric eye in one hour. Find the quotient when $M$ is divided by $10$ .

## Solution 1
Let $n$ be the number of car lengths that separates each car (it is easy to see that this should be the same between each pair of consecutive cars.) Then their speed is at most $15n$ . Let a unit be the distance between the cars (front to front). Then the length of each unit is $4(n + 1)$ . To maximize, in a unit, the CAR comes first, THEN the empty space. So at time zero, the car is right at the eye.
Hence, we count the number of units that pass the eye in an hour: $\frac {15,000n\frac{\text{meters}}{\text{hour}}}{4(n + 1)\frac{\text{meters}}{\text{unit}}} = \frac {15,000n}{4(n + 1)}\frac{\text{units}}{\text{hour}}$ . We wish to maximize this.
Observe that as $n$ gets larger, the $+ 1$ gets less and less significant, so we take the limit as $n$ approaches infinity
Now, as the speeds are clearly finite, we can never actually reach $3750$ full UNITs. However, we only need to find the number of CARS. We can increase their speed so that the camera stops (one hour goes by) after the car part of the $3750$ th unit has passed, but not all of the space behind it. Hence, $3750$ cars is possible, and the answer is $\boxed {375}$ .

## Solution 2
Disclaimer: This is for the people who may not understand calculus, and is also how I did it. First, we assume several things. First, we assume the speeds must be multiples of 15 to maximize cars, because any less will be a waste. Second, we start with one car in front of the photoelectric eye. We first set the speed of the cars as $15k$ . Then, the distance between them is $\frac{4}{1000} \times k\text{km}$ . Therefore, it takes the car closest to the eye not on the eye $\frac{\frac{k}{250}}{15k}$ hours to get to the eye. There is one hour, so the amount of cars that can pass is $\frac{1}{\frac{\frac{k}{250}}{15k}}$ , or $3750$ cars. When divided by ten, you get the quotient of $\boxed{375}$

## Solution 3
Call the speed of each car $s$ , so that the distance between each car will be $\lfloor a/15 \rfloor$ . To maximize the number of cars that pass, let the first car back end line up with the eye. Notice that every $4/1000+ (4/1000)(\lfloor a/15 \rfloor)$ kilometers (distance from front of one car to the front of the consecutive car), one car will be captured. The time it takes to travel this distance is $\frac{4/1000+(4/1000)(\lfloor a/15 \rfloor)}{a}$ , and the number of these intervals in an hour is $\frac{1}{\frac{4/1000+(4/1000)(\lfloor a/15 \rfloor)}{a}}=\frac{250a}{1+\lfloor a/15 \rfloor}$ . Now, let $a=15n$ and we can proceed with Solution 1.

## Video Solution
2008 AIME I #12
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.