# 2011 AIME II Problem 8

## Problem

Let $z_1,z_2,z_3,\dots,z_{12}$ be the 12 zeroes of the polynomial $z^{12}-2^{36}$ . For each $j$ , let $w_j$ be one of $z_j$ or $i z_j$ . Then the maximum possible value of the real part of $\sum_{j=1}^{12} w_j$ can be written as $m+\sqrt{n}$ where $m$ and $n$ are positive integers. Find $m+n$ .

## Solution
The twelve dots above represent the $12$ roots of the equation $z^{12}-2^{36}=0$ . If we write $z=a+bi$ , then the real part of $z$ is $a$ and the real part of $iz$ is $-b$ . The blue dots represent those roots $z$ for which the real part of $z$ is greater than the real part of $iz$ , and the red dots represent those roots $z$ for which the real part of $iz$ is greater than the real part of $z$ . Now, the sum of the real parts of the blue dots is easily seen to be $8+16\cos\frac{\pi}{6}=8+8\sqrt{3}$ and the negative of the sum of the imaginary parts of the red dots is easily seen to also be $8+8\sqrt{3}$ . Hence our desired sum is $16+16\sqrt{3}=16+\sqrt{768}$ , giving the answer $\boxed{784}.$

## Solution
As a small note, we could factor the equation as $z^{12} = 2^{36} \implies (\frac{z}{8})^{12} = 1$ in which these are just the 12th roots of unity for $\frac{z}{8}$ which might be easier to work with. Then we just add up the optimal real parts as in solution 1 and then multiply by 8 at the end.

## Solution
Note that $\sin(x) = \sin(x + \pi/2 - \pi/2) = -\cos(x + \pi/2)$ . When summing the real part of $8i(\cos(x) + i\sin(x))$ is $-8\sin(x) = 8\cos(x + \pi/2)$ .
So, translate all the red dots by $90^{\circ}$ and sum the cosines of angles of the blue and (rotated) red dots.
Then, it's easy to see that points 2, 3, and 4 cancel out with 5, 6, and 7, so you're left with $8 \cdot (\cos \pi/6 + \cos -\pi/6 + \cos 0)$ times two ~ CrazyVideoGamez

## Solution 2
The equation $z^{12}-2^{36}=0$ can be factored as follows: \[(z^6-2^{18})(z^6+2^{18})=0\] \[(z^2-2^6)(z^2+2^6)({(z^2+2^6)}^2-z^2\cdot2^6)({(z^2-2^6)}^2+z^2\cdot2^6)=0\] \[(z^2-2^6)(z^2+2^6)(z^2+2^6-z\cdot2^3)(z^2+2^6+z\cdot2^3) (z^2-2^6-iz\cdot2^3)(z^2-2^6+i z\cdot2^3)=0\]
Since this is a 12th degree equation, there are 12 roots. Also, since each term in the equation is even, the positive or negative value of each root is another root. That would mean there are 6 roots that can be multiplied by $-1$ and since we have 6 factors, that’s 1 root per factor. We just need to solve for $z$ in each factor and pick whether or not to multiply by $i$ and $-1$ for each one depending on the one that yields the highest real value. After that process, we get $8+8+2((4\sqrt{3}+4)+(4\sqrt{3}-4))$ Adding the values up yields $16+16\sqrt{3}$ , or $16+\sqrt{768}$ , and $16+768=\boxed{784}$ .
-Solution by Someonenumber011.

## Solution 3
Clearly, the roots are: $2^3*(\cos{\frac{k\pi}{12}}+i\sin{\frac{k\pi}{12}}), k\in{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}$ .
Now, realize for $z=a+bi$ , $\operatorname{Re}(iz)=-b$ . $\operatorname{Re}(z)=a$ . $\operatorname{Re}(z)<\operatorname{Re}(iz)$ is true when $a<-b$ .
This means:
When $a>0$ , $b<-a<0$ .
When $a<0$ , $0<b<-a$ .
For the 12 roots of the polynomial in the original equation, $8\cos{k\pi/12}=\operatorname{Re}(z), k\in{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}$ . $-8\sin{k\pi/12}=\operatorname{Im}(iz), k\in{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}$ .
So $8\cos{k\pi/12}<-8\sin{k\pi/12}$ . $-\cos{k\pi/12}>\sin{k\pi/12}$ . This can be easily true for roots that are in the 3rd quadrant in the complex plane.
This cannot be true for roots in the 1st quadrant because that would yield a negative number bigger than a positive one.
Consider the roots in the 2nd and 4th quadrants. Calculate the roots, choose, and then add the ones up. You will get $\boxed{784}$ .
~hastapasta

## Solution 4 (Brute Force)
Use De Moivre's Theorem to brute force all the roots out. Then choose the greater value of $\operatorname{Re}(z), \operatorname{Re}(iz)$ . After adding everything up, you get $\boxed{784}$ .
~hastapasta
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .