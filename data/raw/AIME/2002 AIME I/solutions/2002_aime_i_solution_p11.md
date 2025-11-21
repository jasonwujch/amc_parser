# 2002 AIME I Problem 11

## Problem

Let $ABCD$ and $BCFG$ be two faces of a cube with $AB=12$ . A beam of light emanates from vertex $A$ and reflects off face $BCFG$ at point $P$ , which is 7 units from $\overline{BG}$ and 5 units from $\overline{BC}$ . The beam continues to be reflected off the faces of the cube. The length of the light path from the time it leaves point $A$ until it next reaches a vertex of the cube is given by $m\sqrt{n}$ , where $m$ and $n$ are integers and $n$ is not divisible by the square of any prime. Find $m+n$ .

## Solution 1(Easy one)
When a light beam reflects off a surface, the path is like that of a ball bouncing. Picture that, and also imagine X, Y, and Z coordinates for the cube vertices. The coordinates will all involve 0's and 12's only, so that means that the X, Y, and Z distance traveled by the light must all be divisible by 12. Since the light's Y changes by 5 and the X changes by 7 (the Z changes by 12, don't worry about that), and 5 and 7 are relatively prime to 12, the light must make 12 reflections onto the XY plane or the face parallel to the XY plane.
In each reflection, the distance traveled by the light is $\sqrt{ (12^2) + (5^2) + (7^2) }$ = $\sqrt{218}$ . This happens 12 times, so the total distance is $12\sqrt{218}$ . $m=12$ and $n=218$ , so therefore, the answer is $m+n=\boxed{230}$ .

## Solution 2(2D and photons)
We can use a similar trick as with reflections in 2D: Imagine that the entire space is divided into cubes identical to the one we have. Now let's follow two photons of light that start in $A$ at the same time: one of them will reflect as given in the problem statement, the second will simply fly straight through all cubes. It can easily be seen that at any moment in time the photons are in exactly the same position relative to the cubes they are inside at the moment. In other words, we can take the cube with the first photon, translate it and flip if necessary, to get the cube with the other photon.
It follows that both photons will hit a vertex at the same time, and at this moment they will have travelled the same distance.
Now, the path of the second photon is simply a half-line given by the vector $(12,7,5)$ . That is, the points visited by the photon are of the form $(12t,7t,5t)$ for $t\geq 0$ . We are looking for the smallest $t$ such that all three coordinates are integer multiples of $12$ (which is the length of the side of the cube).
Clearly $t$ must be an integer. As $7$ and $12$ are relatively prime, the smallest solution is $t=12$ . At this moment the second photon will be at the coordinates $(12\cdot 12,7\cdot 12,5\cdot 12)$ .
Then the distance it travelled is $\sqrt{ (12\cdot 12)^2 + (7\cdot 12)^2 + (5\cdot 12)^2 } = 12\sqrt{12^2 + 7^2 + 5^2}=12\sqrt{218}$ . And as the factorization of $218$ is $218=2\cdot 109$ , we have $m=12$ and $n=218$ , hence $m+n=\boxed{230}$ .
These problems are copyrighted © by the Mathematical Association of America.