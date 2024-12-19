import csv
import random
from tabulate import tabulate
from datetime import datetime

FILE_NAME_1 = 'qlsv_teacher.csv'
FILE_NAME_2 = "qlsv_student.csv"
FILE_NAME_3 = 'schedule.csv'

class Student:
	def __init__(self, ID, Name, Class, sex, ):
		self.Class = Class
		self.Name = Name
		self.ID = ID
		self.sex = sex

class School_Schedule:
	def __init__(self, Day, Start, End, Course):
		self.Day = Day
		self.Start = Start
		self.End = End
		self.Course = Course

def read_schedule():
	Day = input("Enter Day: ")
	Start = input("Enter Start: ")
	End = input("Enter End: ")
	Course = input("Enter Course: ")
	schedule = School_Schedule(Day, Start, End, Course)

	return schedule
		
def print_schedule(schedule):
	print("Day :", schedule.Day)
	print("Start: ", schedule.Start)
	print("End: ", schedule.End)
	print("Course: ", schedule.Course)

def read_schedules():
	schedules = []
	total_schedules = 7
	for i in range(total_schedules):
		print("------")
		print("Schedule " + str(i + 1))
		schu = read_schedule()	
		schedules.append(schu)
	return schedules	

def print_schedules_table(schedules):
	table = []
	for i, schedule in enumerate(schedules, start = 1):
			table.append([i, schedule.Day, schedule.Start, schedule.End, schedule.Course])

	headers = ["#", "Day", "Start Time", "End Time", "Course"]
	print("=== School Schedule ===")
	print(tabulate(table, headers, tablefmt="grid"))

def write_schedules_to_csv(schedules):
	with open(FILE_NAME_3, mode = "w", newline='', encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow(["Day", "Start", "End", "Course"])
		for schedule in schedules:
			writer.writerow([schedule.Day, schedule.Start, schedule.End, schedule.Course])

def read_schedules_to_csv():
	schedules = []
	with open(FILE_NAME_3, mode = 'r', newline = '', encoding = 'utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			if len(row) == 4:
				schedules.append(School_Schedule(row[0], row[1], row[2], row[3]))

	return schedules

# Nhập từng học sinh
def read_student():
	Name = input("Enter name: ") 
	ID = input("Enter ID: ") 
	sex = input("Enter sex (M/F): ") 
	Class = input("Enter class: ") 
	student = Student(ID, Name, Class, sex)

	return student

# In từng học sinh
def print_student(student):
	print( "Student Name: ", student.Name)
	print( "Student ID: ", student.ID)
	print( "Student sex: ", student.sex)
	print( "Student Class: ", student.Class)

# Nhập nhiều học sinh
def read_students():
	students = []
	total_student = int(input("How many students: "))
	for i in range(total_student):
		print("Student " + str(i + 1)) 
		stu = read_student()
		students.append(stu)
	return students	

# In nhiều học sinh 
def print_students(students):
	for i in range(len(students)):
		print("-----")
		print("Student " + str(i + 1) + ":")
		print_student(students[i])

# Ghi vào file cvs
def write_student_to_csv(students):
	with open(FILE_NAME_1, mode="w", newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(["Name", "ID" , "sex", "Class"])
		for student in students:
			writer.writerow([student.Name, student.ID, student.sex, student.Class])

# Đọc trong file cvs
def read_student_to_csv():
	students = []
	with open(FILE_NAME_1, mode="r", newline='', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			if row:
				Name, ID, sex, Class = row[0], row[1], row[2], row[3]
				student = Student(ID, Name, Class, sex)
				students.append(student)
	return students

# Vẽ menu
def show_menu_manager():
	print("           | MAIN MENU |           ")
	print("-----------------------------------")
	print("| Option 1: For Teachers          |")
	print("| Option 2: For Students          |")
	print("| Option 3: Exit                  |")
	print("-----------------------------------")

# Vẽ menu teacher
def show_menu_teachers():
	print("----------|FOR TEACHERS|-----------")
	print("| Option 1: Excel students.       |")
	print("| Option 2: Random ID.            |")
	print("| Option 3: Student attendance    |")
	print("| Option 4: Excel schedules.      |")
	print("| Option 5: Exit.                 |")
	print("-----------------------------------")

def opt_1_teach():
	print("------|Creative to students|-------")
	print("| Option 1: Creative to students. |")
	print("| Option 2: Show students.        |")
	print("| Option 3: Add student.          |")
	print("| Option 4: Update student.       |")
	print("| Option 5: Delete student.       |")
	print("| Option 6: Save to Exit.         |")
	print("-----------------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice	

def add_student(students):
    print("-----|Enter Add Your Students|-----")
    total_students = int(input("How many students do you want to add: "))
    for i in range(total_students):
        print(f"Student {i + 1}:")
        new_student_Name = input("Enter name: ")
        new_student_ID = input("Enter ID: ")
        new_student_age = input("Enter sex: ")
        new_student_Class = input("Enter class: ")
        new_student = Student(new_student_Name, new_student_ID, new_student_age, new_student_Class)
        students.append(new_student)
    print(f"Added {total_students} students successfully!")
    return students

def update_student(students):
	print_students(students)
	find = select_in_range("Enter a update student (1 - " + str(len(students)) + "): ", 1, int(len(students)))

	print("------|Update Student?|-----")
	print("| 1. Name                  |")
	print("| 2. ID                    |")
	print("| 3. sex                   |")
	print("| 4. Class                 |")
	print("----------------------------")

	choice = select_in_range("Select a number (1 - 4): ", 1, 4)
	if choice == 1:
		students[find - 1].Name = input("Enter new name: ")
	elif choice == 2:
		students[find - 1].ID = input("Enter new ID: ")
	elif choice == 3:
		students[find - 1].sex = input("Enter new sex: ")
	elif choice == 4:
		students[find - 1].Class = input("Enter new class: ")

	print("Update Successfully!!!")	
	return students

def delete_student(students):
	print_students(students)
	choice = select_in_range("Enter a delete student (1 - " + str(len(students)) + "): ", 1, int(len(students)))
	new_list_student = []
	for i in range(len(students)):
		if i == choice - 1 :
			continue

		new_list_student.append(students[i])

	students = new_list_student
	print("Remove Successfully!!!")

	return students		

def opt_2_teach(students):
	if not students:
		print("NO STUDENT")
		return None

	students_random = random.choice(students)
	stu_return = str(students_random.Name) + " - " + str(students_random.ID)
	return stu_return	

def opt_3_teach(students):
	if not students:
		print("NO STUDENT")
		return None

	today = datetime.now().strftime("%Y-%m-%d")

	with open(FILE_NAME_1, mode='r', newline='', encoding='utf-8') as file:
		reader = csv.reader(file)
		data = list(reader)

	if today is not data[0]:
		data[0].append(today)

	day = data[0].index(today)

	present = 0
	absent = 0 
	
	for student in students:
		for row in data[1:]:
			if row[1] == student.ID:
				student_row = row
				break

		while len(student_row) < len(data[0]):
			student_row.append("v")

			print("Student: " + student.Name)
			status = select_in_range("Attendance [0 (vkp)/1 (*)/2 (v)]: ", 0 , 2)
			if status == 1:
				student_row[day] = "*"
				present += 1
			elif status == 2:
				student_row[day] = "v"
				absent += 1
			elif status == 0:
				student_row[day] = "vkp"
				absent += 1

	with open(FILE_NAME_1, mode='w', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerows(data)

	print("--------")
	print("Students present : (" + str(present) + "/" + str(present + absent) + ")")

def opt_4_teach():	
	print("------|Creative to schedule|-------")
	print("| Option 1: Creative to schedules.|")
	print("| Option 2: Show schedule.        |")
	print("| Option 3: Update schedules.     |")
	print("| Option 4: Save to Exit.         |")
	print("-----------------------------------")

def update_schedules(schedules):
	print_schedules_table(schedules)
	if not schedules:
		print("No schedules to update!!!")
		return schedules

	index = select_in_range("Enter a update schedule (1 - " + str(len(schedules)) + "): ", 1, int(len(schedules))) - 1

	print("------|Update Student?|-----")
	print("| 1. Update Day            |")
	print("| 2. Update Start Time     |")
	print("| 3. Update End Time       |")
	print("| 4. Update Course         |")
	print("----------------------------")

	choice = select_in_range("Select an option (1 - 4): ", 1, 4)
	if choice == 1:
		schedules[index].Day = input("Enter new day: ")
	elif choice == 2:
		schedules[index].Start = input("Enter new start time: ")		
	elif choice == 3:
		schedules[index].End = input("Enter new end time: ")
	elif choice == 4:
		schedules[index].Course = input("Enter new course: ")

	return schedules

def show_menu_students():
	print("----------|FOR STUDENTS|-----------")
	print("| Option 1:                       |")
	print("| Option 2:                       |")
	print("| Option 3: Exit.                 |")
	print("-----------------------------------")

def opt_1_stu():
	pass

def main():

	while True:
		show_menu_manager()
		choice_manager = select_in_range("Select an option (1 - 3): ", 1, 3)

		if choice_manager == 1:
			while True:
				show_menu_teachers()
				choice_teach = select_in_range("Select an option (1 - 5): ", 1, 5)

				if choice_teach == 1:

					try:
						students = read_student_to_csv()
						print("Loadinggg...........")
					except:
						print("Welcome, first user!!")

					while True:
						opt_1_teach()
						choice_ex_stu = select_in_range("Select an option (1 - 6): ", 1, 6)	
						
						if choice_ex_stu == 1:
							students = read_students()
						
						try:
							if choice_ex_stu == 2:
								print_students(students)
								input("\nPress Enter to continue.\n")
							elif choice_ex_stu == 3:
								students = add_student(students)
								input("\nPress Enter to continue.\n")
							elif choice_ex_stu == 4:
								students = update_student(students)
								input("\nPress Enter to continue.\n")		
							elif choice_ex_stu == 5:
								students = delete_student(students)
								input("\nPress Enter to continue.\n")		
							elif choice_ex_stu == 6:
								write_student_to_csv(students)
								print("Save Data Successfully !!!! ")
								break
						
						except:
							print("You don't have any students yet!!! ")
							input("\nPress Enter to continue.\n")
						
				try:
					students = read_student_to_csv()
					if choice_teach == 2:
						
						choice_students = opt_2_teach(students)
						
						if choice_students:
							print("Randomly selected:", choice_students)
							input("\nPress Enter to continue.\n")

					elif choice_teach == 3:
						opt_3_teach(students)
						input("\nPress Enter to continue.\n")

					elif choice_teach == 4:
						try:
							schedules = read_schedules_to_csv()
							print("Loadinggg...........")
						except:
							print("Welcome, first user!!")

						while True:
							opt_4_teach()
							choice_ex_sche = select_in_range("Select an option (1 - 4): ", 1, 4)

							if choice_ex_sche == 1:
								schedules = read_schedules()
							try:
								if choice_ex_sche == 2:
									print_schedules_table(schedules)
									input("\nPress Enter to continue.\n")
								elif choice_ex_sche == 3:
									schedules = update_schedules(schedules)	
									input("\nPress Enter to continue.\n")												
								elif choice_ex_sche == 4:
									write_schedules_to_csv(schedules)
									print("Save Data Successfully !!!! ")
									input("\nPress Enter to continue.\n")
									break

							except:
								print("You don't have any schedules yet!!! ")
								input("\nPress Enter to continue.\n")

					elif choice_teach == 5:
						print("Exit Successfully !!!! ")
						break
				except:
					print("You don't have any students yet!!! ")
					input("\nPress Enter to continue.\n")

		elif choice_manager == 2:
			while True:
				show_menu_students()
				choice_stu = select_in_range("Select an option (1 - 3): ", 1, 3)
				if choice_stu == 3:
					print("Exit Successfully !!!! ")
					break

		elif choice_manager == 3:
			print("Exit Successfully !!!! ")
			break			

main()