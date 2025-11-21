# 2000 AIME II Problem 15

## Problem

Find the least positive integer $n$ such that

## Solution 1
We apply the identity
\begin{align*} \frac{1}{\sin n \sin (n+1)} &= \frac{1}{\sin 1} \cdot \frac{\sin (n+1) \cos n - \sin n \cos (n+1)}{\sin n \sin (n+1)} \\ &= \frac{1}{\sin 1} \cdot \left(\frac{\cos n}{\sin n} - \frac{\cos (n+1)}{\sin (n+1)}\right) \\ &= \frac{1}{\sin 1} \cdot \left(\cot n - \cot (n+1)\right). \end{align*}
The motivation for this identity arises from the need to decompose those fractions, possibly into telescoping .
Thus our summation becomes
\[\sum_{k=23}^{67} \frac{1}{\sin (2k-1) \sin 2k} = \frac{1}{\sin 1} \left(\cot 45 - \cot 46 + \cot 47 - \cdots + \cot 133 - \cot 134 \right).\]
Since $\cot (180 - x) = - \cot x$ , the summation simply reduces to $\frac{1}{\sin 1} \cdot \left( \cot 45 - \cot 90 \right) = \frac{1 - 0}{\sin 1} = \frac{1}{\sin 1^{\circ}}$ . Therefore, the answer is $\boxed{001}$ .

## Solution 2
We can make an approximation by observing the following points:
The average term is around the 60's which gives $\frac{4}{3}$ .
There are 45 terms, so the approximate sum is 60.
Therefore, $\sin(n^\circ)$ equals approximately $\frac{1}{60}$ .
Recall that the approximation of $\sin(x)$ in radians is x if x is close to zero. In this case x is close to zero. Converting to radians we see that $\sin(1)$ in degrees is about sin $\frac{1}{57}$ in radians, or is about $\frac{1}{57}$ because of the approximation. What we want is apparently close to that so we make the guess that n is equal to 1 degree. Basically, it boils down to the approximation of $\sin(1)=\frac{1}{60}$ in degrees, convert to radians and use the small angle approximation $\sin(x)=x$ .
~edited for clarity by fermat_sLastAMC

## Solution 3 (Alternate Finish)
Let S be the sum of the sequence. We begin the same as in Solution 1 to get $S\sin(1)=\cot(45)-\cot(46)+\cot(47)-\cot(48)+...+\cot(133)-\cot(134)$ . Observe that this "almost telescopes," if only we had some extra terms. Consider adding the sequence $\frac{1}{\sin(46)\sin(47)}+\frac{1}{\sin(48)\sin(49)}+...+\frac{1}{\sin(134)\sin(135)}$ . By the identity $\sin(x)=\sin(180-x)$ , this sequence is equal to the original one, simply written backwards. By the same logic as before, we may rewrite this sequence as $S\sin(1)=\cot(46)-\cot(47)+\cot(48)-\cot(49)+...+\cot(134)-\cot(135)$ , and when we add the two sequences, they telescope to give $2S\sin(1)=\cot(45)-\cot(135)=2$ . Hence, $S=\frac{1}{\sin(1^\circ)}$ , and our angle is $\boxed{001}$ .
~keeper1098

## Solution 4
First, multiply $\sin n^{\circ}$ on both sides. \begin{align*} \frac{\sin n^\circ}{\sin m^\circ \sin (m+1)^\circ} &= \frac{\sin (k+n-k)^\circ}{\sin m^\circ \sin (m+1)^\circ} \\ &= \frac{\sin (k+n)^\circ \cos k^\circ - \sin k^\circ \cos (k+n)^\circ}{\sin m^\circ \sin (m+1)^\circ} \end{align*} Let $k = m$ since $k$ is could be any number. \begin{align*} &\quad \ \frac{\sin (k+n)^\circ \cos k^\circ}{\sin m^\circ \sin (m+1)^\circ} - \frac{\sin k^\circ \cos (k+n)^\circ}{\sin m^\circ \sin (m+1)^\circ} \\[0.5em] &=\frac{\sin (m+n)^\circ \cos m^\circ}{\sin m^\circ \sin (m+1)^\circ} - \frac{\sin m^\circ \cos (m+n)^\circ}{\sin m^\circ \sin (m+1)^\circ} \end{align*}
### Lemma
### Proof
\begin{align*} &=\frac{\sin (m+1)^\circ \cos m^\circ}{\sin m^\circ \sin (m+1)^\circ} - \frac{\sin m^\circ \cos (m+1)^\circ}{\sin m^\circ \sin (m+1)^\circ} \\[0.5em] &=\frac{\cos m^\circ}{\sin m^\circ} - \frac{\cos (m+1)^\circ}{\sin (m+1)^\circ} \\[0.5em] &= \cot m^\circ - \cot (m+1)^\circ \end{align*} The sum of all numbers could be written. Moreover, notice that $\cot\alpha + \cot\beta = 0$ if $\alpha + \beta = 180^\circ$ . \begin{align*} &\quad \ \cot 45^\circ - \cot 46^\circ + \cot 47^\circ - \cot 48^\circ + \cdots - \cot 132^\circ + \cot 133^\circ - \cot 134^\circ \\ &= (\cot 45^\circ + \cot 47^\circ + \cdots + \cot 89^\circ + \cot 91^\circ + \dots + \cot 133^\circ) \\ &\qquad\qquad\qquad\qquad\qquad\qquad - (\cot 46^\circ + \dots + \cot 88^\circ + \cot 90^\circ + \cot 92^\circ + \dots + \cot 134^\circ) \\ &= \cot 45^\circ - \cot 90^\circ \\ &= 1 \end{align*} Because $1 = 1$ , the lemma is true.
Q.E.D.
$n$ could be 1. Moreover, there are no smaller positive integer less than 1 to test. Thus, the least positive integer $n$ that satisfies the given condition is $\boxed{001}$ .
~MaPhyCom
These problems are copyrighted © by the Mathematical Association of America.