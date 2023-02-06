class SocialBean:
    """ 此类封装社交媒体的的URL """
    def __init__(self,twitter="nothing"):
        self.twitter = twitter
class MoneyBean:
    """ 此类封装CMC上电子货币的信息 """
    def __init__(self,rank,name,index,socials=SocialBean()):
        self.rank = rank
        self.name = name
        self.index = index
        self.socials = socials
class BookBean:
    """ 此类封装书籍信息 """
    def __init__(self,title,rank):
        self.title = title
        self.rank = rank

