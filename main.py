from plotting import plot_polygons_lines_and_points
from data_client import read_problem_from_json
from GA_helpers import *


site_polygon, building_vector = read_problem_from_json()
max_area = polygon_area(site_polygon)

# Search parameters
population_size = 100
number_of_offspring_each_generation = 10
chance_to_do_crossover = 0.9
mutation_rate = 1 / len(building_vector)  # For uniform mutation
number_of_mutations = 1  # For n-point mutation
generations = 200


# Initialize population
population = [Individual([False] * len(building_vector)) for i in range(population_size)]

for i in range(generations):

    # Generate offspring
    offspring = []
    while len(offspring) < number_of_offspring_each_generation:

        # Parent selection
        [parent1, parent2] = random.sample(population=population, k=2)

        # Crossover
        if random.random() < chance_to_do_crossover:
            new_genome = uniform_crossover(parent1.genome, parent2.genome)
            # new_genome = one_point_crossover(parent1.genome, parent2.genome)
        else:
            new_genome = parent1.genome

        # Mutation
        new_genome = uniform_mutation(new_genome, mutation_rate)
        # new_genome = n_point_mutation(new_genome, number_of_mutations)

        child = Individual(new_genome, solution_score(new_genome, building_vector))
        offspring.append(child)

    # Select survivors
    population.extend(offspring)
    population.sort(key=lambda x: x.fitness, reverse=True)
    del population[population_size:]

    # Print search info
    print("\nGeneration ", i + 1)
    print_fitness_values(population, max_area)


# Print population stats and plot site with buildings from best solution 
print("\nSearch over")
print_fitness_values(population, max_area)

solution_buildings = get_best_solution_buildings(population, building_vector)
plot_polygons_lines_and_points(
    blue_polygons=[b for b in solution_buildings], yellow_polygon=site_polygon
)


# Submit solution to scoreboard
# post_best_solution_to_highscore(population=population, name="example")
