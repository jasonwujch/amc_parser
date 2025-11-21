# 2024 AMC 8 Problem 22

## Problem

A roll of tape is $4$ inches in diameter and is wrapped around a ring that is $2$ inches in diameter. A cross section of the tape is shown in the figure below. The tape is $0.015$ inches thick. If the tape is completely unrolled, approximately how long would it be? Round your answer to the nearest $100$ inches.

[asy] /* AMC8 P22 2024, revised by Teacher David */ size(150); pair o = (0,0); real r1 = 1; real r2 = 2; filldraw(circle(o, r2), mediumgray, linewidth(1pt)); filldraw(circle(o, r1), white, linewidth(1pt)); draw((-2,-2.6)--(-2,-2.4)); draw((2,-2.6)--(2,-2.4)); draw((-2,-2.5)--(2,-2.5), L=Label("4 in.")); draw((-1,0)--(1,0), L=Label("2 in.", align=(0,1)), arrow=Arrows()); draw((2,0)--(2,-1.3), linewidth(1pt)); [/asy]

$\textbf{(A) } 300\qquad\textbf{(B) } 600\qquad\textbf{(C) } 1200\qquad\textbf{(D) } 1500\qquad\textbf{(E) } 1800$

## Solution 1
The roll of tape is $1/0.015=66$ layers thick. In order to find the total length, we have to find the average of each concentric circle and multiply it by $66$ . Since the diameter of the small circle is $2$ inches and the diameter of the large one is $4$ inches, the "middle value" (or mean) is $3$ . Therefore, the average circumference is $3\pi$ . Multiplying $3\pi \cdot 66$ gives approximately $(B) \boxed{600}$ . - Ilovemath3141592653589 The actual answer is around 628, but 628 is closer to 600 than 1200. - 1087780lakewashington200 Seojoon Oh, Samantha Smith Elementary School

## Solution 2
There are about $\dfrac{1}{0.015}=\dfrac{200}{3}$ "full circles" of tape, and with average circumference of $\dfrac{4+2}{2}\pi=3\pi.$ $\dfrac{200}{3} \cdot 3\pi=200\pi,$ which means the answer is $\boxed{600}$ .

## Solution 3
We can figure out the length of the tape by considering the side of the tape as a really thin rectangle that has a width of $0.015$ inches. The side of the tape is wrapped into an annulus(The shaded region between 2 circles with the same center), meaning the area of the shaded region is equal to the area of the really thin rectangle.
The area of the shaded region is $\pi(\frac{4}{2})^2 -\pi(\frac{2}{2})^2 = 3\pi$ , and we divide that by $0.015$ to get $200\pi$ . Approximating $\pi$ to be 3, we get the final answer to be $200 \cdot 3 = \textbf {(B) } 600$ .

## Solution 3 (kind of different?, but fun!)
The volume of the tape is always the same, but we can either calculate it when the tape is unrolled as a really long, thin rectangular prism, or we can calculate it as a cylinder with a hole cut out of it. When we calculate it as a long rectangular prism, we can say that the length is $X$ (this is what the problem wants!) and the width is $Y$ . Then, the volume is, of course, $0.015 \cdot X \cdot Y.$ Now, notice that the "width" of our rectangular prism is also the "height" of our cylinder with a hole cut out of it. Then, we can calculate the volume as base times height, or in this case, $3\pi \cdot Y.$ Now, since the volume always stays the same, we know that $3\pi \cdot Y = 0.015 \cdot X \cdot Y.$ Cancelling the $Y$ 's give us an equation for $X$ , and if we approximate $\pi$ as $3$ , then $X = \boxed {600}$ .

## Solution 4
If you cannot notice that the average diameter is $3$ , you can still solve this problem by the following method.
The same with solution 1, we have $\frac{1000}{0.015}$ layers of tape. If we consider every layers with the diameter $2$ , the length should be $\frac{1000}{0.015}2\pi\approx 400$ . If the diameter is seem as $4$ , the length should be $800$ . So, the length is between $400$ and $800$ , the only possible answer is $\boxed{600}$ .

## Video Solution 1 by Math-X (First understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=5YWwuZ_961azySZ-&t=6686
~Math-X

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/cJUWOQ-tSnE
~mr_mathman

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=MFF7Oc2wqpOhm2UU&t=3250 ~hsnacademy

## Video solution
https://youtu.be/NTJM_U-GhlM
Please like and sub

## Video Solution by Power Solve
https://www.youtube.com/watch?v=mGsl2YZWJVU

## Video Solution 2 by OmegaLearn.org
https://youtu.be/k1yAO0pZw-c

## Video Solution (Arithmetic Series)3 by SpreadTheMathlove Using
https://www.youtube.com/watch?v=kv_id-MgtgY

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=uAHP_LPUcwQ
~NiuniuMaths

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=bldjKBbhvkE

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=2679

## Video Solution by Dr. David
https://youtu.be/vnG8JYpuaJM

## Video Solution by WhyMath
https://youtu.be/k2FNc1sf-sE

## Official Video Solution (Real-world visualization method- 2 minutes!)
https://www.youtube.com/watch?v=UL_xlVUKcw8&t=7s ~TheMathGeek

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also