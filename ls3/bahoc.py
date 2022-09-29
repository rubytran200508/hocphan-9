class giay:
    loaigiay="sneaker"
    def __init__(self, ten,mausac, size):
        self.mausac=mausac
        self.size=size
        self.ten=ten
Nike=giay("Nike Air","Trang","37")
Adidas=giay("Adidas Walk","Hồng","35")

print("Nike là{}".format(Nike.__class__.loaigiay))
print("Adidas là {}".format(Adidas.__class__.loaigiay))

print("Giày {} có màu {} , {} là size giày ".format(Nike.ten, Nike.mausac, Nike.size))
print("Giày {} có màu {}, {} là size giày ".format(Adidas.ten, Adidas.mausac, Adidas.size))


