# 2002 AIME II Problem 13

## Problem

In triangle $ABC,$ point $D$ is on $\overline{BC}$ with $CD = 2$ and $DB = 5,$ point $E$ is on $\overline{AC}$ with $CE = 1$ and $EA = 3,$ $AB = 8,$ and $\overline{AD}$ and $\overline{BE}$ intersect at $P.$ Points $Q$ and $R$ lie on $\overline{AB}$ so that $\overline{PQ}$ is parallel to $\overline{CA}$ and $\overline{PR}$ is parallel to $\overline{CB}.$ It is given that the ratio of the area of triangle $PQR$ to the area of triangle $ABC$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Let $X$ be the intersection of $\overline{CP}$ and $\overline{AB}$ .
[asy] size(10cm); pair A,B,C,D,E,X,P,Q,R; A=(0,0); B=(8,0); C=(1.9375,3.4994); D=(3.6696,2.4996); E=(1.4531,2.6246); X=(4.3636,0); P=(2.9639,2.0189); Q=(1.8462,0); R=(6.4615,0); dot(A); dot(B); dot(C); dot(D); dot(E); dot(X); dot(P); dot(Q); dot(R); label("$A$",A,WSW); label("$B$",B,ESE); label("$C$",C,NNW); label("$D$",D,NE); label("$E$",E,WNW); label("$X$",X,SSE); label("$P$",P,NNE); label("$Q$",Q,SSW); label("$R$",R,SE); draw(A--B--C--cycle); draw(P--Q--R--cycle); draw(A--D); draw(B--E); draw(C--X); [/asy]
Since $\overline{PQ} \parallel \overline{CA}$ and $\overline{PR} \parallel \overline{CB}$ , $\angle CAB = \angle PQR$ and $\angle CBA = \angle PRQ$ . So $\Delta ABC \sim \Delta QRP$ , and thus, $\frac{[\Delta PQR]}{[\Delta ABC]} = \left(\frac{PX}{CX}\right)^2$ .
Using mass points :
WLOG , let $W_C=15$ .
Then:
$W_A = \left(\frac{CE}{AE}\right)W_C = \frac{1}{3}\cdot15=5$ .
$W_B = \left(\frac{CD}{BD}\right)W_C = \frac{2}{5}\cdot15=6$ .
$W_X=W_A+W_B=5+6=11$ .
$W_P=W_C+W_X=15+11=26$ .
Thus, $\frac{PX}{CX}=\frac{W_C}{W_P}=\frac{15}{26}$ . Therefore, $\frac{[\Delta PQR]}{[\Delta ABC]} = \left( \frac{15}{26} \right)^2 = \frac{225}{676}$ , and $m+n=\boxed{901}$ . Note we can just use mass points to get $\left( \frac{15}{26} \right)^2= \frac{225}{676}$ which is $\boxed{901}$ .

## Solution 2
First draw $\overline{CP}$ and extend it so that it meets with $\overline{AB}$ at point $X$ .
[asy] size(10cm); pair A,B,C,D,E,X,P,Q,R; A=(0,0); B=(8,0); C=(1.9375,3.4994); D=(3.6696,2.4996); E=(1.4531,2.6246); X=(4.3636,0); P=(2.9639,2.0189); Q=(1.8462,0); R=(6.4615,0); dot(A); dot(B); dot(C); dot(D); dot(E); dot(X); dot(P); dot(Q); dot(R); label("$A$",A,WSW); label("$B$",B,ESE); label("$C$",C,NNW); label("$D$",D,NE); label("$E$",E,WNW); label("$X$",X,SSE); label("$P$",P,NNE); label("$Q$",Q,SSW); label("$R$",R,SE); draw(A--B--C--cycle); draw(P--Q--R--cycle); draw(A--D); draw(B--E); draw(C--X); [/asy]
We have that $[ABC]=\frac{1}{2}\cdot AC \cdot BC\sin{C}=\frac{1}{2}\cdot 4\cdot {7}\sin{C}=14\sin{C}$
By Ceva's, \[3\cdot{\frac{2}{5}}\cdot{\frac{BX}{AX}}=1\implies BX=\frac{5\cdot AX}{6}\] That means that \[\frac{11\cdot {AX}}{6}=8\implies AX=\frac{48}{11} \ \text{and} \ BX=\frac{40}{11}\]
Now we apply mass points. Assume WLOG that $W_{A}=1$ . That means that
\[W_{C}=3, W_{B}=\frac{6}{5}, W_{X}=\frac{11}{5}, W_{D}=\frac{21}{5}, W_{E}=4, W_{P}=\frac{26}{5}\]
Notice now that $\triangle{PBQ}$ is similar to $\triangle{EBA}$ . Therefore,
\[\frac{PQ}{EA}=\frac{PB}{EB}\implies \frac{PQ}{3}=\frac{10}{13}\implies PQ=\frac{30}{13}\]
Also, $\triangle{PRA}$ is similar to $\triangle{DBA}$ . Therefore,
\[\frac{PA}{DA}=\frac{PR}{DB}\implies \frac{21}{26}=\frac{PR}{5}\implies PR=\frac{105}{26}\]
Because $\triangle{PQR}$ is similar to $\triangle{CAB}$ , $\angle{C}=\angle{P}$ .
As a result, $[PQR]=\frac{1}{2}\cdot PQ \cdot PR \sin{C}=\frac{1}{2}\cdot \frac{30}{13}\cdot \frac{105}{26}\sin{P}=\frac{1575}{338}\sin{C}$ .
Therefore, \[\frac{[PQR]}{[ABC]}=\frac{\frac{1575}{338}\sin{C}}{14\sin{C}}=\frac{225}{676}\implies 225+676=\boxed{901}\]
- Not the author writing here, but a note is that Ceva's Theorem was actually not necessary to solve this problem. The information was just nice to know :)

## Solution 3
[asy] size(10cm); pair A,B,C,D,E,P,Q,R; A=(0,0); B=(8,0); C=(1.9375,3.4994); D=(3.6696,2.4996); E=(1.4531,2.6246); P=(2.9639,2.0189); Q=(1.8462,0); R=(6.4615,0); dot(A); dot(B); dot(C); dot(D); dot(E); dot(P); dot(Q); dot(R); label("$A$",A,WSW); label("$B$",B,ESE); label("$C$",C,NNW); label("$D$",D,NE); label("$E$",E,WNW); label("$P$",P,NNE); label("$Q$",Q,SSW); label("$R$",R,SE); draw(A--B--C--cycle); draw(P--Q--R--cycle); draw(A--D); draw(B--E); [/asy] Use the mass of point. Denoting the mass of $C=15,B=6,A=5,D=21,E=20$ , we can see that the mass of $P$ is $26$ , hence we know that $\frac{BP}{PE}=\frac{10}{3}$ , now we can find that $\frac{PQ}{AE}=\frac{10}{13}$ which implies $PQ=\frac{30}{13}$ , it is obvious that $\triangle{PQR}$ is similar to $\triangle{ACB}$ so we need to find the ration between PQ and AC, which is easy, it is $\frac{15}{26}$ , so our final answer is $\left( \frac{15}{26} \right)^2= \frac{225}{676}$ which is $\boxed{901}$ . ~bluesoul

## Solution 4(Ceva & Menelaus)
Construct $\overline{CP}$ and extend it to line $\overline{AB}$ at point $F$ .
[asy] size(10cm); pair A,B,C,D,E,F,P,Q,R; A=(0,0); B=(8,0); C=(1.9375,3.4994); D=(3.6696,2.4996); E=(1.4531,2.6246); F=(4.3636,0); P=(2.9639,2.0189); Q=(1.8462,0); R=(6.4615,0); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(P); dot(Q); dot(R); label("$A$",A,WSW); label("$B$",B,ESE); label("$C$",C,NNW); label("$D$",D,NE); label("$E$",E,WNW); label("$F$",F,SSE); label("$P$",P,NNE); label("$Q$",Q,SSW); label("$R$",R,SE); draw(A--B--C--cycle); draw(P--Q--R--cycle); draw(A--D); draw(B--E); draw(C--F); [/asy]
Using Ceva's Theorem on triangle $ABC$ and point $P$ , we get \[\frac{AF}{BF} \times \frac{BD}{CD} \times \frac{CE}{AE}=1\] Thus, $\frac{AF}{BF}=\frac{6}{5}$ . Then, using this info, we apply Menelaus on triangle $ACF$ and line $BE$ , obtaining \[\frac{AE}{BE} \times \frac{CP}{FP} \times \frac{FB}{AB}=1\] Simplifying and substituting, we find that $\frac{CP}{FP}=\frac{11}{15}$ . Alternatively, $\frac{FP}{CF}=\frac{15}{26}$ , which is also the ratio between the heights of the desired triangles. Finishing, $\left( \frac{15}{26} \right)^2= \frac{225}{676}$ achieving the final answer of $\boxed{901}$ . ~faliure167
These problems are copyrighted © by the Mathematical Association of America.