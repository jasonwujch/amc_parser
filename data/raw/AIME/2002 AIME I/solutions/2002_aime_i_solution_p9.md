# 2002 AIME I Problem 9

## Problem

Harold, Tanya, and Ulysses paint a very long picket fence.

- Harold starts with the first picket and paints every $h$ th picket;

- Tanya starts with the second picket and paints every $t$ th picket; and

- Ulysses starts with the third picket and paints every $u$ th picket.

Call the positive integer $100h+10t+u$ paintable when the triple $(h,t,u)$ of positive integers results in every picket being painted exactly once. Find the sum of all the paintable integers.

## Solution

## Solution 1
Note that it is impossible for any of $h,t,u$ to be $1$ , since then each picket will have been painted one time, and then some will be painted more than once.
$h$ cannot be $2$ , or that will result in painting the third picket twice. If $h=3$ , then $t$ may not equal anything not divisible by $3$ , and the same for $u$ . Now for fourth and fifth pickets to be painted, $t$ and $u$ must be $3$ as well. This configuration works, so $333$ is paintable.
If $h$ is $4$ , then $t$ must be even. The same for $u$ , except that it can't be $2 \mod 4$ . Thus $u$ is $0 \mod 4$ and $t$ is $2 \mod 4$ . Since this is all $\mod 4$ , $t$ must be $2$ and $u$ must be $4$ , in order for $5,6$ to be paint-able. Thus $424$ is paintable.
$h$ cannot be greater than $4$ , since if that were the case then the answer would be greater than $999$ , which would be impossible for the AIME.
Thus the sum of all paintable numbers is $\boxed{757}$ .

## Solution 2
Again, note that $h,t,u \neq 1$ . The three conditions state that no picket number $n$ may satisfy any two of the conditions: $n \equiv 1 \pmod{h},\ n \equiv 2 \pmod{t},\ n \equiv 3 \pmod{u}$ . By the Chinese Remainder Theorem , the greatest common divisor of any pair of the three numbers $\{h,t,u\}$ cannot be $1$ (since otherwise without loss of generality consider $\text{gcd}\,(h,t) = 1$ ; then there will be a common solution $\pmod{h \times t}$ ).
Now for $4$ to be paint-able, we require either $h = 3$ or $t=2$ , but not both.
- In the former condition, since $\text{gcd}\,(h,t),\ \text{gcd}\,(h,u) \neq 1$ , it follows that $3|t,u$ . For $5$ and $6$ to be paint-able, we require $t = u = 3$ , and it is easy to see that $333$ works.
- In the latter condition, similarly we require that $2|h,u$ . All even numbers are painted. We now renumber the remaining odd pickets to become the set of all positive integers ( $1,3,5, \ldots \rightarrow 1',2',3', \ldots$ , where $n' = \frac{n+1}{2}$ ), which requires the transformation $h' = h/2,\ u' = u/2$ , and with the painting starting respectively at $1',2'$ . Our new number system retains the same conditions as above, except without $t$ . We thus need $\text{gcd}\, (h',u') \neq 1, h',u' \neq 1$ . Then for $3',4'$ to be painted, we require $h' = u' = 2$ . This translates to $424$ , which we see works.
Thus the answer is $333+424 = \boxed{757}$ .

## Solution 3
The three conditions state that no picket number $n$ may satisfy any two of the conditions: $n \equiv 1 \pmod{h},\ n \equiv 2 \pmod{t},\ n \equiv 3 \pmod{u}$ . Note that the smallest number, $min \{ h,t,u \},$ divides the other $2$ , and the next smallest divide the largest number, otherwise there is a common solution by the Chinese Remainder Theorem . It is also a necessary condition so that it paints exactly once. Note that the smallest number can't be at least $5$ , otherwise not all picket will be painted. We are left with few cases (we could also exclude $1$ as the possibility) which could be done quickly. Thus the answer is $333+424 = \boxed{757}$ .

## Solution 4
The wording of this problem is a bit dissatisfying and could have been improved by stating that there are at least h + t + u pickets instead of "very long". For example, a very long fence could have 5 pickets, h = 78, t = 47, u = 1. To compensate for this we should lean on the fact that the answer cannot exceed 999.
Clearly we have to accept that there are 4 pickets or more, and the 4th picket is not reached from setting u = 1. If the 4th picket is reached from h = 3, then the 5th picket will not be reached via u = 2, or else we'd be unable to have 7 pickets. So h = 3 => t = 3 => u = 3, and 333 is a solution. We now have h > 3 for any remaining cases, and thus we only have room for 1 more case.
Since the 4th picket must henceforth be reached via t = 2, we either have the 5th picket reached via u = 2 (requiring h to be any number exceeding the number of pickets, and we're stipulating that this is not allowed), or we have the 5th picket reached via h = 4, from which it follows that u = 4. So we have accumulated the solutions 333 and 424 and we have exhausted both the space of reasonable possibilities as well as the available space before we would exceed 999.
These problems are copyrighted © by the Mathematical Association of America.