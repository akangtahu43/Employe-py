from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from datetime import date

class Employee:
    company_name = "TechNusa"
    employee_count = 0

    def __init__(self, name, birth_year, position):
        self.name = name
        self.birth_year = birth_year
        self.position = position
        Employee.employee_count += 1

    def get_age(self):
        return date.today().year - self.birth_year

    def get_info(self):
        return f"{self.name}, {self.position}, {self.get_age()} tahun"

class EmployeeApp(App):
    def build(self):
        self.employees = []

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.name_input = TextInput(hint_text="Nama", multiline=False)
        self.year_input = TextInput(hint_text="Tahun Lahir", multiline=False)
        self.pos_input = TextInput(hint_text="Posisi", multiline=False)

        layout.add_widget(self.name_input)
        layout.add_widget(self.year_input)
        layout.add_widget(self.pos_input)

        add_btn = Button(text="Tambah Karyawan")
        add_btn.bind(on_press=self.add_employee)
        layout.add_widget(add_btn)

        self.info_label = Label(text="Total karyawan: 0", size_hint_y=None, height=30)
        layout.add_widget(self.info_label)

        self.list_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.list_layout)
        layout.add_widget(scroll)

        return layout

    def add_employee(self, instance):
        name = self.name_input.text
        year = int(self.year_input.text)
        position = self.pos_input.text

        emp = Employee(name, year, position)
        self.employees.append(emp)

        self.list_layout.add_widget(Label(text=emp.get_info(), size_hint_y=None, height=30))
        self.info_label.text = f"Total karyawan: {len(self.employees)}"

        self.name_input.text = ""
        self.year_input.text = ""
        self.pos_input.text = ""

if __name__ == "__main__":
    EmployeeApp().run()


class Employee :
    company_name = "TechNusa"
    employee_count = 0
    
    def __init__(self, name, birth_year,possition) :
        self.name =name
        self.birth_year = birth_year
        self.possition = possition

    def get_age (self) :
        return date.today().year - self.birth_year
    def get_info (self) :
        return f"{self.name}, {self.possition},{self.get_age()} tahun"
    @classmethod
    def creat_intern (cls, name, birth_year) :
        return cls(name,birth_year,"Intern")
    @classmethod
    def get_company_info(cls)  :
        return f"{cls.company_name} punya {cls.employee_count} karyawan"
    @staticmethod
    def is_eligible_to_work (age) :
        return age >= 18
    
#buat objek baru
emp1 = Employee ("ikhsan",1999,"Developer")

print(emp1.get_info())
#get info umur
if Employee.is_eligible_to_work(20) :
    print ("bisa bekerja")
else :
    print("Belum bisa awowkwowkowk")

#buat objek intern
int1 = Employee.creat_intern("asep",2000)
print(int1.get_info())