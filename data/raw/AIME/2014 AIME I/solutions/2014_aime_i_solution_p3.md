# 2014 AIME I Problem 3

## Problem

Find the number of rational numbers $r$ , $0<r<1$ , such that when $r$ is written as a fraction in lowest terms, the numerator and the denominator have a sum of 1000.

## Solution 1 (Euclidean algorithm, fast)
Let the numerator and denominator $x,y$ with $\gcd(x,y)=1$ and $x+y = 1000.$ Now if $\gcd(x,y) = 1$ then $\gcd(x,y) =\gcd(x,1000-x)= \gcd(x,1000-x-(-1)x)=\gcd(x,1000)=1.$ Therefore any pair that works satisfies $\gcd(x,1000)= 1.$ By Euler's totient theorem, there are $\phi(1000) = 400$ numbers relatively prime to 1000 from 1 to 1000. Recall that $r=\frac{x}{y}<1$ and note by Euclidean algorithm $\gcd(1000,1000-x)=1$ , so we want $x<y=1000-x.$ Thus the $400$ relatively prime numbers can generate $\boxed{200}$ desired fractions.

## Solution 2
If the initial manipulation is not obvious, consider the Euclidean Algorithm. Instead of using $\frac{n}{m}$ as the fraction to use the Euclidean Algorithm on, we can rewrite this as $\frac{500-x}{500+x}$ or \[\gcd(500+x,500-x)=\gcd((500+x)+(500-x),500-x)=\gcd(1000,500-x).\] Thus, we want $\gcd(1000,500-x)=1$ . You can either proceed as Solution $1$ , or consider that no even numbers work, limiting us to $250$ choices of numbers and restricting $x$ to be odd. If $x$ is odd, $500-x$ is odd, so the only possible common factors $1000$ and $500-x$ can share are multiples of $5$ . Thus, we want to avoid these. There are $50$ odd multiples of $5$ less than $500$ , so the answer is $250-50=\boxed{200}$ .

## Solution 3
Say $r=\frac{d}{1000-d}$ ; then $1\leq d\leq499$ . If this fraction is reducible, then the modulus of some number for $d$ is the same as the modulus for $1000-d$ . Since $1000=2^3\cdot5^3$ , that modulus can only be $2$ or $5$ . This implies that if $d\mid2$ or $d\mid5$ , the fraction is reducible. There are $249$ cases where $d\mid2$ , $99$ where $d\mid5$ , and $49$ where $d\mid(2\cdot5=10)$ , so by PIE, the number of fails is $299$ , so our answer is $\boxed{200}$ .

## Solution 4
We know that the numerator of the fraction cannot be even, because the denominator would also be even. We also know that the numerator cannot be a multiple of $5$ because the denominator would also be a multiple of $5$ . Proceed by listing out all the other possible fractions and we realize that the numerator and denominator are always relatively prime. We have $499$ fractions to start with, and $250$ with odd numerators. Subtract $50$ to account for the multiples of $5$ , and we get $\boxed{200}$ .

## Solution 5
We know that the set of these rational numbers is from $\dfrac{1}{999}$ to $\dfrac{499}{501}$ where each each element $\dfrac{n}{m}$ has $n+m =1000$ and $\dfrac{n}{m}$ is irreducible.
We note that $\dfrac{n}{m} =\dfrac{1000-m}{m}=\dfrac{1000}{m}-1$ . Hence, $\dfrac{n}{m}$ is irreducible if $\dfrac{1000}{m}$ is irreducible, and $\dfrac{1000}{m}$ is irreducible if $m$ is not divisible by $2$ or $5$ . Thus, the answer to the question is the number of integers between $501$ and $999$ inclusive that are not divisible by $2$ or $5$ .
We note there are $499$ numbers between $501$ and $999$ , and
- $249$ numbers are divisible by $2$
- $99$ numbers are divisible by $5$
- $49$ numbers are divisible by $10$
Using the Principle of Inclusion and Exclusion, we get that there are $499-249-99+49=200$ numbers between $501$ and $999$ are not divisible by either $2$ or $5$ , so our answer is $\boxed{200}$ .
Euler's Totient Function can also be used to arrive at $400$ numbers relatively prime to $1000$ , meaning $200$ possible fractions satisfying the necessary conditions. Solution 1 is a more detailed solution utilizing Euler's totient.

## Solution 6
We notice that there are a total of $400$ fractions that are in simplest form where the numerator and denominator add up to $1000$ . Because the numerator and denominator have to be relatively prime, there are $\varphi(1000)=400$ fractions. Half of these are greater than $1$ , so the answer is $400\div2=\boxed{200}$
- bedwarsnoob
~MathFun1000 (Minor Edits)

## Solution 7
Our fraction can be written in the form $\frac{1000 - a}{a} = \frac{1000}{a} - 1.$ Thus the fraction is reducible when $a$ divides $1000.$ We also want $500 < a < 1000.$ By PIE , the total values of $a$ that make the fraction reducible is, \[249 + 99 - 49 = 299.\] By complementary counting , the answer we want is $499 - 299 = \boxed{200}.$

## Solution 8 (Simplest)
Suppose our fraction is $\frac{a}{b}$ . The given condition means $a+b=1000$ . Now, if $a$ and $b$ share a common factor greater than $1$ , then the expression $a+b$ must also contain that common factor. This means our fraction cannot have a factor of $5$ or be even.
There are $250$ fractions that aren’t even. From this, $50$ are divisible by $5$ , which means the answer is $250-50=\boxed{200}$
~Geometry285
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .