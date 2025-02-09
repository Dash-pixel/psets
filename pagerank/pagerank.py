# prnk 0
import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])


    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.

    if the corpus were {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}
    output = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}
    """
    if len(corpus[page]) == 0:
        common_prob = 1 / len(corpus)
        output = dict()
        for i in corpus.keys():
            output[i] = common_prob
        return output

    common_prob = (1 - damping_factor) / len(corpus)
    link_prob = damping_factor/len(corpus[page])
    output = dict()
    prob_sum = 0
    for i in corpus:
        output[i] = common_prob + ((link_prob) if (i in corpus[page]) else 0)
        #but output sums up to 1 so how does this work ?
        prob_sum += output[i]
    

    for key, value in output.items():
        output[key] = float(value)/float(prob_sum) # ok  why the fuck is the value is a string 

    return output

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    
    class Paired_lists:
        def __init__(self, dictionary):
            self.pages = list(dictionary.keys())
            self.weights = list(dictionary.values())

    # the dict of  original probabilities
    prob_distrib = {}
    for element in corpus:
        prob_distrib[element] = Paired_lists(transition_model(corpus, element, damping_factor))


    page = random.choice(list(corpus.keys()))
    prob_sum = {}
    total = n


    while n > 0: #assume that its more than 0
        prob_sum[page] = (prob_sum[page] + 1/total) if page in prob_sum else 1/total

        page = random.choices(prob_distrib[page].pages, prob_distrib[page].weights)[0]
        n -= 1

    return prob_sum





def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    common_prob = (1 - damping_factor) / len(corpus)
    page_ranks = dict()
    for page in corpus:
        page_ranks[page] = 1/len(corpus)







    while True:
        previous_ranks = copy.deepcopy(page_ranks)





        #corpus is a dict of sets page: set of pages
        for page in corpus.keys(): 
            #going over each page summing up the chanse of going to another page

            sum_prob = 0
            for other_page in corpus.keys(): 

                if not corpus[other_page]: # if other_page has no links
                    sum_prob += previous_ranks[other_page]/len(corpus)
                    print(previous_ranks[other_page]/len(corpus))
                    #using no 
                
                if other_page == page:
                    continue

                if page in corpus[other_page]:
                    sum_prob += previous_ranks[other_page]/len(corpus[other_page])

            page_ranks[page] = common_prob + damping_factor * (sum_prob)






        if all(abs(page_ranks[key] - previous_ranks[key]) <= 0.001 for key in page_ranks):
            break

    print(page_ranks)
    return page_ranks    
    

if __name__ == "__main__":
    #iterate_pagerank({'1': {'2'}, '2': {'3', '1'}, '3': {'5', '4', '2'}, '4': {'1', '2'}, '5': set()}, 0.85)
    main()
