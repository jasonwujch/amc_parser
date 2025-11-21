# 2014 AIME I Problem 2

## Problem

An urn contains $4$ green balls and $6$ blue balls. A second urn contains $16$ green balls and $N$ blue balls. A single ball is drawn at random from each urn. The probability that both balls are of the same color is $0.58$ . Find $N$ .

## Solution
First, we find the probability both are green, then the probability both are blue, and add the two probabilities. The sum should be equal to $0.58$ .
The probability both are green is $\frac{4}{10}\cdot\frac{16}{16+N}$ , and the probability both are blue is $\frac{6}{10}\cdot\frac{N}{16+N}$ , so \[\frac{4}{10}\cdot\frac{16}{16+N}+\frac{6}{10}\cdot\frac{N}{16+N}=\frac{29}{50}\] Solving this equation, \[20\left(\frac{16}{16+N}\right)+30\left(\frac{N}{16+N}\right)=29\] Multiplying both sides by $16+N$ , we get
\begin{align*} 20\cdot16+30\cdot N&=29(16+N)\\ 320+30N&=464+29N\\ N&=\boxed{144} \end{align*}
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .