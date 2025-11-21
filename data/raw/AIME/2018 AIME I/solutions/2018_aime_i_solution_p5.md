# 2018 AIME I Problem 5

## Problem

For each ordered pair of real numbers $(x,y)$ satisfying \[\log_2(2x+y) = \log_4(x^2+xy+7y^2)\] there is a real number $K$ such that \[\log_3(3x+y) = \log_9(3x^2+4xy+Ky^2).\] Find the product of all possible values of $K$ .

## Solution 1
Using the logarithmic property $\log_{a^n}b^n = \log_{a}b$ , we note that \[(2x+y)^2 = x^2+xy+7y^2\] That gives \[x^2+xy-2y^2=0\] upon simplification and division by $3$ . Factoring $x^2+xy-2y^2=0$ gives \[(x+2y)(x-y)=0\] Then, \[x=y \text{ or }x=-2y\] From the second equation, \[9x^2+6xy+y^2=3x^2+4xy+Ky^2\] If we take $x=y$ , we see that $K=9$ . If we take $x=-2y$ , we see that $K=21$ . The product is $\boxed{189}$ .
-expiLnCalc

## Solution 2
Do as done in Solution 1 to get \[x^2+xy-2y^2=0\] \[\implies (\frac{x}{y})^2+\frac{x}{y}-2=0\] \[\implies \frac{x}{y}=\frac{-1\pm\sqrt{1+8}}{2}=1,-2\] Do as done in Solution 1 to get \[9x^2+6xy+y^2=3x^2+4xy+Ky^2\] \[\implies 6x^2+2xy+(1-K)y^2=0\] \[\implies 6(\frac{x}{y})^2+2\frac{x}{y}+(1-K)=0\] \[\implies \frac{x}{y}=\frac{-2\pm \sqrt{4-24(1-K)}}{12}\] \[\implies \frac{x}{y}=\frac{-2\pm 2\sqrt{6K-5}}{12}=\frac{-1\pm \sqrt{6K-5}}{6}\] If $\frac{x}{y}=1$ then \[1=\frac{-1\pm \sqrt{6K-5}}{6}\] \[\implies 6=-1\pm \sqrt{6K-5}\] \[\implies 7=\pm \sqrt{6K-5}\] \[\implies 49=6K-5\] \[\implies K=9\] If $\frac{x}{y}=-2$ then \[-2=\frac{-1\pm \sqrt{6K-5}}{6}\] \[\implies -12=-1\pm \sqrt{6K-5}\] \[\implies -11=\sqrt{6K-5}\] \[\implies 121=6K-5\] \[\implies 126=6K\] \[\implies K=21\] Hence our final answer is $21\cdot 9=\boxed{189}$ -vsamc $\newline$

## Solution 3 (Official MAA)
Because $x^2+xy+7y^2=\left(x+\tfrac{y}{2}\right)^2+\tfrac{27}{4}y^2>0,$ the right side of the first equation is real. It follows that the left side of the equation is also real, so $2x+y>0$ and \[\log_2(2x+y)=\log_{2^2}(2x+y)^2=\log_4(4x^2+4xy+y^2).\] Thus $4x^2+4xy+y^2=x^2+xy+7y^2,$ which implies that $0=x^2+xy-2y^2=(x+2y)(x-y).$ Therefore either $x=-2y$ or $x=y,$ and because $2x+y>0,$ $x$ must be positive and $3x+y=x+(2x+y)>0.$ Similarly, \[\log_3(3x+y)=\log_{3^2}(3x+y)^2=\log_9(9x^2+6xy+y^2).\] If $x=-2y\ne 0,$ then $9x^2+6xy+y^2=36y^2-12y^2+y^2=25y^2=3x^2+4xy+Ky^2$ when $K=21.$ If $x=y\ne 0,$ then $9x^2+6xy+y^2=16y^2=3x^2+4xy+Ky^2$ when $K=9.$ The requested product is $21\cdot9=189.$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .