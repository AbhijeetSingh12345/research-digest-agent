from ingestion import fetch_url, load_urls
from extraction import extract_claims
from deduplication import deduplicate
from grouping import group_claims
from output import save_sources, generate_digest

def run_pipeline(input_file):
    urls = load_urls(input_file)

    all_claims = []
    sources_data = []

    for url in urls:
        data = fetch_url(url)

        if not data:
            print(f"Skipping: {url}")
            continue

        claims = extract_claims(data["text"])

        for c in claims:
            c["source"] = url

        sources_data.append({
            "source": url,
            "claims": claims
        })

        all_claims.extend(claims)

    deduped = deduplicate(all_claims)
    grouped = group_claims(deduped)

    save_sources(sources_data)
    generate_digest(grouped)

    print("✅ Done! Check outputs/ folder")


if __name__ == "__main__":
    run_pipeline("sample_inputs/urls.txt")
    