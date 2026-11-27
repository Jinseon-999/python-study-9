
total = 0

with open("order.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = line.strip().split(',')

        menu = data[0].strip()
        ea = data[1].strip()
        price = data[2].strip().replace("원", "")

        ea = int(ea)
        price = int(price)

        if price < 0 or price > 10000 or ea < 0:
            continue

        total += ea * price

    print("전체매출: ", total, "원")
