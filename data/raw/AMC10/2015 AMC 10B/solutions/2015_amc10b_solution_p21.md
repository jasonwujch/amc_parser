# 2015 AMC 10B Problem 21

## Problem

Cozy the Cat and Dash the Dog are going up a staircase with a certain number of steps. However, instead of walking up the steps one at a time, both Cozy and Dash jump. Cozy goes two steps up with each jump (though if necessary, he will just jump the last step). Dash goes five steps up with each jump (though if necessary, he will just jump the last steps if there are fewer than $5$ steps left). Suppose Dash takes $19$ fewer jumps than Cozy to reach the top of the staircase. Let $s$ denote the sum of all possible numbers of steps this staircase can have. What is the sum of the digits of $s$ ?

$\textbf{(A) }9\qquad\textbf{(B) }11\qquad\textbf{(C) }12\qquad\textbf{(D) }13\qquad\textbf{(E) }15$

## Solution 1
Let $n$ be the number of steps. We have
\[\left\lceil \frac{n}{2} \right\rceil - 19 = \left\lceil \frac{n}{5} \right\rceil\]
We will proceed to solve this equation via casework.
Case $1$ : $\left\lceil \frac{n}{2} \right\rceil = \frac{n}{2}$
Our equation becomes $\frac{n}{2} - 19 = \frac{n}{5} + \frac{j}{5}$ , where $j \in \{0,1,2,3,4\}$ Using the fact that $n$ is an integer, we quickly find that $j=1$ and $j=4$ yield $n=64$ and $n=66$ , respectively.
Case $2$ : $\left\lceil \frac{n}{2} \right\rceil = \frac{n}{2}+\frac{1}{2}$
Our equation becomes $\frac{n}{2} +\frac{1}{2} - 19 = \frac{n}{5} + \frac{j}{5}$ , where $j \in \{0,1,2,3,4\}$ Using the fact that $n$ is an integer, we quickly find that $j=2$ yields $n=63$ . Summing up we get $63+64+66=193$ . The sum of the digits is $\boxed{\textbf{(D)}\; 13}$ .
### Supplement
We find the values of $j$ by the following.
Case 1:
Multiplying both sides by $10$ gives us $5n-190=2n+2j \Rightarrow 3n=2j+190 \Rightarrow n=\frac{2j+190}{3}.$
However, also note that $n$ must be an integer (you can't have half a step), so we must have $2j+190\equiv 0 \pmod 3 \Rightarrow 2j+1 \equiv 0 \pmod 3 \Rightarrow 2j \equiv 2 \pmod 3.$
Values $j$ that satisfy this within the domain $j\in {0,1,2,3,4}$ are only $j=1$ and $j=4,$ corresponding to values of $n=64$ and $66.$
Case 2:
Multiplying both sides by $10$ gives us $5n-185=2n+2j \Rightarrow 3n = 2j + 185 \Rightarrow n=\frac{2j+185}{3}.$
Hence we must have $2j+185 \equiv 0 \pmod 3 \Rightarrow 2j \equiv 1 \pmod 3.$
Value $j$ that satisfy this within the domain $j\in {0,1,2,3,4}$ is only $j=2$ which corresponds to $n=63.$ Hence follows.
~mathboy282

## Solution 2
We know from the problem that Dash goes $3$ steps further than Cozy per jump (assuming they aren't within $4$ steps from the top). That means that if Dash takes $19$ fewer jumps than Cozy to get to the top of the staircase, the staircase must be at least $3 \cdot 19=57$ steps high. We then start using guess-and-check:
$57$ steps: $\left \lceil {57/2} \right \rceil = 29$ jumps for Cozy, and $\left \lceil {57/5} \right \rceil = 12$ jumps for Dash, giving a difference of $17$ jumps.
$58$ steps: $\left \lceil {58/2} \right \rceil = 29$ jumps for Cozy, and $\left \lceil {58/5} \right \rceil = 12$ jumps for Dash, giving a difference of $17$ jumps.
$59$ steps: $\left \lceil {59/2} \right \rceil = 30$ jumps for Cozy, and $\left \lceil {59/5} \right \rceil = 12$ jumps for Dash, giving a difference of $18$ jumps.
$60$ steps: $\left \lceil {60/2} \right \rceil = 30$ jumps for Cozy, and $\left \lceil {60/5} \right \rceil = 12$ jumps for Dash, giving a difference of $18$ jumps.
$\vdots$
By the time we test $61$ steps, we notice that when the number of steps exceeds a multiple of $2$ , the difference in jumps increases. So, we have to find the next number that will increase the difference. $62$ doesn't because both both Cozy's and Dash's number of jumps increases, but $63$ does, and $64$ . $65$ actually gives a difference of $20$ jumps, but $66$ goes back down to $19$ (because Dash had to take another jump when Cozy didn't). We don't need to go any further because the difference will stay above $19$ onward.
Therefore, the possible numbers of steps in the staircase are $63$ , $64$ , and $66$ , giving a sum of $193$ . The sum of those digits is $13$ , so the answer is $\boxed{D}$
- Minor Edits by Lolgod2

## Solution 3
We're looking for natural numbers $x$ such that $\left \lceil{\frac{x}{5}}\right \rceil + 19 = \left \lceil{\frac{x}{2}}\right \rceil$ .
Let's call $x = 10a + b$ . We now have $2a + \left \lceil{\frac{b}{5}}\right \rceil + 19 = 5a + \left \lceil{\frac{b}{2}}\right \rceil$ , or
$19 - 3a = \left \lceil{\frac{b}{2}}\right \rceil - \left \lceil{\frac{b}{5}}\right \rceil$ .
Obviously, since $b \le 10$ , this will not work for any value of $a$ under $6$ . In addition, since obviously $\frac{b}{2} \ge \frac{b}{5}$ , this will not work for any value over six, so we have $a = 6$ and $\left \lceil{\frac{b}{2}}\right \rceil - \left \lceil{\frac{b}{5}}\right \rceil = 1.$
This can be achieved when $\left \lceil{\frac{b}{5}}\right \rceil = 1$ and $\left \lceil{\frac{b}{2}}\right \rceil = 2$ , or when $\left \lceil{\frac{b}{5}}\right \rceil = 2$ and $\left \lceil{\frac{b}{2}}\right \rceil = 3$ .
Case One:
We have $b \le 5$ and $3 \le b \le 4$ , so $b = 3, 4$ .
Case Two:
We have $6 \le b \le 9$ and $5 \le b \le 6$ , so $b = 6$ .
We then have $63 + 64 + 66 = 193$ , which has a digit sum of $\boxed{13}$ .

## Solution 4
Translate the problem into following equation:
$n = 5D - \{0 \sim 4\} = 2C - \{0 \sim 1\}$
Since $C = D + 19$ , we have
$5D - \{0 \sim 4\} = 2D + 38 - \{0 \sim 1\}$
i.e.,
$3D = 38 + \{0 \sim 4\} - \{0 \sim 1\}$
We then have $D = 13$ when $\{1\} - \{0\}$ or $\{2\} - \{1\}$ (the dog's last jump has $2$ steps and the cat's last jump has $1$ step), which yields $n = 64$ and $n = 63$ respectively.
Another solution is $D = 14$ when $\{4\} - \{0\}$ , which yields $n = 66$ .
Therefore, with $63 + 64 + 66 = 193$ , the digit sum is $\boxed{13}$ .

## Video Solution
https://youtu.be/TpHZVbBGmVQ
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .