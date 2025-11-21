# 2013 AIME I Problem 14

## Problem

For $\pi \le \theta < 2\pi$ , let \begin{align*} P &= \frac12\cos\theta - \frac14\sin 2\theta - \frac18\cos 3\theta + \frac{1}{16}\sin 4\theta + \frac{1}{32} \cos 5\theta - \frac{1}{64} \sin 6\theta - \frac{1}{128} \cos 7\theta + \cdots \end{align*} and \begin{align*} Q &= 1 - \frac12\sin\theta -\frac14\cos 2\theta + \frac18 \sin 3\theta + \frac{1}{16}\cos 4\theta - \frac{1}{32}\sin 5\theta - \frac{1}{64}\cos 6\theta +\frac{1}{128}\sin 7\theta + \cdots \end{align*} so that $\frac{P}{Q} = \frac{2\sqrt2}{7}$ . Then $\sin\theta = -\frac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
Noticing the $\sin$ and $\cos$ in both $P$ and $Q,$ we think of the angle addition identities:
\[\sin(a + b) = \sin a \cos b + \cos a \sin b, \cos(a + b) = \cos a \cos b - \sin a \sin b\]
With this in mind, we multiply $P$ by $\sin \theta$ and $Q$ by $\cos \theta$ to try and use some angle addition identities. Indeed, we get \begin{align*} P \sin \theta + Q \cos \theta &= \cos \theta + \dfrac{1}{2}(\cos \theta \sin \theta - \sin \theta \cos \theta) - \dfrac{1}{4}(\sin{2 \theta} \sin \theta + \cos{2 \theta} \cos{\theta}) - \cdots \\ &= \cos \theta - \dfrac{1}{4} \cos \theta + \dfrac{1}{8} \sin{2 \theta} + \dfrac{1}{16} \cos{3 \theta} + \cdots \\ &= \cos \theta - \dfrac{1}{2}P \end{align*} after adding term-by-term. Similar term-by-term adding yields \[P \cos \theta + Q \sin \theta = -2(Q - 1).\] This is a system of equations; rearrange and rewrite to get \[P(1 + 2 \sin \theta) + 2Q \cos \theta = 2 \cos \theta\] and \[P \cos^2 \theta + Q \cos \theta(2 + \sin \theta) = 2 \cos \theta.\] Subtract the two and rearrange to get \[\dfrac{P}{Q} = \dfrac{\cos \theta}{2 + \sin \theta} = \dfrac{2 \sqrt{2}}{7}.\] Then, square both sides and use Pythagorean Identity to get a quadratic in $\sin \theta.$ Factor that quadratic and solve for $\sin \theta = -17/19, 1/3.$ Since we're given $\pi\leq\theta<2\pi,$ $\sin\theta$ is nonpositive. We therefore use the negative solution, and our desired answer is $17 + 19 = \boxed{036}.$

## Solution 2
Use sum to product formulas to rewrite $P$ and $Q$
\[P \sin\theta\ + Q \cos\theta\ = \cos \theta\ - \frac{1}{4}\cos \theta + \frac{1}{8}\sin 2\theta + \frac{1}{16}\cos 3\theta - \frac{1}{32}\sin 4\theta + ...\]
Therefore, \[P \sin \theta - Q \cos \theta = -2P\]
Using \[\frac{P}{Q} = \frac{2\sqrt2}{7}, Q = \frac{7}{2\sqrt2} P\]
Plug in to the previous equation and cancel out the "P" terms to get: \[\sin\theta - \frac{7}{2\sqrt2} \cos\theta = -2\]
Then use the pythagorean identity to solve for $\sin\theta$ , \[\sin\theta = -\frac{17}{19} \implies \boxed{036}\]

## Solution 3
Note that \[e^{i\theta}=\cos(\theta)+i\sin(\theta)\]
Thus, the following identities follow immediately: \[ie^{i\theta}=i(\cos(\theta)+i\sin(\theta))=-\sin(\theta)+i\cos(\theta)\] \[i^2 e^{i\theta}=-e^{i\theta}=-\cos(\theta)-i\sin(\theta)\] \[i^3 e^{i\theta}=\sin(\theta)-i\cos(\theta)\]
Consider, now, the sum $Q+iP$ . It follows fairly immediately that:
\[Q+iP=1+\left(\frac{i}{2}\right)^1e^{i\theta}+\left(\frac{i}{2}\right)^2e^{2i\theta}+\ldots=\frac{1}{1-\frac{i}{2}e^{i\theta}}=\frac{2}{2-ie^{i\theta}}\] \[Q+iP=\frac{2}{2-ie^{i\theta}}=\frac{2}{2-(-\sin(\theta)+i\cos(\theta))}=\frac{2}{(2+\sin(\theta))-i\cos(\theta)}\]
This follows straight from the geometric series formula and simple simplification. We can now multiply the denominator by it's complex conjugate to find:
\[Q+iP=\frac{2}{(2+\sin(\theta))-i\cos(\theta)}\left(\frac{(2+\sin(\theta))+i\cos(\theta)}{(2+\sin(\theta))+i\cos(\theta)}\right)\] \[Q+iP=\frac{2((2+\sin(\theta))+i\cos(\theta))}{(2+\sin(\theta))^2+\cos^2(\theta)}\]
Comparing real and imaginary parts, we find: \[\frac{P}{Q}=\frac{\cos(\theta)}{2+\sin(\theta)}=\frac{2\sqrt{2}}{7}\]
Squaring this equation and letting $\sin^2(\theta)=x$ :
$\frac{P^2}{Q^2}=\frac{\cos^2(\theta)}{4+4\sin(\theta)+\sin^2(\theta)}=\frac{1-x^2}{4+4x+x^2}=\frac{8}{49}$
Clearing denominators and solving for $x$ gives sine as $x=-\frac{17}{19}$ .
$017+019=\boxed{036}$

## Solution 4
A bit similar to Solution 3. We use $\phi = \theta+90^\circ$ because the progression cycles in $P\in (\sin 0\theta,\cos 1\theta,-\sin 2\theta,-\cos 3\theta\dots)$ . So we could rewrite that as $P\in(\sin 0\phi,\sin 1\phi,\sin 2\phi,\sin 3\phi\dots)$ .
Similarly, $Q\in (\cos 0\theta,-\sin 1\theta,-\cos 2\theta,\sin 3\theta\dots)\implies Q\in(\cos 0\phi,\cos 1\phi, \cos 2\phi, \cos 3\phi\dots)$ .
Setting complex $z=q_1+p_1i$ , we get $z=\frac{1}{2}\left(\cos\phi+\sin\phi i\right)$
$(Q,P)=\sum_{n=0}^\infty z^n=\frac{1}{1-z}=\frac{1}{1-\frac{1}{2}\cos\phi-\frac{i}{2}\sin\phi}=\frac{1-0.5\cos\phi+0.5i\sin\phi}{\dots}$ .
The important part is the ratio of the imaginary part $i$ to the real part. To cancel out the imaginary part from the denominator, we must add $0.5i\sin\phi$ to the numerator to make the denominator a difference (or rather a sum) of squares. The denominator does not matter. Only the numerator, because we are trying to find $\frac{P}{Q}=\tan\text{arg}(\Sigma)$ a PROPORTION of values. So denominators would cancel out.
$\frac{P}{Q}=\frac{\text{Re}\Sigma}{\text{Im}\Sigma}=\frac{0.5\sin\phi}{1-0.5\cos\phi}=\frac{\sin\phi}{2-\cos\phi}=\frac{2\sqrt{2}}{7}$ .
Setting $\sin\theta=y$ , we obtain \[\frac{\sqrt{1-y^2}}{2+y}=\frac{2\sqrt{2}}{7}\] \[7\sqrt{1-y^2}=2\sqrt{2}(2+y)\] \[49-49y^2=8y^2+32y+32\] \[57y^2+32y-17=0\rightarrow y=\frac{-32\pm\sqrt{1024+4\cdot 969}}{114}\] \[y=\frac{-32\pm\sqrt{4900}}{114}=\frac{-16\pm 35}{57}\] .
Since $y<0$ because $\pi<\theta<2\pi$ , $y=\sin\theta=-\frac{51}{57}=-\frac{17}{19}$ . Adding up, $17+19=\boxed{036}$ .

## Solution 5 (utterly disgusting)
We notice $\sin\theta=-\frac{i}{2}(e^{i\theta}-e^{-i\theta})$ and $\cos\theta=\frac{1}{2}(e^{i\theta}+e^{-i\theta})$
We observe that both $P$ and $Q$ can be split into $2$ parts, namely the terms which contain the $\cos$ and the terms which contain the $\sin .$
The $\cos$ part of $P$ can be expressed as: \begin{align*}\frac12\cos\theta-\frac18\cos3\theta+\cdots&=\frac14\left(e^{i\theta}\left(1-\frac{e^{i2\theta}}{4}+\cdots\right)+e^{-i\theta}\left(1-\frac{e^{-i2\theta}}{4}+\cdots\right)\right) \\ &= \frac{1}{4}\left(\frac{e^{i\theta}}{1+\frac{1}{4}e^{i2\theta}}+\frac{e^{-i\theta}}{1+\frac{1}{4}e^{-i2\theta}}\right)\\ &= \frac{5(e^{i\theta}+e^{-i\theta})}{17+4e^{i2\theta}+4e^{-i2\theta}}.\end{align*}
Repeating the above process, we find that the $\sin$ part of $P$ is \[\frac{2i(e^{i2\theta}-e^{-i2\theta})}{17+4e^{i2\theta}+4e^{-i2\theta}},\] the $\cos$ part of $Q$ is \[\frac{16+2(e^{i2\theta}+e^{-i2\theta})}{17+4e^{i2\theta}+4e^{-i2\theta}},\] and finally, the $\sin$ part of $Q$ is \[\frac{3i(e^{i\theta}-e^{-i\theta})}{17+4e^{i2\theta}+4e^{-i2\theta}}.\]
Converting back to trigonometric form, we have \begin{align*}\frac{2\sqrt{2}}{7}&=\frac{10\cos{\theta}-4\sin{2\theta}}{16+4\cos{2\theta}-6\sin{\theta}}\\ &=\frac{5\cos{\theta}-2\sin{2\theta}}{8+2\cos{2\theta}-3\sin{\theta}}.\end{align*} Using the $\sin$ double identity and simplifying, we have \[\frac{2\sqrt2}{7}=\frac{\cos{\theta}(5-4\sin{\theta})}{10-4\sin^2{\theta}-3\sin{\theta}}.\] Factoring the denominator, we have \[10-4\sin^2{\theta}-3\sin{\theta}=(5-4\sin\theta)(2+\sin\theta).\] Simplifying \begin{align*}\frac{2\sqrt2}{7}&= \frac{\cos{\theta}(5-4\sin{\theta})}{(5-4\sin\theta)(2+\sin\theta)}\\ &=\frac{\cos\theta}{2+\sin\theta}.\end{align*} We set $\sin\theta$ as $x$ , and by the Pythagorean Identity, we have $57x^2+32x-17=0$ . This factors into $(19x+17)(3x-1)=0$ , which yields the 2 solutions $x=-\frac{17}{19}, x=\frac{1}{3}$ . As $\pi\leq\theta<2\pi$ , the latter root is erroneous, and we are left with $\sin\theta=-\frac{17}{19}$ . Thus, our final answer is $17+19=\boxed{036}$ .
~ASAB

## Solution 6
Follow solution 3, up to the point of using the geometric series formula \[Q+iP=\frac{1}{1+\frac{\sin(\theta)}{2}-\frac{Qi\cos(\theta)}{2}}\]
Moving everything to the other side, and considering only the imaginary part, we get \[Pi+\frac{Pi}{2}\sin\theta-\frac{Qi}{2}\cos\theta = 0\]
We can then write $P = 2 \sqrt{2} k$ , and $Q = 7k$ , ( $k \neq 0$ ). Thus, we can substitute and divide out by k. \[2\sqrt{2}+\sqrt{2}\sin\theta-\frac{7}{2}\cos\theta\ =\ 0\] \[2\sqrt{2}+\sqrt{2}\sin\theta-\frac{7}{2}\sqrt{1-\sin^{2}\theta}=\ 0\] \[2\sqrt{2}+\sqrt{2}\sin\theta\ =\frac{7}{2}\left(\sqrt{1-\sin^{2}\theta}\right)\] \[8+8\sin\theta+2\sin^{2}\theta=\frac{49}{4}-\frac{49}{7}\sin^{2}\theta\] \[\frac{57}{4}\sin^{2}\theta+8\sin\theta-\frac{17}{4} = 0\] \[57\sin^{2}\theta+32\sin\theta-17 = 0\] \[\left(3\sin\theta-1\right)\left(19\sin\theta+17\right) = 0\]
Since $\pi \le \theta < 2\pi$ , we get $\sin \theta < 0$ , and thus, $\sin\theta = \frac{-17}{19} \implies \boxed{036}$
-Alexlikemath

## Video Solution
https://youtu.be/036u51CF-EQ?si=SHTrTwSg3LMnE_yH
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .