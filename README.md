# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

The game's purpose is to run a simple number guesssing game. It would choose a secret number, and the user had to guess the number within 8 tries. The game would also give you hints to either go higher or lower after each guess.

I found a multitude of glitches. The hints would be backwards, telling you to go higher when you actually needed to go lower. The enter button would not work to submit the guess, and you would have to click the 'Submit Guess' button twice to give you the hint. The reset button would not work, and the final score would not show with the final message after winning the game. 

There were many fixes I applied in the code using the AI agent. These ranged from fixing simple logic erros and typos to adding and reordering code so it implements in the correct sequence. I also refactored some functions from app.py to logic_utils.py and imported them. The AI agent also helped me create tests to test the functionality of the app properly.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a value of '50'
2. Game returns 'Go Lower!'
3. User enters '25' --> 'Go Lower!'
4. Usr enters '8'
5. Game returns 'Correct!' with balloon animation and final score
6. User resets game to play again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
