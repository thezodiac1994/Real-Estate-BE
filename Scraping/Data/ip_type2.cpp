#include <bits/stdc++.h>

using namespace std;

map <int,double> Airport;
map <int,double> Altamount,Vashi,Virar;
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

    ifstream Vashif ("VashiDistance.txt");

    while(Vashif >> id){
        Vashif >> d;
        Vashi[id] = d;
        //cout << d << endl;
    }

    ifstream Virarf ("VirarDistance.txt");

    while(Virarf >> id){
        Virarf >> d;
        Virar[id] = d;
        //cout << d << endl;
    }


    ifstream TP("TimevsPrice.txt");
    ofstream IP("ip2.txt");
    ofstream TEST("test2.txt");

    int t = 0;
    while(TP >> id){
        TP >> q >> p;
        if(t>300)
            IP << q << " " << Airport[id] << " " << Altamount[id] << " " << Vashi[id] << " " << Virar[id] << " " << p << endl;
        else TEST << q << " " << Airport[id] << " " << Altamount[id] << " " << Vashi[id] << " " << Virar[id]  << " " << p << endl;

        t++;
    }

    return 0;
}
