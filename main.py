from app.encode import Encode
from app.ga import GA
from instance import *

if __name__ == "__main__":
    optimal_fitness_value = 9999  # 最佳适应度（初始化）
    optimal_chromosome = 0  # 最佳适应度对应的基因个体（初始化）

    genetic_algorithm = GA()
    encoder = Encode(processing_times, genetic_algorithm.pop_size, job_operation_counts, operation_count, machine_count)
