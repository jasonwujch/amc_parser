# 2018 AIME I Problem 3

## Problem

Kathy has $5$ red cards and $5$ green cards. She shuffles the $10$ cards and lays out $5$ of the cards in a row in a random order. She will be happy if and only if all the red cards laid out are adjacent and all the green cards laid out are adjacent. For example, card orders $RRGGG$ , $GGGGR$ , or $RRRRR$ will make Kathy happy, but $RRRGR$ will not. The probability that Kathy will be happy is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
We have $2+4\cdot 2$ cases total.
The two are all red and all green. Then, you have 4 of one, 1 of other. 3 of one, 2 of other. 2 of one, 3 of other. 1 of one, 4 of other. Then flip the order, so times two.
Obviously the denominator is $10\cdot 9\cdot 8\cdot 7\cdot 6$ , since we are choosing a card without replacement.
Then, we have for the numerator for the two of all red and green: \[5\cdot 4\cdot 3\cdot 2\cdot 1.\]
For the 4 and 1, we have: \[5\cdot 4\cdot 3\cdot 2\cdot 5.\]
For the 3 and 2, we have: \[5\cdot 4\cdot 3\cdot 5\cdot 4.\]
For the 2 and 3, we have: \[5\cdot 4\cdot 5\cdot 4\cdot 3.\]
For the 1 and 4, we have: \[5\cdot 5\cdot 4\cdot 3\cdot 2.\]
Adding up and remembering to double all of them, since they can be reversed and the 5's can be red or green, we get, after simplifying: $\dfrac{31}{126}$
Thus the answer is $31 + 126 = \boxed{157}$ . -gorefeebuddie

