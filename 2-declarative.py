records = [
    {"name": "Amit", "age": 25},
    {"name": "Sita", "age": 30},
    {"name": "Bishal", "age": 22},
]
threshold = 26

"""Rules
Keep only records with age > threshold
Transform each kept record into a formatted string "Name (Age)"
You must not create a new list inside map. Use pure transformation."""

# filter rule
# return True if the data meets the condition age > threshold otherwise return False


def age_threshold(record, threshold):
    return record['age'] > threshold

# transform rule
# transform the filtered record into a string format 'Name (age)' 'Sita (30)'


def transform_record(filtered_record):
    return f'{filtered_record.get("name")} ({filtered_record.get("age")})'

# pipeline rule
# retain records that meet the threshold rule
# transform the retained records based on the transformation rule
# gather the transformed data in a list container


def pipeline(records, threshold):
    return list(map(transform_record, filter(
        lambda record: age_threshold(record, threshold), records)))


r = pipeline(records, threshold)
print(r)
