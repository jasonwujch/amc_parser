# 2019 AMC 8 Problem 17

## Problem

What is the value of the product

\[\left(\frac{1\cdot3}{2\cdot2}\right)\left(\frac{2\cdot4}{3\cdot3}\right)\left(\frac{3\cdot5}{4\cdot4}\right)\cdots\left(\frac{97\cdot99}{98\cdot98}\right)\left(\frac{98\cdot100}{99\cdot99}\right)?\]

$\textbf{(A) }\frac{1}{2}\qquad\textbf{(B) }\frac{50}{99}\qquad\textbf{(C) }\frac{9800}{9801}\qquad\textbf{(D) }\frac{100}{99}\qquad\textbf{(E) }50$

## Solution 1 (telescoping)
We rewrite: \[\frac{1}{2}\cdot\left(\frac{3\cdot2}{2\cdot3}\right)\left(\frac{4\cdot3}{3\cdot4}\right)\cdots\left(\frac{99\cdot98}{98\cdot99}\right)\cdot\frac{100}{99}\]
The middle terms cancel, leaving us with
\[\left(\frac{1\cdot100}{2\cdot99}\right)= \boxed{\textbf{(B)}\frac{50}{99}}\]

## Solution 2
If you calculate the first few values of the equation, all of the values tend to close to $\frac{1}{2}$ , but are not equal to it. The answer closest to $\frac{1}{2}$ but not equal to it is $\boxed{\textbf{(B)}\frac{50}{99}}$ .

## Solution 3
Rewriting the numerator and the denominator, we get $\frac{\frac{100! \cdot 98!}{2}}{\left(99!\right)^2}$ . We can simplify by canceling 99! on both sides, leaving us with: $\frac{100 \cdot 98!}{2 \cdot 99!}$ We rewrite $99!$ as $99 \cdot 98!$ and cancel $98!$ , which gets $\boxed{\textbf{(B)}\frac{50}{99}}$ .

## Solution 4
All of the terms have the form $\frac{k^2-1}{k^2}$ , which is $<1$ , so the product is $<1$ , so we eliminate options (D) and (E). (C) is too close to 1 to be possible. The partial products seem to be approaching 1/2, so we guess that 1/2 is the limit/asymptote, and so any finite product would be slightly larger than 1/2. Therefore, by process of elimination and a small guess, we get that the answer is $\boxed{\textbf{(B)}\frac{50}{99}}$ .

## Solution 5
The product \[\left(\frac{1 \cdot 3}{2 \cdot 2}\right) \left(\frac{2 \cdot 4}{3 \cdot 3}\right) \left(\frac{3 \cdot 5}{4 \cdot 4}\right) \cdots \left(\frac{98 \cdot 100}{99 \cdot 99}\right)\] can be simplified by observing that in each individual fraction, the numerator and denominator contain factors that cancel out with adjacent terms. Specifically, the factor 3 in the numerator of the first fraction cancels with the 3 in the denominator of the second fraction, the 4 in the numerator of the second fraction cancels with the 4 in the denominator of the third fraction, and so on. This telescoping cancellation continues throughout the entire product.
After all the cancellations, only the first factor of the first fraction, \( \frac{1}{2} \), and the last factor of the last fraction, \( \frac{100}{99} \), remain. The value of the product is therefore: \[\frac{1}{2} \cdot \frac{100}{99} = \frac{50}{99}.\] Thus, the value of the product is: (B) \(\frac{50}{99}\).
-- Rayansh Mankad(SharpWhiz17)

## Video Solution

## Video Solution 1 (Detailed Explanation) 🚀⚡📊
https://youtu.be/kD7Z72cg8bk
-- ChillGuyDoesMath :)

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/IgpayYB48C4?si=UJVe2zopeqT-4rLM&t=5256
~Math-X
https://www.youtube.com/watch?v=yPQmvyVyvaM
Associated video
https://www.youtube.com/watch?v=ffHl1dAjs7g&list=PLLCzevlMcsWNBsdpItBT4r7Pa8cZb6Viu&index=1
~ MathEx

## Video Solution 2
Solution detailing how to solve the problem:
https://www.youtube.com/watch?v=VezsRMJvGPs&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=18

## Video Solution 3
https://youtu.be/e1EJNZu-jxM
~savannahsolver

## Video Solution 3(an Elegant way)
https://www.youtube.com/watch?v=la3en2tgBN0

## Video Solution 4 by OmegaLearn
https://youtu.be/TkZvMa30Juo?t=3326
~ pi_is_3.14

## Video Solution
https://youtu.be/wUvi7tzxuTk
~Education, the Study of Everything

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1
### See Also