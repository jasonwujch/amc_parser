# 2019 AMC 10A Problem 17

## Problem

A child builds towers using identically shaped cubes of different colors. How many different towers with a height $8$ cubes can the child build with $2$ red cubes, $3$ blue cubes, and $4$ green cubes? (One cube will be left out.)

$\textbf{(A) } 24 \qquad\textbf{(B) } 288 \qquad\textbf{(C) } 312 \qquad\textbf{(D) } 1,260 \qquad\textbf{(E) } 40,320$

## Solution 1 (Clever Bijection)
Arranging eight cubes is the same as arranging the nine cubes first, and then removing the last cube. In other words, there is a one-to-one correspondence between every arrangement of nine cubes, and every actual valid arrangement. Thus, we initially get $9!$ . However, we have overcounted, because the red cubes can be permuted to have the same overall arrangement, and the same applies with the blue and green cubes. Thus, we have to divide by the $2!$ ways to arrange the red cubes, the $3!$ ways to arrange the blue cubes, and the $4!$ ways to arrange the green cubes. Thus we have $\frac {9!} {2! \cdot 3! \cdot 4!} = \boxed{\textbf{(D) } 1,260}$ different possible towers.
Note : this can be written more compactly as \[\binom{9}{2,3,4}=\binom{9}{2}\binom{9-2}{3}\binom{9-(2+3)}{4} = \boxed{1,260}\]

## Solution 2 (Casework)
We can divide the problem into three cases, each representing one cube to be excluded:
Case 1 : The red cube is excluded. This gives us the problem of arranging one red cube, three blue cubes, and four green cubes. The number of possible arrangements is $\frac{8!}{4!\cdot3!}=280$ . Note that we do not need to multiply by the number of red cubes because there is no way to distinguish between the first red cube and the second.
Case 2 : The blue cube is excluded. This gives us the problem of arranging two red cubes, two blue cubes, and four green cubes. The number of possible arrangements is $\frac{8!}{2!\cdot2!\cdot4!}=420$ .
Case 3 : The green cube is excluded. This gives us the problem of arranging two red cubes, three blue cubes, and three green cubes. The number of possible arrangements is $\frac{8!}{2!\cdot3!\cdot3!}=560$ .
Adding up the individual cases from above gives the answer as $280+420+560=\boxed{\textbf{(D) } 1,260}$ .

## Solution 3 (Educated Guess (Under 1 minute) )
We start by doing the casework for Case 1, as stated in Solution 2. We see that it would be = $280$ . This eliminates answer choices A, B, and C since they are all too small. Then we see the answer choice E is way too big. This makes us choose $\boxed{\textbf{(D) } 1,260}$ ..
~ Continuous_Pi

## Video Solution by OmegaLearn
https://youtu.be/0W3VmFp55cM?t=612
~ pi_is_3.14

## Video Solution
https://youtu.be/3MiGotKnC_U?t=1083 ~ ThePuzzlr

## Video Solution
https://youtu.be/Sk0Gm__kLpo
Education, the Study of Everything

## Video Solution
https://youtu.be/D9RT489UwyQ?t=1338
~ AMBRIGGS
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .