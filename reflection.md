# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, I was extremely confused because of all the bugs, and it was hard to properly play. The hints would be backward, so if I needed to go higher, it would tel me to go lower. The text box says "press enter", but pressing the key doesnt input the answer. The guesses also start from 0 and it doesnt let me reset and play again. The hints also didn't show until I clicked the "Submit Button" twice. It took me a couple tries of the game to understand where the code was bugging out, and decipher that what the game is supposed to do.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input        | Expected Behavior      | Actual Behavior              | Console Output / Error  |
|--------------|------------------------|------------------------------|-------------------------|
| Guess of 1   | Hint: Go higher        | Hint: Go lower               | None                    | 
| New Game     | Resets game            | No response                  | None                    |
| Submit Guess | Tells hint immediately | 2 clicks before showing hint | None                    |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI tool I used for this project was Claude. When I asked it to fix the opposite hints, it gave me only one of the ride sections of the code to fix, even though there were 2 errors that was creating the problem. After editing the first section, I ran it, and noticed that the hints were still backwards, so I went back to the AI and told it that the problem was still there. It then gave me the correct piece to fix. When I asked it to fix using the enter button, it gave me the right code and a lambda function that I could use so the enter button is fully functional. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To decide whether a bug was really fixed, I first ran the tests in test_game_logic.py to make sure that everything passed. I then ran the game myself, specicially checking and testing the bugs I had noticed at the very start, verifying that the bug was officially fixed. One test I ran manually was playing the whole game myself and resetting the game. I checked the secret number before-hand to make sure the hints it was giving me were correct, and also made sure to reset the game to make sure it reset properly. AI helped me edit and add new tests. In each chat where I fixed the bugs, I asked it to add a test checking this function to test_game_logic.py. It also edited some of the existing tests, since the wording was wrong, specifically the one testing wether the correct hints were given. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

A Stremlit "rerun" is when the code executes chronologically, starting from the top and going all the way to the bottom. This happens with ever interaction, like pressing a button or typing an input. A session state is all the memory needed for a browser sessions. It stops the stored information from completely resetting when a script or code is executed. This way, the session state is able to preserve data when a rerun happens. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit or stratergy I want to reuse in future labs or projects is noting everywhere AI or I made an edit. I think it was useful for me to look back and see where the code and script was edited and who edited it. One thing I would do differently is ask it to make sure all the bugs were fixed before I went and tested it myself. Once, I asked it to fix a bug, and it only partially fixed it, and I had to ask it to debug again to find the other error in the code. I ended up testing the game twice, when I could have only done it once. This project has shown me all the errors that come with AI code. Its a useful tool, but it's not perfect and definitly needs someone with coding experience to debug and check the logic. With the devleopment of AI, I thought it would be a little better at this, but I was proven wrong. 