# 2012 AIME I Problem 12

## Problem

Let $\triangle ABC$ be a right triangle with right angle at $C.$ Let $D$ and $E$ be points on $\overline{AB}$ with $D$ between $A$ and $E$ such that $\overline{CD}$ and $\overline{CE}$ trisect $\angle C.$ If $\frac{DE}{BE} = \frac{8}{15},$ then $\tan B$ can be written as $\frac{m \sqrt{p}}{n},$ where $m$ and $n$ are relatively prime positive integers, and $p$ is a positive integer not divisible by the square of any prime. Find $m+n+p.$

## Solution 1
We have $\angle BCE = \angle ECD = \angle DCA = \tfrac 13 \cdot 90^\circ = 30^\circ$ . Drop the altitude from $D$ to $CB$ and call the foot $F$ .
Let $CD = 8a$ . Using angle bisector theorem on $\triangle CDB$ , we get $CB = 15a$ . Now $CDF$ is a $30$ - $60$ - $90$ triangle, so $CF = 4a$ , $FD = 4a\sqrt{3}$ , and $FB = 11a$ . Finally, $\tan{B} = \tfrac{DF}{FB}=\tfrac{4\sqrt{3}a}{11a} = \tfrac{4\sqrt{3}}{11}$ . Our final answer is $4 + 3 + 11 = \boxed{018}$ .

## Solution 2
Without loss of generality, set $CB = 1$ . Then, by the Angle Bisector Theorem on triangle $DCB$ , we have $CD = \frac{8}{15}$ . We apply the Law of Cosines to triangle $DCB$ to get $1 + \frac{64}{225} - \frac{8}{15} = BD^{2}$ , which we can simplify to get $BD = \frac{13}{15}$ .
Now, we have $\cos \angle B = \frac{1 + \frac{169}{225} - \frac{64}{225}}{\frac{26}{15}}$ by another application of the Law of Cosines to triangle $DCB$ , so $\cos \angle B = \frac{11}{13}$ . In addition, $\sin \angle B = \sqrt{1 - \frac{121}{169}} = \frac{4\sqrt{3}}{13}$ , so $\tan \angle B = \frac{4\sqrt{3}}{11}$ .
Our final answer is $4+3+11 = \boxed{018}$ .

## Solution 3
(This solution does not use the Angle Bisector Theorem or the Law of Cosines, but it uses the Law of Sines and more trig)
Find values for all angles in terms of $\angle B$ . $\angle CEB = 150-B$ , $\angle CED = 30+B$ , $\angle CDE = 120-B$ , $\angle CDA = 60+B$ , and $\angle A = 90-B$ .
Use the law of sines on $\triangle CED$ and $\triangle CEB$ :
In $\triangle CED$ , $\frac{8}{\sin 30} = \frac{CE}{\sin (120-B)}$ . This simplifies to $16 = \frac{CE}{\sin (120-B)}$ .
In $\triangle CEB$ , $\frac{15}{\sin 30} = \frac{CE}{\sin B}$ . This simplifies to $30 = \frac{CE}{\sin B}$ .
Solve for $CE$ and equate them so that you get $16\sin (120-B) = 30\sin B$ .
From this, $\frac{8}{15} = \frac{\sin B}{\sin (120-B)}$ .
Use a trig identity on the denominator on the right to obtain: $\frac{8}{15} = \frac{\sin B}{\sin 120 \cos B - \cos 120 \sin B}$
This simplifies to $\frac{8}{15} = \frac{\sin B}{\frac{\sqrt{3}\cos B}{2} + \frac{\sin B}{2}} = \frac{\sin B}{\frac{\sqrt{3} \cos B + \sin B}{2}} = \frac{2\sin B}{\sqrt{3}\cos B + \sin B}$
This gives $8\sqrt{3}\cos B+8\sin B=30\sin B$ Dividing by $\cos B$ , we have ${8\sqrt{3}}= 22\tan B$
$\tan{B} = \frac{8\sqrt{3}}{22} = \frac{4\sqrt{3}}{11}$ . Our final answer is $4 + 3 + 11 = \boxed{018}$ .

## Solution 4
(This solution avoids advanced trigonometry)
Let $X$ be the foot of the perpendicular from $D$ to $\overline{BC}$ , and let $Y$ be the foot of the perpendicular from $E$ to $\overline{BC}$ .
Now let $EY=x$ . Clearly, triangles $EYB$ and $DXB$ are similar with $\frac{BE}{BD}=\frac{15}{15+8}=\frac{15}{23}=\frac{EY}{DX}$ , so $DX=\frac{23}{15}x$ .
Since triangles $CDX$ and $CEY$ are 30-60-90 right triangles, we can easily find other lengths in terms of $x$ . For example, we see that $CY=x\sqrt{3}$ and $CX=\frac{\frac{23}{15}x}{\sqrt{3}}=\frac{23\sqrt{3}}{45}x$ . Therefore $XY=CY-CX=x\sqrt{3}-\frac{23\sqrt{3}}{45}x=\frac{22\sqrt{3}}{45}x$ .
Again using the fact that triangles $EYB$ and $DXB$ are similar, we see that $\frac{BX}{BY}=\frac{XY+BY}{BY}=\frac{XY}{BY}+1=\frac{23}{15}$ , so $BY=\frac{15}{8}XY=\frac{15}{8}*\frac{22\sqrt{3}}{45}=\frac{11\sqrt{3}}{2}$ .
Thus $\tan \angle B = \frac{x}{\frac{11\sqrt{3}}{12}x}=\frac{4\sqrt{3}}{11}$ , and our answer is $4+3+11=\boxed{018}$ .

## Solution 5
(Another solution without trigonometry)
Extend $CD$ to point $F$ such that $\overline{AF} \parallel \overline{CB}$ . It is then clear that $\triangle AFD$ is similar to $\triangle BCD$ .
Let $AC=p$ , $BC=q$ . Then $\tan \angle B = p/q$ .
With the Angle Bisector Theorem, we get that $CD=\frac{8}{15}q$ . From 30-60-90 $\triangle CAF$ , we get that $AF=\frac{1}{\sqrt{3}}p$ and $FD=FC-CD=\frac{2}{\sqrt{3}}p-\frac{8}{15}q$ .
From $\triangle AFD \sim \triangle BCD$ , we have that $\frac{FD}{CD}=\frac{FA}{CB}=\frac{\frac{2}{\sqrt{3}}p-\frac{8}{15}q}{\frac{8}{15}q}=\frac{\frac{1}{\sqrt{3}}p}{q}$ . Simplifying yields $\left(\frac{p}{q}\right)\left(\frac{2\sqrt{3}}{3}*\frac{15}{8}-\frac{\sqrt{3}}{3}\right)=1$ , and $\tan \angle B=\frac{p}{q}=\frac{4\sqrt{3}}{11}$ , so our answer is $4+3+11=\boxed{018}$ .

## Solution 6
Let $CB = 1$ , and let the feet of the altitudes from $D$ and $E$ to $\overline{CB}$ be $D'$ and $E'$ , respectively. Also, let $DE = 8k$ and $EB = 15k$ . We see that $BD' = 15k\cos B$ and $BE' = 23k\cos B$ by right triangles $\triangle{BDD'}$ and $\triangle{BEE'}$ . From this we have that $D'E' = 8k\cos B$ . With the same triangles we have $DD' = 23k\sin B$ and $EE' = 15k\sin B$ . From 30-60-90 triangles $\triangle{CDD'}$ and $\triangle{CEE'}$ , we see that $CD' = \frac{23k\sqrt{3}\sin B}{3}$ and $CE' = 15k\sqrt{3}\sin B$ , so $D'E' = \frac{22k\sqrt{3}\sin B}{3}$ . From our two values of $D'E'$ we get: $8k\cos B = \frac{22k\sqrt{3}\sin B}{3}$
$\frac{\sin B}{\cos B} = \frac{8k}{\frac{22k\sqrt{3}}{3}} = \tan B$
$\tan B = \frac{8}{\frac{22\sqrt{3}}{3}} = \frac{24}{22\sqrt{3}} = \frac{8\sqrt{3}}{22} = \frac{4\sqrt{3}}{11}$ Our answer is then $4+3+11 = \boxed{018}$ .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/352

## Solution 7
WLOG, let $DE=8$ and $BE=15$ . First, by the Law of Sines on $\triangle CEB$ , we find that \[\frac{\sin\angle B}{CE}=\frac{\sin\angle ECB}{BE}=\frac{1}{30}\implies \sin\angle B=\frac{CE}{30}.\] Now, we will find $CE$ . Consider the following diagram:
We have constructed equilateral triangle $\triangle BDP$ , and its circumcircle. Since $\angle DCB=\angle DPB=60^\circ$ , $C$ lies on $(BDP)$ as well. Let $Q$ be the point diametrically opposite $P$ on $(BCD)$ , and let $R$ be the foot of $Q$ on $BD$ (this is the midpoint of $BD$ ). It is easy to compute that $RQ=\frac{23}{2\sqrt3}$ and $ER=\frac{23}{2}-8=\frac{7}{2}$ . Therefore, by the Pythagorean Theorem, $EQ=\frac{13}{\sqrt{3}}$ . Now, by Power of a Point, we know that $(DE)(BE)=(EQ)(EC)$ , which means that \[120=\frac{13EC}{\sqrt{3}}\implies EC=\frac{120\sqrt{3}}{13}.\] From before, we know that $\sin\angle B=\frac{EC}{30}\implies \sin\angle B=\frac{4\sqrt3}{13}$ . It's now easy to compute $\cos\angle B$ as well using the Pythagorean identity; we find that $\cos\angle B=\frac{11}{13}$ , and thus $\tan\angle B=\frac{4\sqrt3}{11}$ for an answer of $\boxed{018}$ . -brainiacmaniac31

## Solution 8
vladimir.shelomovskii@gmail.com, vvsss

## Solution 9
WLOG, let $DE=8$ and $EB=15$ . (this will be redefined later) Define points $A'$ , $D'$ , $E'$ , and $B'$ such that $A'$ is on $AC$ , $B'$ is on $CB$ and $D'$ and $E'$ are the intersections of $A'B'$ with $CD$ and $CE$ , with $CD' = CE' = 1$ , respectively. From cross ratios, we have: \begin {align*} \frac{(AE)(DB)}{(AB)(DE)} &= \frac{(A'E')(D'B')}{(A'B')(D'E')} \\ \frac{(AD+8)(23)}{(AD+23)(8)} & = \frac{(\cos(15)+\sin(15))^2}{(2 \cos(15))(2 \sin(15))} \\ & \implies AD = 92/11 \end {align*} For simplicity, scale everything by $11$ , so $AD=92$ , $DE=88$ and $EB = 165$ . From the ratio lemma, we have: \begin {align*} \frac{AC}{CB} &= \frac{AD \sin{\angle BCD}}{DB \sin{\angle ACD}} \\ \tan B &= \frac{92 \cdot \sqrt{3}/2}{253 \cdot 1/2} \\ \tan B &= \frac{4 \sqrt{3}}{2}\\ &\implies \boxed{018}. \end{align*} ~ boxtheanswer
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .