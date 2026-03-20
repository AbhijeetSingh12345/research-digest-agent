import json
import os

def save_sources(data):
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/sources.json", "w") as f:
        json.dump(data, f, indent=2)


def generate_digest(groups):
    os.makedirs("outputs", exist_ok=True)

    md = "# Research Digest\n\n"

    for i, group in enumerate(groups):
        md += f"## Theme {i+1}\n\n"

        for claim in group:
            md += f"- **Claim:** {claim['claim']}\n"
            md += f"  - Evidence: \"{claim['evidence']}\"\n"
            md += f"  - Source: {claim['source']}\n\n"

    with open("outputs/digest.md", "w") as f:
        f.write(md)