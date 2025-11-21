# 2015 AIME I Problem 13

## Problem

With all angles measured in degrees, the product $\prod_{k=1}^{45} \csc^2(2k-1)^\circ=m^n$ , where $m$ and $n$ are integers greater than 1. Find $m+n$ .

## Solution 1
Let $x = \cos 1^\circ + i \sin 1^\circ$ . Then from the identity \[\sin 1 = \frac{x - \frac{1}{x}}{2i} = \frac{x^2 - 1}{2 i x},\] we deduce that (taking absolute values and noticing $|x| = 1$ ) \[|2\sin 1| = |x^2 - 1|.\] But because $\csc$ is the reciprocal of $\sin$ and because $\sin z = \sin (180^\circ - z)$ , if we let our product be $M$ then \[\frac{1}{M} = \sin 1^\circ \sin 3^\circ \sin 5^\circ \dots \sin 177^\circ \sin 179^\circ\] \[= \frac{1}{2^{90}} |x^2 - 1| |x^6 - 1| |x^{10} - 1| \dots |x^{354} - 1| |x^{358} - 1|\] because $\sin$ is positive in the first and second quadrants. Now, notice that $x^2, x^6, x^{10}, \dots, x^{358}$ are the roots of $z^{90} + 1 = 0.$ Hence, we can write $(z - x^2)(z - x^6)\dots (z - x^{358}) = z^{90} + 1$ , and so \[\frac{1}{M} = \dfrac{1}{2^{90}}|1 - x^2| |1 - x^6| \dots |1 - x^{358}| = \dfrac{1}{2^{90}} |1^{90} + 1| = \dfrac{1}{2^{89}}.\] It is easy to see that $M = 2^{89}$ and that our answer is $2 + 89 = \boxed{91}$ .

## Solution 2
Let $p=\sin1\sin3\sin5...\sin89$
\[p=\sqrt{\sin1\sin3\sin5...\sin177\sin179}\]
\[=\sqrt{\frac{\sin1\sin2\sin3\sin4...\sin177\sin178\sin179}{\sin2\sin4\sin6\sin8...\sin176\sin178}}\]
\[=\sqrt{\frac{\sin1\sin2\sin3\sin4...\sin177\sin178\sin179}{(2\sin1\cos1)\cdot(2\sin2\cos2)\cdot(2\sin3\cos3)\cdot....\cdot(2\sin89\cos89)}}\]
\[=\sqrt{\frac{1}{2^{89}}\frac{\sin90\sin91\sin92\sin93...\sin177\sin178\sin179}{\cos1\cos2\cos3\cos4...\cos89}}\]
$=\sqrt{\frac{1}{2^{89}}}$ because of the identity $\sin(90+x)=\cos(x)$
we want $\frac{1}{p^2}=2^{89}$
Thus the answer is $2+89=\boxed{091}$

## Solution 3
Similar to Solution $2$ , so we use $\sin{2\theta}=2\sin\theta\cos\theta$ and we find that: \begin{align*}\sin(4)\sin(8)\sin(12)\sin(16)\cdots\sin(84)\sin(88)&=(2\sin(2)\cos(2))(2\sin(4)\cos(4))(2\sin(6)\cos(6))(2\sin(8)\cos(8))\cdots(2\sin(42)\cos(42))(2\sin(44)\cos(44))\\ &=(2\sin(2)\sin(88))(2\sin(4))\sin(86))(2\sin(6)\sin(84))(2\sin(8)\sin(82))\cdots(2\sin(42)\sin(48))(2\sin(44)\sin(46))\\ &=2^{22}(\sin(2)\sin(88)\sin(4)\sin(86)\sin(6)\sin(84)\sin(8)\sin(82)\cdots\sin(42)\sin(48)\sin(44)\sin(46))\\ &=2^{22}(\sin(2)\sin(4)\sin(6)\sin(8)\cdots\sin(82)\sin(84)\sin(86)\sin(88))\end{align*} Now we can cancel the sines of the multiples of $4$ : \[1=2^{22}(\sin(2)\sin(6)\sin(10)\sin(14)\cdots\sin(82)\sin(86))\] So $\sin(2)\sin(6)\sin(10)\sin(14)\cdots\sin(82)\sin(86)=2^{-22}$ and we can apply the double-angle formula again: \begin{align*}2^{-22}&=(\sin(2)\sin(6)\sin(10)\sin(14)\cdots\sin(82)\sin(86)\\ &=(2\sin(1)\cos(1))(2\sin(3)\cos(3))(2\sin(5)\cos(5))(2\sin(7)\cos(7))\cdots(2\sin(41)\cos(41))(2\sin(43)\cos(43))\\ &=(2\sin(1)\sin(89))(2\sin(3)\sin(87))(2\sin(5)\sin(85))(2\sin(7)\sin(87))\cdots(2\sin(41)\sin(49))(2\sin(43)\sin(47))\\ &=2^{22}(\sin(1)\sin(89)\sin(3)\sin(87)\sin(5)\sin(85)\sin(7)\sin(83)\cdots\sin(41)\sin(49)\sin(43)\sin(47))\\ &=2^{22}(\sin(1)\sin(3)\sin(5)\sin(7)\cdots\sin(41)\sin(43))(\sin(47)\sin(49)\cdots\sin(83)\sin(85)\sin(87)\sin(89))\end{align*} Of course, $\sin(45)=2^{-\frac{1}{2}}$ is missing, so we multiply it to both sides: \[2^{-22}\sin(45)=2^{22}(\sin(1)\sin(3)\sin(5)\sin(7)\cdots\sin(41)\sin(43))(\sin(45))(\sin(47)\sin(49)\cdots\sin(83)\sin(85)\sin(87)\sin(89))\] \[\left(2^{-22}\right)\left(2^{-\frac{1}{2}}\right)=2^{22}(\sin(1)\sin(3)\sin(5)\sin(7)\cdots\sin(83)\sin(85)\sin(87)\sin(89))\] \[2^{-\frac{45}{2}}=2^{22}(\sin(1)\sin(3)\sin(5)\sin(7)\cdots\sin(83)\sin(85)\sin(87)\sin(89))\] Now isolate the product of the sines: \[\sin(1)\sin(3)\sin(5)\sin(7)\cdots\sin(83)\sin(85)\sin(87)\sin(89)=2^{-\frac{89}{2}}\] And the product of the squares of the cosecants as asked for by the problem is the square of the inverse of this number: \[\csc^2(1)\csc^2(3)\csc^2(5)\csc^2(7)\cdots\csc^2(83)\csc^2(85)\csc^2(87)\csc^2(89)=\left(\frac{1}{2^{-\frac{89}{2}}}\right)^2=\left(2^{\frac{89}{2}}\right)^2=2^{89}\] The answer is therefore $m+n=(2)+(89)=\boxed{091}$ .

## Solution 4
Let $p=\prod_{k=1}^{45} \csc^2(2k-1)^\circ$ .
Then, $\sqrt{\frac{1}{p}}=\prod_{k=1}^{45} \sin(2k-1)^\circ$ .
Since $\sin\theta=\cos(90^{\circ}-\theta)$ , we can multiply both sides by $\frac{\sqrt{2}}{2}$ to get $\sqrt{\frac{1}{2p}}=\prod_{k=1}^{23} \sin(2k-1)^\circ\cos(2k-1)^\circ$ .
Using the double-angle identity $\sin2\theta=2\sin\theta\cos\theta$ , we get $\sqrt{\frac{1}{2p}}=\frac{1}{2^{23}}\prod_{k=1}^{23} \sin(4k-2)^\circ$ .
Note that the right-hand side is equal to $\frac{1}{2^{23}}\prod_{k=1}^{45} \sin(2k)^\circ\div \prod_{k=1}^{22} \sin(4k)^\circ$ , which is equal to $\frac{1}{2^{23}}\prod_{k=1}^{45} \sin(2k)^\circ\div \prod_{k=1}^{22} 2\sin(2k)^\circ\cos(2k)^\circ$ , again, from using our double-angle identity.
Putting this back into our equation and simplifying gives us $\sqrt{\frac{1}{2p}}=\frac{1}{2^{45}}\prod_{k=23}^{45} \sin(2k)^\circ\div \prod_{k=1}^{22} \cos(2k)^\circ$ .
Using the fact that $\sin\theta=\cos(90^{\circ}-\theta)$ again, our equation simplifies to $\sqrt{\frac{1}{2p}}=\frac{\sin90^\circ}{2^{45}}$ , and since $\sin90^\circ=1$ , it follows that $2p = 2^{90}$ , which implies $p=2^{89}$ . Thus, $m+n=2+89=\boxed{091}$ .

## Solution 5
Once we have the tools of complex polynomials there is no need to use the tactical tricks. Everything is so basic (I think).
Recall that the roots of $x^n+1$ are $e^{\frac{(2k-1)\pi i}{n}}, k=1,2,...,n$ , we have \[x^n + 1 = \prod_{k=1}^{n}(x-e^{\frac{(2k-1)\pi i}{n}})\] Let $x=1$ , and take absolute value of both sides, \[2 = \prod_{k=1}^{n}|1-e^{\frac{(2k-1)\pi i}{n}}|= 2^n\prod_{k=1}^{n}|\sin\frac{(2k-1)\pi}{2n}|\] or, \[\prod_{k=1}^{n}|\sin\frac{(2k-1)\pi}{2n}| = 2^{-(n-1)}\] Let $n$ be even, then, \[\sin\frac{(2k-1)\pi}{2n} = \sin\left(\pi - \frac{(2k-1)\pi}{2n}\right) = \sin\left(\frac{(2(n-k+1)-1)\pi}{2n}\right)\] so, \[\prod_{k=1}^{n}\left|\sin\frac{(2k-1)\pi}{n}\right| = \prod_{k=1}^{\frac{n}{2}}\sin^2\frac{(2k-1)\pi}{2n}\] Set $n=90$ and we have \[\prod_{k=1}^{45}\sin^2\frac{(2k-1)\pi}{180} = 2^{-89}\] , \[\prod_{k=1}^{45}\csc^2\frac{(2k-1)\pi}{180} = 2^{89}\] -Mathdummy

## Solution 6
Recall that $\sin\alpha\cdot \sin(60^{\circ}-\alpha)\cdot \sin(60^{\circ}+\alpha)=\frac{1}{4}\cdot \sin3\alpha$ Since it is in csc, we can write in sin and then take reciprocal. We can group them by threes, $P=(\sin1^{\circ}\cdot \sin59^{\circ}\cdot \sin61^{\circ})\cdots(\sin29^{\circ}\cdot \sin31^{\circ}\cdot \sin89^{\circ})$ . Thus \begin{align*} P &=\frac{1}{4^{15}}\cdot \sin3^{\circ}\cdot \sin9^{\circ}\cdots\sin87^{\circ}\\ &=\frac{1}{4^{20}}\cdot \sin9^{\circ}\cdot \sin27^{\circ}\cdot \sin45^{\circ}\cdot \sin63^{\circ}\cdot \sin81^{\circ}\\ &=\frac{1}{4^{20}}\cdot \frac{\sqrt{2}}{2}\cdot \sin9^{\circ}\cdot \cos9^{\circ}\cdot \sin27^{\circ}\cdot \cos27^{\circ}\\ &=\frac{1}{4^{21}}\cdot \frac{\sqrt{2}}{2}\cdot \sin18^{\circ}\cdot \cos36^{\circ}=\frac{\sqrt{2}}{2^{45}} \end{align*} So we take reciprocal, $\frac 1P=2^{\frac{89}{2}}$ , the desired answer is $\frac{1}{P^2}=2^{89}$ leads to answer $\boxed{091}$
~bluesoul

## Solution 7
We have
\[\prod_{k=1}^{45} \csc^2(2k-1)^\circ = \left(\frac{1}{\sin1^\circ \cdot \sin3^\circ \cdots \sin89^\circ}\right)^2.\]
Multiplying by $\frac{\sin2^\circ \cdot \sin4^\circ \cdots \sin88^\circ}{\sin2^\circ \cdot \sin4^\circ \cdots \sin88^\circ}$ gives
\[\left(\frac{\sin2^\circ \cdot \sin4^\circ \cdots \sin88^\circ}{\sin1^\circ \sin2^\circ \cdot \sin3^\circ \cdots \sin88^\circ \cdot \sin89^\circ}\right)^2\]
\[= \left(\frac{\sin2^\circ \cdot \sin4^\circ \cdots \sin88^\circ}{\sin1^\circ \sin2^\circ \cdot \sin3^\circ \cdots \sin 45^\circ \cdot \cos 44^\circ \cdot \cos 43^\circ \cdots \cos1^\circ}\right)^2.\]
Using $\sin\alpha \cos\alpha = \frac{1}{2}\sin{2\alpha}$ gives
\[\left(\frac{\sin2^\circ \cdot \sin4^\circ \cdots \sin88^\circ}{\frac{1}{2} \sin2^\circ \cdot \frac{1}{2} \sin4^\circ \cdots \frac{1}{2} \sin88^\circ \cdot \sin45^\circ}\right) ^2\]
\[= \left(\frac{1}{(\frac{1}{2})^{44} \cdot \frac{\sqrt{2}}{2}}\right)^2\]
\[= 2^{89}.\]
Thus, the answer is $2+89 = \boxed{091}.$

## Solution 8
Consider the product $\prod_{k=1}^{45} \csc^2(2k-1) = \prod_{k=45}^{1} \sec^2(2k-1) = \prod_{k=1}^{45} \sec^2(2k-1) = \prod_{k=1}^{45} (1+\tan^2(2k-1))$ However, note that the $45$ numbers in the form $\sqrt{\tan^2(2k-1)} = \tan(2k-1)$ for $1\le{k}\le{45}$ are precisely the roots of the equation $\frac{1}{\tan{(\tan^{-1}{90x}})} = 0$ . Thus, it suffices to find $|P(-1)|$ , where $P$ is the polynomial formed by the denominator of $\tan{(\tan^{-1}{90\sqrt{x}})}$ . This is true because $\prod_{k=1}^{45} (x-\tan^2(2k-1)) = \prod_{k=1}^{45} -(-x+\tan^2(2k-1))$ gives us the factored root form of the equation where $P$ is undefined, which corresponds to the equation where the denominator equals $0$ .
It remains to find the denominator of $P$ ; fortunately, we may use tangent angle multiplication rules. Specifically, the denominator of $P$ will be $\sum_{n=0} ^{45} (-1)^n\binom{90}{2n}\sqrt{x}^{2n} = \sum_{n=0} ^{45} (-1)^n\binom{90}{2n}x^n$ . Evaluating at $x = -1$ , we may obtain the sum $\sum_{n=0} ^{45} (-1)^n\binom{90}{2n}(-1)^{n} = \sum_{n=0} ^{45} \binom{90}{2n}$ .
From here, there are two ways to finish; the first is to recognize the well known sum $\sum_{n=0} ^{k} \binom{2k}{2n} = 2^(2k-1)$ , from which we may plug in $k = 45$ to see $|P(-1)| = 2^(45*2-1) = 2^{89}$ to obtain the answer of $2+89=\boxed{091}$ . Otherwise, you may split the previous sum; $\sum_{n=0} ^{45} \binom{90}{2n} = \sum_{n=0} ^{45} \binom{89}{2n-1} + \binom{89}{2n} = \sum_{n=0} ^{89} \binom{89}{n} = 2^{89}$ , which also gives the correct answer. $\blacksquare$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .