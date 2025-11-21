# 2024 AMC 8 Problem 24

## Problem

Jean has made a piece of stained glass art in the shape of two mountains, as shown in the figure below. One mountain peak is $8$ feet high while the other peak is $12$ feet high. Each peak forms a $90^\circ$ angle, and the straight sides form a $45^\circ$ angle with the ground. The artwork has an area of $183$ square feet. The sides of the mountain meet at an intersection point near the center of the artwork, $h$ feet above the ground. What is the value of $h?$

[asy] unitsize(.3cm); filldraw((0,0)--(8,8)--(11,5)--(18,12)--(30,0)--cycle,gray(0.7),linewidth(1)); draw((-1,0)--(-1,8),linewidth(.75)); draw((-1.4,0)--(-.6,0),linewidth(.75)); draw((-1.4,8)--(-.6,8),linewidth(.75)); label("$8$",(-1,4),W); label("$12$",(31,6),E); draw((-1,8)--(8,8),dashed); draw((31,0)--(31,12),linewidth(.75)); draw((30.6,0)--(31.4,0),linewidth(.75)); draw((30.6,12)--(31.4,12),linewidth(.75)); draw((31,12)--(18,12),dashed); label("$45^{\circ}$",(.75,0),NE,fontsize(10pt)); label("$45^{\circ}$",(29.25,0),NW,fontsize(10pt)); draw((8,8)--(7.5,7.5)--(8,7)--(8.5,7.5)--cycle); draw((18,12)--(17.5,11.5)--(18,11)--(18.5,11.5)--cycle); draw((11,5)--(11,0),dashed); label("$h$",(11,2.5),E); [/asy]

$\textbf{(A)}\ 4 \qquad \textbf{(B)}\ 5 \qquad \textbf{(C)}\ 4\sqrt{2} \qquad \textbf{(D)}\ 6 \qquad \textbf{(E)}\ 5\sqrt{2}$

## Solution 1
Extend the "inner part" of the mountain so that the image is two right triangles that overlap in a third right triangle as shown. [asy] unitsize(.2cm); draw((0,0)--(8,8)--(11,5)--(18,12)--(30,0)--cycle,linewidth(1)); draw((11,5)--(6, 0)--(16, 0)--cycle,linewidth(0.5)); label("$8\sqrt{2}$",(4,4),NW); label("$12\sqrt{2}$",(24,6),NE); draw((8,8)--(7.5,7.5)--(8,7)--(8.5,7.5)--cycle); draw((18,12)--(17.5,11.5)--(18,11)--(18.5,11.5)--cycle); draw((11,5)--(11,0),dashed); label("$h$",(11,2.5),E); [/asy] The side length of the largest right triangle is $12\sqrt{2},$ which means its area is $144.$ Similarly, the area of the second largest right triangle is $64$ (the side length is $8\sqrt{2}$ ), and the area of the overlap is $h^2$ (the side length is $h\sqrt{2}$ ). Because the right triangles have a side ratio of 1:1: $\sqrt{2}$ .Thus, \[144+64-h^2=183,\] which means that the answer is $\boxed{\mathbf{(B)}\text{ 5}}.$
~BS201

## Solution 2 (Using a Ruler)
You can measure $h$ with a ruler (rulers are allowed on the AMC 8), and see that $h$ is closest to $\boxed{\mathbf{(B)}\text{ 5}}.$
~SID-DARTH-VATER
(Please note: This is not the best way,as diagrams are NOT ALWAYS DRAWN TO SCALE) ~Anonymous ~Continuous_Pi

## Video Solution 1 by Math-X (First understand the problem!!!!!!!!)
https://youtu.be/BaE00H2SHQM?si=793ml6R_qT79h-aI&t=7651
~Math-X

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/DL83nznn3gM
~mr_mathman

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=D8pGHQYbzJ_eMsEy&t=3678 ~hsnacademy

## Video Solution (Quick solution) by Parshwa
https://youtu.be/Ky-NVrOv4ew

## Video Solution by Power Solve (easy to understand)
https://www.youtube.com/watch?v=PlMGNmWIkBg

## Video Solution by OmegaLearn.org
https://youtu.be/KL_CGQrkXXo

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=RiSt6_WLfrM

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=8353ngt05N0
~NiuniuMaths

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=H5Pq8mf-OVk

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=3126
### 2 minute solve (fast and elegant) by MegaMath
https://www.youtube.com/watch?v=hUh0hux3xuU

## Video solution by Dr. David
https://youtu.be/ZurHG58d1JM

## Video Solution by WhyMath
https://youtu.be/LSVPJAu-jxw

## Video Solution- (Extremely Simple Triangle Theories!!)
https://www.youtube.com/watch?v=3UC1rwf6vfo ~TheMathGeek

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also