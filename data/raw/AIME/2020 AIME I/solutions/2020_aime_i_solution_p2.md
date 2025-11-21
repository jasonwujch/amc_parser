# 2020 AIME I Problem 2

## Problem

There is a unique positive real number $x$ such that the three numbers $\log_8{2x}$ , $\log_4{x}$ , and $\log_2{x}$ , in that order, form a geometric progression with positive common ratio. The number $x$ can be written as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Since these form a geometric series, $\frac{\log_2{x}}{\log_4{x}}$ is the common ratio. Rewriting this, we get $\frac{\log_x{4}}{\log_x{2}} = \log_2{4} = 2$ by base change formula. Therefore, the common ratio is 2. Now $\frac{\log_4{x}}{\log_8{2x}} = 2 \implies \log_4{x} = 2\log_8{2} + 2\log_8{x} \implies \frac{1}{2}\log_2{x} = \frac{2}{3} + \frac{2}{3}\log_2{x}$
$\implies -\frac{1}{6}\log_2{x} = \frac{2}{3} \implies \log_2{x} = -4 \implies x = \frac{1}{16}$ . Therefore, $1 + 16 = \boxed{017}$ .
~ JHawk0224

## Solution 2
If we set $x=2^y$ , we can obtain three terms of a geometric sequence through logarithm properties. The three terms are \[\frac{y+1}{3}, \frac{y}{2}, y.\] In a three-term geometric sequence, the middle term squared is equal to the product of the other two terms, so we obtain the following: \[\frac{y^2+y}{3} = \frac{y^2}{4},\] which can be solved to reveal $y = -4$ . Therefore, $x = 2^{-4} = \frac{1}{16}$ , so our answer is $\boxed{017}$ .
-molocyxu

## Solution 3
Let $r$ be the common ratio. We have \[r = \frac{\log_4{(x)}}{\log_8{(2x)}} = \frac{\log_2{(x)}}{\log_4{(x)}}\] Hence we obtain \[(\log_4{(x)})(\log_4{(x)}) = (\log_8{(2x)})(\log_2{(x)})\] Ideally we change everything to base $64$ and we can get: \[(\log_{64}{(x^3)})(\log_{64}{(x^3)}) = (\log_{64}{(x^6)})(\log_{64}{(4x^2)})\] Now divide to get: \[\frac{\log_{64}{(x^3)}}{\log_{64}{(4x^2)}} = \frac{\log_{64}{(x^6)}}{\log_{64}{(x^3)}}\] By change-of-base we obtain: \[\log_{(4x^2)}{(x^3)} = \log_{(x^3)}{(x^6)} = 2\] Hence $(4x^2)^2 = x^3 \rightarrow 16x^4 = x^3 \rightarrow x = \frac{1}{16}$ and we have $1+16 = \boxed{017}$ as desired.
~skyscraper

## Solution 4 (Exponents > Logarithms)
Let $r$ be the common ratio, and let $a$ be the starting term ( $a=\log_{8}{(2x)}$ ). We then have: \[\log_{8}{(2x)}=a, \log_{4}{(x)}=ar, \log_{2}{(x)}=ar^2\] Rearranging these equations gives: \[8^a=2x, 4^{ar}=x, 2^{ar^2}=x\] Deal with the last two equations first: Setting them equal gives: \[4^{ar}=2^{ar^2} \implies 2^{2ar}=2^{ar^2} \implies 2ar=ar^2 \implies r=2\] Using this value of $r$ , substitute into the first and second equations (or the first and third, it doesn't really matter) to get: \[8^a=2x, 4^{2a}=x\] Changing these to a common base gives: \[2^{3a}=2x, 2^{4a}=x\] Dividing the first equation by 2 on both sides yields: \[2^{3a-1}=x\] Setting these equations equal to each other and removing the exponent again gives: \[3a-1=4a \implies a=-1\] Substituting this back into the first equation gives: \[8^{-1}=2x \implies 2x=\frac{1}{8} \implies x=\frac{1}{16}\] Therefore, $m+n=1+16=\boxed{017}$
~IAmTheHazard

## Solution 5
We can relate the logarithms as follows:
\[\frac{\log_4{x}}{\log_8{(2x)}}=\frac{\log_2{x}}{\log_4{x}}\] \[\log_8{(2x)}\log_2{x}=\log_4{x}\log_4{x}\]
Now we can convert all logarithm bases to $2$ using the identity $\log_a{b}=\log_{a^c}{b^c}$ :
\[\log_2{\sqrt[3]{2x}}\log_2{x}=\log_2{\sqrt{x}}\log_2{\sqrt{x}}\]
We can solve for $x$ as follows:
\[\frac{1}{3}\log_2{(2x)}\log_2{x}=\frac{1}{4}\log_2{x}\log_2{x}\] \[\frac{1}{3}\log_2{(2x)}=\frac{1}{4}\log_2{x}\] \[\frac{1}{3}\log_2{2}+\frac{1}{3}\log_2{x}=\frac{1}{4}\log_2{x}\] We get $x=\frac{1}{16}$ . Verifying that the common ratio is positive, we find the answer of $\boxed{017}$ .
~QIDb602

## Solution 6
If the numbers are in a geometric sequence, the middle term must be the geometric mean of the surrounding terms. We can rewrite the first two logarithmic expressions as $\frac{1+\log_2{x}}{3}$ and $\frac{1}{2}\log_2{x}$ , respectively. Therefore: \[\frac{1}{2}\log_2{x}=\sqrt{\left(\frac{1+\log_2{x}}{3}\right)\left(\log_2{x}\right)}\] Let $n=\log_2{x}$ . We can rewrite the expression as: \[\frac{n}{2}=\sqrt{\frac{n(n+1)}{3}}\] \[\frac{n^2}{4}=\frac{n(n+1)}{3}\] \[4n(n+1)=3n^2\] \[4n^2+4n=3n^2\] \[n^2+4n=0\] \[n(n+4)=0\] \[n=0 \text{ and } -4\] Zero does not work in this case, so we consider $n=-4$ : $\log_2{x}=-4 \rightarrow x=\frac{1}{16}$ . Therefore, $1+16=\boxed{017}$ .
~Bowser498

## Solution 7
Again, by the Change of Base Formula, obtain that the common ratio is 2. If we let $y$ be the exponent of $\log_8 (2x)$ , then we have $8^y=2x;\:4^{2y}=x;\:2^{4y}=x.$ Wee can then divide the first equation by two to have the right side be $x$ . Also, $2^{4y}=\left(2^{4}\right)^y=16^y$ . Setting this equal to $\frac{8^y}{2}$ , we can divide the two equations to get $2^y=\frac12$ . Therefore, $y=-1$ . After that, we can raise $16$ to the $-1$ th power to get $x=16^{-1}\Rightarrow x=\frac1{16}$ . We then get our sum of $1+16=\boxed{\textbf{017}}$ .
~ SweetMango77

## Solution 8 (Official MAA)
By the Change of Base Formula the common ratio of the progression is \[\frac{\log_2 x}{\log_4 x} = \frac{\hphantom{m}\log_2x\hphantom{m}}{\frac{\log_2x}{\log_24}} = 2.\] Hence $x$ must satisfy \[2=\frac{\log_4 x}{\log_8 (2x)}= \frac{\log_2 x}{\log_2 4} \div \frac{\log_2(2x)}{\log_28} = \frac 32\cdot \frac{\log_2x}{1+\log_2x}.\] This is equivalent to $4 + 4\log_2x = 3\log_2x$ . Hence $\log_2x = -4$ and $x = \frac{1}{16}$ . The requested sum is $1+16 = 17$ .

## Solution 9
Let the series be $a,ar,ar^2$ . So, converting these logarithms into exponents we have $8^a = 2x$ , $4^{ar} = x$ , and $2^{ar^2} = x$ . So, setting the 2nd and 3rd equations equal, we have: \[4^{ar} = 2^{ar^2} \Longrightarrow 2^{2ar} = 2^{ar^2} \Longrightarrow 2ar = ar^2 \Longrightarrow r = 2\] . Plugging that into our 3rd equation, we have $2^{4a} = x$ . We recall that $8^a = 2x \Longrightarrow 2^{3a} = 2x$ . So, since $2^{4a} = x$ , $2x = 2^{4a+1}$ . Now, setting $2^{3a}$ , and $2^{4a+1}$ equal, we get $a = -1$ , so plugging into our first equation, we have \[\dfrac{1}{8} = 2x \Longrightarrow x = \dfrac{1}{16} \Longrightarrow \boxed{017}\]
-jb2015007

## Video Solutions
https://youtu.be/nPL7nUXnRbo (Unavailable)
Aarav Navani: https://youtu.be/4FvYVfhhTaQ
Mathematica De Estremo: https://youtu.be/FgrIgCyGVUI
https://youtu.be/mgRNqSDCvgM?t=281s (Unavailable)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .