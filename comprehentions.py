import pandas

# List Comprehension
listing = ["ahmet", "ferhat", "ali", "smith"]
new_listing = [item + "@hotmail.com" for item in listing if len(item) > 4]
# print(new_listing)

# Dictionary Comprehension
obj = {
    "name": "ferhat",
    "lastname": "add",
    "age": 30
}

new_obj = {key: f"{value}@hotmail.com" for (key, value) in obj.items()}
# print(new_obj)

# data = {
#     "names": ["ferhat", "ahmet", "murat"],
#     "ages": [12, 45, 67]
# }


# pandas_data = pandas.DataFrame(data)

# Loop through a data frame
# for (key, value) in pandas_data.items():
#     print(value)

# for (index, row) in pandas_data.iterrows():
#     print(row.ages)

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_data = {row.letter: row.code for (_, row) in csv_data.iterrows()}


def guess_word():
    try:
        name = input("Give me a word ?")
        new_codes = [new_data[item] for item in name.upper()]
        print(new_codes)
    except KeyError:
        guess_word()


guess_word()
