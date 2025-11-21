# 2020 AIME II Problem 5

## Problem

For each positive integer $n$ , let $f(n)$ be the sum of the digits in the base-four representation of $n$ and let $g(n)$ be the sum of the digits in the base-eight representation of $f(n)$ . For example, $f(2020) = f(133210_{\text{4}}) = 10 = 12_{\text{8}}$ , and $g(2020) = \text{the digit sum of }12_{\text{8}} = 3$ . Let $N$ be the least value of $n$ such that the base-sixteen representation of $g(n)$ cannot be expressed using only the digits $0$ through $9$ . Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Let's work backwards. The minimum base-sixteen representation of $g(n)$ that cannot be expressed using only the digits $0$ through $9$ is $A_{16}$ , which is equal to $10$ in base 10. Thus, the sum of the digits of the base-eight representation of the sum of the digits of $f(n)$ is $10$ . The minimum value for which this is achieved is $37_8$ . We have that $37_8 = 31$ . Thus, the sum of the digits of the base-four representation of $n$ is $31$ . The minimum value for which this is achieved is $13,333,333,333_4$ . We just need this value in base 10 modulo 1000. We get $13,333,333,333_4 = 3(1 + 4 + 4^2 + \dots + 4^8 + 4^9) + 4^{10} = 3\left(\dfrac{4^{10} - 1}{3}\right) + 4^{10} = 2*4^{10} - 1$ . Taking this value modulo $1000$ , we get the final answer of $\boxed{151}$ . (If you are having trouble with this step, note that $2^{10} = 1024 \equiv 24 \pmod{1000}$ ) ~ TopNotchMath

## Solution 2 (Official MAA)
First note that if $h_b(s)$ is the least positive integer whose digit sum, in some fixed base $b$ , is $s$ , then $h_b$ is a strictly increasing function. This together with the fact that $g(N) \ge 10$ shows that $f(N)$ is the least positive integer whose base-eight digit sum is 10. Thus $f(N) = 37_\text{eight} = 31$ , and $N$ is the least positive integer whose base-four digit sum is $31.$ Therefore \[N = 13333333333_\text{four} = 2\cdot4^{10} - 1 = 2\cdot1024^2 - 1\] \[\equiv 2\cdot24^2 - 1 \equiv 151 \pmod{1000}.\]

## Video Solutions
https://youtu.be/lTyiRQTtIZI
https://youtu.be/ZWe_99091e4

## Video Solution by OmegaLearn
https://youtu.be/ZhAZ1oPe5Ds?t=5032
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .