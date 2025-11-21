# 2016 AIME II Problem 1

## Problem

Initially Alex, Betty, and Charlie had a total of $444$ peanuts. Charlie had the most peanuts, and Alex had the least. The three numbers of peanuts that each person had formed a geometric progression. Alex eats $5$ of his peanuts, Betty eats $9$ of her peanuts, and Charlie eats $25$ of his peanuts. Now the three numbers of peanuts each person has forms an arithmetic progression. Find the number of peanuts Alex had initially.

## Solution 1
Let $r$ be the common ratio, where $r>1$ . We then have $ar-9-(a-5)=a(r-1)-4=ar^{2}-25-(ar-9)=ar(r-1)-16$ . We now have, letting, subtracting the 2 equations, $ar^{2}+-2ar+a=12$ , so we have $3ar=432,$ or $ar=144$ , which is how much Betty had. Now we have $144+\dfrac{144}{r}+144r=444$ , or $144(r+\dfrac{1}{r})=300$ , or $r+\dfrac{1}{r}=\dfrac{25}{12}$ , which solving for $r$ gives $r=\dfrac{4}{3}$ , since $r>1$ , so Alex had $\dfrac{3}{4} \cdot 144=\boxed{108}$ peanuts.

## Solution 2 (Quadratic Formula)
Let $a$ be Alex's peanuts and $k$ the common ratio. Then we have $a(k^2+k+1)=444$ . Adding $k$ to both sides and factoring,
\[\frac{444}{a}+k=(k+1)^2\]
For the common difference, $ak=5-(a-5)=ak^2-25-(ak-9)$ . Simplifying, $k^2-2k+1=\frac{12}{a}$ . Factoring, \[(k-1)^2=\frac{12}{a}\]
\[(k+1)^2-(k-1)^2=4k \implies 4k=\frac{444-12}{a}+k \implies k=\frac{144}{a}\]
Substitute $k$ in the second equation to get $(\frac{144-a}{a})^2=\frac{12}{a}$ . Expanding and applying the quadratic formula, \[a=150\pm\frac{\sqrt{300^2-4(144^2)}}{2}\] Taking out $4^2\cdot3^2$ from under the radical leaves \[a=150\pm6\sqrt{625-576}=108, 192\] Since Alex's peanut number was the lowest of the trio, and $3*192>444$ , Alex initially had $\boxed{108}$ peanuts.

## Solution 3
Let the initial numbers of peanuts Alex, Betty and Charlie had be $a$ , $b$ , and $c$ respectively. Let the final numbers of peanuts, after eating, be $a'$ , $b'$ , and $c'$ .
We are given that $a + b + c = 444$ . Since a total of $5 + 9 + 25 = 39$ peanuts are eaten, we must have $a' + b' + c' = 444 - 39 = 405$ . Since $a'$ , $b'$ , and $c'$ form an arithmetic progression, we have that $a' = b' - x$ and $c' = b' + x$ for some integer $x$ . Substituting yields $3b' = 405$ and so $b' = 135$ . Since Betty ate $9$ peanuts, it follows that $b = b' + 9 = 144$ .
Since $a$ , $b$ , and $c$ form a geometric progression, we have that $a = \frac{b}{r}$ and $c = br$ . Multiplying yields $ac = b^2 = 144^2$ . Since $a + c = 444 - b = 300$ , it follows that $a = 150 - \lambda$ and $c = 150 + \lambda$ for some integer $\lambda$ . Substituting yields $(150-\lambda)(150+\lambda) = 144^2$ , which expands and rearranges to $\lambda^2 = 150^2-144^2 = 42^2$ . Since $\lambda > 0$ , we must have $\lambda = 42$ , and so $a = 150 - \lambda = \boxed{108}$ .

## Solution 4
Bashing is not difficult. All we have to consider is the first equation. We can write it as $x*(1+r+r^2) = 444$ . The variable $x$ must be an integer, and after trying all the factors of $444$ , it's clear that $r$ is a fraction smaller than $10$ . When calculating the coefficient of $x$ , we must consider that the fraction produced will very likely have a numerator that divides $444$ . Trying a couple will make it easier to find the fraction, and soon you will find that $\frac{4}{3}$ gives a numerator of $37$ , a rather specific factor of $444$ . Solving for the rest will give you an integer value of $\boxed{108}$ . This is by no means a good solution, but it may be faster in a competition if you don't want to mess with several other equations. This is purely up to different individuals.

## Solution 5
Let $b$ be the finish number of Betty's peanuts. Then \[3b = 444-(5 + 9 + 25) = 405 = 3 \cdot 135 \implies b = 135, b+ 9 = 144.\]
Let $k > 1$ be the common ratio. Then \[\frac{144}{k} + 144 + k \cdot 144 = 444 \implies \frac{144}{k} + k \cdot 144 = 300\implies \frac{12}{k} + k \cdot 12 = 25\implies k = \frac{4}{3} \implies \frac {144\cdot 3}{4} = \boxed {108}.\]
vladimir.shelomovskii@gmail.com, vvsss
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .