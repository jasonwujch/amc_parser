# 2001 AIME II Problem 13

## Problem

In quadrilateral $ABCD$ , $\angle{BAD}\cong\angle{ADC}$ and $\angle{ABD}\cong\angle{BCD}$ , $AB = 8$ , $BD = 10$ , and $BC = 6$ . The length $CD$ may be written in the form $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Extend $\overline{AD}$ and $\overline{BC}$ to meet at $E$ . Then, since $\angle BAD = \angle ADC$ and $\angle ABD = \angle DCE$ , we know that $\triangle ABD \sim \triangle DCE$ . Hence $\angle ADB = \angle DEC$ , and $\triangle BDE$ is isosceles . Then $BD = BE = 10$ .
Using the similarity, we have:
\[\frac{AB}{BD} = \frac 8{10} = \frac{CD}{CE} = \frac{CD}{16} \Longrightarrow CD = \frac{64}5\]
The answer is $m+n = \boxed{069}$ .
Extension : To Find $AD$ , use Law of Cosines on $\triangle BCD$ to get $\cos(\angle BCD)=\frac{13}{20}$ Then since $\angle BCD=\angle ABD$ use Law of Cosines on $\triangle ABD$ to find $AD=2\sqrt{15}$

## Solution 2
Draw a line from $B$ , parallel to $\overline{AD}$ , and let it meet $\overline{CD}$ at $M$ . Note that $\triangle{DAB}$ is similar to $\triangle{BMC}$ by AA similarity, since $\angle{ABD}=\angle{MCB}$ and since $BM$ is parallel to $CD$ then $\angle{BMC}=\angle{ADM}=\angle{DAB}$ . Now since $ADMB$ is an isosceles trapezoid, $MD=8$ . By the similarity, we have $MC=AB\cdot \frac{BC}{BD}=8\cdot \frac{6}{10}=\frac{24}{5}$ , hence $CD=MC+MD=\frac{24}{5}+8=\frac{64}{5}\implies 64+5=\boxed{069}$ .

## Solution 3
Since $\angle{BAD}=\angle{ADM}$ , if we extend AB and DC, they must meet at one point to form a isosceles triangle $\triangle{ADM}$ .Now, since the problem told that $\angle{ABD}=\angle{BCD}$ , we can imply that $\angle{DBM}=\angle{BCM}$ Since $\angle{M}=\angle{M}$ , so $\triangle{CBM}\sim\triangle{BDM}$ . Assume the length of $BM=x$ ;Since $\frac{BC}{MB}=\frac{DB}{MD}$ we can get $\frac{6}{x}=\frac{10}{8+x}$ , we get that $x=12$ .So $AM=DM=20$ similarly, we use the same pair of similar triangle we get $\frac{CM}{BM}=\frac{BM}{DM}$ , we get that $CM=\frac{36}{5}$ . Finally, $CD=MD-MC=\frac{64}{5}\implies 64+5=69=\boxed{069}$ ~bluesoul

## Solution 3
Denote $\angle{BAD}=\angle{CDA}=x$ , and $\angle{ABD}=\angle{BCD}=y$ . Note that $\angle{ADB}=180^\circ-x-y$ , and $\angle{DBC}=360^\circ-2x-2y$ . This motivates us to draw the angle bisector of $\angle{DBC}$ because $\angle{DBC} = 2 \angle{ADB}$ , so we do so and consider the intersection with $CD$ as $E$ . By the angle bisector theorem, we have $\frac{CE}{DE} = \frac{BC}{BD} = \frac{3}{5}$ , so we write $CE=3z$ and $DE=5z$ . We also know that $\angle{EBC}=\angle{ADB}$ and $\angle{BCE}=\angle{DBA}$ , so $\triangle{ADB} \sim \triangle{EBC}$ . Hence, $\frac{CE}{BC}=\frac{AB}{BD}$ , so we have $3z=\frac{24}{5}$ . As $CD=8z$ , it must be that $CD=\frac{64}{5}$ , so the final answer is $\boxed{069}$ .

## Video Solution by OmegaLearn
https://youtu.be/NsQbhYfGh1Q?t=75
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.