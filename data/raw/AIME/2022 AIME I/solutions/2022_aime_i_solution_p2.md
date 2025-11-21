# 2022 AIME I Problem 2

## Problem

Find the three-digit positive integer $\underline{a}\,\underline{b}\,\underline{c}$ whose representation in base nine is $\underline{b}\,\underline{c}\,\underline{a}_{\,\text{nine}},$ where $a,$ $b,$ and $c$ are (not necessarily distinct) digits.

## Solution 1
We are given that \[100a + 10b + c = 81b + 9c + a,\] which rearranges to \[99a = 71b + 8c.\] Taking both sides modulo $71,$ we have \begin{align*} 28a &\equiv 8c \pmod{71} \\ 7a &\equiv 2c \pmod{71}. \end{align*} The only solution occurs at $(a,c)=(2,7),$ from which $b=2.$
Therefore, the requested three-digit positive integer is $\underline{a}\,\underline{b}\,\underline{c}=\boxed{227}.$
~MRENTHUSIASM

## Solution 2
As shown in Solution 1, we get $99a = 71b+8c$ .
Note that $99$ and $71$ are large numbers comparatively to $8$ , so we hypothesize that $a$ and $b$ are equal and $8c$ fills the gap between them. The difference between $99$ and $71$ is $28$ , which is a multiple of $4$ . So, if we multiply this by $2$ , it will be a multiple of $8$ and thus the gap can be filled. Therefore, the only solution is $(a,b,c)=(2,2,7)$ , and the answer is $\underline{a}\,\underline{b}\,\underline{c}=\boxed{227}$ .
~KingRavi

## Solution 2a
A little bit more motivation: taking mod $8$ on both sides, we find that $7a\equiv7b\pmod8\implies a\equiv b\pmod8$ , so either $a=b$ or they differ by a multiple of $8$ (okok technically $a=b$ is a subcase of the other one but shh for the sake of clarity). $99$ and $71$ differ by $28$ , so a difference of merely $8$ in $a$ and $b$ accounts for a huge difference on the scale of $28\cdot8=224$ (which is obviously unfillable by the mere $8c$ ), so $a=b$ is very reasonable.
~Technodoggo

## Solution 3
As shown in Solution 1, we get $99a = 71b+8c.$
We list a few multiples of $99$ out: \[99,198,297,396.\] Of course, $99$ can't be made of just $8$ 's. If we use one $71$ , we get a remainder of $28$ , which can't be made of $8$ 's either. So $99$ doesn't work. $198$ can't be made up of just $8$ 's. If we use one $71$ , we get a remainder of $127$ , which can't be made of $8$ 's. If we use two $71$ 's, we get a remainder of $56$ , which can be made of $8$ 's. Therefore we get $99\cdot2=71\cdot2+8\cdot7$ so $a=2,b=2,$ and $c=7$ . Plugging this back into the original problem shows that this answer is indeed correct. Therefore, $\underline{a}\,\underline{b}\,\underline{c}=\boxed{227}.$
~Technodoggo

## Solution 4
As shown in Solution 1, we get $99a = 71b+8c$ .
We can see that $99$ is $28$ larger than $71$ , and we have an $8c$ . We can clearly see that $56$ is a multiple of $8$ , and any larger than $56$ would result in $c$ being larger than $9$ . Therefore, our only solution is $a = 2, b = 2, c = 7$ . Our answer is $\underline{a}\,\underline{b}\,\underline{c}=\boxed{227}$ .
~Arcticturn

## Solution 5
As shown in Solution 1, we get $99a = 71b+8c,$ which rearranges to \[99(a – b) = 8c – 28 b = 4(2c – 7b) \le 4(2\cdot 9 - 0 ) = 72.\] So $a=b, 2c = 7b \implies c=7, b=2,a=2.$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 6
As shown in Solution 1, we have that $99a = 71b + 8c$ .
Note that by the divisibility rule for $9$ , we have $a+b+c \equiv a \pmod{9}$ . Since $b$ and $c$ are base- $9$ digits, we can say that $b+c = 0$ or $b+c=9$ . The former possibility can be easily eliminated, and thus $b+c=9$ . Next, we write the equation from Solution 1 as $99a = 63b + 8(b+c)$ , and dividing this by $9$ gives $11a = 7b+8$ . Taking both sides modulo $7$ , we have $4a \equiv 1 \pmod{7}$ . Multiplying both sides by $2$ gives $a\equiv 2 \pmod{7}$ , which implies $a=2$ . From here, we can find that $b=2$ and $c=7$ , giving an answer of $\boxed{227}$ .
~Sedro

## Video Solution by OmegaLearn
https://youtu.be/SCGzEOOICr4?t=340
~ pi_is_3.14

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=z5Y4bT5rL-s

## Video Solution
https://www.youtube.com/watch?v=CwSkAHR3AcM
~Steven Chen (www.professorchenedu.com)

## Video Solution
https://youtu.be/MJ_M-xvwHLk?t=392
~ThePuzzlr

## Video Solution by MRENTHUSIASM (English & Chinese)
https://www.youtube.com/watch?v=v4tHtlcD9ww&t=360s&ab_channel=MRENTHUSIASM
~MRENTHUSIASM

## Video Solution
https://youtu.be/YcZzxez-j-c
~AMC & AIME Training
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .