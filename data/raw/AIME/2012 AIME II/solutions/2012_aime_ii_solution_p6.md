# 2012 AIME II Problem 6

## Problem

Let $z=a+bi$ be the complex number with $\vert z \vert = 5$ and $b > 0$ such that the distance between $(1+2i)z^3$ and $z^5$ is maximized, and let $z^4 = c+di$ . Find $c+d$ .

## Solution
Let's consider the maximization constraint first: we want to maximize the value of $|z^5 - (1+2i)z^3|$ Simplifying, we have
$|z^3| * |z^2 - (1+2i)|$
$=|z|^3 * |z^2 - (1+2i)|$
$=125|z^2 - (1+2i)|$
Thus we only need to maximize the value of $|z^2 - (1+2i)|$ .
To maximize this value, we must have that $z^2$ is in the opposite direction of $1+2i$ . The unit vector in the complex plane in the desired direction is $\frac{-1}{\sqrt{5}} + \frac{-2}{\sqrt{5}} i$ . Furthermore, we know that the magnitude of $z^2$ is $25$ , because the magnitude of $z$ is $5$ . From this information, we can find that $z^2 = \sqrt{5} (-5 - 10i)$
Squaring, we get $z^4 = 5 (25 - 100 + 100i) = -375 + 500i$ . Finally, $c+d = -375 + 500 = \boxed{125}$

## Solution 2
WLOG, let $z_{1}=5(\cos{\theta_{1}}+i\sin{\theta_{1}})$ and
$z_{2}=1+2i=\sqrt{5}(\cos{\theta_{2}+i\sin{\theta_{2}}})$
This means that
$z_{1}^3=125(\cos{3\theta_{1}}+i\sin{3\theta_{1}})$
$z_{1}^4=625(\cos{4\theta_{1}}+i\sin{4\theta_{1}})$
Hence, this means that
$z_{2}z_{1}^3=125\sqrt{5}(\cos({\theta_{2}+3\theta_{1}})+i\sin({\theta_{2}+3\theta_{1}}))$
And
$z_{1}^5=3125(\cos{5\theta_{1}}+i\sin{5\theta_{1}})$
Now, common sense tells us that the distance between these two complex numbers is maxed when they both are points satisfying the equation of the line $yi=mx$ , or when they are each a $180^{\circ}$ rotation away from each other.
Hence, we must have that $5\theta_{1}=3\theta_{1}+\theta_{2}+180^{\circ}\implies\theta_{1}=\frac{\theta_{2}+180^{\circ}}{2}$
Now, plug this back into $z_{1}^4$ (if you want to know why, reread what we want in the problem!)
So now, we have that $z_{1}^4=625(\cos{2\theta_{2}}+i\sin{2\theta_{2}})$
Notice that $\cos\theta_{2}=\frac{1}{\sqrt{5}}$ and $\sin\theta_{2}=\frac{2}{\sqrt{5}}$
Then, we have that $\cos{2\theta_{2}}=\cos^2{\theta_{2}}-\sin^2{\theta_{2}}=-\frac{3}{5}$ and $\sin{2\theta_{2}}=2\sin{\theta_{2}}\cos{\theta_{2}}=\frac{4}{5}$
Finally, plugging back in, we find that $z_{1}^4=625(-\frac{3}{5}+\frac{4i}{5})=-375+500i$
$-375+500=\boxed{125}$

## Solution 3
Clearly, we want $\arg((1+2i)z^3) = \pi + \arg(z^5)$ . This is equivalent to $\arg(1+2i) = \pi + 2 \arg(z)$ by the additive property of the argument in complex multiplication. Because we want to find $z^4$ , we want an expression for $\arg(z^4)$ . We now have $2\arg(1+2i) = 2\pi + 4 \arg(z) \rightarrow \arg(-3+4i) = 4\arg(z)$ . Thus, $z^4$ is in the direction of $-3 + 4i$ . To achieve a magnitude of 5^4, we need to multiple $-3+4i$ by 125, so $z^4 = 125(-3+4i)$ and the answer is thus $\boxed{125}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .