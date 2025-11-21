# 2021 Fall AMC 10A Problem 18

## Problem

A farmer's rectangular field is partitioned into $2$ by $2$ grid of $4$ rectangular sections as shown in the figure. In each section the farmer will plant one crop: corn, wheat, soybeans, or potatoes. The farmer does not want to grow corn and wheat in any two sections that share a border, and the farmer does not want to grow soybeans and potatoes in any two sections that share a border. Given these restrictions, in how many ways can the farmer choose crops to plant in each of the four sections of the field? [asy] draw((0,0)--(100,0)--(100,50)--(0,50)--cycle); draw((50,0)--(50,50)); draw((0,25)--(100,25)); [/asy] $\textbf{(A)}\ 12 \qquad \textbf{(B)}\ 64 \qquad \textbf{(C)}\ 84 \qquad \textbf{(D)}\ 90 \qquad \textbf{(E)}\ 144$

## Solution 1 (Casework)
There are $4$ possibilities for the top-left section. It follows that the top-right and bottom-left sections each have $3$ possibilities, so they have $3^2=9$ combinations. We have two cases:
1. The top-right and bottom-left sections have the same crop.
1. The top-right and bottom-left sections have different crops.
Note that $3$ of the $9$ combinations of the top-right and bottom-left sections satisfy this case, from which the bottom-right section has $3$ possibilities. Therefore, there are $4\cdot3\cdot3=36$ ways in this case.
Note that $6$ of the $9$ combinations of the top-right and bottom-left sections satisfy this case, from which the bottom-right section has $2$ possibilities. Therefore, there are $4\cdot6\cdot2=48$ ways in this case.
Together, the answer is $36+48=\boxed{\textbf{(C)}\ 84}.$
~Arcticturn ~MRENTHUSIASM

## Solution 2 (Casework)
We will do casework on the type of crops in the field.
Case 1: all of a kind.
If all four sections have the same type of crop, there are simply $\underline{4}$ ways to choose crops for the sections.
Case 2: of a kind, of another kind.
Since the one of another kind must be adjacent to two of the other crops, when choosing the type of crops in this case, we cannot choose soybeans and potatoes, or corn and wheat. Therefore, there are $4 \cdot 3 - 2 \cdot 2 = 8$ choices for the two crops we choose for the section (notice we did not choose by $2$ , since the crop we pick first will be the unique one), and $4$ ways to choose which section the unique crop is planted on. This gives us a total of $4 \cdot 8 = \underline{32}$ ways to choose crops for the sections.
Case 3: of a kind, of another kind.
We cannot choose corn and wheat, or soybeans and potatoes, once again, because if we do, the two would have to be adjacent in some way, which the problem disallows. So, there are ${4 \choose 2} - 2 = 4$ ways to choose our two crops (notice that we did choose by $2$ , since there are two of both crops). There are ${4 \choose 2} = 6$ ways to choose where one of the crops go, so there are $4 \cdot 6 = \underline{24}$ ways to choose crops for the sections.
Case 4: of a kind, of another kind, of another kind.
In cases 2 and 3, we excluded the possibility of choosing bad pairs for our crops (i.e. soybeans and potatoes, or corn and wheat). In this case, it is inevitable that we choose a bad pair, because we are choosing $3$ crops this time. The two sections of the same kind must contain the crop that is not part of the bad pair in the trio: for example, if we choose corn, soybeans and potatoes as our three crop types, nor soybeans and potatoes can be the type which occupies two sections in this case; corn must be the one to do so. There are $4$ ways to choose the crop that is not part of the bad pair, and then $1$ way to choose the bad pair, giving us $4 \cdot 1 = 4$ ways to choose the crops. To separate the bad pair of crops, the two of a kind must be diagonally placed. There are $2$ ways to choose where the two of a kind go, and $2$ ways to choose which of the bad pair goes where, giving us $2 \cdot 2 = 4$ ways to choose the positions for the crops. In total, there are $4 \cdot 4 = \underline{16}$ ways to choose crops for the sections.
Case 5: every single crop.
Bad pairs must be on the same diagonal, so there are $2$ ways to choose which pair gets which diagonal, and $2 \cdot 2 = 4$ ways to choose which of each pair goes where on the diagonal, giving us $2 \cdot 4 = \underline{8}$ ways to choose crops for the sections.
Adding up all our values, we get our final answer of $4+32+24+16+8 = \boxed{\textbf{(C)}\ 84}$ .
~ihatemath123

## Solution 3 (Casework)
To lighten notation, we use C, W, S, P to denote corn, wheat, soybeans, and potatoes, respectively.
We use I, II, III, IV to denote four quadrants, respectively.
We determine an arrangement in the following steps.
Step 1: Determine the crop planted in I.
The number of ways is $4$ .
Step 2: Determine the crops planted in II, III, IV.
To find the number of arrangements in this step, without loss of generality, we assume that we plant C in I.
We do the following casework analysis.
Case 1: Both II and IV are planted with C.
In this case, the number of ways to plant in III is $3$ .
Case 2: In II and IV, only one quadrant is planted with C, and another quadrant is planted with either S or P.
In this case, we determine an arrangement in the following steps.
Step 2.1: Determine whether C is planted in II or IV.
The number of ways is $2$ .
Step 2.2: In II or IV not planted with C, determine whether it is planted with S or P.
The number of ways is $2$ .
Step 2.3: Determine the crop planted in III.
The number of ways is $2$ .
Following from the rule of product, the number of ways in this case is $2 \cdot 2 \cdot 2 = 8$ .
Case 3: II and IV are both planted with S or W.
In this case, we determine an arrangement in the following steps.
Step 2.1: Determine whether S or W is planted in II and IV.
The number of ways is $2$ .
Step 2.2: Determine the crop planted in III.
The number of ways is $3$ .
Following from the rule of product, the number of ways in this case is $2 \cdot 3 = 6$ .
Case 4: In II and IV, exactly one quadrant is planted with S and another one is planted with W.
Step 2.1: Determine which quadrant in II and IV is planted with S.
The number of ways is $2$ .
Step 2.2: Determine the crop planted in III.
The number of ways is $2$ .
Following from the rule of product, the number of ways in this case is $2 \cdot 2 = 4$ .
Putting all cases together, the total number of arrangements in Step 2 is $3 + 8 + 6 + 4 = 21$ .
Following from the rule of product, the total number of arrangements is $4 \cdot 21 = 84$ .
Therefore, the answer is $\boxed{\textbf{(C)}\ 84}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 4 (Principle of Inclusion-Exclusion)
The number of cases with at least one pair of corn and wheat adjacent is $4 \cdot 2 \cdot 4^2 - 4 \cdot 2 \cdot 4 + 0 - 2 = 94$ possible fields (You can easily see this for yourself using PIE.), and WLOG, the same goes for soybean and potatoes. Now, applying PIE on both sets (number of cases with at least one pair of corn and wheat and the number of cases with at least one pair of soybeans and potatoes) yields $2\cdot94 - 16 = 172$ . We want the number of cases without adjacent pairs of soybeans and potatoes or wheat and corn, so we subtract $256 - 172$ , yielding an answer of $\boxed{\textbf{(C)}\ 84}.$
~ icecreamrolls8

## Solution 5 (Tree Diagram)
We can create a tree representing an arbitrary box we start with and the possibilities for other boxes around the grid. We can just designate the crop we start with as $1$ , and the other crops as $2$ , $3$ , and $4$ , where $1$ cannot be next to $2$ and $3$ cannot be next to $4$ in the grid. [asy] size(400); draw((0, 0)--(-10, -2)--(-13, -4)--(-14, -6)); draw((-13, -4)--(-13,-6)); draw((-13, -4)--(-12,-6)); draw((-10, -2)--(-10, -4)--(-10.5, -6)); draw((-10, -4)--(-9.5, -6)); draw((-10, -2)--(-7, -4)--(-7.5, -6)); draw((-7, -4)--(-6.5, -6)); label("$1$", (0, 0), N); label("$1$", (-10, -2), UnFill(0.5mm)); label("$1$", (-13, -4), UnFill(0.5mm)); label("$1$", (-14, -6), UnFill(0.5mm)); label("$3$", (-13, -6), UnFill(0.5mm)); label("$4$", (-12, -6), UnFill(0.5mm)); label("$3$", (-10, -4), UnFill(0.5mm)); label("$1$", (-10.5, -6), UnFill(0.5mm)); label("$3$", (-9.5, -6), UnFill(0.5mm)); label("$4$", (-7, -4), UnFill(0.5mm)); label("$1$", (-7.5, -6), UnFill(0.5mm)); label("$4$", (-6.5, -6), UnFill(0.5mm)); draw((0, 0)--(0, -2)--(-3, -4)--(-4, -6)); draw((-3, -4)--(-3, -6)); draw((-3, -4)--(-2, -6)); draw((0, -2)--(0, -4)--(-0.5, -6)); draw((0, -4)--(0.5, -6)); draw((0, -2)--(3, -4)--(2.5, -6)); draw((3, -4)--(3.5, -6)); label("$3$", (0, -2), UnFill(0.5mm)); label("$1$", (-3, -4), UnFill(0.5mm)); label("$2$", (0, -4), UnFill(0.5mm)); label("$3$", (3, -4), UnFill(0.5mm)); label("$4$", (-2, -6), UnFill(0.5mm)); label("$3$", (-3, -6), UnFill(0.5mm)); label("$1$", (-4, -6), UnFill(0.5mm)); label("$3$", (-0.5, -6), UnFill(0.5mm)); label("$4$", (0.5, -6), UnFill(0.5mm)); label("$1$", (2.5, -6), UnFill(0.5mm)); label("$3$", (3.5, -6), UnFill(0.5mm)); draw((0, 0)--(10, -2)--(13, -4)--(13.5, -6)); draw((13, -4)--(12.5,-6)); draw((10, -2)--(10, -4)--(10.5, -6)); draw((10, -4)--(9.5, -6)); draw((10, -2)--(7, -4)--(8, -6)); draw((7, -4)--(7, -6)); draw((7, -4)--(6, -6)); label("$4$", (10, -2), UnFill(0.5mm)); label("$4$", (13, -4), UnFill(0.5mm)); label("$4$", (13.5, -6), UnFill(0.5mm)); label("$1$", (12.5, -6), UnFill(0.5mm)); label("$2$", (10, -4), UnFill(0.5mm)); label("$4$", (10.5, -6), UnFill(0.5mm)); label("$3$", (9.5, -6), UnFill(0.5mm)); label("$1$", (7, -4), UnFill(0.5mm)); label("$4$", (8, -6), UnFill(0.5mm)); label("$3$", (7, -6), UnFill(0.5mm)); label("$1$", (6, -6), UnFill(0.5mm)); [/asy] As we can see, there are $21$ possibilities. We multiply this by the $4$ (the number of possibilities there are for the crop we started with), so our answer is $\boxed{\textbf{(C)}\ 84}$ .
~NonOxyCrustacean

## Solution 6 (Educated Guess)
The top right box has $4$ choices and the top left box has $3$ choices. Thus, it is reasonable to assume that the answer is a multiple of $12$ . We know that the answer will not be too small or too large, so the answer is $\boxed{\textbf{(C)}\ 84}$ .
~Aidensharp

## Solution 7 (Metasolve)
Estimation suggests B is too low, and clearly 90 is incorrect as it has a factor of $5$ which is impossible to achieve with combinations less than $5$ . Thus, the answer is $\boxed{\textbf{(C)}\ 84}.$
~YOUSmomentumSAG

## Video Solution (Just 2 min!)
https://youtu.be/1II04QhD9Bs
~Education, the Study of Everything

## Video Solution by TheBeautyofMath
https://youtu.be/n5_he263qe8
~IceMatrix

## Video Solution by OmegaLearn
https://youtu.be/kxgUdv_L-ys?t=372
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .