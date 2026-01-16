from playwright.sync_api import sync_playwright
import json
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigation with longer timeout
        try:
            page.goto("https://ekantipur.com/cartoon", timeout=60000)
        except:
            print("Navigation timed out, continuing anyway...")
        
        # Wait for content to load with more flexible approach
        try:
            page.wait_for_selector(".catroon-wrap", timeout=10000)
        except:
            print("Cartoon elements not found immediately, trying fallback...")
        
        # Give time for content to load
        time.sleep(5)

        # Try to find cartoon elements
        cartoons = page.query_selector_all(".catroon-wrap")
        
        # If no elements found with main selector, try alternative selectors
        if not cartoons:
            print("No cartoons found with .catroon-wrap, trying other selectors...")
            # Try other possible selectors
            possible_selectors = [".cartoon-item", "article", ".item", ".card"]
            for selector in possible_selectors:
                cartoons = page.query_selector_all(selector)
                if cartoons:
                    print(f"Found {len(cartoons)} elements with selector: {selector}")
                    break
        
        print(f"Found {len(cartoons)} cartoon elements")

        cartoon_data = []

        # Looping through all cartoon elements
        for cartoon in cartoons:
            title = None
            author = None
            image_url = None
            
            # Try multiple ways to extract title and author
            # Method 1: Try .cartoon-author span
            author_el = cartoon.query_selector(".cartoon-author p span")
            if not author_el:
                author_el = cartoon.query_selector(".cartoon-author span")
            if not author_el:
                author_el = cartoon.query_selector("figcaption")
            
            if author_el:
                full_text = author_el.text_content().strip()
                if " - " in full_text:
                    parts = full_text.split(" - ")
                    title = parts[0].strip()
                    author = parts[1].strip() if len(parts) > 1 else None
                else:
                    title = full_text
            else:
                # Try to find title in h2, h3, or other heading elements
                title_el = cartoon.query_selector("h2, h3, .title, .headline")
                if title_el:
                    title = title_el.text_content().strip()
            
            # Extract image URL
            img_el = cartoon.query_selector("img")
            if img_el:
                image_url = img_el.get_attribute("src")
                # If no src, try srcset
                if not image_url:
                    image_url = img_el.get_attribute("srcset")
                    if image_url:
                        # Take first URL from srcset
                        image_url = image_url.split(",")[0].strip().split(" ")[0]
            
            # Only add if we have at least title or image
            if title or image_url:
                cartoon_data.append({
                    "title": title,
                    "image_url": image_url,
                    "author": author
                })

        # Save JSON
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(
                {"cartoons": cartoon_data},
                f,
                ensure_ascii=False,
                indent=2
            )

        print(f"Scraping complete! Found {len(cartoon_data)} cartoons. Check output.json")

        # automatically close the browser
        browser.close()

if __name__ == "__main__":
    main()