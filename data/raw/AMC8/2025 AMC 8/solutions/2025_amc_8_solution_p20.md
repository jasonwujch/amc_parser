# 2025 AMC 8 Problem 20

## Problem

Sarika, Dev, and Rajiv are sharing a large block of cheese. They take turns cutting off half of what remains and eating it: first Sarika eats half of the cheese, then Dev eats half of the remaining half, then Rajiv eats half of what remains, then back to Sarika, and so on. They stop when the cheese is too small to see. About what fraction of the original block of cheese does Sarika eat in total?

$\textbf{(A)}\ \frac{4}{7} \qquad \textbf{(B)}\ \frac{3}{5} \qquad \textbf{(C)}\ \frac{2}{3} \qquad \textbf{(D)}\ \frac{3}{4} \qquad \textbf{(E)}\ \frac{7}{8}$

## Solution 1
Let the total amount of cheese be $1$ . We will track the amount of cheese Sarika eats throughout the process.
First Round: Sarika eats half of the total cheese, so she eats: \[\frac{1}{2}.\] Second Round: Dev eats half of what remains after Sarika's turn, which is: \[\frac{1}{4}.\] Third Round: Rajiv eats half of the remaining cheese after Dev’s turn, which is: \[\frac{1}{8}.\]
At the end of the first round, the total cheese eaten is: \[\frac{1}{2} + \frac{1}{4} + \frac{1}{8} = \frac{7}{8}.\]
We observe that Sarika’s consumption follows a geometric sequence . In the first round, she eats $\frac{1}{2}$ , and in subsequent rounds, she eats half of what remains from the previous round. This gives the following series for Sarika’s total consumption:
\[\frac{1}{2} + \frac{1}{16} + \frac{1}{128} + \cdots\]
This is a geometric series with first term $\frac{1}{2}$ and common ratio $\frac{1}{8}$ . The sum $S$ of this infinite geometric series is given by the formula:
\[S = \frac{a}{1 - r},\] where $a$ is the first term and $r$ is the common ratio. Substituting $a = \frac{1}{2}$ and $r = \frac{1}{8}$ :
\[S = \frac{\frac{1}{2}}{1 - \frac{1}{8}} = \frac{\frac{1}{2}}{\frac{7}{8}} = \frac{1}{2} \times \frac{8}{7} = \frac{4}{7}.\]
Thus, Sarika eats $\frac{4}{7}$ of the original block of cheese. The correct answer is: \[\boxed{\textbf{(A) } \frac{4}{7}}.\]
$\square$
~ aoum

## Solution 2 (Estimation)
Sarika eats $1/2$ of the original cheese, and then because the others eat $1/4$ and $1/8$ , she eats $1/16$ next, and then $1/128$ , and then so on. Since the values later are going to be too small to make a huge difference, we can use these $3$ values. She ate $(64 + 8 + 1)/128 = 73/128$ . We can replace the $73$ with a $72$ for now, so $72/128 = 9/16$ , which simplifies to around $56.25$ . Since there is a little bit more of the cheese to be accounted for, the amount that she eats will be around $\boxed{\textbf{(A) }\frac{4}{7}}$ .
~Sigmacuber

## Solution 3 Speed
Her first $2$ bites will be $\frac{1}{2}$ and $\frac{1}{16}$ . Everything else won't matter, so the answer will be closest to $\frac{9}{16}$ , $\frac{4}{7}$ .
~Moonwatcher22

## Solution 4 (Basically Video Solution)
Let Sarika eat a total of $x$ units of cheese. We can then see that Dev will eat a total of $\frac{x}{2}$ units and Rajiv will eat $\frac{x}{4}$ units. Our desired answer is $\frac{x}{x + \frac{x}{2} + \frac{x}{4}}$ , or $\boxed{\textbf{(A) }\frac{4}{7}}$ .
~Irfans123

## Video Solution by Pi Academy
https://youtu.be/Iv_a3Rz725w?si=E0SI_h1XT8msWgkK

## Video Solution
Key Idea: Let $x$ be the fraction eaten by Sarika. Then Dev eats $\frac{x}{2}$ and Rajiv eats $\frac{x}{4}$ . Hence $x + \frac{x}{2} + \frac{x}{4} = 1$ so solving for $x$ we get \[x = \boxed{\textbf{(A) }\frac{4}{7}}\] .
Video Link: https://www.youtube.com/watch?v=VUR5VYabbrc

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=E-EnGyXALPVaXvPy&t=2698 ~hsnacademy

## Video Solution by Thinking Feet
https://youtu.be/PKMpTS6b988

## A Concise Video Solution in 56 Seconds by Dr. Xue's Math School
https://youtu.be/nmoYIQKzjVE
Work smarter, work more efficiently, not just harder.
### See Also