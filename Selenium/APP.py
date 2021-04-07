class  APPInfo :
    def __init__(self,appName, companyName,imgPath,star,category=None,reviewPeople=None,star5Rate=None,star4Rate=None,star3Rate=None,star2Rate=None,star1Rate=None):
        self.__appName = appName
        self.__companyName = companyName
        self.__imgPath = imgPath
        self.__star = star
        self.category =category
        self.reviewPeople = reviewPeople
        self.star5Rate = star5Rate
        self.star4Rate = star4Rate
        self.star3Rate = star3Rate
        self.star2Rate = star2Rate
        self.star1Rate = star1Rate

    def getAppName(self):return self.__appName

    def getCompany(self):return self.__companyName

    def getimgPath(self):return self.__imgPath

    def getstar(self):return  self.__star

