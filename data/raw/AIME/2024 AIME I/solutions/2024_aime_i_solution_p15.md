# 2024 AIME I Problem 15

## Problem

Let $\mathcal{B}$ be the set of rectangular boxes with surface area $54$ and volume $23$ . Let $r$ be the radius of the smallest sphere that can contain each of the rectangular boxes that are elements of $\mathcal{B}$ . The value of $r^2$ can be written as $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution 1
Observe that the "worst" possible box is one of the maximum possible length. By symmetry, the height and the width are the same in this antioptimal box. (If the height and width weren't the same, the extra difference between them could be used to make the length longer.) Thus, let the width and height be of length $a$ and the length be $L$ .
We're given that the volume is $23$ ; thus, $a^2L=23$ . We're also given that the surface area is $54=2\cdot27$ ; thus, $a^2+2aL=27$ .
From the first equation, we can get $L=\dfrac{23}{a^2}$ . We do a bunch of algebra:
\begin{align*} L&=\dfrac{23}{a^2} \\ 27&=a^2+2aL \\ &=a^2+2a\left(\dfrac{23}{a^2}\right) \\ &=a^2+\dfrac{46}a \\ 27a&=a^3+46 \\ a^3-27a+46&=0. \\ \end{align*}
We can use the Rational Root Theorem and test a few values. It turns out that $a=2$ works. We use synthetic division to divide by $a-2$ :
As we expect, the remainder is $0$ , and we are left with the polynomial $x^2+2x-23$ . We can now simply use the quadratic formula and find that the remaining roots are $\dfrac{-2\pm\sqrt{4-4(-23)}}2=\dfrac{-2\pm\sqrt{96}}2=\dfrac{-2\pm4\sqrt{6}}2=-1\pm2\sqrt6$ . We want the smallest $a$ to maximize $L$ , and it turns out that $a=2$ is in fact the smallest root. Thus, we let $a=2$ . Substituting this into $L=\dfrac{23}{a^2}$ , we find that $L=\dfrac{23}4$ . However, this is not our answer! This is simply the length of the box; we want the radius of the sphere enclosing it. We know that the diameter of the sphere is the diagonal of the box, and the 3D Pythagorean Theorem can give us the space diagonal. Applying it, we find that the diagonal has length $\sqrt{2^2+2^2+\left(\dfrac{23}4\right)^2}=\sqrt{8+\dfrac{529}{16}}=\sqrt{\dfrac{128+529}{16}}=\dfrac{\sqrt{657}}4$ . This is the diameter; we halve it to find the radius, $\dfrac{\sqrt{657}}8$ . We then square this and end up with $\dfrac{657}{64}$ , giving us an answer of $657+64=\boxed{721}$ .
~Technodoggo

## Solution 2 (constrained optimization with Lagrangian multiplier)
Denote by $x$ , $y$ , $z$ the length, width, and height of a rectangular box. We have \begin{align*} xy + yz + zx & = 27 \hspace{1cm} (1) \\ xyz & = 23 \hspace{1cm} (2) \end{align*}
We have \begin{align*} 4 r^2 & = x^2 + y^2 + z^2 \\ & = \left( x + y + z \right)^2 - 2 \cdot \left( xy + yz + zx \right) \\ & = \left( x + y + z \right)^2 - 54 . \end{align*}
Therefore, we solve the following constrained optimization problem: \begin{align*} \max_{x,y,z} \ & x + y + z \\ \mbox{subject to } & (1), (2) \end{align*}
First, we prove that an optimal solution must have at least two out of $x$ , $y$ , $z$ that are the same.
Denote by $\lambda$ and $\eta$ lagrangian multipliers of constraints (1) and (2), respectively. Consider the following Lagrangian: \begin{align*} \max_{x,y,z, \lambda, \eta} & x + y + z + \lambda \left( xy + yz + zx - 27 \right) + \eta \left( xyz - 23 \right) . \end{align*}
Taking first-order-condition with respect to $x$ , $y$ , $z$ , respectively, we get \begin{align*} 1 + \lambda \left( y + z \right) + \eta yz & = 0 \hspace{1cm} (3) \\ 1 + \lambda \left( z + x \right) + \eta zx & = 0 \hspace{1cm} (4) \\ 1 + \lambda \left( x + y \right) + \eta xy & = 0 \hspace{1cm} (5) \end{align*}
Suppose there is an optimal solution with $x$ , $y$ , $z$ that are all distinct.
Taking $(4)-(3)$ , we get \[ \left( x - y \right) \left( \lambda + \eta z \right) = 0 . \]
Because $x \neq y$ , we have \[ \lambda + \eta z = 0 \hspace{1cm} (6) \]
Analogously, we have \begin{align*} \lambda + \eta x & = 0 \hspace{1cm} (7) \end{align*}
Taking $(6) - (7)$ , we get $\eta \left( z - x \right) = 0$ . Because $z \neq x$ , we have $\eta = 0$ . Plugging this into (6), we get $\lambda = 0$ .
However, the solution that $\lambda = \eta = 0$ is a contradiction with (3). Therefore, in an optimal solution, we cannot have $x$ , $y$ , and $z$ to be all distinct.
W.L.O.G, in our remaining analysis, we assume an optimal solution satisfies $y = z$ .
Therefore, we need to solve the following two-variable optimization problem: \begin{align*} \max_{x,y} \ & x + 2y \\ \mbox{subject to } & 2 xy + y^2 = 27 \\ & xy^2 = 23 \end{align*}
Replacing $x$ with $y$ by using the constraint $xy^2 = 23$ , we solve the following single-variable optimization problem: \begin{align*} \max_y \ & \frac{23}{y^2} + 2y \hspace{1cm} (8) \\ \mbox{subject to } & \frac{46}{y} + y^2 = 27 \hspace{1cm} (9) \end{align*}
By solving (9), we get $y = 2$ and $-1 + 2 \sqrt{6}$ .
Plugging $y = 2$ into (8), we get $\frac{23}{y^2} + 2y = \frac{39}{4}$ .
Plugging $y = -1 + 2 \sqrt{6}$ into (8), we get $\frac{23}{y^2} + 2y = \frac{96 \sqrt{6} - 21}{23}$ .
We have $\frac{96 \sqrt{6} - 21}{23} < \frac{39}{4}$ . Therefore, the maximum value of $x + y + z$ is $\frac{39}{4}$ .
Therefore, \begin{align*} r^2 & = \frac{1}{4} \left( \left( x + y + z \right)^2 - 54 \right) \\ & = \frac{1}{4} \left( \left( \frac{39}{4} \right)^2 - 54 \right) \\ & = \frac{657}{64} . \end{align*}
Therefore, the answer is $657 + 64 = \boxed{\textbf{(721) }}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (Vieta's Formula and Rational Root Theroem)
First, let's list the conditions: Denote by $l$ , $w$ , $h$ the length, width, and height of a rectangular box.
\[lwh=23\] \begin{align*} 2(lw+wh+hl)&=54\\ lw+wh+hl&=27. \end{align*} Applying the Pythagorean theorem, we can establish that
\begin{align*} (2r)^2&=(l^2+w^2+h^2)\\ 4r^2&=(l^2+w^2+h^2)\\ 4r^2&=(l+w+h)^2-2(lw+wh+hl)\\ 4r^2&=(l+w+h)^2-54. \end{align*}
We can spot Vieta's formula hidden inside this equation and call this $m$ . Now we have three equations:
\[lwh=23\] \[lw+wh+hl)=27\] \[l+w+h=m\]
Let there be a cubic equation. $x^3+bx^2+cx+d=0$ . Its roots are $l$ , $w$ and $h$ . We can use our formulas from before to derive $c$ and $d$ .
\[-b=l+w+h=m\]
\[c=lw+wh+lh=27\]
\[-d=lwh=23\]
We can now rewrite the equation from before:
$x^3-mx^2+27x-23=0$
To find the maximum $r$ we need the maximum $m$ . This only occurs when this equation has double roots illustrated with graph below.
WLOG we can set $h=w$ .
Thus:
\[lw+w^2+wl=27\] \[lw^2=23\]
We can substitute $l$ and form a depressed cubic equation with $w$ . \begin{align*} lw^2&=23\\ l&=\frac{23}{w^2}\\ 2\left(\frac{23}{w^2}\right)w+w^2&=27\\ \frac{46}{w}+w^2&=27\\ w^2+\frac{46}{w}-27&=0\\ w^3 -27w+46&=0. \end{align*} Based on Rational Root Theorem the possible rational roots are $\pm1, \pm2, \pm23$
A quick test reveals that $2$ is a root of the equation. Comparing coefficients we can factorize the equation into:
$(w-2)(w^2+2w-23)=0$
Besides $2$ , we derive another positive root using the quadratic formula, $2\sqrt{6}-1$ But to maximize the $m$ we need to pick the smaller $w$ , which is $2$ .
Substituting this into $l=\frac{23}{w^2}$ , we find that $l=\dfrac{23}4$ .
Applying it to our equation above: \begin{align*} 4r^2&=(l+w+h)^2-54\\ 4r^2&=(l+2w)^2-54\\ 4r^2&=\left(\dfrac{23}4+2\cdot2\right)^2-54\\ 4r^2&=\left(\dfrac{39}4\right)^2-54\\ 4r^2&=\left(\dfrac{1521}{16}\right)-54\\ 4r^2&=\left(\dfrac{657}{16}\right)\\ r^2&=\left(\dfrac{657}{64}\right). \end{align*} $657+64=\boxed{721}$ .
~ luckuso

## Solution 3a (Derivative)
to find the maximum m for $x^3-mx^2+27x-23=0$
rewrite $m$ as function of $x$ and calculate derivatives to get maximum value, \[m(x) =x + 27x^{-1} - 23x^{-2}\] \[m'(x) = 1 - 27x^{-2} -46x^{-3} = 0\] \[x^3 -27x+46=0\] \[(x-2)(x^2+2x-23)=0\]
when $x = 2$ , \[m= 2 + \frac{27}{2} - \frac{23}{4} = \frac{39}{4}\] the rest is similar to solution 3
~ luckuso

## Solution 4
This question looks complex, but once converted into a number theory problem, it becomes elementary. We know, if the dimensions are taken to be numbers in the form of coprime numbers p/q,q/r, and r, it is immediately obvious that p=23. And solving we get: \[23(r^2+q)/qr+q=27\] We know length cannot be -ve, in this case, therefore, q=4. And, again, we see: \[23/r+4+23r/4=27\] giving rise to r=2. For a cuboid inside a circle, we know:the radius is half its diagonal or, can we not say, \[r^2=(L^2+b^2+h^2)/4\] or here, \[r^2=(128+529)/64\] so here, \[p+q=657+64=721\]
~Grammaticus

## Solution 5
This problem essentially boils down to maximizing the value of $x+y+z$ (where $x$ , $y$ , and $z$ denote the dimensions of the box) given $xy+xz+yz=27$ and $xyz=23$ . After doing so, we can calculate $r^2$ using $r^2=\frac{(x+y+z)^2-54}{4}$ (as in Solution 2). We can turn $x+y+z$ into an expression in terms of only $x$ and use the method of critical points. Since $xyz=23$ , we have $yz=\frac{23}{x}$ and thus $xy+xz+yz=x(y+z)+\frac{23}{x}=27$ . Isolating $y+z$ , we find $y+z=\frac{27-\frac{23}{x}}{x}$ , so \[x+y+z=x+\frac{27-\frac{23}{x}}{x}=x+\frac{27x-23}{x^2}=x+27\cdot x^{-1}-23\cdot x^{-2}.\] We have turned $x+y+z$ into an equation in $x$ , using all conditions the problem has given us. We proceed with calculus. The maximum value of this function in $x$ is one of the critical points of this function, which can be calculated by equating the function's derivative with $0$ . Using the power rule, the derivative of $f(x)=x+27\cdot x^{-1}-23\cdot x^{-2}$ is $f'(x)=1-27\cdot x^{-2}+46\cdot x^{-3}$ . Equating $f'(x)$ to zero, we get \[1-27\cdot x^{-2}+46\cdot x^{-3}=0 \implies x^3-27x+46=0\] The roots of this can be found using the rational root theorem, yielding $x=2$ or $-1\pm 2\sqrt{6}$ . Don't forget -- $x$ must be positive, so the only possible candidates of $x$ to maximize $f(x)$ are $2$ and $2\sqrt{6}-1$ . Plugging both of them into $f(x)=x+27\cdot x^{-1}-23\cdot x^{-2}$ , we find $x=2$ yields a greater result, $\frac{39}{4}$ . Thus, the maximum value of $x+y+z=f(x)$ is $\frac{39}{4}$ . Therefore, the value of $r^2$ is \[\frac{(\frac{39}{4})^2-54}{4}=\frac{657}{64} \implies p+q=\boxed{721}.\]
~ Mathkiddie

## Solution 6 (If you don't notice that two of the side lengths have to be equal)
From the previous solutions we can see that we have to maximize $m$ in the expression $x^3 - mx^2 + 27x - 23 = 0$ such that $x^3 - mx^2 + 27x - 23 = 0$ has $3$ real and positive roots since the roots correspond to the side lengths of the rectangle. To do this we can use synthetic division to divide this expression by $(x - r)$ for some arbitrary root $r$ to try and see how $m$ relates to the roots. After doing synthetic division, we get \[(x^2 + (r - m)x + (27 + r^2 - rm) + \frac{r^3 - r^2m + 27r - 23}{x - r})(x - r) = x^3 - mx^2 + 27x - 23\] Since we defined r to be a root of the expression, it must divide into it with no remainder, meaning that $r^3-r^2m+27r-23=0$ or $m = r + \frac{27}{r} - \frac{23}{r^2}$
We can now substitute this value into $x^2 + (r-m)x + (27 + r^2 - rm)=0$ to get
$x^2 + (\frac{23}{r^2} - \frac{27}{r})x + \frac{23}{r} = 0$ .
Multiplying everything by $r^2$ yields $r^2x^2 + (23-27r)x + 23r = 0$ .
We now have to find the maximum value of $r$ for which this expression has 2 roots, since $m$ strictly increases with $r$ from our previous expression of $m = r + \frac{27}{r} - \frac{23}{r^2}$
To do this, we can find the discriminant of $r^2x^2 + (23-27r)x + 23r = 0$ and find the maximum value of $r$ for which it is positive.
The discriminant of this expression is $-92r^3 + 729r^2 - 1232r + 529$ , and after using the rational root theorem we can find $\frac{23}{4}$ as a root.
The remaining expression is $(x - \frac{23}{4})(-92x^2 + 200x - 92)$ . We can quickly see using the quadratic formula that $\frac{23}{4}$ is the largest root, meaning that $r=\frac{23}{4}$ is the largest value that a root of $x^3 - mx^2 + 27x - 23 = 0$ can have for which $x^3 - mx^2 + 27x - 23=0$ has $3$ positive, real solutions. From here, we can substitute this value back into the expression for $m$ , giving us $m = \frac{39}{4}$ . The length of the radius squared is $\frac{m^2-54}{4}=\frac{657}{64}$ and $657+64=\boxed{721}$
~Lapcas

## Video Solution 1 by OmegaLearn.org (super short)
https://youtu.be/Io5TLjC3d0U

## Video Solution 2 (constrained optimization with Lagrangian multiplier)
https://www.youtube.com/watch?v=KjEy2Ju2z8A
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution 3 by Kaguya Shinomiya (thorough analysis)
https://www.youtube.com/watch?v=mkSbqG8jly0&t=38s
~ Bloggish
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .