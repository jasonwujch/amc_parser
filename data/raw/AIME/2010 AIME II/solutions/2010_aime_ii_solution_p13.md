# 2010 AIME II Problem 13

## Problem

The $52$ cards in a deck are numbered $1, 2, \cdots, 52$ . Alex, Blair, Corey, and Dylan each picks a card from the deck without replacement and with each card being equally likely to be picked, The two persons with lower numbered cards form a team, and the two persons with higher numbered cards form another team. Let $p(a)$ be the probability that Alex and Dylan are on the same team, given that Alex picks one of the cards $a$ and $a+9$ , and Dylan picks the other of these two cards. The minimum value of $p(a)$ for which $p(a)\ge\frac{1}{2}$ can be written as $\frac{m}{n}$ . where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
Once the two cards are drawn, there are $\dbinom{50}{2} = 1225$ ways for the other two people to draw. Alex and Dylan are the team with higher numbers if Blair and Corey both draw below $a$ , which occurs in $\dbinom{a-1}{2}$ ways. Alex and Dylan are the team with lower numbers if Blair and Corey both draw above $a+9$ , which occurs in $\dbinom{43-a}{2}$ ways. Thus, \[p(a)=\frac{\dbinom{43-a}{2}+\dbinom{a-1}{2}}{1225}.\] Simplifying, we get $p(a)=\frac{(43-a)(42-a)+(a-1)(a-2)}{2\cdot1225}$ , so we need $(43-a)(42-a)+(a-1)(a-2)\ge (1225)$ . If $a=22+b$ , then \begin{align*}(43-a)(42-a)+(a-1)(a-2)&=(21-b)(20-b)+(21+b)(20+b)=2b^2+2(21)(20)\ge (1225) \\ b^2\ge \frac{385}{2} &= 192.5 >13^2 \end{align*} So $b> 13$ or $b< -13$ , and $a=22+b<9$ or $a>35$ , so $a=8$ or $a=36$ . Thus, $p(8) = \frac{616}{1225} = \frac{88}{175}$ , and the answer is $88+175 = \boxed{263}$ .

## Solution 2
Given that Alex and Dylan hold the cards $a$ and $a+9$ , we need to calculate the probability that they end up on the same team. This happens in two scenarios:
1. Both on the Lower Team: This occurs if the other two cards drawn are both greater than $a+9$ . 2. Both on the Higher Team: This occurs if the other two cards drawn are both less than $a$ .
The total number of ways to choose the other two cards from the remaining 50 cards is $\binom{50}{2} = 1225$ .
The number of favorable outcomes is the sum of: The number of ways to choose 2 cards greater than $a+9$ : $\binom{43-a}{2}$ The number of ways to choose 2 cards less than $a$ : $\binom{a-1}{2}$
Thus, the probability $p(a)$ is: \[p(a) = \frac{\binom{a-1}{2} + \binom{43-a}{2}}{\binom{50}{2}} = \frac{\frac{(a-1)(a-2)}{2} + \frac{(43-a)(42-a)}{2}}{1225}.\]
Finding the Minimum $a$ for $p(a) \geq \frac{1}{2}$
Solving the inequality: \[\frac{\binom{a-1}{2} + \binom{43-a}{2}}{1225} \geq \frac{1}{2}\] leads to: \[2(a^2 - 44a + 291) \geq 0.\]
This quadratic inequality is satisfied when $a \leq 8$ or $a \geq 36$ .
The minimum value of $p(a)$ that satisfies $p(a) \geq \frac{1}{2}$ occurs at $a = 8$ (or symmetrically at $a = 36$ ), giving: \[p(8) = \frac{616}{1225} = \frac{88}{175}\] where $88$ and $175$ are coprime.
Final Answer \[88 + 175 = 263\]
Answer: $263$
~ Athmyx
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .