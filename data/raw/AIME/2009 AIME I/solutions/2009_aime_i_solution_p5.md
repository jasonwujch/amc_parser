# 2009 AIME I Problem 5

## Problem

Triangle $ABC$ has $AC = 450$ and $BC = 300$ . Points $K$ and $L$ are located on $\overline{AC}$ and $\overline{AB}$ respectively so that $AK = CK$ , and $\overline{CL}$ is the angle bisector of angle $C$ . Let $P$ be the point of intersection of $\overline{BK}$ and $\overline{CL}$ , and let $M$ be the point on line $BK$ for which $K$ is the midpoint of $\overline{PM}$ . If $AM = 180$ , find $LP$ .

### Diagram

## Solution 1
Since $K$ is the midpoint of $\overline{PM}$ and $\overline{AC}$ , quadrilateral $AMCP$ is a parallelogram, which implies $AM||LP$ and $\bigtriangleup{AMB}$ is similar to $\bigtriangleup{LPB}$
Thus,
\[\frac {AM}{LP}=\frac {AB}{LB}=\frac {AL+LB}{LB}=\frac {AL}{LB}+1\]
Now let's apply the angle bisector theorem.
\[\frac {AL}{LB}=\frac {AC}{BC}=\frac {450}{300}=\frac {3}{2}\]
\[\frac {AM}{LP}=\frac {AL}{LB}+1=\frac {5}{2}\]
\[\frac {180}{LP}=\frac {5}{2}\]
\[LP=\boxed {072}\]

## Solution 2 (Mass Points)
Using the diagram above, we can solve this problem by using mass points. By angle bisector theorem: \[\frac{BL}{CB}=\frac{AL}{CA}\implies\frac{BL}{300}=\frac{AL}{450}\implies 3BL=2AL\] So, we can weight $A$ as $2$ and $B$ as $3$ and $L$ as $5$ . Since $K$ is the midpoint of $A$ and $C$ , the weight of $A$ is equal to the weight of $C$ , which equals $2$ . Also, since the weight of $L$ is $5$ and $C$ is $2$ , we can weight $P$ as $7$ .
By the definition of mass points, \[\frac{LP}{CP}=\frac{2}{5}\implies LP=\frac{2}{5}CP\] By vertical angles, angle $MKA =$ angle $PKC$ . Also, it is given that $AK=CK$ and $PK=MK$ .
By the SAS congruence, $\triangle MKA$ = $\triangle PKC$ . So, $MA$ = $CP$ = $180$ . Since $LP=\frac{2}{5}CP$ , $LP = \frac{2}{5}(180) = \boxed{072}$

## Solution 3 (Law of Cosines Bash)
Using the diagram from solution $1$ , we can also utilize the fact that $AMCP$ forms a parallelogram. Because of that, we know that $AM = CP = 180$ .
Applying the angle bisector theorem to $\triangle CKB$ , we get that $\frac{KP}{PB} = \frac{225}{300} = \frac{3}{4}.$ So, we can let $MK = KP = 3x$ and $BP = 4x$ .
Now, apply law of cosines on $\triangle CKP$ and $\triangle CPB.$
If we let $\angle KCP = \angle PCB = \alpha$ , then the law of cosines gives the following system of equations:
\[9x^2 = 225^2 + 180^2 - 2\cdot 225 \cdot 180 \cdot \cos \alpha\] \[16x^2 = 180^2 + 300^2 - 2 \cdot 180 \cdot 300 \cdot \cos \alpha.\]
Bashing those out, we get that $x = 15 \sqrt{13}$ and $\cos \alpha = \frac{7}{10}.$
Since $\cos \alpha = \frac{7}{10}$ , we can use the double angle formula to calculate that $\cos \left(2 \alpha \right) = -\frac{1}{50}.$
Now, apply Law of Cosines on $\triangle ABC$ to find $AB$ .
We get: \[AB^2 = 450^2 + 300^2 - 2 \cdot 450 \cdot 300 \cdot \left(- \frac{1}{50} \right).\]
Bashing gives $AB = 30 \sqrt{331}.$
From the angle bisector theorem on $\triangle ABC$ , we know that $\frac{AL}{BL} = \frac{450}{300} = \frac{3}{2}.$ So, $AL = 18 \sqrt{331}$ and $BL = 12 \sqrt{331}.$
Now, we apply Law of Cosines on $\triangle ALC$ and $\triangle BLC$ in order to solve for the length of $LC$ .
We get the following system:
\[(18 \sqrt{331})^2 = 450^2 + LC^2 - 2 \cdot 450 \cdot LC \cdot \frac{7}{10}\] \[(12 \sqrt{331})^2 = LC^2 + 300^2 - 2 \cdot 300 \cdot LC \cdot \frac{7}{10}\]
The first equation gives $LC = 252$ or $378$ and the second gives $LC = 252$ or $168$ .
The only value that satisfies both equations is $LC = 252$ , and since $LP = LC - PC$ , we have \[LC = 252 - 180 = \boxed{072}.\]

## Video Solution
https://youtu.be/2Xzjh6ae0MU
~IceMatrix

## Video Solution
https://youtu.be/kALrIDMR0dg
~Shreyas S

## Solution 4(Area Ratios)
Note that we are given that $\overline{MK} = \overline{KP}$ , that $\overline{AK} = \overline{CK}.$ Note then that $\angle MKA = \angle CKB$ by vertical angles. From this, we have $\triangle MKA \cong PKC.$ This means that $\overline{CP}$ is 180. Applying angle bisector theorem on $\triangle ACB$ gives $\frac{\overline{AL}}{\overline{LB}} = \frac{450}{300} = \frac{3}{2}.$ Applying it on $\triangle KCB$ yields \[\frac{\overline{KP}}{\overline{PB}} = \frac{225}{300} = \frac{3}{4}\] Now we can proceed with area ratios. Suppose the area of $\triangle ACB = A.$ This means that \[[\triangle AKL] = \left(\frac{225}{225+225}\right)\left(\frac{3}{5}\right)A = \frac{3}{10}A\] Continuing on $\triangle LPB$ we have \[[\triangle LPB] = \left(\frac{2}{2+3}\right)\left(\frac{1}{2}\right)\left(\frac{4}{4+3}\right) = \frac{4}{35}A\] Since $\overline{AK}=\overline{KC}$ $[\triangle KPL] = [\triangle AKB]-[\triangle AKL] - [\triangle LPB] = \frac{1}{2}A - \frac{3}{10}A - \frac{4}{35}A = \frac{3}{35}A.$ Area ratios on $\triangle KCP$ yield $[\triangle KCP] = \left(\frac{1}{2}\right)\left(\frac{3}{3+4}\right) = \frac{3}{14}.$ Now, suppose $\overline{LP} = x.$ We have that the ratio of areas of $\triangle LKP$ and $\triangle PKC$ is $\frac{x}{180}$ and is also $\frac{\frac{3}{35}}{\frac{3}{14}}$ and equating these gives \[x = \boxed{72}\]
These problems are copyrighted © by the Mathematical Association of America.