# 2017 AIME I Problem 7

## Problem

For nonnegative integers $a$ and $b$ with $a + b \leq 6$ , let $T(a, b) = \binom{6}{a} \binom{6}{b} \binom{6}{a + b}$ . Let $S$ denote the sum of all $T(a, b)$ , where $a$ and $b$ are nonnegative integers with $a + b \leq 6$ . Find the remainder when $S$ is divided by $1000$ .

### Major Note

Most solutions use committee forming (except for the bash solution). To understand more about the techniques used, visit the committee forming page for more information.

## Solution 1 (Committee Forming)
Let $c=6-(a+b)$ , and note that $\binom{6}{a + b}=\binom{6}{c}$ . The problem thus asks for the sum $\binom{6}{a} \binom{6}{b} \binom{6}{c}$ over all $a,b,c$ such that $a+b+c=6$ . Consider an array of 18 dots, with 3 columns of 6 dots each. The desired expression counts the total number of ways to select 6 dots by considering each column separately, which is equal to $\binom{18}{6}=18564$ . Therefore, the answer is $\boxed{564}$ .
-rocketscience

## Solution 1 but different (Committee Forming)
Alternatively, one can note that we can consider groups where $a+b$ is constant, say $c$ . Fix any value of $c$ . Then the sum of all of the values of $T(a,b)$ such that $a+b=c$ is $\binom{6}{a+b} \sum_{a+b=c} \binom{6}{a}\binom{6}{b}$ which by Vandermonde's is $\binom{6}{a+b}\binom{12}{a+b}$ . Remember, that expression is the resulting sum for a fixed $a+b$ . So, for $a+b\le 6$ , we want $\sum_{c=0}^{6} \binom{6}{c}\binom{12}{c}$ . This is (by Vandermonde's or committee forming) $\binom{18}{6} = 18564 \implies \boxed{564}$ ~ firebolt360
### Note
Now just a quick explanation for people who don't fully understand Vandermonde's. Take the first part, $\sum_{a+b=c} \binom{6}{a}\binom{6}{b}$ . Consider $2$ different groups, $A$ and $B$ both of size $6$ people. We wish to chose $a$ peoples from $A$ and $b=c-a$ people from $B$ . In total, we chose $c-a+a=c$ people. We can then draw a bijection towards choosing $c$ people from $A\cup B$ , which has size $12$ . So, it is $\binom{12}{c}=\binom{12}{a+b}$ . Similarly, for $\sum_{c=6} \binom{6}{c}\binom{12}{c}$ , we see that $\binom{6}{c}=\binom{6}{6-c}$ . Now the total is $18$ , and the sum is $6$ . So, we get $\binom{18}{6}$ . See committee forming for more information ~ firebolt360

## Solution 2 (Committee Forming but slightly more bashy)
Treating $a+b$ as $n$ , this problem asks for \[\sum_{n=0}^{6} \left[\binom{6}{n}\sum_{m=0}^{n}\left[\binom{6}{m}\binom{6}{n-m}\right]\right].\] But \[\sum_{m=0}^{n} \left[\binom{6}{m} \binom{6}{n-m}\right]\] can be computed through the following combinatorial argument. Choosing $n$ elements from a set of size $12$ is the same as splitting the set into two sets of size $6$ and choosing $m$ elements from one, $n-m$ from the other where $0\leq m\leq n$ . The number of ways to perform such a procedure is simply $\binom{12}{n}$ . Therefore, the requested sum is \[\sum_{n=0}^{6} \left[\binom{6}{n} \binom{12}{n}\right] = 18564.\] As such, our answer is $\boxed{564}$ .
Note from epiconan: To avoid the bash, you can actually use Vandermondes $\emph{again}$ . \[\sum_{n=0}^{6} \left[\binom{6}{n} \binom{12}{n}\right] = \sum_{n=0}^{6} \left[\binom{6}{6-n} \binom{12}{n}\right] = \binom{6+12}{6} = \binom{18}{6}.\] - Awsomness2000

## Solution 3 (Major Major Bash)
Case 1: $a<b$ .
Subcase 1: $a=0$ \[\binom{6}{0}\binom{6}{1}\binom{6}{1}=36\] \[\binom{6}{0}\binom{6}{2}\binom{6}{2}=225\] \[\binom{6}{0}\binom{6}{3}\binom{6}{3}=400\] \[\binom{6}{0}\binom{6}{4}\binom{6}{4}=225\] \[\binom{6}{0}\binom{6}{5}\binom{6}{5}=36\] \[\binom{6}{0}\binom{6}{6}\binom{6}{6}=1\] \[36+225+400+225+36+1=923\] Subcase 2: $a=1$ \[\binom{6}{1}\binom{6}{2}\binom{6}{3}=1800 \equiv 800 \pmod {1000}\] \[\binom{6}{1}\binom{6}{3}\binom{6}{4}=1800 \equiv 800 \pmod {1000}\] \[\binom{6}{1}\binom{6}{4}\binom{6}{5}=540\] \[\binom{6}{1}\binom{6}{5}\binom{6}{6}=36\] \[800+800+540+36=2176 \equiv 176 \pmod {1000}\] Subcase 3: $a=2$ \[\binom{6}{2}\binom{6}{3}\binom{6}{5}=1800\equiv800\pmod{1000}\] \[\binom{6}{2}\binom{6}{4}\binom{6}{6}=225\] \[800+225=1025\equiv25\pmod{1000}\]
\[923+176+25=1124\equiv124\pmod{1000}\]
Case 2: $b<a$
By just switching $a$ and $b$ in all of the above cases, we will get all of the cases such that $b>a$ is true. Therefore, this case is also $124\pmod{1000}$
Case 3: $a=b$ \[\binom{6}{0}\binom{6}{0}\binom{6}{0}=1\] \[\binom{6}{1}\binom{6}{1}\binom{6}{2}=540\] \[\binom{6}{2}\binom{6}{2}\binom{6}{4}=3375\equiv375\pmod{1000}\] \[\binom{6}{3}\binom{6}{3}\binom{6}{6}=400\] \[1+540+375+400=1316\equiv316\pmod{1000}\]
\[316+124+124=\boxed{\boxed{564}}\]

## Solution 4
We begin as in solution 1 to rewrite the sum as $\binom{6}{a} \binom{6}{b} \binom{6}{c}$ over all $a,b,c$ such that $a+b+c=6$ . Consider the polynomial $P(x)=\left(\binom{6}{0} + \binom{6}{1}x + \binom{6}{2}x^2 + \binom{6}{3}x^3 + \cdot \cdot \cdot + \binom{6}{6}x^6\right)^3$ . We can see the sum we wish to compute is just the coefficient of the $x^6$ term. However $P(x)=((1+x)^6)^3=(1+x)^{18}$ . Therefore, the coefficient of the $x^6$ term is just $\binom{18}{6} = 18564$ so the answer is $\boxed{564}$ .
- mathymath

## Solution 5 (Committee Forming but different)
Let $c=6-(a+b)$ . Then $\binom{6}{a+b}=\binom{6}{c}$ , and $a+b+c=6$ . The problem thus asks for \[\sum_{a+b+c=6}\binom{6}{a}\binom{6}{b}\binom{6}{c} \pmod {1000}.\] Suppose we have $6$ red balls, $6$ green balls, and $6$ blue balls lined up in a row, and we want to choose $6$ balls from this set of $18$ balls by considering each color separately. Over all possible selections of $6$ balls from this set, there are always a nonnegative number of balls in each color group. The answer is $\binom{18}{6} \pmod {1000}=18\boxed{564}$ .

## Solution 5 but different (Committee Forming)
Since $\binom{6}{n}=\binom{6}{6-n}$ , we can rewrite $T(a,b)$ as $\binom{6}{a}\binom{6}{b}\binom{6}{6-(a+b)}$ . Consider the number of ways to choose a committee of 6 people from a group of 6 democrats, 6 republicans, and 6 independents. We can first pick $a$ democrats, then pick $b$ republicans, provided that $a+b \leq 6$ . Then we can pick the remaining $6-(a+b)$ people from the independents. But this is just $T(a,b)$ , so the sum of all $T(a,b)$ is equal to the number of ways to choose this committee. On the other hand, we can simply pick any 6 people from the $6+6+6=18$ total politicians in the group. Clearly, there are $\binom{18}{6}$ ways to do this. So the desired quantity is equal to $\binom{18}{6}$ . We can then compute (routinely) the last 3 digits of $\binom{18}{6}$ as $\boxed{564}$ .

## Solution 6(NICE Journal)
Note that $\binom{6}{a+b} = \binom{6}{6-a-b}$ . So we have $\binom{6}{a}\binom{6}{b}\binom{6}{6-a-b}$ . If we think about this this is essentially choosing a group of $a$ people from $6$ people, a group of $b$ people from $6$ people, and a group of $6 - a -b$ from another group of $6$ people. This is nothing but choosing $6$ people from a group of $18$ people. This is nothing but $\binom{18}{6} = 18564 \Rightarrow 564$ . ~coolmath_2018
### Remark
This problem is an example of the generalization of Vandermonde's theorem, which states that for nonnegative $k_1, k_2, \ldots k_p$ and $n_1, n_2, \ldots n_p$ , we have \[\sum _{k_1+\cdots +k_p=m}\binom{n_1}{k_1} \binom{n_2}{k_2} \cdots \binom{n_p}{k_p} = \binom{n_1+ \cdots +n_p}{m}.\] ~eibc
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .