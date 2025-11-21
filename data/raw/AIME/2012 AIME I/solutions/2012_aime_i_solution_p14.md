# 2012 AIME I Problem 14

## Problem

Complex numbers $a,$ $b,$ and $c$ are zeros of a polynomial $P(z) = z^3 + qz + r,$ and $|a|^2 + |b|^2 + |c|^2 = 250.$ The points corresponding to $a,$ $b,$ and $c$ in the complex plane are the vertices of a right triangle with hypotenuse $h.$ Find $h^2.$

## Solution 1
By Vieta's formula, the sum of the roots is equal to 0, or $a+b+c=0$ . Therefore, $\frac{(a+b+c)}{3}=0$ . Because the centroid of any triangle is the average of its vertices, the centroid of this triangle is the origin. Let one leg of the right triangle be $x$ and the other leg be $y$ . Without the loss of generality, let $\overline{ac}$ be the hypotenuse. The magnitudes of $a$ , $b$ , and $c$ are just $\frac{2}{3}$ of the medians because the origin, or the centroid in this case, cuts the median in a ratio of $2:1$ . So, $|a|^2=\frac{4}{9}\cdot((\frac{x}{2})^2+y^2)=\frac{x^2}{9}+\frac{4y^2}{9}$ because $|a|$ is two thirds of the median from $a$ . Similarly, $|c|^2=\frac{4}{9}\cdot(x^2+(\frac{y}{2})^2)=\frac{4x^2}{9}+\frac{y^2}{9}$ . The median from $b$ is just half the hypotenuse because the median of any right triangle is just half the hypotenuse. So, $|b|^2=\frac{4}{9}\cdot\frac{x^2+y^2}{4}=\frac{x^2}{9}+\frac{y^2}{9}$ . Hence, $|a|^2+|b|^2+|c|^2=\frac{6x^2+6y^2}{9}=\frac{2x^2+2y^2}{3}=250$ . Therefore, $h^2=x^2+y^2=\frac{3}{2}\cdot250=\boxed{375}$ .

## Solution 2
Note that by vieta's, the sum of the roots is $0,$ so the centroid (at (a+b+c)/3) of the right triangle is at the origin. This is all that is required by the structure of the polynomial. Let $A,B,C$ be the vertices of the triangle corresponding to roots $a,b,c$ with (WLOG) $\angle ACB=0.$ Let $O$ be the centroid of the triangle, and let $Z$ be the midpoint of $AB.$ By the property of the centroid as the intersection of the medians, $C,O,$ and $Z$ are collinear in that order. Also, by properties of medians and right triangles $AZ=BZ=CZ$ and $OC=2ZO.$ Then, set $AZ=BZ=CZ=3k$ and $OZ=k$ and $CO=2k.$ Stewart's theorem on ACZ and BCZ and rearranging gets \[3AO^2=12k^2+AC^2,\] \[3BO^2=12k^2+BC^2.\] Summing these up gives us \[3(AO^2+BO^2)=24k^2+(AC^2+BC^2)\] Because $AC^2+BC^2=AB^2=36k^2,$ we have \[AO^2+BO^2=20k^2.\] Because $CO=2k,$ \[AO^2+BO^2+CO^2=24k^2.\] By the second condition, this must be equal to $250.$ Then, $k^2=\frac{125}{12},$ and the hypotenuse squared is \[(6k^2)^2=36k^2=36\left(\dfrac{125}{12}\right)=\boxed{375}.\]
~BS2012

## Solution 3
Assume $q$ and $r$ are real, so at least one of $a,$ $b,$ and $c$ must be real, with the remaining roots being pairs of complex conjugates. Without loss of generality, we assume $a$ is real and $b$ and $c$ are $x + yi$ and $x - yi$ respectively. By symmetry, the triangle described by $a,$ $b,$ and $c$ must be isosceles and is thus an isosceles right triangle with hypotenuse $\overline{bc}.$ Now since $P(z)$ has no $z^2$ term, we must have $a+b+c = a + (x + yi) + (x - yi) = 0$ and thus $a = -2x.$ Also, since the length of the altitude from the right angle of an isosceles triangle is half the length of the hypotenuse, $a-x=y$ and thus $y=-3x.$ We can then solve for $x$ :
\begin{align*} |a|^2 + |b|^2 + |c|^2 &= 250\\ |-2x|^2 + |x-3xi|^2 + |x+3xi|^2 &= 250\\ 4x^2 + (x^2 + 9x^2) + (x^2 + 9x^2) &= 250\\ x^2 &= \frac{250}{24} \end{align*}
Now $h$ is the distance between $b$ and $c,$ so $h = 2y = -6x$ and thus $h^2 = 36x^2 = 36 \cdot \frac{250}{24} = \boxed{375.}$

## Solution 4 (Messy)
Let the roots $a$ , $b$ , and $c$ each be represented by complex numbers $m + ni$ , $p + qi$ , and $r + ti$ . By Vieta's formulas, their sum is 0. Breaking into real and imaginary components, we get:
$m + p + r = 0$
$n + q + t = 0$
And, we know that the sum of the squares of the magnitudes of each is 250, so
$m^2 + n^2 + p^2 + q^2 + r^2 + t^2 = 250$
Given the complex plane, we set each of these complex numbers to points: $(m, n)$ , $(p, q)$ , $(r, t)$ . WLOG let $(r, t)$ be the vertex opposite the hypotenuse.
If the three points form a right triangle, the vectors from $(r, t)$ to $(m, m)$ and $(p, q)$ 's dot product is 0. $mp + r^2 - r(m + p) + nq + t^2 - t(n + q) = 0$
Substituting $m + p + r = 0$ and likewise, simplifying: $mp + 2r^2 + nq + 2t^2 = 0$
Rearranging we get: $r^2 + t^2 = -\frac{mp + nq}{2}$
The answer is the distance from $(m, n)$ to $(p, q)$ = $m^2 + n^2 + p^2 + q^2 - 2(mp + nq)$ . Substituting the equation equal to 250,
$= 250 - r^2 - t^2 - 2(mp + nq)$ $= 250 + \frac{mp + nq}{2} - 2(mp + nq)$ $= 250 - \frac{3}{2} \cdot (mp + nq)$
Taking our original equations summing to 0, and squaring each we get:
$n + q = -t$ ; $m + p = -r$
$n^2 + 2nq + q^2 = t^2$ ; $m^2 + 2mp + p^2 = r^2$
Adding, we get:
$m^2 + n^2 + p^2 + q^2 + 2(mp + nq) = r^2 + t^2$
Substituting again we obtain:
$250 - r^2 - t^2 + 2(mp + nq) = r^2 + t^2$ $2(r^2 + t^2) = 250 + 2(mp + nq)$ $r^2 + t^2 = 125 + (mp + nq)$
Substituting the equivalence of $r^2 + t^2$ :
$-\frac{mp + nq}{2} = 125 + (mp + nq)$
Solving for $mp + nq$ , we find it equal to $-\frac{250}{3}$ .
Substituting this value into our answer expression, we get:
$250 - \frac{3}{2} \cdot (-\frac{250}{3})$ , Answer = $\boxed{375}$ .

## Solution 5 (clean)
As noted in the previous solutions, $a+b+c = 0$ . Let $a = a_1+a_2 i$ , $b = b_1+b_2 i$ , $c = c_1+c_2 i$ and we have $a_1 + b_1 + c_1 = a_2 + b_2 + c_2 = 0$ . Then the given $|a|^2 + |b|^2 + |c|^2 = 250$ translates to $\sum_{} ( {a_1}^2 + {a_2}^2 ) = 250.$ Note that in a right triangle, the sum of the squares of the three sides is equal to two times the square of the hypotenuse, by the pythagorean theorem. Thus, we have \[2h^2 = (a_1 - b_1)^2 + (a_2 - b_2)^2 + (b_1 - c_1)^2 + (b_2 - c_2)^2 + (a_1 - c_1)^2 + (a_2 - c_2)^2\] \[= 2 \left( \sum_{} ( {a_1}^2 + {a_2}^2 ) \right) - 2 \left( \sum_{cyc} a_1 b_1 + \sum_{cyc} a_2 b_2 \right)\] \[= 500 - \left( (a_1 + b_1 + c_1)^2 + (a_2 + b_2 + c_2)^2 - \sum_{cyc} ( {a_1}^2 + {a_2}^2 ) \right)\] \[= 500 - (0^2 + 0^2 - 250)\] so $h^2 = \boxed{375}$ and we may conclude. ~ rzlng

## Solution 5 (dirty because of god intuition + wishful thinking)
First, note that the roots of this cubic will be $a, b$ and $-(a+b)$ due to Vieta's, which means that the sum of the roots are 0.
Now, we use some god level wishful thinking. It would really be nice if one of these roots was on the real axis, and it was a right isosceles triangle, because that would be very convenient and easy to work with. The neat part is that it actually works
Set one of the roots as $r$ , where $r$ is any real number. WLOG, assume that this is the right angle. With symmetry to respect of the x axis (because symmetry makes the imaginary parts of the other 2 roots cancel out, besides the fact that complex conjugate root theorem forces it). This way, we can set the other 2 roots as $\frac{r}{2}+ni$ and $\frac{r}{2}-ni$ , making the roots add up to 0.
Now, as we want the roots to satisfy the original condition (right triangle) we are going to have to set an equation to find $n$ out. We use the fact that it is an isosceles right triangle to find that $\frac{3r}{2}=n$ , which means that the 2 other roots are now $\frac{r}{2}+\frac{3r}{2}i$ and $\frac{r}{2}-\frac{3r}{2}i$
Now we use the fact that $|a|^2+|b|^2+|c|^2=250$ . Clearly one of these is $r$ away from the origin, so that gets $r^2$ , and then we get $2*\frac{r}{2}^2+\frac{3r}{2}^2$ which gets us $5r^2$ , getting $r^2+5r^2=250$ , so $r=\sqrt{\frac{250}{6}}$ . So the final answer comes out to \[(\frac{250}{6}*\frac{9}{4}*2)^2=\boxed{\boxed{375}}\]
-dragoon
P.S.: The main propose, saying that one root is on the real axis and the right triangle is a right isosceles triangle is not actually only a wishful thinking that came out by luck, but actually is something that must be true due to the complex conjugate root theorem. -SuperDolphin
- in this specific problem this logic is incorrect, as the coefficients of the polynomial can be complex. If a question specified real roots, then this would be appropriate. In this case, it is just wishful thinking as stated above

## Solution 6 (vectors)
As shown in the other solutions, $a+b+c = 0$ .
Without loss of generality, let $b$ be the complex number opposite the hypotenuse.
Note that there is an isomorphism between $\mathbb{C}$ under $+$ and $\mathbb{R}^2$ under $+$ .
Let $\Vec{a}$ , $\Vec{b}$ , and $\Vec{c}$ be the corresponding vectors to $a$ , $b$ , and $c$ .
Thus $\Vec{a} + \Vec{b} + \Vec{c} = \Vec{0}$
$\Rightarrow 0 = \Vec{0}\cdot \Vec{0} = (\Vec{a} + \Vec{b} + \Vec{c})\cdot (\Vec{a} + \Vec{b} + \Vec{c}) = \Vec{a}\cdot \Vec{a} + \Vec{b}\cdot \Vec{b} + \Vec{c}\cdot \Vec{c} + 2(\Vec{a}\cdot \Vec{b} + \Vec{a}\cdot \Vec{c} + \Vec{b}\cdot \Vec{c})$
Now $|a|^2 + |b|^2 + |c|^2 = 250$ implies that $\lVert \Vec{a}\rVert^2 + \lVert \Vec{b}\rVert^2 + \lVert \Vec{c}\rVert^2 = 250$
$\Rightarrow \Vec{a}\cdot \Vec{a} + \Vec{b}\cdot \Vec{b} + \Vec{c}\cdot \Vec{c} = \lVert \Vec{a}\rVert^2 + \lVert \Vec{b}\rVert^2 + \lVert \Vec{c}\rVert^2 = 250$
Also note that because there is a right angle at $b$ , $\Vec{a} - \Vec{b}$ and $\Vec{c} - \Vec{b}$ are perpendicular.
$\Rightarrow (\Vec{a} - \Vec{b})\cdot (\Vec{c} - \Vec{b}) = 0$
$\Rightarrow 0 = (\Vec{a} - \Vec{b})\cdot (\Vec{c} - \Vec{b}) = \Vec{a}\cdot \Vec{c} + \Vec{b} \cdot \Vec{b} - \Vec{a} \cdot \Vec{b} - \Vec{b} \cdot \Vec{c}$
Note that $h^2 = |a-c|^2$
$\Rightarrow h^2 = \lVert \Vec{a} - \Vec{c} \rVert^2 = (\Vec{a} - \Vec{c})\cdot (\Vec{a} - \Vec{c}) = \Vec{a} \cdot \Vec{a} + \Vec{c}\cdot \Vec{c} - \Vec{a}\cdot \Vec{c} - \Vec{a}\cdot \Vec{c} = \Vec{a} \cdot \Vec{a} + \Vec{c}\cdot \Vec{c} - 2\Vec{a}\cdot \Vec{c}$ .
$\Rightarrow 0 = \Vec{a}\cdot \Vec{a} + \Vec{b}\cdot \Vec{b} + \Vec{c}\cdot \Vec{c} + 2(\Vec{a}\cdot \Vec{b} + \Vec{a}\cdot \Vec{c} + \Vec{b}\cdot \Vec{c}) = 250 + 2(\Vec{a}\cdot \Vec{b} + \Vec{a}\cdot \Vec{c} + \Vec{b}\cdot \Vec{c})$
$\Rightarrow -250 = 2(\Vec{a}\cdot \Vec{b} + \Vec{a}\cdot \Vec{c} + \Vec{b}\cdot \Vec{c})$
$\Rightarrow -125 = \Vec{a}\cdot \Vec{b} + \Vec{a}\cdot \Vec{c} + \Vec{b}\cdot \Vec{c}$
$\Rightarrow -125 = -125 + 0 = (\Vec{a}\cdot \Vec{b} + \Vec{a}\cdot \Vec{c} + \Vec{b}\cdot \Vec{c}) + (\Vec{a}\cdot \Vec{c} + \Vec{b} \cdot \Vec{b} - \Vec{a} \cdot \Vec{b} - \Vec{b} \cdot \Vec{c}) = 2\Vec{a}\cdot \Vec{c} + \Vec{b} \cdot \Vec{b}$
$\Rightarrow 125 = - \Vec{b} \cdot \Vec{b} - 2\Vec{a}\cdot \Vec{c}$
$\Rightarrow 375 = 250 + 125 = \Vec{a}\cdot \Vec{a} + \Vec{b}\cdot \Vec{b} + \Vec{c}\cdot \Vec{c} - \Vec{b} \cdot \Vec{b} - 2\Vec{a}\cdot \Vec{c} = \Vec{a}\cdot \Vec{a} + \Vec{c}\cdot \Vec{c} - 2\Vec{a}\cdot \Vec{c} = h^2$
$\Rightarrow h^2 = \boxed{375}$

## Solution 6(similar to solution 4)
Note that the roots of the polynomial $(a,b,c)$ must sum to $0$ due to the $z^2$ coefficient equaling $0$ because of Vieta's Formulas. This tells us that $a+b+c = 0$ and $\overline{a} + \overline{b} + \overline{c} = 0$ so $(a+b+c)(\overline{a+b+c}) = |a|^2 + |b|^2 + |c|^2 + a\overline{b} + \overline{a}b + b\overline{c} + \overline{b}c + c\overline{a} + \overline{c}a = 250 + a\overline{b} + \overline{a}b + b\overline{c} + \overline{b}c + c\overline{a} + \overline{c}a = 0$ so $a\overline{b} + \overline{a}b + b\overline{c} + \overline{b}c + c\overline{a} + \overline{c}a = -250.$
Note that terms similar to $\overline{a}b + \overline{b}a$ appear in $|a-b|^2$ so we decide to sum $|a-b|^2 + |b-c|^2 + |c-a|^2$ out of intuition. Note that this corresponds to the sum of the squares of the sidelengths of the right triangle and if WLOG the $|c-a|^2$ side is the hypotenuse then our sum is equal to $2|c-a|^2 = 2h^2.$
\[2|a|^2 + 2|b|^2 + 2|c|^2 -a\overline{b} - \overline{a}b - b\overline{c} - \overline{b}c - c\overline{a} - \overline{c}a = 500 + 250 = 2h^2\]
As a result we know that $h^2 = \boxed{375}$ ~SailS

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/354
~ dolphin7
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .