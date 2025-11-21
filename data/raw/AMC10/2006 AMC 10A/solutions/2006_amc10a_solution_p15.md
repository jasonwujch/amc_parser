# 2006 AMC 10A Problem 15

## Problem

Odell and Kershaw run for $30$ minutes on a circular track. Odell runs clockwise at $\text{250 m/min}$ and uses the inner lane with a radius of $50$ meters. Kershaw runs counterclockwise at $\text{300 m/min}$ and uses the outer lane with a radius of $60$ meters, starting on the same radial line as Odell. How many times after the start do they pass each other?

$\textbf{(A) } 29\qquad\textbf{(B) } 42\qquad\textbf{(C) } 45\qquad\textbf{(D) } 47\qquad\textbf{(E) } 50\qquad$

## Solution
Since $d = rt$ , we note that Odell runs one lap in $\frac{2 \cdot 50\pi}{250} = \frac{2\pi}{5}$ minutes, while Kershaw also runs one lap in $\frac{2 \cdot 60\pi}{300} = \frac{2\pi}{5}$ minutes. They take the same amount of time to run a lap, and since they are running in opposite directions they will meet exactly twice per lap (once at the starting point, the other at the half-way point). Thus, there are $\frac{30}{\frac{2\pi}{5}} \approx 23.8$ laps run by both, or $\lfloor 2\cdot 23.8\rfloor = 23 \cdot 2 + 1 =\boxed{\textbf{(D) } 47}$ meeting points.

## Solution 2
We first find the amount of minutes, $k$ , until Odell and Kershaw's next meeting. Let $a$ be the angle in radians between their starting point and the point where they first meet, measured counterclockwise.
Since Kershaw has traveled $300k$ meters at this point and the circumference of his track is $120\pi$ , $a=\frac{300k}{120\pi}\cdot 2\pi$ . Similarly, $2\pi-a=\frac{250k}{100\pi}\cdot{2\pi}$ since Odell has traveled $250k$ meters in the opposite direction and the circumference of his track is $100\pi$ .
Solving for $a$ in the second equation, we get $a=2\pi-\frac{250k}{100\pi}\cdot 2\pi$ . Then, from the first equation, we have $\frac{300k}{120\pi}\cdot 2\pi=2\pi-\frac{250k}{100\pi}\cdot 2\pi$ . Solving for $k$ , we get $k=\frac{\pi}{5}$ . After $k$ minutes, they are back at the same position, except rotated, so they will meet again in $k$ minutes. So the total amount of meetings is $\lfloor\frac{30}{k}\rfloor=\lfloor\frac{150}{\pi}\rfloor=\boxed{\textbf{(D) }47}$ .
~apsid

## Solution 3 by Alcumus (ikr)
Since Odell's rate is $5/6$ that of Kershaw, but Kershaw's lap distance is $6/5$ that of Odell, they each run a lap in the same time. Hence they pass twice each time they circle the track. Odell runs \[(30 \ \text{min})\left(250\frac{\text{m}}{\text{min}}\right)\left(\frac{1}{100\pi}\frac{\text{laps}}{\text{m}}\right)= \frac{75}{\pi}\,\text{laps}\approx 23.87\ \text{laps},\] as does Kershaw. Because $23.5 < 23.87 < 24$ , they pass each other $2(23.5)=\boxed{47}$ times.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .