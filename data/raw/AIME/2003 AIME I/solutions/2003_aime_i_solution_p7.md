# 2003 AIME I Problem 7

## Problem

Point $B$ is on $\overline{AC}$ with $AB = 9$ and $BC = 21.$ Point $D$ is not on $\overline{AC}$ so that $AD = CD,$ and $AD$ and $BD$ are integers . Let $s$ be the sum of all possible perimeters of $\triangle ACD$ . Find $s.$

## Solution 1 (Pythagorean Theorem)
Denote the height of $\triangle ACD$ as $h$ , $x = AD = CD$ , and $y = BD$ . Using the Pythagorean theorem , we find that $h^2 = y^2 - 6^2$ and $h^2 = x^2 - 15^2$ . Thus, $y^2 - 36 = x^2 - 225 \Longrightarrow x^2 - y^2 = 189$ . The LHS is difference of squares , so $(x + y)(x - y) = 189$ . As both $x,\ y$ are integers, $x+y,\ x-y$ must be integral divisors of $189$ .
The pairs of divisors of $189$ are $(1,189)\ (3,63)\ (7,27)\ (9,21)$ . This yields the four potential sets for $(x,y)$ as $(95,94)\ (33,30)\ (17,10)\ (15,6)$ . The last is not a possibility since it simply degenerates into a line . The sum of the three possible perimeters of $\triangle ACD$ is equal to $3(AC) + 2(x_1 + x_2 + x_3) = 90 + 2(95 + 33 + 17) = \boxed{380}$ .

## Solution 2 (Stewart's Theorem)
Let $AD=c$ and $BD=d$ , then by Stewart's Theorem we have:
$30d^2+21*9*30=9c^2+21c^2=30c^2$ . After simplifying:
$d^2-c^2=189$ .
The solution follows as above.

## Solution 3 (Law of Cosines)
Drop an altitude from point $D$ to side $AC$ . Let the intersection point be $E$ . Since triangle $ADC$ is isosceles, AE is half of $AC$ , or $15$ . Then, label side AD as $x$ . Since $AED$ is a right triangle, you can figure out $\cos A$ with adjacent divided by hypotenuse, which in this case is $AE$ divided by $x$ , or $\frac{15}{x}$ . Now we apply law of cosines. Label $BD$ as $y$ . Applying law of cosines, $y^2 = x^2+9^2- 2 \cdot x \cdot 9 \cdot \cos A$ . Since $\cos A$ is equal to $\frac{15}{x}$ , $y^2 = x^2+9^2- 2 \cdot x \cdot 9 \cdot \frac{15}{x}$ , which can be simplified to $x^2-y^2=189$ . The solution proceeds as the first solution does.
-intelligence_20
- Stewart's Theorem
These problems are copyrighted © by the Mathematical Association of America.