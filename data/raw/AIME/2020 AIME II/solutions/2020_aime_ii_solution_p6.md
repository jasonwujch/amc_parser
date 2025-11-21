# 2020 AIME II Problem 6

## Problem

Define a sequence recursively by $t_1 = 20$ , $t_2 = 21$ , and \[t_n = \frac{5t_{n-1}+1}{25t_{n-2}}\] for all $n \ge 3$ . Then $t_{2020}$ can be expressed as $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution
Let $t_n=\frac{s_n}{5}$ . Then, we have $s_n=\frac{s_{n-1}+1}{s_{n-2}}$ where $s_1 = 100$ and $s_2 = 105$ . By substitution, we find $s_3 = \frac{53}{50}$ , $s_4=\frac{103}{105\cdot50}$ , $s_5=\frac{101}{105}$ , $s_6=100$ , and $s_7=105$ . So $s_n$ has a period of $5$ . Thus $s_{2020}=s_5=\frac{101}{105}$ . So, $\frac{101}{105\cdot 5}\implies 101+525=\boxed{626}$ . ~mn28407

## Solution 2 (Official MAA)
More generally, let the first two terms be $a$ and $b$ and replace $5$ and $25$ in the recursive formula by $k$ and $k^2$ , respectively. Then some algebraic calculation shows that \[t_3 = \frac{b\,k+1}{a\, k^2},~~t_4 = \frac{a\, k + b\,k+1}{a\,b\, k^3},~~ t_5 = \frac{a\,k+1}{b\, k^2},~~ t_6 = a, \text{~ and ~}t_7 =b,\] so the sequence is periodic with period $5$ . Therefore \[t_{2020} = t_{5} = \frac{20\cdot 5 +1}{21\cdot 25} = \frac{101}{525}.\] The requested sum is $101+525=626$ .

## Solution 3
Let us examine the first few terms of this sequence and see if we can find a pattern. We are obviously given $t_1 = 20$ and $t_2 = 21$ , so now we are able to determine the numerical value of $t_3$ using this information: \[t_3 = \frac{5t_{3-1}+1}{25t_{3-2}} = \frac{5t_{2}+1}{25t_{1}} = \frac{5(21) + 1}{25(20)} = \frac{105 + 1}{500}t_3 = \frac{106}{500} = \frac{53}{250}\] \[t_4 = \frac{5t_{4-1}+1}{25t_{4-2}} = \frac{5t_{3}+1}{25t_{2}} = \frac{5(\frac{53}{250}) + 1}{25(21)} = \frac{\frac{53}{50} + 1}{525} = \frac{\frac{103}{50}}{525} = \frac{103}{26250}\] \[t_5 = \frac{5t_{5-1}+1}{25t_{5-2}} = \frac{5t_{4}+1}{25t_{3}} = \frac{5(\frac{103}{26250}) + 1}{25(\frac{53}{250})} = \frac{\frac{103}{5250} + 1}{\frac{53}{10}} = \frac{\frac{5353}{5250}}{\frac{53}{10}} = \frac{101}{525}\] \[t_6 = \frac{5t_{6-1}+1}{25t_{6-2}} = \frac{5t_{5}+1}{25t_{4}} = \frac{5(\frac{101}{525}) + 1}{25(\frac{103}{26250})} = \frac{\frac{101}{105} + 1}{\frac{103}{1050}} = \frac{\frac{206}{105}}{\frac{103}{1050}} \implies t_6 = 20\]
Alas, we have figured this sequence is period 5! But since $2020 \equiv 5 \pmod 5$ , we can state that $t_{2020} = t_5 = \frac{101}{525}$ . According to the original problem statement, our answer is $\boxed{626}$ . ~ nikenissan

## Video Solution
https://youtu.be/_JTWJxbDC1A ~ CNCM

## Video Solution 2
https://youtu.be/__B3pJMpfSk
~IceMatrix
### Quick way to notice recursion loop
Round the first two values to both be 20. Then, the next element can be rounded to $\frac{1}{5}$ . $t_4$ can then be quickly calculated to around $\frac{1}{250}$ , and $t_5$ can be rounded to $\frac{1}{5}$ . $t_6$ turns out to be around 20, which means that there is probably a loop with period 5. The rest of the solution proceeds normally.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .