class giay:
    loaigiay="sneaker"
    def __init__(self, ten,mausac, size):
        self.mausac=mausac
        self.size=size
        self.ten=ten
    #phuongthuc
    def conlai (self, soluongconlai):
        return "{} hiện trong kho còn {} đôi ".format(self.ten, soluongconlai)
    def dabanhet (self):
        return "{} đã bán hết".format(self.ten)
Nike=giay("Nike Air","Trang","37")
Adidas=giay("Adidas Walk","Hồng","35")

#call your instance methods:
print(Nike.conlai("5"))
print(Adidas.dabanhet())

