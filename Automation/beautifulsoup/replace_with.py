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

li_tags = soup.find_all('li')
for li in li_tags:
    # this replace span to b tag
    new_tag = soup.new_tag("b")
    new_tag.string = "[Click Here]"
    li.span.replace_with(new_tag)

print(soup)