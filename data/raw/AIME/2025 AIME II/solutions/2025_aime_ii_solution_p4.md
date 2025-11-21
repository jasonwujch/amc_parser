# 2025 AIME II Problem 4

## Problem

The product \[\prod^{63}_{k=4} \frac{\log_k (5^{k^2 - 1})}{\log_{k + 1} (5^{k^2 - 4})} = \frac{\log_4 (5^{15})}{\log_5 (5^{12})} \cdot \frac{\log_5 (5^{24})}{\log_6 (5^{21})}\cdot \frac{\log_6 (5^{35})}{\log_7 (5^{32})} \cdots \frac{\log_{63} (5^{3968})}{\log_{64} (5^{3965})}\] is equal to $\tfrac mn,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Solution 1
We can rewrite the equation as:
\begin{align*} &= \dfrac{15}{12} \cdot \dfrac{24}{21} \cdot \dfrac{35}{32} \cdot \dots \cdot \dfrac{3968}{3965} \cdot \dfrac{\log_4{5}}{\log_{64}{5}} \\ &= \log_4{64} \cdot \dfrac{(4+1)(4-1)(5+1)(5-1)\cdot \dots \cdot (63+1)(63-1)}{(4+2)(4-2)(5+2)(5-2)\cdot \dots \cdot (63+2)(63-2)} \\ &= 3 \cdot \dfrac{5 \cdot 3 \cdot 6 \cdot 4 \cdot \dots \cdot 64 \cdot 62}{6 \cdot 2 \cdot 7 \cdot 3 \cdot \dots \cdot 65 \cdot 61} \\ &= 3 \cdot \dfrac{5 \cdot 62}{65 \cdot 2} \\ &= 3 \cdot \dfrac{5 \cdot 2 \cdot 31}{5 \cdot 13 \cdot 2} \\ &= 3 \cdot \dfrac{31}{13} \\ &= \dfrac{93}{13} \end{align*}
Desired answer: $93 + 13 = \boxed{106}$
(Feel free to correct any $\LaTeX$ and formatting.)
~ Mitsuihisashi14
~ $\LaTeX$ by Tacos_are_yummy_1
~ Additional edits by aoum

## Solution 2
We can move the exponents to the front of the logarithms like this: \begin{align*} \frac{\log_4 (5^{15})}{\log_5 (5^{12})} \cdot \frac{\log_5 (5^{24})}{\log_6 (5^{21})}\cdot \frac{\log_6 (5^{35})}{\log_7 (5^{32})} \cdots = \frac{15\log_4 (5)}{12\log_5 (5)} \cdot \frac{24\log_5 (5)}{21\log_6 (5)}\cdot \frac{35\log_6 (5)}{32\log_7 (5)} \cdots \end{align*} Now we multiply the logs and fractions separately. Let's do it for the logs first: \begin{align*} \frac{\log_4 (5)}{\log_5 (5)} \cdot \frac{\log_5 (5)}{\log_6 (5)}\cdot \frac{\log_6 (5)}{\log_7 (5)} \cdots \frac{\log_{63} (5)}{\log_{64} (5)} = \frac{\log_4 (5)}{\log_{64} (5)} = 3 \end{align*} Now fractions: \begin{align*} \frac{15}{12} \cdot \frac{24}{21} \cdot \frac{35}{32} \cdots = \frac{3\cdot 5}{2\cdot 6} \cdot \frac{4\cdot 6}{3\cdot 7} \cdot \frac{5\cdot 7}{4\cdot 8} \cdots \frac{62\cdot 64}{61\cdot 65} = \frac{5}{2} \cdot \frac{62}{65} = \frac{31}{13} \end{align*} Multiplying these together gets us the original product, which is $\frac{31}{13} \cdot 3 = \frac{93}{13}$ . Thus $m+n=\boxed{106}$ .
~ Edited by aoum

## Solution 3
Using logarithmic identities and the change of base formula, the product can be rewritten as \[\prod_{k=4}^{63}\frac{k^2-1}{k^2-4}\frac{\log(k+1)}{\log(k)}\] . Then we can separate this into two series. The latter series is a telescoping series, and it can be pretty easily evaluated to be $\frac{\log(64)}{\log(4)}=3$ . The former can be factored as $\frac{(k-1)(k+1)}{(k-2)(k+2)}$ , and writing out the first terms could tell us that this is a telescoping series as well. Cancelling out the terms would yield $\frac{5}{2}\cdot\frac{62}{65}=\frac{31}{13}$ . Multiplying the two will give us $\frac{93}{13}$ , which tells us that the answer is $\boxed{106}$ .

## Solution 4 (thorough)
The product is equal to $\prod^{63}_{k=4} \frac{(k-1)(k+1)\log_k 5}{(k-2)(k+2)\log_{k + 1} 5}$ from difference of squares and properties of logarithms. We can now expand:
\begin{align*} \prod^{63}_{k=4} \frac{(k-1)(k+1)\log_k 5}{(k-2)(k+2)\log_{k + 1} 5} &= \prod^{63}_{k=4}\frac{\log_k 5}{\log_{k+1} 5} \cdot \frac{3 \cdot 5 \cdot 4 \cdot 6 \cdot 5 \cdot 7 \cdots 62 \cdot 64}{2 \cdot 6 \cdot 3 \cdot 7 \cdot 4 \cdot 8 \cdots 61 \cdot 65} \\ &= \frac{\log_4 5 \cdot \log_5 5 \cdots \log_{63} 5}{\log_{5} 5 \cdot \log_6 5 \cdots \log_{64} 5} \cdot \frac{3 \cdot 4 \cdot (5^2 \cdot 6^2 \cdots 62^2) \cdot 63 \cdot 64}{2 \cdot 3 \cdot 4 \cdot 5 \cdot (6^2 \cdot 7^2 \cdots 61^2) \cdot 62 \cdot 63 \cdot 64 \cdot 65} \\ &= \frac{\log_4 5}{\log_{64} 5} \cdot \frac{3 \cdot 4 \cdot 5^2 \cdot (6^2 \cdots 61^2) \cdot 62^2 \cdot 63 \cdot 64}{2 \cdot 3 \cdot 4 \cdot 5 \cdot (6^2 \cdots 61^2) \cdot 62 \cdot 63 \cdot 64 \cdot 65} \\ &= \log_{64} 4 \cdot \frac{3 \cdot 4 \cdot 5 \cdot 62}{2 \cdot 65} \\ &= 3 \cdot \frac{31}{13} \\ &= \frac{93}{13} \end{align*}
Thus the answer is $93+13=\boxed{106}$ .
~ eevee9406
~ Edited by aoum

## Video Solution
https://youtu.be/Mt_vVxWCo3k
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .