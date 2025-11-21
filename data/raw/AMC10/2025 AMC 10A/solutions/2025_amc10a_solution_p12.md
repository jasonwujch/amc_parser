# 2025 AMC 10A Problem 12

## Problem

Carlos uses a $4$ -digit passcode to unlock his computer. In his passcode, exactly one digit is even, exactly one (possibly different) digit is prime, and no digit is $0$ . How many $4$ -digit passcodes satisfy these conditions?

$\textbf{(A) } 176 \qquad\textbf{(B) } 192 \qquad\textbf{(C) } 432 \qquad\textbf{(D) } 464 \qquad\textbf{(E) } 608$

## Solution 1: Casework
The only two digits that are neither prime nor even are $1$ and $9$ . We split this problem into cases based on the number of $2$ s. This is because $2$ is both a prime number and an even number.
Case 1: For this case, there are no $2$ s. There are $4$ choices for where the even digit goes, and $3$ choices for what the even digit is. There are then $3$ choices for where the prime digit goes, and $3$ choices for what the prime digit is. The last two spots have $2$ choices each, $1$ or $9$ . This gives a total of $4\cdot 3^3 \cdot 2^2 = 432$ options for this case.
Case 2: For this case, there is one $2$ . There are $4$ choices for where $2$ goes, and $2$ choices for the other three digits each. This case gives a total of $2^3\cdot 4 = 32$ options.
Hence, the answer is $432 + 32 = \boxed{\textbf{(D) }464}$ ~Tacos_are_yummy_1
~Tacos_are_yummy_1 (w editing chain, let's keep it going haha)
~iiiiiizh (minor edits)
~drekie (very minor edit--ain't no way someone thought 4x3x3x2x2=432 lmao)
~happyfish0922 (minor formatting edits)
~zoyashaikh (extremely minor edits)
~kfclover (minor LaTeX edits)
~aldzandrtc (removed dummy subjects to be specific)
~gvh300 (minor editing)
~minor $\LaTeX$ edits by i_am_not_suk_at_math (saharshdevaraju 14:27, 7 November 2025 (EST)saharshdevaraju)
~Ninekayx wsp
~Strickenox (added an exclamation point just to keep the chain going)
~SixthGradeBookWorm927 (Made the first sentence for each case complete)
~ Strickenox (wsp SixthGradeBookworm927 i see we are both editing this page right now)
~Sharp_logic (made first sentence complete)
~Harrg (very minor edits)
~ZDC0530 (minor LaTeX edit)
~HappyLion (extremely minor grammar mistake)
~Elliecorn (very extremely minor LaTeX edit)
~EZ123 (extremely minor formatting edit to make the solution more pleasing to the eye)
~Galactic_Saber (extremely minor formatting edit)
~lucassf12 (removed period at the end to keep the chain going)
~Ryxo (minor grammar improvements for better flow)
~AoPS_enjoyer (removed unnecessary parenthesis)
~piZZaZedpiZZa (removed space before the colon)
~Gask314 (fixed inconsistencies with punctuation and math mode)
~lprado (did literally nothing)
~EZ123 (another extremely minor formatting edit to make the solution more pleasing to the eye)
~Sakura_kitty (fixed a sentence to make it flow better)
~Gask314 (fixed punctuation to make the solution read more professionally)
~Ummmmmmmm (fixed major punctuation errors - added spaces after the periods)

## Solution 2: Cheese but fast
Let us count the cases where there is a $2$ anywhere in the lock. There are $4$ places to arrange the $2$ s, and the remaining digits can only be $1$ s and $9$ s (since they neither can be even nor prime). Thus, there will be $4\cdot2^3=32$ choices for there to exist one $2$ . We note that answer choice $\text{(D)}$ is $32$ greater than another answer choice (specifically, $\text{(C)}$ ) and is the only answer choice to have this property. Assuming that the pitfall of forgetting the case with a $2$ would be a separate answer choice on its own, we can justify that the answer is $\boxed{\text{(D) }464}$
~megaboy6679, who forgot the case with the $2$

## Video Solution
https://youtu.be/CCYoHk2Af34

## Chinese Video Solution
https://www.bilibili.com/video/BV1nYkUBVEFt/
~metrixgo

## Video Solution (Fast and Easy)
https://youtu.be/TOTJEltmpe0?si=pglACCfjzAHguvlt ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by Daily Dose of Math
https://youtu.be/5Fjos1vBt0A
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .