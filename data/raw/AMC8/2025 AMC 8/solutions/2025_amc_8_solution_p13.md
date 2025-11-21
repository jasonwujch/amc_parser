# 2025 AMC 8 Problem 13

## Problem

Each of the even numbers $2, 4, 6, \ldots, 50$ is divided by $7$ . The remainders are recorded. Which histogram displays the number of times each remainder occurs? [asy] /*By Reda_mandymath*/ unitsize(15); void histogram(pair p, string _str, int[] n) { /* p is shift transformation, _str is choice string, n[] is the array of number of remainders, _pen is the pen style of block, a is the width of block, b is the width of gap _scale is the font scale of labels*/ pen _pen; real a = 0.8; real b = 0.3; real _scale = 0.8; draw(shift(p) * ((0, 0) -- (9, 0) -- (9, 5) -- (0, 5) -- cycle)); label(scale(_scale) * rotate(90) * "Count", (-0.4, 2.5)+p); label(scale(_scale) * "Remainder", (4.5, -1)+p); for (int i = 0; i <= 6; ++i) { if (n[i] == 3) { _pen = mediumgray; } else { _pen = heavygray; } fill(shift(p) * ((a*(i+1) + b*i, 0) -- (a*(i+1) + b*i, n[i]) -- (a*(i+2) + b*i, n[i]) -- (a*(i+2) + b*i, 0) -- cycle), _pen); label(scale(_scale) * string(i), shift(p) * (a*(i+1.5) + b*i, 0), S); label(scale(_scale) * string(n[i]), shift(p) * (a*(i+1.5) + b*i, n[i]), N); } label(_str, shift(p) * (-0.4, 6)); } histogram((0, 0), "$\textbf{(A)}$", new int[] {3, 4, 4, 3, 4, 3, 4}); histogram((12, 0), "$\textbf{(B)}$", new int[] {3, 4, 4, 4, 3, 3, 4}); histogram((24, 0), "$\textbf{(C)}$", new int[] {3, 4, 4, 4, 4, 3, 3}); histogram((0, -8), "$\textbf{(D)}$", new int[] {4, 3, 4, 3, 4, 3, 4}); histogram((12, -8), "$\textbf{(E)}$", new int[] {4, 4, 3, 4, 3, 4, 3}); [/asy]

## Solution 1
Let's take the numbers 2 through 14 (evens). The remainders will be 2, 4, 6, 1, 3, 5, and 0. This sequence keeps repeating itself over and over. We can take floor(50/14) = 3, so after the number 42, every remainder has been achieved 3 times. However, since 44, 46, 48, and 50 are left, the remainders of those will be 2, 4, 6, and 1 respectively. The only histogram in which those 4 numbers are set at 4 is histogram $\boxed{\textbf{(A)}}$ .
~Sigmacuber

## Solution 2
Writing down all the remainders gives us
\[2, 4, 6, 1, 3, 5, 0, 2, 4, 6, 1, 3, 5, 0, 2, 4, 6, 1, 3, 5, 0, 2, 4, 6, 1.\]
In this list, there are $3$ numbers with remainder $0$ , $4$ numbers with remainder $1$ , $4$ numbers with remainder $2$ , $3$ numbers with remainder $3$ , $4$ numbers with remainder $4$ , $3$ numbers with remainder $5$ , and $4$ numbers with remainder $6$ . Manually computation of every single term can be avoided by recognizing the pattern alternates from $0, 2, 4, 6$ to $1, 3, 5$ and there are $25$ terms. The only histogram that matches this is $\boxed{\textbf{(A)}}$ .
~alwaysgonnagiveyouup

## Solution 3
First, we find all of the multiples of $7$ that are even, and are therefore, in this list. Knowing that $7$ is odd, and that odd+odd=even, we can find all of the even multiples of $7$ by simply finding all of the multiples of $14$ that fit on this list. Doing this, we end up with
\[14, 28, 42.\]
Now, we can clearly see that there are only $3$ numbers in this list with $0$ as a remainder. This disproves $2$ of our $5$ answers immediately. Since our remaining answers are identical until we reach $3$ as a remainder, we can skip right to there. Now, we need to find all even numbers that leave a remainder of $3$ when divided by $7$ . To do this, we add $3$ to all ODD multiples of $7$ because odd+odd=even. This gives us
\[10, 24, 38.\]
Note that we don't add $3$ to $49$ because that exceeds $50$ . This shows us that there are only $3$ numbers on this list that have a remainder of $3$ when divided by $7$ , disproving histograms B and C, which say that there are $4$ of these numbers. This reveals the answer to be $\boxed{\textbf{(A)}}$ .
~Kapurnicus ~Minor edit by NYCnerd

## Video Solution 1
https://youtu.be/VP7g-s8akMY?si=JkH2XHbYOhk5-PSc&t=1269 ~hsnacademy

## Video Solution 2 by Thinking Feet
https://youtu.be/PKMpTS6b988

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC
### See Also