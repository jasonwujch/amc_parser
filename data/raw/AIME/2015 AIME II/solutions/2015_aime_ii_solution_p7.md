# 2015 AIME II Problem 7

## Problem

Triangle $ABC$ has side lengths $AB = 12$ , $BC = 25$ , and $CA = 17$ . Rectangle $PQRS$ has vertex $P$ on $\overline{AB}$ , vertex $Q$ on $\overline{AC}$ , and vertices $R$ and $S$ on $\overline{BC}$ . In terms of the side length $PQ = \omega$ , the area of $PQRS$ can be expressed as the quadratic polynomial \[Area(PQRS) = \alpha \omega - \beta \omega^2.\]

Then the coefficient $\beta = \frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
If $\omega = 25$ , the area of rectangle $PQRS$ is $0$ , so
\[\alpha\omega - \beta\omega^2 = 25\alpha - 625\beta = 0\]
and $\alpha = 25\beta$ . If $\omega = \frac{25}{2}$ , we can reflect $APQ$ over $PQ$ , $PBS$ over $PS$ , and $QCR$ over $QR$ to completely cover rectangle $PQRS$ , so the area of $PQRS$ is half the area of the triangle. Using Heron's formula, since $s = \frac{12 + 17 + 25}{2} = 27$ ,
\[[ABC] = \sqrt{27 \cdot 15 \cdot 10 \cdot 2} = 90\]
so
\[45 = \alpha\omega - \beta\omega^2 = \frac{625}{2} \beta - \beta\frac{625}{4} = \beta\frac{625}{4}\]
and
\[\beta = \frac{180}{625} = \frac{36}{125}\]
so the answer is $m + n = 36 + 125 = \boxed{161}$ .

## Solution 2
[asy] unitsize(20); pair A,B,C,E,F,P,Q,R,S; A=(48/5,36/5); B=(0,0); C=(25,0); E=(48/5,0); F=(48/5,18/5); P=(24/5,18/5); Q=(173/10,18/5); S=(24/5,0); R=(173/10,0); draw(A--B--C--cycle); draw(P--Q); draw(Q--R); draw(R--S); draw(S--P); draw(A--E,dashed); label("$A$",A,N); label("$B$",B,SW); label("$C$",C,SE); label("$E$",E,SE); label("$F$",F,NE); label("$P$",P,NW); label("$Q$",Q,NE); label("$R$",R,SE); label("$S$",S,SW); draw(rightanglemark(B,E,A,12)); dot(E); dot(F); [/asy]
Similar triangles can also solve the problem.
First, solve for the area of the triangle. $[ABC] = 90$ . This can be done by Heron's Formula or placing an $8-15-17$ right triangle on $AC$ and solving. (The $8$ side would be collinear with line $AB$ )
After finding the area, solve for the altitude to $BC$ . Let $E$ be the intersection of the altitude from $A$ and side $BC$ . Then $AE = \frac{36}{5}$ . Solving for $BE$ using the Pythagorean Formula, we get $BE = \frac{48}{5}$ . We then know that $CE = \frac{77}{5}$ .
Now consider the rectangle $PQRS$ . Since $SR$ is collinear with $BC$ and parallel to $PQ$ , $PQ$ is parallel to $BC$ meaning $\Delta APQ$ is similar to $\Delta ABC$ .
Let $F$ be the intersection between $AE$ and $PQ$ . By the similar triangles, we know that $\frac{PF}{FQ}=\frac{BE}{EC} = \frac{48}{77}$ . Since $PF+FQ=PQ=\omega$ . We can solve for $PF$ and $FQ$ in terms of $\omega$ . We get that $PF=\frac{48}{125} \omega$ and $FQ=\frac{77}{125} \omega$ .
Let's work with $PF$ . We know that $PQ$ is parallel to $BC$ so $\Delta APF$ is similar to $\Delta ABE$ . We can set up the proportion:
$\frac{AF}{PF}=\frac{AE}{BE}=\frac{3}{4}$ . Solving for $AF$ , $AF = \frac{3}{4} PF = \frac{3}{4} \cdot \frac{48}{125} \omega = \frac{36}{125} \omega$ .
We can solve for $PS$ then since we know that $PS=FE$ and $FE= AE - AF = \frac{36}{5} - \frac{36}{125} \omega$ .
Therefore, $[PQRS] = PQ \cdot PS = \omega (\frac{36}{5} - \frac{36}{125} \omega) = \frac{36}{5}\omega - \frac{36}{125} \omega^2$ .
This means that $\beta = \frac{36}{125} \Rightarrow (m,n) = (36,125) \Rightarrow m+n = \boxed{161}$ .

## Solution 3
Heron's Formula gives $[ABC] = \sqrt{27 \cdot 15 \cdot 10 \cdot 2} = 90,$ so the altitude from $A$ to $BC$ has length $\dfrac{2[ABC]}{BC} = \dfrac{36}{5}.$
Now, draw a parallel to $AB$ from $Q$ , intersecting $BC$ at $T$ . Then $BT = w$ in parallelogram $QPBT$ , and so $CT = 25 - w$ . Clearly, $CQT$ and $CAB$ are similar triangles, and so their altitudes have lengths proportional to their corresponding base sides, and so \[\frac{QR}{\frac{36}{5}} = \frac{25 - w}{25}.\] Solving gives $[PQRS] = \dfrac{36}{5} \cdot \dfrac{25 - w}{25} \cdot w = \dfrac{36w}{5} - \dfrac{36w^2}{125}$ , so the answer is $36 + 125 = 161$ .

## Solution 4
Using the diagram from Solution 2 above, label $AF$ to be $h$ . Through Heron's formula, the area of $\triangle ABC$ turns out to be $90$ , so using $AE$ as the height and $BC$ as the base yields $AE=\frac{36}{5}$ . Now, through the use of similarity between $\triangle APQ$ and $\triangle ABC$ , you find $\frac{w}{25}=\frac{h}{36/5}$ . Thus, $h=\frac{36w}{125}$ . To find the height of the rectangle, subtract $h$ from $\frac{36}{5}$ to get $\left(\frac{36}{5}-\frac{36w}{125}\right)$ , and multiply this by the other given side $w$ to get $\frac{36w}{5}-\frac{36w^2}{125}$ for the area of the rectangle. Finally, $36+125=\boxed{161}$ .

## Solution 5
Using the diagram as shown in Solution 2, let $AE=h$ and $AP=L$ Now, by Heron's formula, we find that the $[ABC]=90$ . Hence, $h=\frac{36}{5}$
Now, we see that $\sin{B}=\frac{PS}{12-L}\implies PS=\sin{B}(12-L)$ We easily find that $\sin{B}=\frac{3}{5}$
Hence, $PS=\frac{3}{5}(12-L)$
Now, we see that $[PQRS]=\frac{3}{5}(12-L)(w)$
Now, it is obvious that we want to find $L$ in terms of $W$ .
Looking at the diagram, we see that because $PQRS$ is a rectangle, $\triangle{APQ}\sim{\triangle{ABC}}$
Hence.. we can now set up similar triangles.
We have that $\frac{AP}{AB}=\frac{PQ}{BC}\implies \frac{L}{12}=\frac{W}{25}\implies 25L=12W\implies L=\frac{12W}{25}$ .
Plugging back in..
$[PQRS]=\frac{3w}{5}(12-(\frac{12W}{25}))\implies \frac{3w}{5}(\frac{300-12W}{25})\implies \frac{900W-36W^2}{125}$
Simplifying, we get $\frac{36W}{5}-\frac{36W^2}{125}$
Hence, $125+36=\boxed{161}$

## Solution 6
Proceed as in solution 1. When $\omega$ is equal to zero, $\alpha - \beta\omega=\alpha$ is equal to the altitude. This means that $25\beta$ is equal to $\frac{36}{5}$ , so $\beta = \frac{36}{125}$ , yielding $\boxed{161}$ .

## Solution 7(Quick and Easy)
Using the diagram in Solution 2, the area of $PQRS$ is ( $w$ )( $PR$ ), we only need to find $PR$ . Because $ABC$ and $APQ$ are similar in a ratio of 25:w. Because of $AB$ : $AC$ =12:15 and $AP$ : $AB$ = $w$ :25, we can derive that $BP$ =frac{(25-w)(12)}{25}. By using LoC on $ABC$ , it is obvious that Cos(B)=\frac{4}{5} and Sin( $B$ )=\frac{3}{5}. $PR$ =\frac{3bp}{5}=\frac{(25-w)(36)}{125}. Multiply $w$ , we get $\frac{36W}{5}-\frac{36W^2}{125}$ which means the answer is\boxed{161}$

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=554s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .