# 2018 AMC 10A Problem 14

## Problem

What is the greatest integer less than or equal to \[\frac{3^{100}+2^{100}}{3^{96}+2^{96}}?\]

$\textbf{(A) }80\qquad \textbf{(B) }81 \qquad \textbf{(C) }96 \qquad \textbf{(D) }97 \qquad \textbf{(E) }625\qquad$

## Solution 1
We write \[\frac{3^{100}+2^{100}}{3^{96}+2^{96}}=\frac{3^{96}}{3^{96}+2^{96}}\cdot\frac{3^{100}}{3^{96}}+\frac{2^{96}}{3^{96}+2^{96}}\cdot\frac{2^{100}}{2^{96}}=\frac{3^{96}}{3^{96}+2^{96}}\cdot 81+\frac{2^{96}}{3^{96}+2^{96}}\cdot 16.\] Hence we see that our number is a weighted average of 81 and 16, extremely heavily weighted toward 81. Hence the number is ever so slightly less than 81, so the answer is $\boxed{\textbf{(A) }80}$ .

## Solution 2
Let's set this value equal to $x$ . We can write \[\frac{3^{100}+2^{100}}{3^{96}+2^{96}}=x.\] Multiplying by $3^{96}+2^{96}$ on both sides, we get \[3^{100}+2^{100}=x(3^{96}+2^{96}).\] Now let's take a look at the answer choices. We notice that $81$ , choice $B$ , can be written as $3^4$ . Plugging this into our equation above, we get \[3^{100}+2^{100} \stackrel{?}{=} 3^4(3^{96}+2^{96}) \Rightarrow 3^{100}+2^{100} \stackrel{?}{=} 3^{100}+3^4\cdot 2^{96}.\] The right side is larger than the left side because \[2^{100} \leq 2^{96}\cdot 3^4.\] This means that our original value, $x$ , must be less than $81$ . The only answer that is less than $81$ is $80$ so our answer is $\boxed{A}$ .
~Nivek

## Solution 3
\[\frac{3^{100}+2^{100}}{3^{96}+2^{96}}=\frac{2^{96}\left(\frac{3^{100}}{2^{96}}\right)+2^{96}\left(2^{4}\right)}{2^{96}\left(\frac{3}{2}\right)^{96}+2^{96}(1)}=\frac{\frac{3^{100}}{2^{96}}+2^{4}}{\left(\frac{3}{2}\right)^{96}+1}=\frac{\frac{3^{100}}{2^{100}}\cdot2^{4}+2^{4}}{\left(\frac{3}{2}\right)^{96}+1}=\frac{2^{4}\left(\frac{3^{100}}{2^{100}}+1\right)}{\left(\frac{3}{2}\right)^{96}+1}.\]
We can ignore the 1's on the end because they won't really affect the fraction. So, the answer is very very very close but less than the new fraction.
\[\frac{2^{4}\left(\frac{3^{100}}{2^{100}}+1\right)}{\left(\frac{3}{2}\right)^{96}+1}<\frac{2^{4}\left(\frac{3^{100}}{2^{100}}\right)}{\left(\frac{3}{2}\right)^{96}},\]
\[\frac{2^{4}\left(\frac{3^{100}}{2^{100}}\right)}{\left(\frac{3}{2}\right)^{96}}=\frac{3^{4}}{2^{4}}*2^{4}=3^{4}=81.\]
So, our final answer is very close but not quite 81, and therefore the greatest integer less than the number is $\boxed{(A) 80}$

## Solution 4
Let $x=3^{96}$ and $y=2^{96}$ . Then our fraction can be written as $\frac{81x+16y}{x+y}=\frac{16x+16y}{x+y}+\frac{65x}{x+y}=16+\frac{65x}{x+y}$ . Notice that $\frac{65x}{x+y}<\frac{65x}{x}=65$ . So , $16+\frac{65x}{x+y}<16+65=81$ . And our only answer choice less than 81 is $\boxed{(A) 80}$ (RegularHexagon)

## Solution 5
Let $x=\frac{3^{100}+2^{100}}{3^{96}+2^{96}}$ . Multiply both sides by $(3^{96}+2^{96})$ , and expand. Rearranging the terms, we get $3^{96}(3^4-x)+2^{96}(2^4-x)=0$ . The left side is decreasing, and it is negative when $x=81$ . This means that the answer must be less than $81$ ; therefore the answer is $\boxed{(A)}$ .

## Solution 6 (eyeball it)
A faster solution. Recognize that for exponents of this size $3^{n}$ will be enormously greater than $2^{n}$ , so the terms involving $2$ will actually have very little effect on the quotient. Now we know the answer will be very close to $81$ .
Notice that the terms being added on to the top and bottom are in the ratio $\frac{1}{16}$ with each other, so they must pull the ratio down from 81 very slightly. (In the same way that a new test score lower than your current cumulative grade always must pull that grade downward.) Answer: $\boxed{\text{\textbf{(A)}}}$ .

## Solution 7
Notice how $\frac{3^{100}+2^{100}}{3^{96}+2^{96}}$ can be rewritten as $\frac{81(3^{96})+16(2^{96})}{3^{96}+2^{96}}=\frac{81(3^{96})+81(2^{96})}{3^{96}+2^{96}}-\frac{65(2^{96})}{3^{96}+2^{96}}=81-\frac{65(2^{96})}{3^{96}+2^{96}}$ . Note that $\frac{65(2^{96})}{3^{96}+2^{96}}<1$ , so the greatest integer less than or equal to $\frac{3^{100}+2^{100}}{3^{96}+2^{96}}$ is $80$ or $\boxed{\textbf{(A)}}$ ~blitzkrieg21

## Solution 8
For positive $a, b, c, d$ , if $\frac{a}{b}<\frac{c}{d}$ then $\frac{c+a}{d+b}<\frac{c}{d}$ . Let $a=2^{100}, b=2^{96}, c=3^{100}, d=3^{96}$ . Then $\frac{c}{d}=3^4$ . So answer is less than 81, which leaves only one choice, 80.
- Note that the algebra here is synonymous to the explanation given in Solution 6. This is the algebraic reason to the logic of if you get a test score with a lower percentage than your average (no matter how many points/percentage of your total grade it was worth), it will pull your overall grade down.
~ ccx09

## Solution 9
Try long division, and notice putting $3^4=81$ as the denominator is too big and putting $3^4-1=80$ is too small. So we know that the answer is between $80$ and $81$ , yielding $80$ as our answer.

## Solution 10 (Using the answer choices)

## Solution 10.1
We can compare the given value to each of our answer choices. We already know that it is greater than $80$ because otherwise there would have been a smaller answer, so we move onto $81$ . We get:
$\frac{3^{100}+2^{100}}{3^{96}+2^{96}} \text{ ? } 3^4$
Cross multiply to get:
$3^{100}+2^{100} \text{ ? }3^{100}+(2^{96})(3^4)$
Cancel out $3^{100}$ and divide by $2^{96}$ to get $2^{4} \text{ ? }3^4$ . We know that $2^4 < 3^4$ , which means the expression is less than $81$ so the answer is $\boxed{(A)}$ .

## Solution 10.2
We know this will be between 16 and 81 because $\frac{3^{100}}{3^{96}} = 3^4 = 81$ and $\frac{2^{100}}{2^{96}} = 2^4 = 16$ . $80=\boxed{(A)}$ is the only option choice in this range.
### Explanation for why 80 is indeed the floor
We need $3^{100}+2^{100} > 80 \cdot 3^{96} + 5 \cdot 2^{100}$ . Since $3^{100} = 81\cdot 3^{96}$ , this translates to \[3^{96} > 4\cdot 2^{100} = 64\cdot 2^{96}.\] We now prove that $(3/2)^k > k$ for all positive integers $k$ . Clearly, $(3/2)^2 = 2.25 > 2$ . Assume $(3/2)^k > k$ where $k\ge 2$ . Then $\left(\frac{3}{2}\right)^{k+1} > \frac{3k}{2} = k + \frac{k}{2}$ . But since $k/2 \ge 1$ , we have that $(3/2)^{k+1} > k+1$ . By induction (and $k=1$ is trivial), the claim is proven.
Thus, $\left(\frac{3}{2}\right)^{96} > 96 > 64$ . Writing this proof backwards and dividing both sides of the initial equation by $80$ yields $80 < \frac{3^{100}+2^{100}}{3^{96}+2^{96}} < 81$ .

## Solution 11
We know that in this problem, $3^{96}+2^{96}$ times some number is equal to $3^{100}+2^{100}$ . Multiplying answer $\boxed{\textbf{(B)}}$ or 81 to $3^{96}+2^{96}$ gives us $3^{100}+2^{96}\cdot3^4$ . We know that $3^4\cdot2^{96}$ is greater than $2^{100}$ , so that means $\boxed{\textbf{(B)}}$ or 81 is too big. That leaves us with only one solution: $80=\boxed{\textbf{(A) } 80}.$
~ Terribleteeth

## Solution 12
Dividing by $2^{96}$ in both numerator and denominator, this fraction can be rewritten as \[\frac{81 \times (1.5)^{96} + 16}{(1.5)^{96} + 1}.\] Notice that the $+1$ and the $+16$ will be so insignificant compared to a number such as $(1.5)^{96},$ and that thereby the fraction will be ever so slightly less than $81$ . Thereby, we see that the answer is $\boxed{\text{(A)} \ 80}.$
~ Professor-Mom [& wow there are now 12 sols to this problem :o :o :o this problem xDD]

## Solution 13 (slightly similar to Solution 7)
If you multiply $(3^{96} + 2^{96})$ by $(3^{4} + 2^{4})$ (to get the exponent up to 100), you'll get $(3^{100} + 2^{100}) + 3^{96} \cdot 2^{4} + 2^{96} \cdot 3^{4}$ . Thus, in the numerator, if you add and subtract by $3^{96} \cdot 2^{4}$ and $2^{96} \cdot 3^{4}$ , you'll get $\frac{(3^{4} + 2^{4})(3^{100} + 2^{100}) - 3^{96} \cdot 2^{4} - 2^{96} \cdot 3^{4}}{3^{96}+2^{96}}$ . You can then take out out the first number to get $3^{4} + 2^{4} - \frac{3^{96} \cdot 2^{4} + 2^{96} \cdot 3^{4}}{3^{96}+2^{96}}$ . This can then be written as $87 - \frac{16 \cdot 3^{96} + 16 \cdot 2^{96} + 75 \cdot 2^{96}}{3^{96}+2^{96}}$ , factoring out the 16 and splitting the fraction will give you $87 - 16 - \frac{65 \cdot 2^{96}}{3^{96}+2^{96}}$ , giving you $81 - \frac{65 \cdot 2^{96}}{3^{96}+2^{96}}$ . While you can roughly say that $\frac{65 \cdot 2^{96}}{3^{96}+2^{96}} < 1$ you can also notice that the only answer choice less than 81 is 80, thus the answer is $\boxed{\text{(A)} \ 80}.$
~ Zeeshan12 [Now there's 13 :) ]

## Solution 14 (Factoring)
If you factor out $3^{100}$ from the numerator and $3^{96}$ from the denominator, you will get $\frac{3^{100}\left(1+(\frac{2}{3}\right)^{100})}{3^{96}\left(1+(\frac{2}{3}\right)^{96})}$ . Divide the numerator and denominator by $3^{96}$ to get $\frac{81\left(1+(\frac{2}{3}\right)^{100})}{\left(1+(\frac{2}{3}\right)^{96})}$ . We see that every time we multiply $\frac{2}{3}$ by itself, it slightly decreases, so $1+(\frac{2}{3})^{100}$ will be ever so slightly smaller than $1+(\frac{2}{3})^{96}$ . Thus, the decimal representation of $\frac{\left(1+(\frac{2}{3}\right)^{100})}{\left(1+(\frac{2}{3}\right)^{96})}$ will be extremely close to $1$ , so our solution will be the largest integer that is less than $81$ . Thus, the answer is $\boxed{\text{(A)} \ 80}.$
~andy_lee

## Video Solution (HOW TO THINK CREATIVELY!)
https://youtu.be/zb0AcwIDqdg
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .