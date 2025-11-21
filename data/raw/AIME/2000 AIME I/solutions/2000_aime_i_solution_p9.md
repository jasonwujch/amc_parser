# 2000 AIME I Problem 9

## Problem

The system of equations \begin{eqnarray*}\log_{10}(2000xy) - (\log_{10}x)(\log_{10}y) & = & 4 \\ \log_{10}(2yz) - (\log_{10}y)(\log_{10}z) & = & 1 \\ \log_{10}(zx) - (\log_{10}z)(\log_{10}x) & = & 0 \\ \end{eqnarray*}

has two solutions $(x_{1},y_{1},z_{1})$ and $(x_{2},y_{2},z_{2})$ . Find $y_{1} + y_{2}$ .

## Solution
Since $\log ab = \log a + \log b$ , we can reduce the equations to a more recognizable form:
\begin{eqnarray*} -\log x \log y + \log x + \log y - 1 &=& 3 - \log 2000\\ -\log y \log z + \log y + \log z - 1 &=& - \log 2\\ -\log x \log z + \log x + \log z - 1 &=& -1\\ \end{eqnarray*}
Let $a,b,c$ be $\log x, \log y, \log z$ respectively. Using SFFT , the above equations become (*)
\begin{eqnarray*}(a - 1)(b - 1) &=& \log 2 \\ (b-1)(c-1) &=& \log 2 \\ (a-1)(c-1) &=& 1 \end{eqnarray*}
Small note from different author: $-(3 - \log 2000) = \log 2000 - 3 = \log 2000 - \log 1000 = \log 2.$
From here, multiplying the three equations gives
\begin{eqnarray*}(a-1)^2(b-1)^2(c-1)^2 &=& (\log 2)^2\\ (a-1)(b-1)(c-1) &=& \pm\log 2\end{eqnarray*}
Dividing the third equation of (*) from this equation, $b-1 = \log y - 1 = \pm\log 2 \Longrightarrow \log y = \pm \log 2 + 1$ . (Note from different author if you are confused on this step: if $\pm$ is positive then $\log y = \log 2 + 1 = \log 2 + \log 10 = \log 20,$ so $y=20.$ if $\pm$ is negative then $\log y = 1 - \log 2 = \log 10 - \log 2 = \log 5,$ so $y=5.$ ) This gives $y_1 = 20, y_2 = 5$ , and the answer is $y_1 + y_2 = \boxed{025}$ .

## Solution 2
Subtracting the second equation from the first equation yields \begin{align*} \log 2000xy-\log 2yz-((\log x)(\log y)-(\log y)(\log z)) &= 3 \\ \log\frac{2000xy}{2yz}-\log y(\log x-\log z) &= 3 \\ \log1000+\log\frac{x}{z}-\log y(\log\frac{x}{z}) &= 3 \\ 3+\log\frac{x}{z}-\log y(\log\frac{x}{z}) &= 3 \\ \log\frac{x}{z}(1-\log y) &= 0 \\ \end{align*} If $1-\log y=0$ then $y=10$ . Substituting into the first equation yields $\log20000=4$ which is not possible.
If $\log\frac{x}{z}=0$ then $\frac{x}{z}=1\Longrightarrow x=z$ . Substituting into the third equation gets \begin{align*} \log x^2-(\log x)(\log x) &= 0 \\ \log x^2-\log x^x &= 0 \\ \log x^{2-x} &= 0 \\ x^{2-x} &= 1 \\ \end{align*} Thus either $x=1$ or $2-x=0\Longrightarrow x=2$ . (Note that here $x\neq-1$ since logarithm isn't defined for negative number.)
Substituting $x=1$ and $x=2$ into the first equation will obtain $y=5$ and $y=20$ , respectively. Thus $y_1+y_2=\boxed{025}$ .
~ Nafer

## Solution 3
Let $a = \log x$ , $b = \log y$ and $c = \log z$ . Then the given equations become:
\begin{align*} \log 2 + a + b - ab = 1 \\ \log 2 + b + c - bc = 1 \\ a+c = ac \\ \end{align*}
Equating the first and second equations, solving, and factoring, we get $a(1-b) = c(1-b) \implies{a = c}$ . Plugging this result into the third equation, we get $c = 0$ or $2$ . Substituting each of these values of $c$ into the second equation, we get $b = 1 - \log 2$ and $b = 1 + \log 2$ . Substituting backwards from our original substitution, we get $y = 5$ and $y = 20$ , respectively, so our answer is $\boxed{025}$ .
~ anellipticcurveoverq

## Solution 4
All logs are base 10 by convention. Rearrange the given statements:
\begin{align*} \log 2000 + \log x + \log y - \log x \log y = 4, \quad \text{which becomes} \quad \log x + \log y = \log x \log y + \log 5. \\ \log 2 + \log y + \log z - \log y \log z = 1, \quad \text{which becomes} \quad \log y + \log z = \log y \log z + \log 5. \\ \log z + \log x - \log z \log x = 0, \quad \text{which becomes} \quad \log x + \log z = \log z \log x. \\ \end{align*}
Subtract the first two equations to obtain $(\log x - \log z) = \log y (\log x - \log z).$
This must mean \(\log x = \log z\) because otherwise \(\log y = 1\) turns the first equation into \(\log y = \log 5\) which is self-contradictory.
With \(\log x = \log z\) we know each value satisfies \(2a = a^2\), so they are both \(0\) or both \(2\). Finally we arrive at our two solutions, where 0 gives us \(0 + \log y = 0 + \log 5\), and \(y = 5\), and 2 gives us \(2 + \log y = 2 \log y + \log 5\), and \(\log y = 2 - \log 5 = \log 20\), so \(y = 20\). Similar to above we arrive at $\boxed{025}$ .
~ GrindOlympiads

## Video solution
https://www.youtube.com/watch?v=sOyLnGJjVvc&t
These problems are copyrighted © by the Mathematical Association of America.