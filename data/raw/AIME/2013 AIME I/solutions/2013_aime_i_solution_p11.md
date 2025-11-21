# 2013 AIME I Problem 11

## Problem

Ms. Math's kindergarten class has $16$ registered students. The classroom has a very large number, $N$ , of play blocks which satisfies the conditions:

(a) If $16$ , $15$ , or $14$ students are present in the class, then in each case all the blocks can be distributed in equal numbers to each student, and

(b) There are three integers $0 < x < y < z < 14$ such that when $x$ , $y$ , or $z$ students are present and the blocks are distributed in equal numbers to each student, there are exactly three blocks left over.

Find the sum of the distinct prime divisors of the least possible value of $N$ satisfying the above conditions.

## Solution 1
$N$ must be some multiple of $\text{lcm}(14, 15, 16)= 2^{4}\cdot 3\cdot 5\cdot 7$ ; this $lcm$ is hereby denoted $k$ and $N = qk$ .
$1$ , $2$ , $3$ , $4$ , $5$ , $6$ , $7$ , $8$ , $10$ , and $12$ all divide $k$ , so $x, y, z = 9, 11, 13$
We have the following three modulo equations:
$nk\equiv 3\pmod{9}$
$nk\equiv 3\pmod{11}$
$nk\equiv 3\pmod{13}$
To solve the equations, you can notice the answer must be of the form $9\cdot 11\cdot 13\cdot m + 3$ where $m$ is an integer.
This must be divisible by $lcm$ $(14, 15, 16)$ , which is $560\cdot 3$ .
Therefore, $\frac{9\cdot 11\cdot 13\cdot m + 3}{560\cdot 3} = q$ , which is an integer. Factor out $3$ and divide to get $\frac{429m+1}{560} = q$ . Therefore, $429m+1=560q$ . We can use Bezout's Identity or a Euclidean algorithm bash to solve for the least of $m$ and $q$ .
We find that the least $m$ is $171$ and the least $q$ is $131$ .
Since we want to factor $1680\cdot q$ , don't multiply: we already know that the prime factors of $1680$ are $2$ , $3$ , $5$ , and $7$ , and since $131$ is prime, we have $2 + 3 + 5 + 7 + 131 = \boxed{148}$ .

## Solution 2
Note that the number of play blocks is a multiple of the LCM of $16$ , $15$ , and $14$ . The value of this can be found to be $(16)(15)(7) = 1680$ . This number is also divisible by $1$ , $2$ , $3$ , $4$ , $5$ , $6$ , $7$ , $8$ , $10$ , and $12$ , thus, the three numbers $x, y, z$ are $9, 11, 13$ .
Thus, $1680k\equiv 3$ when taken mod $9$ , $11$ , $13$ . Since $1680$ is congruent to $6$ mod $9$ and $3$ mod $13$ , and congruent to $8$ mod $11$ , the number $k$ must be a number that is congruent to $1$ mod $13$ , $2$ mod $3$ (because $6$ is a multiple of $3$ , which is a factor of $9$ that can be divided out) and cause $8$ to become $3$ when multiplied under modulo $11$ .
Looking at the last condition shows that $k\equiv 10$ mod $11$ (after a bit of bashing) and is congruent to $1$ mod $13$ and $2$ mod $3$ as previously noted. Listing out the numbers congruent to $10$ mod $11$ and $1$ mod $13$ yield the following lists:
$10$ mod $11$ : $21$ , $32$ , $43$ , $54$ , $65$ , $76$ , $87$ , $98$ , $109$ , $120$ , $131$ ...
$1$ mod $13$ : $14$ , $27$ , $40$ , $53$ , $66$ , $79$ , $92$ , $105$ , $118$ , $131$ , $144$ , $157$ , $170$ ...
Both lists contain $x$ elements where $x$ is the modulo being taken, thus, there must be a solution in these lists as adding $11(13)$ to this solution yields the next smallest solution. In this case, $131$ is the solution for $k$ and thus the answer is $1680(131)$ . Since $131$ is prime, the sum of the prime factors is $2 + 3 + 5 + 7 + 131 = \boxed{148}$ .

## Solution 3
It is obvious that $N=a\cdot 2^4 \cdot 3\cdot 5\cdot 7$ and so the only mod $3$ number of students are $9, 11, 13$ . Therefore, $N=1287\cdot k+3$ . Try some approaches and you will see that this one is one of the few successful ones:
Start by setting the two $N$ equations together, then we get $1680a=1287k+3$ . Divide by $3$ . Note that since the RHS is $1\pmod{3}$ , and since $560$ is $2\pmod{3}$ , then $a=3b+2$ , where $b$ is some nonnegative integer, because $a$ must be $2\pmod{3}$ .
This reduces to $560 \cdot 3b + 1119 = 429k$ . Now, take out the $11!$ With the same procedure, $b=11c-1$ , where $c$ is some nonnegative integer.
You also get $c=13d+4$ , at which point $k=171+560d$ . $d$ cannot be equal to $0$ . Therefore, $c=4, b=43, a=131$ , and we know the prime factors of $N$ are $2, 3, 5, 7, 131$ so the answer is $\boxed{148}$ .

## Solution 4
We start by noticing that $N = a\textbf{lcm}(14, 15, 16) = 1680a$ for some integer $a$ in order to satisfy the first condition.
Next, we satisfy the second condition. Since $x<y<z < 14$ must leave a remainder when dividing $1680a$ , they are not divisors of $1680x$ . Thus, we can eliminate all $y \le 14$ s.t. $\gcd(y, 1680x) \ne 1$ which leaves $(x, y, z) = (9, 11, 13)$ . Thus, $N = 1680a \equiv 3 \pmod 9 \equiv 3 \pmod {11} \equiv 3 \pmod {13}$ . Now, we seek to find the least $a$ which satisfies this set of congruences.
By Chinese Remainder Theorem on the first two congruences, we find that $a \equiv 32 \pmod {33}$ (we divide by three before proceeding in the first congruence to ensure the minimal solution). Finally, by CRT again on $a \equiv 32 \pmod {33}$ and $1680a \equiv 3 \pmod {13}$ we find that $a \equiv 131 \pmod {429}$ .
Thus, the minimal value of $N$ is possible at $a = 131$ . The prime factorization of this minimum value is $2^4 \cdot 3 \cdot 5 \cdot 7 \cdot 131$ and so the answer is $2 + 3 + 5 + 7 + 131 = \boxed{148}$ .

## Solution 5
As the problem stated, the number of boxes is definitely a multiple of $lcm(14,15,16)=1680$ , so we assume total number of boxes is $1680k$
Then, according to $(b)$ statement, we get $1680k \equiv 3 \pmod x \equiv 3 \pmod {y} \equiv 3 \pmod {z}$ . So we have $lcm(x,y,z)+3+m\cdot lcm(x,y,z)=1680k$ , we just write it to be $(1+n)lcm(x,y,z)=1680k-3$ Which tells that $x,y,z$ must be all odd number. Moreover, we can see $(1+m)lcm(x,y,z)$ can't be a multiple of $3,5,7$ (as $1680$ is a multiple of $5,7$ ) which means that $lcm(x,y,z)=lcm(9,11,13)=1287$ We let $n=1+m$
Now, we write $1287n+3=1680k, 429n+1=560k$ It is true that $n\equiv 1 \pmod{10}$ , let $n=10p+1$ , it has $429p+43=56k$ Then, $p$ must be odd, let $p=2q+1$ , it indicates $429q+236=28k$ Now, $q$ must be even, $q=2s$ tells $429s+118=14k$ Eventually, $s$ must be even, $s=2y$ , $858y+59=7k$ , $y=1$ is the smallest. This time, $k=131$
So the number of balls is $1680\cdot 131=2^4\cdot 3\cdot 5\cdot 7 \cdot 131$ , the desired value is $2+3+5+7+131=\boxed{148}$
~bluesoul

## Solution 6(CRT Bash)
From part (a), we know that $2^4\cdot3\cdot5\cdot7 | N$ . From part (b), we know that $N \equiv 3 \pmod {1287}$ . We can expand on part (a) by saying that $N = 1680k$ for some $k$ . Rather than taking the three modulos together, we take them individually. \[1680k \equiv 6k \equiv 3 \pmod 9\] \[k \equiv 2^{-1} \pmod 9\] The inverse of 2 mod 9 is easily seen to be $5$ . \[k \equiv 5 \pmod 9\]
Now moving to the second modulo which we leave as follows, \[1680k \equiv 8k \equiv 3 \pmod {11}\] Now the last modulo, \[1680k \equiv 3k \equiv 3 \pmod {13}\] \[k \equiv 1 \pmod{13}\] CRT on the first and the third one results in $k \equiv 4 \pmod {117}$ . Now doing the second one and the one we just made, $k \equiv 131 \pmod{1287}$ . Thus, the smallest value that works for $k = 131$ . Thus $N = 2^4\cdot3\cdot5\cdot7\cdot131$ $2+3+5+7+131 = \boxed{148}$
~YBSuburbanTea
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .