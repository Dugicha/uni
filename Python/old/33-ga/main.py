import random
# generate population
# repeat
#   run fitness function
#   select fittest
#   reproduce
#   mutate
#   replace old population with new
# until answer not reached
# print final fittest chromosome

POPULATION_SIZE = 100
MAX_GENERATIONS = 500
CHROMOSOME_LENGTH = 300
GENE_LENGTH = 4
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.01

target_number = int(input("input traget number: "))
generation_count = 0

population = []
genes = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "+",
    "1011": "-",
    "1100": "*",
    "1101": "/"
}

def new_individual(chromo):
    return { "chromosome": chromo, "fitness": 0 }

def get_random_chromosome():
    ret = ""
    for i in range(0, int(CHROMOSOME_LENGTH/GENE_LENGTH)):
        ret = ret + random.choice(list(genes.keys()))
    return ret

def decode_chromosome(chromo):
    ret = ""
    for i in range(0, len(chromo), GENE_LENGTH):
        temp = chromo[i : i+GENE_LENGTH]
        ret = ret + genes.get(temp, "")
    return ret

def clean_chromosome(decoded_chromo):
    # enforces int->op->int->op... sequence and removes 0 division
    ret = ""
    # enforce sequence
    temp = ""
    type_number = True
    for i in decoded_chromo:
        if type_number:
            if i != "+" and i != "-" and i != "*" and i != "/":
                temp = temp + i
                type_number = False
        else:
            if i == "+" or i == "-" or i == "*" or i == "/":
                temp = temp + i
                type_number = True
    # remove 0 divisions
    ret = temp.replace("/0", "+0")
    # remove last char if it's an operation
    if ret[-1] == "+" or ret[-1] == "-" or ret[-1] == "/" or ret[-1] == "*":
        ret = ret[0:-1]
    return ret

def get_action(s):
    switcher = {
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y,
        "/": lambda x,y: x/y
    }
    return switcher[s]

def get_answer(chromo):
    buf = int(chromo[0])
    for i in range(1, len(chromo), 2):
        action = get_action(chromo[i])
        buf = action(buf, int(chromo[i+1]))
    return buf

def calculate_fitness(answer, desired_answer):
    if answer == desired_answer:
        return 999.0;
    else:
        return 1 / abs(answer - desired_answer)

# Combines above functions for easier use
def assign_fitness(indiv, desired_answer):
    chromo = indiv["chromosome"]
    decoded = decode_chromosome(chromo)
    cleaned = clean_chromosome(decoded)
    answer = get_answer(cleaned)
    fitness = calculate_fitness(answer, target_number)
    indiv["fitness"] = fitness

def get_fittest_index(pop):
    fittest_index = 0
    fittest_value = pop[0]["fitness"]
    for i in range(1, len(pop)):
        if fittest_value < pop[i]["fitness"]:
            fittest_value = pop[i]["fitness"]
            fittest_index = i
    return fittest_index

def roulette(total_fitness, pop):
    fit_so_far = 0
    arrow = random.random() * total_fitness
    for i in pop:
        fit_so_far += i["fitness"]
        if fit_so_far >= arrow:
            return i["chromosome"]

def crossover(c1, c2):
    if random.random() <= CROSSOVER_RATE:
        crossover_point = random.randint(0, CHROMOSOME_LENGTH)
        ret1 = c1
        ret2 = c2
        temp1 = c1[crossover_point:len(c1)]
        temp2 = c2[crossover_point:len(c2)]
        ret1 = c1[0:crossover_point-1] + temp2
        ret2 = c2[0:crossover_point-1] + temp1
        return (ret1, ret2)
    else:
        return (c1, c2)

def mutate(chromo):
    ret = ""
    for i in range(0, len(chromo)):
        if random.random() <= MUTATION_RATE:
            if chromo[i] == "0":
                ret += "1"
            else:
                ret += "0"
        else:
            ret += chromo[i]
    return ret

def main():
    global generation_count, population
    # Begin cycle of life
    while generation_count < MAX_GENERATIONS:
        print("-"*12)
        print("GENERATION {}".format(generation_count))
        # Assign fitness values
        #print("Assigning fitness values")
        total_fitness = 0
        for i in population:
            assign_fitness(i, target_number)
            total_fitness += i["fitness"]
        # Select fittest
        #print("Selecting chromosomes of the fittest individuals")
        fittest_index = get_fittest_index(population)
        print("Fittest score: {}".format(population[fittest_index]["fitness"]))
        # Check if answer found
        if population[fittest_index]["fitness"] >= 999.0:
            break
        # Repopulate
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            # Roulette selection
            parent1 = roulette(total_fitness, population)
            parent2 = roulette(total_fitness, population)
            # Crossover
            children_chromos = crossover(parent1, parent2)
            # Mutate
            child1 = mutate(children_chromos[0])
            child2 = mutate(children_chromos[1])
            # Birth
            new_population.append(new_individual(child1))
            new_population.append(new_individual(child2))
        population = new_population
        generation_count += 1
    print_answer(population[fittest_index]["chromosome"], generation_count)

def print_answer(chromo, gencount):
    print("="*12)
    print("\nAnswer found in {} generations".format(gencount))
    print("\n----chromosome:----")
    print(chromo)
    print("\n----parsed:----")
    p = clean_chromosome(decode_chromosome(chromo))
    print(p)
    print("\n----answer:----")
    ans = get_answer(p)
    print(ans)
    print("\n----fitness:----")
    fit = calculate_fitness(ans, target_number)
    print(fit)
#####

# Generate random individuals
print("Generating random population")
for i in range(0, POPULATION_SIZE):
    population.append(new_individual(get_random_chromosome()))
main()