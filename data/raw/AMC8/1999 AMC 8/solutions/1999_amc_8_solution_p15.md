# 1999 AMC 8 Problem 15

## Problem

Bicycle license plates in Flatville each contain three letters. The first is chosen from the set {C,H,L,P,R}, the second from {A,I,O}, and the third from {D,M,N,T}.

When Flatville needed more license plates, they added two new letters. The new letters may both be added to one set or one letter may be added to one set and one to another set. What is the largest possible number of ADDITIONAL license plates that can be made by adding two letters?

$\text{(A)}\ 24 \qquad \text{(B)}\ 30 \qquad \text{(C)}\ 36 \qquad \text{(D)}\ 40 \qquad \text{(E)}\ 60$

## Solution

## Solution 1
There are currently $5$ choices for the first letter, $3$ choices for the second letter, and $4$ choices for the third letter, for a total of $5 \cdot 3 \cdot 4 = 60$ license plates.
Adding $2$ letters to the start gives $7\cdot 3 \cdot 4 = 84$ plates.
Adding $2$ letters to the middle gives $5 \cdot 5 \cdot 4 = 100$ plates.
Adding $2$ letters to the end gives $5 \cdot 3 \cdot 6 = 90$ plates.
Adding a letter to the start and middle gives $6 \cdot 4 \cdot 4 = 96$ plates.
Adding a letter to the start and end gives $6 \cdot 3 \cdot 5 = 90$ plates.
Adding a letter to the middle and end gives $5 \cdot 4 \cdot 5 = 100$ plates.
You can get at most $100$ license plates total, giving an additional $100 - 60 = 40$ plates, making the answer $\boxed {D}$

## Solution 2
Using the same logic as above, the number of combinations of plates is simply the product of the size of each set of letters.
In general, when three numbers have the same fixed sum, their product will be maximal when they are as close together as possible. This is a 3D analogue of the fact that a rectangle with fixed perimeter maximizes its area when the sides are equal (ie when it becomes a square). In this case, no matter where you add the letters, there will be $5 + 3 + 4 + 2 = 14$ letters in total. If you divide them as evenly as possible among the three groups, you get $5, 5, 4$ , which is a possible situation.
As before, the answer is $5 \cdot 5 \cdot 4 - 5 \cdot 3 \cdot 4 = 40$ , and the correct choice is $\boxed{D}$

## Solution 3
Before new letters were added, five different letters could have been chosen for the first position, three for the second, and four for the third. This means that $5\cdot 3\cdot 4=60$ plates could have been made.
If two letters are added to the second set, then $5\cdot 5\cdot 4=100$ plates can be made. If one letter is added to each of the second and third sets, then $5\cdot 4\cdot 5=100$ plates can be made. None of the other four ways to place the two letters will create as many plates. So, $100-60=\boxed{40}$ ADDITIONAL plates can be made.So the correct choice is $\boxed{D}$

## Video Solution
https://youtu.be/t_tvXQ_30ZA Soo, DRMS, NM
### See Also