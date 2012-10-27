#! /usr/bin/env python
"""
Evolutionary Algorithm for 8 queen problem  

"""
__version__ = '1.0'
__author__ = 'Abhinav Jauhri<abhinavjauhri@gmail.com>'

from random import shuffle, seed, randint, random,  randrange
from itertools import repeat
from sys import argv

mutation_probability = 0.25

class Configuration:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def get_fitness(individual):
    return individual.fitness


def initialize_population(population_size):
    seed()
    pop = []
    items = [1,2,3,4,5,6,7,8]

    for i in range(0,population_size):
        shuffle(items)
        individual_configuration = Configuration(positions = list(items), fitness=0)
        pop.append(individual_configuration)
    return pop

def calculate_fitness(population):
    for i in range(0,len(population)):
        population[i].fitness = 0
        for j in range(0,8):
            for k in range(j+1,8):
                if population[i].positions[j] - population[i].positions[k] in (k-j,j-k):
                    population[i].fitness = population[i].fitness + 1

def recombination(pop):
     for i in range(0, len(pop),2):
         individuals = random_individuals(pop,5)
         crossover_point = randint(0,7)
         child_one_positions = list()
         child_two_positions = list()
         child_one_positions[:crossover_point] = individuals[0].positions[:crossover_point]
         child_two_positions[:crossover_point] = individuals[1].positions[:crossover_point]
         for i in range(crossover_point+1,8):
             if individuals[1].positions[i] not in child_one_positions:
                 child_one_positions.append(individuals[1].positions[i])
             if individuals[0].positions[i] not in child_two_positions:
                 child_two_positions.append(individuals[0].positions[i])
         i = 0
         while len(child_one_positions) < 8:
             if individuals[1].positions[i] not in child_one_positions:
                 child_one_positions.append(individuals[1].positions[i])
             i = i + 1
         i = 0
         while len(child_two_positions) < 8:
             if individuals[0].positions[i] not in child_two_positions:
                 child_two_positions.append(individuals[0].positions[i])
             i = i + 1
         pop[i].positions = child_one_positions
         pop[i+1].positions = child_two_positions
         if random() < mutation_probability:
             mutate(pop[i])
     return pop
             
         
def random_individuals(pop, size):
    individual_indexes = map(lambda x: randrange(0, len(pop)),range(0,size))
    individuals = map(lambda x: pop[x], individual_indexes)
    individuals = sort_by_fitness(individuals)
    return individuals

def mutate(individual):
    pos1 = randint(0,7)
    pos2 = randint(0,7)
    individual.positions[pos1], individual.positions[pos2] = individual.positions[pos2], individual.positions[pos1]

                             
def sort_by_fitness(pop):
    return sorted(pop, key=get_fitness)


def main():
    pop_size = int(argv[1]) 
    population = initialize_population(pop_size)

    generations = 0
    best = Configuration(fitness = 1000)
    while best.fitness is not 0 and generations < 1000:
        calculate_fitness(population)
        population = sort_by_fitness(population)
        best = population[0]
        print best.positions, best.fitness, generations
        recombination(population)
        generations = generations + 1

if __name__ == "__main__":
    main()    
