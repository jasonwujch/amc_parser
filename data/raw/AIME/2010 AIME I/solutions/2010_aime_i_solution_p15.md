# 2010 AIME I Problem 15

## Problem

In $\triangle{ABC}$ with $AB = 12$ , $BC = 13$ , and $AC = 15$ , let $M$ be a point on $\overline{AC}$ such that the incircles of $\triangle{ABM}$ and $\triangle{BCM}$ have equal radii . Then $\frac{AM}{CM} = \frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p + q$ .

## Solution

## Solution 1
Let $AM = x$ , then $CM = 15 - x$ . Also let $BM = d$ Clearly, $\frac {[ABM]}{[CBM]} = \frac {x}{15 - x}$ . We can also express each area by the rs formula. Then $\frac {[ABM]}{[CBM]} = \frac {p(ABM)}{p(CBM)} = \frac {12 + d + x}{28 + d - x}$ . Equating and cross-multiplying yields $25x + 2dx = 15d + 180$ or $d = \frac {25x - 180}{15 - 2x}.$ Note that for $d$ to be positive, we must have $7.2 < x < 7.5$ .
By Stewart's Theorem , we have $12^2(15 - x) + 13^2x = d^215 + 15x(15 - x)$ or $432 = 3d^2 + 40x - 3x^2.$ Brute forcing by plugging in our previous result for $d$ , we have $432 = \frac {3(25x - 180)^2}{(15 - 2x)^2} + 40x - 3x^2.$ Clearing the fraction and gathering like terms, we get $0 = 12x^4 - 340x^3 + 2928x^2 - 7920x.$
Aside: Since must be rational in order for our answer to be in the desired form, we can use the Rational Root Theorem to reveal that is an integer because we can divide the polynomial by . The only such in the above-stated range is .
Legitimately solving that quartic, note that $x = 0$ and $x = 15$ should clearly be solutions, corresponding to the sides of the triangle and thus degenerate cevians. Factoring those out, we get $0 = 4x(x - 15)(3x^2 - 40x + 132) = x(x - 15)(x - 6)(3x - 22).$ The only solution in the desired range is thus $\frac {22}3$ . Then $CM = \frac {23}3$ , and our desired ratio $\frac {AM}{CM} = \frac {22}{23}$ , giving us an answer of $\boxed{045}$ .

## Solution 2
Let $AM = 2x$ and $BM = 2y$ so $CM = 15 - 2x$ . Let the incenters of $\triangle ABM$ and $\triangle BCM$ be $I_1$ and $I_2$ respectively, and their equal inradii be $r$ . From $r = \sqrt {(s - a)(s - b)(s - c)}/s$ , we find that
\begin{align*}r^2 & = \frac {(x + y - 6)( - x + y + 6)(x - y + 6)}{x + y + 6} & (1) \\ & = \frac {( - x + y + 1)(x + y - 1)( - x - y + 14)}{ - x + y + 14}. & (2) \end{align*}
Let the incircle of $\triangle ABM$ meet $AM$ at $P$ and the incircle of $\triangle BCM$ meet $CM$ at $Q$ . Then note that $I_1 P Q I_2$ is a rectangle. Also, $\angle I_1 M I_2$ is right because $MI_1$ and $MI_2$ are the angle bisectors of $\angle AMB$ and $\angle CMB$ respectively and $\angle AMB + \angle CMB = 180^\circ$ . By properties of tangents to circles $MP = (MA + MB - AB)/2 = x + y - 6$ and $MQ = (MB + MC - BC)/2 = - x + y + 1$ . Now notice that the altitude of $M$ to $I_1 I_2$ is of length $r$ , so by similar triangles we find that $r^2 = MP \cdot MQ = (x + y - 6)( - x + y + 1)$ (3). Equating (3) with (1) and (2) separately yields
\begin{align*} 2y^2 - 30 = 2xy + 5x - 7y \\ 2y^2 - 70 = - 2xy - 5x + 7y, \end{align*}
and adding these we have
\[4y^2 - 100 = 0\implies y = 5\implies x = 11/3 \\ \implies AM/MC = (22/3)/(15 - 22/3) = 22/23 \implies \boxed{045}.\]

## Solution 3
Let the incircle of $ABM$ hit $AM$ , $AB$ , $BM$ at $X_{1},Y_{1},Z_{1}$ , and let the incircle of $CBM$ hit $MC$ , $BC$ , $BM$ at $X_{2},Y_{2},Z_{2}$ . Draw the incircle of $ABC$ , and let it be tangent to $AC$ at $X$ . Observe that we have a homothety centered at A sending the incircle of $ABM$ to that of $ABC$ , and one centered at $C$ taking the incircle of $BCM$ to that of $ABC$ . These have the same power, since they take incircles of the same size to the same circle. Also, the power of the homothety is $AX_{1}/AX=CX_{2}/CX$ .
By standard computations, $AX=\dfrac{AB+AC-BC}{2}=7$ and $CX=\dfrac{BC+AC-AB}{2}=8$ . Now, let $AX_{1}=7x$ and $CX_{2}=8x$ . We will now go around and chase lengths. Observe that $BY_{1}=BA-AY_{1}=BA-AX_{1}=12-7x$ . Then, $BZ_{1}=12-7x$ . We also have $CY_{2}=CX_{2}=8x$ , so $BY_{2}=13-8x$ and $BZ_{2}=13-8x$ .
Observe now that $X_{1}M+MX_{2}=AC-15x=15(1-x)$ . Also, $X_{1}M-MX_{2}=MZ_{1}-MZ_{2}=BZ_{2}-BZ_{1}=BY_{2}-BY_{1}=(1-x)$ . Solving, we get $X_{1}M=8-8x$ and $MX_{2}=7-7x$ (as a side note, note that $AX_{1}+MX_{2}=X_{1}M+X_{2}C$ , a result that I actually believe appears in Mandelbrot 1995-2003, or some book in that time-range).
Now, we get $BM=BZ_{2}+Z_{2}M=BZ_{2}+MX_{2}=20-15x$ . To finish, we will compute area ratios. $\dfrac{[ABM]}{[CBM]}=\dfrac{AM}{MC}=\dfrac{8-x}{7+x}$ . Also, since their inradii are equal, we get $\dfrac{[ABM]}{[CBM]}=\dfrac{40-16x}{40-14x}$ . Equating and cross multiplying yields the quadratic $3x^{2}-8x+4=0$ , so $x=2/3,2$ . However, observe that $AX_{1}+CX_{2}=15x<15$ , so we take $x=2/3$ . Our ratio is therefore $\dfrac{8-2/3}{7+2/3}=\dfrac{22}{23}$ , giving the answer $\boxed{045}$ .
Note: Once we have $MX_1=8-8x$ and $MX_2=7-7x$ , it's bit easier to use use the right triangle of $O_1MO_2$ than chasing the area ratio. The inradius of $\triangle{ABC}$ can be calculated to be $r=\sqrt{14}$ , and the inradius of $ABM$ and $ACM$ are $r_1=r_2= xr$ , so, \[O_1O_2^2 = O_1M^2 + O_2M^2 = r_1^2+X_1M^2 + r_2^2 + X_2M^2\] or, \[(15(1-x))^2 = 2(\sqrt{14}x)^2 + (7(1-x))^2 + (8(1-x))^2\] \[112(1-x)^2 = 28x^2\] \[4(1-x)^2 = x^2\] We get $x=\frac{2}{3}$ or $x=2$ .

## Solution 4
Suppose the incircle of $ABM$ touches $AM$ at $X$ , and the incircle of $CBM$ touches $CM$ at $Y$ . Then
\[r = AX \tan(A/2) = CY \tan(C/2)\]
We have $\cos A = \frac{12^2+15^2-13^2}{2\cdot 12\cdot 15} = \frac{200}{30\cdot 12}=\frac{5}{9}$ , $\tan(A/2) = \sqrt{\frac{1-\cos A}{1+\cos A}} = \sqrt{\frac{9-5}{9+5}} = \frac{2}{\sqrt{14}}$
$\cos C = \frac{13^2+15^2-12^2}{2\cdot 13\cdot 15} = \frac{250}{30\cdot 13} = \frac{25}{39}$ , $\tan(C/2) = \sqrt{\frac{39-25}{39+25}}=\frac{\sqrt{14}}{8}$ ,
Therefore $AX/CY = \tan(C/2)/\tan(A/2) = \frac{14}{2\cdot 8}= \frac{7}{8}.$
And since $AX=\frac{1}{2}(12+AM-BM)$ , $CY = \frac{1}{2}(13+CM-BM)$ ,
\[\frac{12+AM-BM}{13+CM-BM} = \frac{7}{8}\]
\[96+8AM-8BM = 91 +7CM-7BM\]
\[BM= 5 + 8AM-7CM = 5 + 15AM - 7(CM+AM) = 5+15(AM-7) \dots\dots (1)\]
Now,
$\frac{AM}{CM} = \frac{[ABM]}{[CBM]} = \frac{\frac{1}{2}(12+AM+BM)r}{\frac{1}{2}(13+CM+BM)r}=\frac{12+AM+BM}{13+CM+BM}= \frac{12+BM}{13+BM} = \frac{17+15(AM-7)}{18+15(AM-7)}$
\[\frac{AM}{15} = \frac{17+15(AM-7)}{35+30(AM-7)} = \frac{15AM-88}{30AM-175}\] \[6AM^2 - 35AM = 45AM-264\] \[3AM^2 -40AM+132=0\] \[(3AM-22)(AM-6)=0\]
So $AM=22/3$ or $6$ . But from (1) we know that $5+15(AM-7)>0$ , or $AM>7-1/3>6$ , so $AM=22/3$ , $CM=15-22/3=23/3$ , $AM/CM=22/23$ .

## Solution 5
Let the common inradius equal r, $BM = x$ , $AM = y$ , $MC = z$
From the prespective of $\triangle{ABM}$ and $\triangle{BMC}$ we get:
$S_{ABM} = rs = r \cdot (\frac{12+x+y}{2})$ $S_{BMC} = rs = r \cdot (\frac{13+x+z}{2})$
Add two triangles up, we get $\triangle{ABC}$ :
$S_{ABC} = S_{ABM} + S_{BMC} = r \cdot \frac{25+2x+y+z}{2}$
Since $y + z = 15$ , we get:
By drawing an altitude from $I_1$ down to a point $H_1$ and from $I_2$ to $H_2$ , we can get:
$r \cdot cot(\frac{\angle A}{2}) =r \cdot A H_1 = r \cdot \frac{12+y-x}{2}$ and
$r \cdot cot(\frac{\angle C}{2}) = r \cdot H_2 C = r \cdot \frac{13+z-x}{2}$
Adding these up, we get:
$r \cdot (cot(\frac{\angle A}{2})+cot(\frac{\angle C}{2})) = \frac{25+y+z-2x}{2} = \frac{40-2x}{2} = 20-x$
Now, we have 2 values equal to r, we can set them equal to each other:
If we let R denote the incircle of ABC, note:
AC = $(cot(\frac{\angle A}{2})+cot(\frac{\angle C}{2})) \cdot R = 15$ and
$S_{ABC} = \frac{12+13+15}{2} \cdot R = 20 \cdot R$ .
By cross multiplying the equation above, we get:
We can find out x:
Now, we can find ratio of y and z:
The answer is $\boxed{045}$ .
-Alexlikemath

## Solution 6 (Similar to Solution 1 with easier computation)
Let $CM=x, AM=rx, BM=d$ . $x+rx=15\Rightarrow x=\frac{15}{1+r}$ .
Similar to Solution 1, we have \[r=\frac{[AMB]}{[CMB]}=\frac{12+rx+d}{13+x+d} \Rightarrow d=\frac{13r-12}{1-r}\] as well as \[12^2\cdot x + 13^2 rx=15x\cdot rx+15d^2 (\text{via Stewart's Theorem})\] \[\frac{(12^2 + 13^2r) \cdot 15}{1+r} - \frac{15r\cdot 15^2}{(1+r)^2}=\frac{15(13r-12)^2}{(1-r)^2}\] \[\frac{169r^2+88r+144}{(1+r)^2}=\frac{(13r-12)^2}{(1-r)^2} =\frac{169r^2-312r+144}{(1-r)^2} =\frac{400r}{4r}=100\] (here we used the fact that if $\frac{a}{b} = \frac{c}{d} = k,$ then $\frac{a-c}{b-d}=k$ as well.)
Notice $\frac{12}{13} < r < 1$ , so $\frac{13r-12}{1-r} = 10$ and $\boxed{r = \frac{22}{23}}.$
~ asops

## Solution 7 (No Stewart's or trig, fast + clever)
Let $BM = d, AM = x, CM = 15 - x$ . Observe that we have the equation by the incircle formula: \[\frac{[ABM]}{12 + AM + MB} = \frac{[CBM]}{13 + CM + MB} \implies \frac{AM}{CM} = \frac{12 + MB}{13 + MB} \implies \frac{x}{15 - x} = \frac{12 + d}{13 + d}.\] Now let $X$ be the point of tangency between the incircle of $\triangle ABC$ and $AC$ . Additionally, let $P$ and $Q$ be the points of tangency between the incircles of $\triangle ABM$ and $\triangle CBM$ with $AC$ respectively. Some easy calculation yields $AX = 7, CX = 8$ . By homothety we have \[\frac{AP}{7} = \frac{CQ}{8} \implies 8(AP) = 7(CQ) \implies 8(12 + x - d) = 7(13 + 15 - x - d) \implies d = 15x - 100.\] Substituting into the first equation derived earlier it is left to solve \[\frac{x}{15 - x} = \frac{15x - 88}{15x - 87} \implies 3x^2 - 40x + 132 \implies (x - 6)(3x - 22) = 0.\] Now $x = 6$ yields $d = -10$ which is invalid, hence $x = \frac{22}{3}$ so $\frac{AM}{CM} = \frac{\frac{22}{3}}{15 - \frac{22}{3}} = \frac{22}{23}.$ The requested sum is $22 + 23 = \boxed{45}$ . ~blueprimes

## Video Solution
https://www.youtube.com/watch?v=UQVI0Q2PWZw&feature=youtu.be&fbclid=IwAR338IdppnZVuze4rzT0gm8G2NB_uIsmj175WgD6sa43gg3EhFAGm5bAvV0
### Sidenote
In the problem, $BM=10$ and the equal inradius of the two triangles happens to be $\frac {2\sqrt{14}}{3}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .