usr_input = int(input("enter the seconds: \n"))

days = usr_input // (24 * 60 * 60)
remaining_sec = usr_input % (24 * 60 * 60)
hours = remaining_sec // 3600
remaining_sec %= 3600
minutes = remaining_sec // 60
seconds = remaining_sec % 60

print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")