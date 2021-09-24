from string import ascii_letters # in Python 2 one would import letters

class TrieNode:
    def __init__(self): # each node will have
        self.is_word = False # 52 children -
        self.s = {c: None for c in ascii_letters}# most will remain empty

def add(T, w, i=0): # Add a word to the trie
        if T is None:
            T = TrieNode()
        if i == len(w):
            T.is_word = True
        else:
            T.s[w[i]] = add(T.s[w[i]], w, i + 1)
        return T

def Trie(S): # Build the trie for the words in the dictionary S
        T = None
        for w in S:
            T = add(T, w)
        return T

def spell_check(T, w): # Spell check a word against the trie
        assert T is not None
        dist = 0
        while True:
            u = search(T, dist, w)
            if u is not None: # Match at distance dist
                return u
            dist += 1 # No match - try increasing the distance

def search(T, dist, w, i=0):
        if i == len(w):
            if T is not None and T.is_word and dist == 0:
                return ""
            else:
                return None
        if T is None:
            return None
        f = search(T.s[w[i]], dist, w, i + 1) # matching
        if f is not None:
            return w[i] + f
        if dist == 0:
            return None
        for c in ascii_letters:
            f = search(T.s[c], dist - 1, w, i) # insertion
            if f is not None:
                return c+f
            f = search(T.s[c], dist - 1, w, i + 1) # substitution
            if f is not None:
                return c+f
        return search(T, dist - 1, w, i + 1) # deletion
    
T = TrieNode()
trie = Trie(["wait","waiters"])
print(trie)
spell = spell_check(trie,"waiter")
print(spell)