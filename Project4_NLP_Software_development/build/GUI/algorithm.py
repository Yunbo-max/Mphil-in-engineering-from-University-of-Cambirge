# -*- coding = utf-8 -*-
# @time:20/03/2023 09:42
# Author:Yunbo Long
# @File:integration.py
# @Software:PyCharm
import pandas as pd
import time
import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from collections import Counter
from nltk.corpus import stopwords
# extended library
from nltk.collocations import *
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import FreqDist

# Algorithm Implementation
def keywords_extraction(file1,file2,file3):
    # Read the tables
    comment_excel = file1
    takt_excel = file2
    fault_description = file3


    # Filter the dataframe to find rows where the 'property' column contains 'comment'
    filtered_df = comment_excel[comment_excel['property'].str.contains('comment')]

    # Print the filtered dataframe

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    print(filtered_df.head(30))


    # XLOOKUP function
    def xlookup(search_value, search_range, return_range, default_value=None):
        """
        Returns the value from the return_range corresponding to the first match found in the search_range.
        If no match is found, the default_value is returned (if specified).
        """
        for i in range(len(search_range)):
            if search_value == search_range[i]:
                return return_range[i]
        return default_value

    # The first task to associate the comments with deviation

    count = 0
    lookup_array = takt_excel['deviation'].tolist()
    return_array = takt_excel['takt'].tolist()
    comment_final = pd.DataFrame()
    comment_final['deviation']=filtered_df['deviation']
    comment_final['comment']=filtered_df['new_value']
    comment_final['takt']=0

    for i in comment_final['deviation']:
        lookup_value = i
        result = xlookup(lookup_value, lookup_array, return_array)
        comment_final.iloc[count,2]=result
        count = count + 1

    lookup_array2 = fault_description['CCC No.'].tolist()
    return_array2 = fault_description['Reported Fault Description'].tolist()
    count = 0
    comment_final['Fault Description']=0
    for j in comment_final['deviation']:
        lookup_value = j
        result = xlookup(lookup_value, lookup_array2, return_array2)
        comment_final.iloc[count,3]=result
        count = count + 1

    # The second task to associate the Part number with deviation
    lookup_array3 = fault_description['CCC No.'].tolist()
    return_array3 = fault_description['Part Number'].tolist()
    count = 0
    comment_final['Part number']=0

    print(comment_final)
    for k in comment_final['deviation']:
        lookup_value = k
        result = xlookup(lookup_value, lookup_array3, return_array3)
        comment_final.iloc[count,4]=result
        count = count + 1

    #  Create the final table
    data8 = pd.DataFrame()
    data8= fault_description['Part Number'].value_counts().reset_index()
    # rename the columns
    data8.columns = ['part number', 'count']

    # The final input text
    Data_comments = comment_final
    Data_number = data8
    print(Data_number)
    print(Data_number.iloc[0,0])

    a = ''
    b = ''
    # Distribute the comments into groups according to diverse Part Number value
    data2= pd.DataFrame()
    for k in range(Data_number.shape[0]):
        a = ''
        b = ''
        for j in range(Data_comments.shape[0]):

            if Data_comments.iloc[j, 4] == str(Data_number.iloc[k,0]):
                word = Data_comments.iloc[j, 1]
                # print(word)
                word = str(word)
                word = word.replace(r'\n', ', ').replace('=', ' ').replace('[', ' ').replace(']', ' ').replace('%', ' ').replace("\\",' ').replace(".",' ').replace("-",' ')

                a = a+word

                if Data_comments.iloc[j, 3] is not None:
                    if j >0 and Data_comments.iloc[j, 3]!=Data_comments.iloc[j-1, 3]:

                        word1 = Data_comments.iloc[j, 3]
                        word1 = str(word1)
                        word1 = word1.replace(r'\n', ', ').replace('=', ' ').replace('[', ' ').replace(']', ' ').replace('%', ' ').replace(".",' ').replace("\\",' ').replace("-",' ')

                        b = b +'. '+ word1

        # Show the task number in programming
        print(k)
        text = a + b

        # Tokenize the text into words
        words = nltk.word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        # stemmer = PorterStemmer()
        # words = [stemmer.stem(word.lower()) for word in words if word.isalpha() not in stop_words]
        words = [word.lower() for word in words if word.isalpha() not in stop_words]

        # Identify the part of speech for each word
        pos_tags = nltk.pos_tag(words)

        # Extract all two-word and three-word phrases that consist of adjectives or nouns
        phrases = []
        for i in range(len(pos_tags) - 2):
            if pos_tags[i][1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS'] and pos_tags[i + 1][1] in ['JJ', 'JJR', 'JJS', 'NN',
                                                                                              'NNS'] and pos_tags[i + 2][
                1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS']:
                phrase = pos_tags[i][0] + ' ' + pos_tags[i + 1][0] + ' ' + pos_tags[i + 2][0]
                phrases.append(phrase)
            elif pos_tags[i][1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS'] and pos_tags[i + 1][1] in ['JJ', 'JJR', 'JJS', 'NN',
                                                                                                'NNS']:
                phrase = pos_tags[i][0] + ' ' + pos_tags[i + 1][0]
                phrases.append(phrase)

        # Count the occurrences of each phrase
        phrase_counts = Counter(phrases)

        # Print the phrases that appear more than once
        for phrase, count in phrase_counts.items():
            if count > 0:
                print(phrase, count)

        # The final table output
        data1 = pd.DataFrame()
        data1 = pd.DataFrame(list(phrase_counts.items()))
        print(data1)
        data1['Part Number'] = str(Data_number.iloc[k, 0])
        data2 = pd.concat([data2,data1])
        print(data2)

    return data2
