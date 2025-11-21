# 2013 AIME II Problem 12

## Problem

Let $S$ be the set of all polynomials of the form $z^3 + az^2 + bz + c$ , where $a$ , $b$ , and $c$ are integers. Find the number of polynomials in $S$ such that each of its roots $z$ satisfies either $|z| = 20$ or $|z| = 13$ .

## Solution 1
Every cubic with real coefficients has to have either three real roots or one real and two nonreal roots which are conjugates. This follows from Vieta's formulas .
- Case 1: $f(z)=(z-r)(z-\omega)(z-\omega^*)$ , where $r\in \mathbb{R}$ , $\omega$ is nonreal, and $\omega^*$ is the complex conjugate of omega (note that we may assume that $\Im(\omega)>0$ ).
The real root $r$ must be one of $-20$ , $20$ , $-13$ , or $13$ . By Viète's formulas, $a=-(r+\omega+\omega^*)$ , $b=|\omega|^2+r(\omega+\omega^*)$ , and $c=-r|\omega|^2$ . But $\omega+\omega^*=2\Re{(\omega)}$ (i.e., adding the conjugates cancels the imaginary part). Therefore, to make $a$ an integer, $2\Re{(\omega)}$ must be an integer. Conversely, if $\omega+\omega^*=2\Re{(\omega)}$ is an integer, then $a,b,$ and $c$ are clearly integers. Therefore $2\Re{(\omega)}\in \mathbb{Z}$ is equivalent to the desired property. Let $\omega=\alpha+i\beta$ .
- Subcase 1.1: $|\omega|=20$ .
In this case, $\omega$ lies on a circle of radius $20$ in the complex plane. As $\omega$ is nonreal, we see that $\beta\ne 0$ . Hence $-20<\Re{(\omega)}< 20$ , or rather $-40<2\Re{(\omega)}< 40$ . We count $79$ integers in this interval, each of which corresponds to a unique complex number on the circle of radius $20$ with positive imaginary part.
- Subcase 1.2: $|\omega|=13$ .
In this case, $\omega$ lies on a circle of radius $13$ in the complex plane. As $\omega$ is nonreal, we see that $\beta\ne 0$ . Hence $-13<\Re{(\omega)}< 13$ , or rather $-26<2\Re{(\omega)}< 26$ . We count $51$ integers in this interval, each of which corresponds to a unique complex number on the circle of radius $13$ with positive imaginary part.
Therefore, there are $79+51=130$ choices for $\omega$ . We also have $4$ choices for $r$ , hence there are $4\cdot 130=520$ total polynomials in this case.
- Case 2: $f(z)=(z-r_1)(z-r_2)(z-r_3)$ , where $r_1,r_2,r_3$ are all real.
In this case, there are four possible real roots, namely $\pm 13, \pm20$ . Let $p$ be the number of times that $13$ appears among $r_1,r_2,r_3$ , and define $q,r,s$ similarly for $-13,20$ , and $-20$ , respectively. Then $p+q+r+s=3$ because there are three roots. We wish to find the number of ways to choose nonnegative integers $p,q,r,s$ that satisfy that equation. By balls and urns, these can be chosen in $\binom{6}{3}=20$ ways.
Therefore, there are a total of $520+20=\boxed{540}$ polynomials with the desired property.

## Solution 2 (Systematics)
This combinatorics problem involves counting, and casework is most appropriate. There are two cases: either all three roots are real, or one is real and there are two imaginary roots.
Case 1: Three roots are of the set ${13, -13, 20, -20}$ . By stars and bars, there is $\binom{6}{3}=20$ ways (3 bars between all four possibilities, and then 3 stars that represent the roots themselves).
Case 2: One real root: one of $13, -13, 20, -20$ . Then two imaginary roots left; it is well known that because coefficients of the polynomial are integral (and thus not imaginary), these roots are conjugates. Therefore, either both roots have a norm (also called magnitude) of $20$ or $13$ . Call the root $a+bi$ , where $a$ is not the magnitude of the root; otherwise, it would be case 1. We need integral coefficients: expansion of $(x-(a+bi))(x-(a-bi))=-2ax+x^2+(a^2+b^2)$ tells us that we just need $2a$ to be integral, because $a^2+b^2$ IS the norm of the root! (Note that it is not necessary to multiply by the real root. That won't affect whether or not a coefficient is imaginary.) Therefore, when the norm is $20$ , the $a$ term can range from $-19.5, -19, ...., 0, 0.5, ..., 19.5$ or $79$ solutions. When the norm is $13$ , the $a$ term has $51$ possibilities from $-12.5, -12, ..., 12.5$ . In total that's 130 total ways to choose the imaginary root. Now, multiply by the ways to choose the real root, $4$ , and you get $520$ for this case.
And $520+20=540$ and we are done.

## Solution 3 (Comments)
If the polynomial has one real root and two complex roots, then it can be factored as $(z-r)(z^2+pz+q),$ where $r$ is real with $|r|=13,20$ and $p,q$ are integers with $p^2 <4q.$ The roots $z_1$ and $z_2$ are conjugates. We have $|z_1|^2=|z_2|^2=z_1z_2=q.$ So $q$ is either $20^2$ or $13^2$ . The only requirement for $p$ is $p<\sqrt{4q^2}=2q.$ All such quadratic equations are listed as follows:
$z^2+pz+20^2,$ where $p=0,\pm1,\pm2,\cdots,\pm 39,$
$z^2+pz+13^2,$ where $p=0,\pm1,\pm2,\cdots,\pm 25$ .
Total of 130 equations, multiplied by 4 (the number of cases for real $r$ , we have 520 equations, as indicated in the solution.
-JZ

## Solution 4
There are two cases: either all the roots are real, or one is real and two are imaginary.
Case 1: All roots are real. Then each of the roots is a member of the set $\{-20, 20, -13, 13\}$ . It splits into three sub-cases: either no two are the same, exactly two are the same, or all three are the same.
Sub-case 1.1: No two are the same. This is obviously $\dbinom{4}{3}=4$ .
Sub-case 1.2: Exactly two are the same. There are four ways to choose the root that will repeat twice, and three ways to choose the remaining root. For this sub-case, $4\cdot 3=12$ .
Sub-case 1.3: All three are the same. This is obviously $4$ .
Thus for case one, we have $4+12+4=20$ polynomials in $S$ . We now have case two, which we state below.
Case 2: Two roots are imaginary and one is real. Let these roots be $p-qi$ , $p+qi$ , and $r$ . Then by Vieta's formulas
- $-(2p+r)=a$ ;
- $p^{2}+q^{2}+2pr=b$ ;
- $-\left(p^{2}+q^{2}\right)r=c$ .
Since $a$ , $b$ , $c$ , and $r$ are integers, we have that $p=\frac{1}{2}k$ for some integer $k$ . Case two splits into two sub-cases now:
Sub-case 2.1: $|p-qi|=|p+qi|=13$ . Obviously, $|p|<13$ . The $51$ cases in which $p$ is either $0,\pm\frac{1}{2},\pm\frac{2}{2},\pm\frac{3}{2},\ldots,\pm\frac{25}{2}$ are acceptable. Each can pair with one value of $q$ and four values of $r$ , adding $51\cdot 4=204$ polynomials to $S$ .
Sub-case 2.2: $|p-qi|=|p+qi|=20$ . Obviously, $|p|<20$ . Here, the $79$ cases in which $p$ is either $0,\pm\frac{1}{2},\pm\frac{2}{2},\pm\frac{3}{2},\ldots,\pm\frac{39}{2}$ are acceptable. Again, each can pair with a single value of $q$ as well as four values of $r$ , adding $79\cdot 4=316$ polynomials to $S$ .
Thus for case two, $204+316=520$ polynomials are part of $S$ .
All in all, $20+204+316=\boxed{540}$ polynomials can call $S$ home.

## Video Solution
https://youtu.be/-U65hhr1Smw?si=2JfRYL032MhUe276
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .