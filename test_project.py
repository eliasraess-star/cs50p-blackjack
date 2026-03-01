from project import hand_value, is_bust

def test_hand_value_normal():
    assert hand_value(["10♠", "9♥"]) == 19

def test_hand_value_ace_low():
    assert hand_value(["A♠", "9♦", "5♣"]) == 15

def test_hand_value_ace_high():
    assert hand_value(["A♠", "9♦"]) == 20

def test_is_bust_true():
    assert is_bust(["10♠", "9♦", "5♣"]) == True

def test_is_bust_false():
    assert is_bust(["10♠", "9♦"]) == False
