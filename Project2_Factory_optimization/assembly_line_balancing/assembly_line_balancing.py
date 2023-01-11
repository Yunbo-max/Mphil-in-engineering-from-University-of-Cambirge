import localsolver
import sys


#
# Functions to read the instances
#
def read_elem(filename):
    with open(filename) as f:
        return [str(elem) for elem in f.read().split()]


def read_instance(instance_file):
    file_it = iter(read_elem(instance_file))

    for _ in range(3):
        next(file_it)

    # Read number of tasks
    nb_tasks = int(next(file_it))
    max_nb_stations = nb_tasks
    for _ in range(2):
        next(file_it)

    # Read the cycle time limit
    cycle_time = int(next(file_it))
    for _ in range(5):
        next(file_it)

    # Read the processing times
    processing_time_dict = {}
    for _ in range(nb_tasks):
        task = int(next(file_it)) - 1
        processing_time_dict[task] = int(next(file_it))
    for _ in range(2):
        next(file_it)
    processing_time = [elem[1] for elem in sorted(processing_time_dict.items(),
                                                  key=lambda x: x[0])]

    # Read the successors' relations
    successors = {}
    while True:
        try:
            pred, succ = next(file_it).split(',')
            pred = int(pred) - 1
            succ = int(succ) - 1
            if pred in successors:
                successors[pred].append(succ)
            else:
                successors[pred] = [succ]
        except:
            break
    return nb_tasks, max_nb_stations, cycle_time, processing_time, successors


def main(instance_file, output_file, time_limit):
    nb_tasks, max_nb_stations, cycle_time, processing_time_data, \
        successors_data = read_instance(instance_file)

    with localsolver.LocalSolver() as ls:
        #
        # Declare the optimization model
        #
        model = ls.model

        # Decision variables: station_vars[s] is the set of tasks assigned to station s
        station_vars = [model.set(nb_tasks) for s in range(max_nb_stations)]
        stations = model.array(station_vars)
        model.constraint(model.partition(stations))

        # Objective: nb_used_stations is the total number of used stations
        nb_used_stations = model.sum(
            (model.count(station_vars[s]) > 0) for s in range(max_nb_stations))

        # All stations must respect the cycleTime constraint
        processing_time = model.array(processing_time_data)
        time_lambda = model.lambda_function(lambda i: processing_time[i])
        time_in_station = [model.sum(station_vars[s], time_lambda)
                           for s in range(max_nb_stations)]
        for s in range(max_nb_stations):
            model.constraint(time_in_station[s] <= cycle_time)

        # The stations must respect the succession's order of the tasks
        task_station = [model.find(stations, i) for i in range(nb_tasks)]
        for i in range(nb_tasks):
            if i in successors_data.keys():
                for j in successors_data[i]:
                    model.constraint(task_station[i] <= task_station[j])

        # Minimization of the number of active stations
        model.minimize(nb_used_stations)

        model.close()

        # Parameterize the solver
        ls.param.time_limit = time_limit

        ls.solve()

        # Write the solution in a file following the format:
        # - 1st line: value of the objective
        # - 2nd line: number of tasks
        # - following lines: task's number, station's number
        if output_file is not None:
            with open(output_file, 'w') as f:
                f.write("%d\n" % nb_used_stations.value)
                f.write("%d\n" % nb_tasks)
                for i in range(nb_tasks):
                    f.write("{},{}\n".format(i + 1, task_station[i].value + 1))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python assembly_line_balancing.py instance_file \
            [output_file] [time_limit]")
        sys.exit(1)

    instance_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None
    time_limit = int(sys.argv[3]) if len(sys.argv) >= 4 else 20
    main(instance_file, output_file, time_limit)
