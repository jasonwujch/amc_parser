# 2021 AMC 10A Problem 15

## Problem

Values for $A,B,C,$ and $D$ are to be selected from $\{1, 2, 3, 4, 5, 6\}$ without replacement (i.e. no two letters have the same value). How many ways are there to make such choices so that the two curves $y=Ax^2+B$ and $y=Cx^2+D$ intersect? (The order in which the curves are listed does not matter; for example, the choices $A=3, B=2, C=4, D=1$ is considered the same as the choices $A=4, B=1, C=3, D=2.$ )

$\textbf{(A) }30 \qquad \textbf{(B) }60 \qquad \textbf{(C) }90 \qquad \textbf{(D) }180 \qquad \textbf{(E) }360$

## Solution 1 (Intuition):
Visualizing the two curves, we realize they are both parabolas with the same axis of symmetry. WLOG the first equation is above the second, since order doesn't matter. Then $C>A$ and $B>D$ . Therefore the number of ways to choose the four integers is $\tbinom{6}{2}\tbinom{4}{2}=90$ , and the answer is $\boxed{\textbf{(C) }90}$ .
~IceWolf10

## Solution 2 (Algebra):
Setting $y = Ax^2+B = Cx^2+D$ , we find that $Ax^2-Cx^2 = x^2(A-C) = D-B$ , so $x^2 = \frac {D-B}{A-C} \ge 0$ by the trivial inequality. This implies that $D-B$ and $A-C$ must both be positive or negative. If two distinct values are chosen for $(A, C)$ and $(B, D)$ respectively, there are $2$ ways to order them so that both the numerator and denominator are positive/negative (increasing and decreasing). We must divide by $2$ at the end, however, since the $2$ curves aren't considered distinct. Calculating, we get \[\frac {1}{2} \cdot \binom {6}{2} \binom {4}{2} \cdot 2 = \boxed{\textbf{(C) }90}.\] ~ike.chen

## Solution 3 (Symmetry):
Like in Solution 2 , we find $\frac {D-B}{A-C} \ge 0$ . Notice that, since $D \ne B$ , this expression can never equal $0$ , and since $A \ne C$ , there won't be a divide-by- $0$ . This means that every choice results in either a positive or a negative value.
For every choice of $(A,B,C,D)$ that results in a positive value, we can flip $B$ and $D$ to obtain a corresponding negative value. This is a bijection (we could flip $B$ and $D$ again to obtain the original choice (injectivity) and we could flip $B$ and $D$ from any negative choice to obtain the corresponding positive choice (surjectivity)), so half of the choices are positive (where the curves intersect) and half are negative (where they don't).
This means that of the $\frac{6\cdot5\cdot4\cdot3}{2} = 180$ total choices (dividing by $2$ because the order of the curves does not matter), half of them, or $\frac{180}{2} = \boxed{\textbf{(C) }90}$ , lead to intersecting curves.
~ emerald_block

## Solution 4 (Simple)
Notice that one of the parabolas must be the wider one and the other one must be the thinner one. There are only two options: the wider one is above the thinner one, or the thinner one is above the wider one. Only the first option works. Therefore, out of the $\frac{1}{2}\cdot 6\cdot 5\cdot 4\cdot 3=180$ ways to pick $A, B, C,$ and $D$ without regard to order, only $\frac{1}{2}\cdot 180=90$ of these work.
~ Mathkiddie

## Video Solution (Quick & Simple)
https://youtu.be/I0C0lGvFdj0
~ Education, the Study of Everything

## Video Solution (Use of Combinatorics and Algebra)
https://www.youtube.com/watch?v=SRjtftj0tSE&list=PLexHyfQ8DMuKqltG3cHT7Di4jhVl6L4YJ&index=7&t=1s
~ North America Math Contest Go Go Go

## Video Solution by OmegaLearn (Using Vieta's Formulas and clever combinatorics)
https://youtu.be/l85Qah1vGgc
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/t-EEP2V4nAE?t=1376
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .