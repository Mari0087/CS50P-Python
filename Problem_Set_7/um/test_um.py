from um import count

def test_count():
    assert count("um") == 1
    assert count('album') == 0
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album where, um, umm, the clumsy alums play drums?") == 2
    assert count("um? mum?") == 1