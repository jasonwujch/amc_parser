# 2012 AIME II Problem 8

## Problem

The complex numbers $z$ and $w$ satisfy the system \[z + \frac{20i}w = 5+i\] \[w+\frac{12i}z = -4+10i\] Find the smallest possible value of $\vert zw\vert^2$ .

## Solution
Multiplying the two equations together gives us \[zw + 32i - \frac{240}{zw} = -30 + 46i\] and multiplying by $zw$ then gives us a quadratic in $zw$ : \[(zw)^2 + (30-14i)zw - 240 =0.\] Using the quadratic formula, we find the two possible values of $zw$ to be $7i-15 \pm \sqrt{(15-7i)^2 + 240}$ = $6+2i,$ $12i - 36.$ The smallest possible value of $\vert zw\vert^2$ is then obviously $6^2 + 2^2 = \boxed{040}$ .
### Note
A key thing to note here is that $|zw|^2=|z|^2\cdot|w|^2,$ which can be proved as follows:
Proof: Using the values for $z$ and $w$ that we used above, we get:
\begin{align*} |zw|^2&=|(ac-bd)+i(bc+ad)|^2\\ &=(ac-bd)^2+(bc+ad)^2\\ &=a^2c^2+b^2d^2+b^2c^2+a^2d^2-2abcd+2abc\\ &=a^2c^2+b^2d^2+b^2c^2+a^2d^2 \end{align*} Also, $|z|^2=a^2+b^2$ and $|w|^2=c^2+d^2$ . Therefore: \[|z|^2\cdot|w|^2=(a^2+b^2)(c^2+d^2)=a^2c^2+a^2d^2+b^2c^2+b^2d^2\] and our proof is complete.
Now, also note that we found $\sqrt{416-210i}$ by letting $416-210i=(a-bi)^2$ and solving for $a$ and $b$ by considering real and imaginary parts. Then, we substitute that into $a-bi$ which is the value of $\sqrt{416-210i}$ and continue from there.
mathboy282
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .