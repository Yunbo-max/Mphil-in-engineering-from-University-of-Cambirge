using System;
using System.IO;
using System.Collections.Generic;
using localsolver;

public class AssemblyLineBalancing : IDisposable
{
    // Data from the problem
    public int nbTasks;
    public int nbMaxStations;
    public int cycleTime;
    public int[] processingTimeData;
    public List<int>[] successorsData;

    // LocalSolver
    LocalSolver localsolver;

    // Decision variables
    LSExpression[] stationVars;

    // Intermediate expressions
    LSExpression[] timeInStation;
    LSExpression[] taskStation;

    // Objective
    LSExpression nbUsedStations;

    public AssemblyLineBalancing()
    {
        localsolver = new LocalSolver();
    }

    public void Dispose()
    {
        if (localsolver != null)
            localsolver.Dispose();
    }

    /* Read instance data */
    void ReadInstance(string fileName)
    {
        using (StreamReader input = new StreamReader(fileName))
        {
            string[] line;
            input.ReadLine();

            // Read number of tasks
            nbTasks = int.Parse(input.ReadLine());
            nbMaxStations = nbTasks;
            processingTimeData = new int[nbTasks];
            successorsData = new List<int>[nbTasks];
            for (int i = 0; i < 2; ++i)
                input.ReadLine();

            // Read the cycle time limit
            cycleTime = int.Parse(input.ReadLine());
            for (int i = 0; i < 6; ++i)
                input.ReadLine();

            // Read the processing times
            for (int i = 0; i < nbTasks; ++i)
            {
                line = input.ReadLine().Split();
                processingTimeData[i] = int.Parse(line[1]);
            }
            for (int i = 0; i < 2; ++i)
                input.ReadLine();

            // Read the successors' relations
            while (true)
            {
                line = input.ReadLine().Split(',');
                if (line[0] == "")
                    break;
                int predecessor = int.Parse(line[0]) - 1;
                int successor = int.Parse(line[1]) - 1;
                if (successorsData[predecessor] == null)
                    successorsData[predecessor] = new List<int>();
                successorsData[predecessor].Add(successor);
            }
        }
    }

    void Solve(int limit)
    {
        // Declare the optimization model
        LSModel model = localsolver.GetModel();

        // Decision variables: stationVars[s] is the set of tasks assigned to station s
        stationVars = new LSExpression[nbMaxStations];
        LSExpression stations = model.Array();
        for (int s = 0; s < nbMaxStations; ++s)
        {
            stationVars[s] = model.Set(nbTasks);
            stations.AddOperand(stationVars[s]);
        }
        model.Constraint(model.Partition(stations));

        // Objective: nbUsedStations is the total number of used stations
        nbUsedStations = model.Sum();
        for (int s = 0; s < nbMaxStations; ++s)
            nbUsedStations.AddOperand(model.Count(stationVars[s]) > 0);

        // All stations must respect the cycleTime constraint
        timeInStation = new LSExpression[nbMaxStations];
        LSExpression processingTime = model.Array(processingTimeData);
        LSExpression timeLambda = model.LambdaFunction(i => processingTime[i]);
        for (int s = 0; s < nbMaxStations; ++s)
        {
            timeInStation[s] = model.Sum(stationVars[s], timeLambda);
            model.Constraint(timeInStation[s] <= cycleTime);
        }

        // The stations must respect the succession's order of the tasks
        taskStation = new LSExpression[nbTasks];
        for (int i = 0; i < nbTasks; ++i)
            taskStation[i] = model.Find(stations, i);
        for (int i = 0; i < nbTasks; ++i)
            if (successorsData[i] != null)
                foreach (int j in successorsData[i])
                    model.Constraint(taskStation[i] <= taskStation[j]);

        // Minimization of the number of active stations
        model.Minimize(nbUsedStations);

        model.Close();

        // Parametrize the solver
        localsolver.GetParam().SetTimeLimit(limit);

        localsolver.Solve();
    }

    /* Write the solution in a file following the format:
    * - 1st line: value of the objective
    * - 2nd line: number of tasks
    * - following lines: task's number, station's number */
    void WriteSolution(string fileName)
    {
        using (StreamWriter output = new StreamWriter(fileName))
        {
            output.WriteLine(nbUsedStations.GetIntValue());
            output.WriteLine(nbTasks);
            for (int i = 0; i < nbTasks; ++i)
            {
                output.Write(i + 1);
                output.Write(',');
                output.WriteLine(taskStation[i].GetIntValue() + 1);
            }
        }
    }

    public static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("Usage: AssemblyLineBalancing inputFile [solFile] [timeLimit]");
            Environment.Exit(1);
        }
        string instanceFile = args[0];
        string outputFile = args.Length > 1 ? args[1] : null;
        string strTimeLimit = args.Length > 2 ? args[2] : "20";
        using (AssemblyLineBalancing model = new AssemblyLineBalancing())
        {
            model.ReadInstance(instanceFile);
            model.Solve(int.Parse(strTimeLimit));
            if (outputFile != null)
                model.WriteSolution(outputFile);
        }
    }
}
