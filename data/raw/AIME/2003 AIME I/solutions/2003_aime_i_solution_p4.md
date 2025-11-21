# 2003 AIME I Problem 4

## Problem

Given that $\log_{10} \sin x + \log_{10} \cos x = -1$ and that $\log_{10} (\sin x + \cos x) = \frac{1}{2} (\log_{10} n - 1),$ find $n.$

## Solution 1
Using the properties of logarithms , we can simplify the first equation to $\log_{10} \sin x + \log_{10} \cos x = \log_{10}(\sin x \cos x) = -1$ . Therefore, \[\sin x \cos x = \frac{1}{10}.\qquad (*)\]
Now, manipulate the second equation. \begin{align*} \log_{10} (\sin x + \cos x) &= \frac{1}{2}(\log_{10} n - \log_{10} 10) \\ \log_{10} (\sin x + \cos x) &= \left(\log_{10} \sqrt{\frac{n}{10}}\right) \\ \sin x + \cos x &= \sqrt{\frac{n}{10}} \\ (\sin x + \cos x)^{2} &= \left(\sqrt{\frac{n}{10}}\right)^2 \\ \sin^2 x + \cos^2 x +2 \sin x \cos x &= \frac{n}{10} \\ \end{align*}
By the Pythagorean identities, $\sin ^2 x + \cos ^2 x = 1$ , and we can substitute the value for $\sin x \cos x$ from $(*)$ . $1 + 2\left(\frac{1}{10}\right) = \frac{n}{10} \Longrightarrow n = \boxed{012}$ .

## Solution 2
Examining the first equation, we simplify as the following: \[\log_{10} \sin x \cos x = -1\] \[\implies \sin x \cos x = \frac{1}{10}\]
With this in mind, examining the second equation, we may simplify as the following (utilizing logarithm properties): \[\log_{10} (\sin x + \cos x) = \frac{1}{2} (\log_{10} n - \log_{10} 10)\] \[\implies \log_{10} (\sin x + \cos x) = \frac{1}{2} (\log_{10} \frac{n}{10})\] \[\implies \log_{10} (\sin x + \cos x) = \log_{10} \sqrt{\frac{n}{10}}\]
From here, we may divide both sides by $\log_{10} (\sin x + \cos x)$ and then proceed with the change-of-base logarithm property: \[1 = \frac{\log_{10} \sqrt{\frac{n}{10}}}{\log_{10} (\sin x + \cos x)}\] \[\implies 1 = \log_{\sin x + \cos x} \sqrt{\frac{n}{10}}\]
Thus, exponentiating both sides results in $\sin x + \cos x = \sqrt{\frac{n}{10}}$ . Squaring both sides gives us \[\sin^2 x + 2\sin x \cos x + \cos^2 x = \frac{n}{10}\]
Via the Pythagorean Identity, $\sin^2 x + \cos^2 x = 1$ and $2\sin x \cos x$ is simply $\frac{1}{5}$ , via substitution. Thus, substituting these results into the current equation: \[1 + \frac{1}{5} = \frac{n}{10}\] \[\implies \frac{6}{5} = \frac{n}{10}\]
Using simple cross-multiplication techniques, we have $5n = 60$ , and thus $\boxed{n = 012}$ . ~ nikenissan

## Solution 3
By the first equation, we get that $\sin(x)*\cos(x)=10^{-1}$ . We can let $\sin(x)=a$ , $\cos(x)=b$ . Thus $ab=\frac{1}{10}$ . By the identity $\sin^2x+\cos^2x=1$ , we get that $a^2+b^2=1$ . Solving this, we get $a+b=\sqrt{\frac{12}{10}}$ . So we have
\[\log\left(\sqrt{\frac{12}{10}}\right)=\frac12(\log(n)-1)\] \[2\log\left(\sqrt{\frac{12}{10}}\right)=\log(n)-1\] \[\log\left(\frac{12}{10}\right)+1=\log(n)\] \[\log\left(\frac{12}{10}\right)+\log(10)=\log(n)\] \[\log\left(\frac{12}{10}\times 10\right)=\log(12)=\log(n)\]
From here it is obvious that $\boxed{n=012}$ .
~yofro

## Solution 4
Let $\log{x} = \log_{10}{x}.$ Through basic log properties, we see that $\log{a} + \log{b} = \log{(ab)}.$ Thus, we see that $\log{(\sin{x})} + \log{(\cos{x})} = \log{(\sin{x}\cos{x})} = -1.$ Simplifying, we get:
\begin{align*} \log{(\sin{x}\cos{x})} &= -1 \\ \sin{x}\cos{x} &= 10^{-1} = \frac{1}{10} \end{align*}
Next, we can manipulate the second equation to get:
\begin{align*} \log{(\sin{x} + \cos{x})} &= \frac{1}{2}(\log{n}-1) \\ 2\log{(\sin{x} + \cos{x})} &= \log{n}-1 \\ \log{(\sin{x} + \cos{x})^2} + 1 &= \log{n} \end{align*}
Expanding $(\sin{x} + \cos{x})^2,$ we get:
\begin{align*} \log{(\sin^2{x} + \cos^2{x} + 2\sin{x}\cos{x})} + 1 &= \log{n} \\ \log{(1 + 2\sin{x}\cos{x})} + 1 &= \log{n} \\ \log{(1 + \frac{2}{10})} + \log{10} &= \log{n} \\ \log{(\frac{12}{10} \cdot 10)} = \log{n} \\ \log{12} = \log{n} \end{align*}
Finally, we see that $n = \boxed{012}.$
~ Cheetahboy93
These problems are copyrighted © by the Mathematical Association of America.