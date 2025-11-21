# 2021 Fall AMC 10A Problem 14

## Problem

How many ordered pairs $(x,y)$ of real numbers satisfy the following system of equations? \begin{align*} x^2+3y&=9 \\ (|x|+|y|-4)^2 &= 1 \end{align*} $\textbf{(A) } 1 \qquad\textbf{(B) } 2 \qquad\textbf{(C) } 3 \qquad\textbf{(D) } 5 \qquad\textbf{(E) } 7$

## Solution 1 (Graphing)
The second equation is $(|x|+|y| - 4)^2 = 1$ . We know that the graph of $|x| + |y|$ is a very simple diamond shape, so let's see if we can reduce this equation to that form: \[(|x|+|y| - 4)^2 = 1 \implies |x|+|y| - 4 = \pm 1 \implies |x|+|y| = \{3,5\}.\] We now have two separate graphs for this equation and one graph for the first equation, so let's put it on the coordinate plane: [asy] Label f; f.p=fontsize(6); xaxis(-8,8,Ticks(f, 1.0,0.5)); yaxis(-8,8,Ticks(f, 1.0,0.5)); real f(real x) { return 3-x; } draw(graph(f,0,3)); real f(real x) { return 3+x; } draw(graph(f,0,-3)); real f(real x) { return x-3; } draw(graph(f,0,3)); real f(real x) { return -x-3; } draw(graph(f,0,-3)); real f(real x) { return 5-x; } draw(graph(f,0,5)); real f(real x) { return 5+x; } draw(graph(f,0,-5)); real f(real x) { return x-5; } draw(graph(f,0,5)); real f(real x) { return -x-5; } draw(graph(f,0,-5)); real f(real x) { return 3-x; } draw(graph(f,0,3)); real f(real x) { return 3+x; } draw(graph(f,0,-3)); real f(real x) { return x-3; } draw(graph(f,0,3)); real f(real x) { return (-x^2)/3+3; } draw(graph(f,-5,5)); [/asy] We see from the graph that there are $5$ intersections, so the answer is $\boxed{\textbf{(D) } 5}$ .
~KingRavi

## Solution 2 (Casework)
From the first equation, we can express $y$ in terms of $x$ :
$3y = 9 - x^2$ which is $y = (9 - x^2)/3$
The second equation can be rewritten as:
$|x| + |y| - 4 = \pm 1$ .
This gives us two scenarios to examine:
1. $|x| + |y| = 5$
2. $|x| + |y| = 3$
Case 1:
Substituting $y$ ,
$|x| + |(9 - x^2)/3| = 5$ .
First, consider the case when $9 - x^2 \geq 0$ . Then,
$|y| = (9 - x^2)/3$ which is $|x| + (9 - x^2)/3 = 5$ .
Multiplying by 3, we get
$3|x| + 9 - x^2 = 15$ which is $3|x| - x^2 = 6$ which is $x^2 - 3|x| + 6 = 0$ .
However, the discriminant of this quadratic is $(-3)^2 - 4 * 1 * 6 = 9 - 24 = -15$ , which indicates there are no real solutions in this scenario.
Now, we can consider when $9 - x^2 < 0$
$|y| = -(9 - x^2)/3 = (x^2 - 9)/3$ which is $|x| + (x^2 - 9)/3 = 5$ .
Multiplying by 3, we get
$3|x| + x^2 - 9 = 15$ which is $x^2 + 3|x| - 24 = 0$ .
Now, let $u = |x|$ , which gives $u^2 + 3u - 24 = 0$ . When we calculate the discriminant, we get $3^2 - 4 * 1 * (-24) = 9 + 96 = 105$ . So, the roots are $u = (-3 \pm \sqrt(105))/2$ .
Both roots give positive values for $u$ , resulting in two values of $x$ for each root (one positive and one negative).
Case 2: \( |x| + |y| = 3 \)
Substituting $y$ :
$|x| + |(9 - x^2)/3| = 3$ .
If $9 - x^2 \geq 0$ , then $|y| = (9 - x^2)/3$ which is | $x| + (9 - x^2)/3 = 3$ .
Multiplying by 3, we get
$3|x| + 9 - x^2 = 9$ which is $3|x| = x^2$ which is $x^2 - 3|x| = 0$ .
Thus, $|x|(|x| - 3) = 0$ , leading to $x = 0$ or $x = 3$ (both giving corresponding $y$ values).
If $9 - x^2 < 0$ , then $|y| = (x^2 - 9)/3$ which is $|x| + (x^2 - 9)/3 = 3$ .
When we multiply through, we get $3|x| + x^2 - 9 = 9$ which is $x^2 + 3|x| - 18 = 0$ .
The discriminant here is $3^2 - 4 * 1 * (-18) = 9 + 72 = 81$ .
This gives two more real roots for $u = |x|$ .
Now,
- Case 1 contributes 2 solutions
- Case 2 contributes 1 solution from $x = 0$ and $x = 3$ , and 2 solutions from the second sub-case
Thus, counting all solutions gives us a total of 5 unique ordered pairs, and the answer is $\boxed{\textbf{(D) } 5}$ .
~goofytaipan

## Video Solution
https://youtu.be/yASY-XL9vtI
~Education, the Study of Everything

## Video Solution
https://youtu.be/zq3UPu4nwsE?t=974

## Video Solution by WhyMath
https://youtu.be/5SVmxNrZUbY
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .