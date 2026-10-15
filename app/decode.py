class Decode:
    def __init__(self, job_operations):
        self.job_operations = job_operations

    def order_matrix(self, machine_selection):
        selected_machines = []  # 各工序选中的机器
        selected_processing_times = []  # 各工序对应的加工时间
        machine_selection_by_job = []  # 按照工件拆分后的机器选择基因
        gene_index = 0

        for operation_count in self.job_operations.values():
            machine_selection_by_job.append(machine_selection[gene_index:gene_index + operation_count])
            gene_index += operation_count

    def earliest_start(self):
        pass

    def decode(self, chromosomes, chromosome_half_length):
        assert len(chromosomes) == 2 * chromosome_half_length, "染色体长度不正确"
        machine_selection = list(chromosomes[:chromosome_half_length])  # 机器选择基因部分
        operation_sequence = list(chromosomes[chromosome_half_length:])  # 工序排序基因部分

        machine_selection_data = self.order_matrix(machine_selection)
