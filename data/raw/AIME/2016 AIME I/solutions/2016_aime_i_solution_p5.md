# 2016 AIME I Problem 5

## Problem

Anh read a book. On the first day she read $n$ pages in $t$ minutes, where $n$ and $t$ are positive integers. On the second day Anh read $n + 1$ pages in $t + 1$ minutes. Each day thereafter Anh read one more page than she read on the previous day, and it took her one more minute than on the previous day until she completely read the $374$ page book. It took her a total of $319$ minutes to read the book. Find $n + t$ .

## Solution 1
Let $d$ be the number of days Anh reads for. Because the difference between the number of pages and minutes Anh reads for each day stays constant and is an integer, $d$ must be a factor of the total difference, which is $374-319=55$ . Also note that the number of pages Anh reads is $dn+\frac{d(d-1)}{2}$ . Similarly, the number of minutes she reads for is $dt+\frac{d(d-1)}{2}$ . When $d$ is odd (which it must be), both of these numbers are multiples of $d$ . Therefore, $d$ must be a factor of $55$ , $319$ , and $374$ . The only such numbers are $1$ and $11$ . We know that Anh reads for at least $2$ days. Therefore, $d=11$ .
Using this, we find that she reads $55$ "additional" pages and $55$ "additional" minutes. Therefore, $n=\frac{374-55}{11}=29$ , while $t=\frac{319-55}{11}=24$ . The answer is therefore $29+24=\fbox{053}$ .

## Solution 2
We could see that both $374$ and $319$ are divisible by $11$ in the outset, and that $34$ and $29$ , the quotients, are relatively prime. Both are the $average$ number of minutes across the $11$ days, so we need to subtract $\left \lfloor{\frac{11}{2}}\right \rfloor=5$ from each to get $(n,t)=(29,24)$ and $29+24=\boxed{053}$ .

## Solution 3
If we let $k$ be equal to the number of days it took to read the book, the sum of $n$ through $n+k$ is equal to $(2n+k)(k+1)=748$ Similarly, $(2t+k)(k+1)=638$ We know that both factors must be integers and we see that the only common multiple of $748$ and $638$ not equal to $1$ that will get us positive integer solutions for $n$ and $t$ is $11$ . We set $k+1=11$ so $k=10$ . We then solve for $n$ and $t$ in their respective equations, getting $2n+10=68$ . $n=29$ We also get $2t+10=58$ . $t=24$ . Our final answer is $29+24=\boxed{053}$

## Solution 4
Notice $374=34\cdot 11$ and $319=29\cdot 11$ . Also, note the sum of an arithmetic series is $\frac{2n+k}{2} \cdot b$ , where $n$ is our first term, $n+k$ is our final term, and $b$ is the number of terms. Since we know both sequences of $n$ and $t$ have the same length, and since $11$ is prime and shared by both $319$ and $374$ , we deduce that $b=11$ . Thus from here we know $2n+k=68$ and $2t+k=58$ by using our other factors $34$ and $29$ . Finally, we add the two systems up and we get $2t+2k+2n=126$ . But, notice that $k=b-1$ , since the first term has $k=0$ , and our last term has $k=b-1$ . Plugging this back into our equation we get $2n+2t=106 \implies n+t=\boxed{053}$

## Solution 5
We list two equations: \begin{align*} n+(n+1)+...+(n+k)&=374\\ t+(t+1)+...+(t+k)&=319. \end{align*} Subtracting the two, we get: \[(n-t)(k+1)=374-319=55.\] Manipulating the first and second equation, we get: \begin{align*} n(k+1)+\frac{k(k+1)}{2}&=374 \\ t(k+1)+\frac{k(k+1)}{2}&=319. \end{align*} We factor out the common factor $k+1$ : \begin{align*} (k+1)\left(n+\frac{k}{2}\right)&=374 \\ (k+1)\left(t+\frac{k}{2}\right)&=319. \end{align*} Note that $374$ and $319$ have a GCD of $11,$ now combining this with our equation that $(n-t)(k+1)=55,$ we see that $k+1$ has to equal $11.$ Thus, we get: \[(n,t)=(29,24) \Rightarrow n+t=29+24=\boxed{053}.\] Note: We see that because n-t=5, it becomes impossible for n+k/2 and t+k/2 to both be multiples of 11. Thus, this satisfies our condition. Thus k+1 must be 11 to satisfy the common factor 11 constraint. mathboy282
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .