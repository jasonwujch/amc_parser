# 2002 AMC 12P Problem 14

## Problem

Find $i + 2i^2 +3i^3 + ... + 2002i^{2002}.$

$\text{(A) }-999 + 1002i \qquad \text{(B) }-1002 + 999i \qquad \text{(C) }-1001 + 1000i \qquad \text{(D) }-1002 + 1001i \qquad \text{(E) }i$

## Solution 1
Note that $i^4 = 1$ , so $i^n = i^{4m+n}$ for all integers $m$ and $n$ . In particular, $i = 1$ , $i^2 = -1$ , and $i^3 = -i$ . We group the positive and negative real terms together and group the positive and negative imaginary parts together.
The positive real terms have exponents on $i$ that are multiples of 4. Therefore, the positive real part evaluates to \[4 + 8 + ... + 2000\] The negative real terms have exponents on $i$ that are of the form $4k + 2$ for integers $k$ . Therefore, the negative real part evaluates to \[-(2 + 6 + ... + 2002)\] The positive imaginary terms have exponents on $i$ that are of the form $4k + 1$ for integers $k$ . Therefore, the negative real part evaluates to \[(1 + 5 + ... + 2001)i\] The negative imaginary terms have exponents on $i$ that are of the form $4k + 3$ for integers $k$ . Therefore, the negative real part evaluates to \[-(3 + 7 + ... + 1999)i\]
Putting everything together, we have \[i + 2i^2 + ... + 2002i^{2002} = (-2 + 4 - 6 + 8 - ... + 2000 - 2002) + (1 - 3 + 5 - 7 + ... - 1999 + 2001)i\]
Group every 2 consecutive terms as shown below \[((-2 + 4)+(-6 + 8) + ... + (-1998 + 2000)-2002) + ((1 - 3)+(5 - 7) + ... + (1997 - 1999) + 2001)i\]
Now we evaluate each small bracket with 2 terms. We get $500(2) = 1000$ in the real part and $500(-2) = -1000$ in the imaginary part. Therefore, the sum becomes $(1000 - 2002) + (-1000 + 2001)i = \boxed {\text{(D) }-1002 + 1001i}$ .
Note: This problem is similar to 2009 AMC 12A Problem 15
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .