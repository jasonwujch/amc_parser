# 2021 Fall AMC 12B Problem 13

## Problem

Let $c = \frac{2\pi}{11}.$ What is the value of \[\frac{\sin 3c \cdot \sin 6c \cdot \sin 9c \cdot \sin 12c \cdot \sin 15c}{\sin c \cdot \sin 2c \cdot \sin 3c \cdot \sin 4c \cdot \sin 5c}?\]

$\textbf{(A)}\ {-}1 \qquad\textbf{(B)}\ {-}\frac{\sqrt{11}}{5} \qquad\textbf{(C)}\ \frac{\sqrt{11}}{5} \qquad\textbf{(D)}\ \frac{10}{11} \qquad\textbf{(E)}\ 1$

## Solution
Plugging in $c$ , we get \[\frac{\sin 3c \cdot \sin 6c \cdot \sin 9c \cdot \sin 12c \cdot \sin 15c}{\sin c \cdot \sin 2c \cdot \sin 3c \cdot \sin 4c \cdot \sin 5c}=\frac{\sin \frac{6\pi}{11} \cdot \sin \frac{12\pi}{11} \cdot \sin \frac{18\pi}{11} \cdot \sin \frac{24\pi}{11} \cdot \sin \frac{30\pi}{11}}{\sin \frac{2\pi}{11} \cdot \sin \frac{4\pi}{11} \cdot \sin \frac{6\pi}{11} \cdot \sin \frac{8\pi}{11} \cdot \sin \frac{10\pi}{11}}.\] Since $\sin(x+2\pi)=\sin(x),$ $\sin(2\pi-x)=\sin(-x),$ and $\sin(-x)=-\sin(x),$ we get \[\frac{\sin \frac{6\pi}{11} \cdot \sin \frac{12\pi}{11} \cdot \sin \frac{18\pi}{11} \cdot \sin \frac{24\pi}{11} \cdot \sin \frac{30\pi}{11}}{\sin \frac{2\pi}{11} \cdot \sin \frac{4\pi}{11} \cdot \sin \frac{6\pi}{11} \cdot \sin \frac{8\pi}{11} \cdot \sin \frac{10\pi}{11}}=\frac{\sin \frac{6\pi}{11} \cdot \sin \frac{-10\pi}{11} \cdot \sin \frac{-4\pi}{11} \cdot \sin \frac{2\pi}{11} \cdot \sin \frac{8\pi}{11}}{\sin \frac{2\pi}{11} \cdot \sin \frac{4\pi}{11} \cdot \sin \frac{6\pi}{11} \cdot \sin \frac{8\pi}{11} \cdot \sin \frac{10\pi}{11}}=\boxed{\textbf{(E)}\ 1}.\]
~kingofpineapplz ~Ziyao7294 (minor edit)

## Solution 2
Eisenstein used such a quotient in his proof of quadratic reciprocity . Let $c=\frac{2\pi}{p}$ where $p$ is an odd prime number and $q$ is any integer.
Then $\dfrac{\sin(qc)\sin(2qc)\cdots\sin(\frac{p-1}{2}qc)}{\sin(c)\sin(2c)\cdots\sin(\frac{p-1}{2}c)}$ is the Legendre symbol $\left(\frac{q}{p}\right)$ . Legendre symbol is calculated using quadratic reciprocity which is $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right)=(-1)^{\frac{p-1}{2}\frac{q-1}{2}}$ . The Legendre symbol $\left(\frac{3}{11}\right)=(-1)\left(\frac{11}{3}\right)=(-1)\left(\frac{-1}{3}\right)=(-1)(-1)=\boxed{\textbf{(E)}\ 1}$
~Lopkiloinm

## Solution 3
We have that $5^2 \equiv 3 \pmod{11}$ , so 3 is a quadratic residue mod 11. For quadratic residues, their Legendre symbol which we know is the answer from Solution 2 is $\boxed{\textbf{(E)}\ 1}$

## Solution 4
We have $\zeta$ be an 11th primitive root of unity. Then the quotient becomes \[\frac{(\zeta^3-\zeta^{-3})(\zeta^6-\zeta^{-6})(\zeta^9-\zeta^{-9})(\zeta^{12}-\zeta^{-12})(\zeta^{15}-\zeta^{-15})}{(\zeta^1-\zeta^{-1})(\zeta^2-\zeta^{-2})(\zeta^3-\zeta^{-3})(\zeta^{4}-\zeta^{-4})(\zeta^{5}-\zeta^{-5})}\] which we can use modular arithmetic to become \[\frac{(\zeta^3-\zeta^{-3})(\zeta^{-5}-\zeta^{5})(\zeta^{-2}-\zeta^{2})(\zeta^{1}-\zeta^{-1})(\zeta^{4}-\zeta^{-4})}{(\zeta^1-\zeta^{-1})(\zeta^2-\zeta^{-2})(\zeta^3-\zeta^{-3})(\zeta^{4}-\zeta^{-4})(\zeta^{5}-\zeta^{-5})}\] and we see that is $\boxed{\textbf{(E)}\ 1}$
~Lopkiloinm

## Solution 5 (guess)
Since we can't calculate the exact value of $\sin{\frac{2\pi}{11}},$ it's unlikely the answer will have radicals in it. This leaves us with $-1, 1,$ and $\frac{10}{11}.$ The fraction is too precise for it to be a likely answer, so that leaves us with $1$ or $-1.$ Note that if the angle is greater than $\pi,$ the sine will be negative, and if it's less than $\pi$ it'll be positive. The numerator and denominator are therefore both positive, so we eliminate $-1$ to get $\boxed{\textbf{(E)}\ 1}.$
~ grogg007

## Video Solution (Just 2 min!)
https://youtu.be/S44IzCpzTeg
~ Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .