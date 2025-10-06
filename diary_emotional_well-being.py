week_days_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
mood_list = []
for i in range (len(week_days_list)):
    mood = int(input(''))
    stars = mood * '*'
    rating = f"({mood})"
    if 1 <= mood <= 10:
        mood_list.append(stars + " " + rating)
    else:
        mood_list.append(rating)
print("\n".join(mood_list))