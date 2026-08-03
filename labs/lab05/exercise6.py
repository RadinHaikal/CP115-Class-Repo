minutes = int(input("Enter the number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print("original minutes: ", minutes)
print(f"hours: {hours}, remaining minutes: {remaining_minutes}") 
