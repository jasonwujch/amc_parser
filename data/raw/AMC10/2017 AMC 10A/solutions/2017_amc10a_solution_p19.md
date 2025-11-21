# 2017 AMC 10A Problem 19

## Problem

Alice refuses to sit next to either Bob or Carla. Derek refuses to sit next to Eric. How many ways are there for the five of them to sit in a row of $5$ chairs under these conditions?

$\textbf{(A)}\ 12\qquad\textbf{(B)}\ 16\qquad\textbf{(C)}\ 28\qquad\textbf{(D)}\ 32\qquad\textbf{(E)}\ 40$

## Solution 1: Casework
Let Alice be A, Bob be B, Carla be C, Derek be D, and Eric be E. We can split this problem up into two cases:
$\textbf{Case 1: }$ A sits on an edge seat.
Since B and C can't sit next to A, that must mean either D or E sits next to A. After we pick either D or E, then either B or C must sit next to D/E. Then, we can arrange the two remaining people in two ways. Since there are two different edge seats that A can sit in, there are a total of $2 \cdot 2 \cdot 2 \cdot 2 = 16$ .
$\textbf{Case 2: }$ A does not sit in an edge seat.
Still, the only two people that can sit next to A are either D or E, and there are two ways to permute them, and this also handles the restriction that D can't sit next to E. Then, there are two ways to arrange B and C, the remaining people. However, there are three initial seats that A can sit in, so there are $3 \cdot 2 \cdot 2 = 12$ seatings in this case.
Adding up all the seatings, we have $16+12 = \boxed{\textbf{(C) } 28}$ .
Minor clarity edits by SwordAxe

## Solution 2
Label the seats (from left to right) $1$ through $5$ . The number of ways to seat Derek and Eric in the five seats with no restrictions is $5 \cdot 4=20$ . The number of ways to seat Derek and Eric such that they sit next to each other is $8$ (we can treat Derek and Eric as a "block". There are four ways to seat this "block", and two ways to permute Derek and Eric, for a total of $4\cdot 2=8$ ), so the number of ways such that Derek and Eric don't sit next to each other is $20-8=12$ . Note that once Derek and Eric are seated, we can divide into three cases.
The first case is that they sit at each end. There are two ways to seat Derek and Eric. But this is impossible because then Alice, Bob, and Carla would have to sit in some order in the middle three seats which would lead to Alice sitting next to Bob or Carla, a contradiction. So this case gives us $0$ ways.
Another possible case is if Derek and Eric sit in seats $2$ and $4$ in some order. There are $2$ possible ways to seat Derek and Eric like this. This leaves Alice, Bob, and Carla to sit in any order in the remaining three seats. Since no two of these three seats are consecutive, there are $3!=6$ ways to do this. So the second case gives us $2 \cdot 6=12$ total ways.
The last case is if once Derek and Eric are seated, exactly one pair of consecutive seats are available. There are $12-2-2=8$ ways to seat Derek and Eric like this. Once they are seated like this, Alice cannot sit in one of the two consecutive available seats without sitting next to Bob or Carla. So Alice has to sit in the other remaining chair. Then, there are two ways to seat Bob and Carla in the remaining two seats (which are consecutive). So this case gives us $8 \cdot 2=16$ ways.
So in total there are $12+16=28$ ways. Our answer is $\boxed{\textbf{(C)}\ 28}$ . Minor $\LaTeX$ edits by fasterthanlight :)
Minor clarity edits by Carrot_Karen

## Solution 3: PIE
We start with complementary counting. After all, it's much easier to count the cases where some of these restraints are true, than when they aren't.
PIE (principle of inclusion and exclusion): Let's count the total number of cases where one of these is true:
When Alice is with Bob: $2\cdot4!=48$
When Alice is with Carla: $2\cdot4!=48$
When Derek is with Eric: $2\cdot4!=48$
Then, we count the cases where two of these are true.
Alice is next to Carla, and Alice is also next to Bob. There are two ways to rearrange Alice, Bob, and Carla so that this is true: BAC and CAB. $2\cdot3!=12$
Alice is next to Carla, and Derek is also next to Eric. $2\cdot2\cdot3!=24$
Alice is next to Bob, and Derek is also next to Eric. $2\cdot2\cdot3!=24$
Finally, we count the cases where all three of these are true: $2\cdot2\cdot2=8$
We add up the cases where one of these are true: $48\cdot3=144$
Subtract the cases where two of these are true: $144-60=84$
And finally add back the cases where three of these are true: $84+8=92$
Thus, our answer is $5!-92=28$ , or $\boxed{\textbf{(C)} ~28}$
~gladIasked
~minor edit by lapisluminous ty
~minor edit by SwordAxe
~minor clarity edits by hpotter2021

## Solution 4: Enumeration and casework of Alice's position
To find the number of ways, we do casework.
Case 1: Alice sits in the first seat (leftmost) Since Alice refuses to sit with Bob and Carla, then the seat on her immediate right must be Derek or Eric. The middle seat must be Bob or Carla (because Derek and Eric refuse to sit together). The seat to the right of the middle seat could be whoever is left over from Derek and Eric, or whoever is left together from Bob and Carla. The last seat only has one person left. There are $4$ ways to permute Bob, Carla, Derek, and Eric, and $2$ ways to pick who goes in the seat to the right of the middle seat, for $4\cdot2=8$ seating arrangements here.
Case 2: Alice sits in the second seat Derek and Eric must be on both sides of Alice because otherwise, we would have to put Bob or Carla next to Alice which is forbidden. Then Bob and Carla take the remaining two seats. There are $4$ ways to permute and $4$ arrangements here.
Case 3: Alice sits in the middle seat Once again, Derek and Eric must be on both sides of Alice, and Bob and Carla need to take the two remaining seats. There are also $4$ ways to permute and $4$ arrangements here.
Case 4: Alice sits in the fourth seat By symmetry, this is the same as case 2. There are $4$ arrangements.
Case 5: Alice sits in the last seat (rightmost) By symmetry, this is the same as case 1. There are $8$ arrangements.
Adding up the cases, there are $8+4+4+4+8=28$ total seating arrangements $\Longrightarrow \boxed{\textbf{(C) } 28}$
~JH. L
P.S. For this question, it is possible and slightly less insanity-inducing to list out every combination and make an educated guess from there, but is not recommended unless you've given up all hope from doing the solutions above this one :P

## Video Solution by OmegaLearn
https://youtu.be/5UojVH4Cqqs?t=2101
~ pi_is_3.14

## Video Solution
https://youtu.be/umr2Aj9ViOA
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .