import string


class Abbreviations:
    def __init__(self):
        self.tree_list = []
        self.name = ""
        self.master = set()
        self.duplicate = set()

    def get_file_name(self):
        self.name = input("Please enter name of text file: ")
        if ".txt" not in self.name:
            self.name = "../data/"+self.name + ".txt"
        else:
            self.name = "../data/"+self.name
        print("File " + self.name + " is now loading...")

    def read_in_file(self):
        self.tree_list = [elt.strip().replace("-,'", " ").title() for elt in open(self.name, "r").readlines()]

    def create_master_set(self):
        temp = {}
        letter1 = ""
        letter2 = ""
        letter3 = ""

        for tree in self.tree_list:
            letter1 = tree[0]
            i = 1
            j = 2
            for i in range(i, len(tree) - 1):
                letter2 = tree[i]
                for j in range(i + 1, len(tree)):
                    letter3 = tree[j]
                    abb = letter1 + letter2 + letter3
                    if abb.isalpha():
                        if abb in self.master:
                            self.duplicate.add(abb)
                        else:
                            self.master.add(abb)


    def create_abbreviation(self):
        temp = {}
        letter1 = ""
        letter2 = ""
        letter3 = ""
        capLetter = 0


        for tree in self.tree_list:
            temp = {}
            word = tree
            capLetter = 0
            letter1 = tree[0]
            tree = tree.replace(" ","")
            print(word)
            i = 1
            j = 2
            for i in range(i, len(tree) - 1):
                letter2 = tree[i]
                if tree[i] == tree[i].upper():
                    capLetter = i
                    #print("CreateAbb CapLetter is: " + str(capLetter))
                for j in range(i + 1, len(tree)):
                    z = capLetter
                    letter3 = tree[j]
                    abb = letter1 + letter2 + letter3
                    if abb.isalpha():
                        if abb not in self.duplicate:
                            self.get_score(abb,tree,i,j,z)
                            v = self.score
                            print("Abb: " + abb.upper() + " : Score: " + str(v))
                            k = abb.upper()

                            temp[k] = v
                            score = 0
                            #print(abb.upper() +" : " + str(self.score))
            print(word)
            print([key + "("+ str(score) +")"for key in temp])



    def get_score(self, abb, word, i, j, z):
        self.score = 0
        a = abb[1]
        b = abb[2]
        i = i
        j = j
        cap = z

        scoreA = i
        scoreB = j

        if a == a.upper():
            self.score += 0
        if b == b.upper():
            self.score += 0
        #if a == a.upper():
         #   self.score +=(0 - scoreB + (scoreB - scoreA))
        if i > cap:
            self.score += (i - cap)#(0 - scoreA + (scoreA - cap))
        if j > cap:
            self.score += (j-cap)#(0 - scoreB + (scoreB - cap))
        if a in "aeiou":
            self.score += 10
        if b in "aeiou":
            self.score += 10

        return self.score

abb = Abbreviations()
abb.get_file_name()
abb.read_in_file()
abb.create_master_set()
abb.create_abbreviation()