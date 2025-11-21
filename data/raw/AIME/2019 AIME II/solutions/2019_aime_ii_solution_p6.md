# 2019 AIME II Problem 6

## Problem

In a Martian civilization, all logarithms whose bases are not specified are assumed to be base $b$ , for some fixed $b\ge2$ . A Martian student writes down \[3\log(\sqrt{x}\log x)=56\] \[\log_{\log x}(x)=54\] and finds that this system of equations has a single real number solution $x>1$ . Find $b$ .

## Solution 1
Using change of base on the second equation to base b, \[\frac{\log x}{\log \log_{b}{x}}=54\] \[\log x = 54 \cdot \log\log_{b}{x}\] \[x = (\log_{b}{x})^{54}\] Note by dolphin7 - you could also just rewrite the second equation in exponent form.
Substituting this into the $\sqrt x$ of the first equation, \[3\log_{b}{((\log_{b}{x})^{27}\log_{b}{x})} = 56\] \[3\log_{b}{(\log_{b}{x})^{28}} = 56\] \[\log_{b}{(\log_{b}{x})^{84}} = 56\]
We can manipulate this equation to be able to substitute $x = (\log_{b}{x})^{54}$ a couple more times: \[\log_{b}{(\log_{b}{x})^{54}} = 56 \cdot \frac{54}{84}\] \[\log_{b}{x} = 36\] \[(\log_{b}{x})^{54} = 36^{54}\] \[x = 6^{108}\]
However, since we found that $\log_{b}{x} = 36$ , $x$ is also equal to $b^{36}$ . Equating these, \[b^{36} = 6^{108}\] \[b = 6^3 = \boxed{216}\]

## Solution 2
We start by simplifying the first equation to \[3\log_{b}{(\sqrt{x}\log x)}=\log_{b}{(x^{\frac{3}{2}}\log^3x)}=56\] \[x^\frac{3}{2}\cdot \log_b^3x=b^{56}\] Next, we simplify the second equation to \[\log_{\log(x)}(x)=\frac{\log_b(x)}{\log_b(\log_b(x))}=54\] \[\log_bx=54\log_b(\log_b(x))=\log_b(\log_b^{54}(x))\] \[x=\log_b^{54}x\] Substituting this into the first equation gives \[\log_b^{54\cdot \frac{3}{2}}(x)\cdot \log_b^3x=\log_b^{84}x=b^{56}\] \[x=b^{b^{\frac{56}{84}}}=b^{b^{\frac{2}{3}}}\] Plugging this into $x=\log_b^{54}x$ gives \[b^{b^{\frac{2}{3}}}=\log_b^{54}(b^{b^\frac{2}{3}})=b^{\frac{2}{3}\cdot 54}=b^{36}\] \[b^{\frac{2}{3}}=36\] \[b=36^{\frac{3}{2}}=6^3=\boxed{216}\] -ktong

## Solution 3
Apply change of base to \[\log_{\log x}(x)=54\] to yield: \[\frac{\log_b(x)}{\log_b(\log_b(x))}=54\] which can be rearranged as: \[\frac{\log_b(x)}{54}=\log_b(\log_b(x))\] Apply log properties to \[3\log(\sqrt{x}\log x)=56\] to yield: \[3(\frac{1}{2}\log_b(x)+\log_b(\log_b(x)))=56\Rightarrow\frac{1}{2}\log_b(x)+\log_b(\log_b(x))=\frac{56}{3}\] Substituting \[\frac{\log_b(x)}{54}=\log_b(\log_b(x))\] into the equation $\frac{1}{2}\log_b(x)+\log_b(\log_b(x))=\frac{56}{3}$ yields: \[\frac{1}{2}\log_b(x)+\frac{\log_b(x)}{54}=\frac{28\log_b(x)}{54}=\frac{56}{3}\] So \[\log_b(x)=36.\] Substituting this back in to \[\frac{\log_b(x)}{54}=\log_b(\log_b(x))\] yields \[\frac{36}{54}=\log_b(36).\] So, \[b^{\frac{2}{3}}=36\Rightarrow \boxed{b=216}\]
-Ghazt2002

## Solution 4
1st equation: \[\log (\sqrt{x}\log x)=\frac{56}{3}\] \[\log(\sqrt x)+\log(\log x)=\frac{1}{2}\log x+\log(\log x)=\frac{56}{3}\] 2nd equation: \[x=(\log x)^{54}\] So now substitute $\log x=a$ and $x=b^a$ : \[b^a=a^{54}\] \[b=a^{\frac{54}{a}}\] We also have that \[\frac{1}{2}a+\log_{a^\frac{54}{a}} a=\frac{56}{3}\] \[\frac{1}{2}a+\frac{1}{54}a=\frac{56}{3}\] This means that $\frac{14}{27}a=\frac{56}{3}$ , so \[a=36\] \[b=36^{\frac{54}{36}}=36^\frac{3}{2}=\boxed{216}\] .
-Stormersyle

## Solution 5 (Substitution)
Let $y = \log _{b} x$ Then we have \[3\log _{b} (y\sqrt{x}) = 56\] \[\log _{y} x = 54\] which gives \[y^{54} = x\] Plugging this in gives \[3\log _{b} (y \cdot y^{27}) = 3\log _{b} y^{28} = 56\] which gives \[\log _{b} y = \dfrac{2}{3}\] so \[b^{2/3} = y\] By substitution we have \[b^{36} = x\] which gives \[y = \log _{b} x = 36\] Plugging in again we get \[b = 36^{3/2} = \fbox{216}\]
--Hi3142

## Solution 6 (Also Substitution)
This system of equations looks complicated to work with, so we let $a=\log_bx$ to make it easier for us to read.
Now, the first equation becomes $3\log(\sqrt x \cdot a) = 56 \implies \log(\sqrt{x}\cdot a)=\frac{56}3$ .
The second equation, $\log_{\log(x)}(x)=54$ gives us $\underline{a^{54} = x}$ .
Let's plug this back into the first equation to see what we get: $\log_b(\sqrt{a^{54}}\cdot a)=\frac{56}3$ , and simplifying, $\log_b(a^{27}\cdot a^1)=\log_b(a^{28})=\frac{56}{3}$ , so $b^{\frac{56}3}=a^{28}\implies \underline{b^{\frac 23}=a}$ .
Combining this new finding with what we had above $a^{54} = (b^{\frac 23})^{54} = x\implies \mathbf{b^{36} =x}$ .
Now that we've expressed one variable in terms of the other, we can plug this into either equation, say equation 1. Then we get $\log_b(\sqrt{b^{36}}\cdot\log_b(b^{36})=\frac{56}3\implies$ $\log_b(b^{18}\cdot 36)=\frac{56}3\implies b^{\frac{56}3}=b^{18}\cdot 36$ .
Finally, that gives us that $\frac{b^{\frac{56}3}}{b^{18}}=36\implies b^{\frac{56}{3}-18}=b^{\frac{56}{3}-\frac{54}{3}}=b^{\frac 23}=36\implies b=36^{\frac 32}=6^3$ . Thus, $b=\boxed{216}$ .
~BakedPotato66

## Solution 7 (Easy System of Equations)
Using change of base on the second equation, we have
\[\frac{\log_{b} x}{\log_{b} \log_{b} x} = 54\]
Using log rules on the first equation, we have
\[\frac{3}{2} \log_{b} x + 3 \log_{b} \log_{b} x = 56\]
We notice that $\log_{b} x$ and $\log_{b} \log_{b} x$ are in both equations. Thus, we set $m = \log_{b} x$ and $n = \log_{b} \log_{b} x$ and we have
\[\frac{3}{2} m + 3n = 56\] \[\frac{m}{n} = 54\]
Solving this yields $m = 36$ , $n = \frac{2}{3}$ .
Now, $n = \log_{b} \log_{b} x = \log_{b} m = \log_{b} 36$ , so we have $\log_{b} 36 = \frac{2}{3}$ . Solving this yields $b = \boxed{216}$ .
~ adam_zheng

## Solution 8 (Definition of Logarithm)
The second equation implies that \[\log_{\log_b x} x=54\implies (\log_b x)^{54}=x \implies \log_b x=x^{\frac{1}{54}}\] The first equation implies that \[3\log_b(\sqrt{x} \log_b x)=56 \implies b^{\frac{56}{3}}=\sqrt{x} \log_b x\] Substituting the first result into the second gives us \[b^{\frac{56}{3}}=x^{\frac{1}{2}}\cdot x^{\frac{1}{54}} \implies b=x^{\frac{1}{36}}.\] Because $b^{36}=x,$ $\log_b x=36$ by the definition of a logarithm. Substituting this into the second equation, \[\log_{36} x=54 \implies x=36^{54}.\] Finally, \[b=(36^{54})^{\frac{1}{36}}=36^{54\cdot\frac{1}{36}}=6^{2*\frac{3}{2}}=6^3=\boxed{216}.\]
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .