# 2013 AMC 8 Problem 22

## Problem

Toothpicks are used to make a grid that is $60$ toothpicks long and $32$ toothpicks wide. How many toothpicks are used altogether?

[asy] picture corner; draw(corner,(5,0)--(35,0)); draw(corner,(0,-5)--(0,-35)); for (int i=0; i<3; ++i){for (int j=0; j>-2; --j){if ((i-j)<3){add(corner,(50i,50j));}}} draw((5,-100)--(45,-100)); draw((155,0)--(185,0),dotted+linewidth(2)); draw((105,-50)--(135,-50),dotted+linewidth(2)); draw((100,-55)--(100,-85),dotted+linewidth(2)); draw((55,-100)--(85,-100),dotted+linewidth(2)); draw((50,-105)--(50,-135),dotted+linewidth(2)); draw((0,-105)--(0,-135),dotted+linewidth(2));[/asy]

$\textbf{(A)}\ 1920 \qquad \textbf{(B)}\ 1952 \qquad \textbf{(C)}\ 1980 \qquad \textbf{(D)}\ 2013 \qquad \textbf{(E)}\ 3932$

## Video Solution
https://youtu.be/nNDdkv_zfOo ~savannahsolver

## Solution 1
There are $61$ vertical columns with a length of $32$ toothpicks, and there are $33$ horizontal rows with a length of $60$ toothpicks, because $32$ and $60$ are the number of intervals. You can verify this by trying a smaller case, i.e. a $3 \times 4$ grid of toothpicks, with $3 \times 3$ and $2 \times 4$ .
Thus, our answer is $61\cdot 32 + 33 \cdot 60 = \boxed{\textbf{(E)}\ 3932}$ .
~Note by Theraccoon: The person who posted this answer did not include their name. Minor edit by ~NXC

## Solution 2 - Common sense
With a quick mental calculation, 60 * 30 yields 1800, which is roughly where 4 of our 5 answer choices lie in. However, we can tell that each square would require at least 2 toothpicks that uniquely belong to itself, so the answer would be $60\cdot 30 \cdot 2$ which would be roughly $\boxed{\textbf{(E)}\ 3932}$ .
-superplayer24
### See Also