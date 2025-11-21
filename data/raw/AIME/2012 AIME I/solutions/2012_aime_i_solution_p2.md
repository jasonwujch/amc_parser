# 2012 AIME I Problem 2

## Problem

The terms of an arithmetic sequence add to $715$ . The first term of the sequence is increased by $1$ , the second term is increased by $3$ , the third term is increased by $5$ , and in general, the $k$ th term is increased by the $k$ th odd positive integer. The terms of the new sequence add to $836$ . Find the sum of the first, last, and middle terms of the original sequence.

## Solutions

## Solution 1
If the sum of the original sequence is $\sum_{i=1}^{n} a_i$ then the sum of the new sequence can be expressed as $\sum_{i=1}^{n} a_i + (2i - 1) = n^2 + \sum_{i=1}^{n} a_i.$ Therefore, $836 = n^2 + 715 \rightarrow n=11.$ Now the middle term of the original sequence is simply the average of all the terms, or $\frac{715}{11} = 65,$ and the first and last terms average to this middle term, so the desired sum is simply three times the middle term, or $\boxed{195}.$
Alternatively, notice that in the original sequence, $11a_1 + 55d = 715$ , from which $a_1 + 5d = 65$ . Since we are tasked to find $a_1 + a_6 + a_{11} = 3(a_1 + 5d)$ , the desired answer is $3 \cdot 65 = \boxed{195}.$

## Solution 2
After the adding of the odd numbers, the total of the sequence increases by $836 - 715 = 121 = 11^2$ . Since the sum of the first $n$ positive odd numbers is $n^2$ , there must be $11$ terms in the sequence, so the mean of the sequence is $\dfrac{715}{11} = 65$ . Since the first, last, and middle terms are centered around the mean, our final answer is $65 \cdot 3 = \boxed{195}$

## Solution 3
Proceed as in Solution 2 until it is noted that there are 11 terms in the sequence. Since the sum of the terms of the original arithmetic sequence is 715, we note that $\frac{2a_1 + 10d}{2} \cdot 11 = 715$ or $2a_1 + 10d = 130$ for all sets of first terms and common differences that fit the conditions given in the problem. Assume WLOG that $a_1 = 60$ and $d = 1$ . Then the first term of the corresponding arithmetic sequence will be $60$ , the sixth (middle) term will be $65$ , and the eleventh (largest) term will be $70$ . Thus, our final answer is $60 + 65 + 70 = \boxed{195}$ .
~ cxsmi

## Solution 4 (Similar to the above solutions)
Let the sequence be $a,a+d,a+2d,..., a+(k-1)d$ . Since there are $k$ terms, we have an equation $k^2 = 836-715 = 121$ . Solving, we get $k$ as $11$ . Replacing $k$ in our sequence with $11$ , we get $a,a+d,a+2d,..., a+10d$ . The sum of this sequence is equal to $715$ , or $\frac{(2a+10d)(11)}{2} = 715$ , and by simplifying we get $a+5d=65$ . We are asked for the first, middle, and end terms, which are $a$ , $a+5d$ , and $a+10d$ respectively. Their sum is $3a+15$ , or $3 \cdot (a+5d)$ . Our desired answer is $65 \cdot 3 = \boxed{195}$ .
~Irfans123

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/298
~ dolphin7

## Video Solution
https://www.youtube.com/watch?v=T8Ox412AkZc ~Shreyas S

## Video Solution by OmegaLearn
https://youtu.be/tKsYSBdeVuw?t=4689
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .