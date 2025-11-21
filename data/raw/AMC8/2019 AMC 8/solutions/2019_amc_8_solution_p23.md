# 2019 AMC 8 Problem 23

## Problem

After Euclid High School's last basketball game, it was determined that $\frac{1}{4}$ of the team's points were scored by Alexa and $\frac{2}{7}$ were scored by Brittany. Chelsea scored $15$ points. None of the other $7$ team members scored more than $2$ points. What was the total number of points scored by the other $7$ team members?

$\textbf{(A) }10\qquad\textbf{(B) }11\qquad\textbf{(C) }12\qquad\textbf{(D) }13\qquad\textbf{(E) }14$

## Solution 1
Given the information above, we start with the equation $\frac{t}{4}+\frac{2t}{7} + 15 + x = t$ , where $t$ is the total number of points scored and $x\le 14$ is the number of points scored by the remaining 7 team members, we can simplify to obtain the Diophantine equation $x+15 = \frac{13}{28}t$ , or $28x+28\cdot 15=13t$ . Since $t$ is necessarily divisible by 28, let $t=28u$ where $u \ge 0$ and divide by 28 to obtain $x + 15 = 13u$ . Then, it is easy to see $u=2$ ( $t=56$ ) is the only candidate remaining, giving $x=\boxed{\textbf{(B)} 11}$ .
-scrabbler94
~Minor Edits by Wrenmath

## Solution 2
We first start by setting the total number of points as $28$ , since $\text{LCM}(4,7) = 28$ . However, we see that this does not work since we surpass the number of points just with the information given ( $28\cdot\frac{1}{4}+28\cdot\frac{2}{7} + 15 = 30$ $(> 28)$ ). Next, we can see that the total number of points scored is $56$ as, if it is more than or equal to $84$ , at least one of the others will score more than 2 points. With this, we have that Alexa, Brittany, and Chelsea score: $56\cdot\frac{1}{4}+56\cdot\frac{2}{7} + 15 = 45$ , and thus, the other seven players would have scored a total of $56-45 = \boxed{\textbf{(B)} 11}$ . (We see that this works since we could have $4$ of them score $2$ points, and the other $3$ of them score $1$ point.)
-aops5234 -Edited by Penguin_Spellcaster

## Solution 3 — Modular Arithmetic
Adding together Alexa's and Brittany's fractions, we get $\frac{15}{28}$ as the fraction of the total number of points they scored together. However, this is just a ratio, so we can introduce a variable: $\frac{15x}{28x}$ where $x$ is the common ratio. Let $y$ and $z$ and $w$ be the number of people who scored 1, 2, and 0 points, respectively. Writing an equation, we have $\frac{13x}{28x} = 15 + y + 2z + 0w.$ We want all of our variables to be integers. Thus, we want $15 + y + 2z = 0 \pmod {13}.$ Simplifying, $y+2z = 11 \pmod {13}.$ The only possible value, as this integer sum has to be less than $7 \cdot 2 + 1 = 15,$ must be 11. Therefore, $y+2z = 11,$ and the answer is $\boxed{ \textbf{(B) 11}}$ .
- ab2024

## Solution 4: Answer choices
We can rewrite the question as an algebraic equation: $\frac{1}{4} x + \frac{2}{7} x + 15 + y = x$ , where $x$ represents the total amount of points and $y$ the amount of points the $7$ other players scored. From there, we add the two fractions to get $\frac{15}{28} x + 15 + y = x$ . Subtracting $\frac{15}{28} x$ from both sides, we get $\frac{13}{28} x = y + 15$ . We multiply each side by $28$ to get rid of the denominator, in which we get $13x = 420 + 28y$ . Now let’s think of this logically. This equation is telling us that if you add $420$ and $28$ times the amount of points scored by the extra $7$ players, you get $13$ times the amount of points total. And since we have to have a whole number of points total, this means that $420 + 28y$ must be divisible by $13$ . Plugging in all the answer choices for $y$ , we find that the only answer that makes $420 + 28y$ divisible by $13$ is $\boxed{ \textbf{(B) 11}}$ .
~ilee0820

## Video Solution by Math-X
https://youtu.be/IgpayYB48C4?si=JjQHbrlBpeox9TFq&t=7063
~Math-X

## Video Solution by Brain Math Club
https://www.youtube.com/watch?v=fKjmw_zzCUU
- Happytwin

## Video Solution by RMM Club
https://www.youtube.com/watch?v=jE-7Se7ay1c

## Video Solution
https://www.youtube.com/watch?v=3Mae_6qFxoU&t
~ hi_im_bob

## Video Solution by Vincent Lo
https://youtu.be/wsYCn2FqZJE
~Vincent Lo

## Video Solution by Math Ex
https://www.youtube.com/watch?v=o2mcnLOVFBA&list=PLLCzevlMcsWNBsdpItBT4r7Pa8cZb6Viu&index=5
~ MathEx

## Video Solution by Omega Learn
https://youtu.be/HISL2-N5NVg?t=4115
~ pi_is_3.14

## Video Solution
https://youtu.be/dI8RzUHLqZc
~savannahsolver

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1
### See Also