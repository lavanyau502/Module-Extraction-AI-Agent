import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_site(urls, limit=30):
    visited = set()
    pages = []

    for base_url in urls:
        queue = [base_url]

        while queue and len(visited) < limit:
            url = queue.pop(0)
            if url in visited:
                continue

            try:
                res = requests.get(url, timeout=10)
                soup = BeautifulSoup(res.text, "html.parser")
                visited.add(url)

                pages.append({
                    "url": url,
                    "html": soup
                })

                for link in soup.find_all("a", href=True):
                    full_url = urljoin(url, link["href"])
                    if urlparse(full_url).netloc == urlparse(base_url).netloc:
                        queue.append(full_url)

            except Exception:
                continue

    return pages
