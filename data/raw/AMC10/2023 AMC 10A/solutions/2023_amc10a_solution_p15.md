# 2023 AMC 10A Problem 15

## Problem

An even number of circles are nested, starting with a radius of $1$ and increasing by $1$ each time, all sharing a common point. The region between every other circle is shaded, starting with the region inside the circle of radius $2$ but outside the circle of radius $1.$ An example showing $8$ circles is displayed below. What is the least number of circles needed to make the total shaded area at least $2023\pi$ ?

[asy] filldraw(circle((0,0),8),gray); filldraw(circle((-1,0),7),white); filldraw(circle((-2,0),6),gray); filldraw(circle((-3,0),5),white); filldraw(circle((-4,0),4),gray); filldraw(circle((-5,0),3),white); filldraw(circle((-6,0),2),gray); filldraw(circle((-7,0),1),white); [/asy]

$\textbf{(A) } 46 \qquad \textbf{(B) } 48 \qquad \textbf{(C) } 56 \qquad \textbf{(D) } 60 \qquad \textbf{(E) } 64$

## Solution 1
Notice that the area of the shaded region is $(2^2\pi-1^2\pi)+(4^2\pi-3^2\pi)+(6^2\pi-5^2\pi)+ \cdots + (n^2\pi-(n-1)^2 \pi)$ for any even number $n$ .
Using the difference of squares, this simplifies to $(1+2+3+4+\cdots+n) \pi$ . So, we are basically finding the smallest $n$ such that $\frac{n(n+1)}{2}>2023 \Rightarrow n(n+1) > 4046$ . Since $60(61) > 60^2=3600$ , the only option higher than $60$ is $\boxed{\textbf{(E) } 64}$ .
~MrThinker

## Solution 2
After first observing the problem, we can work out a few of the areas.
1st area = $4\pi-\pi = 3\pi$
2nd area = $16\pi-9\pi = 7\pi$
3rd area = $36\pi-25\pi = 11\pi$
4th area = $64\pi-49\pi = 15\pi$
We can see that the pattern is an arithmetic sequence with first term $3$ and common difference $4$ . From here, we can start from the bottom of the answer choices and work our way up. As the question asks for the least number of circles needed total, we have to divide the number of total circles by 2.
We can find the sum of the first $32$ terms of the arithmetic sequence by using the formula.
The last term is: $3 + 4\cdot(32-1) = 127$ .
Then, we can find the sum: $(3+127)/2 \cdot 32 = 65\cdot32 = 2080$ . It is clear that $64$ works.
The next answer choice is $60$ , which we have to divide by 2 to get $30$ .
The last term is: $3 + 4\cdot(30-1) = 119$ .
The sum is: $(3+119)/2 \cdot 30 = 61\cdot30 = 1830$ . This does not work.
As answer choice $D$ does not work and $E$ does, we can conclude that the answer is $\boxed{\textbf{(E) } 64}$ .
~zgahzlkw

## Solution 3 (Similar to Solution 2)
We can easily see that all of the answer choices are even, which helps us solve this problem a little.
Let's just not consider the $\pi$ , since it is not that important, so let's cancel that out.
When we plug in 64, we get $64^2-63^2+62^2-61^2+\cdots +4^2-3^2+2^2-1^2$ . By difference of squares, we get $1+2+3+\cdots+62+63+64$ , which by the sum of an arithmetic sequence, is $\frac{64(64+1)}{2}$ , which is $2080$ .
Similarly, we can use this for answer choice $D$ , and we have $\frac{60(60+1)}{2}$ which is $1830$ .
So, we see that answer choice $D$ is too small to satisfy the requirements, so we conclude the answer is $\boxed{\textbf{(E) } 64}$ .
~ESAOPS

## Solution 4
We can consider making a table.
If there is 1 circle, the area of the shaded region is 0π. (We can write this as 0π.)
If there are 2 circles, the area of the shaded region is 3π. (We can write this as (1+2)π).
If there are 3 circles, the area of the shaded region is 3π. (We can write this as (1+2)π).
If there are 4 circles, the area of the shaded region is 10π. (We can write this as (1+2+3+4)π).
If there are 5 circles, the area of the shaded region is 10π. (We can write this as (1+2+3+4)π).
If there are 6 circles, the area of the shaded region is 21π. (We can write this as (1+2+3+4+5+6)π).
Now the pattern emerges. When $n$ is even, the area of the shaded region is $(1+2+3+\cdots+n)\pi$ , or $\left( \frac{n(n+1)}{2} \right) \pi$ . But remember that the problem stated that there are an even number of circles. So now we are solving the equation \[\left( \frac{n(n+1)}{2} \right) \pi\ge2023\pi.\] Dividing by $\pi$ and multiplying by 2 on both sides, we get $n(n+1)\ge4046$ . Now we can plug in the answer choices, and we start off with $60$ because it is the only answer choice that is a multiple of $10$ . Plugging in we get $60\cdot61=3660$ , and this is not quite yet more than $4046$ . But only option $(\text{E})$ is bigger, so we know that the solution can only be $\boxed{\textbf{(E) } 64}$ .
~ Yrock
(P.S. I did this in the test and I solved it in 2 minutes)

## Solution 5
Denote $S$ the area of shaded region and $W$ the area of white region.
$S > W$ and $S \approx W$ if $R$ is big. Therefore \[\pi R^2 = S + W \approx 2S \ge 4046 \pi \implies R \approx 64.\] So we conclude the answer is $\boxed{\textbf{(E) } 64}$ .
vladimir.shelomovskii@gmail.com, vvsss

## Solution 6 (A Bit slow.)
After first observing the problem, we can work out a few of the areas.
1st area = $4\pi-\pi = 3\pi$
2nd area = $16\pi-9\pi = 7\pi$
3rd area = $36\pi-25\pi = 11\pi$
4th area = $64\pi-49\pi = 15\pi$
Notice that the area of the shaded region is $3\pi+7\pi+11\pi+15\pi...+(4n-1)\pi$ for any even number $n$ .
We can create a formula to compute this sum by doing: $3\pi+7\pi+11\pi+15\pi...+(4n-1)\pi$ + $(4n-1)\pi+...15\pi+11\pi+7\pi+3\pi$ to get $(4n+2)*\frac{n}{2} \to (2n^2+n)\pi$ It is important to realize that each $n$ is $2$ circles, the unshaded and the shaded. So that means for each answer choice there are $2x$ as many circles. Then we just plug in values (strategically) to get that $2*(\frac{64}{2})^2+(\frac{64}{2})$ or $\boxed{\textbf{(E) } 64}$ as the answer.
~algebraic_algorithmic
~kfclover (minor LaTeX edits)

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=TrswrE0Yt9UZW1uv&t=3226 ~little-fermat

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=-FmeM--j5ohBx4eR&t=3784
~Math-X

## Video Solution 🚀 Under 2 Min 🚀
https://youtu.be/QBpDSj-Ew_4
~Education, the Study of Everything

## Video Solution by Power Solve (easy to digest!)
https://youtu.be/m1a4xgjZLmc

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=qjI3FuhS3IQ

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=BaDXj32nFXY

## Video Solution
https://youtu.be/rZrsrMxA7v0
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .