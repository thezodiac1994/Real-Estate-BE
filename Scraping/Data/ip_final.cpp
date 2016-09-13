#include <bits/stdc++.h>

using namespace std;

map <int,double> Airport;
map <int,double> Altamount;
vector <pair <int,int>> TP;

int main () {

    ifstream Alta ("AltamountDistance.txt");
    int id,q,p;
    double d;

    while(Alta >> id){
        Alta >> d;
        Altamount[id] = d;
        //cout << d << endl;
    }

    ifstream Air ("AirportDistance.txt");

    while(Air >> id){
        Air >> d;
        Airport[id] = d;
        //cout << d << endl;
    }

    ifstream TP("TimevsPrice.txt");
    ofstream IP("ip.txt");
    ofstream TEST("test.txt");


    while(TP >> id){
        TP >> q >> p;
        if(q<27)
            IP << q << " " << Airport[id] << " " << Altamount[id] << " " << p << endl;
        else TEST << q << " " << Airport[id] << " " << Altamount[id] << " " << p << endl;
    }

    return 0;
}
