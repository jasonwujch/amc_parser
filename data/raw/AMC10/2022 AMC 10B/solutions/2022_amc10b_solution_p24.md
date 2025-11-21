# 2022 AMC 10B Problem 24

## Problem

Consider functions $f$ that satisfy \[|f(x)-f(y)|\leq \frac{1}{2}|x-y|\] for all real numbers $x$ and $y$ . Of all such functions that also satisfy the equation $f(300) = f(900)$ , what is the greatest possible value of \[f(f(800))-f(f(400))?\] $\textbf{(A)}\ 25 \qquad\textbf{(B)}\ 50 \qquad\textbf{(C)}\ 100 \qquad\textbf{(D)}\ 150 \qquad\textbf{(E)}\ 200$

## Solution 1 (Absolute Values and Inequalities)
We have \begin{align*} |f(f(800))-f(f(400))| &\leq \frac12|f(800)-f(400)| &&(\bigstar) \\ &\leq \frac12\left|\frac12|800-400|\right| \\ &= 100, \end{align*} from which we eliminate answer choices $\textbf{(D)}$ and $\textbf{(E)}.$
Note that \begin{alignat*}{8} |f(800)-f(300)| &\leq \frac12|800-300| &&= 250, \\ |f(800)-f(900)| &\leq \frac12|800-900| &&= 50, \\ |f(400)-f(300)| &\leq \frac12|400-300| &&= 50, \\ |f(400)-f(900)| &\leq \frac12|400-900| &&= 250. \\ \end{alignat*} Let $a=f(300)=f(900).$ Together, it follows that \begin{align*} |f(800)-a|&\leq 50, \\ |f(400)-a|&\leq 50. \\ \end{align*} We rewrite $(\bigstar)$ as \begin{align*} |f(f(800))-f(f(400))| &\leq \frac12|f(800)-f(400)| \\ &= \frac12|(f(800)-a)-(f(400)-a)| \\ &\leq \frac12|50-(-50)| \\ &=\boxed{\textbf{(B)}\ 50}. \end{align*} ~MRENTHUSIASM

## Solution 2 (Lipschitz Condition)
Denote $f(900)-f(600) = a$ . Because $f(300) = f(900)$ , $f(300) - f(600) = a$ .
Following from the Lipschitz condition given in this problem, $|a| \leq 150$ and \[ f(800) - f(600) \leq \min \left\{ a + 50 , 100 \right\} \] and \[ f(400) - f(600) \geq \max \left\{ a - 50 , -100 \right\} . \] Thus, \begin{align*} f(800) - f(400) & \leq \min \left\{ a + 50 , 100 \right\} - \max \left\{ a - 50 , -100 \right\} \\ & = 100 + \min \left\{ a, 50 \right\} - \max \left\{ a , - 50 \right\} \\ & = 100 + \left\{ \begin{array}{ll} a + 50 & \mbox{ if } a \leq -50 \\ 0 & \mbox{ if } -50 < a < 50 \\ -a + 50 & \mbox{ if } a \geq 50 \end{array} \right. . \end{align*} Thus, $f(800) - f(400)$ is maximized at $a = 0$ , $f(800)-f(600) = 50$ , $f(400)-f(600)=-50$ , with the maximal value 100.
By symmetry, following from an analogous argument, we can show that $f(800) - f(400)$ is minimized at $a = 0$ , $f(800)-f(600) = -50$ , $f(400)-f(600)=50$ , with the minimal value $-100$ .
Following from the Lipschitz condition, \begin{align*} f(f(800)) - f(f(400)) & \leq \frac{1}{2} \left| f(800) - f(400) \right| \\ & \leq 50 . \end{align*} We have already construct instances in which the second inequality above is augmented to an equality.
Now, we construct an instance in which the first inequality above is augmented to an equality.
Consider the following piecewise-linear function: \[ f(x) = \left\{ \begin{array}{ll} \frac{1}{2} \left( x - 300 \right) & \mbox{ if } x \leq 300 \\ -\frac{1}{2} \left( x - 300 \right) & \mbox{ if } 300 < x \leq 400 \\ \frac{1}{2} \left( x - 600 \right) & \mbox{ if } 400 < x \leq 800 \\ -\frac{1}{2} \left( x - 900 \right) & \mbox{ if } x > 800 \end{array} \right.. \] Therefore, the maximum value of $f(f(800)) - f(f(400))$ is $\boxed{\textbf{(B)}\ 50}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
~Viliciri (LaTeX edits)

## Solution 3 (Slopes)
Divide both sides by $|x - y|$ to get $\frac{|f(x) - f(y)|}{|x - y|} \leq \frac{1}{2}$ . This means that when we take any two points on $f$ , the absolute value of the slope between the two points is at most $\frac{1}{2}$ .
Let $f(300) = f(900) = c$ , and since we want to find the maximum value of $|f(800) - f(400)|$ , we can take the most extreme case and draw a line with slope $-\frac{1}{2}$ down from $f(300)$ to $f(400)$ and a line with slope $\frac{1}{2}$ up from $f(800)$ to $f(900)$ . Then $f(400) = c - 50$ and $f(800) = c + 50$ , so $|f(800) - f(400)| = |c + 50 - (c - 50)| = 100$ , and this is attainable because the slope of the line connecting $f(400)$ and $f(800)$ still has absolute value less than $\frac{1}{2}$ .
Therefore, $|f(f(800)) - f(f(400))| \leq \frac{1}{2}|f(800) - f(400)| = \frac{1}{2}(100) = \boxed{\textbf{(B)}\ 50}$ .

## Solution 4 (Translation)
Consider $g(x) = f(x)-f(300)$ . Then $g(x)$ satisfies all the conditions and $g(300) = g(900) = 0$ . We would want $g(400)$ and $g(800)$ as distant from each other as possible. So assign $g(400) = -50$ and $g(800) = 50$ , the possible lower and upper bounds respectively. It follows that one can obtain the upper bound for $|g(g(800)) - g(g(400))| = |g(50) - g(-50 )| \leq \frac{1}{2}(100) = \boxed{\textbf{(B)}\ 50}$ as the answer.

## Video Solution
https://youtu.be/2Li0IYOQCFQ
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by OmegaLearn Using Algebraic Manipulation
https://youtu.be/-yzpw6b3_KA
~ pi_is_3.14

## Video Solution by Interstigation
https://youtu.be/n0ZTR6edOBs
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .