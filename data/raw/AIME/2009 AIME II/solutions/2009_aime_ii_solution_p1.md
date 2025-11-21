# 2009 AIME II Problem 1

## Problem

Before starting to paint, Bill had $130$ ounces of blue paint, $164$ ounces of red paint, and $188$ ounces of white paint. Bill painted four equally sized stripes on a wall, making a blue stripe, a red stripe, a white stripe, and a pink stripe. Pink is a mixture of red and white, not necessarily in equal amounts. When Bill finished, he had equal amounts of blue, red, and white paint left. Find the total number of ounces of paint Bill had left.

## Solution 1
Let $x$ be the amount of paint in a strip. The total amount of paint is $130+164+188=482$ . After painting the wall, the total amount of paint is $482-4x$ . Because the total amount in each color is the same after finishing, we have
\[\frac{482-4x}{3} = 130-x\] \[482-4x=390-3x\] \[x=92\]
Our answer is $482-4\cdot 92 = 482 - 368 = \boxed{114}$ .
~ carolynlikesmath

## Solution 2 (Simple Solution)
Let the stripes be $b, r, w,$ and $p$ , respectively. Let the red part of the pink be $\frac{r_p}{p}$ and the white part be $\frac{w_p}{p}$ for $\frac{r_p+w_p}{p}=p$ .
Since the stripes are of equal size, we have $b=r=w=p$ . Since the amounts of paint end equal, we have $130-b=164-r-\frac{r_p}{p}=188-w-\frac{w_p}{p}$ . Thus, we know that \[130-p=164-p-\frac{r_p}{p}=188-p-\frac{w_p}{p}\] \[130=164-\frac{r_p}{p}=188-\frac{w_p}{p}\] \[r_p=34p, w_p=58p\] \[\frac{r_p+w_p}{p}=92=p=b.\] Each paint must end with $130-92=38$ oz left, for a total of $3 \cdot 38 = \boxed{114}$ oz.

## Solution 3
After the pink stripe is drawn, all three colors will be used equally so the pink stripe must bring the amount of red and white paint down to $130$ ounces each. Say $a$ is the fraction of the pink paint that is red paint and $x$ is the size of each stripe. Then equations can be written: $ax = 164 - 130 = 34$ and $(1-a)x = 188 - 130 = 58$ . The second equation becomes $x - ax = 58$ and substituting the first equation into this one we get $x - 34 = 58$ so $x = 92$ . The amount of each color left over at the end is thus $130 - 92 = 38$ and $38 * 3 = \boxed{114}$ .

## Solution 4
We know that all the stripes are of equal size. We can then say that $r$ is the amount of paint per stripe. Then $130 - r$ will be the amount of blue paint left. Now for the other two stripes. The amount of white paint left after the white stripe and the amount of red paint left after the blue stripe are $188 - r$ and $164 - r$ respectively. The pink stripe is also r ounces of paint, but let there be $k$ ounces of red paint in the mixture and $r - k$ ounces of white paint. We now have two equations: $164 - r - k = 188 - r - (r-k)$ and $164 - r - k = 130 - r$ . Solving yields k = 34 and r = 92. We now see that there will be $130 - 92 = 38$ ounces of paint left in each can. $38 * 3 = \boxed{114}$

## Solution 5
Let the amount of paint each stripe painted used be $x$ . Also, let the amount of paint of each color left be $y$ . 1 stripe is drawn with the blue paint, and 3 stripes are drawn with the red and white paints. Add together the amount of red and white paint, $164 + 188 = 352$ and obtain the following equations : $352 - 3x = 2y$ and $130 - x = y$ . Solve to obtain $x = 92$ . Therefore $y$ is $130 - 92 = 38$ , with three cans of equal amount of paint, the answer is $38 * 3 = \boxed{114}$ .

## Solution 6
Let $x$ be the number of ounces of paint needed for a single stripe. We know that in the end, the total amount of red and white paint will equal double the amount of blue paint.
After painting, the amount of red and white paint remaining is equal to $164+188-2x$ , and then minus another $x$ for the pink stripe. The amount of blue paint remaining is equal to $130-x$ . So, we get the equation $2\cdot(130-x)=164+188-3x$ . Simplifying, we get $x=38$ and $3x=\boxed{114}$ .
~LegionOfAvatars

## Solution 7
Just like in solution 1, we note that all colors will be used equally, except for the pink stripe. This must bring red and white down to $130$ each, so $34$ red and $58$ white are used, making for a total of $92$ for the pink stripe. Thus, the other stripes also use $92$ . The answer is $130+164+188-4(92)=\boxed{114}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.