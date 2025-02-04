def tg_calc(paket_price: int, hours: int, price_per_hour: int, bonus_percent: int):
    finaly_price = hours * price_per_hour
    need_bonuses = finaly_price * (bonus_percent / 100)
    calcucalted_price = finaly_price - need_bonuses
    overage = paket_price - calcucalted_price
    return [finaly_price, calcucalted_price, need_bonuses, overage]


names = ["Normal", "Vip", "Bootcamp"] # Для удобство отображения
prices = [140, 190, 250]  # Стоимтось часа в нормал,вип,бутка
packages_names = ["3H", "5H", "Night", "Morning"]
hours_value = [3, 5, 8, 6]
packages = [  # 3, 5, night, morning
    [350, 550, 700, 300],
    [500, 800, 950, 500],
    [650, 1100, 1200, 800],
]

for bn_percent in range(25, 26):
    print(f"Процент бонусами: {bn_percent}")
    for ind_price, price_hour in enumerate(prices):
        print(f"\n{names[ind_price]} ({price_hour}):")
        for ind_package, price_package in enumerate(packages[ind_price]):
            res = tg_calc(
                paket_price=price_package,
                hours=hours_value[ind_package],
                price_per_hour=price_hour,
                bonus_percent=bn_percent,
            )
            is_profit = res[-1] > 0
            print(
                f"[{packages_names[ind_package]}] | Ориг цена: {price_package} | Цена по часам: {res[0]} | Цена с учетом бонусов: {res[1]} | Надо бонусов: {res[2]} | Выгодно: {'YES' if is_profit else 'NO'} | Разница: {res[-1]}"
            )
            # Остановить работу если оплатить киберночь выгоднее баллами
            # if ind_package == 2 and is_profit:
            #     exit(222)
    print("")
print("\n")
