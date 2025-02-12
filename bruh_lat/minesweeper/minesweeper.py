import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()


    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells) # what is this self.cells? why is this?
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"


    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        return self.cells & MinesweeperAI.mines
    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        return self.cells & MinesweeperAI.safes
    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """
    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

        self.duplicate_knowledge = set()

        self.moves = set(self.create_moves())

    def __str__(self):
        string = "Knowledge ["
        for sentence in self.knowledge:
            string += str(sentence) + ", "

        # Remove the last comma and space, then close the bracket
        string = string.rstrip(", ") + "]"
        return string if self.knowledge else ""

    def to_set(self):
        tuple_set = set()
        for sentence in self.knowledge:
            tuple_set.add((tuple(sentence.cells), sentence.count))
        self.duplicate_knowledge = tuple_set

    def create_moves(self):
        return {(row, col) for row in range(self.height) for col in range(self.width)}

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """

        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def resolve_check(self):
        flag = False

        for sentence in self.knowledge.copy():
            if sentence.count == 0:
                for cell in sentence.cells.copy():
                    self.mark_safe(cell)
                    flag = True

            elif sentence.count == len(sentence.cells):
                for cell in sentence.cells.copy():
                    self.mark_mine(cell)
                    flag = True

        # if my sentence will be equal to len == 0 am i going to update it or not?

        return flag

    def sub_check(self):

        flag = False
        to_check = self.knowledge.copy()
        self.to_set()

        #unreadable code
        def add_to_check(sentence, new_sentence):
            created_sentence = Sentence(new_sentence.cells - sentence.cells, new_sentence.count - sentence.count)

            #is this logical condition though?

            #if ((tuple(created_sentence.cells), created_sentence.count)) not in self.duplicate_knowledge:

                #self.duplicate_knowledge.add((tuple(created_sentence.cells), created_sentence.count))
            self.knowledge.append(created_sentence)
            to_check.append(created_sentence)
            return True



        while to_check:
            new_sentence = to_check.pop()
            if not new_sentence.cells:
                continue

            for sentence in self.knowledge:
                if not sentence.cells or (sentence == new_sentence):
                    continue

                if new_sentence.cells.issubset(sentence.cells):
                    if add_to_check(new_sentence, sentence):
                        flag = True

                if sentence.cells.issubset(new_sentence.cells):
                    if add_to_check(sentence, new_sentence):
                        flag = True

        return flag

    def checking(self):

        while self.resolve_check() or self.sub_check(): # we are only checking with one sentence and not with every sentence
            #can be improved by making set more interesting
            self.knowledge = [i for i in self.knowledge if i.cells]


    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            4) mark any additional cells as safe or as mines
            if it can be concluded based on the AI's knowledge base

            5) add any new sentences to the AI's knowledge base
            if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)
        x, y = cell
        sentence = Sentence(count=count, cells=set())
        for i in range(-1, 2):
            if 0 <= x + i < self.width:
                for j in range(-1, 2):
                    if 0 <= y + j < self.height:
                        if (i+x, j+y) in self.mines:
                            sentence.count -= 1
                        if (i+x, j+y) not in self.safes and (i+x, j+y) not in self.mines:
                            sentence.cells.add((i+x, j+y))

        # bug found -- im not minusing the mines from the count, but im skipping them!!!

        #if sentence.cells and ((tuple(sentence.cells), sentence.count) not in self.duplicate_knowledge):
        #self.duplicate_knowledge.add(tuple(sentence.cells))
        self.knowledge.append(sentence)
        self.checking()

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        q = self.safes - self.moves_made

        if q:

            return random.choice(list(q))
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """


        """
        ratio = 1
        if len(self.knowledge) > 4:
            for sentence in self.knowledge:

                if sentence.cells and sentence.count/len(sentence.cells) < ratio:
                    ratio = sentence.count/len(sentence.cells)
                    safest = sentence

            return random.choice(list(safest.cells))

        else:"""
        moves = list((self.moves - self.mines) - self.moves_made)
        if moves:
            return random.choice(moves)
