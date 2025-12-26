from collections import defaultdict
import re


def infer_modules(documents):
    modules = defaultdict(list)

    for doc in documents:
        text = doc["content"]

        sentences = text.split(".")
        for s in sentences:
            s = s.strip()
            if len(s) < 50:
                continue

            # Simple heuristic grouping
            if "account" in s.lower():
                modules["Account Management"].append(s)
            elif "video" in s.lower() or "content" in s.lower():
                modules["Content Management"].append(s)
            elif "billing" in s.lower() or "payment" in s.lower():
                modules["Billing"].append(s)
            else:
                modules["General"].append(s)

    return modules
