#first 2 columns are features and last one is the label

training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

#utility functions

#finding unique values in dataset
#0 is the colour, 1 is size and 2 is label

#using set comprehension instead of list; removes duplicates
def unique_values(rows, col):
    return {row[col] for row in rows}

#counting number of labels in dataset
def class_counts(rows):
    counts = {} #empty dictionary "label: count"
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

#checking if value is numeric (int or float)
def is_numeric(value):
    return isinstance(value, (int, float))
