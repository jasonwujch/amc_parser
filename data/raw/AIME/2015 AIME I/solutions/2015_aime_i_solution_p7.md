# 2015 AIME I Problem 7

## Problem

In the diagram below, $ABCD$ is a square. Point $E$ is the midpoint of $\overline{AD}$ . Points $F$ and $G$ lie on $\overline{CE}$ , and $H$ and $J$ lie on $\overline{AB}$ and $\overline{BC}$ , respectively, so that $FGHJ$ is a square. Points $K$ and $L$ lie on $\overline{GH}$ , and $M$ and $N$ lie on $\overline{AD}$ and $\overline{AB}$ , respectively, so that $KLMN$ is a square. The area of $KLMN$ is 99. Find the area of $FGHJ$ .

[asy] pair A,B,C,D,E,F,G,H,J,K,L,M,N; B=(0,0); real m=7*sqrt(55)/5; J=(m,0); C=(7*m/2,0); A=(0,7*m/2); D=(7*m/2,7*m/2); E=(A+D)/2; H=(0,2m); N=(0,2m+3*sqrt(55)/2); G=foot(H,E,C); F=foot(J,E,C); draw(A--B--C--D--cycle); draw(C--E); draw(G--H--J--F); pair X=foot(N,E,C); M=extension(N,X,A,D); K=foot(N,H,G); L=foot(M,H,G); draw(K--N--M--L); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,dir(90)); label("$F$",F,NE); label("$G$",G,NE); label("$H$",H,W); label("$J$",J,S); label("$K$",K,SE); label("$L$",L,SE); label("$M$",M,dir(90)); label("$N$",N,dir(180)); [/asy]

## Solution 1
Let us find the proportion of the side length of $KLMN$ and $FJGH$ . Let the side length of $KLMN=y$ and the side length of $FJGH=x$ .
[asy] pair A,B,C,D,E,F,G,H,J,K,L,M,N,P; B=(0,0); real m=7*sqrt(55)/5; J=(m,0); C=(7*m/2,0); A=(0,7*m/2); D=(7*m/2,7*m/2); E=(A+D)/2; H=(0,2m); N=(0,2m+3*sqrt(55)/2); G=foot(H,E,C); F=foot(J,E,C); draw(A--B--C--D--cycle); draw(C--E); draw(G--H--J--F); pair X=foot(N,E,C); M=extension(N,X,A,D); K=foot(N,H,G); L=foot(M,H,G); draw(K--N--M--L); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,dir(90)); label("$F$",F,NE); label("$G$",G,NE); label("$H$",H,W); label("$J$",J,S); label("$K$",K,SE); label("$L$",L,SE); label("$M$",M,dir(90)); label("$N$",N,dir(180)); [/asy]
Now, examine $BC$ . We know $BC=BJ+JC$ , and triangles $\Delta BHJ$ and $\Delta JFC$ are similar to $\Delta EDC$ since they are $1-2-\sqrt{5}$ triangles. Thus, we can rewrite $BC$ in terms of the side length of $FJGH$ . \[BJ=\frac{1}{\sqrt{5}}HJ=\frac{x}{\sqrt{5}}=\frac{x\sqrt{5}}{5}, JC=\frac{\sqrt{5}}{2}JF=\frac{x\sqrt{5}}{2}\Rightarrow BC=\frac{7x\sqrt{5}}{10}\]
Now examine $AB$ . We can express this length in terms of $x,y$ since $AB=AN+NH+HB$ . By using similar triangles as in the first part, we have \[AB=\frac{1}{\sqrt{5}}y+\frac{\sqrt{5}}{2}y+\frac{2}{\sqrt{5}}x\] \[AB=BC\Rightarrow \frac{7y\sqrt{5}}{10}+\frac{2x\sqrt{5}}{5}=\frac{7x\sqrt{5}}{10}\Rightarrow \frac{7y\sqrt{5}}{10}=\frac{3x\sqrt{5}}{10}\Rightarrow 7y=3x\]
Now, it is trivial to see that $[FJGH]=\left(\frac{x}{y}\right)^2[KLMN]=\left(\frac{7}{3}\right)^2\cdot 99=\boxed{539}.$

