"""
Ransom note construction using a hash table.

This module decides whether every character in a ransom note can be taken from
a magazine, using each magazine character at most once. It builds a plain
dictionary of magazine character frequencies, then walks the note and
decrements those counts. A missing or already-used-up character stops the
check immediately.

Run the tests from the repository root with Python 3.8+ and no extra packages:

    python test_ransom_note.py

A successful run ends with the celebration line from the test file. You can
also run:

    python -m pytest test_ransom_note.py
"""


def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    A hash table (plain dict) stores how many times each character appears in
    the magazine. Scanning the ransom note then decrements that count for each
    character used. If a character is absent from the table or its count is
    already zero, the note cannot be built and the function returns False
    immediately, before that count is changed. Only a full scan that never
    hits a missing or depleted character returns True. Characters are compared
    exactly as written, including spaces and punctuation, and the match is
    case-sensitive.

    Time complexity is O(m + n), where m is the length of magazine and n is
    the length of ransomNote. Space complexity is O(k), where k is the number
    of distinct characters in magazine.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # A longer note cannot be assembled from a shorter magazine.
    if len(ransomNote) > len(magazine):
        return False

    # Build a frequency table: one dictionary entry per distinct magazine character.
    letter_counts: dict[str, int] = {}
    for ch in magazine:
        # Hash-table write: increment the stored count for this character.
        letter_counts[ch] = letter_counts.get(ch, 0) + 1

    for ch in ransomNote:
        # Hash-table lookup: missing key or a depleted count means we cannot continue.
        if ch not in letter_counts or letter_counts[ch] == 0:
            return False
        # Hash-table update: consume one available copy of this character.
        letter_counts[ch] -= 1

    return True
