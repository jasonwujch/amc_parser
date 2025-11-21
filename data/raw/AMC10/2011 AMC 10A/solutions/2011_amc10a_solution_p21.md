# 2011 AMC 10A Problem 21

## Problem

Two counterfeit coins of equal weight are mixed with $8$ identical genuine coins. The weight of each of the counterfeit coins is different from the weight of each of the genuine coins. A pair of coins is selected at random without replacement from the $10$ coins. A second pair is selected at random without replacement from the remaining $8$ coins. The combined weight of the first pair is equal to the combined weight of the second pair. What is the probability that all $4$ selected coins are genuine?

$\textbf{(A)}\ \frac{7}{11}\qquad\textbf{(B)}\ \frac{9}{13}\qquad\textbf{(C)}\ \frac{11}{15}\qquad\textbf{(D)}\ \frac{15}{19}\qquad\textbf{(E)}\ \frac{15}{16}$

## Solution 1
If we pick $4$ indistinguishable real coins from the set of $8$ real coins, there are $\binom{8}{4}$ ways to pick the coins. If we then place the coins in four distinguishable slots on the scale, there are $4!$ ways to arrange them, giving $4!\cdot \binom{8}{4}$ ways to choose and place $8$ real coins. This gives $1680$ desirable combinations.
If we pick $2$ real coins and $2$ fake coins, there are $\binom{8}{2}\binom{2}{2}$ ways to choose the coins. There are $4$ choices for the first slot on the left side of the scale. Whichever type of coin is placed in that first slot, there are $2$ choices for the second slot on the left side of the scale, since it must be of the opposite type of coin. There are $2$ choices for the first slot on the right side of the scale and only $1$ choice for the last slot on the right side.
Thus, there are $4\cdot 2\cdot 2\cdot 1 = 16$ ways to arrange the coins, and $\binom{8}{2}\binom{2}{2} = 28$ sets of possible coins, for a total of $16\cdot 28 = 448$ combinations that are legal, yet undesirable.
The overall probability is thus $\frac{1680}{1680 + 448} = \boxed{\frac{15}{19} \ \mathbf{(D)}}$ .
Note that in this solution, all four slots on the scale are deemed to be distinguishable. In essence, this "overcounts" all numbers by a factor of $8$ , since you can switch the coins on the left side, you can switch the coins on the right side, or you can switch sides of the scale. But since all numbers are increased 8-fold, it will cancel out when calculating the probability.

## Solution 2
Place the two coins from the first pair in a line followed by the two coins from the second pair followed by the six left-over coins. We can do that in $\binom{10}{2} = 45$ different ways.
We need to exclude those cases where the weight shows a difference. There are two cases where a pair has both counterfeit coins and there are $4\cdot6$ cases where one counterfeit coin is chosen and one is in the left-over. That leaves $45-2-24=19$ cases.
Of these, $\binom{6}{2}=15$ cases has both counterfeit coins in the left-over. The probability of having chosen four genuine coins therefore is $\boxed{\frac{15}{19} \ \mathbf{(D)}}$ .

## Solution 3
WLOG, allow for all the coins to be distinguishable. We split this up into cases. Case $1$ being the weight of $2$ genuine coins together and Case $2$ being the weight of $1$ genuine coin and $1$ counterfeit coin.
Case $1$ : All Genuine coins chosen. This happens in $\frac{\binom{8}{2}\cdot\binom{6}{2}}{2}=210$ ways
Case $2$ : Genuine coin and Counterfeit coin both chosen. This happens in $\dfrac{8\cdot2\cdot7\cdot1}{2!}=8\cdot7=56$ ways.
Hence, the answer is $\dfrac{210}{210+56}=\boxed{\frac{15}{19} \ \mathbf{(D)}}$ .
~AH2025 (minor edit for clarity)

## Solution 4
We start by caluclating the probability that we draw 2 pairs with equivalent weight. There are 2 ways this can be done. The first way is the we draw 2 pairs consisting of one counterfeit coin and one genuine coin. The probability of this is $\frac{8}{10} \cdot \frac{2}{9} \cdot \frac{7}{8} \cdot \frac{1}{7} \cdot 4 = \frac{4}{45}$ . We multiply by 4 because we can draw each pair in 2 ways, fake then real or vice versa. The other way we can draw 2 pairs with equivalent weight is by drawing 4 real coins. There is only one order in which this can be done (Make sure you understand why). We get $\frac{8}{10} \cdot \frac{7}{9} \cdot \frac{6}{8} \cdot \frac{5}{7} = \frac{1}{3}$ We also just found the numerator of the fraction, $\frac{1}{3}$ because the question asks what the probability that all $4$ selected coins are genuine is. Therefore, our final fraction is $\frac{\frac{1}{3}}{\frac{4}{45} + \frac{1}{3}}$ which equals $\boxed{\frac{15}{19} \ \mathbf{(D)}}$ .
-litttle_master

## Video Solution by the Beauty of Math
https://www.youtube.com/watch?v=W5NlV2B_83U&feature=push-u-sub&attr_tag=XAAsHxmGZAHEdZgT%3A6
~Icematrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .