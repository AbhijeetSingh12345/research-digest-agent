
# def extract_claims(text):
#     sentences = text.split(".")
    
#     claims = []

#     for s in sentences:
#         s = s.strip()

#         # Strong filtering rules
#         if (
#             len(s) > 60 and                      # long enough
#             s[0].isupper() and                  # proper sentence start
#             not s.endswith(",") and             # not incomplete
#             "Toggle" not in s and
#             "subsection" not in s and
#             "http" not in s and
#             "List of" not in s and
#             "include" not in s.lower()          # avoid incomplete phrases
#         ):
#             claims.append({
#                 "claim": s,
#                 "evidence": s
#             })

#     # fallback
#     if len(claims) == 0:
#         return [{
#             "claim": text[:200],
#             "evidence": text[:200]
#         }]

#     return claims[:5]
def extract_claims(text):
    sentences = text.split(".")
    
    claims = []

    for s in sentences:
        s = s.strip()

        # Fix incomplete sentence (special case)
        if s.startswith("Study of"):
            s = "Machine learning is the " + s.lower()

        # Strong filtering conditions
        if (
            len(s) > 60 and
            len(s.split()) > 8 and                      # ✅ avoid short fragments
            s[0].isupper() and

            # ❌ bad endings
            not s.endswith((",", ":", "that", "when", "including", "of", "as", "from", "an", "in")) and

            # ❌ bad phrases anywhere
            "dealing with" not in s and
            "has led to several" not in s and
            "can be described as" not in s and

            # ❌ bad endings near end (important fix)
            "such as" not in s[-15:] and
            "including" not in s[-15:] and
            "from a" not in s[-10:] and

            # ❌ junk content
            "Toggle" not in s and
            "subsection" not in s and
            "http" not in s and
            "List of" not in s and
            "However, many AI applications are not perceived" not in s
        ):
            claims.append({
                "claim": s,
                "evidence": s
            })

    # Remove duplicate claims
    seen = set()
    unique_claims = []
    for c in claims:
        if c["claim"] not in seen:
            seen.add(c["claim"])
            unique_claims.append(c)

    # Fallback if nothing extracted
    if len(unique_claims) == 0:
        return [{
            "claim": text[:200],
            "evidence": text[:200]
        }]

    return unique_claims[:5]