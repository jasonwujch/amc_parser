# 2006 AIME II Problem 15

## Problem

Given that $x, y,$ and $z$ are real numbers that satisfy: \begin{align*} x &= \sqrt{y^2-\frac{1}{16}}+\sqrt{z^2-\frac{1}{16}}, \\ y &= \sqrt{z^2-\frac{1}{25}}+\sqrt{x^2-\frac{1}{25}}, \\ z &= \sqrt{x^2 - \frac 1{36}}+\sqrt{y^2-\frac 1{36}}, \end{align*} and that $x+y+z = \frac{m}{\sqrt{n}},$ where $m$ and $n$ are positive integers and $n$ is not divisible by the square of any prime, find $m+n.$

## Solution 1 (Geometric Interpretation)
Let $\triangle XYZ$ be a triangle with sides of length $x, y$ and $z$ , and suppose this triangle is acute (so all altitudes are in the interior of the triangle).
Let the altitude to the side of length $x$ be of length $h_x$ , and similarly for $y$ and $z$ . Then we have by two applications of the Pythagorean Theorem we that \[x = \sqrt{y^2 - h_x^2} + \sqrt{z^2 - h_x^2}\] As a function of $h_x$ , the RHS of this equation is strictly decreasing, so it takes each value in its range exactly once. Thus we must have that $h_x^2 = \frac1{16}$ and so $h_x = \frac{1}4$ and similarly $h_y = \frac15$ and $h_z = \frac16$ .
The area of the triangle must be the same no matter how we measure it; therefore $x\cdot h_x = y\cdot h_y = z \cdot h_z$ gives us $\frac x4 = \frac y5 = \frac z6 = 2A$ and $x = 8A, y = 10A$ and $z = 12A$ .
The semiperimeter of the triangle is $s = \frac{8A + 10A + 12A}{2} = 15A$ so by Heron's formula we have \[A = \sqrt{15A \cdot 7A \cdot 5A \cdot 3A} = 15A^2\sqrt{7}\]
Thus, $A = \frac{1}{15\sqrt{7}}$ and $x + y + z = 30A = \frac2{\sqrt{7}}$ and the answer is $2 + 7 = \boxed{009}$ .
The justification that there is an acute triangle with sides of length $x, y$ and $z$ :
Note that $x, y$ and $z$ are each the sum of two positive square roots of real numbers, so $x, y, z \geq 0$ . (Recall that, by AIME convention , all numbers (including square roots) are taken to be real unless otherwise indicated.)
Also, $\sqrt{y^2-\frac{1}{16}} < \sqrt{y^2} = y$ , so we have $x < y + z$ , $y < z + x$ and $z < x + y$ . But these conditions are exactly those of the triangle inequality , so there does exist such a triangle.

## Solution 2 (Heron Bash)
We can rewrite the equations as follows:
\begin{align*} \frac{1}{4}x &= \sqrt{\left(y+\frac{1}{4}\right) \left(y-\frac{1}{4}\right)\left(\frac{1}{4}\right) \left(\frac{1}{4}\right)}+\sqrt{\left(z+\frac{1}{4}\right) \left(z-\frac{1}{4}\right) \left(\frac{1}{4}\right) \left(\frac{1}{4}\right)} \\ \frac{1}{5} y &= \sqrt{\left(z+\frac{1}{5}\right) \left(z-\frac{1}{5}\right) \left(\frac{1}{5}\right) \left(\frac{1}{5}\right)}+\sqrt{\left(x+\frac{1}{5}\right) \left(x-\frac{1}{5}\right) \left(\frac{1}{5}\right) \left(\frac{1}{5}\right)} \\ \frac{1}{6} z &= \sqrt{\left(x+\frac{1}{6}\right) \left(x-\frac{1}{6}\right) \left(\frac{1}{6}\right) \left(\frac{1}{6}\right)}+\sqrt{\left(y+\frac{1}{6}\right) \left(y-\frac{1}{6}\right) \left(\frac{1}{6}\right) \left(\frac{1}{6}\right)} \end{align*}
Take the first equation. The first square root is the area of a triangle with side lengths $y,y,\frac{1}{2}$ by Heron’s Formula. Similarly, the second square root is the area of a triangle with side lengths $z,z,\frac{1}{2}$ . If we connect these two triangles together at the $\frac{1}{2}$ side, we obtain a kite. The area of the kite is $\frac{1}{4}x$ , and since the first diagonal is $\frac{1}{2}$ , the second diagonal is $\frac{2\cdot\frac{1}{4}x}{\frac{1}{2}}=x$ . If we draw this diagonal, we obtain two triangles with side lengths $x,y,z$ . Let this triangle have area $A$ . Then $\frac{1}{4}x=2A$ ; extend this for the other two equations to get $\frac{1}{5}y=2A$ and $\frac{1}{6}z=2A$ . Therefore $x=8A$ , $y=10A$ , and $z=12A$ . But we can find the area of the $x,y,z$ triangle with Heron's: \[A=\sqrt{(15A)(7A)(5A)(3A)}=15A^2\sqrt{7}\] Therefore $A=\frac{1}{15\sqrt{7}}$ . Hence $x+y+z=30A=\frac{2}{\sqrt{7}}\Rightarrow\boxed{009}$ .
~eevee9406

## Solution 3 (Algebraic)
Note that none of $x,y,z$ can be zero.
Each of the equations is in the form \[a=\sqrt{b^2-d^2}+\sqrt{c^2-d^2}\]
Isolate a radical and square the equation to get \[b^2-d^2=a^2-2a\sqrt{c^2-d^2}+c^2-d^2\]
Now cancel, and again isolate the radical, and square the equation to get \[a^4+b^4+c^4+2a^2c^2-2a^2b^2-2b^2c^2=4a^2c^2-4a^2d^2\]
Rearranging gives \[a^4+b^4+c^4=2a^2b^2+2a^2c^2+2b^2c^2-4a^2d^2\]
Now note that everything is cyclic but the last term (i.e. $-4a^2d^2$ ), which implies \[-4x^2\cdot\frac1{16}=-4y^2\cdot\frac1{25}=-4z^2\cdot\frac1{36}\]
Or
\[x: y: z=4: 5: 6 \implies x=\frac{4y}5 \textrm{ and } z=\frac{6y}5\]
Plug these values into the middle equation to get \[\frac{256y^4+625y^4+1296y^4}{625}=\frac{800y^4}{625}+\frac{1800y^4}{625}+\frac{1152y^4}{625}-\frac{100y^2}{625}\]
Simplifying gives \[1575y^4=100y^2 \textrm{ but } y \neq 0 \implies y^2=\frac4{63} \textrm{ or } y=\frac2{3\sqrt7}\]
Substituting the value of $y$ for $x$ and $z$ gives \[x+y+z = \frac{4y+5y+6y}5 = 3y = 3 \cdot \frac{2}{3\sqrt7} = \frac{2}{\sqrt7}\]
And thus the answer is $\boxed{009}$
~phoenixfire

## Video solution
https://www.youtube.com/watch?v=M6sC26dzb_I

## Video Solution by OmegaLearn.org
https://youtu.be/9Vlt9g8TgRs
These problems are copyrighted © by the Mathematical Association of America.