# 2009 AMC 10A Problem 22

## Problem

Two cubical dice each have removable numbers $1$ through $6$ . The twelve numbers on the two dice are removed, put into a bag, then drawn one at a time and randomly reattached to the faces of the cubes, one number to each face. The dice are then rolled and the numbers on the two top faces are added. What is the probability that the sum is $7$ ?

$\mathrm{(A)}\ \frac{1}{9} \qquad \mathrm{(B)}\ \frac{1}{8} \qquad \mathrm{(C)}\ \frac{1}{6} \qquad \mathrm{(D)}\ \frac{2}{11} \qquad \mathrm{(E)}\ \frac{1}{5}$

## Solution 1
At the moment when the numbers are in the bag, imagine that each of them has a different color. Clearly the situation is symmetric at this moment. Hence after we draw them, attach them and throw the dice, the probability of getting some pair of colors is the same for any two colors.
There are ${12 \choose 2} = 66$ ways to pick two of the colors. We now have to count the ways where the two chosen numbers will have a sum of $7$ .
A sum of $7$ can be obtained as $1+6$ , $2+5$ , or $3+4$ . Each number in the bag has two different colors, hence each of these three options corresponds to four pairs of colors.
Out of the $66$ pairs of colors we can get when throwing the dice, $3\cdot 4=12$ will give us the sum $7$ . Hence the probability that this will happen is $\frac{12}{66} = \boxed{\textbf{(D) }\frac 2{11}}$ .

## Solution 2
Ignoring the numbers that do not affect the probability of the desired outcome (the ones that are not on top of the dice), say that the number on top of the first die is $n$ . For the sum of the $2$ numbers to be $7$ , the second die must have the number $7-n$ on top. There are $11$ remaining numbers that could be on top of the second die, $2$ of which are $7-n$ (since $n\ne7-n$ in all cases and since there are 2 faces for each number 1-6).
Thus, the probability of the sum of the $2$ numbers being $7$ is $\frac{2}{11}$ , so the answer is $\mathrm{(D)}$ .

## Solution 3
Taking out the rolling dice part, we see that we're just taking two numbers out of a bag. There are ${12 \choose 2}=66$ ways to pick two, and there are 12 ways to pick one, and 2 ways to pick the other. (After you pick one, the other one you pick is fixed). Now say you pick n. The other number you pick has to be 7-n. But if you picked 7-n first and n second, that would be the same thing. So we need to divide by 2.
This gives $\frac{\frac{12 \cdot 2}{2}}{66}=\boxed{\frac{2}{11}}$ or $\mathrm{(D)}$ .

## Solution 4 (Educated Guess)
Let first case(Two Same Numbers on One Die) = $A$
Let second case(No Two Same Numbers on One Die) = $B$
Note that the possible combinations of two numbers summing to 7 are $(1,6), (2,5), (3,4), (4,3), (5,2),$ and $(6,1)$ .
The second case( $B$ ) thus has $\frac{6}{36}=\frac{1}{6}$ chance. The other case has another probability of some number.
The sum is $\frac{1}{6}+A$ so the answer must be greater than $\frac{1}{6}$ , which are choices D and E.
Note that there are $\binom{12}{2}=66$ cases for a number without restrictions.
Use answer choices to note that $\frac{1}{6}+\frac{1}{66}=\frac{2}{11}.$ (Answer choice D)
Also use it to note that $\frac{1}{6}+\frac{1}{30}=\frac{1}{5}.$ (Answer Choice E)
Answer choice D makes more sense , so the answer is $\boxed{\mathrm{D}}.$
Also, if you had some time, you would note that only 1 of the 66 total combinations fit the first case, so $\boxed{\mathrm{D}}$ is your answer.
~mathboy282 (Yes I know this is a bad solution but if you had little time left on the test this would be a good educated guess.)

## Video Solution by OmegaLearn
https://youtu.be/IRyWOZQMTV8?t=2808
~ pi_is_3.1415

## Video Solution by TheBeautyofMath
https://youtu.be/W2bgcN-q3ow?t=58
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .