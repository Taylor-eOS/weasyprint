import re

cover_html = """
  <div class="cover">
    <img src="cover.jpg" alt="Cover">
  </div>
"""

with open("input.html", encoding="utf-8") as f:
    content = f.read()
pattern = r"(<body[^>]*>)"
replacement = r"\1" + cover_html
new_content = re.sub(pattern, replacement, content, count=1, flags=re.IGNORECASE)
with open("input.html", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Created input.html")
