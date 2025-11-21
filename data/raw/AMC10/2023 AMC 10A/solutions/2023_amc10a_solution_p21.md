# 2023 AMC 10A Problem 21

## Problem

Let $P(x)$ be the unique polynomial of minimal degree with the following properties:

- $P(x)$ has a leading coefficient $1$ ,

- $1$ is a root of $P(x)-1$ ,

- $2$ is a root of $P(x-2)$ ,

- $3$ is a root of $P(3x)$ , and

- $4$ is a root of $4P(x)$ .

The roots of $P(x)$ are integers, with one exception. The root that is not an integer can be written as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime integers. What is $m+n$ ?

$\textbf{(A) }41\qquad\textbf{(B) }43\qquad\textbf{(C) }45\qquad\textbf{(D) }47\qquad\textbf{(E) }49$

## Solution 1
From the problem statement, we find $P(2-2)=0$ , $P(9)=0$ and $4P(4)=0$ . Therefore, we know that $0$ , $9$ , and $4$ are roots. So, we can factor $P(x)$ as $x(x - 9)(x - 4)(x - a)$ , where $a$ is the unknown root. Since $P(x) - 1 = 0$ , we plug in $x = 1$ which gives $1(-8)(-3)(1 - a) = 1$ , so $24(1 - a) = 1 \implies 1 - a = 1/24 \implies a = 23/24$ . Therefore, our answer is $23 + 24 =\boxed{\textbf{(D) }47}$
~aiden22gao ~cosinesine ~walmartbrian ~sravya_m18 ~ESAOPS ~Andrew_Lu ~sl_hc

## Solution 2
We proceed similarly to solution one. We get that $x(x-9)(x-4)(x-a)=1$ . Expanding, we get that $x(x-9)(x-4)(x-a)=x^4-(a+13)x^3+(13a+36)x^2-36ax$ . We know that $P(1)=1$ , so the sum of the coefficients of the cubic expression is equal to one. Thus $1-(a+13)+(13a+36)-36a=1$ . Solving for $a$ , we get that $a = 23/24$ . Therefore, our answer is $23 + 24 =\boxed{\textbf{(D) }47}$
~Aopsthedude

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=oAdscLjoWqHtVcUX&t=4673 ~little-fermat

## Video Solution 1 by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=HDaV3kGwwywXP2J5&t=7475
~Math-X

## Video Solution 2 by OmegaLearn
https://youtu.be/aOL04sKGyfU

## Video Solution
https://youtu.be/jIqF_dhczsY

## Video Solution by CosineMethod
https://www.youtube.com/watch?v=HEqewKGKrFE

## Video Solution 3
https://youtu.be/Jan9feBsPEg
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution 4 by EpicBird08
https://www.youtube.com/watch?v=D4GWjJmpqEU&t=25s

## Video Solution 5 by MegaMath
https://www.youtube.com/watch?v=4Hwt3f1bi1c&t=1s
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .