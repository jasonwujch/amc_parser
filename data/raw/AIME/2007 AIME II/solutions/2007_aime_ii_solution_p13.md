# 2007 AIME II Problem 13

## Problem

A triangular array of squares has one square in the first row, two in the second, and in general, $k$ squares in the $k$ th row for $1 \leq k \leq 11.$ With the exception of the bottom row, each square rests on two squares in the row immediately below (illustrated in the given diagram). In each square of the eleventh row, a $0$ or a $1$ is placed. Numbers are then placed into the other squares, with the entry for each square being the sum of the entries in the two squares below it. For how many initial distributions of $0$ 's and $1$ 's in the bottom row is the number in the top square a multiple of $3$ ?

[asy] for (int i=0; i<12; ++i){ for (int j=0; j<i; ++j){ //dot((-j+i/2,-i)); draw((-j+i/2,-i)--(-j+i/2+1,-i)--(-j+i/2+1,-i+1)--(-j+i/2,-i+1)--cycle); } } [/asy]

## Solution
Label each of the bottom squares as $x_0, x_1 \ldots x_9, x_{10}$ .
Through induction , we can find that the top square is equal to ${10\choose0}x_0 + {10\choose1}x_1 + {10\choose2}x_2 + \ldots {10\choose10}x_{10}$ . (This also makes sense based on a combinatorial argument: the number of ways a number can "travel" to the top position going only up is equal to the number of times it will be counted in the final sum.)
Examine the equation $\mod 3$ . All of the coefficients from $x_2 \ldots x_8$ will be multiples of $3$ (since the numerator will have a $9$ ). Thus, the expression boils down to $x_0 + 10x_1 + 10x_9 + x_{10} \equiv 0 \mod 3$ . Reduce to find that $x_0 + x_1 + x_9 + x_{10} \equiv 0 \mod 3$ . Out of $x_0,\ x_1,\ x_9,\ x_{10}$ , either all are equal to $0$ , or three of them are equal to $1$ . This gives ${4\choose0} + {4\choose3} = 1 + 4 = 5$ possible combinations of numbers that work.
The seven terms from $x_2 \ldots x_8$ can assume either $0$ or $1$ , giving us $2^7$ possibilities. The answer is therefore $5 \cdot 2^7 = \boxed{640}$ .
### Note
The specific induction process: we want to prove that if the bottom row is $x_0, x_1 \cdots x_{n}$ , the top square is ${n\choose0}x_0 + {n\choose1}x_1 + {n\choose2}x_2 + \ldots {n\choose{n}}x_{n}$ .
Base Case: when n = 1, this is obviously true.
Induction Step: Assume that the statement is true for n, and we wish to prove it for $n + 1$ . Therefore, we add another row below the $n + 1$ row, and name the squares as $a_0, a_1, \cdots a_{n+1}$ . We obtain that $x_0 = a_0 + a_1, x_1 = a_1 + a_2, \cdots x_{n} = a_{n} + a_{n+1}$ , and using the assumption, yield the top square equals ${n\choose0}(a_0 + a_1) + {n\choose1}(a_1 + a_2) + \ldots {n\choose{n}}(a_{n} + a_{n+1})$ . While it's easy to prove that ${n\choose{k}} + {n\choose{k+1}} = {n+1\choose{k+1}}$ (just expand it), we find that the two equations are identical.
Note contributed by MVP_Harry, friend me if you want ~
Assume that the numbers filled in the 11th row is a b c d e f g h i j. Writing the number in each box, you will find that the coefficient of each letter turns out to be a pascal triangle.

## Solution 2
If we label the bottom row of values $a_1,a_2,…,a_11$ then the sum of the bottom row is $a_1+…+a_11$ , the sum of the second row is $a_1+2(a_2+…+a_10)+a_11$ and this pattern continues until the top element is $(a_1+a_11)+2(a_2+a_10)+…+4(a_5+a_7)+5a_6$ . Then, the terms with coefficient 0 mod 3 can be anything, and we do casework on the other solutions mod 3. We get 640. ~joeythetoey
These problems are copyrighted © by the Mathematical Association of America.