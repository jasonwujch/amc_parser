# 2005 AIME I Problem 8

## Problem

The equation $2^{333x-2} + 2^{111x+2} = 2^{222x+1} + 1$ has three real roots . Given that their sum is $m/n$ where $m$ and $n$ are relatively prime positive integers , find $m+n.$

## Solution
Let $y = 2^{111x}$ . Then our equation reads $\frac{1}{4}y^3 + 4y = 2y^2 + 1$ or $y^3 - 8y^2 + 16y - 4 = 0$ . Thus, if this equation has roots $r_1, r_2$ and $r_3$ , by Vieta's formulas we have $r_1\cdot r_2\cdot r_3 = 4$ . Let the corresponding values of $x$ be $x_1, x_2$ and $x_3$ . Then the previous statement says that $2^{111\cdot(x_1 + x_2 + x_3)} = 4$ so taking a logarithm of that gives $111(x_1 + x_2 + x_3) = 2$ and $x_1 + x_2 + x_3 = \frac{2}{111}$ . Thus the answer is $111 + 2 = \boxed{113}$ .
These problems are copyrighted © by the Mathematical Association of America.