# 2019 AIME II Problem 15

## Problem

In acute triangle $ABC$ points $P$ and $Q$ are the feet of the perpendiculars from $C$ to $\overline{AB}$ and from $B$ to $\overline{AC}$ , respectively. Line $PQ$ intersects the circumcircle of $\triangle ABC$ in two distinct points, $X$ and $Y$ . Suppose $XP=10$ , $PQ=25$ , and $QY=15$ . The value of $AB\cdot AC$ can be written in the form $m\sqrt n$ where $m$ and $n$ are positive integers, and $n$ is not divisible by the square of any prime. Find $m+n$ .

### Diagram

[asy] size(200); defaultpen(linewidth(0.4)+fontsize(10)); pen s = linewidth(0.8)+fontsize(8); pair A,B,C,P,Q,X,Y,O; O = origin; real theta = 32; A = dir(180+theta); B = dir(-theta); C = dir(75); Q = foot(B,A,C); P = foot(C,A,B); path c = circumcircle(A,B,C); X = IP(c, Q--(2*P-Q)); Y = IP(c, P--(2*Q-P)); draw(A--B--C--A, black+0.8); draw(c^^X--Y^^B--Q^^C--P); dot("$A$", A, SW); dot("$B$", B, SE); dot("$C$", C, N); dot("$P$", P, SW); dot("$Q$", Q, W); dot("$X$", X, SE); dot("$Y$", Y, NW); label("$25$", P--Q, SW); label("$15$", Q--Y, SW); label("$10$", X--P, SW); [/asy]

## Solution 1
First we have $a\cos A=PQ=25$ , and $(a\cos A)(c\cos C)=(a\cos C)(c\cos A)=AP\cdot PB=10(25+15)=400$ by PoP. Similarly, $(a\cos A)(b\cos B)=15(10+25)=525,$ and dividing these each by $a\cos A$ gives $b\cos B=21,c\cos C=16$ .
It is known that the sides of the orthic triangle are $a\cos A,b\cos B,c\cos C$ , and its angles are $\pi-2A$ , $\pi-2B$ , and $\pi-2C$ . We thus have the three sides of the orthic triangle now. Letting $D$ be the foot of the altitude from $A$ , we have, in $\triangle DPQ$ , \[\cos P,\cos Q=\frac{21^2+25^2-16^2}{2\cdot 21\cdot 25},\frac{16^2+25^2-21^2}{2\cdot 16\cdot 25}= \frac{27}{35}, \frac{11}{20}.\] \[\Rightarrow \cos B=\cos\left(\tfrac 12 (\pi-P)\right)=\sin\tfrac 12 P =\sqrt{\frac{4}{35}},\] similarly, we get \[\cos C=\cos\left(\tfrac 12 (\pi-Q)\right)=\sin\tfrac 12 Q=\sqrt{\frac{9}{40}}.\] To finish, \[bc= \frac{(b\cos B)(c\cos C)}{\cos B\cos C}=\frac{16\cdot 21}{(2/\sqrt{35})(3/\sqrt{40})}=560\sqrt{14}.\] The requested sum is $\boxed{574}$ . - crazyeyemoody907
Remark: The proof that $a \cos A = PQ$ can be found here: http://www.irmo.ie/5.Orthic_triangle.pdf

## Solution 2
Let $BC=a$ , $AC=b$ , and $AB=c$ . Let $\cos\angle A=k$ . Then $AP=bk$ and $AQ=ck$ .
By Power of a Point theorem, \begin{align} AP\cdot BP=XP\cdot YP \quad &\Longrightarrow \quad b^2k^2-bck+400=0\\ AQ\cdot CQ=YQ\cdot XQ \quad &\Longrightarrow \quad c^2k^2-bck+525=0 \end{align} Thus $bck = (bk)^2+400=(ck)^2+525 = u$ . Then $bk=\sqrt{u-400}$ , $ck=\sqrt{u-525}$ , and \[k=\sqrt{\frac{(u-400)(u-525)}{u^2}}\] Use the Law of Cosines in $\triangle APQ$ to get $25^2=b^2k^2+c^2k^2-2bck^3 = 2bck-925-2bck^3$ , which rearranges to \[775=bck - k^2\cdot bck = u-\frac{(u-400)(u-525)}{u}\] Upon simplification, this reduces to a linear equation in $u$ , with solution $u=1400$ . Then \[AB\cdot AC = bc = \frac 1{k}\cdot bck = \frac{u^2}{\sqrt{(u-400)(u-525)}}=560 \sqrt{14}\] So the final answer is $560 + 14 = \boxed{574}$
By SpecialBeing2017

## Solution 3
Let $AP=p$ , $PB=q$ , $AQ=r$ , and $QC=s$ . By Power of a Point, \begin{align} AP\cdot PB=XP\cdot YP \quad &\Longrightarrow \quad pq=400\\ AQ\cdot QC=YQ\cdot XQ \quad &\Longrightarrow \quad rs=525 \end{align} Points $P$ and $Q$ lie on the circle, $\omega$ , with diameter $BC$ , and pow $(A,\omega) = AP\cdot AB = AQ\cdot AC$ , so \[p(p+q)=r(r+s)\quad \Longrightarrow \quad p^2-r^2=125\] Use Law of Cosines in $\triangle APQ$ to get $25^2=p^2+r^2-2pr\cos A$ ; since $\cos A = \frac r{p+q}$ , this simplifies as \[500 \ =\ 2r^2-\frac{2pr^2}{p+q} \ =\ 2r^2-\frac{2p^2r^2}{p^2+400} \ =\ \frac{800r^2}{r^2+525}\] We get $r=5\sqrt{35}$ and thus \[r=5\sqrt{35}, \quad p = \sqrt{r^2+125} = 10\sqrt{10}, \quad q = \frac{400}{p} =4\sqrt{10}, \quad s= \frac{525}{r} = 3\sqrt{35}.\] Therefore $AB\cdot AC = (p+q)\cdot(r+s) = 560\sqrt{14}$ . So the answer is $560 + 14 = \boxed{574}$
By asr41

## Solution 4 (Clean)
This solution is directly based of @CantonMathGuy's solution. We start off with a key claim.
Claim. $XB \parallel AC$ and $YC \parallel AB$ .
Proof.
Let $E$ and $F$ denote the reflections of the orthocenter over points $P$ and $Q$ , respectively. Since $EF \parallel XY$ and \[EF = 2 PQ = XP + PQ + QY = XY,\] we have that $E X Y F$ is a rectangle. Then, since $\angle XYF = 90^\circ$ we obtain $\angle XBF = 90^\circ$ (which directly follows from $XBYF$ being cyclic); hence $\angle XBQ = \angle AQB$ , or $XB \parallel AQ \Rightarrow XB \parallel AC$ .
Similarly, we can obtain $YC \parallel AB$ . $\ \blacksquare$
A direct result of this claim is that $\triangle BPX \sim \triangle APQ \sim \triangle CYQ$ .
Thus, we can set $AP = 5k$ and $BP = 2k$ , then applying Power of a Point on $P$ we get $10 \cdot 40 = 10k^2 \implies k = 2\sqrt{10} \implies AB = 14 \sqrt{10}$ . Also, we can set $AQ = 5l$ and $CQ = 3l$ and once again applying Power of a Point (but this time to $Q$ ) we get
$\phantom{...................}15 \cdot 35 = 15l^2 \implies l = \sqrt{35} \implies AC = 8 \sqrt{35}$ .
Hence,
$\phantom{...................}AB \cdot AC = 112 \sqrt{350} = 112 \cdot 5 \sqrt{14} = 560 \sqrt{14}$
and the answer is $560 + 14 = \boxed{574}$ . ~rocketsri

## Solution 5
mathboy282

## Video Solution
2019 AIME II #15
MathProblemSolvingSkills.com

## Video Solution by MOP 2024
https://youtu.be/aYV09qIwTqs
~r00tsOfUnity

## Video Solution by Mr. Math
https://www.youtube.com/watch?v=rpNnK5n0_P0
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .