# 2000 AIME II Problem 5

## Problem

Given eight distinguishable rings, let $n$ be the number of possible five-ring arrangements on the four fingers (not the thumb) of one hand. The order of rings on each finger is significant, but it is not required that each finger have a ring. Find the leftmost three nonzero digits of $n$ .

## Solution
There are $\binom{8}{5}$ ways to choose the rings, and there are $5!$ distinct arrangements to order the rings [we order them so that the first ring is the bottom-most on the first finger that actually has a ring, and so forth]. The number of ways to distribute the rings among the fingers is equivalent the number of ways we can drop five balls into 4 urns, or similarly dropping five balls into four compartments split by three dividers. The number of ways to arrange those dividers and balls is just $\binom {8}{3}$ .
Multiplying gives the answer: $\binom{8}{5}\binom{8}{3}5! = 376320$ , and the three leftmost digits are $\boxed{376}$ .

## Solution 2
There are $\binom{8}{5}$ to choose the rings. Now, call the rings $A$ , $B$ , $C$ , $D$ , and $E$ . Any possible ring combination can be generating by scrambling $ABCDE$ and adding three dividers - the things to the left of the first divider will be on the first finger, the things between the first and the second will be on the second finger, and so on. For example, $A|D||CBE$ represents ring $A$ on the first finger, $D$ on the second, none on the third, and $C$ , $B$ , and $E$ in that order on the fourth. In other words, we simply need to count the number of distinguishable rearrangements of $ABCDE|||$ . There are $\frac{8!}{3!}$ of them.
Thus the total number of ways is $\binom{8}{5}\frac{8!}{3!} = 376320$ and we submit $\boxed{376}$ .
~ NamelyOrange
These problems are copyrighted © by the Mathematical Association of America.