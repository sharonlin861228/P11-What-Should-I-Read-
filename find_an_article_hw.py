import os
import numpy

def normalize_article(article_path):
    """
    returns a normalized article (see below) as a single string.
    """
    result_str = ""
    with open(article_path, 'r') as f:
        """
        open file to read
        """
        for line in f:
            line = line.strip()
            for word in line.split(" "):
                if word.isalpha():
                    result_str += word.lower() + " "
                else:
                    isFound = False
                    for c in word:
                        if c.isalpha():
                            isFound = True
                            result_str += c.lower()
                    if isFound:
                        result_str += " "
    return result_str

print normalize_article('./silly.txt')


def parse_article(article_path, word_counter):
    """
     updates an already-created dictionary of words and their frequencies from an article.
    """
    na_str = normalize_article(article_path) #updating the frequency table. Returns the frequency table.
    na_str = na_str.strip()
    for word in na_str.split(" "):
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

test_freq = {}
print parse_article('./silly.txt', test_freq)
#print parse_article('./cancer.txt', test_freq)
print test_freq

def parse_query(query):
    """
    given a query like "what is the capital of Wisconsin", generate and return a list of key words.
    """
    qw = ['who', 'what', 'where', 'when', 'why', 'how']
    hv = ['is', 'are', 'do', 'does', 'was', 'were', 'will', 'shall']
    article = ['the', 'a', 'an']
    result = []
    for word in query.split(" "):
        word = word.lower()
        if not(word in qw or word in hv or word in article): # chekc if there are those words inside
            result.append(word)

    return result

print parse_query("Where is Hermione")

def recommend_articles(articles, keywords):
    """
    locates the top 3 articles in the frequency dictionaries with the largest number of keywords, returns their names as a list in descending order.
    """
    appears = []
    articles_list = []
    index = 0
    for key in articles:
        appears.append(0)
        articles_list.append(key)
        for word in keywords:
            if word in articles[key]:
                appears[index] += articles[key][word]
        index += 1

    result = numpy.array(appears).argsort()

    for i in range(len(appears)):
        print "the appears", appears[i], " times in", articles_list[i]
    #print result

    result_list = []
    result_list.append(articles_list[result[-1]])
    result_list.append(articles_list[result[-2]])
    result_list.append(articles_list[result[-3]])

    return result_list

query = "Where is Hermione"
test_dict = {'article1.txt':{'hermione':2,'harry':3,'ron':1},
                 'article2.txt':{'dumbledore':1, 'hermione':3},
                 'article3.txt':{'harry':5}}
print recommend_articles(test_dict, parse_query(query))

def format_article(article_name, output_path, line_width):
    """
    writes the normalized version of the article into the output file, formatted according to line width.
    """
    na_str = normalize_article(article_name)
    na_str = na_str.strip()
    counter = 0;
    result_str = ""

    for word in na_str.split(" "):
        if counter == 0:
            result_str += word
            counter += len(word)
        elif line_width >= counter + len(word):
            result_str += " " + word
            counter += len(word)
        else:
            result_str += "\n" + word
            counter = len(word)

    with open(output_path, 'w') as f:
        f.write(result_str)

print format_article('./silly.txt', './output.txt', 15)

def main():
    """
    get article names once, then repeatedly get queries, destinations, and line widths.
    """
    articles_dict = {}
    articles = raw_input("articles: ")
    for article in articles.split(" "):
        freq_table = {}
        parse_article(article, freq_table)
        articles_dict[article] = freq_table

    while True:
        query = raw_input("query: ")
        topThree = recommend_articles(articles_dict, parse_query(query))

        print "top 3:",
        for item in topThree:
            print item,
        print

        output = raw_input("output file: ")
        #./result.txt
        lw = int(raw_input("line width: "))
        #20
        format_article(topThree[0], output, lw)
        print "written to", output

if __name__ == '__main__':
    main()
