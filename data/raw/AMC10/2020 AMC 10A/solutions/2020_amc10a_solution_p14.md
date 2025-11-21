# 2020 AMC 10A Problem 14

## Problem

Real numbers $x$ and $y$ satisfy $x + y = 4$ and $x \cdot y = -2$ . What is the value of

\[x + \frac{x^3}{y^2} + \frac{y^3}{x^2} + y?\]

$\textbf{(A)}\ 360\qquad\textbf{(B)}\ 400\qquad\textbf{(C)}\ 420\qquad\textbf{(D)}\ 440\qquad\textbf{(E)}\ 480$

## Solutions

## Solution 1
\[x + \frac{x^3}{y^2} + \frac{y^3}{x^2} + y=x+\frac{x^3}{y^2}+y+\frac{y^3}{x^2}=\frac{x^3}{x^2}+\frac{y^3}{x^2}+\frac{y^3}{y^2}+\frac{x^3}{y^2}\]
Continuing to combine \[\frac{x^3+y^3}{x^2}+\frac{x^3+y^3}{y^2}=\frac{(x^2+y^2)(x^3+y^3)}{x^2y^2}=\frac{(x^2+y^2)(x+y)(x^2-xy+y^2)}{x^2y^2}\] From the givens, it can be concluded that $x^2y^2=4$ . Also, \[(x+y)^2=x^2+2xy+y^2=16\] This means that $x^2+y^2=20$ . Substituting this information into $\frac{(x^2+y^2)(x+y)(x^2-xy+y^2)}{x^2y^2}$ , we have $\frac{(20)(4)(22)}{4}=20\cdot 22=\boxed{\textbf{(D)}\ 440}$ . ~PCChess

## Solution 2
As above, we need to calculate $\frac{(x^2+y^2)(x^3+y^3)}{x^2y^2}$ . Note that $x,y,$ are the roots of $x^2-4x-2$ and so $x^3=4x^2+2x$ and $y^3=4y^2+2y$ . Thus $x^3+y^3=4(x^2+y^2)+2(x+y)=4(20)+2(4)=88$ where $x^2+y^2=20$ and $x^2y^2=4$ as in the previous solution. Thus the answer is $\frac{(20)(88)}{4}=\boxed{\textbf{(D)}\ 440}$ . Note( $x^2+y^2=(x+y)^2-2xy=20$ , and $x^2y^2 = (xy)^2 = 4$ )

## Solution 3
Note that $( x^3 + y^3 ) ( \frac{1}{y^2} + \frac{1}{x^2} ) = x + \frac{x^3}{y^2} + \frac{y^3}{x^2} + y.$ Now, we only need to find the values of $x^3 + y^3$ and $\frac{1}{y^2} + \frac{1}{x^2}.$ Recall that $x^3 + y^3 = (x + y) (x^2 - xy + y^2),$ and that $x^2 - xy + y^2 = (x + y)^2 - 3xy.$ We are able to solve the second equation, and doing so gets us $4^2 - 3(-2) = 22.$ Plugging this into the first equation, we get $x^3 + y^3 = 4(22) = 88.$ In order to find the value of $\frac{1}{y^2} + \frac{1}{x^2},$ we find a common denominator so that we can add them together. This gets us $\frac{x^2}{x^2 y^2} + \frac{y^2}{x^2 y^2} = \frac{x^2 + y^2}{(xy)^2}.$ Recalling that $x^2 + y^2 = (x+y)^2 - 2xy$ and solving this equation, we get $4^2 - 2(-2) = 20.$ Plugging this into the first equation, we get $\frac{1}{y^2} + \frac{1}{x^2} = \frac{20}{(-2)^2} = 5.$ Solving the original equation, we get $x + \frac{x^3}{y^2} + \frac{y^3}{x^2} + y = (88)(5) = \boxed{\textbf{(D)}\ 440}.$ ~ emerald_block

## Solution 3.5 (Binomial Theorem and Sum of Cubes, not that messy)
The expression can be rewritten as:
\[x + y + \frac{x^3}{y^2} + \frac{y^3}{x^2} = \frac{x^5 + y^5}{(xy)^2} + (x + y)\]
Plug in what we know:
\[\frac{x^5 + y^5}{4} + 4\]
Use Binomial Theorem to expand and simplify the numerator of the fraction:
\[x^5 + y^5 = (x + y)^5 - 5(x^4y + xy^4 + 2x^3y^2 + 2x^2y^3)\] \[= (x + y)^5 -5xy((x + y)^3 - xy(x + y))\] \[= 4^5 + 10(4^3 + 8).\]
Plug this back into the expression to finally get:
\[\frac{4^5 + 10(4^3 + 8)}{4} + 4 = 4^4 + 10(4^2 + 2) + 4 = 256 + 180 + 4 = \boxed{440}.\]
~ grogg007

