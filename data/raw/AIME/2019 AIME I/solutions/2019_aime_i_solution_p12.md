# 2019 AIME I Problem 12

## Problem

Given $f(z) = z^2-19z$ , there are complex numbers $z$ with the property that $z$ , $f(z)$ , and $f(f(z))$ are the vertices of a right triangle in the complex plane with a right angle at $f(z)$ . There are positive integers $m$ and $n$ such that one such value of $z$ is $m+\sqrt{n}+11i$ . Find $m+n$ .

## Solution 1
Notice that we must have \[\frac{f(f(z))-f(z)}{f(z)-z}=-\frac{f(f(z))-f(z)}{z-f(z)}\in i\mathbb R .\] However, $f(t)-t=t(t-20)$ , so \begin{align*} \frac{f(f(z))-f(z)}{f(z)-z}&=\frac{(z^2-19z)(z^2-19z-20)}{z(z-20)}\\ &=\frac{z(z-19)(z-20)(z+1)}{z(z-20)}\\ &=(z-19)(z+1)\\ &=(z-9)^2-100. \end{align*} Then, the real part of $(z-9)^2$ is $100$ . Since $\text{Im}(z-9)=\text{Im}(z)=11$ , let $z-9=a+11i$ . Then, \[100=\text{Re}((a+11i)^2)=a^2-121\implies a=\pm\sqrt{221}.\] It follows that $z=9+\sqrt{221}+11i$ , and the requested sum is $9+221=\boxed{230}$ .
(Solution by TheUltimate123)

## Solution 2
We will use the fact that segments $AB$ and $BC$ are perpendicular in the complex plane if and only if $\frac{a-b}{b-c}\in i\mathbb{R}$ . To prove this, note that when dividing two complex numbers you subtract the angle of one from the other. Therefore, if the two complex numbers are perpendicular, the difference between their arguments will be 90 degrees, so subtracting the angles will yield an imaginary number with no real part(an argument of 90 degrees puts a complex number on the imaginary axis).
Now to apply this: \[\frac{f(z)-z}{f(f(z))-f(z)}\in i\mathbb{R}\] \[\frac{z^2-19z-z}{(z^2-19z)^2-19(z^2-19z)-(z^2-19z)}\] \[\frac{z^2-20z}{z^4-38z^3+341z^2+380z}\] \[\frac{z(z-20)}{z(z+1)(z-19)(z-20)}\] \[\frac{1}{(z+1)(z-19)}\in i\mathbb{R}\]
The factorization of the nasty denominator above is made easier with the intuition that $(z-20)$ must be a divisor for the problem to lead anywhere. Now we know $(z+1)(z-19)\in i\mathbb{R}$ so using the fact that the imaginary part of $z$ is $11i$ and calling the real part r,
\[(r+1+11i)(r-19+11i)\in i\mathbb{R}\] \[r^2-18r-140=0\]
solving the above quadratic yields $r=9+\sqrt{221}$ so our answer is $9+221=\boxed{230}$

## Solution 3
I would like to use a famous method, namely the coni method.
According to the question given, we can assume , $A= f(f(z)),B=f(z),C= z$ respectively.
WLOG, $Z_1= \frac{f(f(z))-f(z)}{z-f(z)}$ . According to the question $\arg{Z_1}=\frac{\pi}{2}$ .
So, $\Re (Z_1)=0$ .
Now, $Z_1=\frac{z(z-19)(z+1)(z-20)}{-z(z-20)}$ .
$\implies Z_1= -(z^2-18z-19)$ . WLOG, $z=a+11i$ .where $a=m+\sqrt{n}$ .
So, $\Re (Z_1)= -(a^2-18a-140)$ . Solving, $a^2-18a-140=0$ .get ,
$a=9$ ± $\sqrt{221}$ . So, possible value of $a=9+\sqrt{221}$ .
$m+n=\boxed{230}$ . ~ftheftics.
### Proof of this method
Note that if we translate a triangle, the measures of all of its angles stay the same. So we can translate $ABC$ on the complex plane so that $B=0$ . Let the images of $A, B, C$ be $A', B', C'$ respectively. Then, we can use the formula:
\[re^{i\theta}=r\cos(\theta)+i \cdot r\sin(\theta)\] (This is known as Euler's Formula.)
Using Euler's formula (represent each complex number in polar form, then use exponent identities), we can show that \[\text{arg}(\frac{A'}{C'})=\text{arg}(A')-\text{arg}(C')=\angle(A'B'C')=\angle(ABC)\] So this method is valid. ~Math4Life2020

## Solution 4
It is well known that $AB$ is perpendicular to $CD$ iff $\frac{d-c}{b-a}$ is a pure imaginary number. Here, we have that $A=z$ , $B,C=f(z)$ , and $D=f(f(z))$ . This means that this is equivalent to $\frac{f(f(z))-f(z)}{f(z)-z}$ being a pure imaginary number. Plugging in $f(z)=z^2-19z$ , we have that $\frac{(z^2-19z)-19(z^2-19z)-(z^2-19z)}{z^2-19z-z}$ being pure imaginary. Factoring and simplifying, we find that this is simply equivalent to $(z-19)(z+1)$ being pure imaginary. We let $z=a+bi$ , so this is equivalent to $(a+bi-19)(a+bi+1)$ being pure imaginary. Expanding the product, this is equivalent to $a^2+abi+a+abi-b^2+bi-19a-19bi-19$ being pure imaginary. Taking the real part of this, and setting this equal to $0$ , we have that $a^2-18a-b^2-19=0$ . Since $b=11$ , we have that $a^2-18a-140=0$ . By the quadratic formula, $a=9 \pm \sqrt{221}$ , and taking the positive root gives that $a=9+ \sqrt{221}$ , so the answer is $9+221=230$
~smartninja2000

## Solution 5 (Official MAA)
The arguments of the two complex numbers differ by $90^\circ$ if the ratio of the numbers is a pure imaginary number. Thus three distinct complex numbers $A,\,B,$ and $C$ form a right triangle at $B$ if and only if $\tfrac{C-B}{B-A}$ has real part equal to $0.$ Hence \begin{align*} \frac{f(f(z))-f(z)}{f(z)-z}&=\frac{(z^2-19z)^2-19(z^2-19z)-(z^2-19z)}{(z^2-19z)-z}\\ &=\frac{(z^2-19z)(z^2-19z-19-1)}{z^2-20z}\\ &=\frac{z(z-19)(z+1)(z-20)}{z(z-20)} \\ &=z^2-18z-19 \end{align*} must have real part equal to $0.$ If $z=x+11i,$ the real part of $z^2-18z-19$ is $x^2-11^2-18x-19,$ which is $0$ when $x=9\pm\sqrt{221}.$ The requested sum is $9+221=\boxed{230}.$

## Solution 6 (Dot product)
Firstly, the angle between the three complex numbers is equivalent to the angle between $f(z)-z,0,$ and $f(f(z))-f(z)$ .
Using $f(z)=z(z-19)$ to help expand,
$z-f(z)=20z-z^2$ and $f(f(z))-f(z)=(z^2-19z)(z^2-19z-19)-(z^2-19z)$ .
The second equation can be rewritten as $(z^2-19z)(z^2-19z-20)=z(z-19)(z-20)(z+1)$
Note that the angle between $(a+bi), 0,$ and $(a+bi)(c+di)$ is the same as the angle between $1, 0,$ and $c+di$ . The proof of this is as follows:
Treating the complex numbers like vectors (e.g. $a+bi$ turns into $\left[\begin{array}{c} a \\ b \end{array}\right]$ ) we have $cos \theta = \frac{a \cdot (ac-bd) + b \cdot (ad+bc)}{2\sqrt{a^2+b^2}\sqrt{a^2+b^2}\sqrt{c^2+d^2}}$
$cos \theta = \frac{a^2 c - abd + abd + b^2 c}{2(a^2+b^2)\sqrt{c^2+d^2}}$
$cos \theta = \frac{(a^2+b^2)c}{2(a^2+b^2)\sqrt{c^2+d^2}}=\frac{c}{2\sqrt{c^2+d^2}}$ .
Using the dot product formula for the cosine of the angle between the other two vectors (1, c + di) we get the same result. Thus, it is proven.
Now, we see that the three resulting complex numbers have the same angle as $-1,0,$ and $(z-19)(z+1)$ as a factor of $z(z-20)$ can be taken out of both expressions. Note that the value of $z$ clearly is not 0, nor is it 20 as it has a value of $11i$ .
Expanding $z^2-18z-19$ with $z=a+11i$ yields
$a^2-121+22ai-18a-198i-19=a^2-18a-140+22ai-198i$ . Turning these into vectors again, the resulting relation is
$cos(90^\circ)=0=\frac{-(a^2-18a-140)}{2\sqrt{(a^2-18a-140)^2 + (22a-198)^2} \cdot 1}$
In order for this thing to be 0, the numerator must be 0, so setting it equal to 0 yields
$a^2-18a-140=0 \Rightarrow a=9\pm \sqrt{81+140}$ . Neither of these make the denominator in the $cos(90^\circ)$ expression 0, so they are valid. The requested result is the positive root, so the answer is $\boxed{230}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .