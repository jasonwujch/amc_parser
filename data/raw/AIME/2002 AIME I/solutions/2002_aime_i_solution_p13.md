# 2002 AIME I Problem 13

## Problem

In triangle $ABC$ the medians $\overline{AD}$ and $\overline{CE}$ have lengths $18$ and $27$ , respectively, and $AB=24$ . Extend $\overline{CE}$ to intersect the circumcircle of $ABC$ at $F$ . The area of triangle $AFB$ is $m\sqrt{n}$ , where $m$ and $n$ are positive integers and $n$ is not divisible by the square of any prime. Find $m+n$ .

## Solution 1
Applying Stewart's Theorem to medians $AD, CE$ , we have:
\begin{align*} BC^2 + 4 \cdot 18^2 &= 2\left(24^2 + AC^2\right) \\ 24^2 + 4 \cdot 27^2 &= 2\left(AC^2 + BC^2\right) \end{align*}
Substituting the first equation into the second and simplification yields $24^2 = 2\left(3AC^2 + 2 \cdot 24^2 - 4 \cdot 18^2\right)- 4 \cdot 27^2$ $\Longrightarrow AC = \sqrt{2^5 \cdot 3 + 2 \cdot 3^5 + 2^4 \cdot 3^3 - 2^7 \cdot 3} = 3\sqrt{70}$ .
By the Power of a Point Theorem on $E$ , we get $EF = \frac{12^2}{27} = \frac{16}{3}$ . The Law of Cosines on $\triangle ACE$ gives
\begin{align*} \cos \angle AEC = \left(\frac{12^2 + 27^2 - 9 \cdot 70}{2 \cdot 12 \cdot 27}\right) = \frac{3}{8} \end{align*}
Hence $\sin \angle AEC = \sqrt{1 - \cos^2 \angle AEC} = \frac{\sqrt{55}}{8}$ (taking the positive square root since $0^{\circ} < \angle AEC < 180^{\circ}$ , so $\sin\angle AEC > 0$ ). Using the identity $\sin x^{\circ} \equiv \sin\left(180-x\right)^{\circ}$ , we now deduce $\sin \angle AEF = \frac{\sqrt{55}}{8}$ . Finally, because $\triangle AEF, BEF$ have the same height and equal bases, they have the same area, yielding \[[ABF] = 2[AEF] = 2 \cdot \frac 12 \cdot AE \cdot EF \sin \angle AEF = 12 \cdot \frac{16}{3} \cdot \frac{\sqrt{55}}{8} = 8\sqrt{55},\] and so the answer is $8 + 55 = \boxed{063}$ .

## Solution 2
Let $AD$ and $CE$ intersect at $P$ . Since medians split one another in a $2:1$ ratio, we have
\begin{align*} AP = 12, PE = 9 \end{align*}
This gives isosceles $APE$ and thus an easy area calculation. After extending the altitude to $PE$ and using the fact that it is also a median, we find
\begin{align*} [APE] = \frac{27\sqrt{55}}{4} \end{align*}
Using Power of a Point, we have
\begin{align*} EF=\frac{16}{3} \end{align*}
By Same Height Different Base,
\begin{align*} \frac{[AFE]}{[APE]}=\frac{[AFE]}{(\frac{27\sqrt{55}}{4})}=\frac{EF}{PE}=\frac{(\frac{16}{3})}{9}=\frac{16}{27} \end{align*}
Solving gives
\begin{align*} [AFE] = 4\sqrt{55} \end{align*}
and
\begin{align*} [AFB]=2[AFE]=8\sqrt{55} \end{align*}
Thus, our answer is $8+55=\boxed{063}$ .

## Short Solution: Smart Similarity
Use the same diagram as in Solution 1. Call the centroid $P$ . It should be clear that $PE=9$ , and likewise $AP=12$ , $AE=12$ . Then, $\sin \angle AEP = \frac{\sqrt{55}}{8}$ . Power of a Point on $E$ gives $FE=\frac{16}{3}$ , and the area of $\triangle AFB$ is $AE \cdot EF \cdot \sin \angle AEP$ , which is twice the area of $\triangle AEF$ or $\triangle FEB$ (they have the same area because of equal base and height), giving $8\sqrt{55}$ for an answer of $\boxed{063}$ .

## Solution 4 (You've Forgotten Power of a Point Exists)
Note that, as above, it is quite easy to get that $\sin \angle AEP = \frac{\sqrt{55}}{8}$ (equate Heron's and $\frac{1}{2}ab\sin C$ to find this). Now note that $\angle FEA = \angle BEC$ because they are vertical angles, $\angle FAE = \angle ECB$ , and $\angle EFA = \angle ABC$ (the latter two are derived from the inscribed angle theorem). Therefore $\Delta AEF$ ~ $\Delta CEB$ and so $FE = \frac{144}{27}$ and $\sin \angle FEA = \frac{\sqrt{55}}{8}$ so the area of $\Delta BFA$ is $8\sqrt{55}$ giving us $\boxed{063}$ as our answer. (One may just get the area via triangle similarity too--this is if you are tired by the end of test and just want to bash some stuff out--it may also serve as a useful check).
~Dhillonr25

## Solution 5 (Barycentric Coordinates)
Apply barycentric coordinates on $\triangle ABC$ . We know that $D=\left(0, \frac{1}{2}, \frac{1}{2}\right), E=\left(\frac{1}{2}, \frac{1}{2}, 0\right)$ . We can now get the displacement vectors $\overrightarrow{AD} = \left(1, -\frac{1}{2}, -\frac{1}{2}\right)$ and $\overrightarrow{CE}=\left(-\frac{1}{2}, -\frac{1}{2}, 1\right)$ . Now, applying the distance formula and simplifying gives us the two equations \begin{align*} 2b^2+2c^2-a^2&=1296 \\ 2a^2+2b^2-c^2&=2916. \\ \end{align*} Substituting $c=24$ and solving with algebra now gives $a=6\sqrt{31}, b=3\sqrt{70}$ . Now we can find $F$ . Note that $CE$ can be parameterized as $(1:1:t)$ , so plugging into the circumcircle equation and solving for $t$ gives $t=\frac{-c^2}{a^2+b^2}$ so $F=(a^2+b^2:a^2+b^2:-c^2)$ . Plugging in for $a,b$ gives us $F=(1746:1746:-576)$ . Thus, by the area formula, we have \[\frac{[AFB]}{[ABC]}= \left|\begin{matrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \frac{97}{162} & \frac{97}{162} & -\frac{16}{81} \end{matrix}\right|=\frac{16}{81}.\] By Heron's Formula, we have $[ABC]=\frac{81\sqrt{55}}{2}$ which immediately gives $[AFB]=8\sqrt{55}$ from our ratio, extracting $\boxed{063}$ .
-Taco12

## Solution 6 (Law of Cosines + Stewart's theorem)
Since $AD$ is the median, let $BD=BC=x$ . Since $CE$ is a median, $AE=BE=12$ . Applying Power of a Point with respect to point $E$ , we see that $EF=\frac{16}{3}$ . Applying Stewart's Theorem on triangles $\triangle ADC$ and $\triangle ABC$ , we get that $x=3\sqrt{31}$ and $AC=3\sqrt{70}$ . The area of $\triangle AFB$ is simply $\frac{1}{2} \cdot \sin{\angle FBA}\cdot FB\cdot AB$ . We know $AB=24$ . Also, we know that $\angle FBA = \angle FCA$ . Then, applying Law of Cosines on triangle $EAC$ , we get that $\cos{\angle FCA}=\frac{3\sqrt{70}}{28}$ which means that $\sin{\angle FCA=\angle FBA}=\frac{\sqrt{154}}{28}$ . Then, applying Stewart's theorem on triangle $FBC$ with cevian $BE$ allows us to receive that $FB=\frac{4\sqrt{70}}{3}$ . Now, plugging into our earlier area formula, we receive $\frac{1}{2} \cdot \frac{\sqrt{154}}{28} \cdot \frac{4\sqrt{70}}{3} \cdot 24 = 8\sqrt{55}.$ Therefore, the desired answer is $8+55=\boxed{063}$ .
~SirAppel
These problems are copyrighted © by the Mathematical Association of America.