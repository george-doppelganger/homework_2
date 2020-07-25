HEADER_LENGTH = 80

# melon price table
melon_prices = { "Musk":       1.15, 
                 "Hybrid":     1.30, 
                 "Watermelon": 1.75, 
                 "Winter":     4.00 }


def melon_count(order_file_name):
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    with open(order_file_name) as f:
        for line in f:
            (_, melon_type, melon_count) = line.rstrip().split("|")

            melon_tallies[melon_type] += int(melon_count)

    return melon_tallies #this is a dict

def print_melon_sales(mellon_tallies):


    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]


        print("We sold {} {} melons at {:.2f} each for a total of {:.2f}"
                .format(melon_tallies[melon_type], melon_type, price, revenue))



print("*" * HEADER_LENGTH)

melon_tallies = melon_count('orders-by-type.txt')

print_melon_sales(melon_tallies)




print("******************************************")
f = open("orders-with-sales.txt")
sales = {'internet':0, 'salesperson':0}
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales['internet'] += float(d[3])
    else:
        sales['salesperson'] += float(d[3])


print("Salespeople generated ${:.2f} in revenue."
        .format(sales['salesperson']))

print("Internet sales generated ${:.2f} in revenue."
        .format(sales['internet']))

if sales['salesperson'] > sales['internet']:
    print("In-person sales exceeded online-generated revenue")
else:
    print("Online sales exceeded salesperson-generated revenue")

print("******************************************")
