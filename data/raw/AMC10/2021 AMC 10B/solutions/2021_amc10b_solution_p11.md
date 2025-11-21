# 2021 AMC 10B Problem 11

## Problem

Grandma has just finished baking a large rectangular pan of brownies. She is planning to make rectangular pieces of equal size and shape, with straight cuts parallel to the sides of the pan. Each cut must be made entirely across the pan. Grandma wants to make the same number of interior pieces as pieces along the perimeter of the pan. What is the greatest possible number of brownies she can produce?

$\textbf{(A)} ~24 \qquad\textbf{(B)} ~30 \qquad\textbf{(C)} ~48 \qquad\textbf{(D)} ~60 \qquad\textbf{(E)} ~64$

## Solution 1
Let the side lengths of the rectangular pan be $m$ and $n$ . It follows that $(m-2)(n-2) = \frac{mn}{2}$ , since half of the brownie pieces are in the interior. This gives $2(m-2)(n-2) = mn \iff mn - 4m - 4n + 8 = 0$ . Adding $8$ to both sides and applying Simon's Favorite Factoring Trick , we obtain $(m-4)(n-4) = 8$ . Since $m$ and $n$ are both positive, we obtain $(m, n) = (5, 12), (6, 8)$ (up to ordering). By inspection, $5 \cdot 12 = \boxed{\textbf{(D) }60}$ maximizes the number of brownies.
~ ike.chen ~minor edits Marshall_huang

## Solution 2
Obviously, no side of the rectangular pan can have less than $5$ brownies beside it. We let one side of the pan have $5$ brownies, and let the number of brownies on its adjacent side be $x$ . Therefore, $5x=2\cdot3(x-2)$ , and solving yields $x=12$ and there are $5\cdot12=60$ brownies in the pan. $64$ is the only choice larger than $60$ , but it cannot be the answer since the only way to fit $64$ brownies in a pan without letting a side of it have less than $5$ brownies beside it is by forming a square of $8$ brownies on each side, which does not meet the requirement. Thus the answer is $\boxed{\textbf{(D) }60}$ .
-SmileKat32

## Solution 3 (rational function)
Let the interior of the pan have $n$ vertical cuts and $m$ horizontal cuts. We see that $mn = 2(m + n) + 4$ . We want the greatest possible value of $(m+2)(n+2) = 2mn.$ Expanding the first equation we get \[mn = 2m + 2n + 4 \implies (m-2)n = 2m + 4 \implies n = \frac{2m + 4}{m - 2}.\] In the first quadrant, this is a rational function which decreases as $m$ approaches infinity. So we want the smallest value for $m$ for the largest value of $n$ . We know $m \geq 3$ . If $m = 3, n = 10.$ And we know since the function only decreases from here, these must be the greatest possible values. So the answer is $2mn = 2\cdot 30 = \boxed{60}.$
~ grogg007

## Video Solution by OmegaLearn (Simon's Favorite Factoring Trick)
https://youtu.be/vWlRQiyt0c8
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/L1iW94Ue3eI
~IceMatrix

## Video Solution by Interstigation
https://youtu.be/wltQ9m07kzg
~Interstigation

## Video Solution by Challenge 25
https://youtu.be/Gf5YNjxsaoA?t=531

## Solution 3 (Simon's favorite factoring trick)
Let $m$ be the number of brownies on the top horizontal side of the pan and let $n$ be the number of brownies on the leftmost vertical side of the pan. The total number of brownies in the interior is then $(m-2)(n-2).$ Then, the number of brownies on the perimeter would be $2m+2n-4.$ Expanding the left side we get: $mn-2m-2n+4.$ Bringing the right side of the equation to the left side and adding 8 to both the sides we get $(n-4)(m-4)=8.$ Making a table, we get that the highest number possible would be 60 brownies.
-nambha
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .