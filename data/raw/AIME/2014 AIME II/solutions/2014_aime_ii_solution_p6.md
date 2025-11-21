# 2014 AIME II Problem 6

## Problem

Charles has two six-sided die. One of the die is fair, and the other die is biased so that it comes up six with probability $\frac{2}{3}$ and each of the other five sides has probability $\frac{1}{15}$ . Charles chooses one of the two dice at random and rolls it three times. Given that the first two rolls are both sixes, the probability that the third roll will also be a six is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution 1
The probability that he rolls a six twice when using the fair die is $\frac{1}{6}\times \frac{1}{6}=\frac{1}{36}$ . The probability that he rolls a six twice using the biased die is $\frac{2}{3}\times \frac{2}{3}=\frac{4}{9}=\frac{16}{36}$ . Given that Charles rolled two sixes, we can see that it is $16$ times more likely that he chose the second die. Therefore the probability that he is using the fair die is $\frac{1}{17}$ , and the probability that he is using the biased die is $\frac{16}{17}$ . The probability of rolling a third six is
\[\frac{1}{17}\times \frac{1}{6} + \frac{16}{17} \times \frac{2}{3} = \frac{1}{102}+\frac{32}{51}=\frac{65}{102}\] Therefore, our desired $p+q$ is $65+102= \boxed{167}$

## Solution 2 (Official Solution)
This is an incredibly simple problem if one is familiar with conditional probability (SO BE FAMILIAR WITH IT)! The conditional probability that the third roll will be a six given that the first two rolls are sixes, is the conditional probability that Charles rolls three sixes given that his first two rolls are sixes. This is thus $\frac{\frac{1}{2}(\frac{2}{3})^3+\frac{1}{2}(\frac{1}{6})^3}{\frac{1}{2}(\frac{2}{3})^2+\frac{1}{2}(\frac{1}{6})^2}= \frac{65}{102}$ . The answer is therefore $65+102= \boxed {167}$ .
~th1nq3r
Note: I have just found out that this is also the official solution. So I did not STEAL it, but as a coincidence, have come across the EXACT SAME SOLUTION. LIKE EXACTLY THE SAME. I AM SLIGHTLY FRIGHTENED. :/
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .