# 2012 AIME I Problem 9

## Problem

Let $x,$ $y,$ and $z$ be positive real numbers that satisfy \[2\log_{x}(2y) = 2\log_{2x}(4z) = \log_{2x^4}(8yz) \ne 0.\] The value of $xy^5z$ can be expressed in the form $\frac{1}{2^{p/q}},$ where $p$ and $q$ are relatively prime positive integers. Find $p+q.$

## Solution 1
Since there are only two dependent equations given and three unknowns, the three expressions given can equate to any common value (that isn't 0, of course), so to simplify the problem let us assume without loss of generality that \[2\log_{x}(2y) = 2\log_{2x}(4z) = \log_{2x^4}(8yz) = 2.\] Then \begin{align*} 2\log_{x}(2y) = 2 &\implies x=2y\\ 2\log_{2x}(4z) = 2 &\implies 2x=4z\\ \log_{2x^4}(8yz) = 2 &\implies 4x^8 = 8yz \end{align*} Solving these equations, we quickly see that $4x^8 = (2y)(4z) = x(2x) \rightarrow x=2^{-1/6}$ and then $y=z=2^{-1/6 - 1} = 2^{-7/6}.$ Finally, our desired value is $2^{-1/6} \cdot (2^{-7/6})^5 \cdot 2^{-7/6} = 2^{-43/6}$ and thus $p+q = 43 + 6 = \boxed{049.}$

## Solution 2
Notice that $2y\cdot 4z=8yz$ , $2\log_2(2y)=\log_2\left(4y^2\right)$ and $2\log_2(4z)=\log_2\left(16z^2\right)$ .
From this, we see that $8yz$ is the geometric mean of $4y^2$ and $16z^2$ . So, for constant $C\ne 0$ : \[\frac{\log 4y^2}{\log x}=\frac{\log 8yz}{\log 2x^4}=\frac{\log 16z^2}{\log 2x}=C\] Since $\log 4y^2,\log 8yz,\log 16z^2$ are in an arithmetic progression, so are $\log x,\log 2x^4,\log 2x$ .
Therefore, $2x^4$ is the geometric mean of $x$ and $2x$ \[2x^4=\sqrt{x\cdot 2x}\implies 4x^8=2x^2\implies 2x^6=1\implies x=2^{-1/6}\] We can plug $x$ in to any of the two equal fractions aforementioned. So, without loss of generality: \[\frac{\log 4y^2}{\log x}=\frac{\log 16z^2}{\log 2x}\implies \log\left(4y^2\right)\log\left(2x\right)=\log\left(16z^2\right)\log\left(x\right)\] \[\implies \log\left(4y^2\right)\cdot \frac{5}{6}\log 2=\log\left(16z^2\right)\cdot \frac{-1}{6}\log 2\] \[\implies 5\log\left(4y^2\right)=-\log\left(16z^2\right)\implies 5\log\left(4y^2\right)+\log\left(16z^2\right)=0\] \[\implies \left(4y^2\right)^5\cdot 16z^2=1\implies 16384y^{10}z^2=1\implies y^{10}z^2=\frac{1}{16384}\implies y^5z=\frac{1}{128}\]
Thus $xy^5z=2^{-\frac{1}{6}-7}=2^{-\frac{43}{6}}$ and $43+6=\boxed{049}$ .

## Solution 3
Since we are given that $xy^5z = 2^{-p/q}$ , we may assume that $x, y$ , and $z$ are all powers of two. We shall thus let $x = 2^X$ , $y = 2^Y$ , and $z = 2^Z$ . Let $a = \log_{2^X}(2^{Y+1})$ . From this we get the system of equations: \[\] $(1)$ \[a = \log_{2^X}(2^{Y+1}) \Rightarrow aX = Y + 1\] $(2)$ \[a = \log_{2^{X + 1}}(2^{Z + 2}) \Rightarrow aX + a = Z + 2\] $(3)$ \[2a = \log_{2^{4X + 1}}(2^{Y + Z + 3}) \Rightarrow 8aX + 2a = Y + Z + 3\]
Plugging equation $(1)$ into equation $(2)$ yields $Y + a = Z + 1$ . Plugging equation $(1)$ into equation $(3)$ and simplifying yields $7Y + 2a + 6 = Z + 1$ , and substituting $Y + a$ for $Z + 1$ and simplifying yields $Y + 1 = \frac{-a}{6}$ . But $Y + 1 = aX$ , so $aX = \frac{-a}{6}$ , so $X = \frac{-1}{6}$ .
Knowing this, we may substitute $\frac{-1}{6}$ for $X$ in equations $(1)$ and $(2)$ , yielding $\frac{-a}{6} = Y + 1$ and $\frac{5a}{6} = Z + 2$ . Thus, we have that $-5(Y + 1) = Z + 2 \rightarrow 5Y + Z = -7$ . We are looking for $xy^5z = 2^{X+ 5Y + Z}$ . $X = \frac{-1}{6}$ and $5Y + Z = -7$ , so $xy^5z = 2^{-43/6} = \frac{1}{2^{43/6}}$ . The answer is $43+6=\boxed{049}$ .

## Solution 4 (Rigorous and easy)
By the Mediant theorem , we know that \[\frac{\log (4y^2)}{\log (x)} = \frac{\log (16z^2)}{\log (2x)} = \frac{2\log (8yz)}{\log (2x^2)}.\]
Substituting into the original equation yields us $\frac{2\log (8yz)}{\log (2x^2)} = \frac{\log (8yz)}{\log (2x^4)} \Rightarrow 2\log (2x^4) = \log (2x^2) \Rightarrow x=2^{-1/6}.$ For some constant $C\not= 0,$ Let $2\log_{x}(2y) = 2\log_{2x}(4z) = \log_{2x^4}(8yz) = C.$ Then, we obtain the system of equations \[y=2^{-13C/12}\] \[z=2^{-19C/12}\] \[8yz=2^{C/3}.\]
Multiplying the first two equations and dividing by the third, we find $C=1.$ Thus, \[xy^5z=2^{-1/6} \cdot 2^{-65/12} \cdot 2^{-19/12}=2^{-43/6} \Rightarrow p+q=\boxed{049}.\]
~Kscv
~minor edits by makethan

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/348
~ dolphin7
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .