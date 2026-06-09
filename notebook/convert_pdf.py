import os
import asyncio
from playwright.async_api import async_playwright

async def generate_pdf():
    # The report.html is located one folder up relative to this notebook
    html_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'report.html'))
    html_file = f"file:///{html_path}"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        print(f"Loading {html_file} ...")
        await page.goto(html_file)

        # Give it a couple seconds to fully render the report
        await page.wait_for_timeout(2000)

        pdf_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'report.pdf'))
        await page.pdf(path=pdf_path, format="A4")
        await browser.close()
        print(f"PDF saved successfully as {pdf_path}")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
