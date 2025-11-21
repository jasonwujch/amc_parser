# 2011 AIME I Problem 9

## Problem

Suppose $x$ is in the interval $[0, \pi/2]$ and $\log_{24\sin x} (24\cos x)=\frac{3}{2}$ . Find $24\cot^2 x$ .

## Solution 1
We can rewrite the given expression as \[\sqrt{24^3\sin^3 x}=24\cos x\] Square both sides and divide by $24^2$ to get \[24\sin ^3 x=\cos ^2 x\] Rewrite $\cos ^2 x$ as $1-\sin ^2 x$ \[24\sin ^3 x=1-\sin ^2 x\] \[24\sin ^3 x+\sin ^2 x - 1=0\] Testing values using the rational root theorem gives $\sin x=\frac{1}{3}$ as a root, $\sin^{-1} \frac{1}{3}$ does fall in the first quadrant so it satisfies the interval. There are now two ways to finish this problem.
First way: Since $\sin x=\frac{1}{3}$ , we have \[\sin ^2 x=\frac{1}{9}\] Using the Pythagorean Identity gives us $\cos ^2 x=\frac{8}{9}$ . Then we use the definition of $\cot ^2 x$ to compute our final answer. $24\cot ^2 x=24\frac{\cos ^2 x}{\sin ^2 x}=24\left(\frac{\frac{8}{9}}{\frac{1}{9}}\right)=24(8)=\boxed{192}$ .
Second way: Multiplying our old equation $24\sin ^3 x=\cos ^2 x$ by $\dfrac{24}{\sin^2x}$ gives \[576\sin x = 24\cot^2x\] So, $24\cot^2x=576\sin x=576\cdot\frac{1}{3}=\boxed{192}$ .

## Solution 2
Like Solution 1, we can rewrite the given expression as \[24\sin^3x=\cos^2x\] Divide both sides by $\sin^3x$ . \[24 = \cot^2x\csc x\] Square both sides. \[576 = \cot^4x\csc^2x\] Substitute the identity $\csc^2x = \cot^2x + 1$ . \[576 = \cot^4x(\cot^2x + 1)\] Let $a = \cot^2x$ . Then \[576 = a^3 + a^2\] . Since $\sqrt[3]{576} \approx 8$ , we can easily see that $a = 8$ is a solution. Thus, the answer is $24\cot^2x = 24a = 24 \cdot 8 = \boxed{192}$ .

## Video Solution
https://youtu.be/SXwcmdgoQpk
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .