# 2013 AMC 8 Problem 23

## Problem

Angle $ABC$ of $\triangle ABC$ is a right angle. The sides of $\triangle ABC$ are the diameters of semicircles as shown. The area of the semicircle on $\overline{AB}$ equals $8\pi$ , and the arc of the semicircle on $\overline{AC}$ has length $8.5\pi$ . What is the radius of the semicircle on $\overline{BC}$ ? [asy] import graph; pair A,B,C; A=(0,8); B=(0,0); C=(15,0); draw((0,8)..(-4,4)..(0,0)--(0,8)); draw((0,0)..(7.5,-7.5)..(15,0)--(0,0)); real theta = aTan(8/15); draw(arc((15/2,4),17/2,-theta,180-theta)); draw((0,8)--(15,0)); dot(A); dot(C); label("$A$", A, NW); label("$B$", B, SW); label("$C$", C, SE);[/asy]

$\textbf{(A)}\ 7 \qquad \textbf{(B)}\ 7.5 \qquad \textbf{(C)}\ 8 \qquad \textbf{(D)}\ 8.5 \qquad \textbf{(E)}\ 9$

## Video Solution
https://youtu.be/crR3uNwKjk0 ~savannahsolver

## Solution 1
If the semicircle on $\overline{AB}$ were a full circle, the area would be $16\pi$ .
$\pi r^2=16 \pi \Rightarrow r^2=16 \Rightarrow r=+4$ , therefore the diameter of the first circle is $8$ .
The arc of the largest semicircle is $8.5 \pi$ , so if it were a full circle, the circumference would be $17 \pi$ . So the $\text{diameter}=17$ .
By the Pythagorean theorem, the other side has length $15$ , so the radius is $\boxed{\textbf{(B)}\ 7.5}$
~Edited by Theraccoon to correct typos.
### Brief Explanation
SavannahSolver got a diameter of 17 because the given arc length of the semicircle was 8.5π. The arc length of a semicircle can be calculated using the formula πr, where r is the radius. let’s use the full circumference formula for a circle, which is 2πr. Since the semicircle is half of a circle, its arc length is πr, which was given as 8.5π. Solving for r, we get 𝑟=8.5 . Therefore, the diameter, which is 2r, is 2x8.5=17 Then, the other steps to solve the problem will be the same as mentioned above by SavannahSolver the answer is $\boxed{\textbf{(B)}\ 7.5}$
. - TheNerdWhoIsNerdy.

## Solution 2
We go as in Solution 1, finding the diameter of the circle on $\overline{AC}$ and $\overline{AB}$ . Then, an extended version of the theorem says that the sum of the semicircles on the left is equal to the biggest one, so the area of the largest is $\frac{289\pi}{8}$ , and the middle one is $\frac{289\pi}{8}-\frac{64\pi}{8}=\frac{225\pi}{8}$ , so the radius is $\frac{15}{2}=\boxed{\textbf{(B)}\ 7.5}$ .
~Note by Theraccoon: The person who posted this did not include their name.

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=2584
~ pi_is_3.14
### Answer (B) 7.5
~ Mia Wang the Author ~skibidi