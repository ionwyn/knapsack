'Author: Ionwyn Sean'

def knapsack(items, weight):

    table = [[0 for w in xrange(weight + 1)] for i in xrange(len(items) + 1)]

    for i in xrange(1, len(items) + 1):
        item_name, item_weight, item_value = items[i-1]
        for w in xrange(1, weight + 1):
            if (item_weight > w):
                table[i][w] = table[i-1][w]
            else:
                table[i][w] = max(table[i-1][w], table[i-1][w-item_weight] + item_value)

    result = []
    w = weight
    for i in xrange(len(items), 0, -1):
        if (table[i][w] != table[i-1][w]):
            item_name, item_weight, item_value = items[i-1]
            result.append(items[i-1])
            w -= item_weight
    return result

# Counts the total weight and total value of items to be added
def totalvalue(comb):
    weight_total = value_total = 0
    for item_name, item_weight, item_value in comb:
        weight_total  += item_weight
        value_total += item_value
    return (value_total, weight_total)


'items = ("Item Name", weight, value)'
items = (
    ("Book 1", 20, 150),
    ("Book 2", 20, 100),
    ("Water bottle", 5, 20),
    ("Laptop", 80, 200),
    ("Laptop charger", 10, 70),
    ("Phone charger", 3, 45),
    ("House keys", 3, 200),
    ("Notebook", 15, 70),
    ("Pen and pencil case", 5, 50),
    ("Umbrella", 5, 20),
    ("iPad", 10, 30),
    ("Lecture notes", 10, 50),
    ("Extra Clothings", 10, 25),
    ("Gum", 1, 10),
    ("Hygiene products", 10, 20),
    ("Headphones", 3, 70),
    ("Healthy snacks", 4, 35),
    ("Beer", 2, 40),
    )

