# 2013 AIME II Problem 11

## Problem

Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N$ be the number of functions $f$ from set $A$ to set $A$ such that $f(f(x))$ is a constant function. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Any such function can be constructed by distributing the elements of $A$ on three tiers.
The bottom tier contains the constant value, $c=f(f(x))$ for any $x$ . (Obviously $f(c)=c$ .)
The middle tier contains $k$ elements $x\ne c$ such that $f(x)=c$ , where $1\le k\le 6$ .
The top tier contains $6-k$ elements such that $f(x)$ equals an element on the middle tier.
There are $7$ choices for $c$ . Then for a given $k$ , there are $\tbinom6k$ ways to choose the elements on the middle tier, and then $k^{6-k}$ ways to draw arrows down from elements on the top tier to elements on the middle tier.
Thus $N=7\cdot\sum_{k=1}^6\tbinom6k\cdot k^{6-k}=7399$ , giving the answer $\boxed{399}$ .

## Solution 1 Clarified
Define the three layers as domain $x$ , codomain $f(x)$ , and codomain $f(f(x))$ . Each one of them is contained in the set $A$ . We know that $f(f(x))$ is a constant function , or in other words, can only take on one value. So, we can start off by choosing that value $c$ in $7$ ways. So now, we choose the values that can be $f(x)$ for all those values should satisfy $f(f(x))=c$ . Let $S$ be that set of values. First things first, we must have $c$ to be part of $S$ , for the $S$ is part of the domain of $x$ . Since the values in $i\in S$ all satisfy $f(i) = c$ , we have $c$ to be a value that $f(x)$ can be. Now, for the elements other than $5$ :
If we have $k$ elements other than $5$ that can be part of $S$ , we will have $\binom{6}{k}$ ways to choose those values. There will also be $k$ ways for each of the elements in $A$ other than $c$ and those in set $S$ (for when function $f$ is applied on those values, we already know it would be $c$ ). There are $6-k$ elements in $A$ other than $c$ and those in set $S$ . Thus, there should be $k^{6-k}$ ways to match the domain $x$ to the values of $f(x)$ . Summing up all possible values of $k$ ( $[1,6]$ ), we have
\[\sum_{k=1}^6 \binom{6}{k} k^{6-k} = 6\cdot 1 + 15\cdot 16 + 20\cdot 27 + 15\cdot 16 + 6\cdot 5 + 1 = 1057\]
Multiplying that by the original $7$ for the choice of $c$ , we have $7 \cdot 1057 = 7\boxed{399}.$

## Solution 2
It is clear that we must have one fixed point (that is, $f(x)=x$ ). WLOG, let $x=1$ be a fixed point, so $f(1)=1$ .
Now, let's do casework on how many of the inputs $2, 3, 4, 5, 6 ,7$ leads to $1$ . Generally, if some values in that aforementioned list leads to $1$ , then running it in the function again will yield $1$ . All other values must be the the values that leads to $1$ .
For example:
$\textbf{Case 1:}$ All $6$ of $2, 3, 4, 5, 6, 7$ lead to $1$ . In this case, there is only $1$ way.
$\textbf{Case 2:}$ $5$ of $6$ of $2, 3, 4, 5, 6, 7$ lead to $1$ . In this case, we choose $5$ of the $6$ to lead to $1$ : $6\choose5$ .
Then, the other value that does not lead to $1$ should be one of the values that do: $5$ ways.
$\binom{6}{5}\cdot5$
$\textbf{Case 3:}$ $4$ of $6$ lead to $1$ . Choose which lead to $1$ : $6\choose4$ then the other values: $4^2$ ways
$\binom{6}{4}\cdot4^2$
$\textbf{Case 4:}$ $3$ of $6$ lead to $1$ . $\binom{6}{3}\cdot3^3$
$\textbf{Case 5:}$ $2$ of $6$ lead to $1$ . $\binom{6}{2}\cdot2^4$
$\textbf{Case 6:}$ $1$ of $6$ lead to $1$ . $\binom{6}{1}\cdot1^5$
Adding up all the cases, we have $1057$ cases. But don't forget to account for the WLOG and multiply by $7$ , yielding us the final answer of $7\boxed{399}.$
~xHypotenuse

## Video Solution
https://youtu.be/aaO7abKG0BQ?si=KLfz6oyzVR0d8D13
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .