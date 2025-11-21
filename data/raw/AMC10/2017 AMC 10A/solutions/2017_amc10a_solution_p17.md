# 2017 AMC 10A Problem 17

## Problem

Distinct points $P$ , $Q$ , $R$ , $S$ lie on the circle $x^{2}+y^{2}=25$ and have integer coordinates. The distances $PQ$ and $RS$ are irrational numbers. What is the greatest possible value of the ratio $\frac{PQ}{RS}$ ?

$\textbf{(A) } 3 \qquad \textbf{(B) } 5 \qquad \textbf{(C) } 3\sqrt{5} \qquad \textbf{(D) } 7 \qquad \textbf{(E) } 5\sqrt{2}$

## Solution 1
Because $P$ , $Q$ , $R$ , and $S$ are lattice points, there are only a few coordinates that actually satisfy the equation. The coordinates are $(\pm 3,\pm 4), (\pm 4, \pm 3), (0,\pm 5),$ and $(\pm 5,0).$ We want to maximize $PQ$ and minimize $RS.$ They also have to be non perfect squares, because they are both irrational. The greatest value of $PQ$ happens when $P$ and $Q$ are almost directly across from each other and are in different quadrants. For example, the endpoints of the segment could be $(-4,3)$ and $(3,-4)$ because the two points are almost across from each other. Another possible pair could be $(-4,3)$ and $(5,0)$ . To find out which segment is longer, we have to compare the distances from their endpoints to a diameter (which must be the longest possible segment). The closest diameter would be from $(-4,3)$ to $(4,-3)$ . The distance between $(3,-4)$ and $(-4,3)$ is greater than the distance between $(5,0)$ and $(4,-3)$ . Therefore, the segment from $(3,-4)$ to $(-4,3)$ is the longest attainable (the other possible coordinates for $P$ and $Q$ are $(4,3)$ and $(-3, -4)$ , $(3, 4)$ and $(-4, -3)$ , $(-3, 4)$ and $(4, -3)$ . The least value of $RS$ is when the two endpoints are in the same quadrant and are very close to each other. This can occur when, for example, $R$ is $(3,4)$ and $S$ is $(4,3).$ They are in the same quadrant and no other point on the circle with integer coordinates is closer to the point $(3,4)$ than $(4,3)$ and vice versa. Using the distance formula, we get that $PQ$ is $\sqrt{98}$ and that $RS$ is $\sqrt{2}.$ $\frac{\sqrt{98}}{\sqrt{2}}=\sqrt{49}=\boxed{\mathrm{\textbf{(D)}}\ 7}$

## Solution 2
We can look at the option choices. Since we are aiming for the highest possible ratio, let's try using $7$ (though $5 \sqrt{2}$ actually is the highest ratio.) Now, looking at the problem alone, we know that to have the largest ratio possible, we have to let $RS$ be the minimum possible value while at the same time using integer coordinates. Thus, the smallest possible value of $RS$ is $\sqrt{1^{2}+1^{2}} = \sqrt{2}$ . Assuming that $\frac{PQ}{RS} = 7$ , we plug in $RS = \sqrt{2}$ and solve for $PQ$ : $PQ=7\sqrt{2}$ . Remember, we don't know if this is possible yet, we are only trying to figure out if it is. But for what values of $x$ and $y$ does $\sqrt{x^{2}+y^{2}}=7\sqrt2$ ? We see that this can easily be made into a $45-45-90$ triangle. But, instead of substituting $y=x$ into the equation and then using a whole lot of algebra, we can save time and use the little trick, that if in a $45-45-90$ triangle, the two $45$ degree sides have side length $s$ , then the hypotenuse is $s\sqrt2$ . Using this, we can see that $s=7$ , and since our equation does in fact yield a sensible solution, we can be assured that our answer is $\boxed{\mathrm{\textbf{(D)}}\ 7}$ .
Quality Control by fasterthanlight
(Note by Carrot_Karen: We tried $7$ , but some might be confused why we concluded that it was the answer after verifying without trying the others, like why wasn't option $\textbf{(E)}$ tried? This is because the problem can only have one correct answer, so if we have an option that already works, we can conclude that none of the others work and $\textbf{(D)}$ is the answer.
comment:(but in other problems, they had different answer choices that worked, so you cant be sure.)
(Note by Pinotation: The above reasoning for why $\textbf{(E)}$ was not tried is incorrect. Option $\textbf{(E)}$ is gotten by not reading the question thoroughly and choosing the diameter as the longest length. Then, to get the shortest length, you choose points \((-3, -4)\) and \((-4,-3)\) to get a length of \( \sqrt{2} \). This then gives \( \frac{PQ}{RS} = \frac{10}{\sqrt{2}} = 5\sqrt{2} \). This answer is gotten from assuming the diameter, which is 10, but the questions states that PQ and RS are irrational lengths. That is the reason why the answer is $\boxed{\mathrm{\textbf{(D)}}\ 7}$ and not $\textbf{(E)}$ . You may also check out Beauty Of Math's video linked here.)

## Solution 3
By inspection, when $R$ is at $(3, 4)$ and $S$ is at $(4, 3),$ it makes $RS$ as small as possible with a distance of $\sqrt{2}$ . The greatest possible length of $PQ$ arises when $P$ is at $(-3, 4)$ and $Q$ is at $(4, -3).$ Using the distance formula, we find that $PQ$ has a length of $7\sqrt{2}.$ The requested fraction is then $\dfrac{PQ}{RS} = \dfrac{7\sqrt{2}}{\sqrt{2}} = \boxed{\mathrm{\textbf{(D)}}\ 7}$ .

## Video Solution
https://youtu.be/umr2Aj9ViOA?t=162
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .