# 2022 AIME I Problem 7

## Problem

Let $a,b,c,d,e,f,g,h,i$ be distinct integers from $1$ to $9.$ The minimum possible positive value of \[\dfrac{a \cdot b \cdot c - d \cdot e \cdot f}{g \cdot h \cdot i}\] can be written as $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1 (Optimization)
To minimize a positive fraction, we minimize its numerator and maximize its denominator. It is clear that $\frac{a \cdot b \cdot c - d \cdot e \cdot f}{g \cdot h \cdot i} \geq \frac{1}{7\cdot8\cdot9}.$
If we minimize the numerator, then $a \cdot b \cdot c - d \cdot e \cdot f = 1.$ Note that $a \cdot b \cdot c \cdot d \cdot e \cdot f = (a \cdot b \cdot c) \cdot (a \cdot b \cdot c - 1) \geq 6! = 720,$ so $a \cdot b \cdot c \geq 28.$ It follows that $a \cdot b \cdot c$ and $d \cdot e \cdot f$ are consecutive composites with prime factors no other than $2,3,5,$ and $7.$ The smallest values for $a \cdot b \cdot c$ and $d \cdot e \cdot f$ are $36$ and $35,$ respectively. So, we have $\{a,b,c\} = \{2,3,6\}, \{d,e,f\} = \{1,5,7\},$ and $\{g,h,i\} = \{4,8,9\},$ from which $\frac{a \cdot b \cdot c - d \cdot e \cdot f}{g \cdot h \cdot i} = \frac{1}{288}.$
If we do not minimize the numerator, then $a \cdot b \cdot c - d \cdot e \cdot f > 1.$ Note that $\frac{a \cdot b \cdot c - d \cdot e \cdot f}{g \cdot h \cdot i} \geq \frac{2}{7\cdot8\cdot9} > \frac{1}{288}.$
Together, we conclude that the minimum possible positive value of $\frac{a \cdot b \cdot c - d \cdot e \cdot f}{g \cdot h \cdot i}$ is $\frac{1}{288}.$ Therefore, the answer is $1+288=\boxed{289}.$
~MRENTHUSIASM ~jgplay

## Solution 2 (Bash)
Obviously, to find the correct answer, we need to get the largest denominator with the smallest numerator.
To bash efficiently, we can start out with $7\cdot8\cdot9$ as our denominator. This, however, leaves us with the numbers $1, 2, 3, 4, 5,$ and $6$ left. The smallest we can make out of this is $1\cdot5\cdot6 - 2\cdot3\cdot4 = 30 - 24 = 6$ . When simplified, it gives us $\frac{1}{84}$ , which gives a small answer of $85$ . Obviously there are larger answers than this.
After the first bash, we learn to bash even more efficiently, we can consider both the numerator and the denominator when guessing. We know the numerator has to be extremely small while still having a large denominator. When bashing, we soon find out the couple $(a,b,c)=(2,3,6)$ and $(d,e,f)=(1,5,7)$ .
This gives us a numerator of $36-35=1$ , which is by far the smallest yet. With the remaining numbers $4, 8,$ and $9$ , we get $\frac{36-35}{4\cdot8\cdot9}=\frac{1}{288}$ .
Finally, we add up our numerator and denominator: The answer is $1+288=\boxed{289}$ .
~ orenbad

## Solution 3 (Educated Trial and Error)
To minimize the numerator, we must have $abc - def = 1$ . Thus, one of these products must be odd and the other must be even. The odd product must consist of only odd numbers. The smallest such value $(d, e, f) = (1, 3, 5)$ cannot result in a difference of $1$ , and the next smallest product, $(d, e, f) = (1, 3, 7)$ cannot either, but $(d, e, f) = (1, 5, 7)$ can if $(a, b, c) = (2, 3, 6)$ . Thus, the denominator must be $(g, h, i) = (4, 8, 9)$ , and the smallest fraction possible is $\dfrac{36 - 35}{288} = \dfrac{1}{288}$ , making the answer $1 + 288 = \boxed{289}$ .
~ A_MatheMagician
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .