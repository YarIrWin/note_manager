from datetime import datetime
created_date = (input("введите дату создания заметки "))
issue_date = (input("введите дату окончания срока заметки "))
created_date_obj = datetime.strptime(created_date, "%d.%m.%Y")
issue_date_obj = datetime.strptime(issue_date, "%d.%m.%Y")
print(created_date_obj, issue_date_obj)