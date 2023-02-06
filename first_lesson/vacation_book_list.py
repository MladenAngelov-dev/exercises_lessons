number_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_a_day = (number_pages // pages_per_hour) // days_per_book
print(hours_a_day)
