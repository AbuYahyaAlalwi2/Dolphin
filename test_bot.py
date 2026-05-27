from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        # فتح متصفح مخفي
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        # زيارة موقع للتأكد من أن الأذرع تعمل
        page.goto("https://www.google.com")
        print("تم ربط الأذرع بنجاح! المتصفح يعمل.")
        browser.close()

if __name__ == "__main__":
    run_test()