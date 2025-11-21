# 2002 AIME I Problem 10

## Problem

In the diagram below, angle $ABC$ is a right angle. Point $D$ is on $\overline{BC}$ , and $\overline{AD}$ bisects angle $CAB$ . Points $E$ and $F$ are on $\overline{AB}$ and $\overline{AC}$ , respectively, so that $AE=3$ and $AF=10$ . Given that $EB=9$ and $FC=27$ , find the integer closest to the area of quadrilateral $DCFG$ .

## Solution 1
By the Pythagorean Theorem, $BC=35$ . Letting $BD=x$ we can use the Angle Bisector Theorem on triangle $ABC$ to get $x/12=(35-x)/37$ , and solving gives $BD=60/7$ and $DC=185/7$ .
The area of triangle $AGF$ is $10/3$ that of triangle $AEG$ , since they share a common side and angle, so the area of triangle $AGF$ is $10/13$ the area of triangle $AEF$ .
Since the area of a triangle is $\frac{ab\sin{C}}2$ , the area of $AEF$ is $525/37$ and the area of $AGF$ is $5250/481$ .
The area of triangle $ABD$ is $360/7$ , and the area of the entire triangle $ABC$ is $210$ . Subtracting the areas of $ABD$ and $AGF$ from $210$ and finding the closest integer gives $\boxed{148}$ as the answer.

## Solution 2 Bash
By the Pythagorean Theorem, $BC=35$ . From now on, every number we get will be rounded to two decimal points. Using law of cosines on AEF, EF is around 9.46. Using the angle bisector theorem, GF and DC are 7.28 and (185/7), respectively. We also know the lengths of EG and BD, so a quick Stewart's Theorem for triangles ABC and AEF gives lengths 3.76 and 14.75 for AG and AD, respectively. Now we have all segments of triangles AGF and ADC. Joy! It's time for some Heron's Formula. This gives area 10.95 for triangle AGF and 158.68 for triangle ADC. Subtracting gives us 147.73. Round to the nearest whole number and we get $\boxed{148}$ .
-jackshi2006

## Solution 3 Coordinate Bash
By the Pythagorean Theorem, $BC=35$ . By the Angle Bisector Theorem $BD = 60/7$ and $DC = 185/7$ . We can find the coordinates of F, and use that the find the equation of line EF. Then, we can find the coordinates of G. Triangle $ADC = 1110/7$ and we can find the area triangle $AGF$ with the shoelace theorem, so subtracting that from $ADC$ gives us $\boxed{148}$ as the closest integer.
-jackshi2006

## Solution 4 No Trig
By the Pythagorean Theorem, $BC = 35$ , and by the Angle Bisector Theorem $BD = 60/7$ and $DC = 185/7$ . Draw a perpendicular from $F$ to $\overline{AE}$ . Let the intersection of $F$ and $\overline{AE}$ be $H$ . triangle $AHF$ is similar to $ABC$ by $AA$ similarity. thus, $AF/AC = HF/BC$ . We find that $HF = 350/37$ , so the area of $AEF = 525/37$ . The area of triangle $AGF$ is $10/3$ that of triangle $AEG$ , since they share a common side and angle, so the area of triangle $AGF$ is $10/13$ the area of triangle $AEF$ , so the area of $AGF = 5250/481$ . The area of triangle $ADC$ is $1110/7$ , since the base is $185/7$ and the height is $12$ . Thus, the area of $DCFG$ equals the area of $ADC - AGF$ , or rounded to the nearest integer, $\boxed{148}$
~ PaperMath
These problems are copyrighted © by the Mathematical Association of America.