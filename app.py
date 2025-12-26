import argparse
from crawler import crawl_site
from content_extractor import extract_clean_text
from module_inference import infer_modules
from output_formatter import format_output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", nargs="+", required=True)
    args = parser.parse_args()

    print("🔍 Crawling URLs...")
    raw_pages = crawl_site(args.urls)

    print("🧹 Extracting content...")
    documents = extract_clean_text(raw_pages)

    print("🧠 Inferring modules...")
    modules = infer_modules(documents)

    print("📦 Formatting output...")
    result = format_output(modules)

    print("\n✅ Final Output:\n")
    print(result)


if __name__ == "__main__":
    main()
