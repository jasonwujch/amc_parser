# 2002 AIME II Problem 8

## Problem

Find the least positive integer $k$ for which the equation $\left\lfloor\frac{2002}{n}\right\rfloor=k$ has no integer solutions for $n$ . (The notation $\lfloor x\rfloor$ means the greatest integer less than or equal to $x$ .)

## Solutions

## Solution 1
Note that if $\frac{2002}n - \frac{2002}{n+1}\leq 1$ , then either $\left\lfloor\frac{2002}{n}\right\rfloor=\left\lfloor\frac{2002}{n+1}\right\rfloor$ , or $\left\lfloor\frac{2002}{n}\right\rfloor=\left\lfloor\frac{2002}{n+1}\right\rfloor+1$ . Either way, we won't skip any natural numbers.
The greatest $n$ such that $\frac{2002}n - \frac{2002}{n+1} > 1$ is $n=44$ . (The inequality simplifies to $n(n+1)<2002$ , which is easy to solve by trial, as the solution is obviously $\simeq \sqrt{2002}$ .)
We can now compute: \[\left\lfloor\frac{2002}{45}\right\rfloor=44\] \[\left\lfloor\frac{2002}{44}\right\rfloor=45\] \[\left\lfloor\frac{2002}{43}\right\rfloor=46\] \[\left\lfloor\frac{2002}{42}\right\rfloor=47\] \[\left\lfloor\frac{2002}{41}\right\rfloor=48\] \[\left\lfloor\frac{2002}{40}\right\rfloor=50\]
From the observation above (and the fact that $\left\lfloor\frac{2002}{2002}\right\rfloor=1$ ) we know that all integers between $1$ and $44$ will be achieved for some values of $n$ . Similarly, for $n<40$ we obviously have $\left\lfloor\frac{2002}{n}\right\rfloor > 50$ .
Hence the least positive integer $k$ for which the equation $\left\lfloor\frac{2002}{n}\right\rfloor=k$ has no integer solutions for $n$ is $\boxed{049}$ .
### Note
After getting that $\left\lfloor\frac{2002}{45}\right\rfloor=44$ , for ease of computation above, we can use the fact that $(40+k)(49-k)$ varies solely based on $k^2$ and checking these gives us that the pattern fails at $k=0$ giving us $\boxed{049}$ as the answer.
~Dhillonr25

## Solution 2
Rewriting the given information and simplifying it a bit, we have \begin{align*} k \le \frac{2002}{n} < k+1 &\implies \frac{1}{k} \ge \frac{n}{2002} > \frac{1}{k+1}. \\ &\implies \frac{2002}{k} \ge n > \frac{2002}{k+1}. \end{align*}
Now note that in order for there to be no integer solutions to $n,$ we must have $\left\lfloor \frac{2002}{k} \right\rfloor = \left\lfloor \frac{2002}{k+1} \right\rfloor.$ We seek the smallest such $k.$ A bit of experimentation yields that $k=49$ is the smallest solution, as for $k=49,$ it is true that $\left\lfloor \frac{2002}{49} \right\rfloor = \left\lfloor \frac{2002}{50} \right\rfloor = 40.$ Furthermore, $k=49$ is the smallest such case. (If unsure, we could check if the result holds for $k=48,$ and as it turns out, it doesn't.) Therefore, the answer is $\boxed{049}.$

## Solution 3
In this solution we use inductive reasoning and a lot of trial and error. Depending on how accurately you can estimate, the solution will come quicker or slower.
Using values of $k$ as $1, 2, 3, 4,$ and $5,$ we can find the corresponding values of $n$ relatively easily. For $k = 1$ , $n$ is in the range $[2002-1002]$ ; for $k = 2$ , $n$ is the the range $[1001-668]$ , etc: $3, [667,501]; 4, [500-401]; 5, [400-334]$ . For any positive integer $k, n$ is in a range of $\left\lfloor \frac{2002}{k} \right\rfloor -\left\lceil \frac{2002}{k+1} \right\rceil$ .
Now we try testing $k = 1002$ to get a better understanding of what our solution will look like. Obviously, there will be no solution for $n$ , but we are more interested in how the range will compute to. Using the formula we got above, the range will be $1-2$ . Testing any integer $k$ from $1002-2000$ will result in the same range. Also, notice that each and every one of them have no solution for $n$ . Testing $1001$ gives a range of $2-2$ , and $2002$ gives $1-1$ . They each have a solution for $n$ , and their range is only one value. Therefore, we can assume with relative safety that the integer $k$ we want is the lowest integer that follows this equation
\[\left\lfloor\frac{2002}{k}\right\rfloor + 1 = \left\lceil \frac{2002}{k+1}\right\rceil\]
Now we can easily guess and check starting from $k = 1$ . After a few tests it's not difficult to estimate a few jumps, and it took me only a few minutes to realize the answer was somewhere in the forties (You could also use the fact that $45^2=2025$ ). Then it's just a matter of checking them until we get $\boxed{049}$ . Alternatively, you could use the equation above and proceed with one of the other two solutions listed.
-jackshi2006
Edited and $\LaTeX$ ed by PhunsukhWangdu

## Solution 4
Here is an intuitive way to approximate the answer is around $45$ : For the function $f(n)=\frac{2002}{n}$ its derivative is $-\frac{2002}{n^2}$ , which should be close to $-1$ because we need to find the smallest skipped integer. The rest of the steps are the same as Solution 1.
-maxamc
These problems are copyrighted © by the Mathematical Association of America.