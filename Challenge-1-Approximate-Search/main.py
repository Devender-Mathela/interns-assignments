import os


def levenshtein(s1, s2):
    """Calculate the minimum edit distance between two strings."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )
    return dp[m][n]


def is_subsequence(query, word):
    """Check if all characters of query appear in word in order."""
    it = iter(word)
    return all(char in it for char in query)


def load_words(filename="words.txt"):
    """Read words from a text file and store unique words in memory."""
    # Search in current directory, then script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = filename if os.path.isfile(filename) else os.path.join(script_dir, filename)

    try:
        with open(path, "r", encoding="utf-8") as f:
            # Split by whitespace, convert to lowercase, and remove duplicates
            return list(set(f.read().lower().split()))
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return []


def approximate_search(query, words, k=3):
    """Find the top-k similar words for a given query."""
    query = query.lower()
    matches = []

    for word in words:
        dist = levenshtein(query, word)
        sub = is_subsequence(query, word)

        # Match if query is a subsequence (abbreviation) or has low edit distance (typo)
        if sub or dist <= 2:
            matches.append((sub, dist, len(word), word))

    # Sort: subsequence first, then lowest edit distance, then shortest length
    matches.sort(key=lambda x: (not x[0], x[1], x[2], x[3]))

    return [item[3] for item in matches[:k]]


def main():
    words = load_words("words.txt")
    if not words:
        return

    print("===== APPROXIMATE SEARCH =====")
    print(f"Loaded {len(words)} words into memory.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Input >> ").strip()

        if query.lower() == "exit":
            print("Program terminated.")
            break

        if not query:
            continue

        results = approximate_search(query, words, k=3)

        if results:
            print("Output >>", ", ".join(results))
        else:
            print("Output >> No similar words found.")


if __name__ == "__main__":
    main()
