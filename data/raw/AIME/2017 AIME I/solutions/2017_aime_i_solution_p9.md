# 2017 AIME I Problem 9

## Problem

Let $a_{10} = 10$ , and for each positive integer $n >10$ let $a_n = 100a_{n - 1} + n$ . Find the least positive $n > 10$ such that $a_n$ is a multiple of $99$ .

## Solution 1
Writing out the recursive statement for $a_n, a_{n-1}, \dots, a_{10}$ and summing them gives \[a_n+\dots+a_{10}=(a_n+\cdots+a_{11})+a_{10}=100(a_{n-1}+\dots+a_{10})+n+\dots+10\] Which simplifies to \[a_n=99(a_{n-1}+\dots+a_{10})+\frac{1}{2}(n+10)(n-9)\] Therefore, $a_n$ is divisible by 99 if and only if $\frac{1}{2}(n+10)(n-9)$ is divisible by 99, so $(n+10)(n-9)$ needs to be divisible by 9 and 11. Since our goal is just finding the minimum $n$ , we can do casework on whether the $n+10$ or $n-9$ is a multiple of 11 (We choose 11 because it is prime). Assume that $n+10$ is a multiple of 11. Writing out a few terms, $n=12, 23, 34, 45$ , we see that $n=45$ is the smallest $n$ that works in this case. Next, assume that $n-9$ is a multiple of 11. Writing out a few terms, $n=20, 31, 42, 53$ , we see that $n=53$ is the smallest $n$ that works in this case. The smallest $n$ is $\boxed{045}$ .
Note that we can also construct the solution using CRT by assuming either $11$ divides $n+10$ and $9$ divides $n-9$ , or $9$ divides $n+10$ and $11$ divides $n-9$ , and taking the smaller solution. (We know this because it's impossible for both $n+10$ and $n-9$ to be divisible by 3).
### Another way to get the quadratic
Writing out the first couple of terms modulo $99$ , we find $a_n = a_{n-1}+n$ so we have $a_{10}=10,a_{11}=21,a_{12}=33,...$ We can compute their finite differences, \[10,21,33,46,...\] \[11,12,13,...\] \[1,1,...\] Since there are 3 rows we know it is a quadratic and we can continue, by finding the quadratic passing through $(10,10),(11,21),(12,33)$ to get $\frac{(n^2+n-90)}{2}.$ -mathkiddus

## Solution 2
\[a_n \equiv a_{n-1} + n \pmod {99}\] By looking at the first few terms, we can see that \[a_n \equiv 10+11+12+ \dots + n \pmod {99}\] This implies \[a_n \equiv \frac{n(n+1)}{2} - \frac{10*9}{2} \pmod {99}\] Since $a_n \equiv 0 \pmod {99}$ , we can rewrite the equivalence, and simplify \[0 \equiv \frac{n(n+1)}{2} - \frac{10*9}{2} \pmod {99}\] \[0 \equiv n(n+1) - 90 \pmod {99}\] \[0 \equiv 4n^2+4n+36 \pmod {99}\] \[0 \equiv (2n+1)^2+35 \pmod {99}\] \[64 \equiv (2n+1)^2 \pmod {99}\] The only squares that are congruent to $64 \pmod {99}$ are $(\pm 8)^2$ and $(\pm 19)^2$ , so \[2n+1 \equiv -8, 8, 19, \text{or } {-19} \pmod {99}\] $2n+1 \equiv -8 \pmod {99}$ yields $n=45$ as the smallest integer solution.
$2n+1 \equiv 8 \pmod {99}$ yields $n=53$ as the smallest integer solution.
$2n+1 \equiv -19 \pmod {99}$ yields $n=89$ as the smallest integer solution.
$2n+1 \equiv 19 \pmod {99}$ yields $n=9$ as the smallest integer solution. However, $n$ must be greater than $10$ .
The smallest positive integer solution greater than $10$ is $n=\boxed{045}$ .

## Solution 3 (quadratic)
Take the mods of the first few terms: $a_{10} \equiv 10 \pmod{99}$ , $a_{11} \equiv 21 \pmod{99}$ , $a_{12} \equiv 33 \pmod{99}$ , $a_{13} \equiv 46 \pmod{99}$ , etc.
Notice the pattern: We're adding $10$ to the mods, then $11$ , then $12$ , and so on. So we have $a_{n} \equiv n + a_{n - 1} \pmod{99}.$ Using the sum of integers formula, we can create an equation for any general $a_n$ and its mod 99:
\[10 + 11 + \dots + n = \frac{n \cdot (n + 1)}{2} - 45 \implies a_n \equiv \frac{n \cdot (n + 1)}{2} - 45 \pmod{99}.\] Let $\frac{n \cdot (n + 1)}{2} - 45$ equal some multiple of 99 (we'll call this number $99x$ ). We get the quadratic $n^2 + n - (90 + 198x) = 0.$ Using the quadratic formula we solve for $n$ : \[n = \frac{-1 \pm \sqrt{1^2 - 4(1)(-(90+198x))}}{2} = \frac{-1 \pm \sqrt{1 + 360 + 792x}}{2} = \frac{-1 \pm \sqrt{361 + 792x}}{2}.\] So now the problem becomes finding the least $x$ such that $361 + 792x$ is a perfect square, say $p^2.$ Rearranging gives $(p - 19)(p + 19) = 792x.$ We can prime factorize $792$ to get $2^3 \cdot 3^2 \cdot 11.$ So we need to multiply this with some number $x$ so that two factors multiplying to $792x$ differ by $38.$ We find that the least $x$ that works is $x = 10$ (we can have $110 \cdot 72 = 7920$ ). Then $n = \frac{-1 \pm 91}{2} = \xcancel{-46}, \boxed{45}.$
~ grogg007

## Solution 4
$a_n=a_{n-1} + n \pmod{99}$ . Using the steps of the previous solution we get up to $n^2+n \equiv 90 \pmod{99}$ . This gives away the fact that $(n)(n+1) \equiv 0 \pmod{9} \implies n \equiv \{0, 8\} \pmod{9}$ so either $n$ or $n+1$ must be a multiple of 9.
Case 1 ( $9 \mid n$ ): Say $n=9x$ and after simplification $x(9x+1) = 10 \pmod{90} \forall x \in \mathbb{Z}$ .
Case 2: ( $9 \mid n+1$ ): Say $n=9a-1$ and after simplification $(9a-1)(a) = 10 \pmod{90} \forall a \in \mathbb{Z}$ .
As a result $a$ must be a divisor of $10$ and after doing some testing in both cases the smallest value that works is $x=5 \implies \boxed{045}$ .
~First

## Solution 4.5 (not good, risky)
We just notice that $100 \equiv 1 \pmod{99}$ , so we are just trying to find $10 + 11 + 12 + \cdots + n$ modulo $99$ , or $\dfrac{n(n+1)}{2} - 45$ modulo $99$ . Also, the sum to $44$ is divisible by $99$ , and is the first one that is. Thus, if we sum to $45$ the $45$ is cut off and thus is just a sum to $44$ .
Without checking whether there are other sums congruent to $45 \pmod{99}$ , we can just write the answer to be $\boxed{045}$ .

## Solution 5
Let $b_n = 2a_{n+10}$ . We can find a formula for $b_n$ :
$b_n = (20+n)(n+1)$ .
Notice that both can't have a factor of 3. Thus we can limit our search range of n to $n \equiv 7,8 \pmod{9}$ . Testing values for n in our search range (like 7,8,16,17,25,26...), we get that 35 is the least n. But, don't write that down! Remember, $b_n = 2a_{n+10}$ , so, the 35th term in b corresponds to the 45th term in a. Thus our answer is $\boxed{045}$ .
-AlexLikeMath

## Solution 6 (slower and safer bash)
The first thing you should realize is that each term after the tenth is another two-digit number chained to the last number. $10, 1011, 101112, \dots$ . Now the fact that the sequence starts at $10$ can be completely discarded for this solution. Just consider $a(10)$ then same as $a(1)$ , and we can add nine to the answer at the end.
The second step is to split $99$ as $9$ and $11$ and solve for divisibility rules individually. Let's start with $11$ because it gives us the most information to continue.
In any number generated, if the numbers don't go beyond $20$ , then the highest number we can get is $10111213141516171819$ , with every odd digit being $1$ . This is a little risky because we are assuming that it doesn't exceed $20$ . If someone wanted to be absolutely sure they could continue, but this is unnecessary later and a big hassle. Anyways, now we write an equation to check for divisibility by $11$ . The expression being $\frac{((n-1) + 0)\cdot n)}{2}-n$ .
The concept here is to add $0$ to the $n-1^{th}$ term altogether, then subtract the number of ones in it, which is $n$ . Simplify to $\frac{n(n-3)}{2}$ congruent to $0 \pmod{11}$ . Now notice the divide by two can be discarded because one of $n$ or $(n-3)$ will be even. So if $n$ or $n-3$ is to be divisible by $11$ , we can make a simple list.
\[n = 0, 3, 11, 14, 22, 25, 33, 36, 44, 47, \dots\]
Now we test each $n$ for divisibility by $9$ . This is done by making a list that ultimately calculates the sum of every digit in the large number. $n(1)$ to $n(10)$ has the first digit $1$ . $n(11)$ to $n(20)$ has the first digit $2$ , and so on. The necessary thing to realize is that the sum of all digits $0-9$ is divisible by $9$ , so we only have to solve for the sum of the first digits, and then the short list of second digits.
For example, let's test $n=25$ .
So we know that $25$ include both $1-10$ and $11-20$ , so that's $10 + 20$ right away. $21-25$ contains $5$ numbers that have the first digit $3$ , so $+15$ . Then we add $0-4$ together, which is $10$ . $10+20+15+10=55$ , which is not divisible by $9$ , so it is not the answer.
Do this for just a minute you get that $36$ sums to $99$ , a multiple of nine! So $n(36)$ is the answer, right? Don't forget we have to add $9$ because we translated $n(10)$ to $n(1)$ at the very beginning! Finally, after a short bash, we get $\boxed{045}$ .
-jackshi2006 ( $LaTeX$ by PureSwag)

## Solution 7 (Timekilling plain Bash!!!!!!!!!!!!!!!!!)
We will work $\mod 99$ . The recursive formula now becomes $a_n=a_{n-1}+n$ . Now, we will bash. For convenience, everything is taken $\mod 99$ . The sequence is \begin{align*}a_{10}&=10 \\ a_{11}&=10+11=21 \\ a_{12}&=12+21=33 \\ a_{13}&=13+33=46 \\ a_{14}&=46+14=60 \\ a_{15}&=60+15=75 \\ a_{16}&=75+16=91 \\ a_{17}&=91+17=9 \\ a_{18}&=9+18=27 \\ a_{19}&=27+19=46 \\ a_{20}&=46+20=66 \\ a_{21}&=66+21=87 \\ a_{22}&=87+22=10 \\ a_{23}&=10+23=33 \\ a_{24}&=33+24=57 \\ a_{25}&=57+25=82 \\ a_{26}&=82+26=9 \\ a_{27}&=9+27=36 \\ a_{28}&=36+28=64 \\ a_{29}&=64+29=93 \\ a_{30}&=93+30=24 \\ a_{31}&=24+31=55 \\ a_{32}&=55+32=87 \\ a_{33}&=87+33=21 \\ a_{34}&=21+34=55 \\ a_{35}&=55+35=90 \\ a_{36}&=90+36=27 \\ a_{37}&=27+37=64 \\ a_{38}&=64+38=3 \\ a_{39}&=3+39=42 \\ a_{40}&=42+40=82 \\ a_{41}&=82+41=24 \\ a_{42}&=24+42=66 \\ a_{43}&=66+43=10 \\ a_{44}&=10+44=54 \\ a_{45}&=54+45=0.\end{align*} Hence the least number $n$ is $n=45$ .
~typos fixed by lpieleanu

## Solution 8
Taking the recurrence mod $99$ , we have \[a_n=a_{n-1}+n\] for $a_{10}=10$ . Then, we have \[a_n=10+11+12+\cdots+n \implies a_n=\frac{n(n+1)}2-45 \equiv 0 \pmod{99} \implies n(n+1)-90 \equiv 0 \pmod{99} \implies n(n+1)+9 \equiv 0 \pmod{99} \implies n \equiv 0 \pmod{9}.\] Then, we simply can test these values of $n$ to find that $n=\boxed{045}$ produces a value that is also divisible by $11$ .
-A1001
### Note
By the way, if you're wondering, $a_{45}$ is the $72$ -digit number \[101\text{,}112\text{,}131\text{,}415\text{,}161\text{,}718\text{,}192\text{,}021\text{,}222\text{,}324\text{,}252\text{,}627\text{,}282\text{,}930\text{,}313\text{,}233\text{,}343\text{,}536\text{,}373\text{,}839\text{,}404\text{,}142\text{,}434\text{,}445.\] The prime factorization of $a_{45}$ is \[3^{2}~\cdot~5~\cdot~11~\cdot~151~\cdot~1381~\cdot~1559~\cdot~1\text{,}511\text{,}647~\cdot~448\text{,}966\text{,}261\text{,}198\text{,}213\text{,}862\text{,}368\text{,}469~\cdot~925\text{,}800\text{,}120\text{,}162\text{,}193\text{,}934\text{,}310\text{,}647\text{,}599\text{,}013\] and $\frac{a_{45}}{99}$ is the $70$ -digit number \[1\text{,}021\text{,}334\text{,}660\text{,}759\text{,}209\text{,}274\text{,}666\text{,}881\text{,}033\text{,}578\text{,}309\text{,}366\text{,}494\text{,}245\text{,}588\text{,}215\text{,}591\text{,}276\text{,}503\text{,}428\text{,}324\text{,}671\text{,}055.\]
### Question
Is there an efficient way to notice that the only squares that are congruent to $64 \pmod {99}$ are $(\pm 8)^2$ and $(\pm 19)^2$ ? (In Solution 2)
Answer: Yes.
We will solve the question by looking for solutions for $m\in[-49,-48,\cdots,-1,0,1,\cdots,48,49]$ . Let the square be $m$ , thus satisfying $m^2-64\equiv 0\pmod{99}$ and $m^2-64=(m+8)(m-8)=99k$ for some integer $k$ . Checking the first factor, $(m+8)$ , for factors of $11$ yields:
$m+8=0\Rightarrow m-8=-16$
$m+8=11\Rightarrow m-8=-5$
$m+8=22\Rightarrow m-8=6$
$m+8=33\Rightarrow m-8=17$
$m+8=44\Rightarrow m-8=28$
In the first case, the product does divide $99$ , so $m=-8\equiv91$ is a solution. For the others, since the first factor already divides $11$ , the second factor must divide $9$ (or $3$ in the case of $m+8=33$ , which already has a factor of $3$ ) in order for the product to divide $99$ . Here, that is not the case, so $m=-8$ is the only possible solution.
Now we check the second factor, $(m-8)$ :
$m-8=0\Rightarrow m+8=16$
$m-8=11\Rightarrow m+8=27$
$m-8=22\Rightarrow m+8=38$
$m-8=33\Rightarrow m+8=49$
$m-8=44\Rightarrow m+8=60$
We immediately see that $m=8$ is a solution. Using a similar argument as above for the others, we notice that $m=19$ is the only solution in this group. Using the property that $ab\equiv(-a)(-b)\mod99$ , it is clear that $m=-19$ is also a solution. As a result, $m=\pm8$ and $m=\pm19$ are the only solutions. (This process takes a much shorter time than it seems.)
~eevee9406
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .