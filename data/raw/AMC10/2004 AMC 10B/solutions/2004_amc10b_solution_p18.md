# 2004 AMC 10B Problem 18

## Problem

In the right triangle $\triangle ACE$ , we have $AC=12$ , $CE=16$ , and $EA=20$ . Points $B$ , $D$ , and $F$ are located on $AC$ , $CE$ , and $EA$ , respectively, so that $AB=3$ , $CD=4$ , and $EF=5$ . What is the ratio of the area of $\triangle DBF$ to that of $\triangle ACE$ ?

[asy] unitsize(0.5cm); defaultpen(0.8); pair C=(0,0), A=(0,12), E=(20,0); draw(A--C--E--cycle); pair B=A + 3*(C-A)/length(C-A); pair D=C + 4*(E-C)/length(E-C); pair F=E + 5*(A-E)/length(A-E); draw(B--D--F--cycle); label("$A$",A,N); label("$B$",B,W); label("$C$",C,SW); label("$D$",D,S); label("$E$",E,SE); label("$F$",F,NE); label("$3$",A--B,W); label("$9$",C--B,W); label("$4$",C--D,S); label("$12$",D--E,S); label("$5$",E--F,NE); label("$15$",F--A,NE); [/asy]

$\mathrm{(A) \ } \frac{1}{4} \qquad \mathrm{(B) \ } \frac{9}{25} \qquad \mathrm{(C) \ } \frac{3}{8} \qquad \mathrm{(D) \ } \frac{11}{25} \qquad \mathrm{(E) \ } \frac{7}{16}$

## Solution 1 (Trigonometry)
Let $x = [DBF]$ . Because $\triangle ACE$ is divided into four triangles, $[ACE] = [BCD] + [ABF] + [DEF] + x$ .
Because of $SAS$ triangle area, $\frac12 \cdot 12 \cdot 16 = \frac12 \cdot 9 \cdot 4 + \frac12 \cdot 3 \cdot 15 \cdot \sin(\angle A) + \frac12 \cdot 5 \cdot 12 \cdot \sin(\angle E) + x$ .
$\sin(\angle A) = \frac{16}{20}$ and $\sin(\angle E) = \frac{12}{20}$ , so $96 = 18 + 18 + 18 + x$ .
$x = 42$ , so $\frac{[DBF]}{[ACE]} = \frac{42}{96} = \boxed{\textbf{(E)}\frac 7{16}}$ .

## Solution 2
First of all, note that $\frac{AB}{AC} = \frac{CD}{CE} = \frac{EF}{EA} = \frac 14$ , and therefore $\frac{BC}{AC} = \frac{DE}{CE} = \frac{FA}{EA} = \frac 34$ .
Draw the height from $F$ onto $AB$ as in the picture below:
[asy] unitsize(0.5cm); defaultpen(0.8); pair C=(0,0), A=(0,12), E=(20,0); draw(A--C--E--cycle); pair B=A + 3*(C-A)/length(C-A); pair D=C + 4*(E-C)/length(E-C); pair F=E + 5*(A-E)/length(A-E); draw(B--D--F--cycle); label("$A$",A,N); label("$B$",B,W); label("$C$",C,SW); label("$D$",D,S); label("$E$",E,SE); label("$F$",F,NE); label("$3$",A--B,W); label("$9$",0.5*C + 0.5*B,4*W); label("$4$",C--D,S); label("$12$",D--E,S); label("$5$",E--F,NE); label("$15$",F--A,NE); pair G = intersectionpoint(F -- (F-(100,0)), A--C); draw(F--G, dashed); label("$G$",G,W); [/asy]
Now consider the area of $\triangle ABF$ . Clearly the triangles $\triangle AFG$ and $\triangle AEC$ are similar, as they have all angles equal. Their ratio is $\frac {AF}{AE} = \frac 34$ , hence $FG = \frac 34 \cdot CE$ . Now the area $S_{ABF}$ of $\triangle ABF$ can be computed as $S_{ABF} = \frac 12 \cdot AB \cdot FG$ = $\frac 12 \cdot \left( \frac 14 \cdot AC \right) \cdot \left( \frac 34 \cdot EC \right) = \frac 14 \cdot \frac 34 \cdot S_{ACE}$ .
Similarly we can find that $S_{BCD} = S_{DEF} = \frac 3{16}\cdot S_{ACE}$ as well.
Hence $S_{BDF} = S_{ACE} - 3\cdot\left( \frac 3{16} \cdot S_{ACE} \right) = \frac 7{16} \cdot S_{ACE}$ , and the answer is $\frac{S_{BDF}}{S_{ACE}} = \boxed{\frac 7{16}}$ .

## Solution 3 (Coordinate Geometry)
We will put triangle ACE on a xy-coordinate plane with C being the origin. The area of triangle ACE is 96. To find the area of triangle DBF, let D be (4, 0), let B be (0, 9), and let F be (12, 3). You can then use the shoelace theorem to find the area of DBF, which is 42. $\frac {42}{96} = \boxed{\frac 7{16}}$

## Solution 4
You can also place a point $X$ on $CE$ such that $CX$ is $12$ , creating trapezoid $CBFX$ . Then, you can find the area of the trapezoid, subtract the area of the two right triangles $DFX$ and $BCD$ , divide by the area of $ABC$ , and get the ratio of $7/16$ .

## Solution 5
It is well known that for when two triangles share an angle, the two sides around the shared angle is proportional to the areas of each of the two triangles.
We can find all the ratios of the triangles except for $\triangle{BDF}$ and then subtract from $1.$
In this case, we have $\triangle{ABF}$ sharing $\angle{A}$ with $\triangle{ACE}$ .
Therefore, we have $\frac{[ABF]}{[ACE]}=\frac{AB}{AC} \cdot \frac{AF}{AE} = \frac{3}{12} \cdot \frac{15}{20} = \frac{3}{16}.$
Also note that $\triangle{EFD}$ shares $\angle{E}$ with $\triangle{EAC}$ .
Therefore, we have $\frac{[EFD]}{[EAC]}=\frac{ED}{EC} \cdot \frac{EF}{EA} = \frac{12}{16} \cdot \frac{5}{20} = \frac{3}{16}.$
Lastly, note that $\triangle{CDB}$ shares $\angle{C}$ with $\triangle{CAE}$ .
Therefore, we have $\frac{[CDB]}{[CAE]}=\frac{CD}{CE} \cdot \frac{CB}{CA} = \frac{9}{12} \cdot \frac{4}{16} = \frac{3}{16}.$
Thus, the ratio of $\triangle{DBF}$ to $\triangle{ACE}$ is $1- \left( \frac{3}{16}+\frac{3}{16}+\frac{3}{16} \right)=1-\frac{9}{16}=\boxed{\textbf{(E)} \frac {7}{16}}$
~mathboy282

## Solution 6 (Wooga Looga Theorem)
We know that $\frac{CB}{BA}=\frac{AF}{FE}=\frac{ED}{DC}=3$ , so by the The Devil's Triangle we have $\frac{[DBF]}{[ACE]}=\frac{3^2-3+1}{(3+1)^2}=\boxed{\frac7{16}}$ .
~jasperE3
STEP BY STEP SOLUTION BY SCHOLARS FOUNDATION https://youtu.be/NlYJJ8GU7LE?si=v4C5W_y11GHdeVIt&t=481
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .