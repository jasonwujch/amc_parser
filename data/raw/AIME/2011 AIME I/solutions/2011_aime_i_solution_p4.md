# 2011 AIME I Problem 4

## Problem

In triangle $ABC$ , $AB=125$ , $AC=117$ and $BC=120$ . The angle bisector of angle $A$ intersects $\overline{BC}$ at point $L$ , and the angle bisector of angle $B$ intersects $\overline{AC}$ at point $K$ . Let $M$ and $N$ be the feet of the perpendiculars from $C$ to $\overline{BK}$ and $\overline{AL}$ , respectively. Find $MN$ .

## Solution 1
Extend ${CM}$ and ${CN}$ such that they intersect line ${AB}$ at points $P$ and $Q$ , respectively. [asy] defaultpen(fontsize(10)+0.8); size(200); pen p=fontsize(9)+linewidth(3); pair A,B,C,D,K,L,M,N,P,Q; A=origin; B=(125,0); C=IP(CR(A,117),CR(B,120)); L=extension(B,C,A,bisectorpoint(B,A,C)); K=extension(A,C,B,bisectorpoint(C,B,A)); M=foot(C,B,K); N=foot(C,A,L); draw(A--B--C--A); draw(A--L^^B--K, gray+dashed+0.5); draw(M--C--N^^N--extension(A,B,C,N)^^M--extension(A,B,C,M), gray+0.5); dot("$A$",A,dir(200),p); dot("$B$",B,right,p); dot("$C$",C,up,p); dot("$L$",L,2*dir(70),p); dot("$N$",N,2*dir(-90),p); dot("$M$",M,2*dir(-90),p); dot("$P$",extension(A,B,C,M),2*down,p); dot("$Q$",extension(A,B,C,N),2*down,p); label("$125$",A--B,down,fontsize(10)); label("$117$",A--C,2*dir(130),fontsize(10)); label("$120$",B--C,1.5*dir(30),fontsize(10)); [/asy] Since ${BM}$ is the angle bisector of angle $B$ and ${CM}$ is perpendicular to ${BM}$ , $\triangle BCP$ must be an isoceles triangle, so $BP=BC=120$ , and $M$ is the midpoint of ${CP}$ . For the same reason, $AQ=AC=117$ , and $N$ is the midpoint of ${CQ}$ . Hence $MN=\tfrac 12 PQ$ . Since \[PQ=BP+AQ-AB=120+117-125=112,\] so $MN=\boxed{056}$ .

## Solution 2
Let $I$ be the incenter of $ABC$ . Since $I$ lies on $BM$ and $AN$ , $IM \perp MC$ and $IN \perp NC$ , so $\angle IMC + \angle INC = 180^\circ$ . This means that $CMIN$ is a cyclic quadrilateral. By the Law of Sines, $\frac{MN}{\sin \angle MIN} = \frac{2R}{\sin \angle CMI} = 2R = CI$ , where $R$ is the radius of the circumcircle of $CMIN$ . Since $\sin \angle MIN = \sin \angle BIA = \sin (90^\circ + \tfrac 12 \angle BCA) = \cos \tfrac 12 \angle BCA = \cos \angle BCI$ , we have that $MN = CI \cdot \sin \angle MIN = CI \cdot \cos \angle BCI$ . Letting $H$ be the point of contact of the incircle of $ABC$ with side $BC$ , we have $MN = CI \cdot \cos \angle BCI = CI \cdot \frac{CH}{CI} = CH$ . Thus, $MN = s - AB = \frac{117+120-125}{2}=\boxed{056}$ .

## Solution 3 (Bash)
Project $I$ onto $AC$ and $BC$ as $D$ and $E$ . $ID$ and $IE$ are both in-radii of $\triangle ABC$ so we get right triangles with legs $r$ (the in-radius length) and $s - c = 56$ . Since $IC$ is the hypotenuse for the 4 triangles ( $\triangle INC, \triangle IMC, \triangle IDC,$ and $\triangle IEC$ ), $C, D, M, I, N, E$ are con-cyclic on a circle we shall denote as $\omega$ which is also the circumcircle of $\triangle CMN$ and $\triangle CDE$ . To find $MN$ , we can use the Law of Cosines on $\angle MON \implies MN^2 = 2R^2(1 - \cos{2\angle MCN})$ where $O$ is the center of $\omega$ . Now, the circumradius $R$ can be found with Pythagorean Theorem with $\triangle CDI$ or $\triangle CEI$ : $r^2 + 56^2 = (2R)^2$ . To find $r$ , we can use the formula $rs = [ABC]$ and by Heron's, $[ABC] = \sqrt{181 \cdot 61 \cdot 56 \cdot 64} \implies r = \sqrt{\frac{61 \cdot 56 \cdot 64}{181}} \implies 2R^2 = \frac{393120}{181}$ . To find $\angle MCN$ , we can find $\angle MIN$ since $\angle MCN = 180 - \angle MIN$ . $\angle MIN = \angle MIC + \angle NIC = 180 - \angle BIC + 180 - \angle AIC = 180 - (180 - \frac{\angle A + \angle C}{2}) + 180 - (180 - \frac{\angle B + \angle C}{2}) = \frac{\angle A + \angle B + \angle C}{2} + \frac{\angle C}{2}$ . Thus, $\angle MCN = 180 - \frac{\angle A + \angle B + \angle C}{2} - \frac{\angle C}{2}$ and since $\angle A + \angle B + \angle C = 180$ , we have $\angle A + \angle B + \angle C - \frac{\angle A + \angle B + \angle C}{2} - \frac{\angle C}{2} = \frac{\angle A + \angle B}{2}$ . Plugging this into our Law of Cosines (LoC) formula gives $MN^2 = 2R^2(1 - \cos{\angle A + \angle B}) = 2R^2(1 + \cos{\angle C})$ . To find $\cos{\angle C}$ , we use LoC on $\triangle ABC \implies \cos{\angle C} = \frac{120^2 + 117^2 - 125^2}{2 \cdot 117 \cdot 120} = \frac{41 \cdot 19}{117 \cdot 15}$ . Our formula now becomes $MN^2 = \frac{393120}{181} + \frac{2534}{15 \cdot 117}$ . After simplifying, we get $MN^2 = 3136 \implies MN = \boxed{056}$ .
--lucasxia01

## Solution 4
Because $\angle CMI = \angle CNI = 90$ , $CMIN$ is cyclic.
Applying Ptolemy's theorem on CMIN:
$CN \cdot MI+CM \cdot IN=CI \cdot MN$
$CI^2(\cos \angle ICN \sin \angle ICM + \cos \angle ICM \sin \angle ICN) = CI \cdot MN$
$MN = CI \sin \angle MCN$ by sine angle addition formula.
$\angle MCN = 180 - \angle MIN = 90 - \angle BCI$ .
Let $H$ be where the incircle touches $BC$ , then $CI \cos \angle BCI = CH = \frac{a+b-c}{2}$ . $a=120, b=117, c=125$ , for a final answer of $\boxed{056}$ .
Note: This is similar to Solution 2 after the first four lines

## Solution 5 (Trig Bash)
Applying Ptolemy's Theorem on the cyclic quadrilateral $MINC$ , we find that
$MI\cdot CN + IN\cdot MC = MN\cdot IC$ .
$\angle CIN=\frac{\alpha+\gamma}{2}$ and $\angle MIC=\frac{\beta+\gamma}{2}$ by the Exterior Angle Theorem, so from properties of sine and cosine, we can find that
$MI=IC\cdot\cos\left(\frac{\beta+\gamma}{2}\right),$ $MC=IC\cdot\sin\left(\frac{\beta+\gamma}{2}\right),$ $IN=IC\cdot\cos\left(\frac{\alpha+\gamma}{2}\right),$ $CN=IC\cdot\sin\left(\frac{\alpha+\gamma}{2}\right).$
Plugging in the values and simplifying results in $MN = IC\cdot\sin\left(\frac{\alpha+\beta+2\gamma}{2}\right)$ by the angle-addition identity $\sin(A+B)=\sin(A)\cos(B)+\sin(B)\cos(A)$ .
Before we continue, we would like to simplify the value in the sine function. We see that $\frac{\alpha+\beta+2\gamma}{2}=\frac{\gamma}{2}+\frac{\alpha+\beta+\gamma}{2}=\frac{\gamma}{2}+90$ . Using the fact that $\cos(A)=\sin(90-A)$ results in
$\sin\left(\frac{\alpha+\beta+2\gamma}{2}\right)=\sin\left(90+\frac{\gamma}{2}\right)=\sin\left(90-(-\frac{\gamma}{2})\right)=\cos\left(-\frac{\gamma}{2}\right)=\cos\left(\frac{\gamma}{2}\right).$
How do we simplify $IC$ ? Well, we can perform the Law of Sines on triangle $AIC$ . This results in:
$\frac{AC}{\sin(\angle AIC)}=\frac{IC}{\sin\left(\frac{\alpha}{2}\right)}$
The value of $\angle AIC$ is $\frac{\alpha+2\beta+\gamma}{2}$ by the Exterior Angle Theorem on $\triangle ABI$ , so the value of $\sin(\angle AIC)$ is equivalent to the value of $\cos\left(\frac{\beta}{2}\right)$ by a similar argument as above. Then rearranging yields $IC = b\cdot\frac{\sin\left(\frac{\alpha}{2}\right)}{\cos\left(\frac{\beta}{2}\right)}$ .
Going back to the previous formula $MN = IC\cdot\sin\left(\frac{\alpha+\beta+2\gamma}{2}\right)$ and substituting values yields:
$MN = b\cdot\frac{\sin\left(\frac{\alpha}{2}\right)\cos\left(\frac{\gamma}{2}\right)}{\cos\left(\frac{\beta}{2}\right)}$ .
Finally, using the formulae $\sin\left(\frac{\alpha}{2}\right)=\sqrt{\frac{(s-b)(s-c)}{bc}}$ and $\cos\left(\frac{\alpha}{2}\right)=\sqrt{\frac{s(s-a)}{bc}}$ (where $s$ is half the perimeter of the triangle), we reach our final value:
$MN = b\cdot\frac{\sqrt{\frac{(s-b)(s-c)}{bc}}\cdot\sqrt{\frac{s(s-c)}{ab}}}{\sqrt{\frac{s(s-b)}{ac}}}$
$=\frac{\sqrt{s(s-b)(s-c)^2}}{\sqrt{s(s-b)}}$
$=\sqrt{(s-c)^2}$
$=s-c$
$=181-125$
$=\boxed{056}.$

## Video Solution
https://www.youtube.com/watch?v=yIUBhWiJ4Dk ~Mathematical Dexterity

## Video Solution
https://www.youtube.com/watch?v=vkniYGN45F4
~Shreyas S
Alternate Solution: https://www.youtube.com/watch?v=L2OzYI0OJsc&t=12s
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .