# 2000 AIME II Problem 6

## Problem

One base of a trapezoid is $100$ units longer than the other base. The segment that joins the midpoints of the legs divides the trapezoid into two regions whose areas are in the ratio $2: 3$ . Let $x$ be the length of the segment joining the legs of the trapezoid that is parallel to the bases and that divides the trapezoid into two regions of equal area. Find the greatest integer that does not exceed $x^2/100$ .

## Solution
Let the shorter base have length $b$ (so the longer has length $b+100$ ), and let the height be $h$ . The length of the midline of the trapezoid is the average of its bases, which is $\frac{b+b+100}{2} = b+50$ . The two regions which the midline divides the trapezoid into are two smaller trapezoids, both with height $h/2$ . Then,
\[\frac{\frac 12 (h/2) (b + b+50)}{\frac 12 (h/2) (b + 50 + b + 100)} = \frac{2}{3} \Longrightarrow \frac{b + 75}{b + 25} = \frac 32 \Longrightarrow b = 75\]
Construct the perpendiculars from the vertices of the shorter base to the longer base. This splits the trapezoid into a rectangle and two triangles; it also splits the desired line segment into three partitions with lengths $x_1, 75, x_2$ . By similar triangles, we easily find that $\frac{x - 75}{100} = \frac{x_1+x_2}{100} = \frac{h_1}{h}$ .
The area of the region including the shorter base must be half of the area of the entire trapezoid, so
\[2 \cdot \frac 12 h_1 (75 + x) = \frac 12 h (75 + 175) \Longrightarrow x = 125 \cdot \frac{h}{h_1} - 75\]
Substituting our expression for $\frac h{h_1}$ from above, we find that
\[x = \frac{12500}{x-75} - 75 \Longrightarrow x^2 - 75x = 5625 + 12500 - 75x \Longrightarrow x^2 = 18125\]
The answer is $\left\lfloor\frac{x^2}{100}\right\rfloor = \boxed{181}$ .
These problems are copyrighted © by the Mathematical Association of America.