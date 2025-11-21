# 2004 AMC 8 Problem 22

## Problem

At a party there are only single women and married men with their wives. The probability that a randomly selected woman is single is $\frac25$ . What fraction of the people in the room are married men?

$\textbf{(A)}\ \frac13\qquad \textbf{(B)}\ \frac38\qquad \textbf{(C)}\ \frac25\qquad \textbf{(D)}\ \frac{5}{12}\qquad \textbf{(E)}\ \frac35$

## Solution 1
Assume arbitrarily (and WLOG) there are $5$ women in the room, of which $5 \cdot \frac25 = 2$ are single and $5-2=3$ are married. Each married woman came with her husband, so there are $3$ married men in the room as well for a total of $5+3=8$ people. The fraction of the people that are married men is $\boxed{\textbf{(B)}\ \frac38}$ .

## Solution 2 (Algebraic)
Let single women be $S$ , married wives to be $W$ , and men to be $M$ . As such, the number of men is equal to married woman since each husband has his own wife or $W=M$ . We are asked to find the probability of men in the total group or $\frac{M}{S+W+M}$ .
We are also given that out of all the women, 2/5 are single or $\frac{S}{S+W}=\frac{2}{5}$ . Rewrite this as $S=\frac{2}{5}(S+W)$ , $S=\frac{2S}{5}+\frac{2W}{5}$ , isolating $S$ gives us $\frac{3S}{5}=\frac{2W}{5}$ or $S=\frac{2M}{3}$ (because $W=M$ ).
Now, substituting gives us $\frac{M}{\frac{2M}{3}+M+M}=\frac{M}{\frac{2M}{3}+\frac{6M}{3}}=\frac{M}{\frac{8M}{3}}=\boxed{\textbf{(B)}\ \frac38}$ ~RandomMathGuy500
### See Also