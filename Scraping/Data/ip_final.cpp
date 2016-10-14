#include <bits/stdc++.h>

using namespace std;

map <int,double> Airport;
map <int,double> Altamount,Vashi,Virar;
map <int,int> Mallc;

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

    ifstream Malls ("ShoppingMallCount.txt");

    while(Malls >> id){
        Malls >> d;
        Mallc[id] = d;
        //cout << d << endl;
    }


    ifstream TP("TimevsPrice.txt");
    ofstream IP("ip.txt");
    ofstream TEST("test.txt");


    while(TP >> id){
        TP >> q >> p;
        if(q<27)
            IP << q << " " << Airport[id] << " " << Altamount[id] << " " << Vashi[id] << " " << Virar[id] << " " << Mallc[id] << " "  << p << endl;
        else TEST << q << " " << Airport[id] << " " << Altamount[id] << " " << Vashi[id] << " " << Virar[id]  << " " << Mallc[id] << " " << p << endl;
    }

    return 0;
}
