# 2019 AMC 8 Problem 15

## Problem

On a beach $50$ people are wearing sunglasses and $35$ people are wearing caps. Some people are wearing both sunglasses and caps. If one of the people wearing a cap is selected at random, the probability that this person is also wearing sunglasses is $\frac{2}{5}$ . If instead, someone wearing sunglasses is selected at random, what is the probability that this person is also wearing a cap?

$\textbf{(A) }\frac{14}{85}\qquad\textbf{(B) }\frac{7}{25}\qquad\textbf{(C) }\frac{2}{5}\qquad\textbf{(D) }\frac{4}{7}\qquad\textbf{(E) }\frac{7}{10}$

## Solution 1
The number of people wearing caps and sunglasses is $\frac{2}{5}\cdot35=14$ . So then, 14 people out of the 50 people wearing sunglasses also have caps.
$\frac{14}{50}=\boxed{\textbf{(B)}\frac{7}{25}}$

## Solution 2
Let $A$ be the event that a randomly selected person is wearing sunglasses, and let $B$ be the event that a randomly selected person is wearing a cap. We can write $P(A \cap B)$ in two ways: $P(A)P(B|A)$ or $P(B)P(A|B)$ . Suppose there are $t$ people in total. Then \[P(A) = \frac{50}{t}\] and \[P(B) = \frac{35}{t}.\] Additionally, we know that the probability that someone is wearing sunglasses given that they wear a cap is $\frac{2}{5}$ , so $P(A|B) = \frac{2}{5}$ . We let $P(B|A)$ , which is the quantity we want to find, be equal to $x$ . Substituting in, we get \[\frac{50}{t} \cdot x = \frac{35}{t} \cdot \frac{2}{5}\] \[\implies 50x = 35 \cdot \frac{2}{5}\] \[\implies 50x = 14\] \[\implies x = \frac{14}{50}\] \[= \boxed{\textbf{(B)}~\frac{7}{25}}\]
Note: This solution makes use of the dependent events probability formula, $P(A \cap B) = P(A)P(B|A)$ , where $P(B|A)$ represents the probability that $B$ occurs given that $A$ has already occurred and $P(A \cup B)$ represents the probability of both $A$ and $B$ happening.
~ cxsmi

## Video Solution by EzLx
https://youtu.be/SkDf39Cg5z4
~EzLx CookeMonster SirCookies

## Video Solution
https://youtu.be/6xNkyDgIhEE?t=250pih-jsm
### See Also