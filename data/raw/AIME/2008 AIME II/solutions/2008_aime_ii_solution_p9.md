# 2008 AIME II Problem 9

## Problem

A particle is located on the coordinate plane at $(5,0)$ . Define a move for the particle as a counterclockwise rotation of $\pi/4$ radians about the origin followed by a translation of $10$ units in the positive $x$ -direction. Given that the particle's position after $150$ moves is $(p,q)$ , find the greatest integer less than or equal to $|p| + |q|$ .

## Solutions

## Solution 1
Let $P(x, y)$ be the position of the particle on the $xy$ -plane, $r$ be the length $OP$ where $O$ is the origin, and $\theta$ be the inclination of OP to the x-axis. If $(x', y')$ is the position of the particle after a move from $P$ , then we have two equations for $x'$ and $y'$ : \[x'=r\cos(\pi/4+\theta)+10 = \frac{\sqrt{2}(x - y)}{2} + 10\] \[y' = r\sin(\pi/4+\theta) = \frac{\sqrt{2}(x + y)}{2}.\] Let $(x_n, y_n)$ be the position of the particle after the nth move, where $x_0 = 5$ and $y_0 = 0$ . Then $x_{n+1} + y_{n+1} = \sqrt{2}x_n+10$ , $x_{n+1} - y_{n+1} = -\sqrt{2}y_n+10$ . This implies $x_{n+2} = -y_n + 5\sqrt{2}+ 10$ , $y_{n+2}=x_n + 5\sqrt{2}$ . Substituting $x_0 = 5$ and $y_0 = 0$ , we have $x_8 = 5$ and $y_8 = 0$ again for the first time. Thus, $p = x_{150} = x_6 = -5\sqrt{2}$ and $q = y_{150} = y_6 = 5 + 5\sqrt{2}$ . Hence, the final answer is
If you're curious, the points do eventually form an octagon and repeat. Seems counterintuitive, but believe it or not, it happens.
https://www.desmos.com/calculator/febtiheosz

## Solution 2
Let the particle's position be represented by a complex number. Recall that multiplying a number by cis $\left( \theta \right)$ rotates the object in the complex plane by $\theta$ counterclockwise. In this case, we use $a = cis(\frac{\pi}{4})$ . Therefore, applying the rotation and shifting the coordinates by 10 in the positive x direction in the complex plane results to
where a is cis $\left( \theta \right)$ . By De-Moivre's theorem, $\left(cis( \theta \right)^n )$ =cis $\left(n \theta \right)$ . Therefore,
Furthermore, $5a^{150} = - 5i$ . Thus, the final answer is

## Solution 3
As before, consider $z$ as a complex number. Consider the transformation $z \to (z-\omega)e^{i\theta} + \omega$ . This is a clockwise rotation of $z$ by $\theta$ radians about the points $\omega$ . Let $f(z)$ denote one move of $z$ . Then
Therefore, $z$ rotates along a circle with center $\omega = 5+(5+5\sqrt2)i$ . Since $8 \cdot \frac{\pi}{4} = 2\pi$ , $f^9(z) = f(z) \implies f^{150}(z) = f^6(z) \implies p+q = \boxed{019}$ , as desired (the final algebra bash isn't bad).

## Solution 4
Let $T:\begin{pmatrix}x\\y\end{pmatrix}\rightarrow R(\frac{\pi}{4})\begin{pmatrix}x\\y\end{pmatrix}+\begin{pmatrix}10\\0\end{pmatrix}$ . We assume that the rotation matrix $R(\frac{\pi}{4}) = R$ here. Then we have
This simplifies to
Since $R+R^{7}=O, R^2+R^6=O, R^3+R^5=O, I+R^4=O$ , so we have $R^6\begin{pmatrix}5\\0\end{pmatrix}+(-R^6-R^7)\begin{pmatrix}10\\0\end{pmatrix}$ , giving $p=-5\sqrt{2}, q=5\sqrt{2}+5$ . The answer is yet $\lfloor10\sqrt{2}+5\rfloor=\boxed{019}$ .
These problems are copyrighted © by the Mathematical Association of America.