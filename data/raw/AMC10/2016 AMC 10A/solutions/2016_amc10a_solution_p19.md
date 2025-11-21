# 2016 AMC 10A Problem 19

## Problem

In rectangle $ABCD,$ $AB=6$ and $BC=3$ . Point $E$ between $B$ and $C$ , and point $F$ between $E$ and $C$ are such that $BE=EF=FC$ . Segments $\overline{AE}$ and $\overline{AF}$ intersect $\overline{BD}$ at $P$ and $Q$ , respectively. The ratio $BP:PQ:QD$ can be written as $r:s:t$ where the greatest common factor of $r,s,$ and $t$ is $1.$ What is $r+s+t$ ?

$\textbf{(A) } 7 \qquad \textbf{(B) } 9 \qquad \textbf{(C) } 12 \qquad \textbf{(D) } 15 \qquad \textbf{(E) } 20$

## Solution 1 (Similar Triangles)
[asy] size(6cm); pair D=(0,0), C=(6,0), B=(6,3), A=(0,3); draw(A--B--C--D--cycle); draw(B--D); draw(A--(6,2)); draw(A--(6,1)); label("$A$", A, dir(135)); label("$B$", B, dir(45)); label("$C$", C, dir(-45)); label("$D$", D, dir(-135)); label("$Q$", extension(A,(6,1),B,D),dir(-90)); label("$P$", extension(A,(6,2),B,D), dir(90)); label("$F$", (6,1), dir(0)); label("$E$", (6,2), dir(0)); [/asy]
Use similar triangles. Our goal is to put the ratio in terms of ${BD}$ . Since $\triangle APD \sim \triangle EPB,$ $\frac{DP}{PB}=\frac{AD}{BE}=3.$ Therefore, $PB=\frac{BD}{4}$ . Similarly, $\frac{DQ}{QB}=\frac{3}{2}$ . This means that ${DQ}=\frac{3\cdot BD}{5}$ . Therefore, $r:s:t=\frac{1}{4}:\frac{2}{5}-\frac{1}{4}:\frac{3}{5}=5:3:12,$ so $r+s+t=\boxed{\textbf{(E) }20.}$

## Solution 2 (Mass points and Similar Triangles - Easy)
[asy] import geometry; size(9cm); pair D=(0,0), C=(6,0), B=(6,3), A=(0,3), G=(2,1), H=(9,0); draw(A--B--C--D--cycle); draw(B--D); draw(A--(6,2)); draw(A--(6,1)); draw(A--H); draw((6,1)--G); draw(D--H); label("$A$", A, dir(135)); label("$B$", B, dir(45)); label("$C$", C, dir(-45)); label("$D$", D, dir(-135)); pair Q = extension(A,(6,1),B,D); pair P = extension(A,(6,2),B,D); label("$Q$", Q, dir(-90)); label("$P$", P, dir(90)); label("$F$", (6,1), dir(45)); label("$E$", (6,2), dir(45)); label("$H$", H, dir(0)); label("$G$", G, dir(135)); [/asy]
This problem breaks down into finding $QP:PB$ and $DQ:QB$ . We can find the first using mass points, and the second using similar triangles.
Draw point $G$ on $DB$ such that $FG\parallel CD$ . Then, by similar triangles $FG=BF\cdot 2=4$ . Again, by similar triangles $AQB$ and $FQG$ , $AQ:FQ=AB:FG=6:4=3:2$ . Now we begin Mass Points.
We will consider the triangle $ABF$ with center $P$ , so that $E$ balances $B$ and $F$ , and $Q$ balances $A$ and $F$ . Assign a mass of $1$ to $B$ . Then, $BE:FE=1:1$ so $F=B=1$ . By mass points addition, $E=B+F=2$ since $E$ balances $B$ and $F$ . Also, $AQ:QF=3:2$ so $A=\frac{2}{3}F=\frac{2}{3}$ so $Q=\frac{5}{3}$ . Then, $QP:PB=1:\frac{5}{3}=3:5$ .
To calculate $DQ:BQ$ , extend $AF$ past $F$ to point $H$ such that $H$ lies on $BC$ . Then $AFB$ is similar to $HAD$ so $DH=3\cdot AD=9$ . Also, $AQB$ is similar to $HQD$ so $DQ:BQ=9:6=3:2$
Now, we wish to get $DQ:QP:PB$ . Observe that $BQ=QP+PB$ . So, $DQ:BQ=DQ:QP+PB=3:2$ so (since $QP:PB=3:5$ has sum $3+5=8$ ), $DQ:QP+PB=3:2=12:8$ . now, we may combine the two and get $DQ:QP:PB=12:3:5$ so $r+s+t=12+3+5=\boxed{\textbf{(E) }20}$ .
~Firebolt360(minor edits by vadava_lx)

