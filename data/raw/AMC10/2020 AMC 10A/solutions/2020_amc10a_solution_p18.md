# 2020 AMC 10A Problem 18

## Problem

Let $(a,b,c,d)$ be an ordered quadruple of not necessarily distinct integers, each one of them in the set $\{0,1,2,3\}.$ For how many such quadruples is it true that $a\cdot d-b\cdot c$ is odd? (For example, $(0,3,1,1)$ is one such quadruple, because $0\cdot 1-3\cdot 1 = -3$ is odd.)

$\textbf{(A) } 48 \qquad \textbf{(B) } 64 \qquad \textbf{(C) } 96 \qquad \textbf{(D) } 128 \qquad \textbf{(E) } 192$

## Solutions

## Solution 1 (Parity)
In order for $a\cdot d-b\cdot c$ to be odd, consider parity. We must have (even)-(odd) or (odd)-(even). There are $2(2 + 4) = 12$ ways to pick numbers to obtain an even product. There are $2 \cdot 2 = 4$ ways to obtain an odd product. Therefore, the total amount of ways to make $a\cdot d-b\cdot c$ odd is $2 \cdot (12 \cdot 4) = \boxed{\bold{(C)}\ 96}$ .
~Midnight

## Solution 2 (Solution 1 but more in-depth)
Consider parity. We need exactly one term to be odd, one term to be even. Because of symmetry, we can set $ad$ to be odd and $bc$ to be even, then multiply by $2.$ If $ad$ is odd, both $a$ and $d$ must be odd, therefore there are $2\cdot2=4$ possibilities for $ad.$ Consider $bc.$ Let us say that $b$ is even. Then there are $2\cdot4=8$ possibilities for $bc.$ However, $b$ can be odd, in which case we have $2\cdot2=4$ more possibilities for $bc.$ Thus there are $12$ ways for us to choose $bc$ and $4$ ways for us to choose $ad.$ Therefore, also considering symmetry, we have $2 \cdot 4 \cdot 12= \boxed{ \text{(C) } 96}$ total values of $ad-bc.$
~lpieleanu (Reformatting and Minor Edits)

## Solution 3 (Complementary Counting)
There are 4 ways to choose any number independently and 2 ways to choose any odd number independently. To get an even products, we count: $\text{P(any number)} \cdot \text{P(any number)}-\text{P(odd)}\cdot\text{P(odd)}$ , which is $4 \cdot 4 - 2 \cdot 2=12$ . The number of ways to get an odd product can be counted like so: $\text{P(odd)}\cdot\text{P(odd)}$ , which is $2 \cdot 2$ , or $4$ . So, for one product to be odd the other to be even: $2 \cdot 4 \cdot 12= \boxed{ \text{(C) } 96}$ (order matters).
~Anonymous and Arctic_Bunny

## Solution 4 (Solution 3 but more in-depth)
We use complementary counting: If the difference is even, then we can subtract those cases. There are a total of $4^4=256$ cases.
For an even difference, we have (even)-(even) or (odd-odd).
From Solution 3:
"There are 4 ways to choose any number independently and 2 ways to choose any odd number independently. even products:(number)*(number)-(odd)*(odd): $4 \cdot 4 - 2 \cdot 2=12$ . odd products: (odd)*(odd): $2 \cdot 2 =4$ ."
With this, we easily calculate $256-12^2-4^2=\textbf{(C)96}$ .
~kevinmathz

## Solution 5 (Casework)
As in solution 1, we must have (even)-(odd) or (odd)-(even). We see that there are two cases, if $ad$ is even and $bc$ is odd and if $ad$ is odd and $bc$ is even. Because of symmetry, we can multiply by two for when $ad$ is odd and $bc$ is even. Let $e$ denote an even number and let $o$ denote an odd number.
If $ad$ is even and $bc$ is odd, there are three cases:
\[(e,o,o,e)\] \[(e,o,o,o)\] \[(o,o,o,e)\]
For each of these cases, there are $2^4$ ways to choose from the set $(0,1,2,3)$ as there are 2 even's and 2 odd's; because there are three cases, we multiply this by 3. Also, because of there are 2 cases ( $ad$ is even and $bc$ is odd and if $ad$ is odd and $bc$ is even), we multiply this by 2. This gives us:
$2^4 \cdot 3 \cdot 2= \textbf{(C)96}$

## Solution 6
For parity reasons, if $ad - bc$ is to be odd, we must have $ad$ odd and $bc$ even or $ad$ even and $bc$ odd. By symmetry, these cases are identical, so we consider the first one and multiply by two at the end. For $ad$ to be odd, we must have both $a$ and $d$ odd, and there are $2 \cdot 2$ ways to do so. To count the cases where $bc$ is odd, we use PIE. there are $2 \cdot 4 = 8$ ways for $b$ to be odd and $4 \cdot 2 = 8$ ways for $c$ to be odd, and there are $2 \cdot 2 = 4$ ways for both to be odd. Thus, there are $8 + 8 - 4 = 12$ ways for $bc$ to be even. Multiplying out, there are $2 \cdot 4 \cdot 12$ ways to have $ad - bc$ odd for a total of $\boxed{\textbf{(C)}~96}$ .
~ cxsmi

## Video Solutions
Education, The Study of Everything
https://youtu.be/D34FxUr9TvI
https://youtu.be/RKlG6oZq9so
~IceMatrix
https://youtu.be/3bRjcrkd5mQ?t=1
~ pi_is_3.14
### Additional Notes
### Additional Note 1
When calculating the number of even products and odd products, since the only way to get an odd product is to multiply two odd integers together, and there are $2$ odd integers, it can quickly be deduced that there are $2 \cdot 2 = 4$ possibilities for an odd product. Since the product must be either odd or even, and there are $4 \cdot 4 = 16$ ways to choose factors for the product, there are $16 - 4 = 12$ possibilities for an even product. ~ emerald_block
### Additional Note 2
This problem is similar to 2007 AMC10A Problem 16. View it here: https://artofproblemsolving.com/wiki/index.php/2007_AMC_10A_Problems/Problem_16
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .