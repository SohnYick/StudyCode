from urllib import parse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# 获取多少页
page_number = 2
# 每页获取多少个货币信息
coin_number = 5

def init():
    ranking_page_url = "https://coinmarketcap.com/"
    
    # 启用Chrome无头模式
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)

    # 发起请求
    browser.get(ranking_page_url)
    return browser

def get_currency_urls(browser):
    ranking_page_rule = "tbody>tr>td:nth-child(3) a.cmc-link"
    urls = []
    for a_element in browser.find_elements(By.CSS_SELECTOR,ranking_page_rule):
        a_url = a_element.get_attribute("href")
        urls.append(a_url)
    return urls

def _get_index_or_socials_urls(browser):
    """
    由于获取多个 主页地址、社交地址 的代码完全一样，暂时用这个函数作为它们的公共函数
    """
    # 移动鼠标到展示所有 主页、社交 的按钮，让需要的内容出现。
    button = browser.find_element(By.CSS_SELECTOR,"button.link-button:first-child")
    ActionChains(browser).move_to_element(button).perform()
    # 然后开始解析
    rule = "div.tippy-content a"
    urls = []
    for a_element in browser.find_elements(By.CSS_SELECTOR,rule):
        a_url = a_element.get_attribute("href")
        urls.append(a_url)
    return urls
def _get_mul_index(browser):
    return _get_index_or_socials
    _urls(browser)
def _get_socials(browser):
    return _get_index_or_socials_urls(browser)

def get_currency_info(browser,currency_part_url):

    # 货币页URL
    currency_page_url = parse.urljoin(browser.current_url,currency_part_url)

    # 获取货币页
    browser.get(currency_page_url)

    # 分析发现，所有的货币页面都有四个ul.content，而所需信息都在第一个
    # 属性对应的解析规则
    # - 排名
    attr_rank_rule = "div.nameHeader+div>div:first-child"
    # - 币名
    attr_name_rule = "div.nameHeader h2 span"
    # - 首页：有些货币有多个主页，这个是处理单主页的
    attr_index_rule = "div.edVIPP:first-child>ul.content>li:first-child>a"
    # - 社交：社交网站都是多个，因此用一个函数处理。
    attr_socials = _get_socials(browser)
    attr_rank = browser.find_element(By.CSS_SELECTOR,attr_rank_rule).text
    attr_name = browser.find_element(By.CSS_SELECTOR,attr_name_rule).text
    try:
        # 首页：但主页规则用于多主页，会出错
        attr_index = browser.find_element(By.CSS_SELECTOR,attr_index_rule).get_attribute("href")
    except Exception:
        attr_index = _get_mul_index(browser)
    
    return {
        "rank": attr_rank,
        "name": attr_name,
        "index": attr_index,
        "socials":attr_socials
    }


    

if __name__ == "__main__":

    browser = init()

    number = 2
    for currency_page_url in get_currency_urls(browser):

        number -= 1

        a_currency_info = get_currency_info(browser,currency_page_url)
        print(a_currency_info)

        if number <=0:
            break


    
  

    # button = driver.find_element(By.CSS_SELECTOR,"ul.content li:nth-child(3) button.link-button")
    # ActionChains(driver).move_to_element(button).perform()

    # for element in driver.find_elements(By.CSS_SELECTOR,"div.tippy-content a"):
    #     print(element.get_attribute("href"))

    # time.sleep(2)
    # driver.quit()




