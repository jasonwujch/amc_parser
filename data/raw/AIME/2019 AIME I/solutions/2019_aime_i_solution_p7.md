# 2019 AIME I Problem 7

## Problem

There are positive integers $x$ and $y$ that satisfy the system of equations \begin{align*} \log_{10} x + 2 \log_{10} (\text{gcd}(x,y)) &= 60\\ \log_{10} y + 2 \log_{10} (\text{lcm}(x,y)) &= 570. \end{align*} Let $m$ be the number of (not necessarily distinct) prime factors in the prime factorization of $x$ , and let $n$ be the number of (not necessarily distinct) prime factors in the prime factorization of $y$ . Find $3m+2n$ .

## Solution 1
Add the two equations to get that $\log x+\log y+2(\log(\gcd(x,y))+2(\log(\text{lcm}(x,y)))=630$ . Then, we use the theorem $\log a+\log b=\log ab$ to get the equation, $\log (xy)+2(\log(\gcd(x,y))+\log(\text{lcm}(x,y)))=630$ . Using the theorem that $\gcd(x,y) \cdot \text{lcm}(x,y)=x\cdot y$ , along with the previously mentioned theorem, we can get the equation $3\log(xy)=630$ . This can easily be simplified to $\log(xy)=210$ , or $xy = 10^{210}$ .
$10^{210}$ can be factored into $2^{210} \cdot 5^{210}$ , and $m+n$ equals to the sum of the exponents of $2$ and $5$ , which is $210+210 = 420$ . Multiply by two to get $2m +2n$ , which is $840$ . Then, use the first equation ( $\log x + 2\log(\gcd(x,y)) = 60$ ) to show that $x$ has to have lower degrees of $2$ and $5$ than $y$ (you can also test when $x>y$ , which is a contradiction to the restrains we set before). Therefore, $\gcd(x,y)=x$ . Then, turn the equation into $3\log x = 60$ , which yields $\log x = 20$ , or $x = 10^{20}$ . Factor this into $2^{20} \cdot 5^{20}$ , and add the two 20's, resulting in $m$ , which is $40$ . Add $m$ to $2m + 2n$ (which is $840$ ) to get $40+840 = \boxed{880}$ .
~minor mistake fix by virjoy2001 ~minor mistake fix by oralayhan
Remark: You can obtain the contradiction by using LTE. If $\nu_2{(x)}\geq{\nu_2{(y)}}, \nu_2{(y^2x)}=60$ . However, $\nu_2{(xy)}=210$ a contradiction. Same goes with taking $\nu_5{(x,y)}$
### Easier Approach to Finish
After noting that $xy=10^{210},$ notice that we can let $x=10^a$ and $y=10^b.$ Thus, we have from the given equations (1) and (2) respectively, that: \[a+2a=60\] \[b+2b=570\] Solving, we get $(a,b)=(20,190).$ This matches with our constraint that $xy=10^{210}$ (this constraint can actually be rederived by adding the two equations) so we finish from here.
$x=2^{20}\cdot 5^{20}, y=2^{190}\cdot 5^{190}.$ Thus, the answer desired is $3(20+20)+2(190+190)=880.$ ~mathboy282 (minor addition by Technodoggo)

## Solution 2
First simplifying the first and second equations, we get that
\[\log_{10}(x\cdot\text{gcd}(x,y)^2)=60\] \[\log_{10}(y\cdot\text{lcm}(x,y)^2)=570\]
Thus, when the two equations are added, we have that \[\log_{10}(x\cdot y\cdot\text{gcd}^2\cdot\text{lcm}^2)=630\] When simplified, this equals \[\log_{10}(x^3y^3)=630\] so this means that \[x^3y^3=10^{630}\] so \[xy=10^{210}.\]
Now, the following cannot be done on a proof contest but let's (intuitively) assume that $x<y$ and $x$ and $y$ are both powers of $10$ . This means the first equation would simplify to \[x^3=10^{60}\] and \[y^3=10^{570}.\] Therefore, $x=10^{20}$ and $y=10^{190}$ and if we plug these values back, it works! $10^{20}$ has $20\cdot2=40$ total factors and $10^{190}$ has $190\cdot2=380$ so \[3\cdot 40 + 2\cdot 380 = \boxed{880}.\]
Please remember that you should only assume on these math contests because they are timed; this would technically not be a valid solution.

## Solution 3 (Easy Solution)
Let $x=10^a$ and $y=10^b$ and $a<b$ . Then the given equations become $3a=60$ and $3b=570$ . Therefore, $x=10^{20}=2^{20}\cdot5^{20}$ and $y=10^{190}=2^{190}\cdot5^{190}$ . Our answer is $3(20+20)+2(190+190)=\boxed{880}$ .
Note from Wiselion: This solution also uses the assumptions as solution 2. In theory x and y don/t have to be power of 10. Although having it not a power of 10 suggests that the sums won't be integers, if the gcd and lcm logs match up respectively with the remains of log x and y then the logs could add up to an integer. (We'd have to prove it) (PS never wrote the solution)

## Solution 4
We will use the notation $(a, b)$ for $\gcd(a, b)$ and $[a, b]$ as $\text{lcm}(a, b)$ . We can start with a similar way to Solution 1. We have, by logarithm properties, $\log_{10}{x}+\log_{10}{(x, y)^2}=60$ or $x(x, y)^2=10^{60}$ . We can do something similar to the second equation and our two equations become \[x(x, y)^2=10^{60}\] \[y[x, y]^2=10^{570}\] Adding the two equations gives us $xy(x, y)^2[x, y]^2=10^{630}$ . Since we know that $(a, b)\cdot[a, b]=ab$ , $x^3y^3=10^{630}$ , or $xy=10^{210}$ . We can express $x$ as $2^a5^b$ and $y$ as $2^c5^d$ . Another way to express $(x, y)$ is now $2^{min(a, c)}5^{min(b, d)}$ , and $[x, y]$ is now $2^{max(a, c)}5^{max(b, d)}$ . We know that $x<y$ , and thus, $a<c$ , and $b<d$ . Our equations for $lcm$ and $gcd$ now become \[2^a5^b(2^a5^a)^2=10^{60}\] or $a=b=20$ . Doing the same for the $lcm$ equation, we have $c=d=190$ , and $190+20=210$ , which satisfies $xy=210$ . Thus, $3m+2n=3(20+20)+2(190+190)=\boxed{880}$ . ~awsomek

## Solution 5
Let $x=d\alpha, y=d\beta, (\alpha, \beta)=1$ . Simplifying, $d^3\alpha=10^{60}, d^3\alpha^2\beta^3=10^{510} \implies \alpha\beta^3 = 10^{510}=2^{510} \cdot 5^{510}$ . Notice that since $\alpha, \beta$ are coprime, and $\alpha < 5^{90}$ (Prove it yourself !) , $\alpha=1, \beta = 10^{170}$ . Hence, $x=10^{20}, y=10^{190}$ giving the answer $\boxed{880}$ .
(Solution by Prabh1512)

## Solution 6 (Official MAA)
The two equations are equivalent to $x(\gcd(x,y))^2=10^{60}$ and $y(\operatorname{lcm}(x,y))^2=10^{570}$ respectively. Multiplying corresponding sides of the equations leads to $xy(\gcd(x,y)\operatorname{lcm}(x,y))^2=(xy)^3=10^{630}$ , so $xy=10^{210}$ . It follows that there are nonnegative integers $a,\,b,\,c,$ and $d$ such that $(x,y)=(2^a5^b,2^c5^d)$ with $a+c=b+d=210$ . Furthermore, \[\frac{(\operatorname{lcm}(x,y))^2}{x}=\frac{y(\operatorname{lcm}(x,y))^2}{xy}=\frac{10^{570}}{10^{210}}=10^{360}.\] Thus $\max(2a,2c)-a=\max(2b,2d)-b=360.$ Because neither $2a-a$ nor $2b-b$ can equal $360$ when $a+c=b+d=210,$ it follows that $2c-a=2d-b=360$ . Hence $(a,b,c,d)=(20,20,190,190)$ , so the prime factorization of $x$ has $20+20=40$ prime factors, and the prime factorization of $y$ has $190+190=380$ prime factors. The requested sum is $3\cdot40+2\cdot380=880.$

## Solution 7
Add the two equations and use the fact that $\gcd\left(x,y\right)\cdot\mathrm{lcm}\left(x,y\right)=xy$ to find that $xy=10^{210}$ . So let $x=2^a5^b$ and $y=2^{210-a}5^{210-b}$ for $0\leq a,b\leq210$ . If $a\geq105$ then the exponent of $2$ in $x\cdot\gcd\left(x,y\right)^2=10^{60}$ is $a+2\left(210-a\right)=420-a$ , so $a=360$ , contradiction. So $a<105$ . Then the exponent of $2$ in $x\cdot\gcd\left(x,y\right)^2$ is $a+2a=3a$ , so $a=20$ . Similarly, $b=20$ . Then $3m+2n=3\left(a+b\right)+2\left(420-a-b\right)=\boxed{880}$ as desired.
~from trumpeter in the AoPS Forums Contest Discussion

## Solution 8
We can simplify the equations step by step. The first equation simplifies to $log($ (x)( $(gcd(x,y))^2$ ) $)=60$ . The second equation simplifies to log( $(y)$ ( $(lcm(x,y)^2$ ) $)=570$ . Up to here, we used the exponent and addition log identities.
Now before we move on to the next few simplification steps, we must remember that $gcd(a,b)$ * $lcm(a,b)$ = $a*b$ .
We've now gotten to the crucial part of this equation. Though this wouldn't pass for full points in a proof-based contest, this is AIME. So, we assume that $x<y$ . We also let $x$ = $10^a$ and $y$ = $10^b$ That means that $gcd(x,y)$ is $x$ and the $lcm(x,y)$ is $y$ due to the fact that we are also assuming that both $x,y$ are $10^a$ , $10^b$ respectively.
If we put our last few insights together into the first and second equation, we see that $x$ = $10^{20}$ . We also see that $y$ = $10^{190}$ . We could check these if wanted (don't worry they work), but if you were very limited on time for this question, just assume these values work and move on.
Now $10^{20}$ factors as $2^{20}$ * $5^{20}$ . This has $40$ prime factors. $2$ , $20$ times and $5$ , $20$ times. $10^{190}$ factors as $2^{190}$ * $5^{190}$ . This has $380$ prime factors. $2$ , $190$ times and $5$ , $190$ times. Now it's just $40*3+380*2=880$ as our final answer.
-Schintalpati

## Video Solution(Pretty Straightforward)
https://www.youtube.com/watch?v=NOLk9-A4eDo Remember to subscribe!
~North America math Contest Go Go Go
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .