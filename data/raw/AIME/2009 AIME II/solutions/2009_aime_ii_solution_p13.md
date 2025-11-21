# 2009 AIME II Problem 13

## Problem

Let $A$ and $B$ be the endpoints of a semicircular arc of radius $2$ . The arc is divided into seven congruent arcs by six equally spaced points $C_1$ , $C_2$ , $\dots$ , $C_6$ . All chords of the form $\overline {AC_i}$ or $\overline {BC_i}$ are drawn. Let $n$ be the product of the lengths of these twelve chords. Find the remainder when $n$ is divided by $1000$ .

## Solution

## Solution 1
Let the radius be 1 instead. All lengths will be halved so we will multiply by $2^{12}$ at the end. Place the semicircle on the complex plane, with the center of the circle being 0 and the diameter being the real axis. Then $C_1,\ldots, C_6$ are 6 of the 14th roots of unity. Let $\omega=\text{cis}\frac{360^{\circ}}{14}$ ; then $C_1,\ldots, C_6$ correspond to $\omega,\ldots, \omega^6$ . Let $C_1',\ldots, C_6'$ be their reflections across the diameter. These points correspond to $\omega^8\ldots, \omega^{13}$ . Then the lengths of the segments are $|1-\omega|,\ldots, |1-\omega^6|,|1-\omega^8|,\ldots |1-\omega^{13}|$ . Noting that $B$ represents 1 in the complex plane, the desired product is \begin{align*} BC_1\cdots BC_6 \cdot AC_1\cdots AC_6&= BC_1\cdots BC_6 \cdot BC_1'\cdots BC_6'\\ &= |(x-\omega^1)\ldots(x-\omega^6)(x-\omega^8)\ldots(x-\omega^{13})| \end{align*}
for $x=1$ . However, the polynomial $(x-\omega^1)\ldots(x-\omega^6)(x-\omega^8)\ldots(x-\omega^{13})$ has as its zeros all 14th roots of unity except for $-1$ and $1$ . Hence \[(x-\omega^1)\ldots(x-\omega^6)(x-\omega^8)\ldots(x-\omega^{13})=\frac{x^{14}-1}{(x-1)(x+1)}=x^{12}+x^{10}+\cdots +x^2+1.\] Thus the product is $|x^{12}+\cdots +x^2+1|=7$ when the radius is 1, and the product is $2^{12}\cdot 7=28672$ . Thus the answer is $\boxed {672}$ .

## Solution 2
Let $O$ be the midpoint of $A$ and $B$ . Assume $C_1$ is closer to $A$ instead of $B$ . $\angle AOC_1$ = $\frac {\pi}{7}$ . Using the Law of Cosines ,
$\overline {AC_1}^2$ = $8 - 8 \cos \frac {\pi}{7}$ , $\overline {AC_2}^2$ = $8 - 8 \cos \frac {2\pi}{7}$ , . . . $\overline {AC_6}^2$ = $8 - 8 \cos \frac {6\pi}{7}$
So $n$ = $(8^6)(1 - \cos \frac {\pi}{7})(1 - \cos \frac {2\pi}{7})\dots(1 - \cos \frac{6\pi}{7})$ . It can be rearranged to form
$n$ = $(8^6)(1 - \cos \frac {\pi}{7})(1 - \cos \frac {6\pi}{7})\dots(1 - \cos \frac {3\pi}{7})(1 - \cos \frac {4\pi}{7})$ .
Since $\cos a = - \cos (\pi - a)$ , we have
$n$ = $(8^6)(1 - \cos \frac {\pi}{7})(1 + \cos \frac {\pi}{7}) \dots (1 - \cos \frac {3\pi}{7})(1 + \cos \frac {3\pi}{7})$
= $(8^6)(1 - \cos^2 \frac {\pi}{7})(1 - \cos^2 \frac {2\pi}{7})(1 - \cos^2 \frac {3\pi}{7})$
= $(8^6)(\sin^2 \frac {\pi}{7})(\sin^2 \frac {2\pi}{7})(\sin^2 \frac {3\pi}{7})$
It can be shown that $\sin \frac {\pi}{7} \sin \frac {2\pi}{7} \sin \frac {3\pi}{7}$ = $\frac {\sqrt {7}}{8}$ , so $n$ = $8^6(\frac {\sqrt {7}}{8})^2$ = $7(8^4)$ = $28672$ , so the answer is $\boxed {672}$

## Solution 3
Note that for each $k$ the triangle $ABC_k$ is a right triangle. Hence the product $AC_k \cdot BC_k$ is twice the area of the triangle $ABC_k$ . Knowing that $AB=4$ , the area of $ABC_k$ can also be expressed as $2c_k$ , where $c_k$ is the length of the altitude from $C_k$ onto $AB$ . Hence we have $AC_k \cdot BC_k = 4c_k$ .
By the definition of $C_k$ we obviously have $c_k = 2\sin\frac{k\pi}7$ .
From these two observations we get that the product we should compute is equal to $8^6 \cdot \prod_{k=1}^6 \sin \frac{k\pi}7$ , which is the same identity as in Solution 2.
### Computing the product of sines
In this section we show one way how to evaluate the product $\prod_{k=1}^6 \sin \frac{k\pi}7 = \prod_{k=1}^3 (\sin \frac{k\pi}7)^2$ .
Let $\omega_k = \cos \frac{2k\pi}7 + i\sin \frac{2k\pi}7$ . The numbers $1,\omega_1,\omega_2,\dots,\omega_6$ are the $7$ -th complex roots of unity. In other words, these are the roots of the polynomial $x^7-1$ . Then the numbers $\omega_1,\omega_2,\dots,\omega_6$ are the roots of the polynomial $\frac{x^7-1}{x-1} = x^6+x^5+\cdots+x+1$ .
We just proved the identity $\prod_{k=1}^6 (x - \omega_k) = x^6+x^5+\cdots+x+1$ . Substitute $x=1$ . The right hand side is obviously equal to $7$ . Let's now examine the left hand side. We have:
\begin{align*} (1-\omega_k)(1-\omega_{7-k})=|1-\omega_k|^2 & = \left( 1-\cos \frac{2k\pi}7 \right)^2 + \left( \sin \frac{2k\pi}7 \right)^2 \\ & = 2-2\cos \frac{2k\pi}7 \\ & = 2-2 \left( 1 - 2 \left( \sin \frac{k\pi}7 \right)^2 \right) \\ & = 4\left( \sin \frac{k\pi}7 \right)^2 \end{align*}
Therefore the size of the left hand side in our equation is $\prod_{k=1}^3 4 (\sin \frac{k\pi}7)^2 = 2^6 \prod_{k=1}^3 (\sin \frac{k\pi}7)^2$ . As the right hand side is $7$ , we get that $\prod_{k=1}^3 (\sin \frac{k\pi}7)^2 = \frac{7}{2^6}$ .

## Solution 4 (Product of Sines)
Lemma 1: A chord of a circle with center and radius has length .
Proof: Denote as the projection from to line . Then, by definition, . Thus, , which concludes the proof.
Lemma 2:
Proof: Let . Thus, Since, are just the th roots of unity excluding , by Vieta's, , thus completing the proof.
By Lemma 1, the length $AC_k=2r\sin\dfrac{k\pi}{14}$ and similar lengths apply for $BC_k$ . Now, the problem asks for $\left(\prod_{k=1}^6 \left(4\sin\dfrac{k\pi}{14}\right)\right)^2$ . This can be rewritten, due to $\sin \theta = \sin (\pi-\theta)$ , as $\prod_{k=1}^6 \left(4\sin\dfrac{k\pi}{14}\right) \cdot \prod_{k=8}^{13} \left(4\sin\dfrac{k\pi}{14}\right) = \dfrac{1}{\sin \dfrac{7\pi}{14}}\cdot \prod_{k=1}^{13} \left(4\sin\dfrac{k\pi}{14}\right) = \prod_{k=1}^{13} \left(4\sin\dfrac{k\pi}{14}\right).$ By Lemma 2, this furtherly boils down to $4^{12}\cdot \dfrac{14}{2^{13}} = 7\cdot 2^{12} = \boxed{672} \; \text{(mod }1000\text{)}$
~Solution by sml1809

## Video Solution
https://youtu.be/TrKxzgR7V8U?si=FFOBCJxjGrg9sWGC
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.