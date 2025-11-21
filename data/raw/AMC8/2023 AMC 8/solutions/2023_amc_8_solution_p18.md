# 2023 AMC 8 Problem 18

## Problem

Greta Grasshopper sits on a long line of lily pads in a pond. From any lily pad, Greta can jump $5$ pads to the right or $3$ pads to the left. What is the fewest number of jumps Greta must make to reach the lily pad located $2023$ pads to the right of her starting position?

$\textbf{(A) } 405 \qquad \textbf{(B) } 407 \qquad \textbf{(C) } 409 \qquad \textbf{(D) } 411 \qquad \textbf{(E) } 413$

## Solution 1
We have $2$ directions going $5$ right or $3$ left. We can assign a variable to each of these directions. We can call going right $1$ direction $\text{X}$ and we can call going $1$ left $\text{Y}$ . We can build an equation of $5\text{X}-3\text{Y}=2023$ , where we have to limit the number of moves we do. We can do this by making more of our moves the $5$ move turn than the $3$ move turn. The first obvious step is to go some amount of moves in the right direction then subtract off in the left direction to land on $2023$ . The least amount of $3$ ’s added to $2023$ to make a multiple of $5$ is $4$ as $2023 + 4(3) = 2035$ . So now, we have solved the problem as we just go $\frac{2035}{5} = 407$ hops right, and just do 4 more hops left. Yielding $407 + 4 = \boxed{\textbf{(D)}\ 411}$ as our answer.
~apex304, SohumUttamchandani, wuwang2002, TaeKim, Cxrupptedpat

## Solution 2
Notice that $2023 \equiv 3\pmod{5}$ , and jumping to the left increases the value of Greta's position $\pmod{5}$ by $2$ . Therefore, the number of jumps to the left must be $4 \pmod{5}$ . As the number of jumps to the left increases, so does the number of jumps to the right, we must minimize both, which occurs when we jump $4$ to the left and $407$ to the right. The answer is $\boxed{\textbf{(D)}\ 411}$ .
~TRALALA

## Solution 3
$5y - 2023$ must be divisible by 3. The smallest value of $y$ that will achieve this is $407$ , which lands it at $2035$ . After that, it takes $4$ jumps back, making a total of $\boxed{\textbf{(D)}\ 411}$ .
~e___

## Solution 3.1
Here is Solution 3 but worded differently: We can to go back $3x$ steps from $5y$ steps we took past $2023$ . The other way to say this is we go $3x$ steps from $2023$ to get to $5y$ . What is the least value of $3x$ ? We need $2023+3x$ to end in a $5$ or $0$ . The least value for $3x$ , which makes $2023+3x=2035$ , is $4$ . $\frac{2035}{5}=407$ . Therefore, $407+4=$ $\boxed{\textbf{(D)}\ 411}$ .

## Video Solution by STEM Station(Quick and Easy to Understand)
https://youtu.be/WYR3zWkWCV8

## Video Solution by Pi Academy (Fast and Easy)
https://youtu.be/qJVIN4W2WsQ?si=4xJ8dgkJBbaOOG-M
~ Pi Academy

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=1859 ~hsnacademy

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=E5Vs_ZXCVQzSH7Pl&t=3827 ~Math-X

## Video Solution
https://youtu.be/d640itCB9_Y
~Education, the Study of Everything

## Animated Video Solution
https://youtu.be/zmRiG52jxpg
~Star League ( https://starleague.us )

## Video Solution by OmegaLearn (Restrictive Counting)
https://youtu.be/gIjhiw1CUgY

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=3673

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=2295

## Video Solution by harungurcan
https://www.youtube.com/watch?v=Ki4tPSGAapU&t=0s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/Qo5H3RVDSbY

## Video Solution by WhyMath
https://youtu.be/OpnNQ4zBA-4
### See Also