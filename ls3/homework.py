import math
class SinhVien:

    def __init__(self, id, name, sex, age):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age

class QuanLySinhVien:
    listSinhVien = []

    # Hàm tạo ID tăng dần cho nhân viên
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    def nhapSinhVien(self):
        # Khởi tạo một sinh viên mới
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        sv = SinhVien(svId, name, sex, age)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv:SinhVien = self.findByID(ID)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (sv != None):
            # nhập thông tin sinh viên
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            age = int(input("Nhập tuổi sinh viên: "))
            # cập nhật thông tin sinh viên
            sv._name = name
            sv._sex = sex
            sv._age = age
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))



    # Hàm xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted


    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showSinhVien(self, listSV):
        # hien thi tieu de cot
        print("".format("ID", "Name", "Sex", "Age"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("" .format(sv._id, sv._name, sv._sex, sv._age))
        print("\n")

    # Hàm trả về danh sách sinh viên hiện tại
    def getListSinhVien(self):
        return self.listSinhVien


# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ")
    print("*************************MENU**************************")
    print("**  1. Thêm sinh viên.                               **")
    print("**  2. Cập nhật thông tin sinh viên bởi ID.          **")
    print("**  3. Xóa sinh viên bởi ID.                         **")
    print("**  4. Hiển thị danh sách sinh viên.                 **")
    print("**  0. Thoât                                         **")
    print("*******************************************************")
    
    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có id = ", ID, " đã bị xóa.")
            else:
                print("\nSinh vien co id = ", ID ," không tồn tại.")
        else:
            print("\Danh sách sinh viên trống!")

    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình!")
        break
    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng trong hộp menu.")
