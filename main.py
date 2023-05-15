

def sell_product(picked_product, store, user):
    if picked_product in store:
        items_to_delete = []
        for item in store.keys():
            if item == picked_product:
                if user['money'] >= store[item]:
                    user['bag'].append({item: store[item]})
                    user['money'] -= store[item]
                    print(item.capitalize(), "успешно добавлено в вашу сумку.")
                    print("У вас осталось", user['money'], "$.")
                    items_to_delete.append(item)
                else:
                    print("У вас недостаточно денег, чтобы купить", item.capitalize())

        for item in items_to_delete:
            del store[item]

def show_products(store):
    for key, value in store.items():
        print(f"{key} - {value}$")

def check_something(what, where):
    if what in where:
        print(where[what])


def is_quit():
    return input("Хотите продолжить покупки? (y/n): ").lower()

def present_data(data):
    for item in data:
        print(item)


def main():
    is_running=True
    user = {
        "name": "John",
        "money": 48
    }

    store = {
        "sneakers": 23,
        "pepsi": 13,
        "car": 10,
        "fish": 11
    }
    user['bag'] = []

    while is_running:

        print("Привет, выберите что-нибудь: ")

        show_products(store)

        sell_product(input("Выберите, что вы хотите купить: ").lower(), store, user)

        check_something("bag", user)

        present_data([user, store])

        if is_quit() == "n":
            is_running = False


if __name__ == "__main__":
    main()
