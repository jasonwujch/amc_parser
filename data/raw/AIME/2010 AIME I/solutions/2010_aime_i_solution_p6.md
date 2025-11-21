# 2010 AIME I Problem 6

## Problem

Let $P(x)$ be a quadratic polynomial with real coefficients satisfying $x^2 - 2x + 2 \le P(x) \le 2x^2 - 4x + 3$ for all real numbers $x$ , and suppose $P(11) = 181$ . Find $P(16)$ .

## Solution

## Solution 1
Let $Q(x) = x^2 - 2x + 2$ , $R(x) = 2x^2 - 4x + 3$ . Completing the square , we have $Q(x) = (x-1)^2 + 1$ , and $R(x) = 2(x-1)^2 + 1$ , so it follows that $P(x) \ge Q(x) \ge 1$ for all $x$ (by the Trivial Inequality ).
Also, $1 = Q(1) \le P(1) \le R(1) = 1$ , so $P(1) = 1$ , and $P$ obtains its minimum at the point $(1,1)$ . Then $P(x)$ must be of the form $c(x-1)^2 + 1$ for some constant $c$ ; substituting $P(11) = 181$ yields $c = \frac 95$ . Finally, $P(16) = \frac 95 \cdot (16 - 1)^2 + 1 = \boxed{406}$ .

## Solution 2
It can be seen that the function $P(x)$ must be in the form $P(x) = ax^2 - 2ax + c$ for some real $a$ and $c$ . This is because the derivative of $P(x)$ is $2ax - 2a$ , and a global minimum occurs only at $x = 1$ (in addition, because of this derivative, the vertex of any quadratic polynomial occurs at $\frac{-b}{2a}$ ). Substituting $(1,1)$ and $(11, 181)$ we obtain two equations:
Solving, we get $a = \frac{9}{5}$ and $c = \frac{14}{5}$ , so $P(x) = \frac{9}{5}x^2 - \frac{18}{5}x + \frac {14}{5}$ . Therefore, $P(16) = \boxed{406}$ .

## Solution 3
Let $y = x^2 - 2x + 2$ ; note that $2y - 1 = 2x^2 - 4x + 3$ . Setting $y = 2y - 1$ , we find that equality holds when $y = 1$ and therefore when $x^2 - 2x + 2 = 1$ ; this is true iff $x = 1$ , so $P(1) = 1$ .
Let $Q(x) = P(x) - x$ ; clearly $Q(1) = 0$ , so we can write $Q(x) = (x - 1)Q'(x)$ , where $Q'(x)$ is some linear function. Plug $Q(x)$ into the given inequality:
$x^2 - 3x + 2 \le Q(x) \le 2x^2 - 5x + 3$
$(x - 1)(x - 2) \le (x - 1)Q'(x) \le (x - 1)(2x - 3)$ , and thus
$x - 2 \le Q'(x) \le 2x - 3$
For all $x > 1$ ; note that the inequality signs are flipped if $x < 1$ , and that the division is invalid for $x = 1$ . However,
$\lim_{x \to 1} x - 2 = \lim_{x \to 1} 2x - 3 = -1$ ,
and thus by the sandwich theorem $\lim_{x \to 1} Q'(x) = -1$ ; by the definition of a continuous function, $Q'(1) = -1$ . Also, $Q(11) = 170$ , so $Q'(11) = 170/(11-1) = 17$ ; plugging in and solving, $Q'(x) = (9/5)(x - 1) - 1$ . Thus $Q(16) = 390$ , and so $P(16) = \boxed{406}$ .

## Solution 4
Let $Q(x) = P(x) - (x^2-2x+2)$ , then $0\le Q(x) \le (x-1)^2$ (note this is derived from the given inequality chain). Therefore, $0\le Q(x+1) \le x^2 \Rightarrow Q(x+1) = Ax^2$ for some real value A.
$Q(11) = 10^2A \Rightarrow P(11)-(11^2-22+2)=100A \Rightarrow 80=100A \Rightarrow A=\frac{4}{5}$ .
$Q(16)=15^2A=180 \Rightarrow P(16)-(16^2-32+2) = 180 \Rightarrow P(16)=180+226= \boxed{406}$

## Solution 5
Let $P(x) = ax^2 + bx + c$ . Plugging in $x = 1$ to the expressions on both sides of the inequality, we see that $a + b + c = 1$ . We see from the problem statement that $121a + 11b + c = 181$ . Since we know the vertex of $P(x)$ lies at $x = 1$ , by symmetry we get $81a -9b + c = 181$ as well. Since we now have three equations, we can solve this trivial system and get our answer of $\boxed{406}$ .

## Solution 6
Similar to Solution 5, let $P(x) = ax^2 + bx + c$ . Note that $(1,1)$ is a vertex of the polynomial. Additionally, this means that $b = -2a$ (since $\frac{-b}{2a}$ is the minimum $x$ point). Thus, we have $P(x) = ax^2 - 2ax + c$ . Therefore $a - 2a + c = 1$ . Moreover, $99a + c = 181$ . And so our polynomial is $\frac{9}{5}x^2 - \frac{18}{5}x + \frac{14}{5}$ . Plug in $x = 16$ to get $\boxed{406}$ .

## Solution 7
Very similar to Solution 6, start by noticing that $P(x)$ is between two polynomials, we try to set them equal to find a point where the two polynomials intersect, meaning that $P(x)$ would also have to intersect that point (it must be between the two graphs). Setting $x^2 - 2x + 2 = 2x^2 - 4x + 3$ , we find that $x = 1$ . Note that both of these graphs have the same vertex (at $x = 1$ ), and so $P(x)$ must also have the same vertex $(1, 1)$ . Setting $P(x) = ax^2 - 2ax + a + 1$ (this is where we have a vertex at $(1, 1)$ ), we plug in $11$ and find that $a = 1.8$ . Evaluating $1.8x^2 - 3.6x + 2.8$ when $x = 16$ (our intended goal), we find that $P(16) = \boxed{406}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .