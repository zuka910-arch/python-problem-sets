months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip().title()
        if "/" in date:
            m,d,y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if 1<= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02}-{d:02}")
                break
        elif "," in date:
            clean_date = date.replace(",", "")
            m,d,y = clean_date.split(" ")
            if m in months and 1<= m <= 12 and 1 <= d <= 31:
                m_num = months.index(m) + 1
                d = int(d)
                y = int(y)
                print(f"{y}-{m_num:02}-{d:02}")
                break

    except:
        pass