# 2019 AMC 10B Problem 16

## Problem

In $\triangle ABC$ with a right angle at $C$ , point $D$ lies in the interior of $\overline{AB}$ and point $E$ lies in the interior of $\overline{BC}$ so that $AC=CD,$ $DE=EB,$ and the ratio $AC:DE=4:3$ . What is the ratio $AD:DB?$

$\textbf{(A) }2:3\qquad\textbf{(B) }2:\sqrt{5}\qquad\textbf{(C) }1:1\qquad\textbf{(D) }3:\sqrt{5}\qquad\textbf{(E) }3:2$

## Solutions

## Solution 1
Without loss of generality, let $AC = CD = 4$ and $DE = EB = 3$ . Let $\angle A = \alpha$ and $\angle B = \beta = 90^{\circ} - \alpha$ . As $\triangle ACD$ and $\triangle DEB$ are isosceles, $\angle ADC = \alpha$ and $\angle BDE = \beta$ . Then $\angle CDE = 180^{\circ} - \alpha - \beta = 90^{\circ}$ , so $\triangle CDE$ is a $3-4-5$ triangle with $CE = 5$ .
Then $CB = 5+3 = 8$ , and $\triangle ABC$ is a $1-2-\sqrt{5}$ triangle.
In isosceles triangles $\triangle ACD$ and $\triangle DEB$ , drop altitudes from $C$ and $E$ onto $AB$ ; denote the feet of these altitudes by $P_C$ and $P_E$ respectively. Then $\triangle ACP_C \sim \triangle ABC$ by AAA similarity, so we get that $AP_C = P_CD = \frac{4}{\sqrt{5}}$ , and $AD = 2 \times \frac{4}{\sqrt{5}}$ . Similarly, we get $BD = 2 \times \frac{6}{\sqrt{5}}$ , and $AD:DB = \boxed{\textbf{(A) } 2:3}$ .

## Solution 2
Let $AC=CD=4x$ , and $DE=EB=3x$ . (For this solution, $A$ is above $C$ , and $B$ is to the right of $C$ ). Also let $\angle A = t^{\circ}$ , so $\angle ACD = \left(180-2t\right)^{\circ}$ , which implies $\angle DCB = \left(2t - 90\right)^{\circ}$ . Similarly, $\angle B = \left(90-t\right)^{\circ}$ , which implies $\angle BED = 2t^{\circ}$ . This further implies that $\angle DEC = \left(180 - 2t\right)^{\circ}$ .
Now we see that $\angle CDE = 180^{\circ} - \angle ECD - \angle DEC = 180^{\circ} - 2t^{\circ} + 90^{\circ} - 180^{\circ} + 2t^{\circ} = 90^{\circ}$ . Thus $\triangle CDE$ is a right triangle, with side lengths of $3x$ , $4x$ , and $5x$ (by the Pythagorean Theorem, or simply the Pythagorean triple $3-4-5$ ). Therefore $AC=4x$ (by definition), $BC=5x+3x = 8x$ , and $AB=4\sqrt{5}x$ . Hence $\cos{\left(2t^{\circ}\right)} = 2 \cos^{2}{t^{\circ}} - 1$ (by the double angle formula), giving $2\left(\frac{1}{\sqrt{5}}\right)^2 - 1 = -\frac{3}{5}$ .
By the Law of Cosines in $\triangle BED$ , if $BD = d$ , we have \[\begin{split}&d^2 = (3x)^2+(3x)^2-2\cdot\frac{-3}{5}(3x)(3x) \\ \Rightarrow \ &d^2 = 18x^2 + \frac{54x^2}{5} = \frac{144x^2}{5} \\ \Rightarrow \ &d = \frac{12x}{\sqrt{5}}\end{split}\] Now $AD = AB - BD = 4x\sqrt{5} - \frac{12x}{\sqrt{5}} = \frac{8x}{\sqrt{5}}$ . Thus the answer is $\frac{\left(\frac{8x}{\sqrt{5}}\right)}{\left(\frac{12x}{\sqrt{5}}\right)} = \frac{8}{12} = \boxed{\textbf{(A) }2:3}$ .

## Solution 3
WLOG, let $AC=CD=4$ , and $DE=EB=3$ . $\angle CDE = 180^{\circ} - \angle ADC - \angle BDE = 180^{\circ} - \angle DAC - \angle DBE = 90^{\circ}$ . Because of this, $\triangle DEC$ is a 3-4-5 right triangle. Draw the altitude $DF$ of $\triangle DEC$ . $DF$ is $\frac{12}{5}$ by the base-height triangle area formula. $\triangle ABC$ is similar to $\triangle DBF$ (AA). So $\frac{DF}{AC} = \frac{BD}{AB} = \frac35$ . $DB$ is $\frac35$ of $AB$ . Therefore, $AD:DB$ is $\boxed{\textbf{(A) } 2:3}$ .
~Thegreatboy90

## Solution 4 (a bit long)
WLOG, $AC = CD = 4$ and $DE = EB = 3$ . Notice that in $\triangle ACB$ , we have $m\angle BAC + m\angle ABC = 90^{\circ}$ . Since $AC = CD$ and $DE = EB$ , we find that $m\angle DAC = m\angle ADC$ and $m\angle DBE = m\angle BDE$ , so $m\angle ADC + m\angle BDE = 90^{\circ}$ and $\angle EDC$ is right. Therefore, $CE = 5$ by 3-4-5 triangle, $CB = 8$ and $AB = 4\sqrt{5}$ . Define point F such that $CF$ is an altitude; we know the area of the whole triangle is $16$ and we know the hypotenuse is $4\sqrt{5}$ , so $CF = \frac{16}{4\sqrt{5}}\cdot2=\frac{8}{\sqrt{5}}$ . By the geometric mean theorem, $x\left(4\sqrt{5}-x\right)=4\sqrt{5}x-x^{2}=\left(\frac{8}{\sqrt{5}}\right)^{2}=\frac{64}{5}$ . Solving the quadratic we get $x=\frac{10\sqrt{5}\pm6\sqrt{5}}{5}$ , so $x=\frac{4\sqrt{5}}{5} or \frac{16\sqrt{5}}{5}$ . For now, assume $x=\frac{4\sqrt{5}}{5}$ . Then $FB=4\sqrt{5}-\frac{4\sqrt{5}}{5}=\frac{16\sqrt{5}}{5}$ . $CF$ splits $AD$ into two parts (quick congruence by Leg-Angle) so $FD = AF = \frac{4\sqrt{5}}{5}$ and $DB = FB - FD = \frac{16\sqrt{5}}{5}-\frac{4\sqrt{5}}{5}=\frac{12\sqrt{5}}{5}$ . $AD = 2\cdot\frac{4\sqrt{5}}{5}=\frac{8\sqrt{5}}{5}$ . Now we know $AD$ and $DB$ , we can find $\frac{AD}{DB}=\frac{\frac{8\sqrt{5}}{5}}{\frac{12\sqrt{5}}{5}}=\frac{8\sqrt{5}}{5}\cdot\frac{5}{12\sqrt{5}}=\frac{8}{12}=\frac{2}{3}$ or $\boxed{\textbf{(A) } 2:3}$ .

## Solution 5 (Short with Trig)
Let $\angle B=\theta_1$ , then $\angle A=90-\theta_1$ . Since $AC=AD$ , $\angle ADC=90-\theta_1$ . Similarly, $\angle BDE=\theta_1$ . Then, $\angle EDC=180-\theta_1-(90-\theta_1)=90$ . Therefore $\bigtriangleup CDE$ is right. Let $AC=CD=4$ and $DE=EB=3$ , then $EC=5$ . Let $\angle DEC=\angle ACD=\theta_2$ . We know that $\cos \theta_2=\frac{3}{5}$ so we can apply the Law of Cosines on $\bigtriangleup ACD$ to find $AD=\sqrt{32-32\cdot{\frac{3}{5}}}=\sqrt{\frac{2}{5}\cdot{32}} \Longrightarrow \frac{8}{\sqrt{5}}$ . Doing Pythagorean for $BA$ , we get $4\sqrt{5}$ . Then, $BD=4\sqrt{5}-\frac{8}{\sqrt{5}} \Longrightarrow \frac{12}{\sqrt{5}}$ so the requested ratio is $8:12=\boxed{\textbf{(A) } 2:3}$ .
~ Magnetoninja

## Video Solution by TheBeautyofMath
https://youtu.be/_0YaCyxiMBo
~IceMatrix

## Video Solution by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=4245
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .