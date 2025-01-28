from src.rock_paper_scissors import game

def test_draw():
    result = game(1, 1)
    assert result == "Draw!"

def test_p1_win():
    assert game(1, 3) == "Player 2 wins!"
    assert game(2, 1) == "Player 2 wins!"
    assert game(3, 2) == "Player 2 wins!"

def test_p2_win():
    assert game(3, 1) == "Player 1 wins!"
    assert game(1, 2) == "Player 1 wins!"
    assert game(2, 3) == "Player 1 wins!"

def test_input_error():
    assert game(4, 10) == "Error in input"