## Solution 4 (Bashing)
This is basically bashing using Vieta's formulas to find $x$ and $y$ (which I highly do not recommend, I only wrote this solution for fun).
We use Vieta's to find a quadratic relating $x$ and $y$ . We set $x$ and $y$ to be the roots of the quadratic $Q ( n ) = n^2 - 4n - 2$ (because $x + y = 4$ , and $xy = -2$ ). We can solve the quadratic to get the roots $2 + \sqrt{6}$ and $2 - \sqrt{6}$ . $x$ and $y$ are "interchangeable" (WLOG, without loss of generality, we could have $x$ equal one and $y$ equal the other), meaning that it doesn't matter which solution $x$ or $y$ is, because it'll return the same result when plugged in. So we plug in $2 + \sqrt{6}$ for $x$ and $2 - \sqrt{6}$ and get $\boxed{\textbf{(D)}\ 440}$ as our answer.
~Baolan
~<B+

## Solution 5 (Bashing Part 2)
This usually wouldn't work for most problems like this, but we're lucky that we can quickly expand and factor this expression in this question.
We first change the original expression to $4 + \frac{x^5 + y^5}{x^2 y^2}$ , because $x + y = 4$ . This is equal to $4 + \frac{(x + y)(x^4 - x^3 y + x^2 y^2 - x y^3 + y^4)}{4} = x^4 + y^4 - x^3 y - x y^3 + 8$ . We can factor and reduce $x^4 + y^4$ to $(x^2 + y^2)^2 - 2 x^2 y^2 = ((x + y)^2 - 2xy)^2 - 8 = 400 - 8 = 392$ . Now our expression is just $400 - (x^3 y + x y^3)$ . We factor $x^3 y + x y^3$ to get $(xy)(x^2 + y^2) = -40$ . So the answer would be $400 - (-40) = \boxed{\textbf{(D)} 440}$ .

## Solution 6 (Complete Binomial Theorem)
We first simplify the expression to \[x + y + \frac{x^5 + y^5}{x^2y^2}.\] Then, we can solve for $x$ and $y$ given the system of equations in the problem. Since $xy = -2,$ we can substitute $\frac{-2}{x}$ for $y$ . Thus, this becomes the equation \[x - \frac{2}{x} = 4.\] Multiplying both sides by $x$ , we obtain $x^2 - 2 = 4x,$ or \[x^2 - 4x - 2 = 0.\] By the quadratic formula we obtain $x = 2 \pm \sqrt{6}$ . We also easily find that given $x = 2 \pm \sqrt{6}$ , $y$ equals the conjugate of $x$ . Thus, plugging our values in for $x$ and $y$ , our expression equals \[4 + \frac{(2 - \sqrt{6})^5 + (2 + \sqrt{6})^5}{(2 - \sqrt{6})^2(2 + \sqrt{6})^2}\] By the binomial theorem, we observe that every second terms of the expansions $x^5$ and $y^5$ will cancel out (since a positive plus a negative of the same absolute value equals zero). We also observe that the other terms not canceling out are doubled when summing the expansions of $x^5 + y^5$ . Thus, our expression equals \[4 + \frac{2(2^5 + \tbinom{5}{2}2^3 \times 6 + \tbinom{5}{4}2 \times 36)}{(2 - \sqrt{6})^2(2 + \sqrt{6})^2}.\] which equals \[4 + \frac{2(872)}{4}\] which equals $\boxed{\textbf{(D)} 440}$ .
~ fidgetboss_4000

## Solution 7
As before, simplify the expression to \[x + y + \frac{x^5 + y^5}{x^2y^2}.\] Since $x + y = 4$ and $x^2y^2 = 4$ , we substitute that in to obtain \[4 + \frac{x^5 + y^5}{4}.\] Now, we must solve for $x^5 + y^5$ . Start by squaring $x + y$ , to obtain \[x^2 + 2xy + y^2 = 16\] Simplifying, $x^2 + y^2 = 20$ . Squaring once more, we obtain \[x^4 + y^4 + 2x^2y^2 = 400\] Once again simplifying, $x^4 + y^4 = 392$ . Now, to obtain the fifth powers of $x$ and $y$ , we multiply both sides by $x + y$ . We now have \[x^5 + x^4y + xy^4 + y^5 = 1568\] , or \[x^5 + y^5 + xy(x^3 + y^3) = 1568\] We now solve for $x^3 + y^3$ . $(x + y)^3=x^3 + y^3 + 3xy(x + y) = 64$ , so $x^3 + y^3 = 88$ . Plugging this back into $x^5 + x^4y + xy^4 + y^5 = 1568$ , we find that $x^5 + y^5 = 1744$ , so we have \[4 + \frac{1744}{4}.\] . This equals 440, so our answer is $\boxed{\textbf{(D)} 440}$ .
~Binderclips1

## Solution 8
We can use Newton Sums to solve this problem. We start by noticing that we can rewrite the equation as $\frac{x^3}{y^2} + \frac{y^3}{x^2} + x + y.$ Then, we know that $x + y = 4,$ so we have $\frac{x^3}{y^2} + \frac{y^3}{x^2} + 4.$ We can use the equation $x \cdot y = -2$ to write $x = \frac{-2}{y}$ and $y = \frac{-2}{x}.$ Next, we can plug in these values of $x$ and $y$ to get $\frac{x^3}{y^2} + \frac{y^3}{x^2} = \frac{x^5}{4} + \frac{y^5}{4},$ which is the same as \[\frac{x^3}{y^2} + \frac{y^3}{x^2} = \frac{x^5 + y^5}{4}.\] Then, we use Newton sums where $S_n$ is the elementary symmetric sum of the sequence and $P_n$ is the power sum ( $x^n + y^n$ ). Using this, we can make the following Newton sums: \[P_1 = S_1\] \[P_2 = P_1 S_1 - 2S_2\] \[P_3 = P_2 S_1 - P_1 S_2\] \[P_4 = P_3 S_1 - P_2 S_2\] \[P_5 = P_4 S_1 - P_3 S_2.\] We also know that $S_1$ is 4 because $x + y$ is four, and we know that $S_2$ is $-2$ because $x \cdot y$ is $-2$ as well. Then, we can plug in values! We have \[P_1 = S_1 = 4\] \[P_2 = P_1 S_1 - 2S_2 = 16 - (-4) = 20\] \[P_3 = P_2 S_1 - P_1 S_2 = 80 - (-8) = 88\] \[P_4 = P_3 S_1 - P_2 S_2 = 88 \cdot 4 - (-40) = 392\] \[P_5 = P_4 S_1 - P_3 S_2 = 392 \cdot 4 - (-2) \cdot 88 = 1744.\] We earlier noted that $\frac{x^3}{y^2} + \frac{y^3}{x^2} = \frac{x^5 + y^5}{4},$ so we have that this equals $\frac{1744}{4},$ or $436.$ Then, plugging this back into the original equation, this is $436 + 4$ or $440,$ so our answer is $\boxed{\textbf{(D)}\ 440}.$
~Coolpeep

## Solution 9
As in the first solution, we get the expression to be $\frac{x^3+y^3}{x^2} + \frac{x^3+y^3}{y^2}.$
Then, since the numerators are the same, we can put the two fractions as a common denominator and multiply the numerator by $x^2y^2.$ This gets us $\frac{(x^2 + y^2)(x^3 + y^3)}{x^2y^2}.$
Now, since we know $x+y=4$ and $xy=-2,$ instead of solving for $x$ and $y,$ we will try to manipulate the above expression them into a manner that we can substitute the sum and product that we know. Also, another form of $x^3+y^3$ is $(x+y)(x^2-xy+y^2).$
Thus, we can convert the current expression to $\frac{(x^2 + y^2)(x+y)(x^2-xy+y^2)}{x^2y^2}.$
Doing some algebraic multiplications, we get $\frac{((x+y)^2 - 2xy)(x+y)((x+y)^2 - 3xy)}{(xy)^2}.$
Since we know $x+y=4$ and $xy=-2,$ we have $\frac{(16-(-4))(4)(16-(-6))}{4} = \frac{20 \cdot 4 \cdot 22}{4} = 20 \cdot 22 = 440.$
Therefore the answer is $\boxed{\textbf{(D)} 440}.$
~mathboy282

## Solution 10 (Algebra Bash)
We give all of the terms in this expression a common denominator. $x + \frac{x^3}{y^2} + \frac{y^3}{x^2} + y = \frac{x^3y^2 + x^5 + y^5 + x^2y^3}{x^2y^2}$ . We can find $x^2y^2 = (xy)^2 = (-2)^2 = 4$ and we can find $x^3y^2 + x^2y^3 = x^2y^2(x + y) = 16$ . Our expression $\frac{xy^2 + x^5 + y^5 + x^2y}{x^2y^2}$ is now $\frac{16 + x^5 + y^5}{4}$ . Now all we need to find is $x^5 + y^5$ . Using the binomial theorem, $(x + y)^5 = x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5 = 4^5 = 1024$ . The extra terms that we don't need is $5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 = 5xy(x^3 + y^3) + 10x^2y^2(x + y) = -10(x^3 + y^3) + 160$ . What's $x^3 + y^3$ ? We use the same method. Using the binomial theorem, $(x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3 = x^3 + y^3 + 3xy(x + y) = x^3 + y^3 - 24 = 4^3 = 64$ . Now we know that $x^3 + y^3 = 64 + 24 = 88$ , and plugging that into $-10(x^3 + y^3) + 160$ gives $-10(88) + 160 = -880 + 160 = -720$ . Now we see that those extra terms have a sum of $-720$ . Thus $(x + y)^5 = x^5 + y^5 - 720 = 1024$ so $x^5 + y^5 = 1024 + 720 = 1744$ . Remember our goal: we want to find $\frac{-8 + x^5 + y^5}{4}$ . Using $x^5 + y^5 = 1744$ , $\frac{16 + x^5 + y^5}{4} = \frac{16 + 1744}{4} = \frac{1760}{4} = \boxed{\textbf{(D)}\ 440}$ .
~ Yrock

## Solution 11
Since we know $x+y=4$ , we can simplify to $4 + \frac{x^3}{y^2} + \frac{y^3}{x^2}$ . Then, when you add the fractions, you get $\frac{x^5 + y^5}{x^2y^2} = \frac{x^5 + y^5}{4}$ . To find $x^5 + y^5$ , we expand $(x+y)^5 = 4^5$ and then simplify. $x^5+y^5+5x^4y+5xy^4+10x^3y^2+10x^2y^3 = 1024$ . We can use the fact that $xy = -2$ to simplify to $x^5 + y^5-10x^3 - 10y^3 + 40x + 40y = 1024$ . We can factor to get $x^5 + y^5 -10(x^3 + y^3) +40(x+y)$ . To find $x^3 + y^3$ , we simplify $(x+y)^3 = 4^3$ . $x^3+y^3+3x^2y+3y^2x = 64$ . We can use the same process as we did before and get $x^3 + y^3 -6(x+y) = 64$ (using the fact that $xy = -2$ ). Therefore, $x^3 + y^3 = 88$ . Now, plugging it back in to our other expansion, we get $x^5 + y^5 + 160 - 880 = 1024$ . $x^5 +y^5 = 1744$ . Now to get the final answer, all we need to do is to plug it back into the original equation and get $\frac{1744}{4} + 4 = \boxed{\textbf{(D)}\ 440}$ .
~idk12345678

## Solution 12
We have \( x+y = 4 \) and \( xy = -2 \). We solve for \( x \) to get either \( 2 + \sqrt{6} \) or \( 2 - \sqrt{6} \), and WLOG, we say \( x = 2+\sqrt{6} \) and \( y = 2 - \sqrt{6} \). \( \sqrt{6} \) is about 2.44, We then substitute \( \sqrt{6} = 2.44 \) for \( x \) and \( y \), yielding \( x = 4.44 \) and \( y = -0.44 \). We now have \( x+ \frac{x^3}{y^2} + \frac{y^3}{x^2} + y \). \( x+y = 4 \), so we now have \( 4 + \frac{x^3}{y^2} + \frac{y^3}{x^2} \). Substituting the respective values of \( x \) and \( y \) yields 4 + 456 + a negative number, and we get \(460 - n\), where \(n\) is a positive number. We look at our answer choices and see that \(460-n\) lies between $\boxed{\textbf{(D)}\ 440}$ and $\boxed{\textbf{(E)}\ 480}$ , but because we have a negative number, $\boxed{\textbf{(E)}\ 480}$ is not possible. So our answer is $\boxed{\textbf{(D)}\ 440}$ , and we're done.
(Note from Pinotation: Not the most ideal solution, but it works).
~Pinotation

## Video Solutions

## Video Solution 1
https://www.youtube.com/watch?v=x4cF3o3Fzj8&t=376s
~Education, The Study of Everything

## Video Solution 2
https://youtu.be/PNkRlUKWCzg

## Video Solution 3 (q.13 idk why this is here)
https://www.youtube.com/watch?v=jlRmDrL_jmk ~Mathematical Dexterity (Don't Worry, Be Hoppy!)

## Video Solution 4
https://youtu.be/ZGwAasE32Y4?t=457
~IceMatrix

## Video Solution 5
https://youtu.be/XEtzvxfFEJk
~savannahsolver

## Video Solution 6
https://youtu.be/ba6w1OhXqOQ?t=3551
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .