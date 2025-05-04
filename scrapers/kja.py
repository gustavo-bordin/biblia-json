import requests
from lxml import html
import re
import json
import os

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

kja_page = requests.get("https://bkjfiel.com.br/genesis-1", headers=headers)
tree = html.fromstring(kja_page.content)
books_list = tree.xpath("//select[@id='select-book']/option")

json_bible = {
  "slug": "KJV",
  "name": "King James",
  "version": "1611",
  "books": []
}

for book in books_list:
    book_data = {
      "name": book.text,
      "chapters": []
    }

    book_slug = book.get("data-slug")
    chapters_url = f"https://bkjfiel.com.br/{book_slug}"
    chapters_page = requests.get(chapters_url, headers=headers)
    chapters_tree = html.fromstring(chapters_page.content)
    chapters_list = chapters_tree.xpath("//a[@class='btn-link text-xl lg:text-2xl xl:text-3xl']")

    print(f"Book: {book.text}")

    for chapter in chapters_list:
        chapter_url = f"https://bkjfiel.com.br/{book_slug}-{chapter.text}"
        chapter_page = requests.get(chapter_url, headers=headers)
        chapter_tree = html.fromstring(chapter_page.content)
        verses_list = chapter_tree.xpath("//p[@class='pb-6 xl:pb-8']/a")

        chapter_data = {
          "name": f"Capítulo {chapter.text}",
          "number": int(chapter.text),
          "verses": []
        }

        print(f"Chapter: {chapter.text}")

        for verse in verses_list:
            # Get the full text content
            full_text = verse.text_content().strip()

            # Use regex to separate verse number from verse text
            verse_pattern = re.compile(r'(\d+)(.*)', re.S)
            match = verse_pattern.match(full_text)

            if match:
                verse_number = match.group(1)
                verse_text = match.group(2).strip()

                chapter_data["verses"].append({
                  "number": int(verse_number),
                  "text": verse_text
                })

            print(f"{verse_number} - {verse_text}")

        book_data["chapters"].append(chapter_data)

    json_bible["books"].append(book_data)


with open("kjv_bible.json", 'w', encoding='utf-8') as f:
    json.dump(json_bible, f, ensure_ascii=False, indent=2)