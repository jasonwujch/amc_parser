# 2023 AIME I Problem 1

## Problem

Five men and nine women stand equally spaced around a circle in random order. The probability that every man stands diametrically opposite a woman is $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1
For simplicity purposes, we consider two arrangements different even if they only differ by rotations or reflections. In this way, there are $14!$ arrangements without restrictions.
First, there are $\binom{7}{5}$ ways to choose the man-woman diameters. Then, there are $10\cdot8\cdot6\cdot4\cdot2$ ways to place the five men each in a man-woman diameter. Finally, there are $9!$ ways to place the nine women without restrictions.
Together, the requested probability is \[\frac{\tbinom{7}{5}\cdot(10\cdot8\cdot6\cdot4\cdot2)\cdot9!}{14!} = \frac{21\cdot(10\cdot8\cdot6\cdot4\cdot2)}{14\cdot13\cdot12\cdot11\cdot10} = \frac{48}{143},\] from which the answer is $48+143 = \boxed{191}.$
~MRENTHUSIASM

## Solution 2 (Solution 4 but more efficient)
Arranging the 14 people in a circle, one could just see that the probability depends on the men's placement, as any woman can be opposite to a man. Therefore, we just need to consider the men's arrangements.
Place the first man on the circle. There are 14 ways to do this. Doing this removes two spots for the next man, the diametrically opposite slot and the slot already occupied, so the next man has 12 spots left to choose. The third man has 10, fourth man has 8, and fifth man has 6.
In total, there are 14 slots for the first man, 13 for the second, 12 for the third, 11 for the fourth, and 10 for the fifth.
We have \( P(nA) = \frac{14 \times 12 \times 10 \times 8 \times 6}{14 \times 13 \times 12 \times 11 \times 10} \Rightarrow \frac{8 \times 6}{13 \times 11} = \frac{48}{143} \).
Our answer is simply \( 48 + 143 =\) $\boxed{191}.$
~Pinotation

## Solution 3
We can simply just loop through each of the men and find the probability that the person opposite from him is a woman.
Start by sitting down the $1$ st man. The probability that the person opposite to him is a woman is $\frac{9}{13}$ since out of the $13$ people who can sit opposite to him, $9$ can be a woman. With the $2$ nd man, we can use the same logic: there are $11$ people who can sit opposite to him, but only $8$ of them are a woman, so the probability is $\frac{8}{11}.$ We use the same logic for the $3$ rd, $4$ th and $5$ th men to get probabilities of $\frac{7}{9}$ , $\frac{6}{7}$ and $\frac{5}{5},$ respectively.
Multiplying these probabilities, we get a final answer of \[\frac{9}{13}\cdot\frac{8}{11}\cdot\frac{7}{9}\cdot\frac{6}{7}\cdot\frac{5}{5}=\frac{48}{143}\longrightarrow 48+143 = \boxed{191}.\]
~s214425 (Inspired by Math Jam)

## Solution 4
This problem is equivalent to solving for the probability that no man is standing diametrically opposite to another man. We can simply just construct this.
We first place the $1$ st man anywhere on the circle, now we have to place the $2$ nd man somewhere around the circle such that he is not diametrically opposite to the first man. This can happen with a probability of $\frac{12}{13}$ because there are $13$ available spots, and $12$ of them are not opposite to the first man.
We do the same thing for the $3$ rd man, finding a spot for him such that he is not opposite to the other $2$ men, which would happen with a probability of $\frac{10}{12}$ using similar logic. Doing this for the $4$ th and $5$ th men, we get probabilities of $\frac{8}{11}$ and $\frac{6}{10}$ respectively.
Multiplying these probabilities, we get, \[\frac{12}{13}\cdot\frac{10}{12}\cdot\frac{8}{11}\cdot\frac{6}{10}=\frac{48}{143}\longrightarrow\boxed{191}.\]
~s214425

## Solution 5
Assume that rotations and reflections are distinct arrangements, and replace men and women with identical M's and W's, respectively. (We can do that because the number of ways to arrange $5$ men in a circle and the number of ways to arrange $9$ women in a circle, are constants.) The total number of ways to arrange $5$ M's and $9$ W's is $\binom{14}{5} = 2002.$
To count the number of valid arrangements (i.e. arrangements where every M is diametrically opposite a W), we notice that exactly $2$ of the pairs of diametrically opposite positions must be occupied by $2$ W's. There are $\binom{7}{2} = 21$ ways to choose these $2$ pairs. For the remaining $5$ pairs, we have to choose which position is occupied by an M and which is occupied by a W. This can be done in $2^{5} = 32$ ways. Therefore, there are $21*32 = 672$ valid arrangements.
Therefore, the probability that an arrangement is valid is $\frac{672}{2002} = \frac{48}{143}$ for an answer of $\boxed{191}.$
~pianoboy

## Solution 6
To start off, we calculate the total amount of ways to organize all $14$ people irrespective of any constraints. This is simply ${14\choose5} = 2002$ , because we just count how many ways we can place all $5$ men in any of the $14$ slots.
Since men cannot be diametrically opposite with each other, because of the constraints, placing down one man in any given spot will make another spot on the opposite side of the circle unable to hold any men. This means that placing down one man will effectively take away $2$ spots.
There are $14$ possible slots the first man can be placed. Once that man was placed, the next man only have $12$ possible slots because the slot that the first man is in is taken and the diametrically opposite spot to the first man can't have any men. Similar logic applies for the third man, who has $10$ possible slots. The fourth man has $8$ possible slots, and the fifth man has $6$ possible slots.
This means the number of ways you can place all $5$ men down is $14 \cdot 12 \cdot 10 \cdot 8 \cdot 6$ . However, since the men are all indistinct from each other, you also have to divide that value by $5! = 120$ , since there are $120$ ways to arrange the $5$ men in each possible positioning of the men on the circle. This means the total number of ways to arrange the men around the circle so that none of them are diametrically opposite of each other is: $\frac{14 \cdot 12 \cdot 10 \cdot 8 \cdot 6}{5!} = 672$ . The women simply fill in the rest of the available slots in each arrangement of men.
Thus, the final probability is $\frac{672}{2002} = \frac{48}{143}$ , meaning the answer is $48 + 143 = \boxed{191}$ .
~ericshi1685

