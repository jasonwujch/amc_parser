# 2023 AMC 10B Problem 8

## Problem

What is the units digit of $2022^{2023} + 2023^{2022}$ ?

$\text{(A)}\ 7 \qquad \text{(B)}\ 1 \qquad \text{(C)}\ 9 \qquad \text{(D)}\ 5 \qquad \text{(E)}\ 3$

## Solution 1
$2022^{2023} + 2023^{2022} \equiv 2^3 + 3^2 \equiv 17 \equiv 7$ (mod 10). $\boxed{\text{A}}$ ~andliu766
The method omits many steps, and it is important to note that we do not have $a\equiv b\pmod{m}\Rightarrow c^{a}\equiv c^{b}\pmod{m}$ . For example, $5\equiv 2\pmod{3}$ , but $2^{5}\equiv2\not\equiv1\equiv2^{2}\pmod{3}$ .

## Solution 2
When looking at the units digit patterns of the powers of $2$ , we see that
$2^1=$ , units digit $2$
$2^2=$ , units digit $4$
$2^3=$ , units digit $8$
$2^4=$ , units digit $6$
$2^5=$ , units digit $2$
And the pattern repeats. This pattern will apply for the powers of $2022$ as well, since the units digit of $2022$ is $2$ . We can find the pattern for the powers of $3$ too. The pattern follows with units digits, $3$ , $9$ , $7$ , $1$ , $3$ , $9$ , ... Similarly, the units digit of $2023$ will follow the same pattern as the powers of $3$ .
Both of these powers cycle in groups of $4$ . When diving $2023$ by $4$ , we get $505$ remainder $3$ , meaning $505$ complete cycles; or the power being a multiple of $4$ , $505$ times, and $3$ extra. So the units digit of $2022^{2023}$ is $8$ . $2022$ divided by $4$ is $505$ reminder $2$ , which means $505$ complete cycles, or the power being a multiple of $4$ , $505$ times, and $2$ extra. So the units digit of $2023^{2022}$ is $9$ .
We only need to find the units digit in the end, so we just add those $2$ already found units digits, to get a new units digit of $7$ . Therefore the answer is $\boxed{\text{(A) 7}}$
~mk00

## Solution 3 (Digit Cycles)
Note that the units digit will be the same regardless of the tens, hundreds, and thousands digits, so we can simplify this problem to finding the last digit of $2^{2023} + 3^{2022}$ . We can find the units digit of $2^{2023}$ , by listing the units digits of the first few powers of two, and trying to find a pattern.
$2^1=2$
$2^2=4$
$2^3=8$
$2^4=6+10$
$2^5=2+30$
$2^6=4+60$
As we can see the units digits of powers of two repeat after every four iterations. Now we know the units digit of $2^{2020}$ is $6$ and the units digit of $2^{2023} \Rightarrow 2^3\cdot 2^{2020} \Rightarrow 6\cdot 8 \Rightarrow 8$ . Similarly we can find the last digits of powers of three repeat after every four, so the units digit of $3^{2022}$ is $1\cdot 3^2 = 9$ . Adding these together, the ones digit is the same as the ones digit of $9+8$ which is $7$ . $\boxed{\text{(A) 7}}$
~vsinghminhas

## Solution 4 (Bashy)
$2022^{2023}\equiv 2^{2023}=128^{289}\equiv 8^{289}=2^{289\times3}=131072^{51}\equiv 2^{51}=131072^3\equiv 2^3=8$ $(\text{mod}$ $10)$ $2023^{2022}\equiv 3^{2022}=9^{1011}\equiv (-1)^{1011}=-1\equiv 9$ $(\text{mod}$ $10)$
$8+9=17\equiv 7$ $(\text{mod}$ $10)$
~ Yrock
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .