 import os
  from playwright.sync_api import sync_playwright
  def run():
      url = "https://www.kv.ee/en/search?deal_type=2&county=1&parish=1061&price_max=650"

      with sync_playwright() as p:
          browser = p.chromium.launch(headless=True)
          # On utilise un User-Agent pour paraître plus "humain"
          context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
          page = context.new_page()

          print(f"Navigation vers : {url}")
          page.goto(url, wait_until="domcontentloaded")

          # Attendre que la liste des annonces soit présente
          page.wait_for_selector(".offer-row")

          # Extraction des données
          annonces = page.query_selector_all(".offer-row")
          results = []

          for ann in annonces:
              titre = ann.query_selector(".offer-title").inner_text().strip()
              prix = ann.query_selector(".offer-price").inner_text().strip()
              lien = ann.query_selector("a").get_attribute("href")
              results.append(f"{titre} - {prix}\nLien : {lien}\n")

          # Affichage pour les logs de GitHub
          print("\n".join(results))
          browser.close()

  if __name__ == "__main__":
      run()
