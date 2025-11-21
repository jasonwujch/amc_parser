# 2024 AMC 10B Problem 6

## Problem

A rectangle has integer length sides and an area of 2024. What is the least possible perimeter of the rectangle?

$\textbf{(A) } 160 \qquad\textbf{(B) } 180 \qquad\textbf{(C) } 222 \qquad\textbf{(D) } 228 \qquad\textbf{(E) } 390$

## Solution 1 - Prime Factorization
We can start by assigning the values x and y for both sides. Here is the equation representing the area:
$x \cdot y = 2024$
Let's write out 2024 fully factorized.
$2^3 \cdot 11 \cdot 23$
Since we know that $x^2 > (x+1)(x-1)$ , we want the two closest numbers possible. After some quick analysis, those two numbers are $44$ and $46$ . $\\44+46=90$
Now we multiply by $2$ and get $\boxed{\textbf{(B) }180}.$
Solution by IshikaSaini .

## Solution 2 - Squared Numbers Trick
We know that $x^2 = (x-1)(x+1)+1$ . Recall that $45^2 = 2025$ .
If I want 1 less than 2025, which is 2024, I can take 1 number higher and 1 number lower from 45, which are 46 and 44. These are the 2 sides of the minimum perimeter because the 2 numbers are closest to each other, which is what we want to get the minimum.
Finding the perimeter with $2(46+44)$ we get $\boxed{\textbf{(B) }180}.$
Solution by ~Taha Jazaeri
Note: The square of any positive integer with units digit $5$ , written in the format $10x + 5$ where $x$ is a positive integer, is equal to $100(x)(x+1)+25$ .
~Cattycute

## Solution 3 - AM-GM Inequality
Denote the numbers as $x, \frac{2024}{x}$ . We know that per AM-GM, $x+\frac{2024}{x} \geq 2\sqrt{2024}$ , but since $2\sqrt{2025} = 90$ , $2\sqrt{2024}$ must be slightly less than 90, so $2x + 2\frac{2024}{x}$ must be slightly less than 180, eliminating A as a possible answer choice. Proceed with the following solutions above to get 44 and 46, which is $\boxed{\textbf{(B) }180}.$
-aleyang

## Solution 4 - Difference of Squares
Note that the year 2025 is a perfect square. The beauty of this year shines down to 2024, which is 1 year lower. $45^2-1^2=2024=(45-1)(45+1)$
Knowing this is the closest possible we can get to a square with only integer factors of 2024, these two are our happy numbers! Add them up to get:
$44+46+44+46=\boxed{\textbf{180}}$ ~BenjaminDong01

## Solution 5 - Get Lucky
Note: This is what I did.
$\sqrt{2025}=45$
Assuming it's a square,
$45\cdot4=\boxed{\textbf{180}}$
~BenjaminDong01

## Solution 6 (Better Prime Factorization)
The smallest perimeter is achieved if the two numbers are as close as possible to one another. The prime factorization of 2024 is \( 2^3 \cdot 11 \cdot 23 \). Notice that 11 is smaller than 23 and there are three 2's to be distributed between 11 and 23. We give 11 \( 2^2 \) and 23 \( 2^1 \). This guarantee's the smallest perimeter. The side length of the rectangle is \( 44 \times 46 \). The perimeter of a rectangle is \( 2l + 2w \), where \( l = 46 \) and \( w = 44 \), so therefore the perimeter is \( 2(46) + 2(44) = 180 \). Therefore the answer is $\boxed{\textbf{(B)} 180}$ .
~Pinotation

## 🎥✨ Video Solution by Scholars Foundation ➡️ Easy-to-Understand 💡✔️
https://youtu.be/T_QESWAKUUk?si=aCvtmf24mzh2HPCJ

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/QLziG_2e7CY?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=24EZaeAThuE

## Video Solution by Daily Dose of Math
https://youtu.be/k1bGPUrhYE4
~Thesmartgreekmathdude

## Video Solution by TheBeautyofMath
https://youtu.be/ZaHv4UkXcbs
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .