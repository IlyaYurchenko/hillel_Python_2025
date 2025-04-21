usr_input = int(input("enter the seconds: \n"))

days = usr_input // (24 * 60 * 60)
remaining_sec = usr_input % (24 * 60 * 60)
hours = remaining_sec // 3600
remaining_sec %= 3600
minutes = remaining_sec // 60
seconds = remaining_sec % 60

if days % 10 == 1 and days != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (11 <= days <= 14):
    day_word = "дні"
else:
    day_word = "днів"
print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")