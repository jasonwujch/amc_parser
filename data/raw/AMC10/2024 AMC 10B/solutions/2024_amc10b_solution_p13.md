# 2024 AMC 10B Problem 13

## Problem

Positive integers $x$ and $y$ satisfy the equation $\sqrt{x} + \sqrt{y} = \sqrt{1183}$ . What is the minimum possible value of $x+y$ ?

$\textbf{(A) } 585 \qquad\textbf{(B) } 595 \qquad\textbf{(C) } 623 \qquad\textbf{(D) } 700 \qquad\textbf{(E) } 791$

## Solution 1
Note that $\sqrt{1183}=13\sqrt7$ . Since $x$ and $y$ are positive integers, and $\sqrt{x}+\sqrt{y}=\sqrt{1183}$ we can represent each value of $\sqrt{x}$ and $\sqrt{y}$ as the product of a positive integer and $\sqrt7$ . Let's say that $\sqrt{x}=m\sqrt7$ and $\sqrt{y}=n\sqrt7$ , where $m$ and $n$ are positive integers. This implies that \[x+y=(\sqrt{x})^2+(\sqrt{y})^2=7m^2+7n^2=7(m^2+n^2)\] and that $m+n=13$ . WLOG, assume that ${m}\geq{n}$ . It is not hard to see that $x+y$ reaches its minimum when $m^2+n^2$ reaches its minimum. We now apply algebraic manipulation to get that \[m^2+n^2=(m+n)^2-2mn\] Since $m+n$ is determined, we now want $mn$ to reach its maximum. Since $m$ and $n$ are positive integers, we can use the AM-GM inequality to get that: $\frac{m+n}{2}\geq{\sqrt{mn}}$ . When $mn$ reaches its maximum, $\frac{m+n}{2}={\sqrt{mn}}$ . This implies that $m=n=\frac{13}{2}$ . However, this is not possible since $m$ and $n$ and integers. Under this constraint, we can see that $mn$ reaches its maximum when $m=7$ and $n=6$ . Therefore, the minimum possible value of $x+y$ is $7(m^2+n^2)=7(7^2+6^2)=\boxed{\textbf{(B)}595}$
~ Bloggish
A similar method is to take $y=1183-26\sqrt{7x}-x^2$ , then noting $x=7a^2$ and bashing to find the value of a where x is closest to y.
~meihk_neiht

## Solution 2 (Guessing & Answer Choices)
Set $x=y$ , giving the minimum possible values. The given equation becomes \[\sqrt{x}=\sqrt{y}=\dfrac{\sqrt{1183}}{2}\implies x=y=\dfrac{1183}{4}.\] This means that \[x+y=\dfrac{1183}{2}=591.5.\] Since this is closest to answer choice $\text{(B)}$ , the answer is $\boxed{\textbf{(B) }595}$ ~Neoronean ~Tacos_are_yummy_1 (latex)
Note: If using a solution similar to this one it is recommended to still find valid x and y that add to 595.
~meikh neiht

## Solution 3 (quick, no guessing but still answer choices)
Square both sides of the equation to get $2\cdot \sqrt{xy} + (x + y) = 1183.$ We can plug in possible values for $x + y$ based on the answer choices. If we do $585,$ we get $\sqrt{xy} = 299 \implies xy = 299^2.$ So $y = \frac{299^2}{x}.$ Then we have $x^2 + 299^2 = 585x,$ which has no real solutions for $x$ since the discriminant is negative. Following the same process for $595$ we obtain the equation $x^2 + 294^2 = 595x,$ which can be factored as $(x - 252)(x - 343) = 0.$ So the answer must be $\boxed{\textbf{(B) }595}$ .
~ grogg007

## Solution 4 (Calculus)
Since $\sqrt{x}+\sqrt{y}=\sqrt{1183}$ , we can express $y$ in terms of $x$ : $y = x+1183-2\sqrt{1183x}$ . $x+y = 2x+1183-2\sqrt{1183x}$ . Taking the derivative of this, we get $2-2 \cdot \frac{1}{2\sqrt{1183x}} \cdot 1183$ . We find the critical points by setting this expression to equate $0$ . Simplifying, we get $2 = \frac{1183}{\sqrt{1183x}}$ , and then we get $4 \cdot 1183x = 1183^2$ . Dividing by $1183$ , we get $4x=1183$ , so a critical point is $x=\frac{1183}{4}$ . Now, we take the second derivative, we get $\frac{13\sqrt{7x}}{2x^2}$ . When $x=\frac{1183}{4}$ , the second derivative is positive, meaning the minimum value is obtained at $x=\frac{1183}{4}$ . This value is $295.75$ . However, the problem asks for positive integers $x$ and $y$ . We want $x$ to be as close to $295.75$ as possible. We also want $y$ to be an integer, so $x+1183-2\sqrt{1183x}$ should be an integer. Notice how since $x$ is an integer, we just want $\sqrt{1183x}$ to be an integer. Prime factorizing $1183$ , we get $1183=7 \cdot 13^2$ . Therefore, $x$ must contain an odd amount of $7$ 's and an even amount of any other prime factor. We quickly find that $2^2 \cdot 3^2 \cdot 7 = 252$ is the optimal solution for $x$ , and plugging in, we get $y=252 + 1183 - 2 \cdot 2 \cdot 3 \cdot 7 \cdot 13 = 343$ . We find $x+y=595$ , so the answer is choice $\boxed{\text{(B) 595}}$ . ~ lovelearning999
Note: It might not be immediately clear why $x=252$ is the optimal solution. The following explains why $x=252$ is optimal.
$x$ must have an odd amount of $7$ 's and an even amount of any other prime factor. This means that $x$ can be expressed as $7^n \cdot a$ where $a$ is a perfect square. We can simplify this to $7 \cdot 7^{n-1} \cdot a = 7b$ , where $b$ is a perfect square, since $n-1$ is even. This means that $7b$ is as close to $295.75$ as possible. This means that $b \approx \frac{295.75}{7}$ . $\frac{295.75}{7}$ is approximately $42$ , so $b \approx 42$ . Since $b$ is a perfect square, we have two candidates for $b$ : $36$ and $49$ . If $b=36$ , $x=252$ , and if $b=49$ , $x=343$ . To find the optimal value for $x$ , pick the value closest to $295.75$ , and we find that $\left |295.75-252 \right | < \left |295.75 - 343 \right|$ , so $x=252$ is optimal. From now, proceed in the same way as the original solution.
~ lovelearning999

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/YqKmvSR1Ckk?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://youtu.be/7ZKvxU6c75g?si=KvM1x612u6fig_Xc

## Video Solution 3 by TheBeautyofMath
https://youtu.be/dfF39udgqc8?t=724 in Rapid Fire
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .