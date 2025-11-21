# 2025 AMC 10B Problem 5

## Problem

In $\triangle ABC$ , $AB = 10$ , $AC = 18$ , and $\angle B = 130^\circ$ . Let $O$ be the center of the circle containing points $A, B, C$ . What is the degree measure of $\angle CAO$ ?

$\textbf{(A)}\ 20^\circ \qquad \textbf{(B)}\ 30^\circ \qquad \textbf{(C)}\ 40^\circ \qquad \textbf{(D)}\ 50^\circ \qquad \textbf{(E)}\ 60^\circ$

### Note

The triangle lengths in this problem are not important.

## Solution 1 (can someone make the asymptote for this?)
Let us extend $\overline{AO}$ to meet $\odot{O}$ at $D$ .
Since $m\angle{ABC}=130$ °, by the Inscribed Angle Theorem, the measure of major arc $\overarc{AC}=260$ °. $\overline{AD}$ is a diameter of $\odot{O}$ , so the measure of top arc $\overarc{AD}=180$ , so $m\overarc{CD}=260-180=80$ ° and $m\angle{CAO}=\boxed{\textbf{(C) }40\textbf{°}}$ .
~Bocabulary142857

## Solution 2
Since $\angle ABC = 130^\circ$ , by the Inscribed Angle Theorem, it intercepts the major arc $AC$ , so that arc has measure $260^\circ$ . Point $O$ is the circumcenter, and is therefore outside of triangle ABC. Therefore, the minor arc $AC$ has measure $360^\circ - 260^\circ = 100^\circ$ . The central angle $\angle AOC$ subtends the minor arc $AC$ , so $\angle AOC = 100^\circ$ . Because $OA = OC$ are radii of the circumcircle, $\triangle AOC$ is isosceles, so $\angle CAO = \angle ACO$ . Let $\angle CAO = \angle ACO = x$ . Then $x + x + 100^\circ = 180^\circ$ , so $2x = 80^\circ$ and $x = 40^\circ$ . Thus, $\angle CAO = \boxed{40^\circ}$ .
~Strickenox
~EZ123 (Minor edits)
Below is a diagram to help visualize the problem :
[asy] size(220); // Choose coordinates so that angle B is obtuse (~130°) pair B = (0,0); pair C = (3,0); pair A = 3*dir(130); // Circumcenter of triangle ABC (outside since angle at B is obtuse) pair O = circumcenter(A,B,C); // Draw circumcircle draw(circle(O, abs(O - A)), gray(0.7)); // Draw triangle ABC draw(A--B--C--cycle); // Draw radii OA and OC draw(O--A, dashed); draw(O--C, dashed); // Label points dot("$A$", A, NE); dot("$B$", B, S); dot("$C$", C, SE); dot("$O$", O, N); [/asy]

## Solution 3 (similar to solution 1, in a way)
Extend line $\overline{AO}$ to meet $\odot{O}$ at $D$ . We can now easily see that quadrilateral $ABCD$ is a cyclic quadrilateral, thus $\angle ABC + \angle ADC = 180^{\circ}$ .
Since $\angle ABC = 130^{\circ}$ , $\angle ADC = 50^{\circ}$ .
We also know that $\triangle ODC$ is isosceles because of the two radii. Thus $\angle DOC = 180^{\circ} - 2{\times} \angle ADC$ . $\angle DOC = 80^{\circ}$ .
By the inscribed angle theorem, $\angle CAO$ is half of $\angle DOC$ .
So $\angle CAO = \boxed{\textbf{(C) }40\textbf{°}}$ .
~ILoveSpaghetti

