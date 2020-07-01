## KMP_Search.py

## KMP_search class.
## The class pre-process the KMP_pattern index array for searching prefixes.
## KMP pattern searching Time complexity: O (T + P). Space: O (P).
##      T: length of the str text. P: length of the str pattern.

class KMP_search:

    def __init__(self, s_pattern = ""):

        # Initialize the str s and KMP_pattern array.

        self.s              =   s_pattern;
        self.KMP_pattern    =   self.build_KMP_pattern(self.s);

    def build_KMP_pattern(self, word):
        ## Build KMP_pattern array of a string, save it as class variable, and return it.

        self.s = word;        
        ln_word =   len(word);

        pattern =   [0]*ln_word;        # Initialize the KMP_pattern array with 0's.
        i, j = 0, 1;                    # 2 pointers for KMP_pattern. j > i.        

        # Loops to fill in the KMP_pattern array.
        while j< ln_word:
            
            # If prefix and suffix matches, increment both i and j, then update pattern.
            if word[i] == word[j]:
                i+=1;
                pattern[j] =  i;                
                j+=1;

            else:
                # Missmatch characters found. i goes back to previously found prefix index.
                if i == 0:      j += 1;
                else:           i = pattern[i-1];

        # Saves the pattern and returns it.
        self.KMP_pattern = pattern;
        return pattern;

    def KMP_search_index(self, word):
        # Returns the first index of str word where str pattern matches substring of word.
        # Time complexity: O(T + P); T: length of str word. P: length of str pattern.
        # Space complexity: O(P):   P: length of str pattern.

        ln_word =   len(word);
        ln_pat  =   len(self.s);

        i, j = 0, 0;            # 2 pointers: i for word, j for pattern.

        # Loops to find the pattern in str.
        while i< ln_word and j < ln_pat:

            c_word, c_pat = word[i], self.s[j];

            if c_word == c_pat:
                i, j = i+1, j+1;

            else:
                if j == 0:
                    i += 1;
                
                else:
                    j = self.KMP_pattern[j-1];

        if j == ln_pat:     return i - ln_pat;

        else:               return -1;
