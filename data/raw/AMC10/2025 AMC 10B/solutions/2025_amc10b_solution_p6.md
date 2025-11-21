# 2025 AMC 10B Problem 6

## Problem

The line $y = \frac{1}{3}x + 1$ divides the square region defined by $0 \le x \le 2$ and $0 \le y \le 2$ into an upper region and a lower region. The line $x = a$ divides the lower region into two regions of equal area. Then $a$ can be written as $\sqrt{s} - t$ , where $s$ and $t$ are positive integers. What is $s + t$ ?

$\textbf{(A)}~18 \qquad \textbf{(B)}~19 \qquad \textbf{(C)}~20 \qquad \textbf{(D)}~21 \qquad \textbf{(E)}~22$

### Diagram (Not actually in competition)

[asy] import graph; unitsize(4cm); // 1. Define the Square path square = scale(2)*unitsquare; draw(square, linewidth(1.5)); // Label vertices label("$(0,0)$", (0,0), SW); label("$(2,0)$", (2,0), SE); label("$(2,2)$", (2,2), NE); label("$(0,2)$", (0,2), NW); // 2. Define the Lines // Line A: y = x/3 + 1 path line1 = (0,1) -- (2, 5/3); draw(line1, red + linewidth(1)); label("$y=\frac{x}{3}+1$", point(line1, 1), E, red); // Line B: y = 1 path line2 = (0,1) -- (2,1); draw(line2, blue + linewidth(1)); label("$y=1$", point(line2, 1), E, blue); // Line C: x = sqrt(17) - 3 real x_val = sqrt(17) - 3; path line3 = (x_val, 0) -- (x_val, 2); draw(line3, green + dashed + linewidth(1)); label("$x=\sqrt{17}-3$", point(line3, 1), N, green); // Dot at intersection dot((x_val, 1), orange); // 3. Axes // Using standard graph module axes which are most stable xaxis("$x$", -0.5, 2.5, Arrow); yaxis("$y$", -0.5, 2.5, Arrow); [/asy]

## Solution 1
We solve this by finding the areas of trapezoids. The line is $y = \frac{1}{3}x + 1$ . Total Area ( $A_{\text{total}}$ ) of Lower Region: The region from $x=0$ to $x=2$ is a trapezoid. \[A_{\text{total}} = \frac{1}{2}(y(0) + y(2)) \times (2 - 0) = \frac{1}{2}\left(1 + \frac{5}{3}\right)(2) = \frac{8}{3}\] Half Area ( $A_{\text{half}}$ ): The area of the region from $x=0$ to $x=a$ must be $\frac{1}{2}A_{\text{total}}$ . \[A_{\text{half}} = \frac{1}{2} \times \frac{8}{3} = \frac{4}{3}\] Solve for $a$ : This half-region is also a trapezoid. \[A_{\text{half}} = \frac{1}{2}(y(0) + y(a)) \times (a - 0) = \frac{4}{3}\] \[\frac{1}{2}\left(1 + \left(\frac{1}{3}a + 1\right)\right)a = \frac{4}{3}\] \[\frac{1}{2}\left(2 + \frac{a}{3}\right)a = \frac{4}{3}\] \[a + \frac{a^2}{6} = \frac{4}{3}\] Multiplying by 6 gives the quadratic equation: \[a^2 + 6a - 8 = 0\] \[a = \frac{-6 \pm \sqrt{6^2 - 4(1)(-8)}}{2} = \frac{-6 \pm \sqrt{68}}{2} = \frac{-6 \pm 2\sqrt{17}}{2} = -3 \pm \sqrt{17}\] Since $a$ must be positive, $a = \sqrt{17} - 3$ . \[s + t = 17 + 3 = 20\] The correct option is $C$ . ~Jonathanmo

## Solution 2 (Calculus)
The intersection of the line $y = \frac{1}{3}x + 1$ and the square is the point $(2, \frac{5}{3})$ . The total area of the trapezoid formed by the line and the square is thus $\frac{1}{2}(2)(\frac{5}{3} + 1) = \frac{8}{3}$ .
The left trapezoidal region's area is equivalent to the area under the line $y = \frac{1}{3}x + 1$ from $x = 0$ to $x = a$ , which can be evaluated using a definite integral. Setting the integral equal to half of the trapezoidal area, we get: \[\int_{0}^{a} \left(\frac{x}{3} + 1\right)\, dx = \frac{4}{3}\] \[\frac{1}{6}a^2 + a = \frac{4}{3}\] \[a^2 + 6a - 8 = 0\]
We now use the quadratic formula: \[a = \frac{-6 \pm \sqrt{(-6)^2 - 4(1)(8)}}{2} = \sqrt{17} - 3\]
Our answer is $17 + 3 = \boxed{\textbf{(C) 20}}$
~Milkdrinker

## Solution 3 (Cheese)
We know $a$ must be between 1 and 2 because the area from $0,0$ to $1,0$ is less than the area from $1,0$ to $2,0$ . We also know $\sqrt{s}+t$ must be equal to one of the integers from 18-22. We can try out possibilities for a knowing these two things and we find that $a$ must be equal to $\sqrt{s}-3$ when $x$ equals one of the 3 integers $17, 18, 19$ because if $s$ is less than $16$ , $t$ will have to be $2$ to make sure its between $1$ and $2$ and any choice for $s+2$ will be less than $18$ . The same (kind of) applies for numbers greater than $19$ because the smallest $(20)$ added to $3$ will be more than $22$ . If we assume that $s$ is in the simplest form then $s$ cannot be $18$ . We are then left with $a=\sqrt{17}-3$ or $a=\sqrt{19}-3$ . We can just plug in one of them for $a$ and see if it works or not and determine that $a$ must be $\sqrt{17}-3$ so the answer is $\boxed{\textbf{(C)} 20}$
~ToxicWaste

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution 2 (Fast and Easy)
https://www.youtube.com/watch?v=kgwjy5dBvXA ~ Pi Academy

## Video Solution 3 by Daily Dose of Math
https://youtu.be/vayQuXXbr28
~Thesmartgreekmathdude
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .