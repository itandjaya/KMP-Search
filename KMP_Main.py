## KMP_main.py

from KMP_Search import KMP_search;      #Import KMP_search class.



def main():

    ## Testing the KMP_pattern prefix index array.

    test_patterns = [];
    test_patterns.append(    ['AABAACAABAA', [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]]  );
    test_patterns.append(    ['AAAA', [0, 1, 2, 3]] );
    test_patterns.append(    ['ABCDE', [0, 0, 0, 0, 0]]  );
    test_patterns.append(    ['AAACAAAAAC', [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]]   );
    test_patterns.append(    ['AAABAAA', [0, 1, 2, 0, 1, 2, 3]]  );
    test_patterns.append(    ['ABCDE', [0, 0, 0, 0, 0]]  );
    test_patterns.append(    ['A', [0]]  );
    test_patterns.append(    ['', []]  );

    # Compares the computed KMP_pattern index array with the pre-defined solution.
    for word, pattern in test_patterns:
        kmp_s   =   KMP_search(word);
        assert  kmp_s.KMP_pattern == pattern, 'Missmatch {}: {} || {}'.format(word, kmp_s.KMP_pattern, pattern);



    # Testing string txt with pattern pat. Find index where pat first occured in txt.
    
    pat1        =   "ABABCABAB"; 
    kmp_s1      =   KMP_search(pat1);

    txt1 = "ABABDABACDABABCABAB";
    kmp_search_index1 = kmp_s1.KMP_search_index(txt1);
    assert  kmp_search_index1 == 10,  'Incorrect index found. Text: {}, index: {}'.format(txt1, kmp_search_index1);

    txt1 = "ABABDABACDABABCABAA";
    kmp_search_index1 = kmp_s1.KMP_search_index(txt1);
    assert  kmp_search_index1 == -1,  'Incorrect index found. Text: {}, index: {}'.format(txt1, kmp_search_index1);


    
    pat2        =   "ABC"; 
    kmp_s2      =   KMP_search(pat2);

    txt2 = "ABABDABACDABABCABAB";
    kmp_search_index2 = kmp_s2.KMP_search_index(txt2);
    assert  kmp_search_index2 == 12,  'Incorrect index found. Text: {}, index: {}'.format(txt2, kmp_search_index2);
    
    txt2 = "ABABDABACDABABDABAB";
    kmp_search_index2 = kmp_s2.KMP_search_index(txt2);
    assert  kmp_search_index2 == -1,  'Incorrect index found. Text: {}, index: {}'.format(txt2, kmp_search_index2);

    return 0;


if __name__ == '__main__':      main();