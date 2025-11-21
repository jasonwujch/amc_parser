# 2018 AMC 8 Problem 25

## Problem

How many perfect cubes lie between $2^8+1$ and $2^{18}+1$ , inclusive?

$\textbf{(A) }4\qquad\textbf{(B) }9\qquad\textbf{(C) }10\qquad\textbf{(D) }57\qquad \textbf{(E) }58$

## Solution 1
We compute $2^8+1=257$ . We're all familiar with what $6^3$ is, namely $216$ , which is too small. The smallest cube greater than it is $7^3=343$ . $2^{18}+1$ is too large to calculate, but we notice that $2^{18}=(2^6)^3=64^3$ , which therefore will clearly be the largest cube less than $2^{18}+1$ . So, the required number of cubes is $64-7+1= \boxed{\textbf{(E) }58}$ .

## Solution 2 (Brute force)(Advised)(super fast)
First, $2^8+1=257$ . Then, $2^{18}+1=262145$ . Now, we can see how many perfect cubes are between these two parameters. By guessing and checking, we find that it starts from $7$ and ends with $64$ . Now, by counting how many numbers are between these, we find the answer to be $\boxed{\textbf{(E) }58}$ .

## Solution 3 (Guessing)
First, we realize that question writers like to trick us. We know that most people will be calculating the lowest and highest number whose cubes are within the range. The answer will be the highest number $-$ the lowest number $+ 1$ . People will forget the $+1$ so the only possibilities are C and E. We can clearly see that C is too small so our answer is $\boxed{\textbf{(E) }58}$ .

## Solution 4 (If you do not notice that )
There is not so much guessing and checking after we find that it starts from $7$ because $7^3=343$ , which is over $2^8+1=257$ . We can start guessing with the 10, answer C, as it is the middle value. Adding 10 to 7 gives us 17 and $17^3 = 4,913$ , which is a bit low. So, we move "up" to 57, answer D. Adding 57 to 7 gives us 64 and $64^3 = 262,144$ , which is perfect for the $2^{18}+1=262,145$ . But we are not done. Since it is inclusive, we must add 1 to this solution, which give us $\boxed{\textbf{(E) }58}$ .

## Solution 5 (Super fast!)
We can immediately evaluate $2^8+1$ which gives us $257$ and the smallest perfect cube greater than that is $343 = 7^3$ , and you also immediately notice that $2^{18} = (2^6)^3 = 64^3$ . Now, all we have to do is count the cubes, which equals: \begin{align} 64-7+1 &= \boxed{\textbf{(E) }58} \end{align}
-jb2015007

## Video Solution by TheMathGeek (Simple exponent laws in 15 seconds!)
https://www.youtube.com/watch?v=eisR5FAu-vA
~ TheMathGeek

## Video Solution by Pi Academy
https://youtu.be/oSjDIojucGo?si=b_FsVd470FLZYSjx
~ jj_empire10

## Video Solutions
https://www.youtube.com/watch?v=pbnddMinUF8
-Happytwin
https://www.youtube.com/watch?v=2e7gyBYEDOA
- MathEx
https://euclideanmathcircle.wixsite.com/emc1/videos?wix-vod-video-id=5f1ae882ac754e54906db7cfb62c61f6&wix-vod-comp-id=comp-kn8844mv
https://youtu.be/geZupO75zUw
~savannahsolver
https://www.youtube.com/watch?v=r0e_6dXViRI
~David

## Video Solution by OmegaLearn
https://youtu.be/rQUwNC0gqdg?t=297
### See Also