# 2013 AIME I Problem 13

## Problem

Triangle $AB_0C_0$ has side lengths $AB_0 = 12$ , $B_0C_0 = 17$ , and $C_0A = 25$ . For each positive integer $n$ , points $B_n$ and $C_n$ are located on $\overline{AB_{n-1}}$ and $\overline{AC_{n-1}}$ , respectively, creating three similar triangles $\triangle AB_nC_n \sim \triangle B_{n-1}C_nC_{n-1} \sim \triangle AB_{n-1}C_{n-1}$ . The area of the union of all triangles $B_{n-1}C_nB_n$ for $n\geq1$ can be expressed as $\tfrac pq$ , where $p$ and $q$ are relatively prime positive integers. Find $q$ .

## Solution 1
Note that every $B_nC_n$ is parallel to each other for any nonnegative $n$ . Also, the area we seek is simply the ratio $k=\frac{[B_0B_1C_1]}{[B_0B_1C_1]+[C_1C_0B_0]}$ , because it repeats in smaller and smaller units. Note that the area of the triangle, by Heron's formula, is 90.
For ease, all ratios I will use to solve this problem are with respect to the area of $[AB_0C_0]$ . For example, if I say some area has ratio $\frac{1}{2}$ , that means its area is 45.
Now note that $k=$ 1 minus ratio of $[B_1C_1A]$ minus ratio $[B_0C_0C_1]$ . We see by similar triangles given that ratio $[B_0C_0C_1]$ is $\frac{17^2}{25^2}$ . Ratio $[B_1C_1A]$ is $(\frac{336}{625})^2$ , after seeing that $C_1C_0 = \frac{289}{625}$ , . Now it suffices to find 90 times ratio $[B_0B_1C_1]$ , which is given by 1 minus the two aforementioned ratios. Substituting these ratios to find $k$ and clearing out the $5^8$ , we see that the answer is $90\cdot \frac{5^8-336^2-17^2\cdot 5^4}{5^8-336^2}$ , which gives $q= \boxed{961}$ .

## Solution 2
Using Heron's Formula we can get the area of the triangle $\Delta AB_0C_0 = 90$ .
Since $\Delta AB_0C_0 \sim \Delta B_0C_1C_0$ then the scale factor for the dimensions of $\Delta B_0C_1C_0$ to $\Delta AB_0C_0$ is $\dfrac{17}{25}.$
Therefore, the area of $\Delta B_0C_1C_0$ is $(\dfrac{17}{25})^2(90)$ . Also, the dimensions of the other sides of the $\Delta B_0C_1C_0$ can be easily computed: $\overline{B_0C_1}= \dfrac{17}{25}(12)$ and $\overline{C_1C_0} = \dfrac{17^2}{25}$ . This allows us to compute one side of the triangle $\Delta AB_0C_0$ , $\overline{AC_1} = 25 - \dfrac{17^2}{25} = \dfrac{25^2 - 17^2}{25}$ . Therefore, the scale factor $\Delta AB_1C_1$ to $\Delta AB_0C_0$ is $\dfrac{25^2 - 17^2}{25^2}$ , which yields the length of $\overline{B_1C_1}$ as $\dfrac{25^2 - 17^2}{25^2}(17)$ . Therefore, the scale factor for $\Delta B_1C_2C_1$ to $\Delta B_0C_1C_0$ is $\dfrac{25^2 - 17^2}{25^2}$ . Some more algebraic manipulation will show that $\Delta B_nC_{n+1}C_n$ to $\Delta B_{n-1}C_nC_{n-1}$ is still $\dfrac{25^2 - 17^2}{25^2}$ . Also, since the triangles are disjoint, the area of the union is the sum of the areas. Therefore, the area is the geometric series $\dfrac{90 \cdot 17^2}{25^2} \sum_{n=0}^{\infty} (\dfrac{25^2-17^2}{25^2})^2$ At this point, it may be wise to "simplify" $25^2 - 17^2 = (25-17)(25+17) = (8)(42) = 336$ . So the geometric series converges to $\dfrac{90 \cdot 17^2}{25^2} \dfrac{1}{1 - \dfrac{336^2}{625^2}} = \dfrac{90 \cdot 17^2}{25^2} \dfrac{625^2}{625^2 - 336^2}$ . Using the difference of squares, we get $\dfrac{90 \cdot 17^2}{25^2}\dfrac{625^2}{(625 - 336)(625 + 336)}$ , which simplifies to $\dfrac{90 \cdot 17^2}{25^2} \dfrac{625^2}{(289)(961)}$ . Cancelling all common factors, we get the reduced fraction $= \dfrac{90 \cdot 25^2}{31^2}$ . So $\frac{p}{q}=1-\frac{90 \cdot 25^2}{31^2}=\frac{90 \cdot 336}{961}$ , yielding the answer $\fbox{961}$ .

