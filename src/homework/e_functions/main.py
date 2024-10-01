import void_func
import value_return

def main():
    print(value_return.get_hour(3800), ":", value_return.get_minutes(3800), ":", value_return.get_seconds(3800))

    #bonus
    hour, minute, second = value_return.get_time(3800)
    print(hour, ":", minute, ":", second)

    current_time = int(input("What is your current time?"))
    void_func.time_printer(current_time)

main()
