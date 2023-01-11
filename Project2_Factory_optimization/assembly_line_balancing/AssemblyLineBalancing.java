import java.util.*;
import java.io.*;
import localsolver.*;

public class AssemblyLineBalancing {

    // Data from the problem
    int nbTasks;
    int nbMaxStations;
    int cycleTime;
    int[] processingTimeData;
    ArrayList<ArrayList<Integer>> successorsData;

    // LocalSolver
    private final LocalSolver localsolver;

    // Decision variables
    private LSExpression[] stationVars;

    // Intermediate expressions
    private LSExpression[] timeInStation;
    private LSExpression[] taskStation;

    // Objective
    private LSExpression nbUsedStations;

    private AssemblyLineBalancing(LocalSolver localsolver) {
        this.localsolver = localsolver;
    }

    /* Read instance data */
    private void readInstance(String fileName) throws IOException {
        try (Scanner input = new Scanner(new File(fileName))) {
            input.nextLine();

            // Read number of tasks
            nbTasks = input.nextInt();
            nbMaxStations = nbTasks;
            processingTimeData = new int[nbTasks];
            successorsData = new ArrayList<ArrayList<Integer>>(nbTasks);
            for (int i = 0; i < nbTasks; ++i)
                successorsData.add(i, new ArrayList<Integer>());
            for (int i = 0; i < 3; ++i)
                input.nextLine();

            // Read the cycle time limit
            cycleTime = input.nextInt();
            for (int i = 0; i < 7; ++i)
                input.nextLine();

            // Read the processing times
            for (int i = 0; i < nbTasks; ++i)
                processingTimeData[input.nextInt() - 1] = input.nextInt();
            for (int i = 0; i < 3; ++i)
                input.nextLine();

            // Read the successors' relations
            String line = input.nextLine();
            while (!line.isEmpty()) {
                String lineSplit[] = line.split(",");
                int predecessor = Integer.parseInt(lineSplit[0]) - 1;
                int successor = Integer.parseInt(lineSplit[1]) - 1;
                successorsData.get(predecessor).add(successor);
                line = input.nextLine();
            }
        }
    }

    private void solve(int limit) {
        // Declare the optimization model
        LSModel model = localsolver.getModel();

        // Decision variables: stationVars[s] is the set of tasks assigned to station s
        stationVars = new LSExpression[nbMaxStations];
        LSExpression stations = model.array();
        for (int s = 0; s < nbMaxStations; ++s) {
            stationVars[s] = model.setVar(nbTasks);
            stations.addOperand(stationVars[s]);
        }
        model.constraint(model.partition(stations));

        // Objective: nbUsedStations is the total number of used stations
        nbUsedStations = model.sum();
        for (int s = 0; s < nbMaxStations; ++s) {
            nbUsedStations.addOperand(model.gt(model.count(stationVars[s]), 0));
        }

        // All stations must respect the cycleTime constraint
        timeInStation = new LSExpression[nbMaxStations];
        LSExpression processingTime = model.array(processingTimeData);
        LSExpression timeLambda = model.lambdaFunction(i -> model.at(processingTime, i));
        for (int s = 0; s < nbMaxStations; ++s) {
            timeInStation[s] = model.sum(stationVars[s], timeLambda);
            model.constraint(model.leq(timeInStation[s], cycleTime));
        }

        // The stations must respect the succession's order of the tasks
        taskStation = new LSExpression[nbTasks];
        for (int i = 0; i < nbTasks; ++i) {
            taskStation[i] = model.find(stations, i);
        }
        for (int i = 0; i < nbTasks; ++i) {
            ArrayList<Integer> successors_i = successorsData.get(i);
            for (int j : successors_i) {
                model.constraint(model.leq(taskStation[i], taskStation[j]));
            }
        }

        // Minimization of the number of active stations
        model.minimize(nbUsedStations);

        model.close();

        // Parametrize the solver
        localsolver.getParam().setTimeLimit(limit);

        localsolver.solve();
    }

    /*
     * Write the solution in a file following the format:
     * - 1st line: value of the objective
     * - 2nd line: number of tasks
     * - following lines: task's number, station's number
     */
    void writeSolution(String fileName) throws IOException {
        try (PrintWriter output = new PrintWriter(new FileWriter(fileName))) {
            output.println(nbUsedStations.getIntValue());
            output.println(nbTasks);
            for (int i = 0; i < nbTasks; ++i) {
                output.print(i + 1);
                output.print(",");
                output.println(taskStation[i].getIntValue() + 1);
            }
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: AssemblyLineBalancing inputFile [outputFile] [timeLimit]");
            System.exit(1);
        }

        String instanceFile = args[0];
        String outputFile = args.length > 1 ? args[1] : null;
        String strTimeLimit = args.length > 2 ? args[2] : "20";
        try (LocalSolver localsolver = new LocalSolver()) {
            AssemblyLineBalancing model = new AssemblyLineBalancing(localsolver);
            model.readInstance(instanceFile);
            model.solve(Integer.parseInt(strTimeLimit));
            if (outputFile != null)
                model.writeSolution(outputFile);
        } catch (Exception ex) {
            System.err.println(ex);
            ex.printStackTrace();
            System.exit(1);
        }
    }
}
