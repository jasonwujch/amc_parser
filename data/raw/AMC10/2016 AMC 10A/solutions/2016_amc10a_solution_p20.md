# 2016 AMC 10A Problem 20

## Problem

For some particular value of $N$ , when $(a+b+c+d+1)^N$ is expanded and like terms are combined, the resulting expression contains exactly $1001$ terms that include all four variables $a, b,c,$ and $d$ , each to some positive power. What is $N$ ?

$\textbf{(A) }9 \qquad \textbf{(B) } 14 \qquad \textbf{(C) } 16 \qquad \textbf{(D) } 17 \qquad \textbf{(E) } 19$

## Solution 1
All the desired terms are in the form $a^xb^yc^zd^w1^t$ , where $x + y + z + w + t = N$ (the $1^t$ part is necessary to make stars and bars work better.) Since $x$ , $y$ , $z$ , and $w$ must be at least $1$ ( $t$ can be $0$ ), let $x' = x - 1$ , $y' = y - 1$ , $z' = z - 1$ , and $w' = w - 1$ , so $x' + y' + z' + w' + t = N - 4$ . Now, we use stars and bars (also known as ball and urn) to see that there are $\binom{(N-4)+4}{4}$ or $\binom{N}{4}$ solutions to this equation. We notice that $1001=7\cdot11\cdot13$ , which leads us to guess that $N$ is around these numbers. This suspicion proves to be correct, as we see that $\binom{14}{4} = 1001$ , giving us our answer of $\boxed{\textbf{(B) }14.}$
Note: An alternative is instead of making the transformation, we "give" the variables $x, y, z, w$ 1, and then proceed as above.
~ Mathkiddie(minor edits by vadava_lx).

## Solution 2
By the Hockey Stick Identity , the number of terms that have all $a,b,c,d$ raised to a positive power is $\binom{N-1}{3}+\binom{N-2}{3}+\cdots + \binom{4}{3}+\binom{3}{3}=\binom{N}{4}$ . We now want to find some $N$ such that $\binom{N}{4} = 1001$ . As mentioned above, after noticing that $1001 = 7\cdot11\cdot13$ , and some trial and error, we find that $\binom{14}{4} = 1001$ , giving us our answer of $\boxed{\textbf{(B) }14.}$
~minor edits by vadava_lx

## Solution 3 (Casework)
The terms are in the form $a^xb^yc^zd^w1^t$ , where $x + y + z + w + t = N$ . The problem becomes distributing $N$ identical balls to $5$ different boxes $(x, y, z, w, t)$ such that each of the boxes $(x, y, z, w)$ has at least $1$ ball. The $N$ balls in a row have $N-1$ gaps among them. We are going to put $4$ or $3$ divisors into those $N-1$ gaps. There are $2$ cases of how to put the divisors.
Case $1$ : Put 4 divisors into $N-1$ gaps. It corresponds to each of $(a, b, c, d, 1)$ has at least one term. There are $\binom{N-1}{4}$ terms.
Case $2$ : Put 3 divisors into $N-1$ gaps. It corresponds to each of $(a, b, c, d)$ has at least one term. There are $\binom{N-1}{3}$ terms.
So, there are $\binom{N-1}{4}+\binom{N-1}{3}=\binom{N}{4}$ terms. $\binom{N}{4} = 1001$ , and since we have $\binom{14}{4} = 1001, N=\boxed{\textbf{(B) }14.}$
~ isabelchen ...

## Video Solution by OmegaLearn
https://youtu.be/yGJwp72qPzk?t=88
~ pi_is_3.15

## Video Solution
https://www.youtube.com/watch?v=R3eJW3PCYMs

## Video Solution 2
https://youtu.be/TpG8wlj4eRA with 5 Stars and Bars examples preceding the solution. Time stamps in description to skip straight to solution.
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .