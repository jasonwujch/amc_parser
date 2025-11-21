# 2015 AMC 10B Problem 18

## Problem

Johann has $64$ fair coins. He flips all the coins. Any coin that lands on tails is tossed again. Coins that land on tails on the second toss are tossed a third time. What is the expected number of coins that are now heads?

$\textbf{(A) } 32 \qquad\textbf{(B) } 40 \qquad\textbf{(C) } 48 \qquad\textbf{(D) } 56 \qquad\textbf{(E) } 64$

## Solution 1
We can simplify the problem first, then apply reasoning to the original problem. Let's say that there are $8$ coins. Shaded coins flip heads, and blank coins flip tails. So, after the first flip;
[asy] filldraw(circle((-5,0),0.35),white); filldraw(circle((-4,0),0.35),white); filldraw(circle((-3,0),0.35),white); filldraw(circle((-2,0),0.35),white); filldraw(circle((-1,0),0.35),black); filldraw(circle((-0,0),0.35),black); filldraw(circle((1,0),0.35),black); filldraw(circle((2,0),0.35),black); [/asy]
Then, after the second (new heads in blue);
[asy] filldraw(circle((-5,0),0.35),white); filldraw(circle((-4,0),0.35),white); filldraw(circle((-3,0),0.35),blue); filldraw(circle((-2,0),0.35),blue); filldraw(circle((-1,0),0.35),black); filldraw(circle((-0,0),0.35),black); filldraw(circle((1,0),0.35),black); filldraw(circle((2,0),0.35),black); [/asy]
And after the third (new head in green);
[asy] filldraw(circle((-5,0),0.35),white); filldraw(circle((-4,0),0.35),green); filldraw(circle((-3,0),0.35),blue); filldraw(circle((-2,0),0.35),blue); filldraw(circle((-1,0),0.35),black); filldraw(circle((-0,0),0.35),black); filldraw(circle((1,0),0.35),black); filldraw(circle((2,0),0.35),black); [/asy]
So in total, $7$ of the $8$ coins resulted in heads. Now we have the ratio of $\frac{7}{8}$ of the total coins will end up heads. Therefore, we have $\frac{7}{8}\cdot64=\boxed{\mathbf{(D)}\ 56}$

## Solution 2 (Efficient)
Every time the coins are flipped, half of them are expected to turn up heads. The expected number of heads on the first flip is $32$ , on the second flip is $16$ , and on the third flip, it is $8$ . Adding these gives $\boxed{\mathbf{(D)}\ 56}$

## Solution 3
Every time the coins are flipped, each of them has a $1/2$ probability of being tails. Doing this $3$ times, $1/8$ of them will be tails. $64-64*1/8=$ $\boxed{\mathbf{(D)}\ 56}$ .
~Lcz

## Solution 4
(Similar to solution 2)
Notice how:
$E(\text{Heads on 1st flip, 2nd flip, 3rd flip}) = E(\text{Heads on 1st flip}) + E(\text{Heads on 2nd flip}) + E(\text{Heads on 3rd flip})$
The expected number of heads for the first flip is simply $64 \cdot \frac{1}{2}$ , since each coin has a 1 in 2 chance of being heads. Then, we are left with $64 - 32 = 32$ coins. Then, half of these coins will be heads again, which leaves us with $32 - 16 = 16$ coins. Then, half of these coins will be heads again, which leaves us with $16 - 8 = 8$ coins.
Hence, the expected number of heads is simply:
$32 + 16 + 8 = \boxed{56} \implies D$
~yk2007

## Solution 5 (Linearity of Expectation)
As you may have guessed from the title, we will be using Linearity of Expectation to solve this problem. We will first look at the expected value for $1$ coin, then multiply by $64$ at the end, since expected value is linear. First, you can almost imagine, a markov chain or a tree chart. We first have a coin, with $2$ outcomes, heads and tails For heads, there is a $\dfrac{1}{2}$ chance of flipping one, and we multiply it by $1$ since we got $1$ head to come out. Now, lets look at the outcome where we get a tail on the first roll. We just roll, again, so the probability of getting a heads on the second roll is $\dfrac{1}{2} \cdot \dfrac{1}{2} = \dfrac{1}{4}$ . Again, we multiply by $1$ for the same reason. Now, same thing for the third roll it would just be $\dfrac{1}{8} \cdot 1$ . Summing it all up we get: \[\dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8} = \dfrac{7}{8} \cdot 64 = \boxed{\mathbf{(D)\ 56}}\]
~jb2015007

## Video Solution
https://youtu.be/0uCMSH7-Ubk
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .