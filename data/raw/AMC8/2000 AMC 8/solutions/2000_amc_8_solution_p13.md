# 2000 AMC 8 Problem 13

## Problem

In triangle $CAT$ , we have $\angle ACT =\angle ATC$ and $\angle CAT = 36^\circ$ . If $\overline{TR}$ bisects $\angle ATC$ , then $\angle CRT =$

[asy] pair A,C,T,R; C = (0,0); T = (2,0); A = (1,sqrt(5+sqrt(20))); R = (3/2 - sqrt(5)/2,1.175570); draw(C--A--T--cycle); draw(T--R); label("$A$",A,N); label("$T$",T,SE); label("$C$",C,SW); label("$R$",R,NW);[/asy]

$\text{(A)}\ 36^\circ\qquad\text{(B)}\ 54^\circ\qquad\text{(C)}\ 72^\circ\qquad\text{(D)}\ 90^\circ\qquad\text{(E)}\ 108^\circ$

## Solution
In $\triangle ACT$ , the three angles sum to $180^\circ$ , and $\angle C = \angle T$
$\angle CAT + \angle ATC + \angle ACT = 180$
$36 + \angle ATC + \angle ATC = 180$
$2 \angle ATC = 144$
$\angle ATC = 72$
Since $\angle ATC$ is bisected by $\overline{TR}$ , $\angle RTC = \frac{72}{2} = 36$
Now focusing on the smaller $\triangle RTC$ , the sum of the angles in that triangle is $180^\circ$ , so:
$\angle RTC + \angle TCR + \angle CRT = 180$
$36 + \angle ACT + \angle CRT = 180$
$36 + \angle ATC + \angle CRT = 180$
$36 + 72 + \angle CRT = 180$
$\angle CRT = 72^\circ$ , giving the answer $\boxed{C}$
### See Also