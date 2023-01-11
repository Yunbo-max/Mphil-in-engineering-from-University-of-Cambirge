#include "localsolver.h"
#include <fstream>
#include <iostream>
#include <vector>

using namespace localsolver;
using namespace std;

class AssemblyLineBalancing {
private:
    // Data from the problem
    int nbTasks;
    int nbMaxStations;
    int cycleTime;
    string tmp;
    vector<int> processingTimeData;
    vector<vector<int>> successorsData;

    // LocalSolver
    LocalSolver localsolver;

    // Decision variables
    vector<LSExpression> stationVars;

    // Intermediate expressions
    vector<LSExpression> timeInStation;
    vector<LSExpression> taskStation;

    // Objective
    LSExpression nbUsedStations;

public:
    /* Read instance data */
    void readInstance(const string& fileName) {
        ifstream infile;
        infile.exceptions(ifstream::failbit | ifstream::badbit);
        infile.open(fileName.c_str());

        for (int i = 0; i < 3; ++i)
            infile >> tmp;

        // Read number of tasks
        infile >> nbTasks;
        nbMaxStations = nbTasks;
        processingTimeData.resize(nbTasks);
        successorsData.resize(nbTasks);
        for (int i = 0; i < 2; ++i)
            infile >> tmp;

        // Read the cycle time limit
        infile >> cycleTime;
        for (int i = 0; i < 5; ++i)
            infile >> tmp;

        // Read the processing times
        for (int i = 0; i < nbTasks; ++i) {
            int task;
            infile >> task;
            infile >> processingTimeData[task - 1];
        }
        for (int i = 0; i < 2; ++i)
            infile >> tmp;

        // Read the successors' relations
        string delimiter = ",";
        while (infile.eof() != true) {
            string relation;
            infile >> relation;
            string predecessor = relation.substr(0, relation.find(delimiter));
            string successor = relation.substr(relation.find(delimiter) + 1, relation.size());
            if (predecessor == relation)
                break;
            successorsData[stoi(predecessor) - 1].push_back(stoi(successor) - 1);
        }
        infile.close();
    }

    void solve(int limit) {
        // Declare the optimization model
        LSModel model = localsolver.getModel();

        // Decision variables: stationVars[s] is the set of tasks assigned to station s
        stationVars.resize(nbMaxStations);
        LSExpression stations = model.array();
        for (int s = 0; s < nbMaxStations; ++s) {
            stationVars[s] = model.setVar(nbTasks);
            stations.addOperand(stationVars[s]);
        }
        model.constraint(model.partition(stations));

        // Objective: nbUsedStations is the total number of used stations
        nbUsedStations = model.sum();
        for (int s = 0; s < nbMaxStations; ++s)
            nbUsedStations.addOperand((model.count(stationVars[s]) > 0));

        // All stations must respect the cycleTime constraint
        timeInStation.resize(nbMaxStations);
        LSExpression processingTime =
            model.array(processingTimeData.begin(), processingTimeData.end());
        LSExpression timeLambda = model.lambdaFunction([&](LSExpression i) { return processingTime[i]; });
        for (int s = 0; s < nbMaxStations; ++s) {
            timeInStation[s] = model.sum(stationVars[s], timeLambda);
            model.constraint(timeInStation[s] <= cycleTime);
        }

        // The stations must respect the succession's order of the tasks
        taskStation.resize(nbTasks);
        for (int i = 0; i < nbTasks; ++i) {
            taskStation[i] = model.find(stations, i);
        }
        for (int i = 0; i < nbTasks; ++i)
            for (int j : successorsData[i])
                model.constraint(taskStation[i] <= taskStation[j]);

        // Minimization of the number of active stations
        model.minimize(nbUsedStations);

        model.close();

        // Parametrize the solver
        localsolver.getParam().setTimeLimit(limit);

        localsolver.solve();
    }

    /* Write the solution in a file following the format:
     * - 1st line: value of the objective
     * - 2nd line: number of tasks
     * - following lines: task's number, station's number */
    void writeSolution(const string& fileName) {
        ofstream outfile;
        outfile.exceptions(ofstream::failbit | ofstream::badbit);
        outfile.open(fileName.c_str());
        outfile << nbUsedStations.getIntValue() << endl;
        outfile << nbTasks << endl;
        for (int i = 0; i < nbTasks; ++i)
            outfile << i + 1 << "," << taskStation[i].getIntValue() + 1 << endl;
    }
};

int main(int argc, char** argv) {
    if (argc < 2) {
        cerr << "Usage: assembly_line_balancing inputFile [outputFile] [timeLimit]" << endl;
        return 1;
    }
    const char* instanceFile = argv[1];
    const char* solFile = argc > 2 ? argv[2] : NULL;
    const char* strTimeLimit = argc > 3 ? argv[3] : "20";
    try {
        AssemblyLineBalancing model;
        model.readInstance(instanceFile);
        model.solve(atoi(strTimeLimit));
        if (solFile != NULL)
            model.writeSolution(solFile);
        return 0;
    } catch (const exception& e) {
        cerr << "An error occurred: " << e.what() << endl;
        return 1;
    }
}