## Solution 7
We will first assign seats to the men. The first man can be placed in any of the $14$ slots. The second man can be placed in any of the remaining $13$ seats, except for the one diametrically opposite to the first man. So, there are $13 - 1 = 12$ ways to seat him. With a similar argument, the third man can be seated in $10$ ways, the fourth man in $8$ ways and the last man in $6$ ways.
So, the total number of ways to arrange the men is $14 \cdot 12 \cdot 10 \cdot 8 \cdot 6$ .
The women go to the remaining $9$ spots. Note that since none of the seats diametrically opposite to the men is occupied, each man is opposite a woman. The number of ways to arrange the women is therefore, simply $9!$ , meaning that the total number of ways to arrange the people with restrictions is $14 \cdot 12 \cdot 10 \cdot 8 \cdot 6 \cdot 9!$ In general, there are $14!$ ways to arrange the people without restrictions. So, the probability is \[\frac{14 \cdot 12 \cdot 10 \cdot 8 \cdot 6 \cdot 9!}{14!} = \frac{8 \cdot 6}{13 \cdot 11} = \frac{48}{143}.\] The answer is $48 + 143 = \boxed{191}$ .
~baassid24

## Solution 8
First pin one man on one seat (to ensure no rotate situations). Then there are $13!$ arrangements. Because $5$ men must have women at their opposite side, we consider the $2$ nd man and the woman opposite as one group and name it $P_2.$ There are $4$ groups, $P_1, P_2, P_3, P_4$ except the first man pinned on the same point. And for the rest $4$ women, name them $P_5$ and $P_6.$ First to order $P_1, P_2, P_3, P_4, P_5, P_6,$ there are $6!$ ways. For the $1$ st man, there are $9$ women to choose, $8$ for the $2$ nd, $\ldots,$ $5$ for the $5$ th, and then for the $2$ women pairs $3$ and $1.$ Because every $2$ person in the group have chance to change their position, there are $2^6$ possibilities.
So the possibility is \[P=\frac{6!\cdot 9\cdot 8\cdot 7\cdot 6\cdot 5\cdot 3\cdot 1 \cdot 2^6}{13!}=\frac{48}{143}.\]
The answer is $48+143=\boxed{191}.$
~PLASTA

## Solution 9
We get around the condition that each man can't be opposite to another man by simply considering all $7$ diagonals, and choosing $5$ where there will be a single man. For each diagonal, the man can go on either side, and there are $\binom{14}{5}$ ways to arrange the men and the women in total. Thus our answer is $\frac{\binom{7}{5}\cdot 2^5}{\binom{14}{5}} = \frac{48}{143}.$ We get $48 + 143 = \boxed{191}$
~AtharvNaphade

## Solution 9
We can find the probability of one arrangement occurring, and multiply it by the total number of arrangements.
The probability of a man being in any specific position is $\frac{5}{14}.$ The probability of a woman being across from him is $\frac{9}{13}.$ The probability of a man being in any valid position is now $\frac{4}{12},$ and the probability of a woman being across from him is $\frac{8}{11},$ and so forth. We stop when there are no more men left. Multiplying these probabilities together,
\[P(\mathrm{One\ successful\ outcome})=\frac{5}{14}\cdot \frac{9}{13}\cdot \frac{4}{12}\cdot \frac{8}{11}\cdot \frac{3}{10}\cdot \frac{7}{9}\cdot \frac{2}{8}\cdot \frac{1}{6}\cdot \frac{6}{7}\cdot \frac{5}{5} = \frac{1}{2002}.\] To find the total number of successful outcomes, we consider the diagonals; the total number of diagonals to be made is $\binom75$ , since there are $7$ total diagonals, and we want to choose $5$ of them to connect a man to a woman. For each of these diagonals, the man can be on either side of the diagonal.
It follows that there are $2$ possibilities for each diagonal (man on one side, woman on the other, and vice versa). There are $5$ diagonals with a man and a woman, so there are $2^5$ different ways for these diagonals to appear.
There are $\binom75$ successful diagonals, and for each of these diagonals, there are $2^5$ ways to seat the men and the women, there are $\binom75$ $\cdot 2^5$ successful outcomes.
Recall that \[P(\mathrm{Any\ successful\ outcome})=P(\mathrm{One\ successful\ outcome})\cdot P(\mathrm{Total\ number\ of\ successful\ outcomes}).\] Therefore, \[P(\mathrm{Any\ successful\ outcome}) = \frac{1}{2002}\cdot 2^5\cdot \binom75 = \frac{1}{2002}\cdot 2^5\cdot 21 = \frac{2^5\cdot 21}{2002} = \frac{48}{143}.\] The requested sum is $48+143=\boxed{191}.$
-Benedict T (countmath1)

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=KdKysmdgepI

## Video Solution by TheBeautyofMath
https://youtu.be/u7tG8P3vi5o
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .