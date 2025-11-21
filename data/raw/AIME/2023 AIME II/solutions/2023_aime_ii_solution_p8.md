# 2023 AIME II Problem 8

## Problem

Let $\omega = \cos\frac{2\pi}{7} + i \cdot \sin\frac{2\pi}{7},$ where $i = \sqrt{-1}.$ Find the value of the product \[\prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right).\]

## Video solution by grogg007
https://www.youtube.com/watch?v=e-CyXek-ZFs

## Solution 1
For any $k\in Z$ , we have, \begin{align*} & \left( \omega^{3k} + \omega^k + 1 \right) \left( \omega^{3\left( 7 - k \right)} + \omega^{\left( 7 - k \right)} + 1 \right) \\ & = \omega^{3 \cdot 7} + \omega^{2k + 7} + \omega^{3k} + \omega^{-2k + 3 \cdot 7} + \omega^7 + \omega^k + \omega^{3\left( 7 - k \right)} + \omega^{\left( 7 - k \right)} + 1 \\ & = 1 + \omega^{2k} + \omega^{3k} + \omega^{-2k} + 1 + \omega^k + \omega^{-3k} + \omega^{-k} + 1 \\ & = 2 + \omega^{-3k} \sum_{j=0}^6 \omega^{j k} \\ & = 2 + \omega^{-3k} \frac{1 - \omega^{7 k}}{1 - \omega^k} \\ & = 2 . \end{align*} The second and the fifth equalities follow from the property that $\omega^7 = 1$ .
Therefore, \begin{align*} \Pi_{k=0}^6 \left( \omega^{3k} + \omega^k + 1 \right) & = \left( \omega^{3 \cdot 0} + \omega^0 + 1 \right) \Pi_{k=1}^3 \left( \omega^{3k} + \omega^k + 1 \right) \left( \omega^{3\left( 7 - k \right)} + \omega^{\left( 7 - k \right)} + 1 \right) \\ & = 3 \cdot 2^3 \\ & = \boxed{\textbf{024}}. \end{align*} Man, What can I say? Mamba never out!
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
$k$ cannot be a multiple of $7$ , otherwise the first equation would equal $9$ instead of $2$ ~inaccessibles

## Solution 2 (Moduli)
Because the answer must be a positive integer, it is just equal to the modulus of the product. Define $z_n = \left(\textrm{cis }\frac{2n\pi}{7}\right)^3 + \textrm{cis }\frac{2n\pi}{7} + 1$ .
Then, our product is equal to
\[|z_0||z_1||z_2||z_3||z_4||z_5||z_6|.\]
$z_0 = 3$ , and we may observe that $z_x$ and $z_{7-x}$ are conjugates for any $x$ , meaning that their magnitudes are the same. Thus, our product is
\[3|z_1|^2|z_2|^2|z_3|^2\] \[= 3\left((\cos \frac{6\pi}{7} + \cos \frac{2\pi}{7} + 1)^2 + (\sin \frac{6\pi}{7} + \sin \frac{2\pi}{7})^2\right) \left((\cos \frac{12\pi}{7} + \cos \frac{4\pi}{7} + 1)^2 + (\sin \frac{12\pi}{7} + \sin \frac{4\pi}{7})^2\right) \left((\cos \frac{4\pi}{7} + \cos \frac{6\pi}{7} + 1)^2 + (\sin \frac{4\pi}{7} + \sin \frac{6\pi}{7})^2\right)\]
Let us simplify the first term. Expanding, we obtain
\[\cos^2 \frac{6\pi}{7} + \cos^2 \frac{2\pi}{7} + 1 + 2\cos \frac{6\pi}{7}\cos \frac{2\pi}{7} + 2\cos \frac{6\pi}{7} + 2\cos \frac{2\pi}{7} + \sin^2 \frac{6\pi}{7} + \sin^2 \frac{2\pi}{7} + 2\sin \frac{6\pi}{7}\sin \frac{2\pi}{7}.\]
Rearranging and cancelling, we obtain
\[3 + 2\cos \frac{6\pi}{7} + 2\cos \frac{2\pi}{7} + 2\cos \frac{6\pi}{7}\cos \frac{2\pi}{7} + 2\sin \frac{6\pi}{7}\sin \frac{2\pi}{7}.\]
By the cosine subtraction formula, we have $2\cos \frac{6\pi}{7}\cos \frac{2\pi}{7} + 2\sin \frac{6\pi}{7}\sin \frac{2\pi}{7} = \cos \frac{6\pi - 2\pi}{7} = \cos \frac{4\pi}{7}$ .
Thus, the first term is equivalent to
\[3 + 2(\cos \frac{2\pi}{7} + \cos \frac{4\pi}{7} + \cos \frac{6\pi}{7}).\]
Similarly, the second and third terms are, respectively,
\[3 + 2(\cos \frac{4\pi}{7} + \cos \frac{8\pi}{7} + \cos \frac{12\pi}{7}),\textrm{ and}\] \[3 + 2(\cos \frac{6\pi}{7} + \cos \frac{12\pi}{7} + \cos \frac{4\pi}{7}).\]
Next, we have $\cos \frac{2\pi}{7} + \cos \frac{4\pi}{7} + \cos \frac{6\pi}{7} = -\frac{1}{2}$ . This is because
\[\cos \frac{2\pi}{7} + \cos \frac{4\pi}{7} + \cos \frac{6\pi}{7} = \frac{1}{2}(\textrm{cis }\frac{2\pi}{7} + \textrm{cis }\frac{4\pi}{7} + \textrm{cis }\frac{6\pi}{7} + \textrm{cis }\frac{8\pi}{7} + \textrm{cis }\frac{10\pi}{7} + \textrm{cis }\frac{12\pi}{7})\]
\[= \frac{1}{2}(-1)\] \[= -\frac{1}{2}.\]
Therefore, the first term is simply $2$ . We have $\cos x = \cos 2\pi - x$ , so therefore the second and third terms can both also be simplified to $3 + 2(\cos \frac{2\pi}{7} + \cos \frac{4\pi}{7} + \cos \frac{6\pi}{7}) = 2$ . Thus, our answer is simply
\[3 \cdot 2 \cdot 2 \cdot 2\] \[= \boxed{\mathbf{024}}.\]
~mathboy100

## Solution 3 (Inspecting the exponents of powers of )
We write out the product in terms of $\omega$ : \[\prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right)=3(\omega^3+\omega+1)(\omega^6+\omega^2+1)(\omega^9+\omega^3+1)(\omega^{12}+\omega^4+1)(\omega^{15}+\omega^5+1)(\omega^{18}+\omega^6+1).\]
Grouping the terms in the following way exploits the fact that $\omega^{7k}=1$ for an integer $k$ , when multiplying out two adjacent products from left to right:
\[\frac{1}{3} \prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right)=(\omega^3+\omega+1)(\omega^{18}+\omega^6+1)(\omega^6+\omega^2+1)(\omega^{15}+\omega^5+1)(\omega^9+\omega^3+1)(\omega^{12}+\omega^4+1).\]
When multiplying two numbers with like bases, we add the exponents. We can now rewrite the exponents of each product (two at a time, where $1$ is treated as the identity) as a series of arrays:
\[\textbf{(A)}\begin{bmatrix} 3&1 &0 \\ 18&6&0\\ \end{bmatrix}\]
\[\textbf{(B)}\begin{bmatrix} 6&2 &0 \\ 15&5&0\\ \end{bmatrix}\]
\[\textbf{(C)}\begin{bmatrix} 9&3 &0 \\ 12&4&0\\ \end{bmatrix}.\]
Note that $\omega=e^{\frac{2\pi i}{7}}$ . When raising $\omega$ to a power, the numerator of the fraction is $2$ times whatever power $\omega$ is raised to, multiplied by $\pi i$ . Since the period of $\omega$ is $2\pi,$ we multiply each array by $2$ then reduce each entry $\mod{14},$ as each entry in an array represents an exponent which $\omega$ is raised to.
\[\textbf{(A)}\begin{bmatrix} 6&2 &0 \\ 8&12&0\\ \end{bmatrix}\]
\[\textbf{(B)}\begin{bmatrix} 12&4 &0 \\ 2&10&0\\ \end{bmatrix}\]
\[\textbf{(C)}\begin{bmatrix} 4&6 &0 \\ 10&8&0\\ \end{bmatrix}.\]
To obtain the correct exponents, we seperately add each element of the lower row to one element of the top row.
Therefore (after reducing $\mod 14$ again), we get the following sets:
\[\textbf{(A)}\ \{0, 4, 6, 10, 0, 2, 8, 12, 0\}\] \[\textbf{(B)}\ \{0, 8, 12, 6, 0, 4, 2, 10, 0\}\] \[\textbf{(C)}\ \{0, 12, 4, 2, 0, 8, 10, 8, 0\}.\]
Raising $\omega$ to the power of each element in every set then multiplying over $\textbf{(A)}, \textbf{(B)},$ and $\textbf{(C)}$ yields
\[\frac{1}{3} \prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right)=\left(\sum_{a\in \textbf{(A)}} \omega^a\right)\left(\sum_{b\in \textbf{(B)}} \omega^b\right)\left(\sum_{c\in \textbf{(C)}} \omega^c\right)\]
\[=\left(\sum_{a\in \textbf{(A)}} \omega^a\right)^3\]
\[=\left(\omega^0+\omega^4+\omega^6+\omega^{10}+\omega^0+\omega^2+\omega^8+\omega^{12}+\omega^0\right)^3\]
\[=\left(3+\omega^2+\omega^4+\omega^6+\omega^8+\omega^{10}+\omega^{12}\right)^3,\] as these sets are all identical.
Summing as a geometric series,
\[\frac{1}{3} \prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right)=\left(3+\frac{\omega^2(\omega^{12}-1)}{\omega^2-1}\right)^3\]
\[=\left(3+\frac{\omega^{14}-\omega^2}{\omega^2-1}\right)^3\]
\[=\left(3+\frac{1-\omega^2}{\omega^2-1}\right)^3\]
\[=(3-1)^3=8.\]
Therefore,
\[\frac{1}{3} \prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right)=8,\] and \[\prod_{k=0}^6 \left(\omega^{3k} + \omega^k + 1\right)=3\cdot8=\boxed{\textbf{(024)}}.\]
-Benedict T (countmath1)

## Solution 4
The product can be factored into $(1-r)(1-s)(1-t)(w-r)(w-s)(w-t)(w^2-r)(w^2-s)(w^2-t)....(w^6-r)(w^6-s)(w^6-t)$ , (treat $\omega^k$ as $x$ , so $x^3+x+1=0$ then k varies from 0 to 6.
where $r,s,t$ are the roots of the polynomial $x^3+x+1=0$ .
This is then $-(r^7-1)(s^7-1)(t^7-1)$ because $(r^7-1)$ and $(r-1)(r-w)(r-w^2)...(r-w^6)$ share the same roots and leading coefficient so are thus the same polynomial.
To find $-(r^7-1)(s^7-1)(t^7-1)$ ,
Notice that $(r^7-1)=(r-1)(r^6+r^5+r^4+r^3+r^2+r+1)$ . Since r satisfies $x^3+x+1=0$ , $r^6+r^4+r^3=0$
Substituting, you are left with $r^5+r^2+r+1$ . This is $r^2(r^3+1)+r+1$ , and after repeatedly substituting $r^3+r+1=0$ you are left with $-2r^3$ .
So now the problem is reduced to finding $-(r-1)(s-1)(t-1)(-2r^3)(-2s^3)(-2t^3)=8(rst)^3(r-1)(s-1)(t-1)$ , and vietas gives you the result of $\boxed{24}$ -resources

## Solution 5
The product can be written as $(\omega^0+\omega^0+1)(\omega^3+\omega+1)(\omega^6+\omega^2+1)(\omega^9+\omega^3+1)\\(\omega^{12}+\omega^4+1)(\omega^{15}+\omega^5+1)(\omega^{18}+\omega^6+1).$
The key here then is noticing that cis $2\pi=1.$
From this we realize $\omega^{7n+a}=\omega^a$ where $a$ is a residue $\pmod 7.$
Our expression then simplifies to $(3)(\omega^3+\omega+1)(\omega^6+\omega^2+1)(\omega^2+\omega^3+1)\\(\omega^5+\omega^4+1)(\omega+\omega^5+1)(\omega^4+\omega^6+1).$
The key then becomes multiplying the 2nd and 7th, 3rd and 6th, 4th and 5th terms because they would result in a couple of $\omega^7$ which will cancel out.
Multiplying them you obtain $\omega^6+\omega^5+\omega^4+\omega^3+\omega^2+\omega+3$ . Recognizing this as $\frac{\omega^7-1}{\omega-1}+2.$ For terms $2*7, 3*6, 4*5.$
$\omega^7-1=0$ (cis $2\pi=1.$ ) We are left with $(3)(2)(2)(2)=\boxed{024}.$
~BigBrain_2009

## Video Solution by The Power of Logic
https://youtu.be/o6w9t43GpJs?si=aoe-uM3m5AIwpz_H
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .