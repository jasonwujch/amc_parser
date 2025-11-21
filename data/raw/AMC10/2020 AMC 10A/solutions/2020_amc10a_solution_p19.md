# 2020 AMC 10A Problem 19

## Problem

As shown in the figure below, a regular dodecahedron (the polyhedron consisting of $12$ congruent regular pentagonal faces) floats in space with two horizontal faces. Note that there is a ring of five slanted faces adjacent to the top face, and a ring of five slanted faces adjacent to the bottom face. How many ways are there to move from the top face to the bottom face via a sequence of adjacent faces so that each face is visited at most once and moves are not permitted from the bottom ring to the top ring? [asy] import graph; unitsize(5cm); pair A = (0.082, 0.378); pair B = (0.091, 0.649); pair C = (0.249, 0.899); pair D = (0.479, 0.939); pair E = (0.758, 0.893); pair F = (0.862, 0.658); pair G = (0.924, 0.403); pair H = (0.747, 0.194); pair I = (0.526, 0.075); pair J = (0.251, 0.170); pair K = (0.568, 0.234); pair L = (0.262, 0.449); pair M = (0.373, 0.813); pair N = (0.731, 0.813); pair O = (0.851, 0.461); path[] f; f[0] = A--B--C--M--L--cycle; f[1] = C--D--E--N--M--cycle; f[2] = E--F--G--O--N--cycle; f[3] = G--H--I--K--O--cycle; f[4] = I--J--A--L--K--cycle; f[5] = K--L--M--N--O--cycle; draw(f[0]); axialshade(f[1], white, M, gray(0.5), (C+2*D)/3); draw(f[1]); filldraw(f[2], gray); filldraw(f[3], gray); axialshade(f[4], white, L, gray(0.7), J); draw(f[4]); draw(f[5]); [/asy] $\textbf{(A) } 125 \qquad \textbf{(B) } 250 \qquad \textbf{(C) } 405 \qquad \textbf{(D) } 640 \qquad \textbf{(E) } 810$

## Solution 1
Since we start at the top face and end at the bottom face without moving from the lower ring to the upper ring or revisiting a face, our journey must consist of the top face, a series of faces in the upper ring, a series of faces in the lower ring, and the bottom face, in that order.
We have $5$ choices for which face we visit first on the top ring. From there, we have $9$ choices for how far around the top ring we go before moving down: $1,2,3,$ or $4$ faces around clockwise, $1,2,3,$ or $4$ faces around counterclockwise, or immediately going down to the lower ring without visiting any other faces in the upper ring.
We then have $2$ choices for which lower ring face to visit first (since every upper-ring face is adjacent to exactly $2$ lower-ring faces) and then once again $9$ choices for how to travel around the lower ring. We then proceed to the bottom face, completing the trip.
Multiplying together all the numbers of choices we have, we get $5 \cdot 9 \cdot 2 \cdot 9 = \boxed{\textbf{(E) } 810}$ .

## Solution 2 (Similar to Solution 1)
From the top, we can go down in five different ways to the five faces underneath the first face. From here we can go down or go to the adjacent faces. From the face you went down from the top face, you can either go clockwise or counterclockwise $1$ , $2$ , $3$ ,or $4$ times, or you can go straight down. Then from there, you go down into the lower row, which you have two choices, left or right down. From here we have $5 \cdot 9 \cdot 2$ ways multiplied by the ways you can move from the bottom ring to the bottom face, but we don't need to know that since from here we can see that $\boxed{(E)}$ is the only answer choice divisible by $90$ , so our answer is $\boxed{(E)}$ . ~Terribleteeth

## Solution 3
There are five ways to get to the top ring. Casework:
Case 1: directly go to bottom ring For each of the 5 initial top ring faces, we have two ways of directly going to the bottom ring, as each face on the top is adjacent to two faces on the bottom. There are $5 \cdot 2 = 10$ paths here.
Case 2: traversing sideways After entering the top ring, we can also choose to travel sideways along the top ring before going to the bottom ring. For each of the 5 initial top ring faces, we can choose 2 directions to go (clockwise or counterclockwise). Once we choose a direction, we can go 1, 2, 3, or 4 faces in that direction. Notice we cannot travel 5 faces because then we would land on the original top ring face, but the problem specifies that we can only travel each face once. Once again, top ring faces are each adjacent to two bottom ring faces, so after traversing sideways we can choose 2 paths to exit. There are $5 \cdot 2 \cdot 4 \cdot 2 = 80$ paths here.
Adding the two cases together, there are 90 ways to get to the bottom ring from the top.
Next, from the bottom ring to the bottom we do casework again:
Case 1: directly go to the bottom For each of the 90 ways we can get to faces on the bottom ring, there is only 1 way to get to the bottom. So there are 90 ways here.
Case 2: traversing sideways For each of the 90 ways we can get to faces on the bottom ring, there are once again 2 ways to choose the direction and 4 ways to choose the amount of faces traveled. However, after traveling the faces there is only 1 way to go to the bottom face. There are $90 \cdot 2 \cdot 4 \cdot 1 = 720$ paths here.
Adding together the cases, there are 810 paths, or answer choice E. ~JH. L

## Solution 4
Like Solution 3, we can use casework, but in a different way. We can split the caseworks into the amount of moves we spend on each row (top and bottom, where both rows have 5 faces).
Case 1: 1 move on the top row; There are 5 ways to make 1 move on the top row from the starting point (just moving on each of the five faces). Now we want to look at how many ways we can move towards the bottom. Notice how we have two faces on the bottom row that are adjacent to each of the top faces. If we spend one move on the bottom, there are 2 ways. If we spend two moves on the bottom, there are 4 ways (since order matters, we can flip the direction of these moves). If we spend three moves on the bottom, there are also 4 ways (similar reasoning). If we spend four moves on the bottom, there are 4 ways. And if we spend five moves on the bottom, there are again, 4 ways. In total there are $2 + 4 + 4 + 4 + 4 = 18$ ways to move from the bottom after the top moves are chosen. And since there are 5 ways to make 1 move on the top row, there are $5 \cdot 18 = 90$ ways.
Case 2: 2 moves on the top row; From just counting, we can see that there are five ways to move once on the top, and after that, two options for the second move (either left or right), so there are $5 \cdot 2 = 10$ ways. And from using what we obtained in Case 1, there are $10 \cdot 18 = 180$ ways for this case.
Case 3: three moves on the top row; There are, again, 10 ways to do this. And so, there are $10 \cdot 18 = 180$ ways for this case to happen.
Now, we can see that there will be 10 ways for the remaining cases of the first move for the top row (because 5 ways to choose the first, and then you can go either left or right, so $5 \cdot 2 = 10$ ). So for Case 4 and Case 5, there will both also be $10 \cdot 18 = 180$ ways.
Finally, adding all these cases up, we obtain $90 + 180 + 180 + 180 + 180 = 810$ , or $\boxed{(E)}$ ~Misclicked

## Video Solutions

## Video Solution by OmegaLearn
https://youtu.be/HhdpuJt78Hg?t=739
~ pi_is_3.14

## Video Solution 1
Education, The Study of Everything
https://youtu.be/av1hZOm5ELU

## Video Solution 2
https://www.youtube.com/watch?v=Y0gezpr8Mrk&list=PLLCzevlMcsWNcTZEaxHe8VaccrhubDOlQ&index=1 ~ MathEx
### See Also
https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_3 For more explainations.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .