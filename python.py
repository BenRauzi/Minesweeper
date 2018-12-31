def switch_demo(argument):
    switcher = {
        x == 0 and not (y == 0 or y ==9): "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    print(switcher)


switch_demo(1)