# 2023 AIME II Problem 2

## Problem

Recall that a palindrome is a number that reads the same forward and backward. Find the greatest integer less than $1000$ that is a palindrome both when written in base ten and when written in base eight, such as $292 = 444_{\text{eight}}.$

## Solution
Assuming that such palindrome is greater than $777_8 = 511,$ we conclude that the palindrome has four digits when written in base $8.$ Let such palindrome be \[(\underline{ABBA})_8 = 512A + 64B + 8B + A = 513A + 72B.\]
It is clear that $A=1,$ so we repeatedly add $72$ to $513$ until we get palindromes less than $1000:$ \begin{align*} 513+72\cdot0 &= 513, \\ 513+72\cdot1 &= \boxed{585}, \\ 513+72\cdot2 &= 657, \\ 513+72\cdot3 &= 729, \\ 513+72\cdot4 &= 801, \\ 513+72\cdot5 &= 873, \\ 513+72\cdot6 &= 945, \\ 513+72\cdot7 &= 1017. \\ \end{align*}
~MRENTHUSIASM

## Video Solution
https://youtu.be/BxXP6s1za0g
~MathProblemSolvingSkills.com

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=_JTFiqczLvk

## Video Solution by the Power of Logic(#1 and #2)
https://youtu.be/VcEulZ3nvSI
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .