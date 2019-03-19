import random
from polygon_helpers import polygon_area
from polygon_overlapping_area import polygon_intersection_area

NUMERICAL_PRECISION = 1e-10


class Individual:
    def __init__(self, genome, fitness=0):
        self.genome = genome
        self.fitness = fitness


def uniform_mutation(genome, mutation_rate):
    new_genome = [not gene if random.random() < mutation_rate else gene for gene in genome]
    return new_genome


def n_point_mutation(genome, n):
    bit_flip_indices = random.sample(range(len(genome)), n)
    new_genome = [
        not genome[index] if index in bit_flip_indices else genome[index]
        for index in range(len(genome))
    ]
    return new_genome


def uniform_crossover(genome1, genome2):
    new_genome = [
        genome1[index] if random.random() < 0.5 else genome2[index] for index in range(len(genome1))
    ]
    return new_genome


def one_point_crossover(genome1, genome2):
    crossover_index = random.randint(1, len(genome1) - 1)
    new_genome = genome1[:crossover_index] + genome2[crossover_index:]
    return new_genome


def loser_tournament(population, tournament_size):
    # Returns the index of the tournament loser
    contestant_indices = random.sample(range(len(population)), tournament_size)
    contestant_indices.sort(key=lambda index: population[index].fitness)
    return contestant_indices[0]


def simple_tournament(population, tournament_size):
    # Returns a copy of the tournament winner
    contestant_indices = random.sample(range(len(population)), tournament_size)
    contestant_indices.sort(key=lambda index: population[index].fitness, reverse=True)
    return Individual(population[contestant_indices[0]].genome)


def solution_score(genome, building_vector):
    # Calculate the total building footprint area, but return a zero score if solution is infeasible
    included_buildings = []
    for index in range(len(genome)):
        if genome[index]:
            for building in included_buildings:
                if (
                    polygon_intersection_area(building_vector[index]["coordinates"], building)
                    > NUMERICAL_PRECISION
                ):
                    return 0  # Return zero value for infeasible solutions
            included_buildings.append(building_vector[index]["coordinates"])

    return sum([polygon_area(b) for b in included_buildings])


def print_fitness_values(population, max_area):
    fitness_sum = sum([individual.fitness for individual in population])
    best_fitness = max([individual.fitness for individual in population])
    print("Best: \t\t{:.2f}% area coverage".format(100 * (best_fitness / max_area)))
    print(
        "Average: \t{:.2f}% area coverage".format(
            100 * ((fitness_sum / len(population)) / max_area)
        )
    )


def get_best_solution_buildings(population, building_vector):
    # Return the polygons of the buildings included in the best solution
    best_individual = max(population, key=lambda x: x.fitness)
    return [
        building_vector[index]["coordinates"]
        for index in range(len(best_individual.genome))
        if best_individual.genome[index]
    ]

