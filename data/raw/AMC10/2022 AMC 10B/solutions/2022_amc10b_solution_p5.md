# 2022 AMC 10B Problem 5

## Problem

What is the value of \[\frac{\left(1+\frac13\right)\left(1+\frac15\right)\left(1+\frac17\right)}{\sqrt{\left(1-\frac{1}{3^2}\right)\left(1-\frac{1}{5^2}\right)\left(1-\frac{1}{7^2}\right)}}?\] $\textbf{(A)}\ \sqrt3 \qquad\textbf{(B)}\ 2 \qquad\textbf{(C)}\ \sqrt{15} \qquad\textbf{(D)}\ 4 \qquad\textbf{(E)}\ \sqrt{105}$

## Solution 1 (Difference of Squares)
We apply the difference of squares to the denominator, and then regroup factors: \begin{align*} \frac{\left(1+\frac13\right)\left(1+\frac15\right)\left(1+\frac17\right)}{\sqrt{\left(1-\frac{1}{3^2}\right)\left(1-\frac{1}{5^2}\right)\left(1-\frac{1}{7^2}\right)}} &= \frac{\left(1+\frac13\right)\left(1+\frac15\right)\left(1+\frac17\right)}{\sqrt{\left(1+\frac13\right)\left(1+\frac15\right)\left(1+\frac17\right)}\cdot\sqrt{\left(1-\frac13\right)\left(1-\frac15\right)\left(1-\frac17\right)}} \\ &= \frac{\sqrt{\left(1+\frac13\right)\left(1+\frac15\right)\left(1+\frac17\right)}}{\sqrt{\left(1-\frac13\right)\left(1-\frac15\right)\left(1-\frac17\right)}} \\ &= \frac{\sqrt{\frac43\cdot\frac65\cdot\frac87}}{\sqrt{\frac23\cdot\frac45\cdot\frac67}} \\ &= \frac{\sqrt{4\cdot6\cdot8}}{\sqrt{2\cdot4\cdot6}} \\ &= \frac{\sqrt8}{\sqrt2} \\ &= \boxed{\textbf{(B)}\ 2}. \end{align*} ~MRENTHUSIASM

## Solution 2 (Brute Force)
Since these numbers are fairly small, we can use brute force as follows: \[\frac{(1+\frac{1}{3})(1+\frac{1}{5})(1+\frac{1}{7})}{\sqrt{(1-\frac{1}{3^2})(1-\frac{1}{5^2})(1-\frac{1}{7^2})}} =\frac{\frac{4}{3}\cdot\frac{6}{5}\cdot\frac{8}{7}}{\sqrt{\frac{8}{9}\cdot\frac{24}{25}\cdot\frac{48}{49}}} =\frac{\frac{4\cdot6\cdot8}{3\cdot5\cdot7}}{\sqrt{\frac{(2^3)(2^3\cdot3^1)(2^4\cdot3^1)}{(3^2)(5^2)(7^2)}}} =\frac{\frac{64}{35}}{\frac{96}{105}}=\frac{64}{35}\cdot\frac{105}{96}=\boxed{\textbf{(B)}\ 2}.\] ~not_slay

## Solution 3 (Brute Force)
This solution starts precisely like the one above. We simplify to get the following:
\[\frac{(1+\frac{1}{3})(1+\frac{1}{5})(1+\frac{1}{7})}{\sqrt{(1-\frac{1}{3^2})(1-\frac{1}{5^2})(1-\frac{1}{7^2})}} = \frac{\frac{4\cdot6\cdot8}{3\cdot5\cdot7}}{\sqrt{\frac{(2^3)(2^3\cdot3^1)(2^4\cdot3^1)}{(3^2)(5^2)(7^2)}}}\]
But now, we can get a nice simplification as shown: \[\frac{\frac{4\cdot6\cdot8}{3\cdot5\cdot7}}{\sqrt{\frac{(2^3)(2^3\cdot3^1)(2^4\cdot3^1)}{(3^2)(5^2)(7^2)}}} = \dfrac{\frac{4\cdot6\cdot8}{3\cdot5\cdot7}}{\sqrt{\frac{2^{10} \cdot 3^{2}}{3^2\cdot 5^2\cdot 7^2}}} = \dfrac{\frac{4\cdot6\cdot8}{3\cdot5\cdot7}}{\frac{2^5 \cdot 3}{3\cdot5\cdot 7}} =\dfrac{4\cdot6\cdot8}{3\cdot5\cdot7} \hspace{0.05 in} \cdot \hspace{0.05 in}\dfrac{3\cdot5\cdot 7}{2^5 \cdot 3} =\dfrac{2^6\cdot 3}{2^5\cdot 3} = \boxed{\textbf{(B)}\ 2}.\]
~TaeKim
~minor edits by mathboy100

## Video Solution (⚡️3 min solution⚡️)
https://youtu.be/N7hGuy0MWOQ
~Education, the Study of Everything

## Video Solution by Interstigation
https://youtu.be/_KNR0JV5rdI?t=470
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .