import sys

from crossword import Variable, Crossword

from collections import Counter

class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]

        
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        self.domains is a dictionary mapping nodes to sets of possible values

        making sure that every value in a variable’s domain has the same number of letters as the variable’s length.
        To remove value x from the domain of a variable v,
        you can call self.domains[v].remove(x).
        """
        for v in self.domains.keys():
            for x in self.domains[v].copy():
                if len(x) != v.length: # here need to find the amount of spaces for variable v
                    self.domains[v].remove(x)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.

        """
        # checks whether there is an overlap place in crossword.overlaps
        flag = False
        if self.crossword.overlaps[x, y]:
            (i, j) = self.crossword.overlaps[x, y]
            y_overlaps = {word[j] for word in self.domains[y]}

            for word in self.domains[x].copy():
                if word[i] not in y_overlaps:
                    self.domains[x].remove(word)
                    flag = True
        # revision made?
        return flag

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # i feel ac3 should have been used with custom arcs passed in as an argument
        # self.crossword.overlaps[x][y] 
        # returns tuple with index where


        if arcs is None:
            arcs = [(x, y) 
                    for x, y in self.crossword.overlaps.keys() 
                    if self.crossword.overlaps[x, y]
                    ]
            #wrong code
        
        while arcs:
            x, y = arcs.pop()
            if self.revise(x, y):
                if self.domains[x] == 0:
                    return False
                else:
                    for i in self.crossword.variables:
                        if i != x and self.crossword.overlaps[x, i]:
                            arcs.append((x, i))

                    #add to arcs all the arcs that intersect with x
        
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # THIS IS INCORRECT - ASSIGNMENT IS dict
        # go over each variable and check whether there is a value 
        for variable in self.crossword.variables:
            #value is a dict isnt it?
            if variable not in assignment:
                return False
        
        return True 

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.


        The consistent function should check to see if a given assignment is consistent.

        An assignment is a dictionary where the keys are Variable objects and the values are strings representing the words those variables will take on.
        Note that the assignment may not be complete: not all variables will necessarily be present in the assignment.
        An assignment is consistent if it satisfies all of the constraints of the problem: 
        all values are distinct, every value is the correct length, 
        and there are no conflicts between neighboring variables.
        The function should return True if the assignment is consistent and return False otherwise.
        """
        # assignment[variable] = 'word'
        # Check if All Assigned Words are Distinct: -- also check whether there is a word with no variable?
        word_set = set()
        for word in assignment.values():
            if word in word_set:
                return False
            else:
                word_set.add(word)


        # Ensure that for every pair of assigned variables that overlap 
        # (i.e., share a position in the crossword), 
        # the letters in the overlapping positions must match.
        #word_set - self.crossword.neighbors(word)
        for x in assignment.keys():
            for y in assignment.keys():
                if x!= y and self.crossword.overlaps[x, y]:
                    (i, j) = self.crossword.overlaps[x, y]
                    if assignment[x][i] is not assignment[y][j]:
                        return False
        return True 
            
    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.

        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        neighbors = self.crossword.neighbors(var)
        this_words =  self.domains[var]
        exclusion_counter = {x:0 for x in this_words}

        for neighbor in neighbors:
            if neighbor in assignment:
                continue
            else:
                i, j = self.crossword.overlaps[var, neighbor]
                neighbor_words = self.domains[neighbor]
                letter_counter = Counter()
                for word in neighbor_words:
                    #counts number of each letter 
                    letter_counter[word[j]] += 1
                
                for word in this_words:
                    exclusion_counter[word] += (len(neighbor_words) - letter_counter[word[i]])
                
        return [x[0] for x in sorted(exclusion_counter.items(), key= lambda x:x[1])]

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain.

        If there is a tie, choose the variable with the highest
        degree. 
        
        If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # could do a tiny class to structure, 
        # but im just making the length the first value in a list

        choise = None

        for key, values in self.domains.items():
            if key in assignment:
                continue

            if not choise:
               choise = [len(values), key]
               continue

            if len(values) < choise[0]:
                choise = [len(values), key]

            elif len(values) == choise[0]:
                choise.append(key)
            
        if len(choise) > 2:
            degree_choise = None
            assignment_set = set(assignment.keys()) 

            for variable in choise[1::]:
                degrees = len(self.crossword.neighbors(variable) - assignment_set)
                if not degree_choise or degrees > degree_choise[0]:
                    degree_choise = (degrees, variable)

            return degree_choise[1]

        elif len(choise) == 2:
            return choise[1]

        return None 

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        
        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                #a specific value should be consistent
                result = self.backtrack(assignment)
                if result:
                    return result
            assignment.pop(var)
        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
