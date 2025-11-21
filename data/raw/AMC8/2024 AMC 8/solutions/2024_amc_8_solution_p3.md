# 2024 AMC 8 Problem 3

## Problem

Four squares of side length $4, 7, 9,$ and $10$ are arranged in increasing size order so that their left edges and bottom edges align. The squares alternate in color white-gray-white-gray, respectively, as shown in the figure. What is the area of the visible gray region in square units? [asy] size(150); filldraw((0,0)--(10,0)--(10,10)--(0,10)--cycle,gray(0.7),linewidth(1)); filldraw((0,0)--(9,0)--(9,9)--(0,9)--cycle,white,linewidth(1)); filldraw((0,0)--(7,0)--(7,7)--(0,7)--cycle,gray(0.7),linewidth(1)); filldraw((0,0)--(4,0)--(4,4)--(0,4)--cycle,white,linewidth(1)); draw((11,0)--(11,4),linewidth(1)); draw((11,6)--(11,10),linewidth(1)); label("$10$",(11,5),fontsize(14pt)); draw((10.75,0)--(11.25,0),linewidth(1)); draw((10.75,10)--(11.25,10),linewidth(1)); draw((0,11)--(3,11),linewidth(1)); draw((5,11)--(9,11),linewidth(1)); draw((0,11.25)--(0,10.75),linewidth(1)); draw((9,11.25)--(9,10.75),linewidth(1)); label("$9$",(4,11),fontsize(14pt)); draw((-1,0)--(-1,1),linewidth(1)); draw((-1,3)--(-1,7),linewidth(1)); draw((-1.25,0)--(-0.75,0),linewidth(1)); draw((-1.25,7)--(-0.75,7),linewidth(1)); label("$7$",(-1,2),fontsize(14pt)); draw((0,-1)--(1,-1),linewidth(1)); draw((3,-1)--(4,-1),linewidth(1)); draw((0,-1.25)--(0,-.75),linewidth(1)); draw((4,-1.25)--(4,-.75),linewidth(1)); label("$4$",(2,-1),fontsize(14pt)); [/asy] $\textbf{(A)}\ 42 \qquad \textbf{(B)}\ 45\qquad \textbf{(C)}\ 49\qquad \textbf{(D)}\ 50\qquad \textbf{(E)}\ 52$

## Solution 1
We work inwards. The area of the outer shaded square is the area of the whole square minus the area of the second largest square. The area of the inner shaded region is the area of the third largest square minus the area of the smallest square. The sum of these areas is \[10^2 - 9^2 + 7^2 - 4^2 = 100 - 81 + 49 - 16 = 19 + 33 = \boxed{\textbf{(E)}\ 52}\]
This problem appears multiple times in various math competitions including the AMC and MATHCOUNTS.
-Benedict (countmath1) ~Nivaar and anabel.disher

## Solution 2
In solution 1, we can use Difference of squares to get the answer, rather than calculating the squares of the numbers: \[10^2 - 9^2 + 7^2 - 4^2 = (10 - 9)(10 + 9) - (7 - 4)(7 + 4) = 1\cdot19 + 3\cdot11 = 19 + 33 = \boxed{\textbf{(E)}\ 52}\]
~anabel.disher

## Solution 3
Solve for the areas for each square inside the larger one , and then subtract the areas of the white regions from the areas of each square: \[(10^2 + 7^2) - (9^2 + 4^2) = 149 - 97 = \boxed{\textbf{(E)}\ 52}\]
-MrTechguyPCMT and anabel.disher

## Solution 4
We can calculate it as the sum of the areas of $2$ smaller trapezoids and $2$ larger trapezoids. \[2\left(\cfrac{(7+4)(7-4)}{2}\right)+2\left(\cfrac{(10+9)(10-9)}{2}\right)=10^2 - 9^2 + 7^2 - 4^2 = 19 + 33 = \boxed{\textbf{(E)}\ 52}\]
-SahanWijetunga

## Video Solution 1 (Detailed Explanation) 🚀⚡📊
Youtube Link ⬇️
https://youtu.be/ZNAm6x17gro
~ ChillGuyDoesMath :)

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/q64dg8YAJbE
~mr_mathman
### Video by MathTalks_Now
https://www.youtube.com/watch?v=crn37TRMLv4
-rc1219

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=F37qz7vyfRgZm-1u&t=469

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=vSpf507m-7QMFkbZ&t=238
~hsnacademy

## Video Solution (easy to digest) by Power Solve
https://youtu.be/HE7JjZQ6xCk?si=39xd5CKI9nx-7lyV&t=118

## Video Solution by Parshwa
https://www.youtube.com/watch?v=DQbe_BNfPYw

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=Ylw-kJkSpq8
~NiuniuMaths

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=L83DxusGkSY

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://youtu.be/sPzsce8FQtY?si=IS1hVC0cMd-0CYj5

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=158

## Video Solution by Daily Dose of Math (Understandable, Quick, and Speedy)
https://youtu.be/bSPWqeNO11M?si=HIzlxPjMfvGM5lxR
~Thesmartgreekmathdude

## Video Solution by WhyMath
https://youtu.be/653x6HwexjY
### See Also