# 2011 AMC 10B Problem 15

## Problem

Let $@$ denote the "averaged with" operation: $a @ b = \frac{a+b}{2}$ . Which of the following distributive laws hold for all numbers $x, y,$ and $z$ ? \[\text{I. x @ (y + z) = (x @ y) + (x @ z)}\] \[\text{II. x + (y @ z) = (x + y) @ (x + z)}\] \[\text{III. x @ (y @ z) = (x @ y) @ (x @ z)}\]

$\textbf{(A)}\ \text{I only} \qquad\textbf{(B)}\ \text{II only} \qquad\textbf{(C)}\ \text{III only} \qquad\textbf{(D)}\ \text{I and III only} \qquad\textbf{(E)}\ \text{II and III only}$

## Solution
Simplify each operation and see which ones hold true.
\begin{align*} \text{I.} \qquad x @ (y + z) &= (x @ y) + (x @ z)\\ \frac{x+y+z}{2} &= \frac{x+y}{2} + \frac{x+z}{2}\\ \frac{x+y+z}{2} &\not= \frac{2x+y+z}{2} \end{align*}
\begin{align*} \text{II.} \qquad x + (y @ z) &= (x + y) @ (x + z)\\ x+ \frac{y+z}{2} &= \frac{2x+y+z}{2}\\ \frac{2x+y+z}{2} &= \frac{2x+y+z}{2} \end{align*}
\begin{align*} \text{III.} \qquad x @ (y @ z) &= (x @ y) @ (x @ z)\\ x @ \frac{y+z}{2} &= \frac{x+y}{2} @ \frac{x+z}{2}\\ \frac{2x+y+z}{4} &= \frac{2x+y+z}{4} \end{align*}
$\boxed{\textbf{(E)} \text{II and III only}}$

## Solution 2
Alternatively, substitute arbitrary values for $x$ , $y$ , and $z$ where $x\neq y\neq z$ . For example, $x=1$ , $y=2$ , and $z=3$ give that only II and III work. $\boxed{\textbf{(E)} \text{II and III only}}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .