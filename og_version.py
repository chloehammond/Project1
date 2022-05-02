def print_menu():
    print('\nWelcome to generic E-Commerce Store!')
    print('Which of the following would you like to do?')
    print('1. Add Item')
    print('2. Update Item')
    print('3. Delete Item')
    print('4. Display Items by Name')
    print('5. Display Items by Total')
    print('6. View Cart')
    print('7. Quit')


def add_item():
    name = input('Enter the name of the item you want to add: ')
    price = float(input('Enter the price of the item: '))
    quantity = int(input('Enter the quantity of item to be purchased: '))
    items.append(name)
    prices.append(price)
    quantities.append(quantity)


def update_item():  # your lab work
    name_update = input('Enter the name of the item to update: ')
    price_update = float(input('Enter the updated price of the item: '))
    quantity = int(input('Enter the updated quantity of item to be purchased: '))


def delete_item():  # your lab work


def sort_by_name():
    items2 = items.copy()
    prices2 = prices.copy()
    quantities2 = quantities.copy()

    for i in range(len(items)):
        min_index = 0
        for j in range(1, len(items2)):
            if items2[j] < items2[min_index]:
                min_index = j
        items[i] = items2[min_index]
        prices[i] = prices2[min_index]
        quantities[i] = quantities2[min_index]
        items2.pop(min_index)
        prices2.pop(min_index)
        quantities2.pop(min_index)
    view()


def sort_by_price():  # your lab work


def view():
    sum = 0
    for i in range(len(items)):
        sum += prices[i] * quantities[i]
        print(f'{items[i]  ${prices[i]:.2f} X{quantities[i]} for ${prices[i] * quantities[i]:.2f}')
        print(f'Total: ${sum:.2f}')


items = []  # store my products in a list because we want to order it later
prices = []
quantities = []

option = 0
while True:  # ending program controlled by option 7
    print_menu()
    option = int(input('Enter the number of your choice: '))

    if option == 1:
        add_item()
    elif option == 2:
        update_item()
    elif option == 3:
        delete_item()
    elif option == 4:
        sort_by_name()
    elif option == 5:
        sort_by_price()
    elif option == 6:
        view()
    elif option == 7:
        print('Quitting')
        break
    else:
        print('Option unavailable. Please choose an option displayed.')