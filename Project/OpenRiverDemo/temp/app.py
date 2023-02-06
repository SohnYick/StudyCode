from spider import Spider

def check_parse_result(parse_result):
    """
    这个方法检查解析结果。
    如果是需要保存的数据，返回True。
    如果是URL，则返回False。
    """
    # 返回的列表中，最少有一个元素，是字典
    element =  parse_result[0]
    # 如果这个字典中只有一个属性，而且属性名为url，则表示返回的是URL。
    if len(element) == 1 and element.get("url") != None:
        return False
    # 否则，就是真实数据
    return True

if __name__ == "__main__":

    list_page = "https://coinmarketcap.com/"
    list_page_rules = {
        "url":"tbody>tr>td:nth-child(3) .cmc-link::attr(href)"
    }

    info_page_urls = Spider(url=list_page,rules=list_page_rules).parse()

    for url in info_page_urls:
        print(url)
    
    print(len(info_page_urls))
    
  

    
