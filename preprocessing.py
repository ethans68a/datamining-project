import pandas as pd

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

    if orig_val == "motown" or orig_val == "adult standards":
        return "oldies"

    return None


spotify_data = pd.read_csv("Spotify-2000.csv")
# print(spotify_data["TopGenre"])
print(len(pd.unique(spotify_data["TopGenre"])))
pd.DataFrame(pd.unique(spotify_data["TopGenre"])).to_html("html/unique-genres.html",index=False)

spotify_data["TopGenre"] = spotify_data["TopGenre"].apply(clean_genres)
print(spotify_data["TopGenre"])
print(len(pd.unique(spotify_data["TopGenre"])))

spotify_data.head().to_html("html/head.html",index=False)
spotify_data.to_csv("spotify-2000-clean.csv", index=False)
