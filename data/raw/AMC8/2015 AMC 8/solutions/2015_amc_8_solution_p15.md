# 2015 AMC 8 Problem 15

## Problem

At Euler Middle School, $198$ students voted on two issues in a school referendum with the following results: $149$ voted in favor of the first issue and $119$ voted in favor of the second issue. If there were exactly $29$ students who voted against both issues, how many students voted in favor of both issues?

$\textbf{(A) }49\qquad\textbf{(B) }70\qquad\textbf{(C) }79\qquad\textbf{(D) }99\qquad \textbf{(E) }149$

## Solution 1
Let:
We are given:
\[198 - 29 = 169\]
By the principle of inclusion and exclusion: \[A \cup B = A + B - A \cap B\] Substitute known values: \[169 = 149 + 119 - A \cap B\] \[169 = 268 - A \cap B\] \[A \cap B = 268 - 169 = \boxed{\textbf{(D) }99}\]

## Solution 2
We can see that this is a Venn Diagram Problem.
First, we analyze the information given. There are $198$ students. Let's use A as the first issue and B as the second issue.
$149$ students were for A, and $119$ students were for B. There were also $29$ students against both A and B.
Solving this without a Venn Diagram, we subtract $29$ away from the total, $198$ . Out of the remaining $169$ , we have $149$ people for A and
$119$ people for B. We add this up to get $268$ . Since that is more than what we need, we subtract $169$ from $268$ to get
$\boxed{\textbf{(D)}~99}$ .
[asy] defaultpen(linewidth(0.7)); draw(Circle(origin, 5)); draw(Circle((5,0), 5)); label("$A$", (0,5), N); label("$B$", (5,5), N); label("$99$", (2.5, -0.5), N); label("$50$", (-2.5,-0.5), N); label("$20$", (7.5, -0.5), N); [/asy]
Note: One could use the Principle of Inclusion-Exclusion in a similar way to achieve the same result.
~ cxsmi (note)

## Solution 3
There are $198-149=49$ students who voted against the first issue. Out of these, $49-29=20$ voted for the second issue. We also find that $50$ students voted against the second issue but in favor of the first in a similar way. This means that $149-50=119-20=\boxed{\textbf{(D)}~99}$ students voted in favor of both issues.

## Video Solutions

## Video Solution by OmegaLearn
www.youtube.com/watch?v=OOdK-nOzaII&t=829s
~ pi_is_3.14

## Video Solution (HOW TO THINK CRITICALLY!!!)
https://youtu.be/skOXiXCZVK0
~ Education, the Study of Everything

## Video Solution 3
https://youtu.be/OOdK-nOzaII?t=827

## Video Solution 4
https://youtu.be/ATpixMaV-z4
~ savannahsolver
### See Also