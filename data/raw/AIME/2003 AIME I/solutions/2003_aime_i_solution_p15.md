# 2003 AIME I Problem 15

## Problem

In $\triangle ABC, AB = 360, BC = 507,$ and $CA = 780.$ Let $M$ be the midpoint of $\overline{CA},$ and let $D$ be the point on $\overline{CA}$ such that $\overline{BD}$ bisects angle $ABC.$ Let $F$ be the point on $\overline{BC}$ such that $\overline{DF} \perp \overline{BD}.$ Suppose that $\overline{DF}$ meets $\overline{BM}$ at $E.$ The ratio $DE: EF$ can be written in the form $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Solution 1
In the following, let the name of a point represent the mass located there. Since we are looking for a ratio, we assume that $AB=120$ , $BC=169$ , and $CA=260$ in order to simplify our computations.
First, reflect point $F$ over angle bisector $BD$ to a point $F'$ .
As $BD$ is an angle bisector of both triangles $BAC$ and $BF'F$ , we know that $F'$ lies on $AB$ . We can now balance triangle $BF'C$ at point $D$ using mass points.
By the Angle Bisector Theorem , we can place mass points on $C,D,A$ of $120,\,289,\,169$ respectively. Thus, a mass of $\frac {289}{2}$ belongs at both $F$ and $F'$ because BD is a median of triangle $BF'F$ . Therefore, $CB/FB=\frac{289}{240}$ .
Now, we reassign mass points to determine $FE/FD$ . This setup involves $\triangle CFD$ and transversal $MEB$ . For simplicity, put masses of $240$ and $289$ at $C$ and $F$ respectively. To find the mass we should put at $D$ , we compute $CM/MD$ . Applying the Angle Bisector Theorem again and using the fact $M$ is a midpoint of $AC$ , we find \[\frac {MD}{CM} = \frac {\frac{169}{289}\cdot 260 - 130}{130} = \frac {49}{289}\] At this point we could find the mass at $D$ but it's unnecessary. \[\frac {DE}{EF} = \frac {F}{D} = \frac {F}{C}\cdot\frac {C}{D} = \frac {289}{240}\cdot\frac {49}{289} = \boxed{\frac {49}{240}}\] and the answer is $49 + 240 = \boxed{289}$ .

## Solution 2
By the Angle Bisector Theorem, we know that $[CBD]=\frac{169}{289}[ABC]$ . Therefore, by finding the area of triangle $CBD$ , we see that \[\frac{507\cdot BD}{2}\sin\frac{B}{2}=\frac{169}{289}[ABC].\] Solving for $BD$ yields \[BD=\frac{2[ABC]}{3\cdot289\sin\frac{B}{2}}.\] Furthermore, $\cos\frac{B}{2}=\frac{BD}{BF}$ , so \[BF=\frac{BD}{\cos\frac{B}{2}}=\frac{2[ABC]}{3\cdot289\sin\frac{B}{2}\cos\frac{B}{2}}.\] Now by the identity $2\sin\frac{B}{2}\cos\frac{B}{2}=\sin B$ , we get \[BF=\frac{4[ABC]}{3\cdot289\sin B}.\] But then $[ABC]=\frac{360\cdot 507}{2}\sin B$ , so $BF=\frac{240}{289}\cdot 507$ . Thus $BF:FC=240:49$ .
Now by the Angle Bisector Theorem, $CD=\frac{169}{289}\cdot 780$ , and we know that $MC=\frac{1}{2}\cdot 780$ so $DM:MC=\frac{169}{289}-\frac{1}{2}:\frac{1}{2}=49:289$ .
We can now use mass points on triangle CBD. Assign a mass of $240\cdot 49$ to point $C$ . Then $D$ must have mass $240\cdot 289$ and $B$ must have mass $49\cdot 49$ . This gives $F$ a mass of $240\cdot 49+49\cdot 49=289\cdot 49$ . Therefore, $DE:EF=\frac{289\cdot 49}{240\cdot 289}=\frac{49}{240}$ , giving us an answer of $\boxed{289}.$

## Solution 3
Let $\angle{DBM}=\theta$ and $\angle{DBC}=\alpha$ . Then because $BM$ is a median we have $360\sin{(\alpha+\theta)}=507\sin{(\alpha-\theta)}$ . Now we know \[\sin{(\alpha+\theta)}=\sin{\alpha}\cos{\theta}+\sin{\theta}\cos{\alpha}=\dfrac{DF\cdot BD}{BF\cdot BE}+\dfrac{DE\cdot BD}{BE\cdot BF}=\dfrac{BD(DF+DE)}{BF\cdot BE}\] Expressing the area of $\triangle{BEF}$ in two ways we have \[\dfrac{1}{2}BE\cdot BF\sin{(\alpha-\theta)}=\dfrac{1}{2}EF\cdot BD\] so \[\sin{(\alpha-\theta)}=\dfrac{EF\cdot BD}{BF\cdot BE}\] Plugging this in we have \[\dfrac{360\cdot BD(DF+DE)}{BF\cdot BE}=\dfrac{507\cdot BD\cdot EF}{BF\cdot BE}\] so $\dfrac{DF+DE}{EF}=\dfrac{507}{360}$ . But $DF=DE+EF$ , so this simplifies to $1+\dfrac{2DE}{EF}=\dfrac{507}{360}=\dfrac{169}{120}$ , and thus $\dfrac{DE}{EF}=\dfrac{49}{240}$ , and $m+n=\boxed{289}$ .

## Solution 4 (Overpowered Projective Geometry!!)
Firstly, angle bisector theorem yields $\frac{CD}{AD} = \frac{507}{360} = \frac{169}{120}$ . We're given that $AM=MC$ . Therefore, the cross ratio
\[(A,C;M,D) = \frac{AM(CD)}{AD(MC)} = \frac{169}{120}\]
We need a fourth point for this cross ratio to be useful, so reflect point $F$ over angle bisector $BD$ to a point $F'$ . Then $\triangle BFF'$ is isosceles and $BD$ is an altitude so $DF = DF'$ . Therefore,
\[(A,C;M,D) = (F,F';D,E) \implies \frac{FD(EF')}{EF(DF')} = \frac{EF'}{EF} = \frac{169}{120}\]
All that's left is to fiddle around with the ratios:
\[\frac{EF'}{EF} = \frac{ED+DF'}{EF} = \frac{EF+2DE}{EF} = 1\ +\ 2\left(\frac{DE}{EF}\right) \implies \frac{DE}{EF} = \frac{49}{240} \implies \boxed{289}\]

## Solution 5 (Menelaus + Mass Points)
Extend $DF$ to intersect with the extension of $AB$ at $G$ . Notice that $\triangle{BDF} \cong \triangle{BDG}$ , so $GD=DF$ . We now use Menelaus on $\triangle{GBF}$ , as $A$ , $D$ , and $C$ are collinear; this gives us $\frac{GA}{BA} \cdot \frac{BC}{FC} \cdot \frac{DF}{GD}=1$ . As $GD=DF$ , we have $\frac{GA}{AB}=\frac{FC}{BC}$ , hence $\frac{GA}{120}=\frac{FC}{169}$ . Reflect $G$ over $A$ to $G'$ . Note that $\frac{G'A}{BA}=\frac{FC}{BC}$ , and reflexivity, hence $\triangle{ABC} \sim \triangle{BG'F}$ . It's easily concluded from this that $G'F \parallel AC$ , hence $G'F \parallel AD$ . As $GD=DF$ , we have $AD$ is a midsegment of $\triangle{GG'F}$ , thus $G'F = 2AD$ . We now focus on the ratio $\frac{BF}{BC}$ . From similarity, we have $\frac{BF}{BC}=\frac{G'F}{AC}=\frac{2AD}{AC}$ . By the angle bisector theorem, we have $AD:DC=120:169$ , hence $AD:AC=120:289$ , so $\frac{BF}{BC}=\frac{240}{289}$ . We now work out the ratio $\frac{DM}{MC}$ . $\frac{DM}{MC}=\frac{CD-MC}{MC}=\frac{CD}{MC}-1=\frac{2CD}{AC}-1=\frac{338}{289}-1=\frac{49}{289}$ . We now use mass points on $\triangle{BDC}$ . We let the mass of $C$ be $240\cdot 49$ , so the mass of $B$ is $49 \cdot 49$ and the mass of $D$ is $289\cdot 240$ . Hence, the mass of $F$ is $289\cdot 49$ , so the ratio $\frac{DE}{EF}=\frac{49}{240}$ . Extracting gives $49+240=\boxed{289}.$
These problems are copyrighted © by the Mathematical Association of America.