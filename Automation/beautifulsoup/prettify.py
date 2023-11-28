# https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-eliminate-span-html-tags/
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <h1>Hello, BeautifulSoup!</h1>
        <ul>
            <li><a href="http://example.com">Example.com <span>(Link)</span></a></li>
            <li><a href="http://scrapy.org">Scrapy.com <span>(Link)</span></a></li>
        </ul>
    </body>
</html>
"""

    
soup = BeautifulSoup(html_doc, 'html.parser')

body_tag = soup.select_one('body')
print(body_tag.prettify())

# result will be > include selector to
"""
<body>
 <h1>
  Hello, BeautifulSoup!
 </h1>
 <ul>
  <li>
   <a href="http://example.com">
    Example.com
    <span>
     (Link)
    </span>
   </a>
  </li>
  <li>
   <a href="http://scrapy.org">
    Scrapy.com
    <span>
     (Link)
    </span>
   </a>
  </li>
 </ul>
</body>
"""