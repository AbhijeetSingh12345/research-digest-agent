from deduplication import deduplicate

def test_dedup():
    claims = [
        {"claim": "EVs reduce emissions"},
        {"claim": "Electric vehicles reduce emissions"}
    ]

    result = deduplicate(claims)
    assert len(result) == 1