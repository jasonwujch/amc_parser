# 2002 AIME II Problem 10

## Problem

While finding the sine of a certain angle, an absent-minded professor failed to notice that his calculator was not in the correct angular mode. He was lucky to get the right answer. The two least positive real values of $x$ for which the sine of $x$ degrees is the same as the sine of $x$ radians are $\frac{m\pi}{n-\pi}$ and $\frac{p\pi}{q+\pi}$ , where $m$ , $n$ , $p$ , and $q$ are positive integers. Find $m+n+p+q$ .

## Solution 1
Note that $x$ degrees is equal to $\frac{\pi x}{180}$ radians. Also, for $\alpha \in \left[0 , \frac{\pi}{2} \right]$ , the two least positive angles $\theta > \alpha$ such that $\sin{\theta} = \sin{\alpha}$ are $\theta = \pi-\alpha$ , and $\theta = 2\pi + \alpha$ .
Clearly $x > \frac{\pi x}{180}$ for positive real values of $x$ .
$\theta = \pi-\alpha$ yields: $x = \pi - \frac{\pi x}{180} \Rightarrow x = \frac{180\pi}{180+\pi} \Rightarrow (p,q) = (180,180)$ .
$\theta = 2\pi + \alpha$ yields: $x = 2\pi + \frac{\pi x}{180} \Rightarrow x = \frac{360\pi}{180-\pi} \Rightarrow (m,n) = (360,180)$ .
So, $m+n+p+q = \boxed{900}$ .

## Solution 2
The first case is when the two angles, $x$ and $\frac{\pi x}{180}$ , are coterminal. The second case is when they are reflections of the $y$ axis.
1. $x+2\pi a = \frac{\pi x}{180}$ for any integer $a$ So $x=\frac{360\pi a }{\pi -180}$
2. $(2b+1)\pi -x = \frac{\pi x}{180}$ for any integer $b$ So $x = \frac{180(2b+1)\pi}{\pi + 180}$
Choosing carefully $a,b$ such that it's the minimum gives the answer same as above.
These problems are copyrighted © by the Mathematical Association of America.