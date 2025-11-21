# 2009 AIME II Problem 8

## Problem

Dave rolls a fair six-sided die until a six appears for the first time. Independently, Linda rolls a fair six-sided die until a six appears for the first time. Let $m$ and $n$ be relatively prime positive integers such that $\dfrac mn$ is the probability that the number of times Dave rolls his die is equal to or within one of the number of times Linda rolls her die. Find $m+n$ .

## Solutions

## Solution 1
There are many almost equivalent approaches that lead to summing a geometric series. For example, we can compute the probability of the opposite event. Let $p$ be the probability that Dave will make at least two more throws than Linda. Obviously, $p$ is then also the probability that Linda will make at least two more throws than Dave, and our answer will therefore be $1-2p$ .
How to compute $p$ ?
Suppose that Linda made exactly $t$ throws. The probability that this happens is $(5/6)^{t-1}\cdot (1/6)$ , as she must make $t-1$ unsuccessful throws followed by a successful one. In this case, we need Dave to make at least $t+2$ throws. This happens if his first $t+1$ throws are unsuccessful, hence the probability is $(5/6)^{t+1}$ .
Thus for a fixed $t$ the probability that Linda makes $t$ throws and Dave at least $t+2$ throws is $(5/6)^{2t} \cdot (1/6)$ .
Then, as the events for different $t$ are disjoint, $p$ is simply the sum of these probabilities over all $t$ . Hence:
\begin{align*} p & = \sum_{t=1}^\infty \left(\frac 56\right)^{2t} \cdot \frac 16 \\ & = \frac 16 \cdot \left(\frac 56\right)^2 \cdot \sum_{x=0}^\infty \left(\frac{25}{36}\right)^x \\ & = \frac 16 \cdot \frac{25}{36} \cdot \frac 1{1 - \dfrac{25}{36}} \\ & = \frac 16 \cdot \frac{25}{36} \cdot \frac{36}{11} \\ & = \frac {25}{66} \end{align*}
Hence the probability we were supposed to compute is $1 - 2p = 1 - 2\cdot \frac{25}{66} = 1 - \frac{25}{33} = \frac 8{33}$ , and the answer is $8+33 = \boxed{041}$ .

## Solution 2
Let $p$ be the probability that the number of times Dave rolls his die is equal to or within one of the number of times Linda rolls her die. (We will call this event "a win", and the opposite event will be "a loss".)
Let both players roll their first die.
With probability $\frac 1{36}$ , both throw a six and we win.
With probability $\frac{10}{36}$ exactly one of them throws a six. In this case, we win if the remaining player throws a six in their next throw, which happens with probability $\frac 16$ .
Finally, with probability $\frac{25}{36}$ none of them throws a six. Now comes the crucial observation: At this moment, we are in exactly the same situation as in the beginning. Hence in this case we will win with probability $p$ .
We just derived the following linear equation: \[p = \frac 1{36} + \frac{10}{36} \cdot \frac 16 + \frac{25}{36} \cdot p\]
Solving for $p$ , we get $p=\frac 8{33}$ , hence the answer is $8+33 = \boxed{041}$ .

## Solution 3
Let's write out the probabilities with a set number of throws that Linda rolls before getting a 6. The probability of Linda rolling once and gets 6 right away is $\frac{1}{6}$ . The probability that Dave will get a six in the same, one less, or one more throw is $\frac{1}{6} + \frac{5}{6} * \frac{5}{6}$ . Thus the combined probability is $\frac{11}{216}$ .
Let's do the same with the probability that Linda rolls twice and getting a six. This time it is $\frac{5}{6} * \frac{1}{6}$ . The probability that Dave meets the requirements set is $\frac{1}{6} + \frac{5}{6} * \frac{1}{6} + \frac{5}{6} * \frac{5}{6} * \frac{1}{6}$ . Combine the probabilities again to get $\frac{455}{7776}$ . (or not, because you can simplify without calculating later)
It's clear that as the number of rolls before getting a six increases, the probability that Dave meets the requirements is multiplied by $\frac{5}{6} * \frac{5}{6}$ . We can use this pattern to solve for the sum of an infinite geometric series.
First, set the case where Linda rolls only once aside. It doesn't fit the same pattern as the rest, so we'll add it separately at the end. Next, let $a = (\frac{5}{6} * \frac{1}{6}) * (\frac{1}{6} + \frac{5}{6} * \frac{1}{6} + \frac{5}{6} * \frac{5}{6} * \frac{1}{6}) = \frac{455}{7776}$ as written above. Each probability where the number of tosses Linda makes increases by one will be $a * (\frac{25}{36})^{n+1}$ . Let $S$ be the sum of all these probabilities.
$S = a + a * \frac{25}{36} + a * (\frac{25}{36})^2...$
$S * \frac{25}{36} = a * \frac{25}{36} + a * (\frac{25}{36})^2 + a * (\frac{25}{36})^3...$
Subtract the second equation from the first to get
$S * \frac{11}{36} = a$
$S = a * \frac{36}{11}$
$S = \frac{455}{2376}$
Don't forget to add the first case where Linda rolls once.
$\frac{455}{2376} + \frac{11}{216} = \frac{8}{33}$
$8 + 33 = \boxed{41}$
-jackshi2006
Note: this is equivalent to computing $\frac{1}{36}(\sum_{n=1}^{\infty} (\frac{5}{6})^n((\frac{5}{6})^{n-1}+(\frac{5}{6})^{n}+(\frac{5}{6})^{n+1})+1+\frac{5}{6})$
### See Also
These problems are copyrighted © by the Mathematical Association of America.