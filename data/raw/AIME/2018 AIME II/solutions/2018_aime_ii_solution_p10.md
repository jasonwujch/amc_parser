# 2018 AIME II Problem 10

## Problem

Find the number of functions $f(x)$ from $\{1, 2, 3, 4, 5\}$ to $\{1, 2, 3, 4, 5\}$ that satisfy $f(f(x)) = f(f(f(x)))$ for all $x$ in $\{1, 2, 3, 4, 5\}$ .

## Solution 1
Just to visualize solution 1. If we list all possible $(x,f(x))$ , from ${1,2,3,4,5}$ to ${1,2,3,4,5}$ in a specific order, we get $5 \cdot 5 = 25$ different $(x,f(x))$ 's. Namely:
\[(1,1) (1,2) (1,3) (1,4) (1,5)\] \[(2,1) (2,2) (2,3) (2,4) (2,5)\] \[(3,1) (3,2) (3,3) (3,4) (3,5)\] \[(4,1) (4,2) (4,3) (4,4) (4,5)\] \[(5,1) (5,2) (5,3) (5,4) (5,5)\]
To list them in this specific order makes it a lot easier to solve this problem. We notice, In order to solve this problem at least one pair of $(x,x)$ where $x\in{1,2,3,4,5}$ must exist.In this case I rather "go backwards". First fixing $5$ pairs $(x,x)$ , (the diagonal of our table) and map them to the other fitting pairs $(x,f(x))$ . You can do this in $\frac{5!}{5!} = 1$ way. Then fixing $4$ pairs $(x,x)$ (The diagonal minus $1$ ) and map them to the other fitting pairs $(x,f(x))$ . You can do this in $4\cdot\frac{5!}{4!} = 20$ ways. Then fixing $3$ pairs $(x,x)$ (The diagonal minus $2$ ) and map them to the other fitting pairs $(x,f(x))$ . You can do this in $\tfrac{(5\cdot4\cdot3\cdot6\cdot3)}{3!2!} + \tfrac{(5\cdot4\cdot3\cdot6\cdot1)}{3!} = 150$ ways. Fixing $2$ pairs $(x,x)$ (the diagonal minus $3$ ) and map them to the other fitting pairs $(x,f(x))$ . You can do this in $\frac{(5\cdot4\cdot6\cdot4\cdot2)}{2!3!} + \frac{(5\cdot4\cdot6\cdot4\cdot2)}{2!2!} + \frac{(5\cdot4\cdot6\cdot2\cdot1)}{2!2!} = 380$ ways. Lastly, fixing $1$ pair $(x,x)$ (the diagonal minus $4$ ) and map them to the other fitting pairs $(x,f(x))$ . You can do this in $\tfrac{5!}{4!} + 4\cdot\tfrac{5!}{3!} + 5! = 205$ ways.
So $1 + 20 + 150 + 380 + 205 = \framebox{756}$

## Solution 2
We perform casework on the number of fixed points (the number of points where $f(x) = x$ ). There must be at least one fixed point, given $f(f(x))$ has some value and is a fixed point. To better visualize this, use the grid from Solution 1.
Case 1: 5 fixed points
Case 2: 4 fixed points
Case 3: 3 fixed points
Case 4: 2 fixed points
Case 5: 1 fixed point
Therefore, the answer is $1+20+150+380+205 = \boxed{756}$
~First

## Solution 3
We can do some caseworks about the special points of functions $f$ for $x\in\{1,2,3,4,5\}$ . Let $x$ , $y$ and $z$ be three different elements in set $\{1,2,3,4,5\}$ . There must be elements such like $k$ in set $\{1,2,3,4,5\}$ satisfies $f(k)=k$ , and we call the points such like $(k,k)$ on functions $f$ are "Good Points" (Actually its academic name is "fixed-points"). The only thing we need to consider is the "steps" to get "Good Points". Notice that the "steps" must less than $3$ because the highest iterations of function $f$ is $3$ . Now we can classify $3$ cases of “Good points” of $f$ .
$\textbf{Case 1:}$ One "step" to "Good Points": Assume that $f(x)=x$ , then we get $f(f(x))=f(x)=x$ , and $f(f(f(x)))=f(f(x))=f(x)=x$ , so $f(f(f(x)))=f(f(x))$ .
$\textbf{Case 2:}$ Two "steps" to "Good Points": Assume that $f(x)=y$ and $f(y)=y$ , then we get $f(f(x))=f(y)=y$ , and $f(f(f(x)))=f(f(y))=f(y)=y$ , so $f(f(f(x)))=f(f(x))$ .
$\textbf{Case 3:}$ Three "steps" to "Good Points": Assume that $f(x)=y$ , $f(y)=z$ and $f(z)=z$ , then we get $f(f(x))=f(y)=z$ , and $f(f(f(x)))=f(f(y))=f(z)=z$ , so $f(f(f(x)))=f(f(x))$ .
Divide set $\{1,2,3,4,5\}$ into three parts which satisfy these three cases, respectively. Let the first part has $a$ elements, the second part has $b$ elements and the third part has $c$ elements, it is easy to see that $a+b+c=5$ . First, there are $\binom{5}{a}$ ways to select $x$ for Case 1. Second, we have $\binom{5-a}{b}$ ways to select $x$ for Case 2. After that we map all elements that satisfy Case 2 to Case 1, and the total number of ways of this operation is $a^b$ . Finally, we map all the elements that satisfy Case 3 to Case 2, and the total number of ways of this operation is $b^c$ . As a result, the number of such functions $f$ can be represented in an algebraic expression contains $a$ , $b$ and $c$ : $\boxed{\binom{5}{a}\cdot \binom{5-a}{b}\cdot a^b\cdot b^c}$
Now it's time to consider about the different values of $a$ , $b$ and $c$ and the total number of functions $f$ satisfy these values of $a$ , $b$ and $c$ :
For $a=5$ , $b=0$ and $c=0$ , the number of $f$ s is $\binom{5}{5}=1$
For $a=4$ , $b=1$ and $c=0$ , the number of $f$ s is $\binom{5}{4}\cdot \binom{1}{1}\cdot 4^1\cdot 1^0=20$
For $a=3$ , $b=1$ and $c=1$ , the number of $f$ s is $\binom{5}{3}\cdot \binom{2}{1}\cdot 3^1\cdot 1^1=60$
For $a=3$ , $b=2$ and $c=0$ , the number of $f$ s is $\binom{5}{3}\cdot \binom{2}{2}\cdot 3^2\cdot 2^0=90$
For $a=2$ , $b=1$ and $c=2$ , the number of $f$ s is $\binom{5}{2}\cdot \binom{3}{1}\cdot 2^1\cdot 1^2=60$
For $a=2$ , $b=2$ and $c=1$ , the number of $f$ s is $\binom{5}{2}\cdot \binom{3}{2}\cdot 2^2\cdot 2^1=240$
For $a=2$ , $b=3$ and $c=0$ , the number of $f$ s is $\binom{5}{2}\cdot \binom{3}{3}\cdot 2^3\cdot 3^0=80$
For $a=1$ , $b=1$ and $c=3$ , the number of $f$ s is $\binom{5}{1}\cdot \binom{4}{1}\cdot 1^1\cdot 1^3=20$
For $a=1$ , $b=2$ and $c=2$ , the number of $f$ s is $\binom{5}{1}\cdot \binom{4}{2}\cdot 1^2\cdot 2^2=120$
For $a=1$ , $b=3$ and $c=1$ , the number of $f$ s is $\binom{5}{1}\cdot \binom{4}{3}\cdot 1^3\cdot 3^1=60$
For $a=1$ , $b=4$ and $c=0$ , the number of $f$ s is $\binom{5}{1}\cdot \binom{4}{4}\cdot 1^4\cdot 4^0=5$
Finally, we get the total number of function $f$ , the number is $1+20+60+90+60+240+80+20+120+60+5=\boxed{756}$
~Solution by $BladeRunnerAUG$ (Frank FYC)
### Note (fun fact)
This exact problem showed up earlier on the 2011 Stanford Math Tournament, Advanced Topics Test. This problem also showed up on the 2010 Mock AIME 2 here: https://artofproblemsolving.com/wiki/index.php/Mock_AIME_2_2010_Problems
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .