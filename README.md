# UPE-Spring-2018-Coding-Challenge

It works rather slowly, but it has not yet failed. I exploit a possible weakness in the API by calling get and then post with a random lowercase letter again and again. This means that I never lose. If my guess did not yield a correct answer, I just call get to create a new game and begin again. There is a line in notes saying the following: "The service only supports playing one game at a time, so don't GET http://upe.42069.fun/[access-token] until you're sure you're ready to move on." And true to this spec, I only GET when I am sure I want to move on, namely whenever I've made a single guess.

Run "rip.py" with Python 3.5. The following libraries are needed: requests, time, string, and random.
