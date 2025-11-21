# 2019 AMC 10A Problem 11

## Problem

How many positive integer divisors of $201^9$ are perfect squares or perfect cubes (or both)? $\textbf{(A) }32 \qquad \textbf{(B) }36 \qquad \textbf{(C) }37 \qquad \textbf{(D) }39 \qquad \textbf{(E) }41$

## Solution 1 (PIE)
Prime factorizing $201^9$ , we get $3^9\cdot67^9$ . A perfect square must have even powers of its prime factors, so our possible choices for our exponents to get a perfect square are $0, 2, 4, 6, 8$ for both $3$ and $67$ . This yields $5\cdot5 = 25$ perfect squares.
Perfect cubes must have multiples of $3$ for each of their prime factors' exponents, so we have either $0, 3, 6$ , or $9$ for both $3$ and $67$ , which yields $4\cdot4 = 16$ perfect cubes, for a total of $25+16 = 41$ .
Subtracting the overcounted powers of $6$ ( $3^0\cdot67^0$ , $3^0\cdot67^6$ , $3^6\cdot67^0$ , and $3^6\cdot67^6$ ), we get $41-4 = \boxed{\textbf{(C) }37}$ .
~ Continuous_Pi

## Solution 2
Observe that $201 = 67 \cdot 3$ . Now divide into cases:
Case 1 : The factor is $3^n$ . Then we can have $n = 2$ , $3$ , $4$ , $6$ , $8$ , or $9$ .
Case 2 : The factor is $67^n$ . This is the same as Case 1.
Case 3 : The factor is some combination of $3$ s and $67$ s.
This would be easy if we could just have any combination, as that would simply give $6 \cdot 6$ . However, we must pair the numbers that generate squares with the numbers that generate squares and the same for cubes. In simpler terms, let's organize our values for $n$ .
$n = 2$ is a "square" because it would give a factor of this number that is a perfect square. More generally, it is even.
$n = 3$ is a "cube" because it would give a factor of this number that is a perfect cube. More generally, it is a multiple of $3$ .
$n = 4$ is a "square".
$n = 6$ is interesting, since it's both a "square" and a "cube". Don't count this as either because this would double-count, so we will count this in another case.
$n = 8$ is a "square"
$n = 9$ is a "cube".
Now let's consider subcases:
Subcase 1 : The squares are with each other.
Since we have $3$ square terms, and they would pair with $3$ other square terms, we get $3 \cdot 3 = 9$ possibilities.
Subcase 2 : The cubes are with each other.
Since we have $2$ cube terms, and they would pair with $2$ other cube terms, we get $2 \cdot 2 = 4$ possibilities.
Subcase 3 : A number pairs with $n=6$ .
Since any number can pair with $n=6$ (as it gives both a square and a cube), there would be $6$ possibilities. Remember however that there can be two different bases ( $3$ and $67$ ), and they would produce different results. Thus, there are in fact $6 \cdot 2 = 12$ possibilities.
Finally, summing the cases gives $6+6+9+4+12 = \boxed{\textbf{(C) }37}$ .

## Solution 3 (A Little Long)
Notice that $201=3 \cdot 67$ . We factorize $201^9$ to get $3^9 \cdot 67^9$ . We then list perfect squares and cubes. $3^2$ , $3^4$ , $3^6$ , $3^8$ . $3^3$ , $3^6$ , $3^9$ . $67^2$ , $67^4$ , $67^6$ , $67^8$ . $67^3$ , $67^6$ , $67^9$ . Notice that the powers of $6$ overlap. We must not forget $1$ though. Of course, all of these factors already work. This gives us $15-2=3$ . Next, we count the perfect squares. Since there are $4$ options we have $4 \cdot 4=16$ . We do the same for the perfect cubes except with 3 options this time, and we have $3 \cdot 3=9$ . However, we accidentally overcounted $3^6 \cdot 67^6$ . We add our answers and subtract $1$ to get $13+16+9-1 = \boxed{\textbf{(C) }37}$
~ PerseverePlayer

## Video Solution
https://youtu.be/JR1LpMc3Ntg
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/ZhAZ1oPe5Ds?t=2402
~ pi_is_3.14

## Video Solution
https://youtu.be/XZiO19KNiYA
Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .