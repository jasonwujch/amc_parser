# 2008 AIME II Problem 7

## Problem

Let $r$ , $s$ , and $t$ be the three roots of the equation \[8x^3 + 1001x + 2008 = 0.\] Find $(r + s)^3 + (s + t)^3 + (t + r)^3$ .

## Solution 1
By Vieta's formulas , we have $r + s + t = 0$ so $t = -r - s.$ Substituting this into our problem statement, our desired quantity is \[(r + s)^3 - r^3 - s^3 = 3r^2s + 3rs^2 = 3rs(r + s).\] Also by Vieta's formulas we have \[rst = -rs(r + s) = -\dfrac{2008}{8} = -251\] so negating both sides and multiplying through by 3 gives our answer of $\boxed{753}.$

## Solution 2
By Vieta's formulas , we have $r+s+t = 0$ , and so the desired answer is $(r+s)^3 + (s+t)^3 + (t+r)^3 = (0-t)^3 + (0-r)^3 + (0-s)^3 = -(r^3 + s^3 + t^3)$ . Additionally, using the factorization \[r^3 + s^3 + t^3 - 3rst = (r+s+t)(r^2 + s^2 + t^2 - rs - st - tr) = 0\] we have that $r^3 + s^3 + t^3 = 3rst$ . By Vieta's again, $rst = \frac{-2008}8 = -251 \Longrightarrow -(r^3 + s^3 + t^3) = -3rst = \boxed{753}.$

## Solution 3
Vieta's formulas gives $r + s + t = 0$ . Since $r$ is a root of the polynomial, $8r^3 + 1001r + 2008 = 0\Longleftrightarrow - 8r^3 = 1001r + 2008$ , and the same can be done with $s,\ t$ . Therefore, we have \begin{align*}8\{(r + s)^3 + (s + t)^3 + (t + r)^3\} &= - 8(r^3 + s^3 + t^3)\\ &= 1001(r + s + t) + 2008\cdot 3 = 3\cdot 2008\end{align*} yielding the answer $\boxed{753}$ .
Also, Newton's Sums yields an answer through the application. http://www.artofproblemsolving.com/Wiki/index.php/Newton's_Sums

## Solution 4
Expanding, you get: \[r^3 + 3r^2s + 3s^2r +s^3 +\] \[s^3 + 3s^2t + 3t^2s +t^3 +\] \[r^3 + 3r^2t + 3t^2r +t^3\] \[= 2r^3 + 2s^3 + 2t^3 + 3r^2s + 3s^2r + 3s^2t + 3t^2s + 3r^2t + 3t^2r\] This looks similar to $(r+s+t)^3 = r^3 + s^3 + t^3 + 3r^2s + 3s^2r + 3s^2t + 3t^2s + 3r^2t + 3t^2r + 6rst$ Substituting: \[(r+s+t)^3 - 6rst + r^3+s^3+t^3 = (r + s)^3 + (s + t)^3 + (t + r)^3\] Since $r+s+t = 0$ , \[(r+s)^3 + (s+t)^3 + (t+r)^3 = (0-t)^3 + (0-r)^3 + (0-s)^3 = -(r^3 + s^3 + t^3)\] Substituting, we get \[(r+s+t)^3 - 6rst + r^3+s^3+t^3 = -(r^3 + s^3 + t^3)\] or, \[0^3 - 6rst + r^3+s^3+t^3 = -(r^3 + s^3 + t^3) \implies 2(r^3 + s^3 + t^3) = 6rst\] We are trying to find $-(r^3 + s^3 + t^3)$ . Substituting: \[-(r^3 + s^3 + t^3) = -3srt = \frac{-2008*3}{8} = \boxed{753}.\]

## Solution 5
Write $(r+s)^3+(s+t)^3+(t+r)^3=-(r^3+s^3+t^3)$ and let $f(x)=8x^3+1001x+2008$ . Then \[f(r)+f(s)+f(t)=8(r^3+s^3+t^3)+1001(r+s+t)+6024=8(r^3+s^3+t^3)+6024=0.\] Solving for $r^3+s^3+t^3$ and negating the result yields the answer $\boxed{753}.$

## Solution 6
Here by Vieta's formulas : $r+s+t = 0$ --(1)
$rst = \frac{-2008}{8} = -251$ --(2)
By the factorisation formula: Let $a = r+s$ , $b = s+t$ , $c = t+r$ , $a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca) = 0$ (By (1))
So \[a^3+b^3+c^3 = 3abc = 3(r+s)(s+t)(t+r) = 3(-t)(-r)(-s) = 3[-(-251)] = \boxed{753}.\]

## Solution 7
Let's construct a polynomial with the roots $(r+s), (s+t),$ and $(t+r)$ .
sum of the roots:
$=2(r+s+t)=2\cdot0=0$
pairwise product of the roots:
$(r+s)(s+t)+(s+t)(t+r)+(t+r)(r+s)=r^2+s^2+t^2+3(rs+st+tr)$
$=(r+s+t)^2+rs+st+tr=0+\frac{1001}{8}$
product of the roots:
$(r+s)(s+t)(t+r)=r^2t+r^2s+s^2r+s^2t+t^2r+t^2s+3rst$
$=(rs+st+tr)(r+s+t)-3rst+2rst=-rst=-\frac{2008}{8}$
thus, the polynomial we get is
$x^3+\frac{1001}{8}x+-\frac{2008}{8}=0$
as $(r+s), (s+t),$ and $(t+r)$ are roots of this polynomial, we know that (using power reduction)
$(r+s)^3+\frac{1001}{8}(r+s)-\frac{2008}{8}=0$
$(s+t)^3+\frac{1001}{8}(s+t)-\frac{2008}{8}=0$
$(t+r)^3+\frac{1001}{8}(t+r)-\frac{2008}{8}=0$
adding all of the equations up, we see that
$(r+s)^3+(s+t)^3+(t+r)^3=3\cdot\frac{2008}{8}-\frac{1001}{8}(2r+2s+2t)=251(3)+0=\boxed{753}$

## Solution 8
We want to find what is $-(r^3+s^3+t^3)$ which reminds us of Newton sum. So we can see that $8S_3+0\cdot S_2+1001\cdot S_1+3\cdot 2008=0$ Notice that $S_1=0$ so it is just $S_3=-\frac{2008\cdot 3}{8}=-753$ , the desired answer is $\boxed{753}$
~bluesoul

## Solution 9
This solution uses Vietas, as with everyone else's solution. Expanding the expression we get
\[(r+s)^3+(s+t)^3+(t+r)^3 = r^3+3r^2s+3rs^2+\dots +3s^2t+3ts^2+t^3\]
Seeing the cubes, we try to find a $(r+s+t)^3$ and upon doing so, we get
\[(r+s)^3+(s+t)^3+(t+r)^3=(r+s+t)^3-6rst+(r^3+s^3+t^3)\]
Recall that $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ . Thus, we get
\[(r+s)^3+(s+t)^3+(t+r)^3=(r+s+t)^3-3rst+(r+s+t)(r^2+s^2+t^2-rs-st-tr)\]
Plugging in $(r+s+t)=0$ we get
\[(r+s)^3+(s+t)^3+(t+r)^3=0-3rst+0=-3\cdot -251=\boxed{753}\]
~firebolt360

## Solution 10
$8x^3+1001x+2008=0$
We want to find $(r+s)^3+(s+t)^3+(t+r)^3.$ Let's call this result n.
From vieta's formulas, we find that $r+s+t=-0/8=0$ , $rs+st+tr=1001/8$ , and $rst=-2008/8=-251.$
Expanding and rearranging gives us $n=(r+s)^3+(s+t)^3+(t+r)^3=r^3+3r^2s+3rs^2+s^3+s^3+3s^2t+3st^2+t^3+t^3+3t^2r+3tr^2+r^3=2r^3+2s^3+3r^2s+3rs^2+3s^2t+3st^2+3t^2r+3tr^2=3(r^3+s^3+t^3-(r^2s+rs^2+s^2t+st^2+t^2r+tr^2))-(r^3+s^3+t^3)=3((r+s+t)(r^2+s^2+t^2))-((r+s+t)^3-3(r^2s+rs^2+s^2t+st^2+t^2r+tr^2)-6rst)=3(r+s+t)((r+s+t)^2-2(rs+st+tr))-((r+s+t)^3-3(r^2s+rs^2+s^2t+st^2+t^2r+tr^2)-6rst)$
Let $k=r^2s+rs^2+s^2t+st^2+t^2r+tr^2$
$k=r^2s+rs^2+s^2t+st^2+t^2r+tr^2=(r+s+t)(r^2+s^2+t^2)-(r^3+s^3+t^3)=(r+s+t)((r+s+t)^2-2(rs+st+tr))-((r+s+t)^3-3k-6rst)=(0)(0^2-2(1001/8))-(0^3-3k-6(-251))=0-(0-3k+1506)=3k-1506$
Solving gives us $k=753$
$n=3(r+s+t)((r+s+t)^2-2(rs+st+tr))-((r+s+t)^3-3(r^2s+rs^2+s^2t+st^2+t^2r+tr^2)-6rst)=3(0)(0^2-2(1001/8))-(0^3-3k-6(-251))=0-(0-3(753)+1506)=753$
Therefore, the answer is $753.$
Also note that this is the only solution that still would have worked effectively if $r+s+t$ was nonzero.

## Video Solution by Punxsutawney Phil
https://www.youtube.com/watch?v=6mYZYh9gJBs (unavailable)
These problems are copyrighted © by the Mathematical Association of America.