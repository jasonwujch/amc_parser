# 2024 AMC 8 Problem 17

## Problem

A chess king is said to attack all the squares one step away from it, horizontally, vertically, or diagonally. For instance, a king on the center square of a $3$ x $3$ grid attacks all $8$ other squares, as shown below. Suppose a white king and a black king are placed on different squares of a $3$ x $3$ grid so that they do not attack each other (in other words, not right next to each other). In how many ways can this be done?

[asy] unitsize(29pt); import math; add(grid(3,3)); pair [] a = {(0.5,0.5), (0.5, 1.5), (0.5, 2.5), (1.5, 2.5), (2.5,2.5), (2.5,1.5), (2.5,0.5), (1.5,0.5)}; for (int i=0; i<a.length; ++i) { pair x = (1.5,1.5) + 0.4*dir(225-45*i); draw(x -- a[i], arrow=EndArrow()); } label("$K$", (1.5,1.5)); [/asy]

$\textbf{(A)}\ 20 \qquad \textbf{(B)}\ 24 \qquad \textbf{(C)}\ 27 \qquad \textbf{(D)}\ 28 \qquad \textbf{(E)}\ 32$

## Solution 1
If you place a king in any of the $4$ corners, the other king will have $5$ spots to go and there are $4$ corners, so $5 \times 4=20$ . If you place a king in any of the $4$ edges, the other king will have $3$ spots to go and there are $4$ edges so $3 \times 4=12$ . That gives us $20+12=32$ spots for the other king to go into in total. So $\boxed{\textbf{(E)} 32}$ is the answer. ~andliu766, captaindiamond868 (minor edits) ~AliceDubbleYou

## Solution 2
We see that the center is not a viable spot for either of the kings to be in, as it would attack all nearby squares.
This gives three combinations:
Corner-corner: There are 4 corners, and none of them are touching orthogonally or diagonally, so it's $\binom{4}{2}=6$
Corner-edge: For each corner, there are two edges that don't border it, $4\cdot2=8$
Edge-edge: The only possible combinations of this that work are top-bottom and left-right edges, so $2$ for this type
$6+8+2=16$
Multiply by two to account for arrangements of colors to get $\fbox{E) 32}$ ~ c_double_sharp

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/eQ6UUmZuhhY
~mr_mathman

## Video Solution 1 by Math-X (First understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=Q2e8OfkuzKZXmoau&t=4624
~Math-X

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=_SHs3ZXS1ZKF4-v2&t=2381 ~hsnacademy

## Video Solution 2 (super clear!) by Power Solve
https://youtu.be/SG4PRARL0TY

## Video Solution 3 by OmegaLearn.org
https://youtu.be/UJ3esPnlI5M

## Video Solution 4 by SpreadTheMathLove
https://www.youtube.com/watch?v=Svibu3nKB7E

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc
~NiuniuMaths

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=quWFZIahQCg

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=1922

## Video Solution by Dr. David
https://youtu.be/vO1rcJZzIrQ

## Video Solution by WhyMath
https://youtu.be/psiAz9Owyzk

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also