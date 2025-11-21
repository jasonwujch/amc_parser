# 2023 AMC 10A Problem 8

## Problem

Barb the baker has developed a new temperature scale for her bakery called the Breadus scale, which is a linear function of the Fahrenheit scale. Bread rises at $110$ degrees Fahrenheit, which is $0$ degrees on the Breadus scale. Bread is baked at $350$ degrees Fahrenheit, which is $100$ degrees on the Breadus scale. Bread is done when its internal temperature is $200$ degrees Fahrenheit. What is this in degrees on the Breadus scale?

$\textbf{(A) }33\qquad\textbf{(B) }34.5\qquad\textbf{(C) }36\qquad\textbf{(D) }37.5\qquad\textbf{(E) }39$

## Solution 1 (Substitution)
To solve this question, you can use $f(x) = mx + b$ where the $x$ is Fahrenheit and the $y$ is Breadus. We have $(110,0)$ and $(350,100)$ . We want to find the value of $y$ in $(200,y)$ that falls on this line. The slope for these two points is $\frac{5}{12}$ ; $y = \frac{5}{12}x + b$ . Solving for $b$ using $(110, 0)$ , $\frac{550}{12} = -b$ . We get $b = \frac{-275}{6}$ . Plugging in $(200, y), \frac{1000}{12}-\frac{550}{12}=y$ . Simplifying, $\frac{450}{12} = \boxed{\textbf{(D) }37.5}$
~walmartbrian

## Solution 2 (Faster)
Let $^\circ B$ denote degrees Breadus. We notice that $200^\circ F$ is $90^\circ F$ degrees more than $0^\circ B$ , and $150^\circ F$ less than $100^\circ B$ . This ratio is $90:150=3:5$ ; therefore, $200^\circ F$ will be $\dfrac3{3+5}=\dfrac38$ of the way from $0$ to $100$ , which is $\boxed{\textbf{(D) }37.5}$
~Technodoggo

## Solution 3 (Intuitive)
From $110$ to $350$ degrees Fahrenheit, the Breadus scale goes from $1$ to $100$ . $110$ to $350$ degrees is a span of $240$ , and we can use this to determine how many Fahrenheit each Breadus unit is worth. $240$ divided by $100$ is $2.4$ , so each Breadus unit is $2.4$ Fahrenheit, starting at $110$ Fahrenheit. For example, $1$ degree on the Breadus scale is $110 + 2.4$ , or $112.4$ Fahrenheit. Using this information, we can figure out how many Breadus degrees $200$ Fahrenheit is. $200-110$ is $90$ , so we divide $90$ by $2.4$ to find the answer, which is $\boxed{\textbf{(D) }37.5}$
~MercilessAnimations

## Solution 4
We note that the range of F temperatures that $0-100$ $\text{Br}^\circ$ represents is $350-110 = 240$ $\text{F}^\circ$ . $200$ $\text{F}^\circ$ is $(200-110) = 90$ $\text{F}^\circ$ along the way to getting to $240$ $\text{F}^\circ$ , the end of this range, or $90/240 = 9/24 = 3/8 = 0.375$ of the way. Therefore if we switch to the Br scale, we are $0.375$ of the way to $100$ from $0$ , or at $\boxed{\textbf{(D) }37.5}$ $\text{Br}^\circ$ .
~Dilip ~Minor edits by FutureSphinx

## Solution 5
We have the points $(0, 110)$ and $(100, 350)$ . We want to find $(x, 200)$ . The equation of the line is $y=\frac{12}{5}x+110$ . We use this to find $x=\frac{75}{2}=37.5$ , or $\boxed{D}$ . ~MC413551

## Solution 6 (extremely simple)
We can write the value $y$ on the Breadus scale as $y = mt + b$ , where $t$ is the temperature in Fahrenheit. From the problem, $110m + 1b = 0$ and $350m + 1b = 100.$ We can rewrite this problem in terms of linear algebra to solve it.
$Let \: A =\begin{bmatrix} 110 & 1 \\ 350 & 1 \end{bmatrix}, let \: B = \begin{bmatrix} 0 \\ 100 \end{bmatrix}, and \: let \: x = \begin{bmatrix} m \\ b \end{bmatrix}.$ We can write the system of equations as Ax = B. We can solve for x using the expression x = $A^{-1}B$ . Calculating this value we get $x = \begin{bmatrix} -1/240 & 1/240 \\ 35/24 & -11/24 \end{bmatrix}\cdot\begin{bmatrix} 0 \\ 100 \end{bmatrix}=\begin{bmatrix} 5/12 \\ -275/6 \end{bmatrix}.$ Therefore, $m = 5/12 \: and \: b = -275/6$ . Plugging in $t = 200$ , we get $(5/12)200+(-275/6) = \boxed{\textbf{(D) }37.5}$ .
~Loquacious Autodidact

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=rxjQH1lLtTftMj9a&t=1428 ~little-fermat

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=prG8ONR_AgTR4HkL&t=1683 ~Math-X

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=dfrF_P-FIEA

## Video Solution
https://youtu.be/bYzV5B425V4
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution (easy to digest) by Power Solve
https://www.youtube.com/watch?v=Yi5p3_x9iU8
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .