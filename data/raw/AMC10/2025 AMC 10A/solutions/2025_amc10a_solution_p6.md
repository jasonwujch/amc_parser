# 2025 AMC 10A Problem 6

## Problem

In an equilateral triangle each interior angle is trisected by a pair of rays. The intersection of the interiors of the middle 20°-angle at each vertex is the interior of a convex hexagon. What is the degree measure of the smallest angle of this hexagon?

$\textbf{(A) } 80 \qquad\textbf{(B) } 90 \qquad\textbf{(C) } 100 \qquad\textbf{(D) } 110 \qquad\textbf{(E) } 120$

### Diagram

[asy] /* AMC 10A 2025 Problem — Equilateral Triangle Trisectors Diagram */ import olympiad; size(220); pair A = (0,0); pair B = (10,0); pair C = (5,8.660254037844386); // height = 5*sqrt(3) // Triangle draw(A--B--C--cycle, linewidth(1)); // Mark vertices dot("$A$", A, SW); dot("$B$", B, SE); dot("$C$", C, N); // Length of trisectors (visual only) real L = 8.8; // Trisectors from each vertex (20° and 40° offsets from sides) draw(A--(A + L*dir(20)), blue+linewidth(0.8)); draw(A--(A + L*dir(40)), blue+linewidth(0.8)); draw(B--(B + L*dir(140)), blue+linewidth(0.8)); draw(B--(B + L*dir(160)), blue+linewidth(0.8)); draw(C--(C + L*dir(260)), blue+linewidth(0.8)); draw(C--(C + L*dir(280)), blue+linewidth(0.8)); // Intersection points (precomputed numerically) pair P1 = (4.07604, 3.4202); pair P2 = (5, 4.1955); pair P3 = (5.92396, 3.4202); pair P4 = (6.13341, 2.23238); pair P5 = (5, 1.81985); pair P6 = (3.86659, 2.23238); // Hexagon interior filldraw(P1--P2--P3--P4--P5--P6--cycle, lightred+opacity(0.4), red+linewidth(0.8)); // Mark intersection region label("$P_1$", P1, NW); label("$P_2$", P2, N); label("$P_3$", P3, NE); label("$P_4$", P4, SE); label("$P_5$", P5, S); label("$P_6$", P6, SW); label("Hexagon formed by the middle 20° trisectors", (5, -1.2)); [/asy]

~Avs2010

~i_am_not_suk_at_math

## Solution 1
Assume you have a diagram in front of you.
Because each angle of the triangle is trisected, we have 9 $20^\circ$ angles. Using a side of the triangle as a base, we have an isosceles triangle with two $20^\circ$ angles. Using this we can show that the third angle is $140^\circ$ .
Following that, we use the principle of vertical angles to show that one angle of the hexagon is $140^\circ$ . And with rotational symmetry, three. The average of all 6 angles has to be $120^\circ$ , so the answer is $\boxed{\textbf{(C) }100}$ - SpectralScholar

## Solution 1.5
Note that the hexagon’s interior angle sum is $720$ , and due to 3-way symmetry there are 3 wider(bigger) angles and 3 smaller ones. We can split these angles into 3 groups, each with one big angle and one small angle that sum up to $720/3 = 240$ degrees. Seeing this, we can eliminate answer choice $(E)120$ as it is asking for the smallest angle. Plugging in the other answer choices yields that only option C with a big angle of $140$ and a small angle of $100$ keeps the adjacent triangle’s interior angles sum equal to $180$ . So the answer is $(C)100$ (Draw a diagram and draw supplementary angles to figure out the sum of the adjacent triangle’s interior angles.)
-Amon26

## Solution 2
It is obvious that of the 6 angles inside the convex hexagon, there are only two different angle measures, 3 of one and 3 of another. A convex quadrilateral formed by the 2 rays of any angle in the equilateral triangle and two sides of the convex hexagon will have a total degree of 360.
Therefore, we have: $3a+3b=720 \implies a+b=240$ (total sum of all angles in a convex hexagon is 720) and also $20+2a+b=360 \implies 2a+b=340$ (the rays will form an inner angle of $\frac{60}{3}=20$ degrees). Subtracting the two equations yields $a=100$ and $b=140$ . Hence our smallest angle in this convex hexagon is $\boxed{\textbf{(C) }100}$ . ~hxve

## Solution 3 (cheese)
Notice that only answer choices $(a)$ and $(c)$ sum to 180, a familiar number, and since $(a)$ is not a common answer, choose $(c)$ Note: this is a super informal way to do this, use only if you can't draw a picture or have no idea. 17:51, 6 November 2025 (EST)~Pungent_Muskrat

## Solution 4 [SIMPLE: ONLY ISOSCELES TRIANGLES]
https://imgur.com/a/Hm7Bybf
Angle A is split into three so the triangle $AEB$ is an isosceles triangle because the bottom angles A and B are congruent and both $20^\circ$ .
Therefore, angle E is $140^\circ$ , and the vertical angle in the hexagon is also $140^\circ$ .
Now find G. Triangle $CJD$ is isosceles with angles $C$ and $D$ being $80^\circ$ because angle J in that triangle is $20^\circ$ .
Now angles $C$ , $D$ , and $E$ are known and sum to $80 + 80 + 140 = 300$ .
The pentagon $DCFE$ and its other vertex (not named in my image) sum to $540^\circ$ .
So subtracting angles $C$ , $D$ , $E$ , and knowing that $F$ (let it be $x$ ) is congruent (due to symmetry) to the other vertex angle (not named in my image), we have: \[x + x = 240 \implies x = 120^\circ.\]
Thus, angle $G$ is $100^\circ$ because of triangle $FGE$ .
Now find H. In isosceles triangle $AHB$ , angles $A$ and $B$ are $40^\circ$ , so angle $H$ is $100^\circ$ .
Now find I. The red hexagon’s interior angles sum to $720^\circ$ , and angle $I$ is congruent to the angle across from it by symmetry.
Let $I$ and its symmetric angle be $x$ . Then: \[2x + 140(E) + 2(100)(G\ \&\ \text{its symmetry}) + 100(H) = 720\] \[\implies x = 140^\circ.\]
The smallest angle is $100^\circ$ .
~PUER_137

## Solution 5 [Most outer triangle]
Using the outside triangle made by a trisection, we know that two of the angles are $20^\circ$ and $60^\circ,$ it follows that the third angle in the triangle, the foot of a trisection is $100^\circ.$
We then take a different triangle, that utilizes two of the same lines as the first triangle we examined and also has the $100^\circ$ angle. This time, we can use the $40^\circ$ angle made by two of the trisections, and we get a triangle with angles $40^\circ, 40^\circ, 100^\circ.$
We can look at a dart-like figure (inverted kite) and we get by symmetry, the angle opposite of the initial $40^\circ$ angle is also $40^\circ,$ there is also the middle angle formed by the trisection, $20^\circ.$ Using the dart theorem (I don't know why this isn't a thing when I search it up) we find that one angle in the hexagon is $100^\circ$ and by symmetry, that is the smallest angle, so the answer is $\boxed{\textbf{(C) }100}$
~happyfish0922

## Video Solution
https://youtu.be/l1RY_C20Q2M

## Chinese Video Solution
https://www.bilibili.com/video/BV1SV2uBtESe/
~metrixgo

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution (Done in 1 Min)
https://youtu.be/qVm7neHfDrI?si=n7nLnWY_p1SLXoxr ~ Pi Academy

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by Daily Dose of Math
https://youtu.be/gPh9w3X3QSw
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .