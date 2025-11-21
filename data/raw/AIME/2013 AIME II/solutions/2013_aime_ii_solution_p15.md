# 2013 AIME II Problem 15

## Problem

Let $A,B,C$ be angles of a triangle with \begin{align*} \cos^2 A + \cos^2 B + 2 \sin A \sin B \cos C &= \frac{15}{8} \text{ and} \\ \cos^2 B + \cos^2 C + 2 \sin B \sin C \cos A &= \frac{14}{9} \end{align*} There are positive integers $p$ , $q$ , $r$ , and $s$ for which \[\cos^2 C + \cos^2 A + 2 \sin C \sin A \cos B = \frac{p-q\sqrt{r}}{s},\] where $p+q$ and $s$ are relatively prime and $r$ is not divisible by the square of any prime. Find $p+q+r+s$ .

## Solution 1
Let's draw the triangle. Since the problem only deals with angles, we can go ahead and set one of the sides to a convenient value. Let $BC = \sin{A}$ .
By the Law of Sines, we must have $CA = \sin{B}$ and $AB = \sin{C}$ .
Now let us analyze the given:
\begin{align*} \cos^2A + \cos^2B + 2\sin A\sin B\cos C &= 1-\sin^2A + 1-\sin^2B + 2\sin A\sin B\cos C \\ &= 2-(\sin^2A + \sin^2B - 2\sin A\sin B\cos C) \end{align*}
Now we can use the Law of Cosines to simplify this:
\[= 2-\sin^2C\]
Therefore: \[\sin C = \sqrt{\dfrac{1}{8}},\cos C = \sqrt{\dfrac{7}{8}}.\] Similarly, \[\sin A = \sqrt{\dfrac{4}{9}},\cos A = \sqrt{\dfrac{5}{9}}.\] Note that the desired value is equivalent to $2-\sin^2B$ , which is $2-\sin^2(A+C)$ . All that remains is to use the sine addition formula and, after a few minor computations, we obtain a result of $\dfrac{111-4\sqrt{35}}{72}$ . Thus, the answer is $111+4+35+72 = \boxed{222}$ .
Note that the problem has a flaw because $\cos B < 0$ which contradicts with the statement that it's an acute triangle. Would be more accurate to state that $A$ and $C$ are smaller than 90. -Mathdummy

## Solution 2
Let us use the identity $\cos^2A+\cos^2B+\cos^2C+2\cos A \cos B \cos C=1$ .
Add \begin{align*} \cos^2 C+2(\cos A\cos B-\sin A \sin B)\cos C \end{align*} to both sides of the first given equation.
Thus, as \begin{align*} \cos A\cos B-\sin A\sin B=\cos (A+B)=-\cos C ,\end{align*} we have \begin{align*} \dfrac{15}{8}-2\cos^2 C +\cos^2 C=1, \end{align*} so $\cos C$ is $\sqrt{\dfrac{7}{8}}$ and therefore $\sin C$ is $\sqrt{\dfrac{1}{8}}$ .
Similarily, we have $\sin A =\dfrac{2}{3}$ and $\cos A=\sqrt{\dfrac{14}{9}-1}=\sqrt{\dfrac{5}{9}}$ and the rest of the solution proceeds as above.

## Solution 3
Let \begin{align*} \cos^2 A + \cos^2 B + 2 \sin A \sin B \cos C &= \frac{15}{8} \text{ ------ (1)}\\ \cos^2 B + \cos^2 C + 2 \sin B \sin C \cos A &= \frac{14}{9} \text{ ------ (2)}\\ \cos^2 C + \cos^2 A + 2 \sin C \sin A \cos B &= x \text{ ------ (3)}\\ \end{align*}
Adding (1) and (3) we get: \[2 \cos^2 A + \cos^2 B + \cos^2 C + 2 \sin A( \sin B \cos C + \sin C \cos B) = \frac{15}{8} + x\] or \[2 \cos^2 A + \cos^2 B + \cos^2 C + 2 \sin A \sin (B+C) = \frac{15}{8} + x\] or \[2 \cos^2 A + \cos^2 B + \cos^2 C + 2 \sin ^2 A = \frac{15}{8} + x\] or \[\cos^2 B + \cos^2 C = x - \frac{1}{8} \text{ ------ (4)}\]
Similarly adding (2) and (3) we get: \[\cos^2 A + \cos^2 B = x - \frac{4}{9} \text{ ------ (5)}\] Similarly adding (1) and (2) we get: \[\cos^2 A + \cos^2 C = \frac{14}{9} - \frac{1}{8} \text{ ------ (6)}\]
And (4) - (5) gives: \[\cos^2 C - \cos^2 A = \frac{4}{9} - \frac{1}{8} \text{ ------ (7)}\]
Now (6) - (7) gives: $\cos^2 A = \frac{5}{9}$ or $\cos A = \sqrt{\dfrac{5}{9}}$ and $\sin A = \frac{2}{3}$ so $\cos C$ is $\sqrt{\dfrac{7}{8}}$ and therefore $\sin C$ is $\sqrt{\dfrac{1}{8}}$
Now $\sin B = \sin(A+C)$ can be computed first and then $\cos^2 B$ is easily found.
Thus $\cos^2 B$ and $\cos^2 C$ can be plugged into (4) above to give x = $\dfrac{111-4\sqrt{35}}{72}$ .
Hence the answer is = $111+4+35+72 = \boxed{222}$ .
Kris17

## Solution 4
Let's take the first equation $\cos^2 A + \cos^2 B + 2 \sin A \sin B \cos C = \frac{15}{8}$ . Substituting $180 - A - B$ for C, given A, B, and C form a triangle, and that $\cos C = \cos(A + B)$ , gives us:
$\cos^2 A + \cos^2 B + 2 \sin A \sin B \cos (A+B) = \frac{15}{8}$
Expanding out gives us $\cos^2 A + \cos^2 B + 2 \sin^2 A \sin^2 B - 2 \sin A \sin B \cos A \cos B = \frac{15}{8}$ .
Using the double angle formula $\cos^2 k = \frac{\cos (2k) + 1}{2}$ , we can substitute for each of the squares $\cos^2 A$ and $\cos^2 B$ . Next we can use the Pythagorean identity on the $\sin^2 A$ and $\sin^2 B$ terms. Lastly we can use the sine double angle to simplify.
$\cos^2 A + \cos^2 B + 2(1 - \cos^2 A)(1 - \cos^2 B) - \frac{1}{2} \cdot \sin 2A \sin 2B = \frac{15}{8}$ .
Expanding and canceling yields, and again using double angle substitution,
$1 + 2 \cdot \frac{\cos (2A) + 1}{2} \cdot \frac{\cos (2B) + 1}{2} - \frac{1}{2} \cdot \sin 2A \sin 2B = \frac{15}{8}$ .
Further simplifying yields:
$\frac{3}{2} + \frac{\cos 2A \cos 2B - \sin 2A \sin 2B}{2} = \frac{15}{8}$ .
Using cosine angle addition formula and simplifying further yields, and applying the same logic to Equation $2$ yields:
$\cos (2A + 2B) = \frac{3}{4}$ and $\cos (2B + 2C) = \frac{1}{9}$ .
Substituting the identity $\cos (2A + 2B) = \cos(2C)$ , we get:
$\cos (2C) = \frac{3}{4}$ and $\cos (2A) = \frac{1}{9}$ .
Since the third expression simplifies to the expression $\frac{3}{2} + \frac{\cos (2A + 2C)}{2}$ , taking inverse cosine and using the angles in angle addition formula yields the answer, $\frac{111 - 4\sqrt{35}}{72}$ , giving us the answer $\boxed{222}$ .

## Solution 5
We will use the sum to product formula to simply these equations. Recall \[2\sin{\frac{\alpha+\beta}{2}}\sin{\frac{\alpha-\beta}{2}} = \cos{\alpha}+\cos{\beta}.\] Using this, let's rewrite the first equation: \[\cos^2(A) + \cos^2(B) + 2 \sin(A) \sin(B) \cos(C) = \frac{15}{8}\] \[\cos^2(A) + \cos^2(B) + (\cos(A+B)+\cos(A-B))\cos(C).\] Now, note that $\cos(C)=-\cos(A+B)$ . \[\cos^2(A) + \cos^2(B) + (\cos(A+B)+\cos(A-B))(-\cos(A+B))\] \[\cos^2(A) + \cos^2(B) - \cos(A+B)\cos(A-B)+cos^2(A+B)=\frac{15}{8}.\] We apply the sum to product formula again. \[\cos^2(A) + \cos^2(B) - \frac{\cos(2A)+\cos(2B)}{2}+cos^2(A+B)=\frac{15}{8}.\] Now, recall that $\cos(2\alpha)=2\cos^2(\alpha)-1$ . We apply this and simplify our expression to get: \[\cos^2(A+B)=\frac{7}{8}\] \[\cos^2(C)=\frac{7}{8}.\] Analogously, \[\cos^2(A)=\frac{5}{9}.\] \[\cos^2(A+C)=\frac{p-q\sqrt{r}}{s}-1.\] We can find this value easily by angle sum formula. After a few calculations, we get $\frac{111 - 4\sqrt{35}}{72}$ , giving us the answer $\boxed{222}$ . ~superagh

## Solution 6
According to LOC $a^2+b^2-2ab\cos{\angle{c}}=c^2$ , we can write it into $\sin^2{\angle{A}}+\sin^2{\angle{B}}-2\sin{\angle{A}}\sin{\angle{B}}\cos{\angle{C}}=\sin^2{\angle{C}}$ . $\sin^2{\angle{A}}+\sin^2{\angle{B}}-2\sin{\angle{A}}\sin{\angle{B}}\cos{\angle{C}}+cos^2A+cos^2B+2sinAsinBcosC=\frac{15}{8}+sin^2C$ We can simplify to $2=sin^2C+\frac{15}{8}$ . Similarly, we can generalize $2=sin^2A+\frac{14}{9}$ . After solving, we can get that $sinA=\frac{2}{3}; cosA=\frac{\sqrt{5}}{3}; sinC=\frac{\sqrt{2}}{4}; cosC=\frac{\sqrt{14}}{4}$ Assume the value we are looking for is $x$ , we get $sin^2B+x=2$ , while $sinB=sin(180^{\circ}-A-C)=sin(A+C)$ which is $\frac{2\sqrt{14}+\sqrt{10}}{12}$ , so $x=\frac{111 - 4\sqrt{35}}{72}$ , giving us the answer $\boxed{222}$ .~bluesoul

## Video Solution
https://youtu.be/_wB0WyhNoQE?si=wjjJtQ_rxi2dsDbo
~MathProblemSolvingSkills.com

## Video Solution by The Power Of Logic
https://youtu.be/9TVhH2bFjT0
~Hayabusa1
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .