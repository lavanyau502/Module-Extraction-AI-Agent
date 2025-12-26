from bs4 import BeautifulSoup

def clean_content(html):
    """
    Extract meaningful documentation text from raw HTML.
    Focuses on main content blocks and removes noise.
    Returns a list of cleaned text strings.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Step 2: Remove unwanted tags
    for tag in soup(["script", "style", "header", "footer", "nav"]):
        tag.decompose()

    # Step 3: Focus on main content
    content_blocks = []
    main_content = soup.find_all(["main", "article", "section"])

    # Fallback: if no <main>/<article>/<section>, use whole page
    if not main_content:
        main_content = [soup]

    for block in main_content:
        for tag in block.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
            text = tag.get_text(strip=True)
            if text:
                content_blocks.append(text)

    # Step 4: Normalize and deduplicate
    cleaned = []
    seen = set()
    for text in content_blocks:
        if text not in seen:
            cleaned.append(text.strip())
            seen.add(text)

    return cleaned
