# 2015 AIME II Problem 6

## Problem

Steve says to Jon, "I am thinking of a polynomial whose roots are all positive integers. The polynomial has the form $P(x) = 2x^3-2ax^2+(a^2-81)x-c$ for some positive integers $a$ and $c$ . Can you tell me the values of $a$ and $c$ ?"

After some calculations, Jon says, "There is more than one such polynomial."

Steve says, "You're right. Here is the value of $a$ ." He writes down a positive integer and asks, "Can you tell me the value of $c$ ?"

Jon says, "There are still two possible values of $c$ ."

Find the sum of the two possible values of $c$ .

## Solution 1 (Algebra)
We call the three roots (some may be equal to one another) $x_1$ , $x_2$ , and $x_3$ . Using Vieta's formulas, we get $x_1+x_2+x_3 = a$ , $x_1 \cdot x_2+x_1 \cdot x_3+x_2 \cdot x_3 = \frac{a^2-81}{2}$ , and $x_1 \cdot x_2 \cdot x_3 = \frac{c}{2}$ .
Squaring our first equation we get $x_1^2+x_2^2+x_3^2+2 \cdot x_1 \cdot x_2+2 \cdot x_1 \cdot x_3+2 \cdot x_2 \cdot x_3 = a^2$ .
We can then subtract twice our second equation to get $x_1^2+x_2^2+x_3^2 = a^2-2 \cdot \frac{a^2-81}{2}$ .
Simplifying the right side:
\begin{align*} a^2-2 \cdot \frac{a^2-81}{2} &= a^2-a^2+81\\ &= 81.\\ \end{align*}
So, we know $x_1^2+x_2^2+x_3^2 = 81$ .
We can then list out all the triples of positive integers whose squares sum to $81$ :
We get $(1, 4, 8)$ , $(3, 6, 6)$ , and $(4, 4, 7)$ .
These triples give $a$ values of $13$ , $15$ , and $15$ , respectively, and $c$ values of $64$ , $216$ , and $224$ , respectively.
We know that Jon still found two possible values of $c$ when Steve told him the $a$ value, so the $a$ value must be $15$ . Thus, the two $c$ values are $216$ and $224$ , which sum to $\boxed{\text{440}}$ .
~BealsConjecture~

## Solution 2 (Algebra + Brute Force)
First things first. Vietas gives us the following:
\begin{align} x_1+x_2+x_3 = a\\ x_1 \cdot x_2+x_1 \cdot x_3+x_2 \cdot x_3 = \frac{a^2-81}{2}\\ x_1 \cdot x_2 \cdot x_3 = \frac{c}{2} \end{align}
From $(2)$ , $a$ must have odd parity, meaning $a^2-81$ must be a multiple of $4$ , which implies that both sides of $(2)$ are even. Then, from $(1)$ , we see that an odd number of $x_1$ , $x_2$ , and $x_3$ must be odd, because we have already deduced that $a$ is odd. In order for both sides of $(2)$ to be even, there must only be one odd number and two even numbers.
Now, the theoretical maximum value of the left side of $(2)$ is $3 \cdot \biggl(\frac{a}{3}\biggr)^2=\frac{a^2}{3}$ . That means that the maximum bound of $a$ is where \[\frac{a^2}{3} > \frac{a^2-81}{2},\] which simplifies to $\sqrt{243} > a$ , meaning \[16 > a.\] So now we have that $9<a$ from $(2)$ , $a<16$ , and $a$ is odd from $(2)$ . This means that $a$ could equal $11$ , $13$ , or $15$ . At this point, we have simplified the problem to the point where we can casework+ brute force. As said above, we arrive at our solutions of $(1, 4, 8)$ , $(3, 6, 6)$ , and $(4, 4, 7)$ , of which the last two return equal $a$ values. Then, $2(3 \cdot 6 \cdot 6+4 \cdot 4 \cdot 7)=\boxed{440}$ AWD.

## Solution 3 (Basic calculus)
Since each of the roots is positive, the local maximum of the function must occur at a positive value of $x$ . Taking $\frac{d}{dx}$ of the polynomial yields $6x^2-4ax+a^2-81$ , which is equal to $0$ at the local maximum. Since this is a quadratic in $a$ , we can find an expression for $a$ in terms of $x$ . The quadratic formula gives $a=\frac{4x\pm\sqrt{324-8x^2}}{2}$ , which simplifies to $a=2x\pm\sqrt{81-2x^2}$ . We know that $a$ is a positive integer, and testing small positive integer values of $x$ yields $a=15$ or $a=1$ when $x=4$ , and $a=15$ or $a=9$ when $x=6$ . Because the value of $a$ alone does not determine the polynomial, $a$ , $a$ must equal $15$ .
Now our polynomial equals $2x^3-30x^2+144x-c$ . Because one root is less than (or equal to) the $x$ value at the local maximum (picture the graph of a cubic equation), it suffices to synthetically divide by small integer values of $x$ to see if the resulting quadratic also has positive integer roots. Dividing by $x=3$ leaves a quotient of $2x^2-24x+72=2(x-6)^2$ , and dividing by $x=4$ leaves a quotient of $2x^2-22x+56=2(x-4)(x-7)$ . Thus, $c=2\cdot 3\cdot 6\cdot 6=216$ , or $c=2\cdot 4\cdot 4\cdot 7=224$ . Our answer is $216+224=\boxed{440}$ ~bad_at_mathcounts

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=427s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .