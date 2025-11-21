# 2015 AMC 8 Problem 24

## Problem

A baseball league consists of two four-team divisions. Each team plays every other team in its division $N$ games. Each team plays every team in the other division $M$ games with $N>2M$ and $M>4$ . Each team plays a $76$ game schedule. How many games does a team play within its own division?

$\textbf{(A) } 36 \qquad \textbf{(B) } 48 \qquad \textbf{(C) } 54 \qquad \textbf{(D) } 60 \qquad \textbf{(E) } 72$

## Solution 1
On one team they play $3N$ games in their division and $4M$ games in the other. This gives $3N+4M=76$ .
Since $M>4$ we start by trying M=5. This doesn't work because $56$ is not divisible by $3$ .
Next, $M=6$ does not work because $52$ is not divisible by $3$ .
We try $M=7$ does work by giving $N=16$ , $~M=7$ and thus $3\times 16=\boxed{\textbf{(B)}~48}$ games in their division.
$M=10$ seems to work, until we realize this gives $N=12$ , but $N>2M$ so this will not work.

## Solution 2
$76=3N+4M > 10M$ , giving $M \le 7$ . Since $M>4$ , we have $M=5,6,7$ . Since $4M$ is $1$ $\pmod{3}$ , we must have $M$ equal to $1$ $\pmod{3}$ , so $M=7$ .
This gives $3N=48$ , as desired. The answer is $\boxed{\textbf{(B)}~48}$ .

## Solution 3
Notice that each team plays $N$ games against each of the three other teams in its division. So that's $3N$ .
Since each team plays $M$ games against each of the four other teams in the other division, that's $4M$ .
So $3N+4M=76$ , with $M>4, N>2M$ .
Let's start by solving this Diophantine equation. In other words, $N=\frac{76-4M}{3}$ .
So $76-4M\equiv0 \pmod{3}$ (remember: $M$ must be divisible by 3 for $N$ to be an integer!). Therefore, after reducing $76$ to $1$ and $-4M$ to $2M$ (we are doing things in $\pmod{3}$ ), we find that $M\equiv1 \pmod{3}$ .
Since $M>4$ , so the minimum possible value of $M$ is $7$ . However, remember that $N>2M$ ! To find the greatest possible value of M, we assume that $N=2M$ and that is the upper limit of $M$ (excluding that value because $N>2M$ ). Plugging $N=2M$ in, $10M=76$ . So $M<7.6$ . Since you can't have $7.6$ games, we know that we can only check $M=7$ since we know that since $M>4, M<7.6, M\equiv1 \pmod{3}$ . After checking $M=7$ , we find that it will work.
So $M=7, N=16$ . So each team plays 16 games against each team in its division. Since they are asking for games in it division, which equals $3n = 48$ . Select $\boxed{\textbf{(B)}~48}$ .
This might be too complicated. But you should know what's happening if you read the The Art of Problem Solving: Introduction to Number Theory by Mathew Crawford. Notice how I used chapter 12's ideas of basic modular arithmetic operations and chapter 14's ideas of solving linear congruences. Remember: the Introduction Series books by AoPS are for 6th-10th graders! So make sure to read the curriculum books!
This goes same for high school students and little kids as well, and especially for those who want to continue on their path of AIME/USA(J)MO.
~hastapasta

## Video Solution by OmegaLearn
https://youtu.be/HISL2-N5NVg?t=4968

## Video Solutions
https://youtu.be/LiAupwDF0EY - Happytwin
https://www.youtube.com/watch?v=bJSWtw91SLs - Oliver Jiang
https://youtu.be/0ZMDsuOYGqE
~savannahsolver
### See Also