# 2005 AIME I Problem 15

## Problem

Triangle $ABC$ has $BC=20.$ The incircle of the triangle evenly trisects the median $AD.$ If the area of the triangle is $m \sqrt{n}$ where $m$ and $n$ are integers and $n$ is not divisible by the square of a prime, find $m+n.$

## Video Solution(For those who prefer)
https://youtu.be/OEXzJxdrP20 ~MC

## Solution 1
Let $E$ , $F$ and $G$ be the points of tangency of the incircle with $BC$ , $AC$ and $AB$ , respectively. Without loss of generality, let $AC < AB$ , so that $E$ is between $D$ and $C$ . Let the length of the median be $3m$ . Then by two applications of the Power of a Point Theorem , $DE^2 = 2m \cdot m = AF^2$ , so $DE = AF$ . Now, $CE$ and $CF$ are two tangents to a circle from the same point, so by the Two Tangent Theorem $CE = CF = c$ and thus $AC = AF + CF = DE + CE = CD = 10$ . Then $DE = AF = AG = 10 - c$ so $BG = BE = BD + DE = 20 - c$ and thus $AB = AG + BG = 30 - 2c$ .
Now, by Stewart's Theorem in triangle $\triangle ABC$ with cevian $\overline{AD}$ , we have
\[(3m)^2\cdot 20 + 20\cdot10\cdot10 = 10^2\cdot10 + (30 - 2c)^2\cdot 10.\]
Our earlier result from Power of a Point was that $2m^2 = (10 - c)^2$ , so we combine these two results to solve for $c$ and we get
\[9(10 - c)^2 + 200 = 100 + (30 - 2c)^2 \quad \Longrightarrow \quad c^2 - 12c + 20 = 0.\]
Thus $c = 2$ or $= 10$ . We discard the value $c = 10$ as extraneous (it gives us a line) and are left with $c = 2$ , so our triangle has area $\sqrt{28 \cdot 18 \cdot 8 \cdot 2} = 24\sqrt{14}$ and so the answer is $24 + 14 = \boxed{038}$ .

## Solution 2
WLOG let E be be between C & D (as in solution 1). Assume $AD = 3m$ . We use power of a point to get that $AG = DE = \sqrt{2}m$ and $AB = AG + GB = AG + BE = 10+2\sqrt{2} m$
Since now we have $AC = 10$ , $BC = 20, AB = 10+2\sqrt{2} m$ in triangle $\triangle ABC$ and cevian $AD = 3m$ . Now, we can apply Stewart's Theorem .
\[2000 + 180 m^2 = 10(10+2\sqrt{2}m)^{2} + 1000\] \[1000 + 180 m^2 = 1000 + 400\sqrt{2}m + 80 m^{2}\] \[100 m^2 = 400\sqrt{2}m\]
$m = 4\sqrt{2}$ or $m = 0$ if $m = 0$ , we get a degenerate triangle, so $m = 4\sqrt{2}$ , and thus $AB = 26$ . You can now use Heron's Formula to finish. The answer is $24 \sqrt{14}$ , or $\boxed{038}$ .
-Alexlikemath

## Solution 3
Let $E, F$ , and $G$ be the point of tangency (as stated in Solution 1). We can now let $AD$ be $3m$ . By using Power of a Point Theorem on A to the incircle, you get that $AG^2 = 2m^2$ . We can use it again on point D to the incircle to get the equation $(10 - CE)^2 = 2m^2$ . Setting the two equations equal to each other gives $(10 - CE)^2 = AG^2$ , and it can be further simplified to be $10 - CE = AG$
Let lengths $AC$ and $AB$ be called $b$ and $c$ , respectively. We can write $AG$ as $\frac{b + c - 20}{2}$ and $CE$ as $\frac{b + 20 - c}{2}$ . Plugging these into the equation, you get:
\[10 - \frac{b + 20 - c}{2} = \frac{b + c - 20}{2}\] \[b + c - 20 + b + 20 - c = 20 \rightarrow b = 10\]
Additionally, by Median of a triangle formula, you get that $3m = \frac{\sqrt{2c^2 - 200}}{2}$
Refer back to the fact that $AG^2 = 2m^2$ . We can now plug in our variables.
\[\left(\frac{b + c - 20}{2}\right)^2 = 2m^2 \rightarrow (c - 10)^2 = 8m^2\] \[c^2 - 20c + 100 = 8 \cdot \frac{2c^2 - 200}{36}\] \[9c^2 - 180c + 900 = 4c^2 - 400\] \[5c^2 - 180c + 1300 = 0\] \[c^2 - 36c + 260 = 0\]
Solving, you get that $c = 26$ or $10$ , but the latter will result in a degenerate triangle, so $c = 26$ . Finally, you can use Heron's Formula to get that the area is $24\sqrt{14}$ , giving an answer of $\boxed{038}$
~sky2025
These problems are copyrighted © by the Mathematical Association of America.