import pandas as pd
import numpy as np
import csv
import itertools
from sklearn.model_selection import train_test_split


def str_to_int_cleaner(orig_val):
    try:
        val_as_int = int(orig_val)
        return val_as_int
    except ValueError as e:
        return orig_val


def del_unwanted_char(orig_val_param, what_char='"'):
    if isinstance(orig_val_param, str):
        # orig_val = orig_val_param.replace("'", "")
        orig_val = orig_val_param.replace(what_char, "")
        return orig_val

    return orig_val_param


def clean_genres(orig_val):
    easy_replace_list = ["alternative", "blues", "dance", "jazz", "metal", "country", "folk",
                         "rock", "funk", "pop", "hip hop", "soul", "latin", "reggae"]

    for word in easy_replace_list:
        if word in orig_val:
            return word

    if ("electro" in orig_val) or ("trance" in orig_val):
        return "electronic"

    if ("edm" in orig_val) or (orig_val == "disco") or (orig_val == "big room"):
        return "dance"

    if "boy band" in orig_val:
        return "pop"

    if orig_val == "ccm":
        return "christian"

    if "punk" in orig_val or (orig_val == "dutch prog"):
        return "rock"

    if (orig_val == "motown") or (orig_val == "adult standards"):
        return "oldies"

    if "rap" in orig_val:
        return "hip hop"

    return None


spotify_data = pd.read_csv("csv/Spotify-2000.csv")

# apply function to each record, apply to TopGenre column
spotify_data["TopGenre"] = spotify_data["TopGenre"].apply(clean_genres)
spotify_data["Length (Duration)"] = spotify_data["Length (Duration)"].apply(
    del_unwanted_char, args=(','))

# fix characters
spotify_data = spotify_data.applymap(del_unwanted_char)

# remove songs that we were unable to manually narrow down
spotify_data = spotify_data.dropna()
spotify_data = spotify_data.drop(axis=1, columns=['Index'])

spotify_data = spotify_data.applymap(str_to_int_cleaner)

# verify shape
print(spotify_data.shape)

# output to HTML files for presentation and to CSV

spotify_data.head().to_html("html/head.html", index=False)
spotify_data.to_csv("csv/spotify-2000-clean.csv",
                    index=False, quoting=csv.QUOTE_NONNUMERIC)
spotify_data.to_json("json/spotify-2000-clean.json", orient="records")

raise SystemExit  # we will use weka or do training testing as needed
# create training and testing data sets
training_test_list = train_test_split(
    spotify_data, shuffle=True, train_size=0.70, test_size=0.30)

labels = ["train", "test"]
for (dataset, labels) in zip(training_test_list, labels):
    dataset.to_csv(f"csv/spotify-2000-{labels}.csv",
                   index=False, quoting=csv.QUOTE_NONNUMERIC)
