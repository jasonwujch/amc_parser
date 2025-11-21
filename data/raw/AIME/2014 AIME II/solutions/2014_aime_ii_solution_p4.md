# 2014 AIME II Problem 4

## Problem

The repeating decimals $0.abab\overline{ab}$ and $0.abcabc\overline{abc}$ satisfy

\[0.abab\overline{ab}+0.abcabc\overline{abc}=\frac{33}{37},\]

where $a$ , $b$ , and $c$ are (not necessarily distinct) digits. Find the three digit number $abc$ .

## Solution 1
Notice repeating decimals can be written as the following:
$0.\overline{ab}=\frac{10a+b}{99}$
$0.\overline{abc}=\frac{100a+10b+c}{999}$
where a,b,c are the digits. Now we plug this back into the original fraction:
$\frac{10a+b}{99}+\frac{100a+10b+c}{999}=\frac{33}{37}$
Multiply both sides by $999*99.$ This helps simplify the right side as well because $999=111*9=37*3*9$ :
$9990a+999b+9900a+990b+99c=33/37*37*3*9*99=33*3*9*99$
Dividing both sides by $9$ and simplifying gives:
$2210a+221b+11c=99^2=9801$
At this point, seeing the $221$ factor common to both a and b is crucial to simplify. This is because taking $mod 221$ to both sides results in:
$2210a+221b+11c \equiv 9801 \mod 221 \iff 11c \equiv 77 \mod 221$
Notice that we arrived to the result $9801 \equiv 77 \mod 221$ by simply dividing $9801$ by $221$ and seeing $9801=44*221+77.$ Okay, now it's pretty clear to divide both sides by $11$ in the modular equation but we have to worry about $221$ being multiple of $11.$ Well, $220$ is a multiple of $11$ so clearly, $221$ couldn't be. Also, $221=13*17.$ Now finally we simplify and get:
$c \equiv 7 \mod 221$
But we know $c$ is between $0$ and $9$ because it is a digit, so $c$ must be $7.$ Now it is straightforward from here to find $a$ and $b$ :
$2210a+221b+11(7)=9801 \iff 221(10a+b)=9724 \iff 10a+b=44$
and since a and b are both between $0$ and $9$ , we have $a=b=4$ . Finally we have the $3$ digit integer $\boxed{447}$

## Solution 2
Note that $\frac{33}{37}=\frac{891}{999} = 0.\overline{891}$ . Also note that the period of $0.abab\overline{ab}+0.abcabc\overline{abc}$ is at most $6$ . Therefore, we only need to worry about the sum $0.ababab+ 0.abcabc$ . Adding the two, we get \[\begin{array}{ccccccc}&a&b&a&b&a&b\\ +&a&b&c&a&b&c\\ \hline &8&9&1&8&9&1\end{array}\] From this, we can see that $a=4$ , $b=4$ , and $c=7$ , so our desired answer is $\boxed{447}$

## Solution 3
Noting as above that $0.\overline{ab} = \frac{10a + b}{99}$ and $0.\overline{abc} = \frac{100a + 10b + c}{999}$ , let $u = 10a + b$ . Then \[\frac{u}{99} + \frac{10u + c}{999} = \frac{33}{37}\]
\[\frac{u}{11} + \frac{10u + c}{111} = \frac{9\cdot 33}{37}\]
\[\frac{221u + 11c}{11\cdot 111} = \frac{9\cdot 33}{37}\]
\[221u + 11c = \frac{9\cdot 33\cdot 11\cdot 111}{37}\]
\[221u + 11c = 9\cdot 33^2.\]
Solving for $c$ gives
\[c = 3\cdot 9\cdot 33 - \frac{221u}{11}\]
\[c = 891 - \frac{221u}{11}\]
Because $c$ must be integer, it follows that $u$ must be a multiple of $11$ (because $221$ clearly is not). Inspecting the equation, one finds that only $u = 44$ yields a digit $c, 7$ . Thus $abc = 10u + c = \boxed{447}.$

## Solution 4
We note as above that $0.\overline{ab} = \frac{10a + b}{99}$ and $0.\overline{abc} = \frac{100a + 10b + c}{999},$ so
\[\frac{10a + b}{99} + \frac{100a + 10b + c}{999} = \frac{33}{37} = \frac{891}{999}.\]
As $\frac{10a + b}{99}$ has a factor of $11$ in the denominator while the other two fractions don't, we need that $11$ to cancel, so $11$ divides $10a + b.$ It follows that $a = b,$ so $\frac{10a + b}{99} = \frac{11a}{99} = \frac{111a}{999},$ so
\[\frac{111a}{999} + \frac{110a+c}{999} = \frac{891}{999}.\]
Then $111a + 110a + c = 891,$ or $221a + c = 891.$ Thus $a = b = 4$ and $c = 7,$ so the three-digit integer $abc$ is $\boxed{447}.$

## Video Solution
https://youtu.be/7g5dztxGUrk
~savannahsolver
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .