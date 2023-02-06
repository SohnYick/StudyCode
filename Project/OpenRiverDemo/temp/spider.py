import requests
import parsel

class Spider:
    """ 
    此类负责爬取数据。
    默认使用pyquery解析
    """

    def __init__(self,url,rules):
        """
        :param url: 解析的URL地址
        :param rules: 解析规则集
        """
        self.url = url
        self.rules = rules
        # 解析的方式：要么JSON，要么DOM
        self.rules_method = self.check_rules()

        # 响应对象
        self.response = None
        # 数据列表
        self.data_list = []
        
    def parse(self):
        """
        :return: 返回列表
        如果解析出的是URL，那么列表中的每个元素应该是字符串。
        如果解析出的是需要持久化的数据，每个元素都应该是字典。
        """
        # 发起网络请求
        self._send()

        # 解析响应的数据：判断解析方式，调用相应的函数
        if self.rules_method == "json":
            self._json_parse()
        if self.rules_method == "dom":
            self._dom_parse()

        # 
        return self.data_list

    def _send(self):
        self.response = requests.get(self.url,headers={
            "origin": "https://coinmarketcap.com",
            "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
        })

    def _dom_parse(self):

        # 得到HTML文档
        html = self.response.text
        selector = parsel.Selector(html)
        
        # 解析出需要的数据，封装成一个个的Bean，装到 self.data_list

        is_first_attribute = True         
        # 遍历传入的字典，得到规则和其对应的名称
        for rule_name in self.rules:
            # 遍历根据规则从HTML中解析出的数据
            for index,value in enumerate(selector.css(self.rules[rule_name]).getall()):
                # 如果是第一个属性
                if is_first_attribute:
                    # 使用append()添加字典
                    self.data_list.append({
                        rule_name:value
                    })
                # 非第一个属性
                else:
                    # 往指定下标位置的字典中加入属性
                    self.data_list[index][rule_name] = value
            # 内层for结束，表示第一个属性已经遍历完毕，之后遍历的就不再是第一个属性。
            is_first_attribute = False

    def _json_parse(self):
        json = self.response.json()


    def check_rules(self):
        """ 检查规则集 """
        # 解析的是JSON
        if type(self.rules) is list or type(self.rules) is tuple:
            return "json"
        # 解析的是DOM
        if type(self.rules) is dict:
            return "dom"
        # 否则就是错误的参数，抛出异常
        raise Exception(f"解析规则只能是tuple、list或dict，不能是{type(self.rules)}")
    
    