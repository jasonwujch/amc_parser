# 2021 AMC 10A Problem 24

## Problem

The interior of a quadrilateral is bounded by the graphs of $(x+ay)^2 = 4a^2$ and $(ax-y)^2 = a^2$ , where $a$ is a positive real number. What is the area of this region in terms of $a$ , valid for all $a > 0$ ?

$\textbf{(A)} ~\frac{8a^2}{(a+1)^2}\qquad\textbf{(B)} ~\frac{4a}{a+1}\qquad\textbf{(C)} ~\frac{8a}{a+1}\qquad\textbf{(D)} ~\frac{8a^2}{a^2+1}\qquad\textbf{(E)} ~\frac{8a}{a^2+1}$

### Diagram

Graph in Desmos: https://www.desmos.com/calculator/satawguqsc

~MRENTHUSIASM

## Solution 1 (Generalized Value of a)
The cases for $(x+ay)^2 = 4a^2$ are $x+ay = \pm2a,$ or two parallel lines. We rearrange each case and construct the table below: \[\begin{array}{c||c|c|c|c} & & & & \\ [-2.5ex] \textbf{Case} & \textbf{Line's Equation} & \boldsymbol{x}\textbf{-Intercept} & \boldsymbol{y}\textbf{-Intercept} & \textbf{Slope} \\ [0.5ex] \hline & & & & \\ [-1.5ex] 1 & x+ay-2a=0 & 2a & 2 & -\frac1a \\ [2ex] 2 & x+ay+2a=0 & -2a & -2 & -\frac1a \\ [0.75ex] \end{array}\] The cases for $(ax-y)^2 = a^2$ are $ax-y=\pm a,$ or two parallel lines. We rearrange each case and construct the table below: \[\begin{array}{c||c|c|c|c} & & & & \\ [-2.5ex] \textbf{Case} & \textbf{Line's Equation} & \boldsymbol{x}\textbf{-Intercept} & \boldsymbol{y}\textbf{-Intercept} & \textbf{Slope} \\ [0.5ex] \hline & & & & \\ [-1.5ex] 1* & ax-y-a=0 & 1 & -a & a \\ [2ex] 2* & ax-y+a=0 & -1 & a & a \\ [0.75ex] \end{array}\] Since the slopes of intersecting lines $(1)\cap(1*), (1)\cap(2*), (2)\cap(1*),$ and $(2)\cap(2*)$ are negative reciprocals, we get four right angles, from which the quadrilateral is a rectangle.
Two solutions follow from here:

## Solution 1.1 (Distance Between Parallel Lines)
Recall that for constants $A,B,C_1$ and $C_2,$ the distance $d$ between parallel lines $\begin{cases} Ax+By+C_1=0 \\ Ax+By+C_2=0 \end{cases}$ is \[d=\frac{\left|C_2-C_1\right|}{\sqrt{A^2+B^2}}.\] From this formula:
- The distance between lines $(1)$ and $(2)$ is $\frac{4a}{\sqrt{1+a^2}},$ the length of this rectangle.
- The distance between lines $(1*)$ and $(2*)$ is $\frac{2a}{\sqrt{a^2+1}},$ the width of this rectangle.
The area we seek is \[\frac{4a}{\sqrt{1+a^2}}\cdot\frac{2a}{\sqrt{a^2+1}}=\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}.\] ~MRENTHUSIASM

## Solution 1.2 (Distance Between Points)
The solutions to systems of equations $(1)\cap(1*), (1)\cap(2*), (2)\cap(2*), (2)\cap(1*)$ are \[(x,y)=\left(\frac{a(a+2)}{a^2+1},\frac{a(2a-1)}{a^2+1}\right), \left(-\frac{a(a-2)}{a^2+1},\frac{a(2a+1)}{a^2+1}\right), \left(-\frac{a(a+2)}{a^2+1},-\frac{a(2a-1)}{a^2+1}\right), \left(\frac{a(a-2)}{a^2+1},-\frac{a(2a+1)}{a^2+1}\right),\] respectively, which are the consecutive vertices of this rectangle.
By the Distance Formula, the length and width of this rectangle are $\frac{4a\sqrt{a^2+1}}{a^2+1}$ and $\frac{2a\sqrt{a^2+1}}{a^2+1},$ respectively.
The area we seek is \[\frac{4a\sqrt{a^2+1}}{a^2+1}\cdot\frac{2a\sqrt{a^2+1}}{a^2+1}=\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}.\] ~MRENTHUSIASM

## Solution 2 (Specified Value of a)
In this solution, we will refer to equations $(1),(2),(1*),$ and $(2*)$ from Solution 1.
Substituting $a=2$ into the answer choices gives
$\textbf{(A)} ~\frac{32}{9}\qquad\textbf{(B)} ~\frac{8}{3}\qquad\textbf{(C)} ~\frac{16}{3}\qquad\textbf{(D)} ~\frac{32}{5}\qquad\textbf{(E)} ~\frac{16}{5}$
At $a=2,$ the solutions to systems of equations $(1)\cap(1*), (1)\cap(2*), (2)\cap(2*), (2)\cap(1*)$ are \[(x,y)=\left(\frac 85, \frac 65\right), (0,2), \left(-\frac 85, -\frac 65\right), (0,-2),\] respectively, which are the consecutive vertices of the quadrilateral.
Two solutions follow from here:

## Solution 2.1 (Area of a Rectangle)
From the tables in Solution 1, we conclude that the quadrilateral is a rectangle.
By the Distance Formula, the length and width of this rectangle are $\frac{8\sqrt5}{5}$ and $\frac{4\sqrt5}{5},$ respectively.
The area we seek is \[\frac{8\sqrt5}{5}\cdot\frac{4\sqrt5}{5}=\frac{32}{5},\] from which the answer is $\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}.$
~MRENTHUSIASM

## Solution 2.2 (Area of a General Quadrilateral)
Even if we do not recognize that the quadrilateral is a rectangle, we can apply the Shoelace Theorem to its consecutive vertices \begin{align*} (x_1,y_1) &= \left(\frac 85, \frac 65\right), \\ (x_2,y_2) &= (0,2), \\ (x_3,y_3) &= \left(-\frac 85, -\frac 65\right), \\ (x_4,y_4) &= (0,-2). \end{align*} The area we seek is \[\frac{1}{2} \left|(x_1y_2 + x_2y_3 + x_3y_4 + x_4y_1) - (y_1x_2 + y_2x_3 + y_3x_4 + y_4x_1)\right| = \frac{32}{5}.\] from which the answer is $\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}.$
~MRENTHUSIASM

## Solution 3 (Slopes and Intercepts)
The quadrilateral is enclosed by four lines. Similar to Solution 1, we will use the equations from the four cases:
1. $x+ay=2a.$ This is a line with $x$ -intercept $2a,$ $y$ -intercept $2,$ and slope $-\frac 1a.$
1. $x+ay=-2a.$ This is a line with $x$ -intercept $-2a,$ $y$ -intercept $-2,$ and slope $-\frac 1a.$
1. $ax-y=a.$ This is a line with $x$ -intercept $1,$ $y$ -intercept $-a,$ and slope $a.$
1. $ax-y=-a.$ This is a line with $x$ -intercept $-1,$ $y$ -intercept $a,$ and slope $a.$
It follows that $DF = 4$ and $DE = \sqrt{4^2 - s^2}$ .
Because the slope of line $y = -\frac{x}{a} + 2$ is $-\frac{1}{a}$ , $\frac{1}{a} = \frac{DE}{EF} = \frac{\sqrt{16-s^2}}{s}$ , $s^2(a^2+1) = 16a^2$ , $s = \frac{4a}{\sqrt{a^2+1}}$ .
It follows that $AC = 2a$ and $BC = \sqrt{(2a)^2 - w^2}$ .
Because the slope of line $y = ax - a$ is $a$ , $a = \frac{BC}{AB} = \frac{\sqrt{4a^2-w^2}}{w}$ , $w^2(a^2+1)=4a^2$ , $w=\frac{2a}{\sqrt{a^2+1}}$ .
Therefore, the answer is \[\text{Area} = s \cdot w=\frac{4a}{\sqrt{a^2+1}} \cdot \frac{2a}{\sqrt{a^2+1}} = \boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}.\]
~ isabelchen

## Solution 4 (Trigonometry)
Similar to Solution 1, we will use the equations from the four cases:
1. $x+ay=2a.$ This is a line with $x$ -intercept $2a,$ $y$ -intercept $2,$ and slope $-\frac 1a.$
1. $x+ay=-2a.$ This is a line with $x$ -intercept $-2a,$ $y$ -intercept $-2,$ and slope $-\frac 1a.$
1. $ax-y=a.$ This is a line with $x$ -intercept $1,$ $y$ -intercept $-a,$ and slope $a.$
1. $ax-y=-a.$ This is a line with $x$ -intercept $-1,$ $y$ -intercept $a,$ and slope $a.$
Let $\tan A=a.$ The area of the rectangle created by the four equations can be written as \begin{align*} 2a\cdot \cos A\cdot4\sin A &= 8a\cos A \cdot \sin A \\ &= 8a\cdot~\frac{1}{\sqrt{a^2+1}}\cdot~\frac{a}{\sqrt{a^2+1}} \\ &= \boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}. \end{align*} ~fnothing4994 (Solution)
~MRENTHUSIASM (Code Adjustments)

## Solution 5 (Observations)
The conditions $(x+ay)^2 = 4a^2$ and $(ax-y)^2 = a^2$ give $|x+ay| = |2a|$ and $|ax-y| = |a|$ or $x+ay = \pm 2a$ and $ax-y = \pm a$ . The slopes here are perpendicular, so the quadrilateral is a rectangle. Plug in $a=1$ and graph it. We quickly see that the area is $2\sqrt{2} \cdot \sqrt{2} = 4$ , so the answer can't be $\textbf{(A)}$ or $\textbf{(B)}$ by testing the values they give (test it!). Now plug in $a=2$ . We see using a ruler that the sides of the rectangle are about $\frac74$ and $\frac72$ . So the area is about $\frac{49}8 = 6.125$ . Testing $\textbf{(C)}$ , we get $\frac{16}3$ which is clearly less than $6$ , so it is out. Testing $\textbf{(D)}$ , we get $\frac{32}5$ which is near our answer, so we leave it. Testing $\textbf{(E)}$ , we get $\frac{16}5$ , way less than $6$ , so it is out. So, the only plausible answer is $\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}$ .
~firebolt360

## Solution 6 (Observations)
Trying $a = 1$ narrows down the choices to options $\textbf{(C)}$ , $\textbf{(D)}$ and $\textbf{(E)}$ . Trying $a = 2$ and $a = 3$ eliminates $\textbf{(C)}$ and $\textbf{(E)}$ , to obtain $\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}$ as our answer. Refer to Solution 2 for a detailed explanation.
~¢

## Solution 7 (Observations: Cheap)
Note that $a=2$ yields different values for all answer choices. If we put in $a=2,$ we find that the area of the quadrilateral is $\frac{32}{5}.$ This means that the answer must be $\boxed{\textbf{(D)} ~\frac{8a^2}{a^2+1}}.$ Refer to Solution 2 for a detailed explanation.

## Video Solution by OmegaLearn (System of Equations and Shoelace Formula)
https://youtu.be/2iohPYkZpkQ
~ pi_is_3.14

## Video Solution by MRENTHUSIASM (English & Chinese)
https://www.youtube.com/watch?v=oEY-kX4d87M
~MRENTHUSIASM
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .