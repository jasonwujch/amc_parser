# 2019 AMC 8 Problem 14

## Problem

Isabella has $6$ coupons that can be redeemed for free ice cream cones at Pete's Sweet Treats. In order to make the coupons last, she decides that she will redeem one every $10$ days until she has used them all. She knows that Pete's is closed on Sundays, but as she circles the $6$ dates on her calendar, she realizes that no circled date falls on a Sunday. On what day of the week does Isabella redeem her first coupon?

$\textbf{(A) }\text{Monday}\qquad\textbf{(B) }\text{Tuesday}\qquad\textbf{(C) }\text{Wednesday}\qquad\textbf{(D) }\text{Thursday}\qquad\textbf{(E) }\text{Friday}$

## Solution 1 ( Guess and Check! )
Let $\text{Day }1$ to $\text{Day\\ }2$ denote a day where one coupon is redeemed and the day when the second coupon is redeemed.
If she starts on a $\text{Monday}$ , she redeems her next coupon on $\text{Thursday}$ .
$\text{Thursday}$ to $\text{Sunday}$ .
Thus, $\textbf{(A)}\ \text{Monday}$ is incorrect.
If she starts on a $\text{Tuesday}$ , she redeems her next coupon on $\text{Friday}$ .
$\text{Friday}$ to $\text{Monday}$ .
$\text{Monday}$ to $\text{Thursday}$ .
$\text{Thursday}$ to $\text{Sunday}$ .
Thus $\textbf{(B)}\ \text{Tuesday}$ is incorrect.
If she starts on a $\text{Wednesday}$ , she redeems her next coupon on $\text{Saturday}$ .
$\text{Saturday}$ to $\text{Tuesday}$ .
$\text{Tuesday}$ to $\text{Friday}$ .
$\text{Friday}$ to $\text{Monday}$ .
$\text{Monday}$ to $\text{Thursday}$ .
And on $\text{Thursday}$ , she redeems her last coupon.
No Sunday occured; thus, $\boxed{\textbf{(C)}\ \text{Wednesday}}$ is correct.
Checking for the other options,
If she starts on a $\text{Thursday}$ , she redeems her next coupon on $\text{Sunday}$ .
Thus, $\textbf{(D)}\ \text{Thursday}$ is incorrect.
If she starts on a $\text{Friday}$ , she redeems her next coupon on $\text{Monday}$ .
$\text{Monday}$ to $\text{Thursday}$ .
$\text{Thursday}$ to $\text{Sunday}$ .
Checking for the other options gave us negative results; thus, the answer is $\boxed{\textbf{(C)}\ \text{Wednesday}}$ .
~KangarooPrecise and ( ??? )

## Solution 2
Let
Sunday $\equiv 0 \pmod{7}$
Monday $\equiv 1 \pmod{7}$
Tuesday $\equiv 2 \pmod{7}$
Wednesday $\equiv 3 \pmod{7}$
Thursday $\equiv 4 \pmod{7}$
Friday $\equiv 5 \pmod{7}$
Saturday $\equiv 6 \pmod{7}$
$10 \equiv 3 \pmod{7}$
$20 \equiv 6 \pmod{7}$
$30 \equiv 2 \pmod{7}$
$40 \equiv 5 \pmod{7}$
$50 \equiv 1 \pmod{7}$
$60 \equiv 4 \pmod{7}$
Which indicates if you start from a $x \equiv 3 \pmod{7}$ you will not get a $y \equiv 0 \pmod{7}$ .
Any other starting value may lead to a $y \equiv 0 \pmod{7}$ .
Which means our answer is $\boxed{\textbf{(C)\ Wednesday}}$ .
~phoenixfire

## Solution 3
Like Solution 2, let the days of the week be numbers $\pmod 7$ . $3$ and $7$ are coprime, so continuously adding $3$ to a number $\pmod 7$ will cycle through all numbers from $0$ to $6$ . If a string of 6 numbers in this cycle does not contain $0$ , then if you minus 3 from the first number of this cycle, it will always be $0$ . So, the answer is $\boxed{\textbf{(C) Wednesday}}$ .
~~SmileKat32

## Solution 4
Start counting on Sunday, to maximize the number of 10-day jumps before reaching Sunday again. Add the 10 ( $\equiv 3 \pmod 7$ ) days to reach the first coupon day on $\boxed{\textbf{(C)\ Wednesday}}$ .
~~ gorefeebuddie
Note: This only works when 7 and 3 are relatively prime. Otherwise, you’d prefer to start on a day whose distance from Sunday is relatively prime to the jump size.

## Solution 5
Let Sunday be Day 0, Monday be Day 1, Tuesday be Day 2, and so forth. We see that Sundays fall on Day $n$ , where n is a multiple of seven. If Isabella starts using her coupons on Monday (Day 1), she will fall on a Day that is a multiple of seven, a Sunday (her third coupon will be "used" on Day 21). Similarly, if she starts using her coupons on Tuesday (Day 2), Isabella will fall on a Day that is a multiple of seven (Day 42). Repeating this process, if she starts on Wednesday (Day 3), Isabella will first fall on a Day that is a multiple of seven, Day 63 (13, 23, 33, 43, 53 are not multiples of seven), but on her seventh coupon, of which she only has six. So, the answer is $\boxed{\textbf{(C)}\text{ Wednesday}}$ .

## Video Solution
https://youtu.be/gOZOCFNXMhE ~ The Learning Royal
### Video
Check the box below

## Solution 6
Associated video - https://www.youtube.com/watch?v=LktgMtgb_8E
Solution detailing how to solve the problem: https://www.youtube.com/watch?v=MOQj1zxH2gY&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=15

## Video Solution
https://youtu.be/8VQc6fbZMvg
~savannahsolver

## Video Solution
https://youtu.be/9NNJE3pkmVc
~Education, the Study of Everything

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1