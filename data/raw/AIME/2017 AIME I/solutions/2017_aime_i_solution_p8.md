# 2017 AIME I Problem 8

## Problem

Two real numbers $a$ and $b$ are chosen independently and uniformly at random from the interval $(0, 75)$ . Let $O$ and $P$ be two points on the plane with $OP = 200$ . Let $Q$ and $R$ be on the same side of line $OP$ such that the degree measures of $\angle POQ$ and $\angle POR$ are $a$ and $b$ respectively, and $\angle OQP$ and $\angle ORP$ are both right angles. The probability that $QR \leq 100$ is equal to $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Noting that $\angle OQP$ and $\angle ORP$ are right angles, we realize that we can draw a semicircle with diameter $\overline{OP}$ and points $Q$ and $R$ on the semicircle. Since the radius of the semicircle is $100$ , if $\overline{QR} \leq 100$ , then $\overarc{QR}$ must be less than or equal to $60^{\circ}$ .
This simplifies the problem greatly. Since the degree measure of an angle on a circle is simply half the degree measure of its subtended arc, the problem is simply asking:
Given $a, b$ such that $0<a, b<75$ , what is the probability that $|a-b| \leq 30$ ? Through simple geometric probability, we get that $P = \frac{16}{25}$ .
The answer is $16+25=\boxed{041}$
~IYN~ Note: The Geometric probability can be easily be found through graphing on the x-y plane.

## Solution 2 (Trig Bash)
Put $\triangle POQ$ and $\triangle POR$ with $O$ on the origin and the triangles on the $1^{st}$ quadrant. The coordinates of $Q$ and $P$ is $(200 \cos^{2}a,200 \cos a\sin a )$ , $(200\cos^{2}b,200\cos(b)\sin b)$ . So $PQ^{2}$ = $(200 \cos^{2} a - 200 \cos^{2} b)^{2} +(200 \cos a \sin a - 200 \cos b \sin b)^{2}$ , which we want to be less then $100^{2}$ . So $(200 \cos^{2} a - 200 \cos^{2} b)^{2} +(200 \cos a \sin a - 200 \cos b \sin b)^{2} \le 100^{2}$ \[(\cos^{2} a - \cos^{2} b)^{2} +(\cos a \sin a - \cos b \sin b)^{2} \le \frac{1}{4}\] \[\cos^{4} a + \cos^{4} b - 2\cos^{2} a \cos^{2} b +\cos^{2}a \sin^{2} a + \cos^{2} b \sin^{2} b - 2 \cos a \sin a \cos b \sin b \le \frac{1}{4}\] \[\cos^{2} a(\cos^{2} a + \sin^{2} a)+\cos^{2} b(\cos^{2} b+\sin^{2} b) - 2\cos^{2} a \cos^{2} b- 2 \cos a \sin a \cos b \sin b \le \frac{1}{4}\] \[\cos^{2} a(1-\cos^{2} b)+\cos^{2} b(1-\cos^{2} a) - 2 \cos a \sin a \cos b \sin b \le \frac{1}{4}\] \[(\cos a\sin b)^{2} +(\cos b\sin a)^{2} - 2 (\cos a \sin b)(\cos b \sin a)\le \frac{1}{4}\] \[(\cos a\sin b-\cos b\sin a)^{2}\le \frac{1}{4}\] \[\sin^{2} (b-a) \le \frac{1}{4}\] So we want $-\frac{1}{2} \le \sin (b-a) \le \frac{1}{2}$ , which is equivalent to $-30 \le b-a \le 30$ or $150 \le b-a \le 210$ . The second inequality is impossible so we only consider what the first inequality does to our $75$ by $75$ box in the $ab$ plane. This cuts off two isosceles right triangles from opposite corners with side lengths $45$ from the $75$ by $75$ box. Hence the probability is $1-\frac{45^2}{75^2} = 1- \frac{9}{25}=\frac{16}{25}$ and the answer is $16+25 = \boxed{41}$
Solution by Leesisi

## Solution 3 (Quicker Trig)
[asy] pair O, P, Q, R; draw(circle(O, 10)); O = (10, 0); P = (-10, 0); Q = (10*cos(pi/3), 10*sin(pi/3)); R = (10*cos(5*pi/6), 10*sin(5*pi/6)); dot(Q); dot(O); dot(P); dot(R); draw(P--O--Q--P--R--O); draw(Q--R, red); label("$O$", O, 2*E); label("$P$", P, 2*W); label("$Q$", Q, NE); label("$R$", R, NW); label("$200$", (0,0), 2*S); label("$x$", (Q+R)/2, N); draw(rightanglemark(O, Q, P, 38)); draw(rightanglemark(O, R, P, 38)); [/asy] Let $QR=x.$ Since we are given many angles in the problem, we can compute the lengths of some of the lines in terms of trigonometric functions: $OQ = 200 \cos a, PQ = 200 \sin a, PR = 200 \sin b, OR = 200 \cos b.$ Now observe that quadrilateral $OQRP$ is a cyclic quadrilateral . Thus, we are able to apply Ptolemy's Theorem to it: \[200 x + (200 \cos a) (200 \sin b) = (200 \sin a) (200 \cos b),\] \[x + 200 (\cos a \sin b) = 200 (\sin a \cos b),\] \[x = 200(\sin a \cos b - \sin b \cos a),\] \[x = 200 \sin(a-b).\] We want $|x| \le 100$ (the absolute value comes from the fact that $a$ is not necessarily greater than $b,$ so we cannot assume that $Q$ is to the right of $R$ as in the diagram), so we substitute: \[|200 \sin(a-b)| \le 100,\] \[|\sin(a-b)| \le \frac{1}{2},\] \[|a-b| \le 30 ^\circ,\] \[-30 \le a-b \le 30.\] By simple geometric probability (see Solution 2 for complete explanation), $\frac{m}{n} = 1 - \frac{2025}{5625} = 1 - \frac{9}{25} = \frac{16}{25},$ so $m+n = \boxed{041}.$
~burunduchok

## Solution 4
Scale the circle down from radius 100 (diameter 200) to radius 6 (diameter 12). Then we want the probability that $PQ \le 6$ . Now note that all possible $P$ and $Q$ lie on a $5\pi$ interval on the circumference of the circle. But for $PQ<6$ , $P$ and $Q$ must be less than $2\pi$ apart on the circumference of the circle. Simple geometric probability gives us $\frac{16}{25}$ , so the answer is $\fbox{41}$ . (Professor-Mom)

## Solution 5
Impose a coordinate system as follows:
Let the midpoint of $\overline{OP}$ be the origin, and let $\overline{OP}$ be the x-axis. We construct a circle with center at the origin with radius 100. Since $\angle OQP$ and $\angle ORP$ are both right angles, points $Q$ and $R$ are on our circle. Place $Q$ and $R$ in the first quadrant of the Cartesian Plane. Suppose we construct $Q'$ and $R'$ such that they are clockwise rotations of $Q$ and $R$ , respectively by an angle of $2b$ degrees. Thus, we see that $\overline{QR}=100\sqrt{2}\sqrt{\cos(2|a-b|)}$ . We want this quantity to be less than $100$ . This happens when $\cos(2|a-b|) \ge 1/2,$ or when $|a-b|\le 30^{\circ}$ . The probability that the last inequality is satisfied is $16/25$ . Therefore, the probability that $QR$ is less than $100$ is $16/25$ . Hence, $m+n=\boxed{41}$
~MathIsFun286
slightly edited
~Txu

## Solution 6
WLOG, let $b\ge a$ . It does not actually matter, but it is necessary for this particular setup. It should be apparent that $\Delta RAQ\sim\Delta OAP$ . We write the equation
\[\dfrac{RA}{AO}=\dfrac{RQ}{OP}.\]
If we examine right triangle $\Delta ROA$ , we can see that $\sin(b-a)=\dfrac{RA}{AO}$ . Also, we are given $OP=200$ , so now we have
\[\sin(b-a)=\dfrac{QR}{200}.\]
We want $QR$ to be less than or equal to $100$ ; this is equivalent to $\dfrac{QR}{200}\le\dfrac12.$ We solve from there:
\begin{align*} \dfrac{QR}{200}&\le\dfrac12 \\ \sin(b-a)&\le\dfrac12 \\ \arcsin(\sin(b-a))&\le\arcsin\left(\dfrac12\right) \\ b-a&\le30^\circ. \\ \end{align*}
(Notice that if $a>b$ , then this would become $a-b\le30^\circ.$ As in Solution 1, we can write $|a-b|\le30$ .) One can now proceed as in Solution 1, but let us tackle the geometric probability for completeness.
We now have transformed this problem into another problem asking for the probability of two uniformly, randomly, and independently chosen real numbers between $0$ and $75$ being no more than $30$ from each other.
If the first number (let this be $x$ ) is between $30$ and $45$ , then the other number can be from $x-30$ to $x+30$ - a range of $60$ . Thus, the probability that this contributes is $\dfrac{45-30}{75}\cdot\dfrac{60}{75}=\dfrac4{25}$ .
If $x$ is between $0$ and $30$ or $45$ to $75$ (these two cases are equivalent), the chance is the same as that of the average value since the ranges are uniform. For $x=15$ (the average), the second number can be from $0$ to $15+30=45$ - a range of $45$ . The total range is $(30-0)+(75-45)=30+30=60$ . Thus, this case contributes $\dfrac{45}{75}\cdot\dfrac{60}{75}=\dfrac{12}{25}$ .
Adding the two, we get $\dfrac{16}{25}$ for an answer of $16+25=\boxed{041}$ .
~~Technodoggo

## Solution 7
We notice that the arc $QR=2a-2b$ . We let $M$ be the midpoint of $OP$ and the center of the semicircle shown in the diagram in Solution 3. From arc $QR$ , we find $\angle QMR=2a-2b$ . Because the radius of the semicircle is 100, we can use law of cosines to find the length of $QR$ giving us, \[QR^2=100^2+100^2-2(100)(100)\cos(2a-2b).\] Because $QR<100$ , we know $QR^2<100^2$ giving us, \[100^2\ge100^2+100^2-2(100^2)\cos(2a-2b),\] \[1\ge2-2\cos(2a-2b),\] \[\cos(2a-2b)\ge\frac{1}{2}.\]
Because $\cos^{-1}\left(\frac{1}{2}\right)=\pm60^{\circ}$ , we know that $2a-2b\le60$ or $2a-2b\ge300$ . However, the maximum value of $a$ is $65$ meaning $2a-2b\ge300$ is impossible. Thus, we find, \[a-b<30.\] We can use geometric probability to find the probability of this occurring which ends up giving us the following equation, \[\frac{75^2-45^2}{75^2}=\frac{16}{25}.\] We add the numerator and denominator of our resulting fraction giving us the answer $41$ . $\square$ -mark888
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .