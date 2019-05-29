from lxml import etree

text = '''
<li class="li li-first" name='item'><a href="link.html">first item</a></li>
'''
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[1]/child::[@href="link1.html"]')
print(result)