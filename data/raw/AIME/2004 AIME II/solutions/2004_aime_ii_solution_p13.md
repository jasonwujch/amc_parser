# 2004 AIME II Problem 13

## Problem

Let $ABCDE$ be a convex pentagon with $AB \parallel CE, BC \parallel AD, AC \parallel DE, \angle ABC=120^\circ, AB=3, BC=5,$ and $DE = 15.$ Given that the ratio between the area of triangle $ABC$ and the area of triangle $EBD$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers, find $m+n.$

## Solution
Let the intersection of $\overline{AD}$ and $\overline{CE}$ be $F$ . Since $AB \parallel CE, BC \parallel AD,$ it follows that $ABCF$ is a parallelogram , and so $\triangle ABC \cong \triangle CFA$ . Also, as $AC \parallel DE$ , it follows that $\triangle ABC \sim \triangle EFD$ .
By the Law of Cosines , $AC^2 = 3^2 + 5^2 - 2 \cdot 3 \cdot 5 \cos 120^{\circ} = 49 \Longrightarrow AC = 7$ . Thus the length similarity ratio between $\triangle ABC$ and $\triangle EFD$ is $\frac{AC}{ED} = \frac{7}{15}$ .
Let $h_{ABC}$ and $h_{BDE}$ be the lengths of the altitudes in $\triangle ABC, \triangle BDE$ to $AC, DE$ respectively. Then, the ratio of the areas $\frac{[ABC]}{[BDE]} = \frac{\frac 12 \cdot h_{ABC} \cdot AC}{\frac 12 \cdot h_{BDE} \cdot DE} = \frac{7}{15} \cdot \frac{h_{ABC}}{h_{BDE}}$ .
However, $h_{BDE} = h_{ABC} + h_{CAF} + h_{EFD}$ , with all three heights oriented in the same direction. Since $\triangle ABC \cong \triangle CFA$ , it follows that $h_{ABC} = h_{CAF}$ , and from the similarity ratio, $h_{EFD} = \frac{15}{7}h_{ABC}$ . Hence $\frac{h_{ABC}}{h_{BDE}} = \frac{h_{ABC}}{2h_{ABC} + \frac {15}7h_{ABC}} = \frac{7}{29}$ , and the ratio of the areas is $\frac{7}{15} \cdot \frac 7{29} = \frac{49}{435}$ . The answer is $m+n = \boxed{484}$ .
### Additional Trigonometry-Free Alternative
Instead of using the Law of Cosines, we can draw a line perpendicular to line BC down from point A until it intersects BC at a point $P$ . Since $\angle PBA = 60^{\circ}$ , we can use the $30-60-90$ triangle to deduce that $PB = \frac{3}{2}$ , and $PA = \frac{3\sqrt{3}}{2}$ . From here, we can use Pythagorean theorem to deduce that $AC = 7$ . Then, we can follow with the rest of the solution above.
These problems are copyrighted © by the Mathematical Association of America.