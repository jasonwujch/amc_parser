# 2006 AIME I Problem 5

## Problem

The number $\sqrt{104\sqrt{6}+468\sqrt{10}+144\sqrt{15}+2006}$ can be written as $a\sqrt{2}+b\sqrt{3}+c\sqrt{5},$ where $a, b,$ and $c$ are positive integers . Find $abc$ .

## Solution 1
We begin by equating the two expressions:
\[a\sqrt{2}+b\sqrt{3}+c\sqrt{5} = \sqrt{104\sqrt{6}+468\sqrt{10}+144\sqrt{15}+2006}\]
Squaring both sides yields:
\[2ab\sqrt{6} + 2ac\sqrt{10} + 2bc\sqrt{15} + 2a^2 + 3b^2 + 5c^2 = 104\sqrt{6}+468\sqrt{10}+144\sqrt{15}+2006\]
Since $a$ , $b$ , and $c$ are integers, we can match coefficients:
\begin{align*} 2ab\sqrt{6} &= 104\sqrt{6} \\ 2ac\sqrt{10} &=468\sqrt{10} \\ 2bc\sqrt{15} &=144\sqrt{15}\\ 2a^2 + 3b^2 + 5c^2 &=2006 \end{align*}
Solving the first three equations gives: \begin{eqnarray*}ab &=& 52\\ ac &=& 234\\ bc &=& 72 \end{eqnarray*}
Multiplying these equations gives $(abc)^2 = 52 \cdot 234 \cdot 72 = 2^63^413^2 \Longrightarrow abc = \boxed{936}$ .

## Solution 2
We realize that the quantity under the largest radical is a perfect square and attempt to rewrite the radicand as a square. Start by setting $x=\sqrt{2}$ , $y=\sqrt{3}$ , and $z=\sqrt{5}$ . Since
\[(px+qy+rz)^2=p^2x^2+q^2y^2+r^2z^2+2(pqxy+prxz+qryz)\]
we attempt to rewrite the radicand in this form:
\[2006+2(52xy+234xz+72yz)\]
Factoring, we see that $52=13\cdot4$ , $234=13\cdot18$ , and $72=4\cdot18$ . Setting $p=13$ , $q=4$ , and $r=18$ , we see that
\[2006=13^2x^2+4^2y^2+18^2z^2=169\cdot2+16\cdot3+324\cdot5\]
so our numbers check. Thus $104\sqrt{2}+468\sqrt{3}+144\sqrt{5}+2006=(13\sqrt{2}+4\sqrt{3}+18\sqrt{5})^2$ . Square rooting gives us $13\sqrt{2}+4\sqrt{3}+18\sqrt{5}$ and our answer is $13\cdot4\cdot18=\boxed{936}$
These problems are copyrighted © by the Mathematical Association of America.