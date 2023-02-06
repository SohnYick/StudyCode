""" 负责存储的模块 """

class ExcelStorage:

    def __init__(self,path="./",work_book="cmcdata.xlsx",work_sheet="money info"):
        self.path = path
        self.work_book = work_book
        self.work_sheet = work_sheet