## Solution 3(Coordinate Bash)
We can set coordinates for the points. $D=(0,0), C=(6,0), B=(6,3),$ and $A=(0,3)$ . The line $BD$ 's equation is $y = \frac{1}{2}x$ , line $AE$ 's equation is $y = -\frac{1}{6}x + 3$ , and line $AF$ 's equation is $y = -\frac{1}{3}x + 3$ . Adding the equations of lines $BD$ and $AE$ , we find that the coordinates of $P$ are $\left(\frac{9}{2},\frac{9}{4}\right)$ . Furthermore we find that the coordinates of $Q$ are $\left(\frac{18}{5}, \frac{9}{5}\right)$ . Using the Pythagorean Theorem , we get that the length of $QD$ is $\sqrt{\left(\frac{18}{5}\right)^2+\left(\frac{9}{5}\right)^2} = \sqrt{\frac{405}{25}} = \frac{\sqrt{405}}{5} = \frac{9\sqrt{5}}{5}$ , and the length of $DP$ is $\sqrt{\left(\frac{9}{2}\right)^2+\left(\frac{9}{4}\right)^2} = \sqrt{\frac{81}{4} + \frac{81}{16}} = \sqrt{\frac{405}{16}} = \frac{\sqrt{405}}{4} = \frac{9\sqrt{5}}{4}.$ $PQ = DP - DQ = \frac{9\sqrt{5}}{4} - \frac{9\sqrt{5}}{5} = \frac{9\sqrt{5}}{20}.$ The length of $DB = \sqrt{6^2 + 3^2} = \sqrt{45} = 3\sqrt{5}$ . Then $BP= 3\sqrt{5} - \frac{9\sqrt{5}}{4} = \frac{3\sqrt{5}}{4}.$ The ratio $BP : PQ : QD = \frac{3\sqrt{5}}{4} : \frac{9\sqrt{5}}{20} : \frac{9\sqrt{5}}{5} = 15\sqrt{5} : 9\sqrt{5} : 36\sqrt{5} = 15 : 9 : 36 = 5 : 3 : 12.$ Then $r, s,$ and $t$ is $5, 3,$ and $12$ , respectively. The problem tells us to find $r + s + t$ , so $5 + 3 + 12 = \boxed{\textbf{(E) }20}$ ~ minor $\LaTeX$ edits by dolphin7

## Solution 4
Extend $AF$ to meet $CD$ at point $T$ . Since $FC=1$ and $BF=2$ , $TC=3$ by similar triangles $\triangle TFC$ and $\triangle AFB$ . It follows that $\frac{BQ}{QD}=\frac{BP+PQ}{QD}=\frac{2}{3}$ . Now, using similar triangles $\triangle BEP$ and $\triangle DAP$ , $\frac{BP}{PD}=\frac{BP}{PQ+QD}=\frac{1}{3}$ . WLOG let $BP=1$ . Solving for $PQ, QD$ gives $PQ=\frac{3}{5}$ and $QD=\frac{12}{5}$ . So our desired ratio is $5:3:12$ and $5+3+12=\boxed{\textbf{(E) } 20}$ .

## Solution 5 (Mass Points)
Draw line segment $AC$ , and call the intersection between $AC$ and $BD$ point $K$ . In $\triangle ABC$ , observe that $BE:EC=1:2$ and $AK:KC=1:1$ . Using mass points, find that $BP:PK=1:1$ . Again utilizing $\triangle ABC$ , observe that $BF:FC=2:1$ and $AK:KC=1:1$ . Use mass points to find that $BQ:QK=4:1$ . Now, draw a line segment with points $B$ , $P$ , $Q$ , and $K$ ordered from left to right. Set the values $BP=x$ , $PK=x$ , $BQ=4y$ and $QK=y$ . Setting both sides segment $BK$ equal, we get $y= \frac{2}{5}x$ . Plugging in and solving gives $QK= \frac{2}{5}x$ , $PQ=\frac{3}{5}x$ , $BP=x$ . The question asks for $BP:PQ:QD$ , so we add $2x$ to $QK$ and multiply the ratio by $5$ to create integers. This creates $5(1:\frac{3}{5}:\frac{12}{5})= 5:3:12$ . This sums up to $3+5+12=\boxed{\textbf{(E) }20}$

## Solution 6 (Easy Coord Bash)
We set coordinates for the points. Let $A=(0,3), B=(6,3), C=(6,0)$ and $D=(0,0)$ . Then the equation of line $AE$ is $y = -\frac{1}{6}x + 3,$ the equation of line $AF$ is $y = -\frac{1}{3}x + 3,$ and the equation of line $BD$ is $y = \frac{1}{2}x$ . We find that the x-coordinate of point $P$ is $\frac 9 2$ by solving $-\frac{1}{6}x + 3=\frac{1}{2}x.$ Similarly we find that the x-coordinate of point $Q$ is $\frac {18} 5$ by solving $-\frac{1}{3}x + 3=\frac{1}{2}x.$ It follows that $BP:PQ:QD=6-\frac 9 2 : \frac 9 2 - \frac {18} 5 : \frac {18} 5= \frac 3 2 : \frac 9 {10} : \frac {18} 5 = 5:3:12.$ Hence $r,s,t=5,3,12$ and $r+s+t=5+3+12=\boxed{\textbf{(E) } 20}.$ ~ Solution by dolphin7

## Video Solution
https://www.youtube.com/watch?v=aG9JiBMd0ag

## Video Solution 2
https://youtu.be/us3e2jMjWnw
~IceMatrix

## Video Solution 3 by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=3406
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .