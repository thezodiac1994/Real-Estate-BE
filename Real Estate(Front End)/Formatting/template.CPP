#include <bits/stdc++.h>
#define LL long long int
#define mod 1000000007
using namespace std;


map <int,string> Name;
map <int,vector <pair <double,double>>> Values;

int main () {

    ifstream QP("QvsP.txt");
    ifstream P("prediction.txt");
    ifstream IN("id_vs_name.txt");

    ifstream TP("TimevsPrice.txt");
    ofstream OP("out.txt");

    int id;
    double q,p;
    while(TP >> id){
        TP >> q >> p;
        Values[id].push_back(make_pair(q,p));
    }

    string nm;
    while(IN >> id){
        getline(IN,nm);
 //       IN >> nm;
        while(nm[0]==' ')
            nm = nm.substr(1,nm.length());

        Name[id] = nm;
    }

    id = 2;
    double pr1,pr2;
    while(id<=355){
        P >> pr1 >> pr2;
        Values[id].push_back(make_pair(30,pr1));
        Values[id].push_back(make_pair(31,pr2));
        id++;
    }

    for(int i=1;i<=355;i++){

        if(i>=2) OP << "else ";

        OP << "if(area_name== \"" << Name[i] << "\"){\n\tvar yaxis=[";
        for(int j=0;j<Values[i].size();j++){
            OP << Values[i][j].second;
            if(j!=Values[i].size()-1)
                OP << ",";
            else OP << "];";
        }

        OP << "\n\tvar xaxis=[,";
        for(int j=0;j<Values[i].size();j++){
            OP << Values[i][j].first;
            if(j!=Values[i].size()-1)
                OP << ",";
            else OP << "];\n";
        }

        OP << "}\n";

    }





}
