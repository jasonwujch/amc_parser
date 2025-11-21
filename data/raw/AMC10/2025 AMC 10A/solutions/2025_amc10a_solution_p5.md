# 2025 AMC 10A Problem 5

## Problem

Consider the sequence of positive integers $1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2 \dots$

$\textbf{(A) } 5 \qquad\textbf{(B) } 15 \qquad\textbf{(C) } 16 \qquad\textbf{(D) } 44 \qquad\textbf{(E) } 45$

What is the $2025$ th term in the sequence?

## Solution 1
One possible way the sequence could've been constructed was by putting "mountains" going up from $1$ , to $n+1,$ then going back down to $2.$ For example, the first few "mountains" look like this:
$12|1232|123432|12345432|...$
So, the $n^{th}$ mountain has length $2n$ and has highest number $n+1.$ We want to add mountains until we get a total length as close as possible, but not exceeding, $2025.$ Let the last mountain we sum be mountain $a.$ Hence, \[2+4+6+...+2a=2(1+2+3+...+a)=a(a+1)\le2025\] \[\implies a^2<2025\implies a<45,\] so our max $a$ is $44.$ In this $44^{th}$ mountain, the max number is $45,$ so the $45^{th}$ mountain has max number $46.$ Next, $44(44+1)=1980,$ so we're looking for the $45^{th}$ number in the $45^{th}$ mountain, which is $\boxed{\text{(E) }45}.$
~Tacos_are_yummy_1

## Solution 2 (nice equation)
Group the numbers by their hill pattern: $(12)(1232)(123432)(12345432)...$
The maximums of each hill occur at terms $n = 2, 5, 10, 17...$ These terms correspond to maximums of $2, 3, 4,...$ Let $a$ be the maximum at term $N$ . Since the sum of the first $x$ odd numbers is $x^2$ we have $1 + (a-1)^2 = N.$ So for example, if a = $4,$ then $N = 10,$ telling us that the peak of the hill with maximum $4$ occurs at the $10$ th term.
Now, we know $2025 = 45^2,$ so let $a = 46.$ Then $N = 2026,$ so the $2026$ th term is $46.$ Then the $2025$ th term must be $\boxed{\text{(E) }45}.$
~ grogg007

## Solution 3
Note that the first $1$ is the first number from the left, the second $1$ is the third number from the left, and the third $1$ is the seventh number from the left. Since the second differences between the indices of the $n^{th}$ $1$ ’s are equal, there is a quadratic function for the position of the $n^{th}$ $1$ . As the second differences are $2$ , the leading coefficient of this function is $1$ . Let the function be $f(x)=x^2+ax+b$ . Then, we have $1+a+b=1$ , and $4+2a+b=3$ . Solving, we get $a=-1$ and $b=1$ . Therefore, the $n$ th $1$ from the left is the $(n^2-n+1)$ th number from the left. Plugging in $n=45$ gives $f(n)=1981$ , so the $1981$ st number is a $1$ .
Also, the sequence shows that the first instance of a positive integer $k$ is always to the left of the $k^{th}$ $1$ . This means that following the $1981^{st}$ number, the numbers go to or above $45$ . Adding $2025-1981$ to $1$ means that the $2025^{th}$ term of the sequence is $\boxed{\textbf{(E) }45}.$
~joiceeliu
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 11:09, 7 November 2025 (EST)saharshdevaraju)

## Solution 4 (Quick and Fast!🚀)
Note that every $n^2$ th term is $n$ . For example, the $3^2$ th term is $3$ , the $4^2$ th term is $4$ , and so on. We also notice that $45^2 = 2025$ , so the $2025$ th term is $45$ , which is answer choice $\boxed{\textbf{(E)}45}.$
~iiiiiizh
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 09:35, 7 November 2025 (EST)saharshdevaraju)
~nithins
~AquaNotFoundPlayz

## Solution 5 (Super Simple!!)
Upon inspecting the problem, we see that the $1^{st}$ term is 1, and so are the $3^{rd}$ , $7^{th}$ , $13^{th}$ , $18^{th}$ , $31^{st}$ , and so on. We see that the pattern comes from the differences: $+2$ , $+4$ , $+6$ , $+8$ , $+10$ , and so on. From this we see that a $1$ appears at each position that is a number of the form $n^{2}-n+1$ . We know that $2025 = 45 \cdot 45$ . Plugging $45$ as $n$ gives $1981$ , meaning that the $2025^{th}$ term is $2025-1981+1=45$ . Therefore, the solution is $\boxed{\textbf{(E)}45}.$
~vgarg
~major $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 15:27, 7 November 2025 (EST)saharshdevaraju)

## Solution 6 - ⚡ Fastest and Easiest! ⚡
\(\large \textbf{Takes less than 20 seconds!}\)
Immediately by looking at the sequence, we observe that the digit in the place of each perfect square is the square root of that number. For example, the first term in the sequence is \(1\) (because \(\sqrt{1}=1\)), the \(4^{th}\) term is \(2\) (because \(\sqrt{4}=2\)), the \(9^{th}\) term is \(3\) (because \(\sqrt{9}=3\)), the \(16^{th}\) term is \(4\) (because \(\sqrt{16}=4\)), the \(25^{th}\) term is \(5\) (because \(\sqrt{25}=5\)), and so on. And since \(2025\) is a perfect square, it makes it easy for us because \(\sqrt{2025}=45\), which makes the answer choice \(\boxed{\textbf{(E) }45}.\)
To make it easier to understand my way of solving it, here is a table.
Let \(n =\) the position of the said number in the sequence
Let \(\sqrt{n} =\) the number located in that position itself
\begin{array}{c|c|c} n & \sqrt{n} \\[6pt] \hline 1 & 1 \\[6pt] 4 & 2 \\[6pt] 9 & 3 \\[6pt] 16 & 4 \\[6pt] 25 & 5 \\[6pt] 36 & 6 \\[6pt] \dots & \dots \\[6pt] 2025 & \boxed{\textbf{(E) }45} \end{array}
\(\textbf{Note}\): I am just saying that the square root of the position (if the position is a perfect square) is the number that appears in the said position in the above sequence. I am not saying that the root itself is the first time it appears in the said sequence. To elaborate, the number \(6\) appears on the \(26^{th}\) number, as \(\textit{well}\) as the \(36^{th}\) number as expected (because \(\sqrt{36} = 6\)).
~i_am_not_suk_at_math (saharshdevaraju 21:14, 6 November 2025 (EST)saharshdevaraju)

## Solution 7 - Pattern Recognition
After looking at the problem, it is evident that a pattern exists for the first occurence of a number in the sequence. Knowing this, we can write the places that each number appears at: \begin{align} &1: 1 \\ &2: 2 \\ &3: 5 \\ &4: 10 \\ &5: 17 \end{align} If we write down the difference between the each numbers position in sequence, we get $1, 3, 5, \text{and } 7$ . We notice how these numbers are similar to how the square numbers increase (square numbers: $1, 4, 9, 16…$ ). We also notice how the position of the first instance of each number $n$ is just $(n-1)^2+1$ . Since we're trying to find the $2025^{th}$ number and $2025 = 45^2$ , we can plug in $45$ for $n-1$ . As a result, we get that the first instance of the number $46$ appears at $(45)^2+1$ or $2026$ . Knowing that the number before the first instance of a number $n$ is $n-1$ , we get the answer choice $\boxed{\textbf{(E) }45}.$
~Kasoisanti
~minor edits by i_am_not_suk_at_math (saharshdevaraju 09:34, 7 November 2025 (EST)saharshdevaraju)
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 15:22, 7 November 2025 (EST)saharshdevaraju)

## Solution 9: Patterns
We list the positions of the $\text{1s}$ in the sequence and get that they appear at $1,3,7,13,...$ We see that the $n\text{th}$ $1$ in the sequence, its location is at the $n(n+1)+1\text{th}$ position. So, we can find that the $1$ closest to $2025$ happens where $n=44,$ due to our knowledge that $2025=45^2.$ Since $44(45)+1=1981,$ we can start counting from $1981,$ getting that the 2025th term in the sequence is $\boxed{45}.$
~ gogogo2022

## Solution 10: Brute force
Solve it using brute force gng not that deep🥀 ~Antonyhuang123
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 14:33, 17 November 2025 (EST)saharshdevaraju)

## Video Solution
https://youtu.be/l1RY_C20Q2M

## Chinese Video Solution
https://www.bilibili.com/video/BV1gV2uBbEJe/
~metrixgo

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution (Fast and easy)
https://youtu.be/ZQhAdIs2FIg?si=mEgnYvdQ2sMrCx1P ~ Pi Academy

## Video Solution by Daily Dose of Math
https://youtu.be/LN5ofIcs1kY
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .