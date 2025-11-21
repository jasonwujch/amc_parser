# 2008 AIME I Problem 8

## Problem

Find the positive integer $n$ such that

\[\arctan\frac {1}{3} + \arctan\frac {1}{4} + \arctan\frac {1}{5} + \arctan\frac {1}{n} = \frac {\pi}{4}.\]

## Solution 1
Since we are dealing with acute angles, $\tan(\arctan{a}) = a$ .
Note that $\tan(\arctan{a} + \arctan{b}) = \dfrac{a + b}{1 - ab}$ , by tangent addition. Thus, $\arctan{a} + \arctan{b} = \arctan{\dfrac{a + b}{1 - ab}}$ .
Applying this to the first two terms, we get $\arctan{\dfrac{1}{3}} + \arctan{\dfrac{1}{4}} = \arctan{\dfrac{7}{11}}$ .
Now, $\arctan{\dfrac{7}{11}} + \arctan{\dfrac{1}{5}} = \arctan{\dfrac{23}{24}}$ .
We now have $\arctan{\dfrac{23}{24}} + \arctan{\dfrac{1}{n}} = \dfrac{\pi}{4} = \arctan{1}$ . Thus, $\dfrac{\dfrac{23}{24} + \dfrac{1}{n}}{1 - \dfrac{23}{24n}} = 1$ ; and simplifying, $23n + 24 = 24n - 23 \Longrightarrow n = \boxed{47}$ .

## Solution 2 (generalization)
From the expansion of $e^{iA}e^{iB}e^{iC}e^{iD}$ , we can see that \[\cos(A + B + C + D) = \cos A \cos B \cos C \cos D - \tfrac{1}{4} \sum_{\rm sym} \sin A \sin B \cos C \cos D + \sin A \sin B \sin C \sin D,\] and \[\sin(A + B + C + D) = \sum_{\rm cyc}\sin A \cos B \cos C \cos D - \sum_{\rm cyc} \sin A \sin B \sin C \cos D .\] If we divide both of these by $\cos A \cos B \cos C \cos D$ , then we have \[\tan(A + B + C + D) = \frac {1 - \sum \tan A \tan B + \tan A \tan B \tan C \tan D}{\sum \tan A - \sum \tan A \tan B \tan C},\] which makes for more direct, less error-prone computations. Substitution gives the desired answer.

## Solution 3: Complex Numbers
Adding a series of angles is the same as multiplying the complex numbers whose arguments they are. In general, $\arctan\frac{1}{n}$ , is the argument of $n+i$ . The sum of these angles is then just the argument of the product \[(3+i)(4+i)(5+i)(n+i)\] and expansion give us $(48n-46)+(48+46n)i$ . Since the argument of this complex number is $\frac{\pi}{4}$ , its real and imaginary parts must be equal; then, we can we set them equal to get \[48n - 46 = 48 + 46n.\] Therefore, $n=\boxed{47}$ .

## Solution 4 Sketch
You could always just bash out $\sin(a+b+c)$ (where a,b,c,n are the angles of the triangles respectively) using the sum identities again and again until you get a pretty ugly radical and use a triangle to get $\cos(a+b+c)$ and from there you use a sum identity again to get $\sin(a+b+c+n)$ and using what we found earlier you can find $\tan(n)$ by division that gets us $\frac{23}{24}$
~YBSuburbanTea
These problems are copyrighted © by the Mathematical Association of America.