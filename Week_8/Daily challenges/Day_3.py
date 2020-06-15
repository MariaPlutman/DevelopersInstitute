import random


class Gene:
    def __init__(self):
        self.value = 0

    def flip(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0


class Chromosome:
    def __init__(self):
        self.genes = []
        for i in range(10):
            self.genes.append(Gene())

    def mutate(self):
        for gene in self.genes:
            if random.randint(0, 2) == 1:
                gene.flip()


class DNA:
    def __init__(self):
        self.chromosomes = []
        for i in range(10):
            self.chromosomes.append(Chromosome())

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.randint(0, 2) == 1:
                chromosome.flip()


class Organism:
    def __init__(self, dna, environement):
        self.dna = dna
        self.environement = environement

    def only_ones(self):
        for chromosome in self.dna.chromosomes:
            for gene in chromosome.genes:
                if gene.value == 0:
                    return False
        return True

    def mutate(self):
        if random.random() <= self.environement:
            self.dna.mutate()


organisms = [
    Organism(DNA(), 0.5),
    Organism(DNA(), 0.8),
    Organism(DNA(), 0.2)
]

gen_ix = 0
while True:
    for org in organisms:
        org.mutate()
        if org.only_ones():
            print("Only ones reached in {} generations".format(gen_ix))
    gen_ix
