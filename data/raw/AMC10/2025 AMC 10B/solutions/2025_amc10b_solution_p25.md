# 2025 AMC 10B Problem 25

## Problem

Square $ABCD$ has sides of length $4$ . Points $P$ and $Q$ lie on $\overline{AD}$ and $\overline{CD}$ , respectively, with $AP=\frac{8}{5}$ and $DQ=\frac{10}{3}$ . A path begins along the segment from $P$ to $Q$ and continues by reflecting against the sides of $ABCD$ (with congruent incoming and outgoing angles). If the path hits a vertex of the square, it terminates there; otherwise it continues forever. At which vertex does the path terminate?

[asy] size(8cm); defaultpen(linewidth(0.9)); dotfactor = 3; pair A=(0,0), B=(4,0), C=(4,4), D=(0,4); pair P=(0, 8/5); pair Q=(10/3, 4); draw(A--B--C--D--cycle); draw(P--Q, red+linewidth(1.2)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,NE); label("$D$",D,NW); label("$P$",P,W); label("$Q$",Q,N); draw(arc(Q,0.3,0, -35.78)); draw(arc(Q,0.3,180,180+35.78)); pair arrow_dir = Q + 0.75*dir(-35.78); draw(Q--arrow_dir, red+linewidth(1.2), EndArrow(size=10, FillDraw(red))); dot(A); dot(B); dot(C); dot(D); dot(P); dot(Q); [/asy]

$\textbf{(A) } A \qquad \textbf{(B) } B \qquad \textbf{(C) } C \qquad \textbf{(D) } D \qquad \textbf{(E) } \text{The path continues forever.}$

## Solution 1 (Cheese, draw the path)
For this question, I cheesed it by just drawing the path with a ruler and an compass, and you can find that the path eventually terminates at vertex B by doing so. Therefore, the answer is $\boxed{\mathbf{(B)\,\mathnormal{B}}}$ .
~EZ123
Note - Protractors are not allowed on the AMC Exam, but you can sort of achieve the same thing with a compass
~🧀
~🧀
~🧀
~🧀
~🧀 ITS RAINING TACOS
Remark: I actually did this on the test, and I didn't even sketch out the diagram either. I had like a minute left on the clock, and I traced the path of the line lightly on my screen (I was taking digital version) and somehow got it correctly lol. I didn't even use a compass or anything either 🤣
(lol, so did ~Sakura_kitty)

## Solution 2 (Trivial Algebra)
First, let me introduce the reflection trick. Basically, instead of bending the line segment a bunch of times, map any path of the line segment into a reflected square, reflecting the square about the segment that the ray touches. Every time this happens, we map the latest square onto a new one. After we do this many times, the entire path becomes a straight line:
Illustration link, hosted on imgbb (I'm too tired to use Asymptote)
So now, we could just imagine the whole reflection path as a huge straight ray in the coordinate plane. When it lands upon a $x$ and $y$ both divisible by $4$ , since a corner reflected is still a corner, we can then trace the corner back.
Note that by some trivial arithmetic you get that $PD=4-\frac{8}{5}=\frac{12}{5}$ , and if we let $A$ be the origin of a coordinate plane, $AD$ be the $y$ -axis and $AB$ be the $x$ -axis, the slope of $PQ$ is $\frac{12}{5}\div\frac{10}{3}$ using rise over run, which is $\frac{18}{25}$ . Trivially, the $y$ -intercept of $PQ$ is $\frac{8}{5}$ , so the equation of $PQ$ becomes \[y=\frac{18}{25}x+\frac{8}{5}\] and you want both $x$ and $y$ to be divisible by $4$ . Right off the bat, note that the denominator in the linear term is $25$ , so to have any chance of $y$ being an integer AT ALL, $x$ must be divisible by $5$ (else the resulting fraction will have something over $25$ plus something over $5$ , so there's extra $1/25$ s.)
Therefore, $x$ must be a multiple of $20$ . Then let's try $x=20$ ! We get $y=16$ , which is divisible by $4$ ! Yay!!! You might start to sweat about the exact path and how to trace the vertices now, but that does not matter: we can see that if we first reflect to the right and then up, it's no difference than if we went up and then right. So it doesn't matter if we do all the horizontal or vertical reflections all together.
Illustration link, hosted on imgbb (I'm too tired to use Asymptote)
Now you can just label a random square $ABCD$ , and reflect to the right $4$ times (since you already have 1 square) and then up $3$ times. You'll then notice that $(20,16)$ is just a copy of $\boxed{\mathbf{(B)\,\mathnormal{B}}}$ .
~johnzhou721

## Solution 3
[asy] unitsize(20); pair _A, _B, _C, _D, _P, _Q; _A = (0, 0); _B = (0, 4); _C = (4, 4); _D = (4, 0); _P = (0, 8/5); _Q = (4, 10/3); draw(_A -- _B -- _C -- _D -- _A ^^ _P -- _Q); draw(extension(_P, _Q, _B, _C) -- _Q -- 2*_C - extension(_P, _Q, _B, _C), dashed); label("$A$", _A, SW); label("$B$", _B, NW); label("$C$", _C, NE); label("$D$", _D, SE); label("$P$", _P, W); label("$Q$", _Q, SE); [/asy]
The square can be placed with $A=(0,0),B=(4,0),C=(4,4),D=(0,4)$ . Then \[P=(0,\frac{8}{5}),Q=(\frac{10}{3},4).\]
Straight line reflection is equivalent to passing through. The straight line from $P$ to $Q$ is \[y = \frac{18}{25}x + \frac{8}{5}\] \[25y = 18x + 40 \equiv 4 \pmod{18}\]
Notice that $25 \times 2 \equiv 7 \times 2 \equiv -4 \pmod{18}$ , so $25 \times (-2) \equiv 4 \pmod{18}$ , $y \equiv -2 \equiv 16 \pmod{18}$ , then $x = 20$ , the line passed through $(20, 16)$ .
From $(0, \frac{8}{5})$ to $(20, 16)$ , $x$ coordinate increases 20 whole units, $y$ coordinate increases 15 whole units. Excluding the case where $PQ$ passes through a lattice point at the final grid point, the segment $PQ$ crosses integer grid lines a total of $(20 - 1) + (15 - 1) = 33$ times. Each time the line crosses an integer grid line, it corresponds to one reflection; every four reflections, the path completes a full rotation within the square. $33 \equiv 1 \pmod{4}$ , after one reflection off side $CD$ , the line $PQ$ will pass through point $\boxed{\textbf{(B) }B}$ .
~ reda_mandymath

## Upgraded Solution 1
Use the scratch paper's corner and fold it to necessary to mold and replicate angles, then use a straightedge to trace it.

## Video Solution 1 by OmegaLearn.org
https://youtu.be/honKBgPkly4

## Video Solution 2 (Fast and Easy)
https://www.youtube.com/watch?v=v8eH8myCSxo
~ Pi Academy

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=-ZOTMCwLXGE
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .