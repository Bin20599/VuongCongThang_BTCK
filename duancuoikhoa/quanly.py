import os
print("Current working directory:", os.getcwd())
print("Script directory:", os.path.dirname(os.path.abspath(__file__)))
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILENAME = os.path.join(BASE_DIR, "sinhvien.csv")

def load_students(filename=FILENAME):
    students = []
    if not os.path.exists(filename):
        print(f"File {filename} không tồn tại, sẽ tạo mới khi lưu.")
        return students
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['age'] = int(row['age'])
                    students.append(row)
                except ValueError:
                    print(f"Dữ liệu không hợp lệ ở dòng: {row}")
    except Exception as e:
        print("Lỗi khi đọc file:", e)
    return students

def save_students(students, filename=FILENAME):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'name', 'age', 'major']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow(s)
        print("Đã lưu dữ liệu vào", filename)
    except Exception as e:
        print("Lỗi khi lưu file:", e)

def display_students(students):
    if not students:
        print("Danh sách sinh viên trống.")
        return
    print(f"{'ID':<5} {'Tên':<25} {'Tuổi':<5} {'Ngành học'}")
    print("-"*60)
    for s in students:
        print(f"{s['id']:<5} {s['name']:<25} {s['age']:<5} {s['major']}")

def add_student(students):
    id_ = input("Nhập ID: ").strip()
    if any(s['id'] == id_ for s in students):
        print("ID đã tồn tại! Thêm thất bại.")
        return
    name = input("Nhập họ tên: ").strip()
    try:
        age = int(input("Nhập tuổi: "))
    except ValueError:
        print("Tuổi phải là số nguyên. Thêm thất bại.")
        return
    major = input("Nhập ngành học: ").strip()
    students.append({'id': id_, 'name': name, 'age': age, 'major': major})
    print("Đã thêm sinh viên thành công.")
    save_students(students)
    display_students(students)

def update_student(students):
    id_ = input("Nhập ID sinh viên cần cập nhật: ").strip()
    for s in students:
        if s['id'] == id_:
            name = input(f"Nhập họ tên mới ({s['name']}): ").strip() or s['name']
            try:
                age_input = input(f"Nhập tuổi mới ({s['age']}): ").strip()
                age = int(age_input) if age_input else s['age']
            except ValueError:
                print("Tuổi không hợp lệ. Cập nhật thất bại.")
                return
            major = input(f"Nhập ngành học mới ({s['major']}): ").strip() or s['major']
            s.update({'name': name, 'age': age, 'major': major})
            print("Cập nhật thành công.")
            save_students(students)
            display_students(students)
            return
    print("Không tìm thấy sinh viên với ID này.")

def delete_student(students):
    id_ = input("Nhập ID sinh viên cần xóa: ").strip()
    for i, s in enumerate(students):
        if s['id'] == id_:
            students.pop(i)
            print("Xóa sinh viên thành công.")
            save_students(students)
            display_students(students)
            return
    print("Không tìm thấy sinh viên với ID này.")

def search_student(students):
    keyword = input("Nhập tên sinh viên cần tìm: ").strip().lower()
    found = [s for s in students if keyword in s['name'].lower()]
    if found:
        display_students(found)
    else:
        print("Không tìm thấy sinh viên nào phù hợp.")

def main():
    students = load_students()
    print("\n=== Danh sách sinh viên hiện tại ===")
    display_students(students)

    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            display_students(students)
        elif choice == '0':
            save_students(students)
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

