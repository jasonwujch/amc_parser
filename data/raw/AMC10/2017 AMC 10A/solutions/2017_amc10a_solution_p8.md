# 2017 AMC 10A Problem 8

## Problem

At a gathering of $30$ people, there are $20$ people who all know each other and $10$ people who know no one. People who know each other hug, and people who do not know each other shake hands. How many handshakes occur within the group?

$\textbf{(A)}\ 240\qquad\textbf{(B)}\ 245\qquad\textbf{(C)}\ 290\qquad\textbf{(D)}\ 480\qquad\textbf{(E)}\ 490$

## Solution 1
Each one of the ten people has to shake hands with all the $20$ other people they don’t know. So $10\cdot20 = 200$ . From there, we calculate how many handshakes occurred between the people who don’t know each other. This is simply counting how many ways to choose two people to shake hands from $10$ , or $\binom{10}{2} = 45$ . Thus the answer is $200 + 45 = \boxed{\textbf{(B)}\ 245}$ .

## Solution 2
We can also use complementary counting. First of all, $\dbinom{30}{2}=435$ handshakes or hugs occur. Then, if we can find the number of hugs, then we can subtract it from $435$ to find the handshakes. Hugs only happen between the $20$ people who know each other, so there are $\dbinom{20}{2}=190$ hugs. $435-190= \boxed{\textbf{(B)}\ 245}$ .

## Solution 3
We can focus on how many handshakes the $10$ people who don't know anybody get.
The first person gets $29$ handshakes with other people not him/herself, the second person gets $28$ handshakes with other people not him/herself and not the first person, ..., and the tenth receives $20$ handshakes with other people not him/herself and not the first, second, ..., ninth person. We can write this as the sum of an arithmetic sequence:
$\frac{10(20+29)}{2}\implies 5(49)\implies 245.$ Therefore, the answer is $\boxed{\textbf{(B)}\ 245}$

## Solution 4
First, we can find out the number of handshakes that the $10$ people who don't know anybody share with the $20$ other people. This is simply $10 \cdot 20 = 200$ . Next, we need to find out the number of handshakes that are shared within the $10$ people who don't know anybody. Here, we can use the formula $\frac{n(n-1)}{2}$ , where $n$ is the number of people being counted. The reason we divide by $2$ is because $n(n-1)$ counts the case where the $1^{st}$ person shakes hands with the $2^{nd}$ person $and$ the case where the $2^{nd}$ shakes hands with the $1^{st}$ (and these 2 cases are the same). Thus, plugging $n=10$ gives us $\frac{10 \cdot 9}{2} \implies 45$ . Adding up the 2 cases gives us $200+45=\boxed{\textbf{(B)}\ 245}$

## Video Solution
https://youtu.be/3MiGotKnC_U?t=1627 ~ ThePuzzlr

## Video Solution
https://youtu.be/pxg7CroAt20
https://youtu.be/cTtqZmui7D4
~savannahsolver

## Video Solution
https://youtu.be/0W3VmFp55cM?t=3464
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .