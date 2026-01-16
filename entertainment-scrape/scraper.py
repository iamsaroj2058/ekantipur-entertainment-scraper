from playwright.sync_api import sync_playwright
import json

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigation
        page.goto("https://ekantipur.com")
        page.click("a:has-text('मनोरञ्जन')")  # Click Entertainment section
        page.wait_for_selector("article")      # Wait for articles
        page.wait_for_load_state("networkidle")

        # Selecting articles
        articles = page.query_selector_all("article")[:5]  # Top 5

        entertainment_news = []

        # Looping through elements
        for article in articles:
            title_el = article.query_selector("h2")
            title = title_el.text_content() if title_el else None

            img_el = article.query_selector("img")
            image_url = img_el.get_attribute("src") if img_el else None

            author_el = article.query_selector(".author")
            author = author_el.text_content() if author_el else None

            entertainment_news.append({
                "title": title.strip() if title else None,
                "image_url": image_url,
                "category": "मनोरञ्जन",
                "author": author.strip() if author else None
            })

        # Save JSON
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(
                {"entertainment_news": entertainment_news},
                f,
                ensure_ascii=False,
                indent=2
            )

        print("Scraping complete! Check output.json")

        browser.close()

if __name__ == "__main__":
    main()