## Solution 3
For this problem, the key is to find the $\frac{[\triangle{B_nB_{n-1}C_n}]}{[\triangle{AB_{n-1}C_{n-1}}]}$ .
The area of the biggest triangle is $90$ according to the Heron's formula easily
Firstly, we discuss the ratio of $\frac{[\triangle{B_0C_1C_0}]}{[\triangle{AB_0C_0}]}$
Since the problem said that two triangles are similar, so $\frac{C_1C_0}{B_0C_0}=\frac{17}{25}$ ,
Getting that $C_1C_0=\frac{289}{25}$ , which is not hard to find that $AC_1=\frac{336}{25}$ , Since $\frac{AB_1}{AB_0}=\frac{AC_1}{AC_0}=\frac{336}{625}$ ,
we can find the ratio of $\frac{[\triangle{B_0B_1C_1}]}{[\triangle{AB_0C_0}]}=\frac{336}{625}\cdot\frac{289}{625}$ , the common ratio between two similar triangles is $(\frac{336}{625})^2$ , the similar triangles means two consecutive $(\triangle{AB_nC_n});(\triangle{AB_{n+1}C_{n+1}})$
Now the whole summation of $S=1+(\frac{336}{625})^2+(\frac{336}{625})^4+....+(\frac{336}{625})^n=\frac{625^2}{961\cdot289}$
The desired answer is $90\cdot\frac{336\cdot289\cdot625^2}{625^2\cdot961\cdot289}=\frac{30240}{961}$ Which our answer is $\fbox{961}$
~bluesoul ~Marshall_Huang (some minor latex stuff}

## Solution 4
Let $k$ be the coefficient of the similarity of triangles \[\triangle B_0 C_1 C_0 \sim \triangle AB_0 C_0 \implies k = \frac {B_0 C_0}{AC_0} = \frac {17}{25}.\] Then area $\frac {[B_0 C_1 C_0]}{[AB_0 C_0 ]} = k^2 \implies \frac {[AB_0 C_1]}{[AB_0 C_0]} = 1 – k^2.$
The height of triangles $\triangle B_0C_1A$ and $\triangle AB_0C_0$ from $B_0$ is the same $\implies \frac {AC_1}{AC_0} = 1 – k^2.$
The coefficient of the similarity of triangles $\triangle AB_1C_1 \sim \triangle AB_0C_0$ is $\frac {AC_1}{AC_0} = 1 – k^2 \implies \frac {[B_1C_1C_2 ]}{[AB_0C_0 ]} = k^2 (1 – k^2)^2.$
Analogically the coefficient of the similarity of triangles $\triangle AB_2C_2 \sim \triangle AB_0C_0$ is $(1 – k^2)^2 \implies \frac {[B_2C_2C_3]}{[AB_0C_0 ]} = k^2 (1 – k^2)^4$ and so on.
The yellow area $[Y]$ is $\frac {[Y]}{[AB_0C_0 ]} = k^2 + k^2 (1 – k^2)^2 + k^2 (1 – k^2)^4 +.. = \frac {k^2}{1 – (1 – k^2)^2} = \frac{1}{2 – k^2}.$
The required area is $[AB_0C_0 ] – [Y] = [AB_0C_0 ] \cdot (1 – \frac{1}{2 – k^2}) = [AB_0C_0 ] \cdot \frac {1 – k^2}{2 – k^2} = [AB_0C_0 ] \cdot \frac {25^2 – 17^2} {2 \cdot 25^2 – 17^2} = [AB_0C_0 ] \cdot \frac {336}{961}.$
The number $961$ is prime, $[AB_0C_0]$ is integer but not $961,$ therefore the answer is $\boxed{961}$ .
vladimir.shelomovskii@gmail.com, vvsss

## Video Solution
https://youtu.be/IdM24SLrxQw?si=mu5fQ-_rFZM4ud2_
~MathProblemSolvingSkills.com

## Video Solution by mop 2024
https://youtu.be/byoHYJx40bU
~r00tsOfUnity
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .