import numpy as np


class GeneticAlgorithm:

    def __init__(self, pop_size, chromo_length, pc, pm, term_cri):
        '''
        constructor variable:
            pop_size:       population size
            chromo_length:  length of chromosome
            pc:             probability of performing crossover
            pm:             probability of mutation
            term_cri:       term_crit
        '''
        self.pop_size = pop_size
        self.chromo_length = chromo_length
        self.pc = pc
        self.pm = pm
        self.term_cri = term_cri

        '''
        variable:
            populations:    all chromosome(key) with rank as value
            _surviver:      Final output
        '''
        self.populations = {}
        self._surviver = None

    def initialization():
        # generate chromosome and population accordingly
        for i in range(self.pop_size):
            chromosome = str(np.random.randint(2, size=self.chromo_length))
            while chromosome in self.populations:
                chromosome = str(np.random.randint(2, size=self.chromo_length))
            self.populations[chromosome] = -999

    def fitness_evaluation(self, f):
        # It is quite easy -> avg from CV
        return

    def mutation(self):
        return
