# 2023 AMC 10B Problem 7

## Problem

Square $ABCD$ is rotated $20^{\circ}$ clockwise about its center to obtain square $EFGH$ , as shown below. What is the degree measure of $\angle EAB$ ?

[asy] size(170); defaultpen(linewidth(0.6)); real r = 25; draw(dir(135)--dir(45)--dir(315)--dir(225)--cycle); draw(dir(135-r)--dir(45-r)--dir(315-r)--dir(225-r)--cycle); label("$A$",dir(135),NW); label("$B$",dir(45),NE); label("$C$",dir(315),SE); label("$D$",dir(225),SW); label("$E$",dir(135-r),N); label("$F$",dir(45-r),E); label("$G$",dir(315-r),S); label("$H$",dir(225-r),W); [/asy]

$\text{(A)}\ 24^{\circ} \qquad \text{(B)}\ 35^{\circ} \qquad \text{(C)}\ 30^{\circ} \qquad \text{(D)}\ 32^{\circ} \qquad \text{(E)}\ 20^{\circ}$

## Solution 1
First, let's call the center of both squares $I$ . Then, $\angle{AIE} = 20$ , and since $\overline{EI} = \overline{AI}$ , $\angle{AEI} = \angle{EAI} = 80$ . Then, we know that $AI$ bisects angle $\angle{DAB}$ , so $\angle{BAI} = \angle{DAI} = 45$ . Subtracting $45$ from $80$ , we get $\boxed{\text{(B)} 35}$
~jonathanzhou18

## Solution 2
First, label the point between $A$ and $H$ point $O$ and the point between $A$ and $H$ point $P$ . We know that $\angle{AOP} = 20$ and that $\angle{A} = 90$ . Subtracting $20$ and $90$ from $180$ , we get that $\angle{APO}$ is $70$ . Subtracting $70$ from $180$ , we get that $\angle{OPB} = 110$ . From this, we derive that $\angle{APE} = 110$ . Since triangle $APE$ is an isosceles triangle, we get that $\angle{EAP} = (180 - 110)/2 = 35$ . Therefore, $\angle{EAB} = 35$ . The answer is $\boxed{\text{(B)} 35}$ .
~Stead (a.k.a. Aaron)

## Solution 3
Call the center of both squares point $O$ , and draw circle $O$ such that it circumscribes the squares. $\angle{EOF} = 90$ and $\angle{BOF} = 20$ , so $\angle{EOB} = 70$ . Since $\angle{EAB}$ is inscribed in arc $\overset \frown {EB}$ , $\angle{EAB} = 70/2 = \boxed{\textbf{(B) }35}$ .
~hpotter2021

## Solution 4
Draw $EA$ : we want to find $\angle EAB$ . Call $P$ the point at which $AB$ and $EH$ intersect. Reflecting $\triangle APE$ over $EA$ , we have a parallelogram. Since $\angle EPB = 70^{\circ}$ , angle subtraction tells us that two of the angles of the parallelogram are $110^{\circ}$ . The other two are equal to $2\angle EAB$ (by properties of reflection).
Since angles on the transversal of a parallelogram sum to $180^{\circ}$ , we have $2\angle EAB + 110 = 180$ , yielding $\angle EAB = \boxed{\textbf{(B) }35}$
-Benedict T (countmath1)

## Solution 5 (Educated Guess)
We call the point where $AB$ and $EH$ intersect I. We can make an educated guess that triangle AEI is isosceles so $AI=EI$ , $\angle AIE = 110^{\circ}$ , $\angle AIH = 20^{\circ}$ , and $\angle EIB = 70^{\circ}$ . So, we get $\angle EAI$ is $(180^{\circ} - 110^{\circ})/2 = \boxed{\textbf{(B) }35}$ .
~aleyang

## Solution 6 (Solution 1 Remastered)
Like in solution 1, we label the center of the squares \( R \).
Draw the lines \( AR \) and \( RE \). Because Vertex \( A \) is just Vertex \( E \) shifted \( 20^\circ \) about the center \( R \), \( \angle ARE = 20^\circ \).
Now, notice how \( AM \) and \( ME \) are the diagonals (or half the diagonals, doesn't really matter) of the squares \( ABCD \) and \( EFGH \) respectively. This implies that \( AM = ME \), and, connecting a new segment \( AE \), we see that \( \triangle ARE \) is isoseles, and \( AR = AE \), implying that \( \angle EAM \cong \angle MEA \). We can easily solve this through the sum of interior angles of a triangle, and we get \( m \angle EAM = m \angle MEA = 80^\circ \).
Because \( AM \) is a diagonal of \( \square ABCD \), that means that \( \angle BAC \) is bisected, and \( \angle MAD = 45^\circ \).
Finally, to find \( \angle EAB \), we are just subtracting \( 80^\circ \) and \( 45^\circ \), giving us \( 80^\circ - 45^\circ = 35^\circ \) or $\boxed{B}$ .
~Pinotation

## Solution 7 (Overkill complex bash)
Let the center be the origin of the complex plane. WLOG, let $A = -1 + i$ . Then, $E = (-1+i)e^{-\frac{i \pi}{9}} = (-\cos(20^\circ) + \sin(20^\circ)) + i(\sin(20^\circ)+\cos(20^\circ))$ . So, $\angle EAB = \arctan(\frac{\sin(20^\circ)+\cos(20^\circ)-1}{-\cos(20^\circ) + \sin(20^\circ)+1})$ , because the slope is just the tangent of the angle. Now, we have a bunch of trig bashing. Let $\theta = 20^\circ$ . Then we have inside the inverse tangent, $\frac{\sin(\theta)+\cos(\theta)-1}{-\cos(\theta)+\sin(\theta)+1}$ . Using $\sin(\theta)=2\cos(\frac{\theta}{2})\sin(\frac{\theta}{2})$ , $\cos(\theta)=\cos^2(\frac{\theta}{2})-\sin^2(\frac{\theta}{2})$ , and the Pythagorean identity, this ultimately simplifies to $\frac{1-\tan(\frac{\theta}{2})}{1+\tan(\frac{\theta}{2})}$ , which can be recognized using the tangent angle subtraction formula as $\tan(45^\circ-\frac{\theta}{2})$ , since $\tan(45^\circ)=1$ . Therefore, inside of the inverse tangent we have $\tan(35^\circ)$ , so the inverse tangent of that is $35^\circ$ , or $\boxed{B}$ .
~vaishnav

## Video Solution by MegaMath
https://www.youtube.com/watch?v=KsAxW53-P0A&t=4s
~megahertz13

## Video Solution 2 by OmegaLearn
https://youtu.be/LI1Xq2onHHg

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=cT-0V4a3FYY

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/EuLkw8HFdk4?si=Te_9kmP_bmBoKrTn&t=1393
~Math-X

## Video Solution
https://youtu.be/R9uCV2KsXc8
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by Interstigation
https://youtu.be/gDnmvcOzxjg?si=cYB6uChy7Ue0UT4L
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .