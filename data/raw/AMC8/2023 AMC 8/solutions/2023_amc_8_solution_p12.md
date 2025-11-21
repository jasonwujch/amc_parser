# 2023 AMC 8 Problem 12

## Problem

The figure below shows a large white circle with a number of smaller white and shaded circles in its interior. What fraction of the interior of the large white circle is shaded?

[asy] // Diagram by TheMathGuyd size(6cm); draw(circle((3,3),3)); filldraw(circle((2,3),2),lightgrey); filldraw(circle((3,3),1),white); filldraw(circle((1,3),1),white); filldraw(circle((5.5,3),0.5),lightgrey); filldraw(circle((4.5,4.5),0.5),lightgrey); filldraw(circle((4.5,1.5),0.5),lightgrey); int i, j; for(i=0; i<7; i=i+1) { draw((0,i)--(6,i), dashed+grey); draw((i,0)--(i,6), dashed+grey); } [/asy]

$\textbf{(A)}\ \frac{1}{4} \qquad \textbf{(B)}\ \frac{11}{36} \qquad \textbf{(C)}\ \frac{1}{3} \qquad \textbf{(D)}\ \frac{19}{36} \qquad \textbf{(E)}\ \frac{5}{9}$

## Solution 1
First, the total area of the radius $3$ circle is simply just $9\cdot \pi$ when using our area of a circle formula.
Now from here, we have to find our shaded area. This can be done by adding the areas of the $\frac{1}{2}$ -radius circles and add; then, take the area of the $1$ radius circles and subtract that from the area of the $2$ radius circle to get our resulting complex shape area. Adding these up, we will get $3\cdot \frac{1}{4} \pi + 4 \pi -\pi - \pi = \frac{3}{4} \pi + 2 \pi = \frac{11\cdot \pi}{4}$ .
So, our answer is $\frac {\frac{11}{4} \pi}{9 \pi} = \boxed{\textbf{(B)}\ \frac{11}{36}}$ .
~apex304 Minor edits by ~NXC
Minor edits by ~Shriyans Chowdhury

## Solution 2
Pretend each circle is a square. The large shaded circle is a square with area $16~\text{units}^2$ , and the two white circles inside it each have areas of $4~\text{units}^2$ , which adds up to $8~\text{units}^2$ . The three small shaded circles become three squares with area $1~\text{units}^2$ , and add up to $3~\text{units}^2$ . Adding the areas of the shaded circles (19) and subtracting the areas of the white circles (8), we get $11~\text{units}^2$ . Since the largest white circle in which all these other circles are becomes a square that has area $36~\text{units}^2$ , our answer is $\boxed{\textbf{(B)}\ \dfrac{11}{36}}$ .
-claregu LaTeX (edits -apex304, CoOlPoTaToEs, KGINSPECTORBOI, SlimeKnight, rickastleylover99)

## Video Solution by Math-X (How to do this question under 30 seconds)
https://youtu.be/Ku_c1YHnLt0?si=stUHQ9nHZZE_x-CC&t=1852
~Math-X

## Video Solution by CoolMathProblems
https://youtu.be/9WP3LQaMIVg?feature=shared&t=128

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=765 ~hsnacademy

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/5wpEBWZjl6o
~Education the Study of everything

## Video Solution (Animated)
https://youtu.be/5RRo6pQqaUI
~Star League ( https://starleague.us )

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=4590

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=UWoUhV5T92Y

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=1137

## Video Solution by harungurcan
https://www.youtube.com/watch?v=oIGy79w1H8o&t=1154s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/2Ih7F0XHmls

## Video Solution by WhyMath
https://youtu.be/ZOi0faHzBR4
### See Also