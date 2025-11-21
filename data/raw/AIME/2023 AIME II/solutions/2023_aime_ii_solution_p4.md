# 2023 AIME II Problem 4

## Problem

Let $x,y,$ and $z$ be real numbers satisfying the system of equations \begin{align*} xy + 4z &= 60 \\ yz + 4x &= 60 \\ zx + 4y &= 60. \end{align*} Let $S$ be the set of possible values of $x.$ Find the sum of the squares of the elements of $S.$

## Solution 1
We first subtract the second equation from the first, noting that they both equal $60$ . \begin{align*} xy+4z-yz-4x&=0 \\ 4(z-x)-y(z-x)&=0 \\ (z-x)(4-y)&=0 \end{align*}
Case 1: Let $y=4$ .
The first and third equations simplify to: \begin{align*} x+z&=15 \\ xz&=44 \end{align*} from which it is apparent that $x=4$ and $x=11$ are solutions.
Case 2: Let $x=z$ .
The first and third equations simplify to: \begin{align*} xy+4x&=60 \\ x^2+4y&=60 \end{align*}
We subtract the following equations, yielding: \begin{align*} x^2+4y-xy-4x&=0 \\ x(x-4)-y(x-4)&=0 \\ (x-4)(x-y)&=0 \end{align*}
We thus have $x=4$ and $x=y$ , substituting in $x=y=z$ and solving yields $x=6$ and $x=-10$ .
Then, we just add the squares of the solutions (make sure not to double count the $4$ ), and get \[4^2+11^2+6^2+(-10)^2=16+121+36+100=\boxed{273}.\] ~SAHANWIJETUNGA

## Solution 2
We index these equations as (1), (2), and (3), respectively. Taking $(1)-(2)$ , we get \[ \left( x - z \right) \left( y - 4 \right) = 0 . \]
Denote $x' = x - 4$ , $y' = y - 4$ , $z' = z - 4$ . Thus, the above equation can be equivalently written as \[ \left( x' - z' \right) y' = 0 . \hspace{1cm} (1') \]
Similarly, by taking $(2)-(3)$ , we get \[ \left( y' - x' \right) z' = 0 . \hspace{1cm} (2') \]
By taking $(3) - (1)$ , we get \[ \left( z' - y' \right) x' = 0 . \hspace{1cm} (3') \]
From $(3')$ , we have the following two cases.
Case 1: $x' = 0$ .
Plugging this into $(1')$ and $(2')$ , we get $y'z' = 0$ . Thus, $y' = 0$ or $z' = 0$ .
Because we only need to compute all possible values of $x$ , without loss of generality, we only need to analyze one case that $y' = 0$ .
Plugging $x' = 0$ and $y' = 0$ into (1), we get a feasible solution $x = 4$ , $y = 4$ , $z = 11$ .
Case 2: $x' \neq 0$ and $z' - y' = 0$ .
Plugging this into $(1')$ and $(2')$ , we get $\left( x' - y' \right) y' = 0$ .
Case 2.1: $y' = 0$ .
Thus, $z' = 0$ . Plugging $y' = 0$ and $z' = 0$ into (1), we get a feasible solution $x = 11$ , $y = 4$ , $z = 4$ .
Case 2.2: $y' \neq 0$ and $x' = y'$ .
Thus, $x' = y' = z'$ . Plugging these into (1), we get $\left( x, y, z \right) = \left( -10, -10, -10 \right)$ or $\left( 6, 6, 6 \right)$ .
Putting all cases together, $S = \left\{ 4, 11, -10, 6 \right\}$ . Therefore, the sum of the squares of the elements of $S$ is \begin{align*} 4^2 + 11^2 + \left( -10 \right)^2 + 6^2 = \boxed{\textbf{(273) }} . \end{align*}
~ Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (Quadratic Formula and Vieta's Formulas)
We index these equations as (1), (2), and (3), respectively. Using equation (1), we get $z = \frac{60 - xy}{4} = 15 - \frac{xy}{4}$ We need to solve for x, so we plug this value of z into equation (3) to get:
\[15x - \frac{x^2y}{4} - 4y = 60\] \[\frac{y}{4} * x^2 - 15x + (60 + 4y) = 0\]
We use the quadratic formula to get possible values of x:
\[x = \frac{15 \pm \sqrt{15^2 - 4(\frac{y}{4})(60 + 4y)}}{\frac{y}{2}}\] \[x = \frac{30 \pm 2\sqrt{225 - 60y + 4y^2}}{y}\] \[x = \frac{30 \pm 2\sqrt{(2y-15)^2}}{y}\] \[x = \frac{30 \pm 2(2y - 15)}{y}\] \[x = \frac{30 \pm (4y - 30)}{y}\]
Here, we have two cases, (plus) and (minus) In the plus case, we have: \[x = \frac{(30 + 4y - 30)}{y}\] \[x = 4\]
So, our first case gives us one value of x, which is 4. In the minus case, we have: \[x = \frac{30 - (4y - 30)}{y}\] \[x = \frac{60 - 4y}{y}\] \[x = \frac{60}{y} - 4\]
For this case, we now have values of x in terms of y. Plugging this expression for x in equation (1), we get \[60 - 4y + 4z = 60\] \[4z = 4y\] \[z = y\]
So we know that for this case, z = y. Using this information in equation (2), we get \[y^2 + \frac{240}{y} - 16 = 60\] \[y^2 + \frac{240}{y} - 76 = 0\] Multiplying both sides by y, we get a cubic expression: \[y^3 + 0y^2 - 76y + 240 = 0\] Here we just have to figure out the values of y that make this equation true. I used Vieta's Formulas to get a possible list, but you could also use the rational root theorem and synthetic division to find these. We call the three values of y that solve this equation: $y_{1},y_{2},y_{3}$ Using Vieta's Formulas, you get these three expressions: \[y_{1} + y_{2} + y_{3} = 0\] \[y_{1} * y_{2} * y_{3} = -240\] \[(y_{1} * y_{2}) + (y_{2} * y_{3}) + (y_{1} * y_{3}) = -76\]
In addition, we know that $y \vert 60$ , because of our expression for x. Since the three values of y multiply to a negative number but also add to 0, we know that one value is negative and the other two are positive, and that the absolute value of the negative value is greater than both of the positive values. List of possible values for y are $\{-60,-30,-20,-15,-12,-10,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,10,12,15,20,30,60\}$ From a list of these values, the only values that work are $y_1 = -10, y_2 = 6, y_3 = 4$ because \[-10 + 6 + 4 = 0\] \[-10 * 6 * 4 = -240\] \[(-10 * 6) + (-10 * 4) + (6 * 4) = -60 - 40 + 24 = -76\]
Plugging in these values for y into our expression for x, we get: \[x = \frac{60}{-10} - 4 = -10\] \[x = \frac{60}{6} - 4 = 6\] \[x = \frac{60}{4} - 4 = 11\]
So, now we have accounted for both cases, and we have 4 values of x = $\{-10,4,6,11\}$ Squaring all these terms we get: 100 + 16 + 36 + 121 = 273, so our answer is $\boxed{\textbf{(273)}}$
~Cardtricks

## Solution 4 (even more Vieta's)
Since all three equations are in the form $\frac{K}{a} + 4a = 60$ where $K = xyz$ , we can rearrange this to see that $x$ , $y$ , and $z$ all satisfy
\[ 4a^2 - 60a + K = 0. \]
Let this quadratic have roots $a_1$ and $a_2$ . Then, there are two cases to consider: two of $x$ , $y$ , $z$ are equal to $a_1$ and the third is equal to $a_2$ , or all of $x$ , $y$ , $z$ are equal to $a_1$ .
Case 1: WLOG let $x = y = a_1$ and $z = a_2$ .
Then by Vieta's,
\[x + z = 15 \hspace{1cm} (1)\] \[xz = \frac{x^2z}{4} \hspace{1cm} (2)\]
which gives $x = y = 4$ and $z = 11$ . But we can swap $x$ , $y$ , and $z$ however we like, so this also gives $x = 11$ as a solution. In total, this case yields $x = 4$ and $x = 11$ as possible values of $x$ .
Case 2: WLOG let $x = y = z = a_1$ .
Again, by Vieta's,
\[x + a_2 = 15 \hspace{1cm} (1)\] \[xa_2 = \frac{x^3}{4} \hspace{1cm} (2)\]
We can use $(2)$ to isolate $a_2$ in terms of $x$ , then plug that into $(1)$ to get that $x^2 + 4x - 60 = 0$ . This yields $x = -10$ and $x = 6$ as additional possible values of $x$ .
In all, $x$ can be any of $\{ 4, 11, -10, 6 \}$ , so the requested answer is $4^2 + 11^2 + (-10)^2 + 6^2 = \boxed{273}.$

## Solution 5
We index these equations as (1), (2), and (3) respectively (same as solution 2). There are two possible cases:
Case 1: $x = \pm 4$
In this case, we simply plug in $x = 4$ and $x = -4$ . We note that $x=4$ is a valid case.
Case 2: $x \neq \pm 4$
In this case, using equation (3), we get $y = 15 - \frac{xz}{4}$ . Plugging that into equation (1), we get $z = \frac{240-60x}{16-x^2}$ . Plugging that expression back into the original expression for $y$ we obtain $y = 15 - \frac{60x-15x^2}{16-x^2}$ . Now we plug these two expressions into equation (2): \[\left(15 - \frac{60x-15x^2}{16-x^2}\right)\left(\frac{240-60x}{16-x^2}\right) = 60-4x\] multiplying both sides by $(16-x^2)$ and factoring, we get: \[\left(15(4-x)(4+x)-60x+15x^2\right)\left(\frac{60(4-x)}{(4+x)(4-x)}\right) = 4(15 - x)(4 + x)(4 - x)\] which simplifies to: \[x^3 - 7x^2 - 104x + 660 = 0\] we note that $x = 6$ is a root. Factoring, we get the other roots, -10 and 11.
Our desired answer is the sum of the square of all these roots: \[4^2 + 6^2 + (-10)^2 + 11^2 = \boxed{273}\]
~Chupdogs

## Video Solution by The Power of Logic(#3 and #4)
https://youtu.be/dS9K1o4gCA0
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .