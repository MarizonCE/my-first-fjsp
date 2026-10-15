class GA:
    def __init__(self):
        self.pop_size = 400  # 种群数量
        self.p_c = 0.8  # 交叉概率
        self.p_m = 0.1  # 变异概率
        self.max_gen = 100  # 最大迭代次数

    def fitness(
            self,
            chromosomes: list[list],
            job_operations: dict,
            processing_times,
            machine_count: int,
            chromosome_half_length: int,
    ):
        """
        计算各染色体的适应度值（最大完工时间）
        :param chromosomes: 一批染色体，即生产方案候选解
        :param job_operations: 各工件对应的工序数量
        :param processing_times: 工件各工序在不同机器上的加工时间
        :param machine_count: 机器总数
        :param chromosome_half_length: 染色体前半部分的长度
        :return: 各染色体的适应度值
        """
        fitness_values = []
        for chromosome in chromosomes:
            decoder = Decode(job_operations, processing_times, machine_count)
            fitness_value = decoder.decode(chromosome, chromosome_half_length)
            fitness_values.append(fitness_value)
        return fitness_values

    def machine_crossover(self):
        pass

    def operation_crossover(self):
        pass

    def machine_mutation(self):
        pass

    def operation_mutation(self):
        pass
