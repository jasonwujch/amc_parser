# 2014 AMC 8 Problem 11

## Problem

Jack wants to bike from his house to Jill's house, which is located three blocks east and two blocks north of Jack's house. After biking each block, Jack can continue either east or north, but he needs to avoid a dangerous intersection one block east and one block north of his house. In how many ways can he reach Jill's house by biking a total of five blocks?

$\textbf{(A) }4\qquad\textbf{(B) }5\qquad\textbf{(C) }6\qquad\textbf{(D) }8\qquad \textbf{(E) }10$

## Video Solution (CREATIVE THINKING)
https://youtu.be/YCr5GFcmdcI
~Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=rxrQLNxESW0 ~David
https://youtu.be/pWLm41JtiCw ~savannahsolver

## Solution 1
We can apply complementary counting and count the paths that DO go through the blocked intersection, which is $\dbinom{2}{1}\dbinom{3}{1}=6$ . There are a total of $\dbinom{5}{2}=10$ paths, so there are $10-6=4$ paths possible. $\boxed{(\text{A})4}$ is the correct answer.

## Solution 2
We can make a diagram of the roads available to Jack. [asy] size(50); defaultpen(linewidth(0.8)); pair A=(0,2),B=origin,C=(2,0),D=(2,2),E=(2,1),F=(3,2),G=(3,1),H=(3,0); draw(A--B--H--F--A); draw(D--C); draw(E--G); [/asy] Then, we can simply list the possible routes. [asy] size(50); defaultpen(linewidth(0.8)); pair A=(0,2),B=origin,C=(2,0),D=(2,2),E=(2,1),F=(3,2),G=(3,1),H=(3,0); draw(B--H--F); draw(D--C,dotted); draw(E--G,dotted); draw(F--A--B,dotted); [/asy] [asy] size(50); defaultpen(linewidth(0.8)); pair A=(0,2),B=origin,C=(2,0),D=(2,2),E=(2,1),F=(3,2),G=(3,1),H=(3,0); draw(B--C--E--G--F); draw(B--A--F,dotted); draw(D--E,dotted); draw(C--H--G,dotted); [/asy] [asy] size(50); defaultpen(linewidth(0.8)); pair A=(0,2),B=origin,C=(2,0),D=(2,2),E=(2,1),F=(3,2),G=(3,1),H=(3,0); draw(B--C--D--F); draw(B--A--D,dotted); draw(E--G,dotted); draw(F--H--C,dotted); [/asy] [asy] size(50); defaultpen(linewidth(0.8)); pair A=(0,2),B=origin,C=(2,0),D=(2,2),E=(2,1),F=(3,2),G=(3,1),H=(3,0); draw(B--A--F); draw(B--H--F,dotted); draw(D--C,dotted); draw(E--G,dotted); [/asy] There are 4 possible routes, so our answer is $\boxed{A}$ .
Note: This is not recommended in more complicated problems (e.g. Jill's house is 1000 blocks east and 400 blocks north of Jack's house).
### See Also