## Solution 4 (longest way, used in-comp)
Yes, you can solve this problem without all this but whatever
To begin, imagine triangle $ABC$ floating in the plane. Nothing restricts the orientation, so for convenience we place point $B$ at the origin of a coordinate plane. Let $B=(0,0)$ . Choose the positive $x$ -axis to lie along segment $BA$ , which places $A$ on the positive $x$ -axis. Because $AB=10$ , we place \[ A=(10,0). \]
Now determine coordinates of point $C$ . We know $AC=18$ and angle $B=130^\circ$ . Since $BA$ points horizontally to the right, segment $BC$ makes an angle of $130^\circ$ above the positive $x$ -axis. If the length $BC$ is $x$ , then \[ C=(x\cos130^\circ,\;x\sin130^\circ). \]
We compute $x$ from the Law of Cosines at angle $B$ : \[ AC^2 = AB^2 + BC^2 - 2(AB)(BC)\cos B. \] Substitute $AB=10,\ AC=18,\ \cos130^\circ=-\cos50^\circ\approx -0.6427876097$ : \[ 324=100 + x^2 - 2(10)x(-0.6427876097), \] so \[ 324 = 100 + x^2 + 12.85575219\,x. \] Move all terms to one side: \[ x^2 + 12.85575219\,x - 224 = 0. \]
Using the quadratic formula: \[ x=\frac{-12.85575219\pm\sqrt{(12.85575219)^2+4\cdot224}}{2}. \] Compute: \[ (12.85575219)^2 \approx 165.301,\qquad 4\cdot224=896, \] so the discriminant is \[ 1061.301,\qquad \sqrt{1061.301}\approx 32.583. \] Thus \[ x=\frac{-12.85575219+32.583}{2}\approx 9.8636. \]
Hence \[ C=(9.8636\cos130^\circ,\;9.8636\sin130^\circ). \] Using $\cos130^\circ=-0.6427876097$ and $\sin130^\circ=0.7660444431$ : \[ C_x\approx -6.339,\qquad C_y\approx 7.554, \] so \[ C\approx(-6.339,\;7.554). \]
Now the three sides of triangle $ABC$ are \[ AB=10,\qquad AC=18,\qquad BC\approx 9.8636. \]
\textbf{Compute angle $A$ using the Law of Sines:} \[ \frac{\sin A}{BC}=\frac{\sin B}{AC} \] so \[ \sin A = \frac{BC\sin130^\circ}{18}
\] Thus \[ A\approx \arcsin(0.41965)\approx 24.78^\circ. \] Then \[ C=180^\circ-A-B=180^\circ-24.78^\circ-130^\circ=25.22^\circ. \]
\textbf{Confirm angle $C$ using vectors:}
\[ CA=A-C=(16.339,\,-7.554),\qquad CB=B-C=(6.339,\,-7.554). \] Dot product: \[ CA\cdot CB = 103.530 + 57.050 = 160.580. \] Magnitudes: \[ |CA|\approx 18,\qquad |CB|\approx 9.8636. \] Thus \[ \cos C = \frac{160.580}{18\cdot 9.8636} \approx 0.9045, \qquad C\approx 25.22^\circ. \]
\textbf{Circumradius $R$ :} \[ R=\frac{a}{2\sin A}=\frac{BC}{2\sin A} = \frac{9.8636}{0.83930}\approx 11.759. \]
\textbf{Compute angle $\angle CAO$ .}
In triangle $AOC$ , we know $OA=OC=R$ and $AC=18$ . Apply Law of Cosines: \[ AC^2 = OA^2 + OC^2 - 2(OA)(OC)\cos\theta, \] where $\theta=\angle AOC$ . Substitute: \[ 324 = 2(11.759^2)-2(11.759)^2\cos\theta \] \[ 324=276.58-276.58\cos\theta. \] Thus \[ \cos\theta = -\frac{47.42}{276.58}\approx -0.17148, \qquad \theta\approx 99.86^\circ. \] Since triangle $AOC$ is isosceles, with base angles $\phi=\angle CAO$ , \[ 2\phi + 99.86^\circ = 180^\circ, \qquad \phi = 40.07^\circ. \]
\textbf{Coordinate confirmation:}
Circumcenter lies at intersection of $x=5$ and perpendicular bisector of $BC$ . This yields \[ O=(5,\;10.627). \] Vectors: \[ AO=(-5,\;10.627),\qquad AC=(-16.339,\;7.554). \] Compute \[ AO\cdot AC = 161.943, \qquad |AO|\approx 11.747,\; |AC|=18. \] So \[ \cos\angle CAO=\frac{161.943}{11.747\cdot 18}\approx 0.7655, \] \[ \angle CAO\approx 40.1^\circ. \]
\[ \boxed{\angle CAO \approx 40^\circ.} \]
~notvalid

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution 2 (Fast and Easy)
https://www.youtube.com/watch?v=CLj9QhT65Wc
~ Pi Academy

## Video Solution 3 by Daily Dose of Math
https://youtu.be/s-Wimgu9wto
~Thesmartgreekmathdude
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .