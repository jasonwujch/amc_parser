# 2018 AMC 10A Problem 15

## Problem

Two circles of radius $5$ are externally tangent to each other and are internally tangent to a circle of radius $13$ at points $A$ and $B$ , as shown in the diagram. The distance $AB$ can be written in the form $\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. What is $m+n$ ?

[asy] draw(circle((0,0),13)); draw(circle((5,-6.2),5)); draw(circle((-5,-6.2),5)); label("$B$", (9.5,-9.5), S); label("$A$", (-9.5,-9.5), S); [/asy]

$\textbf{(A) } 21 \qquad \textbf{(B) } 29 \qquad \textbf{(C) } 58 \qquad \textbf{(D) } 69 \qquad \textbf{(E) } 93$

## Solution 1
[asy] draw(circle((0,0),13)); draw(circle((5,-6.25),5)); draw(circle((-5,-6.25),5)); label("$A$", (-8.125,-10.15), S); label("$B$", (8.125,-10.15), S); draw((0,0)--(-8.125,-10.15)); draw((0,0)--(8.125,-10.15)); draw((-5,-6.25)--(5,-6.25)); draw((-8.125,-10.15)--(8.125,-10.15)); label("$X$", (0,0), N); label("$Y$", (-5,-6.25),NW); label("$Z$", (5,-6.25),NE); [/asy]
Let the center of the surrounding circle be $X$ . The circle that is tangent at point $A$ will have point $Y$ as the center. Similarly, the circle that is tangent at point $B$ will have point $Z$ as the center. Connect $AB$ , $YZ$ , $XA$ , and $XB$ . Now observe that $\triangle XYZ$ is similar to $\triangle XAB$ by SAS.
Writing out the ratios, we get \[\frac{XY}{XA}=\frac{YZ}{AB} \Rightarrow \frac{13-5}{13}=\frac{5+5}{AB} \Rightarrow \frac{8}{13}=\frac{10}{AB} \Rightarrow AB=\frac{65}{4}.\] Therefore, our answer is $65+4= \boxed{\textbf{(D) } 69}$ .

## Solution 2 (Longer)
As in Solution 1, let the center of the surrounding circle be $X$ , a tangent circle be tangent at point $A$ and have point $Y$ as the center, and the other tangent circle be tangent at point $B$ and have point $Z$ as the center (see the figure in Solution 1). We can deduce that $XY=XZ=8$ and $YZ=10$ .
Then, by the Law of Cosines, we have \[YZ^2 = XY^2 + XZ^2 - 2(XY)(XZ)\cos{\angle YXZ} \Rightarrow 100 = 64 + 64 - 2 (8) (8)\cos{\angle YXZ}\] \[\Rightarrow\cos{\angle YXZ}=\frac{7}{32}\]
Now, notice $XA=XB=13$ . Further notice that $\angle YXZ=\angle AXB$ . Again, by the Law of Cosines, \[AB^2 = XA^2 + XB^2 - 2(XA)(XB)\cos{\angle AXB}\] \[\Rightarrow AB = \sqrt{169 + 169 - 2(13)(13)(\frac{7}{32})} = \frac{65}{4}\] Thus, our answer is $65+4= \boxed{\textbf{(D) } 69}$ .
~RedKalkulus
### Note
Let the circle of radius 13 have center $O$ . Let the circle tangent to $\odot O$ at $A$ have center $O_1$ and that tangent at $B$ have center $O_2$ .
Here we prove by contradiction that the intersection of $\overleftrightarrow{OO_1}$ and $\odot O$ must be the point of tangency of $\odot O$ and $\odot O_1$ .
Assume that $A$ is not the point of tangency of $\odot O$ and $\odot O_1$ . Furthermore, let $A$ be the intersection of $\overleftrightarrow{OO_1}$ and $\odot O$ . Then, let $\odot O$ and $\odot O_1$ be tangent at $T$ .
It follows that $\angle ATO_1$ is a right angle, so if we continue $TO_1$ to hit $\odot O$ at $I$ , we have that $\angle ATI$ must intercept a semicircle. $I$ therefore has to be the intersection of the diameter through $A$ and $O$ and $\odot O$ . We previously assumed that $O_1$ had to be on $\overleftrightarrow{OA}$ , so $O_1$ is point $I$ . Clearly, however, if point $O_1$ is point $I$ , $\odot O_1$ will intersect $\odot O$ at more than one point, and therefore will not be tangent, leading to a contradiction.
Therefore, we have proved that $A$ , the intersection of $\overleftrightarrow{OO_1}$ and $\odot O$ , is the point of tangency between $\odot O$ and $\odot O_1$ , so $A$ , $O$ , and $O_1$ are collinear. Therefore, there exists a line through all three points. Likewise, we can perform the same proof on the circle tangent at B, and our solutions above are valid.
~LeonQS

## Video Solution (HOW TO THINK CREATIVELY!)
https://youtu.be/xFnLbr-qt6I
~Education, the Study of Everything

## Video Solution 1
https://youtu.be/HJALwsbHZXc
- Whiz
https://www.youtube.com/watch?v=llMgyOkjNgU&list=PL-27w0UNlunxDTyowGrnvo_T7z92OCvpv&index=3 - amshah

## Video Solution 2 by OmegaLearn
https://youtu.be/NsQbhYfGh1Q?t=1328
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .