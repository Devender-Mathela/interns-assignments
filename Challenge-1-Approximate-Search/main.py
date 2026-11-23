
from difflib import get_close_matches

with open("words.txt", "r") as file:
    words = file.read().lower().split()

print("===== APPROXIMATE WORD SEARCH =====")

while True:
    query = input("\nEnter word (exit to quit): ").lower().strip()

    if query == "exit":
        break

    matches = get_close_matches(query, words, n=3, cutoff=0.5)

    if matches:
        print("Results:", ", ".join(matches))
    else:
        print("No matching words found.")
