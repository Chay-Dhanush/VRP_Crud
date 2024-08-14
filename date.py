from datetime import date


start_date=date(2024,8,1)

current_date=date.today()

total_days=90

finished_days=(current_date-start_date).days

print("Remaning days ",total_days-finished_days)
print("Finished days ",finished_days)