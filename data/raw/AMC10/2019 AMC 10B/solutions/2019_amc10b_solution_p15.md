# 2019 AMC 10B Problem 15

## Problem

Right triangles $T_1$ and $T_2$ , have areas of 1 and 2, respectively. A side of $T_1$ is congruent to a side of $T_2$ , and a different side of $T_1$ is congruent to a different side of $T_2$ . What is the square of the product of the lengths of the other (third) sides of $T_1$ and $T_2$ ?

$\textbf{(A) }\frac{28}{3}\qquad\textbf{(B) }10\qquad\textbf{(C) }\frac{32}{3}\qquad\textbf{(D) }\frac{34}{3}\qquad\textbf{(E) }12$

## Solution 1
First of all, let the two sides which are congruent be $x$ and $y$ , where $y > x$ . The only way that the conditions of the problem can be satisfied is if $x$ is the shorter leg of $T_{2}$ and the longer leg of $T_{1}$ , and $y$ is the longer leg of $T_{2}$ and the hypotenuse of $T_{1}$ .
Notice that this means the value we are looking for is the square of $\sqrt{x^{2}+y^{2}} \cdot \sqrt{y^{2}-x^{2}} = \sqrt{y^{4}-x^{4}}$ , which is just $y^{4}-x^{4}$ .
The area conditions give us two equations: $\frac{xy}{2} = 2$ and $\frac{x\sqrt{y^{2}-x^{2}}}{2} = 1$ .
This means that $y = \frac{4}{x}$ and that $\frac{4}{x^{2}} = y^{2} - x^{2}$ .
Taking the second equation, we get $x^{2}y^{2} - x^{4} = 4$ , so since $xy = 4$ , $x^{4} = 12$ .
Since $y = \frac{4}{x}$ , we get $y^{4} = \frac{256}{12} = \frac{64}{3}$ .
The value we are looking for is just $y^{4}-x^{4} = \frac{64-36}{3} = \frac{28}{3}$ so the answer is $\boxed{\textbf{(A) }\frac{28}{3}}$ .

## Solution 2
Like in Solution 1, we have $\frac{xy}{2} = 2$ and $\frac{x\sqrt{y^{2}-x^{2}}}{2} = 1$ .
Squaring both equations yields $x^2y^2=16$ and $x^2(y^2-x^2)=4$ .
Let $a = x^2$ and $b = y^2$ . Then $b = \frac{16}{a}$ , and $a\left(\frac{16}{a}-a\right)=4 \implies 16 - a^2 = 4 \implies a = 2\sqrt3$ , so $b = \frac{16}{2\sqrt3} = \frac{8\sqrt3}{3}$ .
We are looking for the value of $y^4 - x^4 = b^2 - a^2$ , so the answer is $\frac{64}{3} - 12 = \boxed{\textbf{(A) }\frac{28}{3}}$ .

## Solution 3
Firstly, let the right triangles be $\triangle ABC$ and $\triangle EDF$ , with $\triangle ABC$ being the smaller triangle. As in Solution 1, let $\overline{AB} = \overline{EF} = x$ and $\overline{BC} = \overline{DF} = y$ . Additionally, let $\overline{AC} = z$ and $\overline{DE} = w$ .
We are given that $[ABC] = 1$ and $[EDF] = 2$ , so using $\text{area} = \frac{bh}{2}$ , we have $\frac{xy}{2} = 1$ and $\frac{xw}{2} = 2$ . Dividing the two equations, we get $\frac{xy}{xw}$ = $\frac{y}{w} = 2$ , so $y = 2w$ .
Thus $\triangle EDF$ is a $30^{\circ}-60^{\circ}-90^{\circ}$ right triangle, meaning that $x = w\sqrt{3}$ . Now by the Pythagorean Theorem in $\triangle ABC$ , $\left(w\sqrt{3}\right)^2 + \left(2w\right)^2 = z^2 \Rightarrow 3w^2 + 4w^2 = z^2 \Rightarrow 7w^2 = z^2 \Rightarrow w\sqrt{7} = z$ .
The problem requires the square of the product of the third side lengths of each triangle, which is $(wz)^2$ . By substitution, we see that $wz$ = $\left(w\right)\left(w\sqrt{7}\right) = w^2\sqrt{7}$ . We also know $\frac{xw}{2} = 1 \Rightarrow\frac{(w)\left(w\sqrt{3}\right)}{2} =1 \Rightarrow (w)\left(w\sqrt{3}\right) = 2 \Rightarrow w^2\sqrt{3} = 2 \Rightarrow w^2 = \frac{2\sqrt{3}}{3}$ .
Since we want $\left(w^2\sqrt{7}\right)^2$ , multiplying both sides by $\sqrt{7}$ gets us $w^2\sqrt{7} = \frac{2\sqrt{21}}{3}$ . Now squaring gives $\left(\frac{2\sqrt{21}}{3}\right)^2 = \frac{4*21}{9} = \boxed{\textbf{(A) }\frac{28}{3}}$ .
[Note: there is a mismatch of variables near the beginning that someone can fix: xw/2 is the area of the small triangle, which is actually the 30-60-90.]

## Video Solution
https://youtu.be/mXvetCMMzpU
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .