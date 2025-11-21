# 2025 AMC 10A Problem 17

## Problem

Let $N$ be the unique positive integer such that dividing $273436$ by $N$ leaves a remainder of $16$ and dividing $272760$ by $N$ leaves a remainder of $15$ . What is the tens digit of $N$ ?

$\textbf{(A) } 0 \qquad\textbf{(B) } 1 \qquad\textbf{(C) } 2 \qquad\textbf{(D) } 3 \qquad\textbf{(E) } 4$

## Video Solution
https://youtu.be/CCYoHk2Af34

## Solution 1
The problem statement implies that $N$ divides both $273436-16=273420$ and $272760-15=272745$ . We want to find $N > 16$ that satisfies both of these conditions. Hence, we can just find the greatest common divisor of the two numbers. $\gcd(273420,272745)=\gcd(675,272745)=\gcd(675,45)=45$ by the Euclidean Algorithm, so the answer is $\boxed{\text{(E) }4}.$
Note: If an integer $a$ is congruent to an integer $b$ modulo a positive integer $c$ , denoted by $a \equiv b \pmod{c}$ , this means that $c$ divides the difference $a-b$
~Tacos_are_yummy_1
~andliu766
minor edit by AD_12

## Solution 2
We are given that $273436 \equiv 16 \pmod N$ and $272760 \equiv 15 \pmod N$ , from which we get $273420 \equiv 0 \pmod N$ and $272745 \equiv 0 \pmod N$ .
Substracting the two gives $273420 - 272745 = 675$ , which is also divisible by $N$ .
Since $N$ must be greater than $16$ , the only possible divisors of $675$ are $25, 27, 45, 75, 135, 225,$ and $675$ . Checking which ones also divide $273436$ and $273420$ eliminates $25$ and $27$ , but $273420 \equiv 0 \pmod {45}$ .
Since both $273420$ and $675$ are divisible by $45$ , so is $273420-675=272745$ . Thus, $N = 45$ works, and its tens digit is $\boxed{\text{(E) }4}$ .
~Continuous_Pi
~edited by Zhixing

## Solution 3
We get that: $273436 \equiv {16}\pmod{N}$ and $272760 \equiv {15}\pmod{N}$ .
So we also have that: $273420 \equiv {0}\pmod{N}$ and $272745 \equiv {0}\pmod{N}.$
Notice that these are a multiple of $5$ . Now, we subtract these numbers to get $675$ . We see that $675 = 25 \cdot 27.$ There is a factor of $5$ and $9$ . $273420$ and $272745$ are multiples of $9$ as well, so our answer is just 45, or $\boxed{\text{(E) }4}$ .
~Aarav22
~reformatting by Alzwang
~minor editing by kfclover

## Solution 4
We are given that $273436 \equiv 16 \pmod{N}$ and $272760 \equiv 15 \pmod{N}.$ Subtracting, we get $273436 - 272760 = 676 \equiv 1 \pmod{N}.$
This means $N$ divides $675.$ Also, since $273436 \equiv 16 \pmod{N},$ we have $273420 \equiv 0 \pmod{N}.$
Thus, $N$ divides both $273420$ and $675.$ Using the Euclidean Algorithm: $273420 - 405 \times 675 = 45,$ so $\gcd(273420, 675) = 45.$
Hence $N = 45,$ and the tens digit of $N$ is $\boxed{\text{(E) }4}.$
~samma ~minor LaTeX edits by vinceS

## Chinese Video Solution
https://www.bilibili.com/video/BV1nLkQBpEXR/
~metrixgo

## Video Solution (In 2 Mins)
https://youtu.be/ax76SAmVuYw?si=1YPIk87CnrevwHRm ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .