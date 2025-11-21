# 2015 AMC 8 Problem 2

## Problem

Point $O$ is the center of the regular octagon $ABCDEFGH$ , and $X$ is the midpoint of the side $\overline{AB}.$ What fraction of the area of the octagon is shaded?

$\textbf{(A) }\frac{11}{32} \quad\textbf{(B) }\frac{3}{8} \quad\textbf{(C) }\frac{13}{32} \quad\textbf{(D) }\frac{7}{16}\quad \textbf{(E) }\frac{15}{32}$

[asy] pair A,B,C,D,E,F,G,H,O,X; A=dir(45); B=dir(90); C=dir(135); D=dir(180); E=dir(-135); F=dir(-90); G=dir(-45); H=dir(0); O=(0,0); X=midpoint(A--B); fill(X--B--C--D--E--O--cycle,rgb(0.75,0.75,0.75)); draw(A--B--C--D--E--F--G--H--cycle); dot("$A$",A,dir(45)); dot("$B$",B,dir(90)); dot("$C$",C,dir(135)); dot("$D$",D,dir(180)); dot("$E$",E,dir(-135)); dot("$F$",F,dir(-90)); dot("$G$",G,dir(-45)); dot("$H$",H,dir(0)); dot("$X$",X,dir(135/2)); dot("$O$",O,dir(0)); draw(E--O--X); [/asy]

## Solutions

## Solution 1
Since octagon $ABCDEFGH$ is a regular octagon, it is split into $8$ equal parts, such as triangles $\bigtriangleup ABO, \bigtriangleup BCO, \bigtriangleup CDO$ , etc. These parts, since they are all equal, are $\frac{1}{8}$ of the octagon each. The shaded region consists of $3$ of these equal parts plus half of another, so the fraction of the octagon that is shaded is $\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{16}=\boxed{\textbf{(D) }\dfrac{7}{16}}.$

## Solution 2
[asy] pair A,B,C,D,E,F,G,H,O,X,a,b,c,d,e,f,g; A=dir(45); B=dir(90); C=dir(135); D=dir(180); E=dir(-135); F=dir(-90); G=dir(-45); H=dir(0); O=(0,0); X=midpoint(A--B); a=midpoint(B--C); b=midpoint(C--D); c=midpoint(D--E); d=midpoint(E--F); e=midpoint(F--G); f=midpoint(G--H); g=midpoint(H--A); fill(X--B--C--D--E--O--cycle,rgb(0.75,0.75,0.75)); draw(A--B--C--D--E--F--G--H--cycle); dot("$A$",A,dir(45)); dot("$B$",B,dir(90)); dot("$C$",C,dir(135)); dot("$D$",D,dir(180)); dot("$E$",E,dir(-135)); dot("$F$",F,dir(-90)); dot("$G$",G,dir(-45)); dot("$H$",H,dir(0)); dot("$X$",X,dir(135/2)); dot("$O$",O,dir(0)); draw(E--O--X); draw(B--F); draw(A--O); draw(D--H); draw(C--G); draw(a--e); draw(b--f); draw(c--g); draw(d--O); [/asy]
The octagon has been divided up into $16$ identical triangles (and thus they each have equal area). Since the shaded region occupies $7$ out of the $16$ total triangles, the answer is $\boxed{\textbf{(D)}~\dfrac{7}{16}}$ .
-Flare

## Solution 3
For starters, what I find helpful is to divide the whole octagon up into triangles as shown here: [asy] pair A,B,C,D,E,F,G,H,O,X; A=dir(45); B=dir(90); C=dir(135); D=dir(180); E=dir(-135); F=dir(-90); G=dir(-45); H=dir(0); O=(0,0); X=midpoint(A--B); fill(X--B--C--D--E--O--cycle,rgb(0.75,0.75,0.75)); draw(A--B--C--D--E--F--G--H--cycle); dot("$A$",A,dir(45)); dot("$B$",B,dir(90)); dot("$C$",C,dir(135)); dot("$D$",D,dir(180)); dot("$E$",E,dir(-135)); dot("$F$",F,dir(-90)); dot("$G$",G,dir(-45)); dot("$H$",H,dir(0)); dot("$X$",X,dir(135/2)); dot("$O$",O,dir(0)); draw(E--O--X); draw(C--O--B); draw(B--O--A); draw(A--O--H); draw(H--O--G); draw(G--O--F); draw(F--O--E); draw(E--O--D); draw(D--O--C); [/asy]
Now, it is just a matter of counting the larger triangles. Remember that $\triangle BOX$ and $\triangle XOA$ are not full triangles and are only half for these purposes. We count it up and we get a total of $\frac{3.5}{8}$ of the shape shaded. We then simplify it to get our answer of $\boxed{\textbf{(D)}~\frac{7}{16}}$ .

## Solution 4
[asy] pair A,B,C,D,E,F,G,H,O,X; A=dir(45); B=dir(90); C=dir(135); D=dir(180); E=dir(-135); F=dir(-90); G=dir(-45); H=dir(0); O=(0,0); X=midpoint(A--B); fill(X--B--C--D--E--O--cycle,rgb(0.75,0.75,0.75)); draw(A--B--C--D--E--F--G--H--cycle); dot("$A$",A,dir(45)); dot("$B$",B,dir(90)); dot("$C$",C,dir(135)); dot("$D$",D,dir(180)); dot("$E$",E,dir(-135)); dot("$F$",F,dir(-90)); dot("$G$",G,dir(-45)); dot("$H$",H,dir(0)); dot("$X$",X,dir(135/2)); dot("$O$",O,dir(0)); draw(E--O--X); draw(C--O--B); draw(B--O--A); draw(A--O--H); draw(H--O--G); draw(G--O--F); draw(F--O--E); draw(E--O--D); draw(D--O--C); [/asy]
We can divide the octagon into 8 parts and pretend that the area is 64. We know that X is the midpoint of BA and that each space between two points is 8 because 64/8=8. This means that BX=4 because 8/2=4. Then, we add that to 3*8 because there are 3 spaces between points that are each 8. After that, you turn it into a fraction, 28/64, and simplify to get $\boxed{\textbf{(D)}~\frac{7}{16}}$ .

## Solution 5 (Quick and Efficient)
[asy] pair A,B,C,D,E,F,G,H,O,X; A=dir(45); B=dir(90); C=dir(135); D=dir(180); E=dir(-135); F=dir(-90); G=dir(-45); H=dir(0); O=(0,0); X=midpoint(A--B); fill(X--B--C--D--E--O--cycle,rgb(0.75,0.75,0.75)); draw(A--B--C--D--E--F--G--H--cycle); dot("$A$",A,dir(45)); dot("$B$",B,dir(90)); dot("$C$",C,dir(135)); dot("$D$",D,dir(180)); dot("$E$",E,dir(-135)); dot("$F$",F,dir(-90)); dot("$G$",G,dir(-45)); dot("$H$",H,dir(0)); dot("$X$",X,dir(135/2)); dot("$O$",O,dir(0)); draw(E--O--X); [/asy] We see that the midpoint of $\overline{AB}$ is $X$ . We can also notice that point $X$ to point $E$ *ALMOST* makes the octagon half shaded. Since we know an octagon has 8 sides, $X$ is one-half of $\overline{AB}$ which means instead of counting in eights, we need to count in sixteenths. Now back to the problem. Let's say that the midpoint of $\overline{EF}$ is $Y$ , then $\overline{XY}$ cuts the octagon perfectly in half, but since there is no $Y$ , we are now $\frac1{16}$ away from one-half. We know that $\frac1{2}=\frac8{16}$ , so we can just do $\frac8{16}-\frac1{16}$ which gets us, for the final answer, $\boxed{\textbf{(D)}~\frac{7}{16}}$ .
~ AM24

## Video Solution (HOW TO THINK CRITICALLY!!)
https://youtu.be/azFKEreETAw
~Education, the Study of Everything

## Video Solution
https://youtu.be/NbIav9YlPEY
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/51K3uCzntWs?t=2314
~ pi_is_3.14
### See Also