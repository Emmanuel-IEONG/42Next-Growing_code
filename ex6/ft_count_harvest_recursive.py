def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count = days

    def count_days(count):
        if (count <= 0):
            print("Harvest time!")
            return
        print(f"Day {days + 1 - count}")
        count_days(count - 1)

    count_days(count)
