## What have you done this week? // General?
I've mainly struggled with how to continue the game. I spent some time trying to figure out the flipping, transposing, merging etc. and couldn't really figure it out. Mostly tested out stuff in the one game file and couldn't get anything done and gave up for the day. Then later I found one [video](https://www.youtube.com/watch?v=0fOLkZJ-Q6I&ab_channel=MichaelSchrandt) that I heavily used to help me along the project and divided my game file into manager and play (future ui?). I couldn't find the exact rules on how much I can take help from the internet and how much I should figure out myself from pseudocode and such (Only the chatgpt one). Like I said I did heavily this week rely on the example, which hopefully is still fine as I did still write the code? I'd be interested to know if it really is okay? I need to fix/change some (move mainly) of the code next week anyway because of the pylint mistakes it set off (Which this week I just ignored in the .pylintrc file), but I'm once again working on this way too last minute to fix them this week. 

Especially with the expectiminimax I'm not sure I would've gotten anywhere alone with the pseudocode. Though even with the help of the video my algorithm is still broken and can't reach that high of a score. This I want to fix on my own next week rather than re-watching the video again. But for this I really feel I need to create some kind of different ui, because I find it very hard to follow the game on the command line.

I did also start the testing document, but as all my test are very temporary right now and I need to fix other parts of the code first and I couldn't really do much with it. Hopefully the tests are still enough.. I generally I think I tested everything I could with the current code I have (I chose to ignore the ai code I can't test without changing the ui first from the coverage)? 

## How has the project progressed?
- For the user the game works as it should
- A version of expectiminimax is somewhat working (Not sure what's exactly wrong)
    - On infinite loop because of there not being proper ui (without you'd have to keep pressing enter. tkinkter or pygame schould fix this next week!)
- Not very good tests currenty as a lot of the code is going to change and I can't really test the ai currently because it works on an infinite loop.

## What did you learn this week?
- I did spend time on trying to understand firstly the flipping/transpose, which I did kind of understand.
- I also understood the new move way better and will try to better divide it into parts next week.
- I think I understood expectiminimax quite well thanks to the example and think i'll be able to fix my current problems with the ai next week!
- A small thing but I never knew with range I could also define the steps as I do in the move part. I was very excited to learn that!

## What has been unclear or problematic? Please answer this question truthfully, as this is something the course assistant may be able to help with.
Well generally I was surprised to see this ""seuraavan viikon aikana olisi hyvä saada toteutettua expectiminimax, joka pelaa peliä automaattisesti." in the feedback and I think it generally scared me into relying so heavily on an example, as I felt I needed to have some working version this week done. This was simply a surprise because based on the week schedule I was expecting to "maybe" start on it this week and first get the game and ui done. But I think it worked out in the end? If I was allowed to rely this much on examples I found?

## What next?
Well if I'm allowed to continue with this and don't have to redo stuff without the example:
- Create UI to help see how to fix the expectiminimax!
    - Fix the algorithm.
- Generally clean the code
- Testing and testing document in a better and more final shape!!

## Time spent
9 hours
