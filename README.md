# P11-What-Should-I-Read-
CS301-11
Program Skills
Reading and processing text files
Writing text files
Practice with dictionaries
Summary
 There are so many things to read and so little time to read them - creating a program to help you figure out what's relevant to your interests by using key words can at least help reduce the amount of time you waste reading completely irrelevant things.

This week you'll be creating a program to read through a number of files, get a query from the user, and write the most relevant article to a new file.

Program Requirements
You must implement six (6) functions with the following names and behaviors:

normalize_article(article_path) - returns a normalized article (see below) as a single string.
parse_article(article_path, word_counter) - updates an already-created dictionary of words and their frequencies from an article.
parse_query(query) - given a query like "what is the capital of Wisconsin", generate and return a list of key words.
recommend_articles(articles, keywords) - locates the top 3 articles in the frequency dictionaries with the largest number of keywords, returns their names as a list in descending order.
format_article(article_name, output_path, line_width) - writes the normalized version of the article into the output file, formatted according to line width.
main() - get article names once, then repeatedly get queries, destinations, and line widths.
Please write these functions in a file called find_an_article_hw.py.

1. Normalize article
This function expects the path to an existing file, reads its contents, and processes those contents into a single string with only lowercase letters and spaces. (Useful functions: str.isalpha(), str.isspace(), and str.split(). Remember to add spaces between words!)

You will probably want to read in the whole file to one string as it is, then go through that string character by character and concatenate normalized values into a result string.

For example, if my file contentsPreview the document were "I am Lord Voldemort!!111eleven":

>>> print normalize_article('./silly.txt')
i am lord voldemorteleven
You can also try this with our other example files, five articles about various topics that I'll reference in later examples:

bodycams.txtPreview the document
cancer.txtPreview the document
mars.txtPreview the document
sealevel.txtPreview the document
solarpanels.txtPreview the document
These files should go in the same directory as your Python source code. (Again, you won't be able to use repl.it this week - sorry!)

2. Parse article
In order to tell which are the most relevant articles to our search terms, it will be useful to have a dictionary mapping each word that appears in the file to the number of times it occurs. You should do this in the same way that you implemented create_freq_table() last week, but in this case the dictionary is already provided to you and not returned. 

>>> test_freq = {}
>>> print parse_article('./silly.txt', test_freq)
None
>>> print test_freq
{'i': 1, 'lord': 1, 'am': 1, 'voldemorteleven': 1}
3. Parse query
The user can type in a normal English sentence as their query, and we want to parse it down to a list of all-lowercase key words. You may assume that the query will not contain punctuation.

Words you shouldn't include in key words (I'll violate this in a later example, but shhh):

Question words: who, what, where, when, why, how
Helping verbs: is, are, do, does, was, were, will, shall
Articles: the, a, an
So the function should run like this:

>>> print parse_query("Where is Hermione")
['hermione']
4. Recommend articles
This function depends a lot on our internal structure for storing file word frequencies: a nested dictionary. The keys in this dictionary will be the names of the files that we're going to search through, and the values will be the word count dictionaries like the ones we made in the parse_article() function. For example, if our only file were silly.txt, the articles dictionary might look like this:

{'./silly.txt': {'i': 1, 'lord': 1, 'am': 1, 'voldemorteleven': 1}}
You'll want to keep track of which files have had how many instances of the provided search terms. A good way to do this might be to create another dictionary (I know) of the article names as keys and an integer count of number of keyword instances as the value.

Your function should then return the TOP THREE article names in descending order (if there is a tie, you may select in any way you like - we will not test behavior for tied queries):

>>> query = "Where is Hermione"
>>> test_dict = {'article1.txt':{'hermione':2,'harry':3,'ron':1},
                 'article2.txt':{'dumbledore':1, 'hermione':3},
                 'article3.txt':{'harry':5}}
>>> print recommend_articles(test_dict, parse_query(query))
['article2.txt', 'article1.txt', 'article3.txt']
You may find it helpful for debugging purposes to add some extra output temporarily (in this case, articles is the full frequencies dictionary made from all of the example files and is too big to write out as a literal here):

>>> print recommend_articles(articles, ['the'])
  the appears 25 times in ./cancer.txt
  the appears 14 times in ./solarpanels.txt
  the appears 28 times in ./mars.txt
  the appears 70 times in ./bodycams.txt
  the appears 96 times in ./sealevel.txt
['./sealevel.txt','./bodycams.txt','./mars.txt']
5. Format article
This function should take in an article name and write the normalized version of the text from that file to the file specified in the output_path argument. HOWEVER! We also have a specified line width, so that each line of the output file should be no longer than that many characters, without splitting words.

To implement this, use the normalized file text, but split it out by words again - if adding a space and the next word in the file would make the line too long, write the line so far and a newline character to the file and start the next line with the next word. (Hint: before you write a line to a file, it's just a string variable.)

>>> print format_article('./silly.txt', './output.txt', 15)
None
Note: this function returns nothing and writes nothing to the screen! The result of running this function should be a file containing "i am lord \nvoldemorteleven". (Remember \n is the newline character.)

6. Main function
Okay, let's put this all together.

Your main function should prompt the user for article paths, separated by spaces. From this list, it should create the nested articles dictionary as referenced in the Recommend article section above.

Once this is complete, it should repeatedly prompt the user for a query, find the top three files that match that query, and write the top article to a file that the user specifies.

>>> main()
articles: ./bodycams.txt ./cancer.txt ./mars.txt ./sealevel.txt ./solarpanels.txt
query: what level is this
top 3: ./sealevel.txt ./bodycams.txt ./mars.txt
output file: ./result.txt
line width: 20
written to ./result.txt
query:
This program run should result in the normalized version of ./sealevel.txt written to the file ./result.txt with a maximum of 20 characters on each line.

FAQs:
What if a file the user provides doesn't exist? Don't worry about this. If you want to handle it, you may, but we'll only test with files that exist.
What if no files contain the search terms or multiple files contain the same number? Your choice. We won't test tie situations.
What if the doesn't type in filenames? Print the error message "Error, no files provided" and exit the program.
Does the file need to run automatically from the command line? It doesn't need to, but it's always good practice to include the if __name__ == "__main__" check if you do.
Commenting Your Code
Comments are still important this week - the docstrings will be enough for most functions, but your longer functions should still include comments within the code, particularly if you like using very short variable names.

Comment each function using a docstring.
Comment inside your code (like if statements and loops, tell us what variables are for, etc)
Handing In Your Program
Students completing this program in pairs should join a P11 Group. If you are having trouble joining (not creating!) a P11 Group, please contact Hobbes with your partner's name.

When you're done, upload your program in a file called find_an_article_hw.py.
