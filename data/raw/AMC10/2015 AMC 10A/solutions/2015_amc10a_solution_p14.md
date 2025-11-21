# 2015 AMC 10A Problem 14

## Problem

The diagram below shows the circular face of a clock with radius $20$ cm and a circular disk with radius $10$ cm externally tangent to the clock face at $12$ o' clock. The disk has an arrow painted on it, initially pointing in the upward vertical direction. Let the disk roll clockwise around the clock face. At what point on the clock face will the disk be tangent when the arrow is next pointing in the upward vertical direction?

[asy]size(170);defaultpen(linewidth(0.9)+fontsize(13pt));draw(unitcircle^^circle((0,1.5),0.5)); path arrow = origin--(-0.13,-0.35)--(-0.06,-0.35)--(-0.06,-0.7)--(0.06,-0.7)--(0.06,-0.35)--(0.13,-0.35)--cycle; for(int i=1;i<=12;i=i+1){draw(0.9*dir(90-30*i)--dir(90-30*i));label("$"+(string) i+"$",0.78*dir(90-30*i));} dot(origin);draw(shift((0,1.87))*arrow);draw(arc(origin,1.5,68,30),EndArrow(size=12));[/asy]

$\textbf{(A) }\text{2 o' clock} \qquad\textbf{(B) }\text{3 o' clock} \qquad\textbf{(C) }\text{4 o' clock} \qquad\textbf{(D) }\text{6 o' clock} \qquad\textbf{(E) }\text{8 o' clock}$

## Solution 1 (Important Clarification)
The below solutions don't do a great job on telling you why the answer is not $\textbf{(D) }\text{6 o' clock}$ . For those who don't understand it, the below video is great on explaining it.
The SAT question everyone got wrong
Skip to 10:13.
Here is the best approach to the problem, and any problem of this manner.
If you had watched the video (highly recommended), you should have learned that when a circle $A$ travels along the outside of any figure $B$ , the total number of rotations circle $A$ made along the revolution of the figure is just the perimeter $P_B$ plus the circumference $C_A$ divided by $C_A$ , or $\frac{P_B + C_A}{C_A}$ . (This is proved in the video as well).
Therefore, the total number of rotations of the smaller circle rotating around the clock is the circumference of the clock, which is $40\pi$ , plus the circumference of the smaller circle, which is $20\pi$ , divided by the circumference of the smaller circle, which is $20\pi$ . Then, we see that the arrow rotates a total of $\frac{40\pi + 20\pi}{20\pi} \Rightarrow \frac{60\pi}{20\pi} \Rightarrow \frac{60}{20} \Rightarrow 3$ .
Finally, because the clock is marked at 12 intervals, each rotation is at every $12/3 = 4$ hour intervals.
Therefore, if the circle starts at 12:00, then it will make its first full rotation at $\boxed{\textbf{(C) }4 \ \text{o' clock}}$ , not $\textbf{(D) }\text{6 o' clock}$ .
I hope this cleared all confusion. It is important to understand these topics to avoid mistakes on later tests.
~Pinotation

## Solution 2
The circumference of the clock is twice that of the disk. So, a quarter way around the clock (3:00), the point halfway around the disk will be tangent. The arrow will point to the left. We can see the disk made a 75% rotation from 12 to 3, and 3 is 75% of 4, so it would make 100% rotation from 12 to 4. The answer is $\boxed{\textbf{(C) }4 \ \text{o' clock}}$ . Similarly, the arrow would be pointing downward at 6:00. It would already have completed three 180 degree turns. Therefore, two 180 degree turns would be completed at 4:00.

## Solution 3
The rotation factor of the arrow is the sum of the rates of the regular rotation of the arrow (360° every 360° rotation = 1) and the rotation of the disk around the clock with twice the circumference (360° every 180° = 2). Thus, the rotation factor of the arrow is 3, and so our answer corresponds to 360°/3 = 120°, which is 4 o' clock. $\boxed{\textbf{(C) }4 \ \text{o' clock}}$

## Solution 4
The arrow travels a path of radius 30 (20 from the interior clock and 10 from the radius of the disk itself). We note that 1 complete rotation of 360 degrees is needed for the arrow to appear up again, so, therefore, the disk must travel its circumference before the arrow goes up. Its circumference is $20\pi$ , so that is $20\pi$ traveled on a $60\pi$ arrow path. This is a ratio of 1/3, so the angle it carves is 120 degrees, which leads us to the correct answer of 4 o' clock. $\boxed{\textbf{(C) }4 \ \text{o' clock}}$

## Solution 5
Suppose that the small disk also had a clock face on it, and that both disks were toothed wheels, free to rotate around their centers. The part of the picture where they engage would look like this: [asy] fill(arc((0,0),2,30,150)--cycle,lightgrey); draw(arc((0,0),2,30,150)); draw(1.8*dir(90)--2*dir(90)); draw(1.8*dir(60)--2*dir(60)); label("12",1.56*dir(90)); label("1",1.56*dir(60)); draw(arc((0,3),1,-15,-165)); draw(0.9*dir(-90)+(0,3)--dir(-90)+(0,3)); draw(0.9*dir(-60)+(0,3)--dir(-60)+(0,3)); draw(0.9*dir(-30)+(0,3)--dir(-30)+(0,3)); label("6",.74*dir(-90)+(0,3)); label("5",.74*dir(-60)+(0,3)); label("4",.74*dir(-30)+(0,3)); [/asy] The small cog has half the radius, and therefore half the circumference. If the large cog turns $30^\circ$ counterclockwise (i.e. 1 hour), the small cog turns $60^\circ$ clockwise (i.e. 2 hours). [asy] fill(arc((0,0),2,30,150)--cycle,lightgrey); draw(arc((0,0),2,30,150),EndArcArrow);label("$30^\circ$",2*dir(150),W); draw(1.8*dir(120)--2*dir(120)); draw(1.8*dir(90)--2*dir(90)); label(rotate(30)*"12",1.56*dir(120)); label(rotate(30)*"1",1.56*dir(90)); draw(arc((0,3),1,-15,-165),EndArcArrow);label("$60^\circ$",dir(-165)+(0,3),W); draw(0.9*dir(-90)+(0,3)--dir(-90)+(0,3)); draw(0.9*dir(-120)+(0,3)--dir(-120)+(0,3)); draw(0.9*dir(-150)+(0,3)--dir(-150)+(0,3)); label(rotate(-60)*"6",.74*dir(-150)+(0,3)); label(rotate(-60)*"5",.74*dir(-120)+(0,3)); label(rotate(-60)*"4",.74*dir(-90)+(0,3)); [/asy] However, in the original problem the large cog does not rotate; it stays where it is. Therefore we must turn the whole diagram above $30^\circ$ clockwise to see what happens when the small cog rolls around it. [asy] fill(arc((0,0),2,30,150)--cycle,lightgrey); draw(arc((0,0),2,30,150)); draw(1.8*dir(90)--2*dir(90)); draw(1.8*dir(60)--2*dir(60)); label("12",1.56*dir(90)); label("1",1.56*dir(60)); pair c=(1.5,sqrt(27)/2); draw(arc(c,1,0,-200),EndArcArrow);label("$90^\circ$",dir(-180)+c,W); draw(0.9*dir(-120)+c--dir(-120)+c); draw(0.9*dir(-150)+c--dir(-150)+c); draw(0.9*dir(-180)+c--dir(-180)+c); label(rotate(-90)*"6",.74*dir(-180)+c); label(rotate(-90)*"5",.74*dir(-150)+c); label(rotate(-90)*"4",.74*dir(-120)+c); [/asy] It turns out that, when the point of tangency moves $30^\circ$ clockwise (one hour), from our point of view the small disk rotates $90^\circ$ clockwise (three hours) around its center. Thus, for the small disk to perform a complete rotation of $360^\circ$ (twelve hours) around its center from our point of view, the point of tangency must move round four hours. So the answer is $\boxed{\textbf{(C) }4 \ \text{o' clock}}$

## Solution 6
We unfold the big clock and draw the small clock. We know that the small clocks arrow will be facing up again at 6 o clock on the unfolded big clock. However, because of the coin rotation paradox, the small clock actually needs to rotate thrice and not twice to go all the way around the big clock, so the answer would be $\boxed{\textbf{(C) }4 \ \text{o' clock}}$ . We now draw corresponding arrows at each hour and fold it back again.

## Solution 7
We can approach this problem with angle measures. As the circumference of the disk is $10\pi,$ and the clock $20 \pi,$ we have that 30 degrees, or the angular measure between hours, of the disk is only 15 degrees of the clock. This yields that every two hour ticks that the clock rotates, on the third one, the ticks will meet. However, the disk must rotate 360 degrees in order to come back to its original position, so the angular measure that the disk has covered relative to the clock is simply $12 \cdot 15 \cdot \frac{2}{3},$ or $120^\circ$ from the 12 starting point, so $\boxed{\textbf{(C) }4 \ \text{o' clock}}$ .
~ab2024

## Solution 8
If the big clock were a flat plane, then the smaller clock could travel $\dfrac{40\pi}{20\pi}=2$ full revolutions.
But we also need to account for rotation. If we mark a red dot on the bottom of the small clock/bottom of the arrow, and then drag it around the clock, the direction of the arrow would still change. After traveling around the big clock, the small clock would travel $1$ full rotation.
Considering these two movements, the small clock travels 3 full rotations around the big clock so the arrow is next pointing upwards at $\dfrac{12 \text{ o'clock}}{3}=\boxed{\textbf{(C) }4 \ \text{o' clock}}$ .
~BakedPotato66

## Solution 9
The center of rotation is in the center of the smaller circle, but extends to the center of the larger circle. That means the circumference of the circle in relation to the arrow is $60 \pi$ . The other circle is $20 \pi$ and so that is $\frac{1}{3}$ . So $\frac{12}{3} = 4$ which is $\boxed{\textbf{(C) }4 \ \text{o' clock}}$ .

## Solution 10 (Astronomy)
Let the center of the disk be Planet X with orbit eccentricity $0$ and the center of the clock be the Sun. Note that the question would then be asking for the solar day of Planet X, rather than the sidereal day. Because planet X is rotating around its axis in the same direction as it is revolving around the Sun, the solar day can be calculated as $d_{solar}=\frac{1}{\frac{1}{y}+\frac{1}{d_{siderial}}}$ , where $y$ is the length of the year of Planet X and $d_{siderial}$ is one sidereal day. It is easy to see that $y=12$ and $d_{siderial}=6$ , therefore the answer is $\frac{1}{\frac{1}{12}+\frac{1}{6}}=\frac{1}{\frac{1}{4}}=\boxed{\textbf{(C) }4 \ \text{o' clock}}$ ~That one kid

## Video Solution 1
https://youtu.be/hPEgOYA4Xq8
~savannahsolver

## Video Solution 2
Video Solution: https://www.youtube.com/watch?v=kCsQbTi3iLU
### See Also
2014 AIME I #10: https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_10
Coin Rotation Paradox: https://en.wikipedia.org/wiki/Coin_rotation_paradox
A related problem from the SAT in 1982 (see Coin Rotation Paradox above) This gives a more rigorous proof by looking at relative velocities and showing that the distance the center of the disk travels equals the total distance the disk rotates. https://www.youtube.com/watch?v=FUHkTs-Ipfg
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .