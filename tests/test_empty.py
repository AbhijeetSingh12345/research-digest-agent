from ingestion import fetch_url

def test_empty():
    assert fetch_url("http://invalid-url.com") is None