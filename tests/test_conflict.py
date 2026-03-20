def test_conflict():
    claims = [
        {"claim": "Remote work increases productivity"},
        {"claim": "Remote work decreases productivity"}
    ]

    assert len(claims) == 2