# 2009 AMC 10A Problem 6

## Problem

A circle of radius $2$ is inscribed in a semicircle, as shown. The area inside the semicircle but outside the circle is shaded. What fraction of the semicircle's area is shaded?

[asy] unitsize(6mm); defaultpen(linewidth(.8pt)+fontsize(8pt)); dotfactor=4; filldraw(Arc((0,0),4,0,180)--cycle,gray,black); filldraw(Circle((0,2),2),white,black); dot((0,2)); draw((0,2)--((0,2)+2*dir(60))); label("$2$",midpoint((0,2)--((0,2)+2*dir(60))),SE); [/asy]

$\mathrm{(A)}\ \frac{1}{2} \qquad \mathrm{(B)}\ \frac{\pi}{6} \qquad \mathrm{(C)}\ \frac{2}{\pi} \qquad \mathrm{(D)}\ \frac{2}{3} \qquad \mathrm{(E)}\ \frac{3}{\pi}$

## Solution
Area of the circle inscribed inside the semicircle $= \pi r^2 \Rightarrow \pi(2^2) = 4 \pi .$ Area of the larger circle (semicircle's area x 2) $= \pi r^2 \Rightarrow \pi(4^2)= 16 \pi$ (4, or the diameter of the inscribed circle is the same thing as the radius of the semicircle). Thus, the area of the semicircle is $\frac{1}{2}(16 \pi) \Rightarrow 8 \pi .$ Part of the semicircle that is unshaded is $\frac{4 \pi}{8 \pi} = \frac{1}{2}$ Therefore, the shaded part is $1 - \frac{1}{2} = \frac{1}{2}$
Thus the answer is $\frac{1}{2}\Rightarrow \fbox{A}$

## Solution
The solution above is the standard method of solving it, but we can also realize something about their radii. If we see, we know that the smaller circle has a radius of $2$ while the larger semicircle has a radius of $4$ . We know for a fact that if we have $2$ normal full circles and one has a radius that is double the other, the smaller circle will always be $4$ times smaller than the larger one (if you didn't know, now you know). Now, we have a semicircle, so the same thing applies but the larger circle is cut in half, so therefore, the semicircle (which has the bigger radius), will be double the size of the small circle that is inscribed in it. Double means that $2$ of the small full circles will be able to fit the larger semi-circle. So, therefore, the area that is shaded is equal to the area of the small full circle, making $2$ equal parts, so the shaded area is $\frac{1}{2}$ of the whole semi-circle
$\frac{1}{2}\Longrightarrow \fbox{A}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .