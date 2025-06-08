from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("-" * 30)
    print("*** CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ***")
    print("*** 1. Thêm sinh viên.                 ***")
    print("*** 2. Cập nhật thông tin sinh viên bởi ID. ***")
    print("*** 3. Xóa sinh viên bởi ID.            ***")
    print("*** 4. Tìm kiếm sinh viên theo tên.       ***")
    print("*** 5. Sắp xếp sinh viên theo điểm trung bình. ***")
    print("*** 6. Sắp xếp sinh viên theo tên chuyên ngành. ***")
    print("*** 7. Hiển thị danh sách sinh viên.    ***")
    print("*** 0. Thoát.                           ***")
    print("-" * 30)

    key = int(input("Nhập tùy chọn: "))

    if key == 1:
        print("\n--- Thêm sinh viên ---")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công!")
    elif key == 2:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n--- Cập nhật thông tin sinh viên ---")
            ID = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống!")
    elif key == 3:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n--- Xóa sinh viên ---")
            ID = int(input("Nhập ID sinh viên cần xóa: "))
            if (qlsv.deleteById(ID)):
                print(f"\nSinh viên có ID = {ID} đã bị xóa.")
            else:
                print(f"\nSinh viên có ID = {ID} không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống!")
    elif key == 4:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n--- Tìm kiếm sinh viên theo tên ---")
            nameSearch = input("Nhập tên để tìm kiếm: ")
            searchResult = qlsv.findByName(nameSearch)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống!")
    elif key == 5:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n--- Sắp xếp sinh viên theo điểm trung bình (GPA) ---")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif key == 6:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n--- Sắp xếp sinh viên theo tên chuyên ngành ---")
            qlsv.sortByTenChuyenNganh()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif key == 7:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n--- Danh sách sinh viên ---")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
        