## Solution 2
[asy] pair A,B,C,D,E,F,G,H,J,K,L,M,N,P; B=(0,0); real m=7*sqrt(55)/5; J=(m,0); C=(7*m/2,0); A=(0,7*m/2); D=(7*m/2,7*m/2); E=(A+D)/2; H=(0,2m); N=(0,2m+3*sqrt(55)/2); G=foot(H,E,C); F=foot(J,E,C); draw(A--B--C--D--cycle); draw(C--E); draw(G--H--J--F); pair X=foot(N,E,C); M=extension(N,X,A,D); K=foot(N,H,G); L=foot(M,H,G); draw(K--N--M--L); P=foot(E,M,L); draw(P--E); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,dir(90)); label("$F$",F,NE); label("$G$",G,NE); label("$H$",H,W); label("$J$",J,S); label("$K$",K,SE); label("$L$",L,SE); label("$M$",M,dir(90)); label("$N$",N,dir(180)); label("$P$",P,dir(235)); [/asy]
We begin by denoting the length $ED$ $a$ , giving us $DC = 2a$ and $EC = a\sqrt5$ . Since angles $\angle DCE$ and $\angle FCJ$ are complementary, we have that $\triangle CDE \sim \triangle JFC$ (and similarly the rest of the triangles are $1-2-\sqrt5$ triangles). We let the sidelength of $FGHJ$ be $b$ , giving us:
\[JC = \sqrt5 \cdot FC = \sqrt5 \cdot FJ/2 = \frac{b\sqrt 5}{2}\] and \[BJ = \frac{1}{\sqrt5} \cdot HJ = \frac{b}{\sqrt5}\]
Since $BC = CJ + BJ$ ,
\[2a = \frac{b\sqrt 5}{2} + \frac{b}{\sqrt5}\]
Solving for $b$ in terms of $a$ yields \[b = \frac{4a\sqrt5}{7}\]
We now use the given that $[KLMN] = 99$ , implying that $KL = LM = MN = NK = 3\sqrt{11}$ . We also draw the perpendicular from $E$ to $ML$ and label the point of intersection $P$ as in the diagram at the top
This gives that \[AM = 2 \cdot AN = 2 \cdot \frac{3\sqrt{11}}{\sqrt5}\] and \[ME = \sqrt5 \cdot MP = \sqrt5 \cdot \frac{EP}{2} = \sqrt5 \cdot \frac{LG}{2} = \sqrt5 \cdot \frac{HG - HK - KL}{2} = \sqrt{5} \cdot \frac{\frac{4a\sqrt5}{7} - \frac{9\sqrt{11}}{2}}{2}\]
Since $AE$ = $AM + ME$ , we get
\[2 \cdot \frac{3\sqrt{11}}{\sqrt5} + \sqrt{5} \cdot \frac{\frac{4a\sqrt5}{7} - \frac{9\sqrt{11}}{2}}{2} = a\]
\[\Rightarrow 12\sqrt{11} + 5(\frac{4a\sqrt5}{7} - \frac{9\sqrt{11}}{2}) = 2\sqrt5a\]
\[\Rightarrow \frac{-21}{2}\sqrt{11} + \frac{20a\sqrt5}{7} = 2\sqrt5a\]
\[\Rightarrow -21\sqrt{11} = 2\sqrt5a\frac{14 - 20}{7}\]
\[\Rightarrow \frac{49\sqrt{11}}{4} = \sqrt5a\]
\[\Rightarrow 7\sqrt{11} = \frac{4a\sqrt{5}}{7}\]
So our final answer is $(7\sqrt{11})^2 = \boxed{539}$ .

## Solution 3
This is a relatively quick solution but a fakesolve. We see that with a ruler, $KL = \frac{3}{2}$ cm and $HG = \frac{7}{2}$ cm. Thus if $KL$ corresponds with an area of $99$ , then $HG$ ( $FGHJ$ 's area) would correspond with $99*(\frac{7}{3})^2 = \boxed{539}$ - aops5234
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .