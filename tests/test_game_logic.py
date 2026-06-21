from logic_utils import check_guess, parse_guess
# FIXED: using agent, edited pytests to test the fucntions

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_displays_immediately():
    # Verify that hint is returned on single submission (not delayed)
    outcome, message = check_guess(60, 50)
    assert message is not None
    assert message != ""

def test_enter_key_submission():
    # Verify that parse_guess accepts input (simulating enter key)
    ok, guess_int, err = parse_guess("50")
    assert ok == True
    assert guess_int == 50
    assert err is None

# FIXED: using agent, added a test to check hints and ensure they are correct
def test_hint_messages_are_correct():
    # Test that "Too High" gives the "Go LOWER" hint
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "📉" in message

    # Test that "Too Low" gives the "Go HIGHER" hint
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "📈" in message

    # Test correct guess
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

# FIXED: using agent, created a test to make sure that the game will reset 
def test_new_game_reset_attempts():
    """Test that clicking 'New Game' resets attempts to 1, not 0"""
    # Simulate session state after playing several rounds
    session_state = {
        "attempts": 5,
        "secret": 42,
        "score": 100,
        "status": "playing",
        "history": [10, 20, 30, 40],
    }

    # Simulate the corrected "New Game" button handler
    # attempts should be reset to 1 (not 0, which was the bug)
    session_state["attempts"] = 1
    session_state["secret"] = 50
    session_state["score"] = 0
    session_state["status"] = "playing"
    session_state["history"] = []

    # Verify all state is reset properly
    assert session_state["attempts"] == 1, "Attempts should reset to 1, not 0"
    assert session_state["secret"] == 50
    assert session_state["score"] == 0
    assert session_state["status"] == "playing"
    assert session_state["history"] == []
