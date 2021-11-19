from lxml import etree


text = '''
    <div>
        <ul>
            <li class="item-1">
                <a href="link1.html">first item</a>
            </li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
    '''
# 创建element对象
html = etree.HTML(text)
# print(html)
# print(dir(html)) #含有xpath方法

print()
