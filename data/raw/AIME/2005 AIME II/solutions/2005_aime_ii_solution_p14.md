# 2005 AIME II Problem 14

## Problem

In triangle $ABC, AB=13, BC=15,$ and $CA = 14.$ Point $D$ is on $\overline{BC}$ with $CD=6.$ Point $E$ is on $\overline{BC}$ such that $\angle BAE\cong \angle CAD.$ Given that $BE=\frac pq$ where $p$ and $q$ are relatively prime positive integers, find $q.$

## Solution 1
By the Law of Sines and since $\angle BAE = \angle CAD, \angle BAD = \angle CAE$ , we have
\begin{align*} \frac{CD \cdot CE}{AC^2} &= \frac{\sin CAD}{\sin ADC} \cdot \frac{\sin CAE}{\sin AEC} \\ &= \frac{\sin BAE \sin BAD}{\sin ADB \sin AEB} \\ &= \frac{\sin BAE}{\sin AEB} \cdot \frac{\sin BAD}{\sin ADB}\\ &= \frac{BE \cdot BD}{AB^2} \end{align*}
Substituting our knowns, we have $\frac{CE}{BE} = \frac{3 \cdot 14^2}{2 \cdot 13^2} = \frac{BC - BE}{BE} = \frac{15}{BE} - 1 \Longrightarrow BE = \frac{13^2 \cdot 15}{463}$ . The answer is $q = \boxed{463}$ .

## Solution 2 (Similar Triangles)
Drop the altitude from A and call the base of the altitude Q. Also, drop the altitudes from E and D to AB and AC respectively. Call the feet of the altitudes R and S respectively.
From here, we can use Heron's Formula to find the altitude. The area of the triangle is $\sqrt{21*6*7*8} = 84$ . We can then use similar triangles with triangle $AQC$ and triangle $DSC$ to find $DS=\frac{24}{5}$ . Consequently, from Pythagorean theorem, $SC = \frac{18}{5}$ and $AS = 14-SC = \frac{52}{5}$ . We can also use the Pythagorean theorem on triangle $AQB$ to determine that $BQ = \frac{33}{5}$ .
Label $AR$ as $y$ and $RE$ as $x$ . $RB$ then equals $13-y$ . Then, we have two similar triangles.
Firstly: $\triangle ARE \sim \triangle ASD$ . From there, we have $\frac{x}{y} = \frac{\frac{24}{5}}{\frac{53}{5}}$ .
Next: $\triangle BRE \sim \triangle BQA$ . From there, we have $\frac{x}{13-y} = \frac{\frac{56}{5}}{\frac{33}{5}}$ .
Solve the system to get $x = \frac{2184}{463}$ and $y = \frac{4732}{463}$ . Notice that 463 is prime, so even though we use the Pythagorean theorem on $x$ and $13-y$ , the denominator won't change. The answer we desire is $\boxed{463}$ .

## Solution 3 (LoC and LoS bash)
Let $\angle CAD = \angle BAE = \theta$ . Note by Law of Sines on $\triangle BEA$ we have \[\frac{BE}{\sin{\theta}} = \frac{AE}{\sin{B}} = \frac{AB}{\sin{\angle BEA}}\] As a result, our goal is to find $\sin{\angle BEA}$ and $\sin{\theta}$ (we already know $AB$ ).
Let the foot of the altitude from $A$ to $BC$ be $H$ . By law of cosines on $\triangle ABC$ we have \[169 = 196 + 225 - 2 \cdot 14 \cdot 15 \cdot \cos{C} \Rightarrow \cos{C} = \frac{3}{5}\] It follows that $AH = \frac{56}{5}$ and $HC = \frac{42}{5} \Rightarrow HD = \frac{12}{5}$ .
Note that by PT on $\triangle AHD$ we have that $AD^2 = \left(\frac{56}{5}\right)^2 + \left(\frac{12}{5}\right)^2 = \frac{656}{5}$ . By Law of Sines on $\triangle ADC$ (where we square everything to avoid taking the square root) we see \[\frac{36}{\sin^2{\theta}} = \frac{656}{5 \cdot \frac{16}{25}} \Rightarrow \sin^2{\theta} = \frac{36}{205}.\] How are we going to find $\sin{\angle BEA}$ though? $\angle BEA$ and $\theta$ are in the same triangle. Applying Law of Sines on $\triangle ABC$ we see that \[\frac{13}{\frac{4}{5}} = \frac{14}{\sin{\angle B}} \Rightarrow \sin{\angle B} = \frac{56}{65} \Rightarrow \cos{\angle B} = \frac{33}{65}.\] $\theta$ , $\angle B$ , and $\angle BEA$ are all in the same triangle. We know they add up to $180^{\circ}$ . There's a good chance we can exploit this using the identity $\sin{p} = \sin{180^{\circ}-p}$ .
We have that $\sin{(180^{\circ} - (\theta + \angle B))} = \sin{\angle BEA} = \sin{(\theta + \angle B)}$ . Success! We know $\sin{\theta}$ and $\sin{\angle B}$ already. Applying the $\sin$ addition formula we see \[\sin{\theta + \angle B} = \sin{\theta} \cos{\angle B} + \sin{\angle B} \cos{\theta} = \frac{6}{\sqrt{205}} \cdot \frac{33}{65} + \frac{56}{65} \cdot \frac{13}{\sqrt{205}}=\frac{1}{65 \cdot \sqrt{205}} (198 + 728) = \frac{926}{65 \sqrt{205}}.\] This is the last stretch! Applying Law of Sines a final time on $\triangle BEA$ we see \[\frac{BE}{\sin{\theta}} = \frac{13}{\sin{BEA}} \Rightarrow \frac{BE}{\frac{6}{\sqrt{205}}} = \frac{13}{\frac{926}{65\sqrt{205}}} \Rightarrow \frac{BE}{6} = \frac{13 \cdot 65}{926} \Rightarrow \frac{13 \cdot 65 \cdot 6}{926} = BE = \frac{2535}{463}.\] It follows that the answer is $\boxed{463}$ .

## Solution 4 (Ratio Lemma and Angle Bisector Theorem)
Let $AK$ be the angle bisector of $\angle A$ such that $K$ is on $BC$ .
Then $\angle KAB = \angle KAC$ , and thus $\angle KAE = \angle KAD$ .
By the Ratio Lemma, $\frac{BE}{KE} = \frac{BA}{KA} * \frac{\sin{BAE}}{\sin{KAE}}$ and $\frac{CD}{KD} = \frac{CA}{KA} * \frac{\sin{CAD}}{\sin{KAD}}$ .
This implies that $\frac{BE}{KE*BA} = \frac{CD}{KD*CA}$ .
Thus, $\frac{BE}{KE} = \frac{13}{14} * \frac{6}{DK}$ .
$DK = CK - 6 = 14*15/27 - 6 = 16/9$ . Thus, $\frac{BE}{KE} = \frac{13*54}{14*16}$ .
Additionally, $BE + KE = 13*15/27 = 65/9$ . Solving gives that $q = 463.$
Alternate: By the ratio lemma, $BD/DC = (13/14)*(\sin BAD/\sin DAC)$ $EC/EB = (14/13)*(\sin EAC/\sin BAE)$
Combining these, we get $(BD/DC)(14/13) = (EC/EB)(13/14)$ $(3/2)(14/13)(14/13) = (15-x)(x)$
$x = 2535/463$ Thus, $q = 463$

## Solution 5 (Isogonal lines with respect to A angle bisesector)
Since $AE$ and $AD$ are isogonal with respect to the $A$ angle bisector, we have \[\frac{BE}{EC}\cdot \frac{BD}{DC}=(\frac{AB}{AC})^2.\] To prove this, let $\angle BAE=\angle DAC=x$ and $\angle BAD=\angle CAE=y.$ Then, by the Ratio Lemma, we have \[\frac{BD}{DC}=\frac{AB\sin y}{AC\sin x}\] \[\frac{BE}{EC}=\frac{AB\sin x}{AC\sin y}\] and multiplying these together proves the formula for isogonal lines. Hence, we have \[\frac{BE}{15-BE}\cdot \frac{9}{6}=\frac{169}{196}\implies BE=\frac{2535}{463}\] so our desired answer is $\boxed{463}.$

## Solution 6 (Tangent subtraction formulas)
Note: We first recall some helpful tips regarding 13, 14, 15 triangles. Drawing an altitude H from B to AC results in AHB being a 5-12-13 right triangle and CHB being a 3-4-5 (9-12-15) right triangle.
Now we start by drawing altitudes from D and E onto AC, labeling them as F and G, and labelling $\angle DAG = \alpha$ . Now we know that $\overline{DF} = \frac{24}{5}$ and $\overline{FC} = \frac{18}{5}$ . Therefore, $\overline{AF} = \frac{52}{5}$ , so $\tan{(\alpha)} = \frac{6}{13}$ . Our goal now is to use tangent $\angle EAG$ in triangle $AEG$ . We set $\overline{BE}$ to $x$ , so $\overline{ED} = 9 - x$ and $\overline{EC} = 15 - x$ , so $\overline{EG} = \frac{4}{5}(15-x)$ and $\overline{GC} = \frac{3}{5}(15-x)$ so $\overline{AG} = \frac{3x+25}{5}$ . Now we just need tangent of $\angle EAG$ .
We find this using $\tan{(EAG)} = \tan{(A - \alpha)} = \frac{\tan{A} - \tan{\alpha}}{1 + \tan{A}\tan{\alpha}}$ , which is $\frac{\frac{12}{5} - \frac{6}{13}}{1 + \frac{12}{5} \cdot \frac{6}{13}}$ or $\frac{126}{137}$ . Now we solve the equation $\tan{\angle EAG} = \frac{126}{137} = \frac{\frac{60-4x}{5}}{\frac{3x+25}{5}}$ , so $x = \frac{2535}{463}$

## Solution 8 (Isogonal Conjugates)
Let $ED = x$ , such that $BE = 9-x$ . Since $\overline{AE}$ and $\overline{AD}$ are isogonal, we get $\frac{9-x}{6+x} \cdot \frac{9}{6} = \frac{13^2}{14^2} \Rightarrow 588(9 - x) = 338(6 + x)$ , and we can solve to get $x = \frac{1632}{463}$ (and $BE = \frac{2535}{463}$ ). Hence, our answer is $\boxed{463}$ . - Spacesam

## Solution 9 (Short and no IQ Required Altogether-Bash)
Diagram borrowed from Solution 1.
Applying Law of Cosines on $\bigtriangleup ABC$ with respect to $\angle C$ we have \[AB^2=AC^2+BC^2-2(AC)(BC)\cos C\] Solving gets $\cos C=\frac{3}{5}$ , which implies that \[\sin C=\sqrt{1-\cos C}=\frac{4}{5}\] Applying Stewart's Theorem with cevian $AD$ we have \[(BC)(AD)^2+(BC)(BD)(CD)=(CD)(AB)^2+(BD)(AC)^2\] Solving gets $AD=\frac{4\sqrt{205}}{5}$ .
Applying Law of Sines on $\bigtriangleup ACD$ to solve for $\sin CAD$ we have \[\frac{AD}{\sin C}=\frac{CD}{\sin CAD}\] Solving gets $\sin CAD=\frac{6\sqrt{205}}{205}$ . Thus $\sin BAE=\sin CAD=\frac{6\sqrt{205}}{205}$ .
Applying Law of Sines on $\bigtriangleup ABC$ we have \[\frac{AC}{\sin B}=\frac{AB}{\sin C}\] Solving gets $\sin B=\frac{56}{65}$ .
Applying Stewart's Theorem with cevian $AE$ we have \[(BC)(AE)^2+(BC)(BE)(CE)=(CE)(AB)^2+(BE)(AC)^2\] \[(BC)(AE)^2+(BC)(BE)(BC-BE)=(BC-BE)(AB)^2+(BE)(AC)^2\] Solving gets $AE=\sqrt{\frac{15BE^2-198BE+2535}{15}}$
Finally, applying Law of Sines on $\bigtriangleup BAE$ we have \[\frac{AE}{\sin B}=\frac{BE}{\sin BAE}\] \[\frac{\sqrt{\frac{15BE^2-198BE+2535}{15}}}{\frac{56}{65}}=\frac{BE}{\frac{6\sqrt{205}}{205}}\] \[7605BE^2-32342BE+2535=0\] Solving the easy quadratic equation gets $BE=\frac{1632}{463}\Longrightarrow q=\boxed{463}$
~ Nafer

## Solution 10
Making perpendicular lines from $D$ to $AC$ , meeting at $N$ ; from $E$ to $AB$ , meeting at $J$ . According to LOC, we can get that $\cos\angle{C}=\frac{3}{5}$ . So we get that $CN=\frac{18}{5};DN=\frac{24}{5};AN=AC-CN=\frac{52}{5}$ . Now we can see that $\tan\angle{DAN}=\frac{DN}{AN}=\frac{6}{13}$ . Now we see that in $\triangle{EJA}$ , assuming $EJ=6x;AJ=13x$ since $\tan\angle{JAE}=\tan\angle{DAN}$ . Now we need to find the tangent of $\angle{B}$ . Making a perpendicular line from $C$ to $AB$ at $M$ . We can see that $CM=\frac{168}{13};AM=\frac{70}{13};BM=AB-AM=13-\frac{70}{13}=\frac{99}{13}$ . We get that $\tan\angle{B}=\frac{56}{33}$ so $BJ=\frac{33}{56}*6x=\frac{99x}{28}$ . After getting AJ and BJ, we can get that $AB=AJ+BJ=\frac{463x}{28}=13$ , which means that $x=\frac{364}{463}$ . According to the similarity, $\frac{CM}{BC}=\frac{JE}{BE};BE=\frac{2535}{463}$ which $\boxed{463}$ is our answer ~bluesoul

## Solution 11 (Ultimate Stewarts Bash)
First, apply Stewart's theorem to triangle $ABC$ with cevian $AD$ , from which we receive $AD=\frac{4\sqrt{41}}{\sqrt{5}}$ . Then, set $AE=y$ and $BE=x.$ Hence, $DE=9-x$ . Applying Stewart's on triangle $ACE$ , with cevian $AD$ , we receive that $y^2-x^2=169-\frac{66}{5}x$ . By also applying the sine ratio formula on triangles $ACD$ and $AEB$ , since these triangles share the same height, we get that $\frac{6}{x}=\frac{\frac{1}{2} \cdot 14 \cdot \frac{4\sqrt{41}}{\sqrt{5}}}{\frac{1}{2} \cdot 13 \cdot y}$ . Here, we can simplify to receive that $\frac{32144}{7605}x^2=y^2$ . We plug this into our earlier equation, and get that $\frac{24539}{7605}x^2=169-\frac{66}{5}x \implies 24539x^2+66 \cdot 39^2x-169 - 169 \cdot 39^2 \cdot 5=0.$ We then apply the quadratic formula (which may seem computationally intensive, but factoring kills it), and get $\frac{-66 \cdot 39^2 + \sqrt{66^2 \cdot 39^4+4(24539)(169 \cdot39^2 \cdot 5)}}{2 \cdot 24539}$ . (Note we only take the plus symbol instead of $\pm$ since $x > 0$ .) After factoring heavily, we get the answer to be $\frac{-33 \cdot 39^2+39 \cdot 13 \cdot 364}{24539} = \frac{2535}{463}$ , and the answer is $\boxed{463}.$
~SirAppel

## Solution 12 (Clean)
We begin by drawing a line through point $B$ parallel to side $AC$ . Extend Lines $AE$ and $AD$ to meet the new parallel line at points $F$ and $G$ , respectively. This will help us create a lot of similar triangles.
The first pair of similar triangles that is easy to spot is triangle $ACD$ and triangle $GBD$ by AA similarity ( $\angle{ADC}=\angle{GDB}$ by vertical angles, and $\angle{DAC}=\angle{DGB}$ by alternate interior angles). With the ratios $\frac{AC}{BG}=\frac{CD}{BD}$ $\rightarrow$ $\frac{14}{BG}=\frac{6}{9}$ $\rightarrow$ $BG=21$ .
The next pair of similar triangles is triangle $BAG$ and triangle $BFA$ by AA similarity ( $\angle{CAD}=\angle{BAF}$ as given, and $\angle{CAD}=\angle{BGA}$ by alternate interior angles, so by transitive property, $\angle{BAF}=\angle{BGA}$ . Additionaly, $\angle{ABF}=\angle{GBA}$ as they are the same angle.). With the ratios $\frac{AB}{BG}=\frac{BF}{AB}$ $\rightarrow$ $\frac{13}{21}=\frac{BF}{13}$ $\rightarrow$ $BF=\frac{169}{21}$ .
The last pair of similar triangles we need is triangle $BEF$ and triangle $CAE$ by AA similarity (similar by vertical angles and alternate interior angles). With the ratios $\frac{AC}{BF}=\frac{CE}{BE}$ $\rightarrow$ $\frac{14}{\frac{169}{21}}=\frac{15-x}{x}$ $\rightarrow$ $x=\frac{169*15}{463}$ . This cannot be simplified further, and the problem asks for the denominator, so the answer is $\boxed{463}$ .
~ChaitraliKA
These problems are copyrighted © by the Mathematical Association of America.