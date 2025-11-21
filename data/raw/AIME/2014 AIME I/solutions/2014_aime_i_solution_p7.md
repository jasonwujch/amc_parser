# 2014 AIME I Problem 7

## Problem

Let $w$ and $z$ be complex numbers such that $|w| = 1$ and $|z| = 10$ . Let $\theta = \arg \left(\tfrac{w-z}{z}\right)$ . The maximum possible value of $\tan^2 \theta$ can be written as $\tfrac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ . (Note that $\arg(w)$ , for $w \neq 0$ , denotes the measure of the angle that the ray from $0$ to $w$ makes with the positive real axis in the complex plane)

## Solution 1
Let $w = \operatorname{cis}{(\alpha)}$ and $z = 10\operatorname{cis}{(\beta)}$ . Then, $\dfrac{w - z}{z} = \dfrac{\operatorname{cis}{(\alpha)} - 10\operatorname{cis}{(\beta)}}{10\operatorname{cis}{\beta}}$ .
Multiplying both the numerator and denominator of this fraction by $\operatorname{cis}{(-\beta)}$ gives us:
$\dfrac{w - z}{z} = \dfrac{1}{10}\operatorname{cis}{(\alpha - \beta)} - 1 = \dfrac{1}{10}\cos{(\alpha - \beta)} + \dfrac{1}{10}i\sin{(\alpha - \beta)} - 1$ .
We know that $\tan{\theta}$ is equal to the imaginary part of the above expression divided by the real part. Let $x = \alpha - \beta$ . Then, we have that:
$\tan{\theta} = \dfrac{\sin{x}}{\cos{x} - 10}.$
We need to find a maximum of this expression, so we take the derivative:
Note (not from author): To take the derivative, we need to use the Quotient Rule . In this case, \[\frac{d}{dx}\left(\frac{\sin x}{\cos x-10}\right)=\frac{\cos x(\cos x-10)-(-\sin x)\sin x}{(\cos x-10)^2}=\dfrac{1 - 10\cos{x}}{(\cos{x} - 10)^2}\]
Thus, we see that the maximum occurs when $\cos{x} = \dfrac{1}{10}$ . Therefore, $\sin{x} = \pm\dfrac{\sqrt{99}}{10}$ , and $\tan{\theta} = \pm\dfrac{\sqrt{99}}{99}$ . Thus, the maximum value of $\tan^2{\theta}$ is $\dfrac{99}{99^2}$ , or $\dfrac{1}{99}$ , and our answer is $1 + 99 = \boxed{100}$ .

## Solution 2
Without the loss of generality one can let $z$ lie on the positive x axis and since $arg(\theta)$ is a measure of the angle if $z=10$ then $arg(\dfrac{w-z}{z})=arg(w-z)$ and we can see that the question is equivalent to having a triangle $OAB$ with sides $OA =10$ $AB=1$ and $OB=t$ and trying to maximize the angle $BOA$ [asy] pair O = (0,0); pair A = (100,0); pair B = (80,30); pair D = (sqrt(850),sqrt(850)); draw(A--B--O--cycle); dotfactor = 3; dot("$A$",A,dir(45)); dot("$B$",B,dir(45)); dot("$O$",O,dir(135)); dot("$ \theta$",O,(7,1.2)); label("$1$", ( A--B )); label("$10$",(O--A)); label("$t$",(O--B)); [/asy]
using the Law of Cosines we get: $1^2=10^2+t^2-t*10*2\cos\theta$ rearranging: \[20t\cos\theta=t^2+99\] solving for $\cos\theta$ we get:
\[\frac{99}{20t}+\frac{t}{20}=\cos\theta\] if we want to maximize $\theta$ we need to minimize $\cos\theta$ , using AM-GM inequality we get that the minimum value for $\cos\theta= 2\left(\sqrt{\dfrac{99}{20t}\dfrac{t}{20}}\right)=2\sqrt{\dfrac{99}{400}}=\dfrac{\sqrt{99}}{10}$ hence using the identity $\tan^2\theta=\sec^2\theta-1$ we get $\tan^2\theta=\frac{1}{99}$ and our answer is $1 + 99 = \boxed{100}$ .
Note : You can also realize that the max $\theta$ is when the line from $0$ is tangent to the circle of radius $1$ centered at $10.$

## Solution 3
Note that $\frac{w-z}{z}=\frac{w}{z}-1$ , and that $\left|\frac{w}{z}\right|=\frac{1}{10}$ . Thus $\frac{w}{z}-1$ is a complex number on the circle with radius $\frac{1}{10}$ and centered at $-1$ on the complex plane. Let $\omega$ denote this circle.
Let $A$ and $C$ be the points that represent $\frac{w}{z}-1$ and $-1$ respectively on the complex plane. Let $O$ be the origin. In order to maximize $\tan^2(\theta)$ , we need to maximize $\angle{AOC}$ . This angle is maximized when $AO$ is tangent to $\omega$ . Using the Pythagorean Theorem, we get
\[AO^2=1^2-\left(\frac{1}{10}\right)^2=\frac{99}{100}\]
Thus
\[\tan^2(\theta)=\frac{AC^2}{AO^2}=\frac{1/100}{99/100}=\frac{1}{99}\]
And the answer is $1+99=\boxed{100}$ .

## Video Solution by Punxsutawney Phil
https://www.youtube.com/watch?v=yakhEuPy6Sg
~sugar_rush
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .