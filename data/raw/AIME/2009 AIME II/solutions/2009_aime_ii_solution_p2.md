# 2009 AIME II Problem 2

## Problem

Suppose that $a$ , $b$ , and $c$ are positive real numbers such that $a^{\log_3 7} = 27$ , $b^{\log_7 11} = 49$ , and $c^{\log_{11}25} = \sqrt{11}$ . Find \[a^{(\log_3 7)^2} + b^{(\log_7 11)^2} + c^{(\log_{11} 25)^2}.\]

## Solution 1
First, we have: \[x^{(\log_y z)^2} = x^{\left( (\log_y z)^2 \right) } = x^{(\log_y z) \cdot (\log_y z) } = \left( x^{\log_y z} \right)^{\log_y z}\]
Now, let $x=y^w$ , then we have: \[x^{\log_y z} = \left( y^w \right)^{\log_y z} = y^{w\log_y z} = y^{\log_y (z^w)} = z^w\]
This is all we need to evaluate the given formula. Note that in our case we have $27=3^3$ , $49=7^2$ , and $\sqrt{11}=11^{1/2}$ . We can now compute:
\[a^{(\log_3 7)^2} = \left( a^{\log_3 7} \right)^{\log_3 7} = 27^{\log_3 7} = (3^3)^{\log_3 7} = 7^3 = 343\]
Similarly, we get \[b^{(\log_7 11)^2} = (7^2)^{\log_7 11} = 11^2 = 121\]
and \[c^{(\log_{11} 25)^2} = (11^{1/2})^{\log_{11} 25} = 25^{1/2} = 5\]
and therefore the answer is $343+121+5 = \boxed{469}$ .

## Solution 2
We know from the first three equations that $\log_a27 = \log_37$ , $\log_b49 = \log_711$ , and $\log_c\sqrt{11} = \log_{11}25$ . Substituting, we find
\[a^{(\log_a27)(\log_37)} + b^{(\log_b49)(\log_711)} + c^{(\log_c\sqrt {11})(\log_{11}25)}.\]
We know that $x^{\log_xy} =y$ , so we find
\[27^{\log_37} + 49^{\log_711} + \sqrt {11}^{\log_{11}25}\]
\[(3^{\log_37})^3 + (7^{\log_711})^2 + ({11^{\log_{11}25}})^{1/2}.\]
The $3$ and the $\log_37$ cancel to make $7$ , and we can do this for the other two terms. Thus, our answer is
\[7^3 + 11^2 + 25^{1/2}\] \[= 343 + 121 + 5\] \[= \boxed {469}.\]

## Solution 3
First, let us take the log base 3 of the first expression. We get $\log_3{a^{\log_3{7}}} = 3$ . Simplifying, we get \[(\log_3{7})(\log_3{a}) = 3\] . So, \[\log_3 a = \frac{3}{\log_3{7}}\] , and \[a = 3^\frac{3}{log_3{7}}\] . We can repeat the same process for the other equations, giving us \[b = 7^\frac{2}{\log_7{11}}\] , and \[c = (\sqrt{11})^\frac{1}{\log_ {11}{25}}\] . Raising $a$ to the power of $(\log_3{7})^2$ , we get \[3^{3\log_3{7}} = 3^{\log_3{343}} = 343\] . Repeating a similar process for the other ones(you have to turn the square root to a fractional power for c), we get $343+121+5 = \boxed{469}$
~idk12345678
### See Also
These problems are copyrighted © by the Mathematical Association of America.