# 2024 AMC 8 Problem 7

## Problem

A $3 \times 7$ rectangle is covered without overlap by 3 shapes of tiles: $2 \times 2$ , $1\times4$ , and $1\times1$ , shown below. What is the minimum possible number of $1\times1$ tiles used?

$\textbf{(A) } 1\qquad\textbf{(B)} 2\qquad\textbf{(C) } 3\qquad\textbf{(D) } 4\qquad\textbf{(E) } 5$

## Solution 1
We can eliminate B, C, and D, because they are not $21$ subtracted by any multiple of $4$ . Finally, we see that there is no way to have A, so the solution is $\boxed{\textbf{(E)\ 5}}$ .

## Solution 2
Let $x$ be the number of $1$ by $1$ tiles. There are $21$ squares and each $2$ by $2$ or $1$ by $4$ tile takes up 4 squares, so $x \equiv 1 \pmod{4}$ , so it is either $1$ or $5$ . Color the columns, starting with red, then blue, and alternating colors, ending with a red column. There are $12$ red squares and $9$ blue squares, but each $2$ by $2$ and $1$ by $4$ shape takes up an equal number of blue and red squares, so there must be $3$ more $1$ by $1$ tiles on red squares than on blue squares, which is impossible if there is just one, so the answer is $\boxed{\textbf{(E)\ 5}}$ , which can easily be confirmed to work.
~arfekete

## Solution 3
Suppose there are $a$ different $2\times 2$ tiles, $b$ different $4\times 1$ tiles and $c$ different $1\times 1$ tiles. Since the areas of these tiles must total up to $21$ (area of the whole grid), we have \[4a + 4b + c = 21.\] Reducing modulo $4$ gives $c\equiv 1\pmod{4}$ , or $c = 1$ or $c = 5$ .
If $c = 1$ , then $a + b = 5$ . After some testing, there is no valid pair $(a, b)$ that works, so the answer must be $\boxed{\textbf{(E)\ 5}}$ , which can be constructed in many ways.
-Benedict T (countmath1)

## Solution 4
Since the rectangle is a 3x7 grid, its total area (or the number of 1x1 squares) is 21. To minimize the number of 1x1 squares used, we begin by filling the area with larger shapes. Specifically, we can use two 2x2 squares, each covering 4 squares, and two 1x4 rectangles, each also covering 4 squares. This gives us a total of 4+4=8 4+4=8 squares filled by larger shapes.After filling 16 squares, we have 5 squares left. We can then fill in 5 additional 1x1 squares, leaving us with a total of 5 1x1 squares.
Thus, the least number of 1x1 squares required is $\boxed{\textbf{(E)\ 5}}$ . -AADHYA2012
### Video by MathTalks 😉
https://youtu.be/9GVWXv9Pg1E?si=lhCKMjJ0wvfc_MfY
~rc1219

## Video Solution 1 (Detailed Explanation) 🚀⚡📊
Youtube Link ⬇️
https://youtu.be/-MD8uFguEUQ
~ ChillGuyDoesMath :)

## Video Solution by Central Valley Math Circle(Goes through the full thought process)
https://youtu.be/5pFxqcqE220
~mr_mathman

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=eg8T8wApi2j83Ia_&t=1497
~Math-X

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=WogR3xd8zMwJgzRf&t=712
~hsnacademy

## Video Solution 1 (easy to digest) by Power Solve
https://youtu.be/16YYti_pDUg?si=KjRhUdCOAx10kgiW&t=59

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc
~NiuniuMaths

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=L83DxusGkSY

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=L4ouVVVkFo4

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=578

## Video Solution by Daily Dose of Math (Certified, Simple, and Logical)
https://youtu.be/8GHuS5HEoWc
~Thesmartgreekmathdude

## Video Solution by WhyMath
https://youtu.be/LCCDCb1EHg0
### See Also