## Solution 2
Our probability will be $\dfrac{\text{number of "happy" configurations of cards}}{\text{total number of configurations of cards}}.$
First of all, we have $10$ choices for the first card, $9$ choices for the second card, $8$ choices for the third card, $7$ choices for the fourth card, and $6$ choices for the last card. This gives a total of $10\cdot 9\cdot 8\cdot 7\cdot 6$ possible ways for five cards to be chosen.
Finding the number of configurations that make Kathy happy is a more difficult task, however, and we will resort to casework to do it.
First, let's look at the appearances of the "happy configurations" that Kathy likes. Based on the premise of the problem, we can realize that there are ten cases for the appearance of the configurations: \[\text{RRRRR},\] \[\text{GGGGG},\] \[\text{RRRRG},\] \[\text{GGGGR},\] \[\text{RRRGG},\] \[\text{GGGRR},\] \[\text{RRGGG},\] \[\text{GGRRR},\] \[\text{RGGGG},\] \[\text{GRRRR}.\] But this doesn't mean there are 10 "happy configurations" in total-- remember that we've been treating these cards as distinguishable, so we must continue to do so.
To lighten the load of 10 cases on the human brain, we can note that in the eyes of what we will soon do, $RRRRR$ and $GGGGG$ are effectively equivalent, and therefore may be treated in the same case. We will have to multiply by 2 at the end, though.
Similarly, we can equate $RRRRG,$ $GGGGR,$ $RGGGG,$ and $GRRRR,$ as well as $RRRGG,$ $GGGRR,$ $RRGGG,$ and $GGRRR,$ so that we just have three cases. We can approach each of these cases with constructive counting.
Case 1: $RRRRR$ -type.
For this case, there are $5$ available choices for the first card, $4$ available choices for the second card, $3$ for the third card, $2$ for the fourth card, and $1$ for the last card. This leads to a total of $5\cdot 4\cdot 3\cdot 2\cdot 1=120$ configurations for this case. There are $2$ cases of this type.
Case 2: $RRRRG$ -type.
For this case, there are $5$ available choices for the first card, $4$ available choices for the second card, $3$ for the third card, $2$ for the fourth card, and $5$ choices for the last card (not $1$ , because we're doing a new color). This leads to a total of $5\cdot 4\cdot 3\cdot 2\cdot 5=600$ configurations for this case. There are $4$ cases of this type.
Case 3: $RRRGG$ -type.
For this case, there are $5$ available choices for the first card, $4$ available choices for the second card, $3$ for the third card, $5$ for the fourth card, and $4$ choices for the last card. This leads to a total of $5\cdot 4\cdot 3\cdot 5\cdot 4=1200$ configurations for this case. There are $4$ cases of this type.
Adding the cases up gives $2\cdot 120+4\cdot 600+4\cdot 1200=7440$ "happy" configurations in total.
This means that the probability that Kathy is happy will be $\dfrac{7440}{10\cdot 9\cdot 8\cdot 7\cdot 6},$ which simplifies to $\dfrac{31}{126}.$
So the answer is $31+126=\boxed{157}$

## Solution 3
As the problem states, some examples of valid are $RRGGG$ , $GGGGR$ , and $RRRRR$ . Let's use each of these as more general cases.
Let $RRGGG$ be the case when there are 2 adjacents of one color, and 3 adjacents of the other color. This yields $4$ combinations ( $RRGGG$ , $GGRRR$ , $RRRGG$ , and $GGGRR$ ). The probability of each of these is equal, equating to $\frac{5}{10}\cdot \frac{4}{9}\cdot \frac{5}{8}\cdot \frac{4}{7}\cdot \frac{3}{6}=\frac{5}{126}$ , and since there are $4$ combinations, the probability of this case is $4\cdot \frac{5}{126}=\frac{10}{63}$
Next case is $GGGGR$ . Let this be when there are 4 adjacents of one color, and 1 individual color. Once again, this yields $4$ combinations ( $GGGGR$ , $RRRRG$ , $RGGGG$ , and $GRRRR$ ). The probability of each is the same, equating to $\frac{5}{10}\cdot \frac{4}{9}\cdot \frac{3}{8}\cdot \frac{2}{7}\cdot \frac{5}{6}=\frac{5}{252}$ , and since there are $4$ combinations, the probability of this case is $4\cdot \frac{5}{252}=\frac{5}{63}$
The final case is $RRRRR$ , in which there is just an adjacent block of $5$ colors. There are only $2$ combinations this time, each equating to the probability $\frac{5}{10}\cdot \frac{4}{9}\cdot \frac{3}{8}\cdot \frac{2}{7}\cdot \frac{1}{6}=\frac{1}{252}$ , and since there are $2$ combinations, the probability of this case is $2\cdot \frac{1}{252}=\frac{1}{126}$ .
Thus, the total probability is $\frac{10}{63}+\frac{5}{63}+\frac{1}{126}=\frac{31}{126} \implies m+n=\boxed{157}$

## Solution 4
Kathy will draw the 10 cards in some order, but the restriction of having all greens in a row and all reds in a row only applies to the first 5 cards drawn. The total number of ways the 10 cards can be drawn is simply 10 choose 5 which is 252. Now we just count the number of possible successful configurations of the ten cards. The first 5 cards can start either be $GRRRR$ , $GGRRR$ , $GGGRR$ , $GGGGR$ , $GGGGG$ or the same thing except starting with a red. The number of ways to order $GRRRR$ is the number of ways to order the last 5 cards, which is 5C1. Doing all of the other cases, the total is $(\binom{5}{1}+\binom{5}{2}+\binom{5}{3}+\binom{5}{4}+\binom{5}{5})*2 = 62$ . $\frac{62}{252} = \frac{31}{126},$ so the solution is $31 + 126 = \boxed{157}$
-bradleyguo Minor LaTeX edits by fasterthanlight

## Solution 5
Suppose $k$ of the first $5$ cards are red. There are $\binom{5}{k}$ ways to order the last five cards, and either $1$ or $2$ ways to order the first five cards: $1$ if $k=0$ or $k=5$ , otherwise $2$ . So, the number of orderings that work is \[\binom{5}{0} + 2\binom{5}{1} + 2\binom{5}{2} + 2\binom{5}{3} + 2\binom{5}{4} + \binom{5}{5} = 2\sum_{k=0}^{5}\binom{5}{k} - 2 = 2^6 - 2.\]
The total number of orderings is $\binom{10}{5} = 252,$ so the answer is $\frac{62}{252} = \boxed{\frac{31}{126}}$

## Solution 6 (Official MAA)
Assume without loss of generality that the first card laid out is red. Then the arrangements that satisfy Kathy’s requirements are RRRRR, RRRRG, RRRGG, RRGGG, and RGGGG. The probability that Kathy will lay out one of these arrangements is \[\frac49\cdot\frac38\cdot\frac27\cdot\frac16\] \[\frac49\cdot\frac38\cdot\frac27\cdot\frac56\] \[\frac49\cdot\frac38\cdot\frac57\cdot\frac46\] \[\frac49\cdot\frac58\cdot\frac47\cdot\frac36\] \[+\frac59\cdot\frac48\cdot\frac37\cdot\frac26\] \[\overline{..........................}\] \[\frac{31}{126}\] The requested sum is $31+126=\boxed{157}.$

## Video Solution
https://www.youtube.com/watch?v=WVtbD8x9fCM ~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .