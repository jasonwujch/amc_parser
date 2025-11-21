# 2022 AIME II Problem 4

## Problem

There is a positive real number $x$ not equal to either $\tfrac{1}{20}$ or $\tfrac{1}{2}$ such that \[\log_{20x} (22x)=\log_{2x} (202x).\] The value $\log_{20x} (22x)$ can be written as $\log_{10} (\tfrac{m}{n})$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
Define $a$ to be $\log_{20x} (22x) = \log_{2x} (202x)$ , what we are looking for. Then, by the definition of the logarithm, \[\begin{cases} (20x)^{a} &= 22x \\ (2x)^{a} &= 202x. \end{cases}\] Dividing the first equation by the second equation gives us $10^a = \frac{11}{101}$ , so by the definition of logs, $a = \log_{10} \frac{11}{101}$ . This is what the problem asked for, so the fraction $\frac{11}{101}$ gives us $m+n = \boxed{112}$ .
~ihatemath123

## Solution 2
We could assume a variable $v$ which equals to both $\log_{20x} (22x)$ and $\log_{2x} (202x)$ .
So that $(20x)^v=22x \textcircled{1}$ and $(2x)^v=202x \textcircled{2}$
Express $\textcircled{1}$ as: $(20x)^v=(2x \cdot 10)^v=(2x)^v \cdot \left(10^v\right)=22x \textcircled{3}$
Substitute $\textcircled{{2}}$ to $\textcircled{3}$ : $202x \cdot (10^v)=22x$
Thus, $v=\log_{10} \left(\frac{22x}{202x}\right)= \log_{10} \left(\frac{11}{101}\right)$ , where $m=11$ and $n=101$ .
Therefore, $m+n = \boxed{112}$ .

## Solution 3
We have \begin{align*} \log_{20x} (22x) & = \frac{\log_k 22x}{\log_k 20x} \\ & = \frac{\log_k x + \log_k 22}{\log_k x + \log_k 20} . \end{align*}
We have \begin{align*} \log_{2x} (202x) & = \frac{\log_k 202x}{\log_k 2x} \\ & = \frac{\log_k x + \log_k 202 }{\log_k x + \log_k 2} . \end{align*}
Because $\log_{20x} (22x)=\log_{2x} (202x)$ , we get \[ \frac{\log_k x + \log_k 22}{\log_k x + \log_k 20} = \frac{\log_k x + \log_k 202 }{\log_k x + \log_k 2} . \]
We denote this common value as $\lambda$ .
By solving the equality $\frac{\log_k x + \log_k 22}{\log_k x + \log_k 20} = \lambda$ , we get $\log_k x = \frac{\log_k 22 - \lambda \log_k 20}{\lambda - 1}$ .
By solving the equality $\frac{\log_k x + \log_k 202 }{\log_k x + \log_k 2} = \lambda$ , we get $\log_k x = \frac{\log_k 202 - \lambda \log_k 2}{\lambda - 1}$ .
By equating these two equations, we get \[ \frac{\log_k 22 - \lambda \log_k 20}{\lambda - 1} = \frac{\log_k 202 - \lambda \log_k 2}{\lambda - 1} . \]
Therefore, \begin{align*} \log_{20x} (22x) & = \lambda \\ & = \frac{\log_k 22 - \log_k 202}{\log_k 20 - \log_k 2} \\ & = \frac{\log_k \frac{11}{101}}{\log_k 10} \\ & = \log_{10} \frac{11}{101} . \end{align*}
Therefore, the answer is $11 + 101 = \boxed{\textbf{112}}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 4 (Solution 1 with more reasoning)
Let $a$ be the exponent such that $(20x)^a = 22x$ and $(2x)^a = 202x$ . Dividing, we get \begin{align*} \dfrac{(20x)^a}{(2x)^a} &= \dfrac{22x}{202x}. \\ \left(\dfrac{20x}{2x}\right)^a &= \dfrac{22x}{202x}. \\ 10^a &= \dfrac{11}{101}. \\ \end{align*} Thus, we see that $\log_{10} \left(\dfrac{11}{101}\right) = a = \log_{20x} 22x$ , so the answer is $11 + 101 = \boxed{112}$ .
~A_MatheMagician

## Solution 5
By the change of base rule, we have $\frac{\log 22x}{\log 20x}=\frac{\log 202x}{\log 2x}$ , or $\frac{\log 22 +\log x}{\log 20 +\log x}=\frac{\log 202 +\log x}{\log 2 +\log x}=k$ . We also know that if $a/b=c/d$ , then this also equals $\frac{a-c}{b-d}$ . We use this identity and find that $k=\frac{\log 202 -\log 22}{\log 2 -\log 20}=-\log\frac{202}{22}=\log\frac{11}{101}$ . The requested sum is $11+101=\boxed{112}.$
~MathIsFun286

## Solution 6
By change of base formula, \[\frac{\log_{2x} 22x}{\log_{2x} 20x} = \frac{{\log_{2x} 11} + 1}{{\log_{2x} 10} + 1} = {\log_{2x} 101} + 1\] \[\log_{2x} 11 + 1 = (\log_{2x} 10)(\log_{2x} 101) + \log_{2x} 10 + 1\] \[\frac{\log_{2x} \frac{11}{1010}}{\log_{2x} 10} = \log_{2x} 101\] \[\log_{10} {\frac{11}{1010}} = \log_{2x} 101\] \[\log_{10} {\frac{11}{1010}} + 1 = \log_{2x} 101 + 1 = \log_{2x} 202x = \log_{20x} {22x}\] Thus, \[\log_{20x} 22x = \log_{10} \left( \frac{11}{1010} \times 10 \right) = \log_{10} \frac{11}{101}\] The requested answer is $11 + 101 = \boxed{112}$ .
~ adam_zheng

## Video Solution
https://www.youtube.com/watch?v=4qJyvyZN630

## Video Solution by Power of Logic
https://youtu.be/m2Cm9r5_Jvs
~Hayabusa1
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .