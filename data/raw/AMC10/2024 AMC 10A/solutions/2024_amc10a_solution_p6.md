# 2024 AMC 10A Problem 6

## Problem

What is the minimum number of successive swaps of adjacent letters in the string $ABCDEF$ that are needed to change the string to $FEDCBA?$ (For example, $3$ swaps are required to change $ABC$ to $CBA;$ one such sequence of swaps is $ABC\to BAC\to BCA\to CBA.$ )

$\textbf{(A)}~6\qquad\textbf{(B)}~10\qquad\textbf{(C)}~12\qquad\textbf{(D)}~15\qquad\textbf{(E)}~24$

## Solution 1 (Analysis)
Procedurally, it takes:
- $5$ swaps for $A$ to move to the sixth spot, giving $BCDEFA.$
- $4$ swaps for $B$ to move to the fifth spot, giving $CDEFBA.$
- $3$ swaps for $C$ to move to the fourth spot, giving $DEFCBA.$
- $2$ swaps for $D$ to move to the third spot, giving $EFDCBA.$
- $1$ swap for $E$ to move to the second spot (so $F$ becomes the first spot), giving $FEDCBA.$
Together, the answer is $5+4+3+2+1=\boxed{\textbf{(D)}~15}.$
~MRENTHUSIASM

## Solution 2 (Recursive Approach)
We can proceed by a recursive tactic on the number of letters in the string.
Looking at the string $A$ , there are $0$ moves needed to change it to the string $A$
Then, there is $1$ move to change $AB$ to $BA$ .
Similarly, there is $3$ moves needed for three letters (said in the problem).
There are $6$ moves needed to change $ABCD$ to $DCBA$ .
We see a pattern of $0,1,3,6,...$ . We notice that the difference between consecutive terms is increasing by $1$ , so in the same way, for $5$ letters, we would need $10$ moves, and for $6$ , we would need $\boxed{\textbf{(D)}~15}$ moves.
Thinking why, when we start making these moves, we see that for a string of length $n$ , it takes $n-1$ moves to move the last letter to the front. After, we get a string that will be changed identically to a string of length $n-1$ . This works in our pattern above and is another way to think about the problem!
~world123
Note:
The sequence consists of triangular numbers shifted a term up (as it starts with $0$ on term $1$ and $1$ on term $2$ .) Thus, our explicit formula is \[\dfrac{(n-1)(n+1-1)}{2} = \dfrac{(n)(n-1)}{2}\] and as $n = 6$ in this case ( $6$ letters), our answer is $\dfrac{(6)(6-1)}{2} = \boxed{\textbf{(D)}~15}$
~NSAoPS

## Solution 3 (Solution 2 Done Fast)
We can see that the most efficient way to change $ABCDEF$ to $FEDCBA$ is the same as changing $ABCDE$ to $EDCBA$ and then moving $F$ to the front in $5$ moves. Similarly, this would carry on downwards, where to change $ABCDE$ to $EDCBA$ would be to change $ABCD$ to $DCBA$ and move $E$ $4$ times to the front. This pattern will carry on until $AB$ to $BA$ would be $1$ , and $A$ to $A$ would be $0$ . The answer would be $0(A)+1(B)+2(C)+3(D)+4(E)+5(F)$ , which is $\boxed{\textbf{(D)}~15}$ moves.
~Moonwatcher22

## Solution 4 (If you don't notice anything)
Simply, just blindly doing it, the most straightforward way is to shift F all the way back. From ABCDEF:
$ABCDFE ->ABCFDE ->ABFCDE ->AFBCDE ->FABCDE$
For E:
$FABCED -> FABECD -> FAEBCD -> FEABCD$
For D:
$FEABDC -> FEADBC -> FEDABC$
For C:
$FEDACB -> FEDCAB$
For B:
FEDCBA
That's it, you don't need to do it with A. Still $\boxed{\textbf{(D)}~15}$ moves.
~pepper2831

## Solution 5 (Inversions of Permutations)
Let the letters $A, B, C, D, E, F$ correspond to the numbers $1, 2, 3, 4, 5, 6$ respectively. We want to find the number of swaps required to transform the permutation $1 2 3 4 5 6$ into the permutation $6 5 4 3 2 1$ .
Here, we let $1 2 3 4 5 6$ be the natural order. Then the total number of inversions of the permutation $6 5 4 3 2 1$ is $1+2+3+4+5=15$ . Hence the answer is $\boxed{\textbf{(D)}~15}$
~tsun26

## Video Solution by Central Valley Math Circle
https://youtu.be/3E881mgzXO8
~mr_mathman

## Video Solution
https://youtu.be/l3VrUsZkv8I
~MC

## Video Solution by Pi Academy
https://youtu.be/6qYaJsgqkbs?si=K2Ebwqg-Ro8Yqoiv

## Video Solution 1 by Power Solve
https://youtu.be/j-37jvqzhrg?si=ieBRx0-CUihcKttE&t=616

## Video Solution by Daily Dose of Math
https://youtu.be/-EFTk2pBFug
~Thesmartgreekmathdude

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=_o5zagJVe1U

## Video Solution by Just Math⚡
https://youtu.be/KrkjGpk1uZs

## Video Solution by Dr. David
https://youtu.be/aeckUgolmIM

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=890s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .