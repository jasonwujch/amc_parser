# 2007 AIME I Problem 2

## Problem

A 100 foot long moving walkway moves at a constant rate of 6 feet per second. Al steps onto the start of the walkway and stands. Bob steps onto the start of the walkway two seconds later and strolls forward along the walkway at a constant rate of 4 feet per second. Two seconds after that, Cy reaches the start of the walkway and walks briskly forward beside the walkway at a constant rate of 8 feet per second. At a certain time, one of these three persons is exactly halfway between the other two. At that time, find the distance in feet between the start of the walkway and the middle person.

## Solution
Clearly we have people moving at speeds of $6,8$ and $10$ feet/second. Notice that out of the three people, Cy is at the largest disadvantage to begin with and since all speeds are close, it is hardest for him to catch up. Furthermore, Bob is clearly the farthest along. Thus it is reasonable to assume that there is some point when Al is halfway between Cy and Bob. At this time $s$ , we have that
$\frac{8(s-4)+10(s-2)}{2}=6s$ After solving, $s=\frac{26}{3}$ . At this time, Al has traveled $6\cdot\frac{26}{3}=52$ feet.
We could easily check that Al is in the middle by trying all three possible cases. $\frac{6s + 8(s-4)}{2} = 10(s-2)$ yields that $s = \frac 43$ , which can be disregarded since both Bob and Cy hadn't started yet. $\frac{6s + 10(s-2)}{2} = 8(s-4)$ yields that $-10=-32$ , a contradiction. Thus, the answer is $\boxed{052}$ .

## Video Solution by OmegaLearn
https://youtu.be/4WttvHavnkM?t=733
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.