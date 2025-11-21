# 2013 AMC 10A Problem 21

## Problem

A group of $12$ pirates agree to divide a treasure chest of gold coins among themselves as follows. The $k^{\text{th}}$ pirate to take a share takes $\frac{k}{12}$ of the coins that remain in the chest. The number of coins initially in the chest is the smallest number for which this arrangement will allow each pirate to receive a positive whole number of coins. How many coins does the $12^{\text{th}}$ pirate receive?

$\textbf{(A)}\ 720\qquad\textbf{(B)}\ 1296\qquad\textbf{(C)}\ 1728\qquad\textbf{(D)}\ 1925\qquad\textbf{(E)}\ 3850$

## Solution 1
Let $x$ be the number of coins. After the $k^{\text{th}}$ pirate takes his share, $\frac{12-k}{12}$ of the original amount is left. Thus, we know that
$x \cdot \frac{11}{12} \cdot \frac{10}{12} \cdot \frac{9}{12} \cdot \frac{8}{12} \cdot \frac{7}{12} \cdot \frac{6}{12} \cdot \frac{5}{12} \cdot \frac{4}{12} \cdot \frac{3}{12} \cdot \frac{2}{12} \cdot \frac{1}{12}$ must be an integer. Simplifying, we get
$x \cdot \frac{11}{12} \cdot \frac{5}{6} \cdot \frac{1}{2} \cdot \frac{7}{12} \cdot \frac{1}{2} \cdot \frac{5}{12} \cdot \frac{1}{3} \cdot \frac{1}{4} \cdot \frac{1}{6} \cdot \frac{1}{12}$ . Now, the minimal $x$ is the denominator of this fraction multiplied out, obviously. We mentioned before that this product must be an integer. Specifically, it is an integer and it is the amount that the $12^{\text{th}}$ pirate receives, as he receives $\frac{12}{12} = 1 =$ all of what is remaining.
Thus, we know the denominator is canceled out, so the number of gold coins received is going to be the product of the numerators, $11 \cdot 5 \cdot 7 \cdot 5 = \boxed{\textbf{(D) }1925}$ .

## Solution 2 (Using the answer choices)
Solution $1$ mentioned the expression $x \cdot \frac{11}{12} \cdot \frac{10}{12} \cdot ... \cdot \frac{1}{12}$ . Note that this is equivalent to $\frac{x \cdot 11!}{12^{11}}$ .
We can compute the amount of factors of $2$ , $3$ , $5$ , etc. but this is not necessary. To minimize this expression, we must take out factors of $2$ and $3$ , since $12^{11}=2^{22} \cdot 3^{11}$ . $11!$ has neither $22$ factors of $2$ , nor $11$ factors of $3$ . This means that if $11!$ contains $a$ factors of $2$ , then $x$ will contain $22-a$ factors of $2$ . This also holds for factors of $3$ .
Thus, once simplified, the expression will have no factors of $2$ . It will also have no factors of $3$ .
Looking at the answer choices, there is only one answer which is not even, which is $\boxed{\textbf{(D) }1925}$ .

## Solution 3
We know that the 11th pirate takes $\frac{11}{12}$ of what is left from the 10th pirate, so we have the 12th pirate taking \[\frac{12}{12}\cdot(1-\frac{11}{12})=1\cdot\frac{1}{12}\] of what is left from the 10th pirate. Similarly, since the 10th pirate takes $\frac{10}{12}$ of what is left from the 9th pirate, we have the 11th pirate taking \[\frac{11}{12}\cdot(1-\frac{10}{12})=\frac{11}{12}\cdot\frac{2}{12}\] of what is left from the 9th pirate. Thus, the 12th pirate takes \[1\cdot\frac{1}{12}\cdot\frac{2}{12}\] of what is left from the 9th pirate. Repeating the method, we can find that the 12th pirate takes \[1\cdot\frac{1}{12}\cdot\frac{2}{12}\cdot\frac{3}{12}\cdot...\cdot\frac{10}{12}\cdot\frac{11}{12}\] of what is left from the 1st pirate, or \[1\cdot\frac{1}{12}\cdot\frac{2}{12}\cdot\frac{3}{12}\cdot...\cdot\frac{10}{12}\cdot\frac{11}{12}\cdot\frac{12}{12}\] of the total amount of coins.
Now canceling out the denominator with the numerator as possible, we are left with $\frac{1\cdot5\cdot7\cdot5\cdot11}{...}=\frac{1925}{...}$ with some factors of 12 in the denominator. For this fraction to be an integer, the smallest possible number of coins is the same as the denominator, so the numerator is the number of coins taken by the 12th pirate, or $1925 \,\boxed{\mathrm{\textbf{(D)}}}$
~ Nafer

## Video Solution by Richard Rusczyk
https://www.youtube.com/watch?v=-3d31c-7xm8
~dolphin7
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .