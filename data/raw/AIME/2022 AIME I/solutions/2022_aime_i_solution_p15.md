# 2022 AIME I Problem 15

## Problem

Let $x,$ $y,$ and $z$ be positive real numbers satisfying the system of equations: \begin{align*} \sqrt{2x-xy} + \sqrt{2y-xy} &= 1 \\ \sqrt{2y-yz} + \sqrt{2z-yz} &= \sqrt2 \\ \sqrt{2z-zx} + \sqrt{2x-zx} &= \sqrt3. \end{align*} Then $\left[ (1-x)(1-y)(1-z) \right]^2$ can be written as $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1 (geometric interpretation)
First, let define a triangle with side lengths $\sqrt{2x}$ , $\sqrt{2z}$ , and $l$ , with altitude from $l$ 's equal to $\sqrt{xz}$ . $l = \sqrt{2x - xz} + \sqrt{2z - xz}$ , the left side of one equation in the problem.
Let $\theta$ be angle opposite the side with length $\sqrt{2x}$ . Then the altitude has length $\sqrt{2z} \cdot \sin(\theta) = \sqrt{xz}$ and thus $\sin(\theta) = \sqrt{\frac{x}{2}}$ , so $x=2\sin^2(\theta)$ and the side length $\sqrt{2x}$ is equal to $2\sin(\theta)$ .
We can symmetrically apply this to the two other equations/triangles.
By law of sines, we have $\frac{2\sin(\theta)}{\sin(\theta)} = 2R$ , with $R=1$ as the circumradius, same for all 3 triangles. The circumcircle's central angle to a side is $2 \arcsin(l/2)$ , so the 3 triangles' $l=1, \sqrt{2}, \sqrt{3}$ , have angles $120^{\circ}, 90^{\circ}, 60^{\circ}$ , respectively.
This means that by half angle arcs, we see that we have in some order, $x=2\sin^2(\alpha)$ , $y=2\sin^2(\beta)$ , and $z=2\sin^2(\gamma)$ (not necessarily this order, but here it does not matter due to symmetry), satisfying that $\alpha+\beta=180^{\circ}-\frac{120^{\circ}}{2}$ , $\beta+\gamma=180^{\circ}-\frac{90^{\circ}}{2}$ , and $\gamma+\alpha=180^{\circ}-\frac{60^{\circ}}{2}$ . Solving, we get $\alpha=\frac{135^{\circ}}{2}$ , $\beta=\frac{105^{\circ}}{2}$ , and $\gamma=\frac{165^{\circ}}{2}$ .
We notice that \[[(1-x)(1-y)(1-z)]^2=[\sin(2\alpha)\sin(2\beta)\sin(2\gamma)]^2=[\sin(135^{\circ})\sin(105^{\circ})\sin(165^{\circ})]^2\] \[=\left(\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{6}-\sqrt{2}}{4} \cdot \frac{\sqrt{6}+\sqrt{2}}{4}\right)^2 = \left(\frac{\sqrt{2}}{8}\right)^2=\frac{1}{32} \to \boxed{033}. \blacksquare\]
- kevinmathz

## Solution 2 (Condensed Algebraic Trig)
Let $\sin{A} = \sqrt{\frac{x}{2}}$ , $\sin{B} = \sqrt{\frac{y}{2}}$ , and $\sin{C} = \sqrt{\frac{z}{2}}$ for some $A,B,C \in (0^\circ,90^\circ)$ ; therefore, $\cos{A} = \sqrt{\frac{2-x}{2}}$ , etc. Dividing all three given equations by $2$ , we see that they are equivalent to \begin{align*} \sin(A+B) &= \sin(30^\circ) \\ \sin(B+C) &= \sin(45^\circ) \\ \sin(C+A) &= \sin(60^\circ), \end{align*} which produces $A=\frac{45}{2}^\circ$ , $B=\frac{15}{2}^\circ$ , and $C=\frac{75}{2}^\circ$ . Thus our answer is \begin{align*} [(1-x)(1-y)(1-z)]^2 &= [(1-2\sin^2 A)(1-2\sin^2 B)(1-2\sin^2 C)]^2 \\ &= (\cos(2A)\cos(2B)\cos(2C))^2 \\ &= \left(\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{6}+\sqrt{2}}{2} \cdot \frac{\sqrt{6}-\sqrt{2}}{2}\right)^2 \\ &= \frac{1}{32}, \end{align*} producing the answer of $\boxed{033}$ .
Remark. Note that liberties have been taken in mathematical rigor in the above solution, especially when dealing with angles $A,B,C$ and the inverse sine function. However, these details do not affect the overall solution and may be carefully checked during the contest if desired; thus we feel justified in leaving them out to emphasize the elegance of the trigonometric substitution.
~Oxymoronic15 (edited for length by Viliciri)

## Solution 3 (substitution)
Let $1-x=a;1-y=b;1-z=c$ , rewrite those equations
$\sqrt{(1-a)(1+b)}+\sqrt{(1+a)(1-b)}=1$ ;
$\sqrt{(1-b)(1+c)}+\sqrt{(1+b)(1-c)}=\sqrt{2}$
$\sqrt{(1-a)(1+c)}+\sqrt{(1-c)(1+a)}=\sqrt{3}$
and solve for $m/n = (abc)^2 = a^2b^2c^2$
Square both sides and simplify, to get three equations:
$2ab-1=2\sqrt{(1-a^2)(1-b^2)}$
$2bc~ ~ ~ ~ ~ ~=2\sqrt{(1-b^2)(1-c^2)}$
$2ac+1=2\sqrt{(1-c^2)(1-a^2)}$
Square both sides again, and simplify to get three equations:
$a^2+b^2-ab=\frac{3}{4}$
$b^2+c^2~ ~ ~ ~ ~ ~=1$
$a^2+c^2+ac=\frac{3}{4}$
Subtract first and third equation, getting $(b+c)(b-c)=a(b+c)$ , $a=b-c$
Put it in first equation, getting $b^2-2bc+c^2+b^2-b(b-c)=b^2+c^2-bc=\frac{3}{4}$ , $bc=\frac{1}{4}$
Since $a^2=b^2+c^2-2bc=\frac{1}{2}$ , $m/n = a^2b^2c^2 = a^2(bc)^2 = \frac{1}{2}\left(\frac{1}{4}\right)^2=\frac{1}{32}$ and so the final answer is $\boxed{033}$
~bluesoul

## Solution 4
Denote $u = 1 - x$ , $v = 1 - y$ , $w = 1 - z$ . Hence, the system of equations given in the problem can be written as \begin{align*} \sqrt{(1-u)(1+v)} + \sqrt{(1+u)(1-v)} & = 1 \hspace{1cm} (1) \\ \sqrt{(1-v)(1+w)} + \sqrt{(1+v)(1-w)} & = \sqrt{2} \hspace{1cm} (2) \\ \sqrt{(1-w)(1+u)} + \sqrt{(1+w)(1-u)} & = \sqrt{3} . \hspace{1cm} (3) \end{align*}
Each equation above takes the following form: \[ \sqrt{(1-a)(1+b)} + \sqrt{(1+a)(1-b)} = k . \]
Now, we simplify this equation by removing radicals.
Denote $p = \sqrt{(1-a)(1+b)}$ and $q = \sqrt{(1+a)(1-b)}$ .
Hence, the equation above implies \[ \left\{ \begin{array}{l} p + q = k \\ p^2 = (1-a)(1+b) \\ q^2 = (1+a)(1-b) \end{array} \right.. \]
Hence, $q^2 - p^2 = (1+a)(1-b) - (1-a)(1+b) = 2 (a-b)$ . Hence, $q - p = \frac{q^2 - p^2}{p+q} = \frac{2}{k} (a-b)$ .
Because $p + q = k$ and $q - p = \frac{2}{k} (a-b)$ , we get $q = \frac{a-b}{k} + \frac{k}{2}$ . Plugging this into the equation $q^2 = (1+a)(1-b)$ and simplifying it, we get \[ a^2 + \left( k^2 - 2 \right) ab + b^2 = k^2 - \frac{k^4}{4} . \]
Therefore, the system of equations above can be simplified as \begin{align*} u^2 - uv + v^2 & = \frac{3}{4} \\ v^2 + w^2 & = 1 \\ w^2 + wu + u^2 & = \frac{3}{4} . \end{align*}
Denote $w' = - w$ . The system of equations above can be equivalently written as \begin{align*} u^2 - uv + v^2 & = \frac{3}{4} \hspace{1cm} (1') \\ v^2 + w'^2 & = 1 \hspace{1cm} (2') \\ w'^2 - w'u + u^2 & = \frac{3}{4} \hspace{1cm} (3') . \end{align*}
Taking $(1') - (3')$ , we get \[ (v - w') (v + w' - u) = 0 . \]
Thus, we have either $v - w' = 0$ or $v + w' - u = 0$ .
$\textbf{Case 1}$ : $v - w' = 0$ .
Equation (2') implies $v = w' = \pm \frac{1}{\sqrt{2}}$ .
Plugging $v$ and $w'$ into Equation (2), we get contradiction. Therefore, this case is infeasible.
$\textbf{Case 2}$ : $v + w' - u = 0$ .
Plugging this condition into (1') to substitute $u$ , we get \[ v^2 + v w' + w'^2 = \frac{3}{4} \hspace{1cm} (4) . \]
Taking $(4) - (2')$ , we get \[ v w' = - \frac{1}{4} . \hspace{1cm} (5) . \]
Taking (4) + (5), we get \[ \left( v + w' \right)^2 = \frac{1}{2} . \]
Hence, $u^2 = \left( v + w' \right)^2 = \frac{1}{2}$ .
Therefore, \begin{align*} \left[ (1-x)(1-y)(1-z) \right]^2 & = u^2 (vw)^2 \\ & = u^2 (vw')^2 \\ & = \frac{1}{2} \left( - \frac{1}{4} \right)^2 \\ & = \frac{1}{32} . \end{align*}
Therefore, the answer is $1 + 32 = \boxed{\textbf{(033) }}$ .
~Steven Chen (www.professorchenedu.com)
bu-bye \begin{align*} \sin(\alpha + \beta) &= 1/2 \\ \sin(\alpha + \gamma) &= \sqrt2/2 \\ \sin(\beta + \gamma) &= \sqrt3/2. \end{align*} Thus, \begin{align*} \alpha + \beta &= 30^{\circ} \\ \alpha + \gamma &= 45^{\circ} \\ \beta + \gamma &= 60^{\circ}, \end{align*} so $(\alpha, \beta, \gamma) = (15/2^{\circ}, 45/2^{\circ}, 75/2^{\circ})$ . Hence,
\[abc = (1-2\sin^2(\alpha))(1-2\sin^2(\beta))(1-2\sin^2(\gamma))=\cos(15^{\circ})\cos(45^{\circ})\cos(75^{\circ})=\frac{\sqrt{2}}{8},\] so $(abc)^2=(\sqrt{2}/8)^2=\frac{1}{32}$ , for a final answer of $\boxed{033}$ .
Remark
The motivation for the trig substitution is that if $\sin^2(\alpha)=(1-a)/2$ , then $\cos^2(\alpha)=(1+a)/2$ , and when making the substitution in each equation of the initial set of equations, we obtain a new equation in the form of the sine addition formula.
~ Leo.Euler

## Solution 6 (Geometric)
In given equations, $0 \leq x,y,z \leq 2,$ so we define some points: \[\bar {O} = (0, 0), \bar {A} = (1, 0), \bar{M} = \left(\frac {1}{\sqrt{2}},\frac {1}{\sqrt{2}}\right),\] \[\bar {X} = \left(\sqrt {\frac {x}{2}}, \sqrt{1 – \frac{x}{2}}\right), \bar {Y'} = \left(\sqrt {\frac {y}{2}}, \sqrt{1 – \frac{y}{2}}\right),\] \[\bar {Y} = \left(\sqrt {1 – \frac{y}{2}},\sqrt{\frac {y}{2}}\right), \bar {Z} = \left(\sqrt {1 – \frac{z}{2}},\sqrt{\frac {z}{2}}\right).\] Notice, that \[\mid \vec {AO} \mid = \mid \vec {MO} \mid = \mid \vec {XO} \mid =\mid \vec {YO} \mid = \mid \vec {Y'O} \mid =\mid \vec {ZO} \mid = 1\] and each points lies in the first quadrant.
We use given equations and get some scalar products: \[(\vec {XO} \cdot \vec {YO}) = \frac {1}{2} = \cos \angle XOY \implies \angle XOY = 60 ^\circ,\] \[(\vec {XO} \cdot \vec {ZO}) = \frac {\sqrt{3}}{2} = \cos \angle XOZ \implies \angle XOZ = 30^\circ,\] \[(\vec {Y'O} \cdot \vec {ZO}) = \frac {1}{\sqrt{2}} = \cos \angle Y'OZ \implies \angle Y'OZ = 45^\circ.\] So $\angle YOZ = \angle XOY – \angle XOZ = 60 ^\circ – 30 ^\circ = 30 ^\circ, \angle Y'OY = \angle Y'OZ + \angle YOZ = 45^\circ + 30 ^\circ = 75^\circ.$
Points $Y$ and $Y'$ are symmetric with respect to $OM.$
Case 1 \[\angle YOA = \frac{90^\circ – 75^\circ}{2} = 7.5^\circ, \angle ZOA = 30^\circ + 7.5^\circ = 37.5^\circ, \angle XOA = 60^\circ + 7.5^\circ = 67.5^\circ .\] \[1 – x = \left(\sqrt{1 – \frac{x}{2}} \right)^2– \left(\sqrt{\frac {x}{2}}\right)^2 = \sin^2 \angle XOA – \cos^2 \angle XOA = –\cos 2 \angle XOA = –\cos 135^\circ,\] \[1 – y = \cos 15^\circ, 1 – z = \cos 75^\circ \implies \left[ (1–x)(1–y)(1–z) \right]^2 = \left[ \sin 45^\circ \cdot \cos 15^\circ \cdot \sin 15^\circ \right]^2 =\] \[=\left[ \frac {\sin 45^\circ \cdot \sin 30^\circ}{2} \right]^2 = \frac {1}{32} \implies \boxed{\textbf{033}}.\] Case 2
\[\angle Y_1 OA = \frac{90^\circ + 75^\circ}{2} = 82.5^\circ, \angle Z_1 OA = 82.5^\circ – 30^\circ = 52.5^\circ, \angle X_1 OA = 82.5^\circ – 60^\circ = 22.5^\circ \implies \boxed{\textbf{033}}.\]
vladimir.shelomovskii@gmail.com, vvsss

## Video Solution
https://youtu.be/i6kDMbav2sk
~Math Gold Medalist

## Video Solution
https://youtu.be/aa_VY4e4OOM?si=1lHSwY3v7RICoEpk
~MathProblemSolvingSkills.com

## Video Solution
https://www.youtube.com/watch?v=ihKUZ5itcdA
~Steven Chen (www.professorchenedu.com)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .