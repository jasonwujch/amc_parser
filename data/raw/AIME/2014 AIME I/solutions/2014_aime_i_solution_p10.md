# 2014 AIME I Problem 10

## Problem

A disk with radius $1$ is externally tangent to a disk with radius $5$ . Let $A$ be the point where the disks are tangent, $C$ be the center of the smaller disk, and $E$ be the center of the larger disk. While the larger disk remains fixed, the smaller disk is allowed to roll along the outside of the larger disk until the smaller disk has turned through an angle of $360^\circ$ . That is, if the center of the smaller disk has moved to the point $D$ , and the point on the smaller disk that began at $A$ has now moved to point $B$ , then $\overline{AC}$ is parallel to $\overline{BD}$ . Then $\sin^2(\angle BEA)=\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
[asy] size(150); pair a=(5,0),b=(2,3*sqrt(3)),c=(6,0),d=(3,3*sqrt(3)),e=(0,0); draw(circle(e,5)); draw(circle(c,1)); draw(circle(d,1)); dot(a^^b^^c^^d^^e^^(5/2,5*sqrt(3)/2)); label("$A$",a,W,fontsize(9)); label("$B$",b,NW,fontsize(9)); label("$C$",c,E,fontsize(9)); label("$D$",d,E,fontsize(9)); label("$E$",e,SW,fontsize(9)); label("$F$",(5/2,5*sqrt(3)/2),SSW,fontsize(9)); [/asy]
Let $F$ be the new tangency point of the two disks. The smaller disk rolled along minor arc $\overset{\frown}{AF}$ on the larger disk.
Let $\alpha = \angle AEF$ , in radians. The smaller disk must then have rolled along an arc of length $5\alpha$ , since the larger disk has a radius of $5$ . Since all of the points on major arc $\overset{\frown}{BF}$ on the smaller disk have come into contact with the larger disk at some point during the rolling, and none of the other points on the smaller disk did, \[\overset{\frown}{BF}=\overset{\frown}{AF}=5\alpha\] .
Since $\overline{AC} || \overline{BD}$ , \[\angle BDF \cong \angle FEA\] so the angles of minor arc $\overset{\frown}{BF}$ and minor arc $\overset{\frown}{AF}$ are equal, so minor arc $\overset{\frown}{BF}$ has an angle of $\alpha$ . Since the smaller disk has a radius of $1$ , the length of minor arc $\overset{\frown}{BF}$ is $\alpha$ . This means that $5\alpha + \alpha$ equals the circumference of the smaller disk, so $6\alpha = 2\pi$ , or $\alpha = \frac{\pi}{3}$ .
Now, to find $\sin^2{\angle BEA}$ , we construct $\triangle BDE$ . Also, drop a perpendicular from $D$ to $\overline{EA}$ , and call this point $X$ . Since $\alpha = \frac{\pi}{3}$ and $\angle DXE$ is right, \[DE = 6\] \[EX = 3\] and \[DX = 3\sqrt{3}\]
Now drop a perpendicular from $B$ to $\overline{EA}$ , and call this point $Y$ . Since $\overline{BD} || \overline{EA}$ , \[XY = BD = 1\] and \[BY = DX = 3\sqrt{3}\] Thus, we know that \[EY = EX - XY = 3 - 1 = 2\] and by using the Pythagorean Theorem on $\triangle BEY$ , we get that \[BE = \sqrt{31}\] Thus, \[\sin{\angle BEA} = \frac{\sqrt{27}}{\sqrt{31}}\] so \[\sin^2{\angle BEA} = \frac{27}{31}\] and our answer is $27 + 31 = \boxed{058}$ .

## Solution 2
First, we determine how far the small circle goes. For the small circle to rotate completely around the circumference, it must rotate $5$ times (the circumference of the small circle is $2\pi$ while the larger one has a circumference of $10\pi$ ) plus the extra rotation the circle gets for rotating around the circle, for a total of $6$ times. Therefore, one rotation will bring point $D$ $60^\circ$ from $C$ .
Now, draw $\triangle DBE$ , and call \[\angle BED = x^{\circ}\] We know that $\overline{ED}$ is 6, and $\overline{BD}$ is 1. Since $EC || BD$ , \[\angle BDE = 60^\circ\]
By the Law of Cosines, \[\overline{BE}^2=36+1-2\times 6\times 1\times \cos{60^\circ} = 36+1-6=31\] and since lengths are positive, \[\overline{BE}=\sqrt{31}\]
By the Law of Sines, we know that \[\frac{1}{\sin{x}}=\frac{\sqrt{31}}{\sin{60^\circ}}\] so \[\sin{x} = \frac{\sin{60^\circ}}{\sqrt{31}} = \frac{\sqrt{93}}{62}\] As $x$ is clearly between $0$ and $90^\circ$ , $\cos{x}$ is positive. As $\cos{x}=\sqrt{1-\sin^2{x}}$ , \[\cos{x} = \frac{11\sqrt{31}}{62}\]
Now we use the angle sum formula to find the sine of $\angle BEA$ : \[\sin 60^\circ\cos x + \cos 60^\circ\sin x = \frac{\sqrt{3}}{2}\frac{11\sqrt{31}}{62}+\frac{1}{2}\frac{\sqrt{93}}{62}\] \[= \frac{11\sqrt{93}+\sqrt{93}}{124} = \frac{12\sqrt{93}}{124} = \frac{3\sqrt{93}}{31} = \frac{3\sqrt{31}\sqrt{3}}{31} = \frac{3\sqrt{3}}{\sqrt{31}}\]
Finally, we square this to get \[\frac{9\times 3}{31}=\frac{27}{31}\] so our answer is $27+31=\boxed{058}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .