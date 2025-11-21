# 2019 AIME I Problem 6

## Problem

In convex quadrilateral $KLMN$ side $\overline{MN}$ is perpendicular to diagonal $\overline{KM}$ , side $\overline{KL}$ is perpendicular to diagonal $\overline{LN}$ , $MN = 65$ , and $KL = 28$ . The line through $L$ perpendicular to side $\overline{KN}$ intersects diagonal $\overline{KM}$ at $O$ with $KO = 8$ . Find $MO$ .

## Solution 1 (Trig)
Let $\angle MKN=\alpha$ and $\angle LNK=\beta$ . Let $P$ be the project of $L$ onto line $NK$ . Note $\angle KLP=\beta$ .
Then, $KP=28\sin\beta=8\cos\alpha$ . Furthermore, $KN=\frac{65}{\sin\alpha}=\frac{28}{\sin\beta} \Rightarrow 65\sin\beta=28\sin\alpha$ .
Dividing the equations gives \[\frac{65}{28}=\frac{28\sin\alpha}{8\cos\alpha}=\frac{7}{2}\tan\alpha\Rightarrow \tan\alpha=\frac{65}{98}\]
Thus, $MK=\frac{MN}{\tan\alpha}=98$ , so $MO=MK-KO=\boxed{090}$ .

## Solution 2 (Cyclic Quads, PoP)
NOTE: this solution is wrong. The equation is correct due to similar triangles as described in solution 8, not PoP.
[asy] size(250); real h = sqrt(98^2+65^2); real l = sqrt(h^2-28^2); pair K = (0,0); pair N = (h, 0); pair M = ((98^2)/h, (98*65)/h); pair L = ((28^2)/h, (28*l)/h); pair P = ((28^2)/h, 0); pair O = ((28^2)/h, (8*65)/h); draw(K--L--N); draw(K--M--N--cycle); draw(L--M); label("K", K, SW); label("L", L, NW); label("M", M, NE); label("N", N, SE); draw(L--P); label("P", P, S); dot(O); label("O", shift((1,1))*O, NNE); label("28", scale(1/2)*L, W); label("65", ((M.x+N.x)/2, (M.y+N.y)/2), NE); [/asy]
Because $\angle KLN = \angle KMN = 90^{\circ}$ , $KLMN$ is a cyclic quadrilateral. Hence, by Power of Point, \[KO\cdot KM = KL^2 \implies KM=\dfrac{28^2}{8}=98 \implies MO=98-8=\boxed{090}\] as desired.
~Mathkiddie

## Solution 3 (Similar triangles)
[asy] size(250); real h = sqrt(98^2+65^2); real l = sqrt(h^2-28^2); pair K = (0,0); pair N = (h, 0); pair M = ((98^2)/h, (98*65)/h); pair L = ((28^2)/h, (28*l)/h); pair P = ((28^2)/h, 0); pair O = ((28^2)/h, (8*65)/h); draw(K--L--N); draw(K--M--N--cycle); draw(L--M); label("K", K, SW); label("L", L, NW); label("M", M, NE); label("N", N, SE); draw(L--P); label("P", P, S); dot(O); label("O", shift((1,1))*O, NNE); label("28", scale(1/2)*L, W); label("65", ((M.x+N.x)/2, (M.y+N.y)/2), NE); [/asy]
First, let $P$ be the intersection of $LO$ and $KN$ as shown above. Note that $m\angle KPL = 90^{\circ}$ as given in the problem. Since $\angle KPL \cong \angle KLN$ and $\angle PKL \cong \angle LKN$ , $\triangle PKL \sim \triangle LKN$ by AA similarity. Similarly, $\triangle KMN \sim \triangle KPO$ . Using these similarities we see that \[\frac{KP}{KL} = \frac{KL}{KN}\] \[KP = \frac{KL^2}{KN} = \frac{28^2}{KN} = \frac{784}{KN}\] and \[\frac{KP}{KO} = \frac{KM}{KN}\] \[KP = \frac{KO \cdot KM}{KN} = \frac{8\cdot KM}{KN}\] Combining the two equations, we get \[\frac{8\cdot KM}{KN} = \frac{784}{KN}\] \[8 \cdot KM = 28^2\] \[KM = 98\] Since $KM = KO + MO$ , we get $MO = 98 -8 = \boxed{090}$ .
Solution by vedadehhc

## Solution 4 (Similar triangles, orthocenters)
Extend $KL$ and $NM$ past $L$ and $M$ respectively to meet at $P$ . Let $H$ be the intersection of diagonals $KM$ and $LN$ (this is the orthocenter of $\triangle KNP$ ).
As $\triangle KOL \sim \triangle KHP$ (as $LO \parallel PH$ , using the fact that $H$ is the orthocenter), we may let $OH = 8k$ and $LP = 28k$ .
Then using similarity with triangles $\triangle KLH$ and $\triangle KMP$ we have
\[\frac{28}{8+8k} = \frac{8+8k+HM}{28+28k}\]
Cross-multiplying and dividing by $4+4k$ gives $2(8+8k+HM) = 28 \cdot 7 = 196$ so $MO = 8k + HM = \frac{196}{2} - 8 = \boxed{090}$ . (Solution by scrabbler94)

## Solution 5 (Algebraic Bashing)
First, let $P$ be the intersection of $LO$ and $KN$ . We can use the right triangles in the problem to create equations. Let $a=NP, b=PK, c=NO, d=OM, e=OP, f=PC,$ and $g=NC.$ We are trying to find $d.$ We can find $7$ equations. They are \[4225+d^2=c^2,\] \[4225+d^2+16d+64=a^2+2ab+b^2,\] \[a^2+e^2=c^2,\] \[b^2+e^2=64,\] \[b^2+e^2+2ef+f^2=784,\] \[a^2+e^2+2ef+f^2=g^2,\] and \[g^2+784=a^2+2ab+b^2.\] We can subtract the fifth equation from the sixth equation to get $a^2-b^2=g^2-784.$ We can subtract the fourth equation from the third equation to get $a^2-b^2=c^2-64.$ Combining these equations gives $c^2-64=g^2-784$ so $g^2=c^2+720.$ Substituting this into the seventh equation gives $c^2+1504=a^2+2ab+b^2.$ Substituting this into the second equation gives $4225+d^2+16d+64=c^2+1504$ . Subtracting the first equation from this gives $16d+64=1504.$ Solving this equation, we find that $d=\boxed{090}.$ (Solution by DottedCaculator)

## Solution 6 (5-second PoP)
[asy] size(8cm); pair K, L, M, NN, X, O; K=(-sqrt(98^2+65^2)/2, 0); NN=(sqrt(98^2+65^2)/2, 0); L=sqrt(98^2+65^2)/2*dir(180-2*aSin(28/sqrt(98^2+65^2))); M=sqrt(98^2+65^2)/2*dir(2*aSin(65/sqrt(98^2+65^2))); X=foot(L, K, NN); O=extension(L, X, K, M); draw(K -- L -- M -- NN -- K -- M); draw(L -- NN); draw(arc((K+NN)/2, NN, K)); draw(L -- X, dashed); draw(arc((O+NN)/2, NN, X), dashed); draw(rightanglemark(K, L, NN, 100)); draw(rightanglemark(K, M, NN, 100)); draw(rightanglemark(L, X, NN, 100)); dot("$K$", K, SW); dot("$L$", L, unit(L)); dot("$M$", M, unit(M)); dot("$N$", NN, SE); dot("$X$", X, S); [/asy] Notice that $KLMN$ is inscribed in the circle with diameter $\overline{KN}$ and $XOMN$ is inscribed in the circle with diameter $\overline{ON}$ . Furthermore, $(XLN)$ is tangent to $\overline{KL}$ . Then, \[KO\cdot KM=KX\cdot KN=KL^2\implies KM=\frac{28^2}{8}=98,\] and $MO=KM-KO=\boxed{090}$ .
(Solution by TheUltimate123)
If you're wondering why $KX \cdot KN=KL^2,$ it's because PoP on $(XLN)$ or by $KX \cdot KN=KX \cdot (KX+XN)=KX^2+KX \cdot XN=KX^2+LX^2=KL^2$ (last part by geometric mean theorem / similarity).
Note: the "semicircle" circumscribing points XOMN is not a semicircle. That is just there to tell you that X, O, M, N are indeed concyclic, so ignore the subtlety of the diagram that makes O seems slightly off the marks than it should be.

## Solution 7 (Alternative PoP)
[asy] size(250); real h = sqrt(98^2+65^2); real l = sqrt(h^2-28^2); pair K = (0,0); pair N = (h, 0); pair M = ((98^2)/h, (98*65)/h); pair L = ((28^2)/h, (28*l)/h); pair P = ((28^2)/h, 0); pair O = ((28^2)/h, (8*65)/h); draw(K--L--N); draw(K--M--N--cycle); draw(L--M); label("K", K, SW); label("L", L, NW); label("M", M, NE); label("N", N, SE); draw(L--P); label("P", P, S); dot(O); label("O", shift((1,1))*O, NNE); label("28", scale(1/2)*L, W); label("65", ((M.x+N.x)/2, (M.y+N.y)/2), NE); [/asy]
(Diagram by vedadehhc)
Call the base of the altitude from $L$ to $NK$ point $P$ . Let $PO=x$ . Now, we have that $KP=\sqrt{64-x^2}$ by the Pythagorean Theorem. Once again by Pythagorean, $LO=\sqrt{720+x^2}-x$ . Using Power of a Point, we have
\[(KO)(OM)=(LO)(OQ)\] ( $Q$ is the intersection of $OL$ with the circle $\neq L$ )
\[8(MO)=(\sqrt{720+x^2}-x)(\sqrt{720+x^2}+x)\]
\[8(MO)=720\]
\[MO=\boxed{090}\] .
(Solution by RootThreeOverTwo) \[\]
### Remark: Length of OQ
Since $P$ is on the circle’s diameter, $QP = LP = \sqrt{720+x^2}$ . So, $OQ = PQ + PO = x + \sqrt{720+x^2}$ . ~diyarv

## Solution8 (just one pair of similar triangles)
[asy] size(250); real h = sqrt(98^2+65^2); real l = sqrt(h^2-28^2); pair K = (0,0); pair N = (h, 0); pair M = ((98^2)/h, (98*65)/h); pair L = ((28^2)/h, (28*l)/h); pair P = ((28^2)/h, 0); pair O = ((28^2)/h, (8*65)/h); draw(K--L--N); draw(K--M--N--cycle); draw(L--M); label("K", K, SW); label("L", L, NW); label("M", M, NE); label("N", N, SE); draw(L--P); label("P", P, S); dot(O); label("O", shift((1,1))*O, NNE); label("28", scale(1/2)*L, W); label("65", ((M.x+N.x)/2, (M.y+N.y)/2), NE); [/asy] Note that since $\angle KLN = \angle KMN$ , quadrilateral $KLMN$ is cyclic. Therefore, we have \[\angle LMK = \angle LNK = 90^{\circ} - \angle LKN = \angle KLP,\] so $\triangle KLO \sim \triangle KML$ , giving \[\frac{KM}{28} = \frac{28}{8} \implies KM = 98.\] Therefore, $OM = 98-8 = \boxed{90}$ .

## Solution 9 (Pythagoras Bash)
[asy] size(250); real h = sqrt(98^2+65^2); real l = sqrt(h^2-28^2); pair K = (0,0); pair N = (h, 0); pair M = ((98^2)/h, (98*65)/h); pair L = ((28^2)/h, (28*l)/h); pair P = ((28^2)/h, 0); pair O = ((28^2)/h, (8*65)/h); draw(K--L--N); draw(K--M--N--cycle); draw(L--M); label("K", K, SW); label("L", L, NW); label("M", M, NE); label("N", N, SE); draw(L--P); label("P", P, S); dot(O); label("O", shift((1,1))*O, NNE); label("28", scale(1/2)*L, W); label("65", ((M.x+N.x)/2, (M.y+N.y)/2), NE); [/asy]
By Pythagorean Theorem, $KM^2+65^2 = KN^2 = 28^2 + LN^2$ . Thus, $LN^2 = KM^2 + 65^2 - 28^2$ .
By Pythagorean Theorem, $KP^2 + LP^2 = 28^2$ , and $PN^2 + LP^2 = LN^2$ .
\[PN^2 = (KN - KP)^2 = (\sqrt{KM^2 + 65^2} - KP)^2\]
It follows that \[(\sqrt{KM^2 + 65^2} - KP)^2 + LP^2 = KM^2 + 65^2 - 28^2\]
\[KM^2 + 65^2 - 2\sqrt{KM^2 + 65^2}(KP) + KP^2 + LP^2 = KM^2 + 65^2 - 28^2\]
Since $KP^2 + LP^2 = 28^2$ , \[KM^2 + 65^2 - 2\sqrt{KM^2 + 65^2}(KP) + 28^2 = KM^2 + 65^2 - 28^2\]
\[-2\sqrt{KM^2 + 65^2}(KP) = -2 \times 28^2\]
\[KP = \frac{28^2}{\sqrt{KM^2 + 65^2}}\]
$\angle OKP = \angle NKM$ (it's the same angle) and $\angle OPK = \angle KMN = 90^{\circ}$ . Thus, $\triangle KOP \sim \triangle KNM$ .
Thus,
\[\frac{KO}{KN} = \frac{KP}{KM}\]
\[\frac{8}{\sqrt{KM^2 + 65^2}} = \frac{\frac{28^2}{\sqrt{KM^2 + 65^2}}}{KM}\]
Multiplying both sides by $\sqrt{KM^2 + 65^2}$ :
\[8 = \frac{28^2}{KM}\]
\[KM = 98\]
Therefore, $OM = 98-8 = \boxed{90}$
~ Solution by adam_zheng

## Video Solution
Video Solution: https://www.youtube.com/watch?v=0AXF-5SsLc8

## Video Solution 2
https://youtu.be/I-8xZGhoDUY
~Shreyas S

## Video Solution 3
https://www.youtube.com/watch?v=pP3cih_8bg4
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .