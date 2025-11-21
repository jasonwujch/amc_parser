# 2017 AIME II Problem 6

## Problem

Find the sum of all positive integers $n$ such that $\sqrt{n^2+85n+2017}$ is an integer.

## Solution 1
Manipulating the given expression, $\sqrt{n^2+85n+2017}=\frac{1}{2}\sqrt{4n^2+340n+8068}=\frac{1}{2}\sqrt{(2n+85)^2+843}$ . The expression under the radical must be an square number for the entire expression to be an integer, so $(2n+85)^2+843=s^2$ . Rearranging, $s^2-(2n+85)^2=843$ . By difference of squares, $(s-(2n+85))(s+(2n+85))=1\times843=3\times281$ . It is easy to check that those are all the factor pairs of 843. Considering each factor pair separately, $2n+85$ is found to be $421$ and $139$ . The two values of $n$ that satisfy one of the equations are $168$ and $27$ . Summing these together gives us the answer ; $168+27=\boxed{195}$ .

## Solution 2
Clearly, the result when $n$ is plugged into the given expression is larger than $n$ itself. Let $x$ be the positive difference between that result and $n$ , so that $\sqrt{n^2+85n+2017}=n+x$ . Squaring both sides and canceling the $n^2$ terms gives $85n+2017=2xn+x^2$ . Combining like terms, $(85-2x)n=x^2-2017$ , so
\[n=\frac{x^2-2017}{85-2x}.\]
Since $n$ is positive, there are two cases, which are simple (luckily). Remembering that $x$ is a positive integer, then $x^2-2017$ and $85-2x$ are either both positive or both negative. The smallest value for which $x^2>2017$ is 45, which makes the denominator, and the entire expression, negative. Evaluating the other case where numerator and denominator are both negative, then we have that $x<45$ (from the numerator) and $85-2x<0$ , which means $x>42$ . This only gives two solutions, $x=43, 44$ . Plugging these into the expression for $n$ , we find that they result in 27 and 168, which both satisfy the initial question. Therefore, the answer is $168+27=\boxed{195}$ .

## Solution 3 (Abuse the discriminant)
Let the integer given by the square root be represented by $x$ . Then $0 = n^2 + 85n + 2017 - x^2$ . For this to have rational solutions for $n$ (checking whether they are integers is done later), the discriminant of this quadratic must be a perfect square. (This can be easily shown using the quadratic formula.)
Thus, $b^2 - 4ac = 7225 + 4x^2 - 8068 = y^2$ for some integer $y$ . Then $4x^2 - 843 = y^2$ . Rearranging this equation yields that $843 = (2x+y)(2x-y)$ . Noticing that there are 2 factor pairs of $843$ , namely, $1*843$ and $3*281$ , there are 2 systems to solve for $x$ and $y$ that create rational $n$ . These yield solutions $(x,y)$ of $(211, 421)$ and $(71, 139)$ .
The solution to the initial quadratic in $n$ must then be $\frac{-85 \pm \sqrt{85^2 - 4(2017 - x^2)}}{2}$ . Noticing that for each value of $x$ that has rational solutions for $n$ , the corresponding value of the square root of the discriminant is $y$ , the formula can be rewritten as $n = \frac{-85 \pm y}{2}$ . One solution is $\frac{421 - 85}{2} = 168$ and the other solution is $\frac{139 - 85}{2} = 27$ . Thus the answer is $168 + 27 = \boxed{195}$ as both rational solutions are integers.

## Solution 4 (Squeezing/Sandwich method)
Notice that $(n+42)^2= n^2+84n+1764$ . Also note that $(n+45)^2= n^2+90n+2025$ . Thus, \[(n+42)^2< n^2+85n+2017<(n+45)^2\] where $n^2+85n+2017$ is a perfect square. Hence, \[n^2+85n+2017= (n+43)^2\] or \[n^2+85n+2017= (n+44)^2.\] Solving the two equations yields the two solutions $n= 168, 27$ . Therefore, our answer is $\boxed{195}$ .

## Solution 5 (Using factors)
Let the expression be equal to $a$ . This expression can be factored into $\sqrt{(n+44)^2-3n+81}$ . Then square both sides, and the expression becomes $(n+44)^2-3n+81=a^2$ . We have a difference of two squares. Rearranging, we have $(n+44+a)(n+44-a)=3(n-27)$ . By inspection, the only possible values for $(n+44-a)$ are 0 and 1. When $(n+44-a)=0$ , we must have $n-27=0$ . Therefore, $27$ is a solution. When we have $(n+44-a)=1$ , so $n=a-43$ . Plugging this back to $(n+44+a)=3(n-27)$ (since $(n+44-a)=1$ ), we find that $a=211 \implies n=168$ . Thus, the answer is $27+168= \boxed{195}$ .
-RootThreeOverTwo

## Solution 6
Ignore the square root for now. This expression can be factored into $(n+44)^2-3n+81$ . Just by inspection, when $n=27$ , the expression becomes $71^2$ , so $27$ is a solution. Proceed as Solution 5 to find the other solution(s).

## Solution 7 (alternative factoring)
More intuitive, but a little bit slower considering the decimals.
Label the entire given expression as $k^2$ .
Instinctively we can do a crude completion of the square, resulting in $k^2$ = $(n+42.5)^2+210.75$ Rearrange the equation to get a difference of squares.
$k^2-(n+42.5)^2 = 210.75$
$(k+n+42.5)(k-n-42.5) = 210.75$
Factor $21,075$ to get $3^1$ , $5^2$ , and $281^1$
Now the two factors given are either divided by 10 each or one being divided by 100. Let's start with the former case.
If you try $281*3/10$ and $5*5/10$ , you quickly realize that $n$ becomes negative. Naturally, you will realize you want the number's difference to be larger. Try $281*5/10$ and $3*5/10$ . This gives an answer of $27$ for $x$ . The next largest possibility also works, giving an $n$ of $168$ . As you rise, some numbers don't work because it results in an n that is not an integer, as in the example of $\frac{281*5*5}{10}$ and $\frac{3}{10}$ .
Now if you continue on with the next case, where one factor is divided by $100$ , very swiftly will you realize most don't work simply because the difference is too small, or it doesn't give an integer. It helps a lot when you realize that the decimal does not end in a $5$ , the answer will not be an integer. After a few short tests, we get $168+27=\boxed{195}$ .
-jackshi2006 - minor latex edits by jske25

## Video Solution
https://youtu.be/Z23Yz05eblY
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .