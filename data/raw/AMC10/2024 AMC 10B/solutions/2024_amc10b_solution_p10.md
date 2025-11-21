# 2024 AMC 10B Problem 10

## Problem

Quadrilateral $ABCD$ is a parallelogram, and $E$ is the midpoint of the side $\overline{AD}$ . Let $F$ be the intersection of lines $EB$ and $AC$ . What is the ratio of the area of quadrilateral $CDEF$ to the area of $\triangle CFB$ ?

$\textbf{(A) } 5:4 \qquad\textbf{(B) } 4:3 \qquad\textbf{(C) } 3:2 \qquad\textbf{(D) } 5:3 \qquad\textbf{(E) } 2:1$

## Solution 1
Let $AB = CD$ have length $b$ and let the altitude of the parallelogram perpendicular to $\overline{AD}$ have length $h$ .
The area of the parallelogram is $bh$ and the area of $\triangle ABE$ equals $\frac{(b/2)(h)}{2} = \frac{bh}{4}$ . Thus, the area of quadrilateral $BCDE$ is $bh - \frac{bh}{4} = \frac{3bh}{4}$ .
We have from $AA$ that $\triangle CBF \sim \triangle AEF$ . Also, $CB/AE = 2$ , so the length of the altitude of $\triangle CBF$ from $F$ is twice that of $\triangle AEF$ . This means that the altitude of $\triangle CBF$ is $2h/3$ , so the area of $\triangle CBF$ is $\frac{(b)(2h/3)}{2} = \frac{bh}{3}$ .
Then, the area of quadrilateral $CDEF$ equals the area of $BCDE$ minus that of $\triangle CBF$ , which is $\frac{3bh}{4} - \frac{bh}{3} = \frac{5bh}{12}$ . Finally, the ratio of the area of $CDEF$ to the area of triangle $CFB$ is $\frac{\frac{5bh}{12}}{\frac{bh}{3}} = \frac{\frac{5}{12}}{\frac{1}{3}} = \frac{5}{4}$ , so the answer is $\boxed{\textbf{(A) } 5:4}$ .

## Solution 2
Let $[AFE]=1$ . Since $\triangle AFE\sim\triangle CFB$ with a scale factor of $2$ , $[CFB]=4$ . The scale factor of $2$ also means that $\dfrac{AF}{FC}=\dfrac{1}{2}$ , therefore since $\triangle BCF$ and $\triangle BFA$ have the same height, $[BFA]=2$ . Since $ABCD$ is a parallelogram, \[[BCA]=[DAC]\implies4+2=1+[CDEF]\implies [CDEF]=5\implies\boxed{\text{(A) }5:4}\]
vladimir.shelomovskii@gmail.com, vvsss

## Solution 3 (Techniques)
We assert that $ABCD$ is a square of side length $6$ . Notice that $\triangle AFE\sim\triangle CFB$ with a scale factor of $2$ . Since the area of $\triangle ABC$ is $18 \implies$ the area of $\triangle CFB$ is $12$ , so the area of $\triangle AFE$ is $3$ . Thus the area of $CDEF$ is $18-3=15$ , and we conclude that the answer is $\frac{15}{12}\implies\boxed{\text{(A) }5:4}$

## Solution 4
Let $ABCE$ be a square with side length $1$ , to assist with calculations. We can put this on the coordinate plane with the points $D = (0,0)$ , $C = (1, 0)$ , $B = (1, 1)$ , and $A = (0, 1)$ . We have $E = (0, 0.5)$ . Therefore, the line $EB$ has slope $0.5$ and y-intercept $0.5$ . The equation of the line is then $y = 0.5x + 0.5$ . The equation of line $AC$ is $y = -x + 1$ . The intersection is when the lines are equal to each other, so we solve the equation. $0.5x + 0.5 = -x + 1$ , so $x = \frac{1}{3}$ . Therefore, plugging it into the equation, we get $y= \frac{2}{3}$ . Using the shoelace theorem, we get the area of $CDEF$ to be $\frac{5}{12}$ and the area of $CFB$ to be $\frac{1}{3}$ , so our ratio is $\frac{\frac{5}{12}}{\frac{1}{3}} = \boxed{(A) 5:4}$ ~idk12345678

## Solution 5 (wlog)
Let $ABCE$ be a square with side length $2$ . We see that $\triangle AFE \sim \triangle CFB$ by a Scale factor of $2$ . Let the altitude of $\triangle AFE$ and altitude of $\triangle CFB$ be $h$ and $2h$ , respectively. We know that $h+2h$ is equal to $2$ , as the height of the square is $2$ . Solving this equation, we get that $h = \frac{2}3.$ This means $[\triangle CFB] = \frac{4}3,$ we can also calculate the area of $\triangle ABE$ . Adding the area we of $\triangle CFB$ and $\triangle ABE$ we get $\frac{7}3.$ We can then subtract this from the total area of the square: $4$ , this gives us $\frac{5}3$ for the area of quadrilateral $CFED.$ Then we can compute the ratio which is equal to $\boxed{\textbf{(A) } 5:4}.$
~yuvag
(why does the $\LaTeX$ always look so bugged.)

## Solution 6 (barycentrics)
$A=(1,0,0), B=(0,1,0), C=(0,0,1), D=(1,-1,1)$ . Since $E$ is the midpoint of $\overline{AD}$ , $E=(1,-0.5,0.5)$ . The equation of $\overline{EB}$ is: \[0 = \begin{vmatrix} x & y & z \\ 1 & -0.5 & 0.5 \\ 0 & 1 & 0 \end{vmatrix}\] The equation of $\overline{AC}$ is: \[0 = \begin{vmatrix} x & y & z \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{vmatrix}\] We also know that $x+y+z=1$ . To find the intersection, we can solve the system of equations. Solving, we get $x=2/3,y=0,z=1/3$ . Therefore, $F=\left(\frac{2}{3}, 0, \frac{1}{3}\right)$ . Using barycentric area formula, \[\frac{[CFB]}{[ABC]} = \begin{vmatrix} 0 & 0 & 1 \\ 2/3 & 0 & 1/3 \\ 0 & 1 & 0 \end{vmatrix} =\frac{2}{3}\] \[\frac{[CDEF]}{[ABC]} = \begin{vmatrix} 0 & 0 & 1 \\ 1 & -0.5 & 0.5 \\ 2/3 & 0 & 1/3 \end{vmatrix} + \begin{vmatrix} 0 & 0 & 1 \\ 1 & -1 & 1 \\ 1 & -0.5 & 0.5 \end{vmatrix} =\frac{5}{6}\] $\frac{[CDEF]}{[CFB]}=\frac{\frac{5}{6}}{\frac{2}{3}}=\boxed{\textbf{(A) } 5:4}$

## 🎥✨ Video Solution by Scholars Foundation ➡️ (Easy-to-Understand 💡✔️)
https://youtu.be/T_QESWAKUUk?si=TG7ToQnDsYKsNSSJ&t=648

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/QLziG_2e7CY?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=24EZaeAThuE

## Video Solution 3 by TheBeautyofMath
https://youtu.be/ZaHv4UkXcbs?t=1360
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .