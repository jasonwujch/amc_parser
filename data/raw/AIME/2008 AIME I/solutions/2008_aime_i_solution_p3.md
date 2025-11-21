# 2008 AIME I Problem 3

## Problem

Ed and Sue bike at equal and constant rates. Similarly, they jog at equal and constant rates, and they swim at equal and constant rates. Ed covers $74$ kilometers after biking for $2$ hours, jogging for $3$ hours, and swimming for $4$ hours, while Sue covers $91$ kilometers after jogging for $2$ hours, swimming for $3$ hours, and biking for $4$ hours. Their biking, jogging, and swimming rates are all whole numbers of kilometers per hour. Find the sum of the squares of Ed's biking, jogging, and swimming rates.

## Solution 1
Let the biking rate be $b$ , swimming rate be $s$ , jogging rate be $j$ , all in km/h.
We have $2b + 3j + 4s = 74,2j + 3s + 4b = 91$ . Subtracting the second from twice the first gives $4j + 5s = 57$ . Mod 4, we need $s\equiv1\pmod{4}$ . Thus, $(j,s) = (13,1),(8,5),(3,9)$ .
$(13,1)$ and $(3,9)$ give non-integral $b$ , but $(8,5)$ gives $b = 15$ . Thus, our answer is $15^{2} + 8^{2} + 5^{2} = \boxed{314}$ .
Note : You can really quickly take the first equation $2b + 3j + 4s = 74$ mod 2, which will give $j \equiv 0 \pmod{2}$ . The only one of the ordered pairs that has an even j is $(8,5)$ . ~ unhappyfarmer

## Solution 2
Let $b$ , $j$ , and $s$ be the biking, jogging, and swimming rates of the two people. Hence, $2b + 3j + 4s = 74$ and $4b + 2j + 3s = 91$ . Subtracting gives us that $2b - j - s = 17$ . Adding three times this to the first equation gives that $8b + s = 125\implies b\le 15$ . Adding four times the previous equation to the first given one gives us that $10b - j = 142\implies b > 14\implies b\ge 15$ . This gives us that $b = 15$ , and then $j = 8$ and $s = 5$ . Therefore, $b^2 + s^2 + j^2 = 225 + 64 + 25 = \boxed{314}$ .

## Solution 3
Creating two systems, we get $2x+3y+4z=74$ , and $2y+3z+4x=91$ . Subtracting the two expressions we get $y+z-2x=-17$ . Note that $-17$ is odd, so one of $x,y,z$ is odd. We see from our second expression that $z$ must be odd, because $91$ is also odd and $2y$ and $4x$ are odd. Thus, with this information, we can test cases quickly:
When readdressing the first equation, we see that if $2x+3y$ will be a multiple of $6$ , $4z \equiv 2 \pmod{6} = 5$ , we get that $x=15$ and $y=8$ , which works because of integer values. Therefore, $225+64+25=\boxed{314}.$

## Solution 4 (Logic)
Building on top of Solution 3, we can add $j+s-2b=17$ and $2b+3j+4s=74$ (sorry, I used different variables) to get $4j+5s=57$ . Logically speaking, most athletic people swim a lot faster than 1 km/h (0.62 mph), so we test out the next case that works, which is 5 km/h (3.1 mph). This seems much more logical, so we plug it into the equation to get $4j+25=57\implies j=8$ . This seems reasonable, as people usually jog at around 8 to 16 km/h. Plugging these values into $2b+3j+4s=74$ , we get $b=15$ . 15 km/h is a little slow (most people bike at 20 km/h), but is still reasonable. So, we get $5^2+8^2+15^2=\boxed{314}$ .
Note: Solving $4j+5s=57$ yields 3 solutions for $(j,s)$ : $(13,1),(8,5),(3,9)$ , and only $(8,5)$ gives us an integer $b$ value and we don't need the assumption, which is also false, since swimming at $5 km/h$ over $4$ hours is also pretty insane, so none of the swimming speeds make any sense.
These problems are copyrighted © by the Mathematical Association of America.