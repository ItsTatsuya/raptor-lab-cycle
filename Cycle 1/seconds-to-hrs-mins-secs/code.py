seconds = int(input("Enter the seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
rem_seconds = seconds % 60

print(f"{seconds} sec formatted to {hours}Hrs:{minutes}Minutes:{rem_seconds}Sec")
