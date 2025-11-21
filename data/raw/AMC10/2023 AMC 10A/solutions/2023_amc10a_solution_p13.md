# 2023 AMC 10A Problem 13

## Problem

Abdul and Chiang are standing $48$ feet apart in a field. Bharat is standing in the same field as far from Abdul as possible so that the angle formed by his lines of sight to Abdul and Chiang measures $60^\circ$ . What is the square of the distance (in feet) between Abdul and Bharat?

$\textbf{(A) } 1728 \qquad \textbf{(B) } 2601 \qquad \textbf{(C) } 3072 \qquad \textbf{(D) } 4608 \qquad \textbf{(E) } 6912$

## Solution 1 (Using Trigonometry)
Let $\theta=\angle ACB$ and $x=\overline{AB}$ .
According to the Law of Sines, we know that $\dfrac{\sin\theta}x=\dfrac{\sin60^\circ}{48}=\dfrac{\sqrt3}{96}$ . Rearranging, we get that $x=\dfrac{\sin\theta}{\frac{\sqrt3}{96}}=32\sqrt3\sin\theta$ where $x$ is a function of $\theta$ . We want to maximize $x$ .
We know that the maximum value of $\sin\theta=1$ , so this yields $x=32\sqrt3\implies x^2=\boxed{\textbf{(C) }3072.}$
A quick check verifies that $\theta=90^\circ$ indeed works.
~Technodoggo ~(minor grammar edits by vadava_lx)

## Solution 2 (Inscribed Angles)
We can draw a circle such that the chord AC inscribes an arc of 120 degrees. This way, any point B on the circle not in the inscribed arc will form an angle of 60 degrees with $\angle{ABC}$ . To maximize the distance between A and B, they must be opposite each other. So, the problem is now finding the length of the diameter of the circle. We know AOC is 120 degrees, so dropping a perpendicular form O to AC gives us the radius as $16\sqrt{3}$ . So, the diameter is $32\sqrt{3}$ which gives us the answer $\boxed{\textbf{(C) }3072}$
~AwesomeParrot

## Solution 3 (Guessing)
Guess that the optimal configuration is a 30-60-90 triangle, as an equilateral triangle gives an answer of $48^2=2304$ , which is not on the answer choices. Its ratio is $\frac{48}{\sqrt{3}}$ , so $\overline{AB}=\frac{96}{\sqrt{3}}$ .
Its square is then $\frac{96^2}{3}=\boxed{\textbf{(C) }3072}$
Note: The distance between Abdul and Chiang is constant, so let that be represented as ${x}$ . If we were dealing with an equilateral triangle, the height would be ${{x\sqrt3}/2}$ , and if we were dealing with a 30-60-90 triangle, the height would be ${x\sqrt3}$ , which is greater than ${{x\sqrt3}/2}$ .
Note: The problem states that the distance from A to B is maximized, and the longest side of a triangle will always correspond to the largest possible angle, aka 90 so 90 and 60 makes it a 30-60-90.
~not_slay
~Chicken123123
~wangzrpi

## Solution 4
We use $A$ , $B$ , $C$ to refer to Abdul, Bharat and Chiang, respectively. We draw a circle that passes through $A$ and $C$ and has the central angle $\angle AOC = 60^\circ \cdot 2$ . Thus, $B$ is on this circle. Thus, the longest distance between $A$ and $B$ is the diameter of this circle. Following from the law of sines, the square of this diameter is \[ \left( \frac{48}{\sin 60^\circ} \right)^2 = \boxed{\textbf{(C) 3072}}. \]
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 5
We can represent Abdul, Bharat and Chiang as $A$ , $B$ , and $C$ , respectively. Since we have $\angle ABC=60^\circ$ and (from other solutions) $\angle BCA=90^\circ$ , this is a $30-60-90$ triangle. By the side ratios of a $30-60-90$ triangle, we can infer that $AB=\frac{48\times 2}{\sqrt{3}}$ . Squaring AB we get $\boxed{\textbf{(C) 3072}}$ .
~ESAOPS

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=ISeW3ruGd-iLhQZi&t=2819 ~little-fermat

## Video Solution by Math-X
https://youtu.be/GP-DYudh5qU?si=unB-KAz2AXgMuLSS&t=3337
~Math-X

## Video Solution 🚀 Under 2 min 🚀
https://youtu.be/d5XeBKZvTGQ
~Education, the Study of Everything

## Video Solution by Power Solve
https://www.youtube.com/watch?v=jkfsBYzBJbQ

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=nmVZxartc-o

## Video Solution 1 by OmegaLearn
https://youtu.be/mx2iDUeftJM

## Video Solution by CosineMethod
https://www.youtube.com/watch?v=BJKHsHQyoTg

## Video Solution
https://youtu.be/wuew6LaAM48
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by MegaMath
https://www.youtube.com/watch?v=ZsiqPRWCEkQ&t=3s
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .