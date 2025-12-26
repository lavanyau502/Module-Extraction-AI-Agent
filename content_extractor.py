def extract_clean_text(pages):
    documents = []

    for page in pages:
        soup = page["html"]

        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = " ".join(p.get_text(strip=True) for p in soup.find_all("p"))

        if len(text) > 200:
            documents.append({
                "url": page["url"],
                "content": text
            })

    return documents

