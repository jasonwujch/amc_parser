# 2024 AIME II Problem 13

## Problem

Let $\omega\neq 1$ be a $13$ th root of unity. Find the remainder when \[\prod_{k=0}^{12}(2-2\omega^k+\omega^{2k})\] is divided by $1000$ .

## Solution 1
\[\prod_{k=0}^{12} \left(2- 2\omega^k + \omega^{2k}\right) = \prod_{k=0}^{12} \left((1 - \omega^k)^2 + 1\right) = \prod_{k=0}^{12} \left((1 + i) - \omega^k)((1 - i) - \omega^k\right)\]
Now, we consider the polynomial $x^{13} - 1$ whose roots are the 13th roots of unity. Taking our rewritten product from $0$ to $12$ , we see that both instances of $\omega^k$ cycle through each of the 13th roots. Then, our answer is:
\[((1 + i)^{13} - 1)((1 - i)^{13} - 1)\]
\[= (-64(1 + i) - 1)(-64(1 - i) - 1)\]
\[= (65 + 64i)(65 - 64i)\]
\[= 65^2 + 64^2\]
\[= \boxed{\textbf{321}}\]
~Mqnic_

## Solution 2
To find $\prod_{k=0}^{12} (2 - 2w^k + w^{2k})$ , where $w\neq1$ and $w^{13}=1$ , rewrite this is as
$(r-w)(s-w)(r-w^2)(s-w^2)...(r-w^{12})(s-w^{12})$ where $r$ and $s$ are the roots of the quadratic $x^2-2x+2=0$ .
Grouping the $r$ 's and $s$ 's results in $\frac{r^{13}-1}{r-1} \cdot\frac{s^{13}-1}{s-1}$ (note that this is because the equations have the same roots and the same leading coefficients.
the denominator is $(r-1)(s-1)=1$ by vietas.
the numerator $(rs)^{13} - (r^{13} + s^{13}) + 1 = 2^{13} - (-128) + 1= 8321$ by Newton's sums OR finding and expanding the roots
so the answer is $\boxed{321}$
~resources

## Solution 3
Denote $r_j = e^{\frac{i 2 \pi j}{13}}$ for $j \in \left\{ 0, 1, \cdots , 12 \right\}$ .
Thus, for $\omega \neq 1$ , $\left( \omega^0, \omega^1, \cdots, \omega^{12} \right)$ is a permutation of $\left( r_0, r_1, \cdots, r_{12} \right)$ .
We have \begin{align*}\ \Pi_{k = 0}^{12} \left( 2 - 2 \omega^k + \omega^{2k} \right) & = \Pi_{k=0}^{12} \left( 1 + i - \omega^k \right) \left( 1 - i - \omega^k \right) \\ & = \Pi_{k=0}^{12} \left( \sqrt{2} e^{i \frac{\pi}{4}} - \omega^k \right) \left( \sqrt{2} e^{-i \frac{\pi}{4}} - \omega^k \right) \\ & = \Pi_{k=0}^{12} \left( \sqrt{2} e^{i \frac{\pi}{4}} - r_k \right) \left( \sqrt{2} e^{-i \frac{\pi}{4}} - r_k \right) \\ & = \left( \Pi_{k=0}^{12} \left( \sqrt{2} e^{i \frac{\pi}{4}} - r_k \right) \right) \left( \Pi_{k=0}^{12} \left( \sqrt{2} e^{-i \frac{\pi}{4}} - r_k \right) \right) . \hspace{1cm} (1) \end{align*} The third equality follows from the above permutation property.
Note that $r_0, r_1, \cdots , r_{12}$ are all zeros of the polynomial $z^{13} - 1$ . Thus, \[ z^{13} - 1 = \Pi_{k=0}^{12} \left( z - r_k \right) . \]
Plugging this into Equation (1), we get \begin{align*} (1) & = \left( \left( \sqrt{2} e^{i \frac{\pi}{4}} \right)^{13} - 1 \right) \left( \left( \sqrt{2} e^{-i \frac{\pi}{4}} \right)^{13} - 1 \right) \\ & = \left( - 2^{13/2} e^{i \frac{\pi}{4}} - 1 \right) \left( - 2^{13/2} e^{-i \frac{\pi}{4}} - 1 \right) \\ & = 2^{13} + 1 + 2^{13/2} \cdot 2 \cos \frac{\pi}{4} \\ & = 2^{13} + 1 + 2^7 \\ & = 8321 . \end{align*}
Therefore, the answer is $\boxed{\textbf{(321) }}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4
Since $\omega \ne 1$ is a $13^\text{th}$ root of unity, and $13$ is a prime, we have \[f(z) \coloneqq z^{13} - 1 = \prod_{k = 0}^{12}(z - \omega^k)\] by the Fundamental Theorem of Algebra. Next, observe that the quadratic $2 - 2z + z^2$ factors as \[2 - 2z + z^2 = (1 - i - z)(1 + i - z).\] Take the product of the above identity over $z \in \{1, \omega, \omega^2, \dots, \omega^{12} \}$ to get the product of interest \begin{align*} P &:= \prod_{k = 0}^{12}(2 - 2\omega^k + \omega^{2k}) \\ &= \prod_{k = 0}^{12}(1 - i - \omega^k) \cdot \prod_{k = 0}^{12}(1 + i - \omega^k) \\ &= f(1-i) \cdot f(1+i) \\ &= \overline{f(1+i)} \cdot f(1+i) \\ P &= \big| f(1+i) \big|^2. \end{align*} (Here, we use the fact that $f(\overline{z}) = \overline{f(z)}$ whenever $f(z)$ is a polynomial of real coefficients.) Next, notice that \[(1+i)^{13} = (1+i)(1+i)^{12} = (1+i)\big( (1+i)^2 \big)^6 = (1+i)(2i)^6 = -64 - 64i\] which means $f(1+i) = (1+i)^{13} - 1 = -65 - 64i$ . So \[P = \big| f(1+i) \big|^2 = \big| -65 - 64i \big|^2 = 65^2 + 64^2 = 8321 \equiv \boxed{321} \pmod{1000}.\] And we are done. Alternatively, to add some geometric flavor, we can also compute $\big| f(1+i) \big|^2 = \big| (1+i)^{13} - 1 \big|^2$ by law of cosines.
-- VensL.

## Video Solution
https://youtu.be/aSD8Xz0dAI8?si=PUDeOrRg-0bVXNpp
~MathProblemSolvingSkills.com

## Video Solution
https://youtu.be/CtIdbP4F28Q
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .