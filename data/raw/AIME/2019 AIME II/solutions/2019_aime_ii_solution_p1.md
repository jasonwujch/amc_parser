# 2019 AIME II Problem 1

## Problem

Two different points, $C$ and $D$ , lie on the same side of line $AB$ so that $\triangle ABC$ and $\triangle BAD$ are congruent with $AB = 9$ , $BC=AD=10$ , and $CA=DB=17$ . The intersection of these two triangular regions has area $\tfrac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
[asy] unitsize(10); pair A = (0,0); pair B = (9,0); pair C = (15,8); pair D = (-6,8); pair E = (-6,0); draw(A--B--C--cycle); draw(B--D--A); label("$A$",A,dir(-120)); label("$B$",B,dir(-60)); label("$C$",C,dir(60)); label("$D$",D,dir(120)); label("$E$",E,dir(-135)); label("$9$",(A+B)/2,dir(-90)); label("$10$",(D+A)/2,dir(-150)); label("$10$",(C+B)/2,dir(-30)); label("$17$",(D+B)/2,dir(60)); label("$17$",(A+C)/2,dir(120)); draw(D--E--A,dotted); label("$8$",(D+E)/2,dir(180)); label("$6$",(A+E)/2,dir(-90)); [/asy] - Diagram by Brendanb4321
Extend $AB$ to form a right triangle with legs $6$ and $8$ such that $AD$ is the hypotenuse and connect the points $CD$ so that you have a rectangle. (We know that $\triangle ADE$ is a $6-8-10$ , since $\triangle DEB$ is an $8-15-17$ .) The base $CD$ of the rectangle will be $9+6+6=21$ . Now, let $O$ be the intersection of $BD$ and $AC$ . This means that $\triangle ABO$ and $\triangle DCO$ are with ratio $\frac{21}{9}=\frac73$ . Set up a proportion, knowing that the two heights add up to 8. We will let $y$ be the height from $O$ to $DC$ , and $x$ be the height of $\triangle ABO$ . \[\frac{7}{3}=\frac{y}{x}\] \[\frac{7}{3}=\frac{8-x}{x}\] \[7x=24-3x\] \[10x=24\] \[x=\frac{12}{5}\]
This means that the area is $A=\tfrac{1}{2}(9)(\tfrac{12}{5})=\tfrac{54}{5}$ . This gets us $54+5=\boxed{059}.$
-Solution by the Math Wizard, Number Magician of the Second Order, Head of the Council of the Geometers

## Solution 2
Using the diagram in Solution 1, let $E$ be the intersection of $BD$ and $AC$ . We can see that angle $C$ is in both $\triangle BCE$ and $\triangle ABC$ . Since $\triangle BCE$ and $\triangle ADE$ are congruent by AAS, we can then state $AE=BE$ and $DE=CE$ . It follows that $BE=AE$ and $CE=17-BE$ . We can now state that the area of $\triangle ABE$ is the area of $\triangle ABC-$ the area of $\triangle BCE$ . Using Heron's formula, we compute the area of $\triangle ABC=36$ . Using the Law of Cosines on angle $C$ , we obtain
\[9^2=17^2+10^2-2(17)(10)cosC\] \[-308=-340cosC\] \[cosC=\frac{308}{340}\] (For convenience, we're not going to simplify.)
Applying the Law of Cosines on $\triangle BCE$ yields \[BE^2=10^2+(17-BE)^2-2(10)(17-BE)cosC\] \[BE^2=389-34BE+BE^2-20(17-BE)(\frac{308}{340})\] \[0=389-34BE-(340-20BE)(\frac{308}{340})\] \[0=389-34BE+\frac{308BE}{17}\] \[0=81-\frac{270BE}{17}\] \[81=\frac{270BE}{17}\] \[BE=\frac{51}{10}\] This means $CE=17-BE=17-\frac{51}{10}=\frac{119}{10}$ . Next, apply Heron's formula to get the area of $\triangle BCE$ , which equals $\frac{126}{5}$ after simplifying. Subtracting the area of $\triangle BCE$ from the area of $\triangle ABC$ yields the area of $\triangle ABE$ , which is $\frac{54}{5}$ , giving us our answer, which is $54+5=\boxed{059}.$ -Solution by flobszemathguy

## Solution 3 (Very quick)
[asy] unitsize(10); pair A = (0,0); pair B = (9,0); pair C = (15,8); pair D = (-6,8); draw(A--B--C--cycle); draw(B--D--A); label("$A$",A,dir(-120)); label("$B$",B,dir(-60)); label("$C$",C,dir(60)); label("$D$",D,dir(120)); label("$9$",(A+B)/2,dir(-90)); label("$10$",(D+A)/2,dir(-150)); label("$10$",(C+B)/2,dir(-30)); label("$17$",(D+B)/2,dir(60)); label("$17$",(A+C)/2,dir(120)); draw(D--(-6,0)--A,dotted); label("$8$",(D+(-6,0))/2,dir(180)); label("$6$",(A+(-6,0))/2,dir(-90)); draw((4.5,0)--(4.5,2.4),dotted); label("$h$", (4.5,1.2), dir(180)); label("$4.5$", (6,0), dir(90)); [/asy] - Diagram by Brendanb4321 extended by Duoquinquagintillion
Begin with the first step of solution 1, seeing $AD$ is the hypotenuse of a $6-8-10$ triangle and calling the intersection of $DB$ and $AC$ point $E$ . Next, notice $DB$ is the hypotenuse of an $8-15-17$ triangle. Drop an altitude from $E$ with length $h$ , so the other leg of the new triangle formed has length $4.5$ . Notice we have formed similar triangles, and we can solve for $h$ .
\[\frac{h}{4.5} = \frac{8}{15}\] \[h = \frac{36}{15} = \frac{12}{5}\]
So $\triangle ABE$ has area \[\frac{ \frac{12}{5} \cdot 9}{2} = \frac{54}{5}\] And $54+5=\boxed{059}.$ - Solution by Duoquinquagintillion

## Solution 4
Let $a = \angle{CAB}$ . By Law of Cosines, \[\cos a = \frac{17^2+9^2-10^2}{2*9*17} = \frac{15}{17}\] \[\sin a = \sqrt{1-\cos^2 a} = \frac{8}{17}\] \[\tan a = \frac{8}{15}\] \[A = \frac{1}{2}* 9*\frac{9}{2}\tan a = \frac{54}{5}\] And $54+5=\boxed{059}.$
- by Mathdummy

## Solution 5
Because $AD = BC$ and $\angle BAD = \angle ABC$ , quadrilateral $ABCD$ is cyclic. So, Ptolemy's theorem tells us that \[AB \cdot CD + BC \cdot AD = AC \cdot BD \implies 9 \cdot CD + 10^2 = 17^2 \implies CD = 21.\]
From here, there are many ways to finish which have been listed above. If we let $AB \cap CD = P$ , then \[\triangle APB \sim \triangle CPD \implies \frac{AP}{AB} = \frac{CP}{CD} \implies \frac{AP}{9} = \frac{17-AP}{21} \implies AP = 5.1.\]
Using Heron's formula on $\triangle ABP$ , we see that \[[ABC] = \sqrt{9.6(9.6-5.1)(9.6-5.1)(9.6-9)} = 10.8 = \frac{54}{5}.\]
Thus, our answer is $059$ . ~a.y.711

## Solution 6
Let $A=(0,0), B=(9,0)$ . Now consider $C$ , and if we find the coordinates of $C$ , by symmetry about $x=4.5$ , we can find the coordinates of D.
So let $C=(a,b)$ . So the following equations hold:
$\sqrt{(a-9)^2+(b)^2}=17$ .
$\sqrt{a^2+b^2}=10$ .
Solving by squaring both equations and then subtracting one from the other to eliminate $b^2$ , we get $C=(-6,8)$ because $C$ is in the second quadrant.
Now by symmetry, $D=(16, 8)$ .
So now you can proceed by finding the intersection and then calculating the area directly. We get $\boxed{059}$ .
~hastapasta

## Solution 7
Since the figure formed by connecting the vertices of the congruent triangles is a isoceles trapezoid, by Ptolemys, the other base of the trapezoid is $21.$ Then, dropping altitudes to the base of $21$ and using pythagorean theorem, we have the height is $8,$ and we can use similar triangles to finish.

## Solution 8 (Very, very, quick, but for observant people only)
[asy] //Made by Afly. I used some resources. //Took me 10 min to get everything right. import olympiad; unitsize(18); pair A = (0,0); pair B = (0,8); pair C = (6,0); pair D = (15,0); pair E = (21,0); pair F = (21,8); pair G = (21/2,0); pair H = intersectionpoints(B--D,C--F)[0]; pen dash1 = linetype(new real [] {9,9})+linewidth(1); pen solid1 = linetype(new real [] {9,0})+linewidth(1); pen dash2 = linetype(new real [] {3,3})+linewidth(1); fill(C--G--H--cycle,rgb(3/4,1/4,1/4)); fill(D--G--H--cycle,rgb(3/4,3/4,1/4)); draw(C--A--B,dash1); draw(C--B--D--C,solid1); draw(F--E--D,dash1); draw(F--D--C--F,solid1); draw(G--H,dash2); draw(brace(D+dir(270),A+dir(270)),solid1); draw(brace(D,C),solid1); draw(A--A+2*dir(180),dash1,EndArrow); draw(E--E+2*dir(0),dash1,EndArrow); pair L1 = (15/2,-7/2); pair L2 = (21/2,-13/8); label("15",L1); label("8",A--B,W); label("6",A--C,S); label("10",B--C,SW); label("17",B--D,NE); label("9",L2); label("4.5",G--D,S); label("2.4",G--H,W); markscalefactor = 1/16; draw(rightanglemark(H,G,D)); draw(rightanglemark(B,A,C)); draw(rightanglemark(D,E,F)); label("A",C,SW); label("B",D,SE); label("C",B,NW); label("D",F,NE); label("E",A,SW); label("F",E,SE); label("G",G,NW); label("H",H,N); [/asy]
First, let's define H as the intersection of CB and DA, and define G as the midpoint of AB. Next, let E and F be the feet of the perpendicular lines from C and D to line AB respectively. We get a pleasing line of symmetry HG where A maps to B, C maps to D, and E maps to F. We notice that 8-15-17 and 8-6-10 are both pythagorean triples and we test that theory. Then, we find AB = 15 - 6 = 9 and GB = 4.5. Since △CEB~△HGB, we find that HG = 2.4. Then, the area of △HGB is 5.4 and the total overlap is 10.8 = 54/5. Noting that GCD(54,5)=1, we add them to get 59.
Note: I omitted some computation
~ Afly ( talk )
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .