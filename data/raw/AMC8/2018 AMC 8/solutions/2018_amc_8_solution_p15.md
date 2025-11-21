# 2018 AMC 8 Problem 15

## Problem

In the diagram below, a diameter of each of the two smaller circles is a radius of the larger circle. If the two smaller circles have a combined area of $1$ square unit, then what is the area of the shaded region, in square units?

[asy] size(4cm); filldraw(scale(2)*unitcircle,gray,black); filldraw(shift(-1,0)*unitcircle,white,black); filldraw(shift(1,0)*unitcircle,white,black); [/asy]

$\textbf{(A) } \frac{1}{4} \qquad \textbf{(B) } \frac{1}{3} \qquad \textbf{(C) } \frac{1}{2} \qquad \textbf{(D) } 1 \qquad \textbf{(E) } \frac{\pi}{2}$

## Solution 1
Let the radius of the large circle be $R$ . Then, the radius of the smaller circles are $\frac R2$ . The areas of the circles are directly proportional to the square of the radii, so the ratio of the area of the small circle to the large one is $\frac 14$ ( $\frac {R^2}{4}$ is $\frac 14$ of $R^2$ .) This means the combined area of the 2 smaller circles is half of the larger circle, and therefore the shaded region is equal to the combined area of the 2 smaller circles, which is $\boxed{\textbf{(D) } 1}$ .

## Solution 2
Let the radius of the two smaller circles be $r$ . It follows that the area of one of the smaller circles is ${\pi}r^2$ . Thus, the area of the two inner circles combined would evaluate to $2{\pi}r^2$ which is $1$ . Since the radius of the bigger circle is two times that of the smaller circles (the diameter), the radius of the larger circle in terms of $r$ would be $2r$ . The area of the larger circle would come to $(2r)^2{\pi} = 4{\pi}r^2$ .
Subtracting the area of the smaller circles from that of the larger circle (since that would be the shaded region), we have \[4{\pi}r^2 - 2{\pi}r^2 = 2{\pi}r^2 = 1.\]
Therefore, the area of the shaded region is $\boxed{\textbf{(D) } 1}$ .

## Solution 3
The area of a small circle is $\frac{1}{2}= \pi r^2$ . Solving, we get $r = \sqrt{\frac{1}{2\pi}}$ .
The radius of the large circle is $R=2r$ . The area of the large circle is ${\pi}R^2={\pi}(2r)^2=4{\pi}r^2=4{\pi}\frac{1}{2\pi}=2$ .
Subtract the area of the small circles from the area of the large circle to get the area of the shaded region: $2-1=$ $\boxed{\textbf{(D) } 1}$ .

## Solution 4 (Similar to Solution 3)
To get the area of the small circles, we can get the equation $\frac{1}{2}= \pi r^2$ . Solving for $r$ , we get $r = \sqrt{\frac{1}{2\pi}}$ . Then, we can get the radius of the big circle by doubling the small circle's radius, and that gives $2\sqrt{\frac{1}{2\pi}}$ . Because the area of a circle is $\pi r^2$ , you'll have to square the answer and multiple it by $\pi$ . After you square it, you'll get $4 \cdot \frac{1}{2\pi}$ , which equals to $\frac{4}{2\pi}$ . Since the area of a circle is $\pi r^2$ , we get $\pi \cdot \frac{4}{2\pi}$ , and that equals $\frac{4\pi}{2\pi}$ , which equals 2. Since each of the circles' area is $\frac{1}{2}$ , the combined area of the small circles is $1$ . Since $2-1=1$ , the area of the shaded region is $\boxed{\textbf{(D) } 1}$ .

## Video Solution (CREATIVE ANALYSIS!!!)
https://youtu.be/tYfMj2SSVJc
~Education, the Study of Everything

## Video Solutions
https://youtu.be/-3WEf3EjGu0
https://youtu.be/-JR7R0PyU-w
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/51K3uCzntWs?t=1474
~ pi_is_3.14
### See Also