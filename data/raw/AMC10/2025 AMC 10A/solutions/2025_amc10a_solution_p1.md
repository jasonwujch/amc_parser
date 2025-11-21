# 2025 AMC 10A Problem 1

## Problem

Andy and Betsy both live in Mathville. Andy leaves Mathville on his bicycle at $1{:}30$ , traveling due north at a steady $8$ miles per hour. Betsy leaves on her bicycle from the same point at $2{:}30$ , traveling due east at a steady $12$ miles per hour. At what time will they be exactly the same distance from their common starting point?

$\textbf{(A) } 3{:}30 \qquad \textbf{(B) } 3{:}45 \qquad \textbf{(C) } 4{:}00 \qquad \textbf{(D) } 4{:}15 \qquad \textbf{(E) } 4{:}30$

### This page has some problems with rendering; thanks to everyone trying to fix it

## Solution 1
We can see that at $2{:}30$ , Andy will be $8$ miles ahead. For every hour that they both travel, Betsy will gain $4$ miles on Andy. Therefore, it will take $2$ more hours for Betsy to catch up, and they will be at the same point at $\boxed{\textbf{(E) } 4{:}30}$ .
~vinceS ~minor LaTeX edits by zoyashaikh

## Solution 2
Let $h$ be the number of hours after Andy starts. Andy travels $8h$ miles, and Betsy has traveled $12(h-1)$ miles since she started one hour later. Setting them equal:
$8h = 12(h-1)$ $\Rightarrow 8h = 12h - 12$ $\Rightarrow 4h = 12$ $\Rightarrow h = 3$
Since Andy started at $1{:}30$ , the catch-up time is $4{:}30$ . Answer: $\textbf{(E)}$ .
Alternatively, from Betsy's perspective: $8(h+1) = 12h$ $\Rightarrow 8h + 8 = 12h$ $\Rightarrow h = 2$ Same result: $\textbf{(E) } 4{:}30$ .
~kapiltheangel (2A) ~mithu542 (2B)

## Solution 3
Try the answer choices:
At $3{:}30$ : Andy $=16$ , Betsy $=12$ At $3{:}45$ : Andy $=18$ , Betsy $=15$ At $4{:}00$ : Andy $=20$ , Betsy $=18$ At $4{:}15$ : Andy $=22$ , Betsy $=21$ At $4{:}30$ : Andy $=24$ , Betsy $=24$
Thus the correct answer is $\boxed{\textbf{(E) } 4{:}30}$ .
~vgarg

## Solution 4
Since $\text{lcm}(8,12)=24$ , the time for Andy to reach 24 miles is $24/8 = 3$ hours.
$1{:}30 + 3{:}00 = \boxed{\textbf{(E) } 4{:}30}$ .
~Boywithnuke ~minor edits by ChickensEatGrass ~minor edits by RISHADA

## Solution 5
Andy goes $8x$ miles, Betsy goes $12(x-1)$ miles. Set equal:
$8x = 12(x-1)$ $\Rightarrow x = 3$
Thus the answer is $\textbf{(E) } 4{:}30$ .
~minor LaTeX edits by zoyashaikh ~minor $\LaTeX$ edits by i_am_not_suk_at_math

## Solution 6
Using constant rates:
\[\begin{array}{c|c|c} \text{Time} & \text{Andy} & \text{Betsy} \\ \hline 1{:}30 & 0 & 0 \\ 2{:}30 & 8 & 0 \\ 3{:}30 & 16 & 12 \\ 4{:}30 & 24 & 24 \end{array}\]
Thus the answer is $\textbf{(E) } 4{:}30$ .
~i_am_not_suk_at_math ~minor LaTeX edits by vinceS ~minor edits by A-V-N-I

## Solution 7 (Calculus Overkill)
Let $D_A(t) = 8t$ , $D_B(t) = 12(t-1)$ for $t \ge 1$ .
Difference: $F(t) = 12(t-1) - 8t = 4t - 12$ .
Set $F(t)=0$ : $4t - 12 = 0$ $t = 3$ hours.
$1{:}30 + 3 = 4{:}30$ .
-apex304

## Solution 8 (Easy to understand, fast)
Let \( t \) denote time in hours measured from 1:30 PM:
\( t := \text{hours after } 1:30 \text{ PM} \).
Thus \( t = 0 \) at 1:30 PM, \( t = 1 \) at 2:30 PM, and the physically relevant domain for both riders having left is \( t \geq 1 \).
Velocity/position (vectorized). Choose orthonormal basis \( \{ i, j \} \) with \( i \) east and \( j \) north. Define piecewise position vectors \( r_A(t), r_B(t) \in \mathbb{R}^2 \) (for all \( t \geq 0 \)):
\( r_A(t) = 8t \, j = (0, 8t) \), \[r_B(t) = \begin{cases} (0, 0), & 0 \leq t < 1, \\ 12(t - 1) \, i, & t \geq 1, \end{cases} = (12 \max\{t - 1, 0\}, 0).\]
Define scalar distance functions (Euclidean norm / 2-norm):
\( D_A(t) := \| r_A(t) \|_2 = \sqrt{0^2 + (8t)^2} = 8t \), \( D_B(t) := \| r_B(t) \|_2 = 12 \max\{t - 1, 0\} \).
We seek \( t \) with \( D_A(t) = D_B(t) \) and \( t \geq 1 \). For \( t \geq 1 \) the equality reduces to the linear equation
\( 8t = 12(t - 1) \).
Bring like terms together:
\( 8t = 12t - 12 \implies 12 = 12t - 8t \).
Compute the difference \( 12t - 8t \) digit-by-digit: \( 12t - 8t = (12 - 8)t = 4t \). So
\( 12 = 4t \).
Divide \( 12 \) by \( 4 \) carefully: \( 12 \div 4 = 3 \). Hence
\( t = 3 \).
~N0lan

## Video Solution (Fast and Easy)
https://youtu.be/fjpeOuUMOyc?si=ROuzlwgz7UByUx_9
~ Pi Academy

## Video Solution by Power Solve
https://www.youtube.com/watch?v=QBn439idcPo

## Chinese Video Solution
https://www.bilibili.com/video/BV1852uBoE8K/
~metrixgo

## Video Solution (Intuitive, Quick Explanation!)

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution by Daily Dose of Math 🔥🔥🔥
~Thesmartgreekmathdude

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video solution
https://youtu.be/l1RY_C20Q2M

## Easy Solution
https://www.youtube.com/watch?v=kHwBHvvvTbY
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .