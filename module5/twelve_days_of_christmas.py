def days(day: int):
    days_str = ["first", "second", "third", "fourth", "fifth", "sixth", 
                "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    return days_str[day]

def main():
    lyric_first = "On the first day of Christmas, \nmy true love gave to me\n"
    gift = ["And a partridge in a pear tree.", "Two turtle doves", "Three French hens", "Four calling birds",
            "Five golden rings", "Six geese a-laying", "Seven swans a-swimming", "Eight maids a-milking",
            "Nine ladies dancing", "Ten lords a-leaping", "Eleven pipers piping", "Twelve drummers drumming"]
    for day in range(12):
        if day == 0:
            lyric_without_first = gift[day]
            print(f"On the {days(day)} day of Christmas, \nmy true love gave to me\n" + "A" + gift[day][5:])
            print("")
        elif day == 11:
            lyric_without_first = gift[day] + ",\n" + lyric_without_first
            print(f"On the {days(day)} day of Christmas, \nmy true love gave to me\n" + lyric_without_first[:-1]+"!")
            print("")
        else:
            lyric_without_first = gift[day] + ",\n" + lyric_without_first
            print(f"On the {days(day)} day of Christmas, \nmy true love gave to me\n" + lyric_without_first)
            print("")
    return None

main()