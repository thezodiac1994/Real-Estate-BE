#include <bits/stdc++.h>

using namespace std;

map <int,double> Airport;
map <int,double> Altamount,Vashi,Virar;
map <int,int> Mallc,Hospc;

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
    ifstream Hosp ("HospitalCount.txt");

    while(Hosp >> id){
        Hosp >> d;
        Hospc[id] = d;
        //cout << d << endl;
    }

    ifstream TP("TimevsPrice.txt");
    ofstream TEST("ftest.txt");
    ofstream FT("fto.txt");

    TEST << "Bias,Time,Airport,Altamount,Vashi,Virar,Mallc,Hospc" <<  endl;
    FT << "OUT" << endl;

    while(TP >> id){
        TP >> q >> p;

        if(q==29){
            TEST << "1," << q+1 << "," << Airport[id] << "," << Altamount[id] << "," << Vashi[id] << "," << Virar[id] << "," << Mallc[id] << "," << Hospc[id] <<  endl;
           // TEST << q+2 << "," << Airport[id] << "," << Altamount[id] << "," << Vashi[id] << "," << Virar[id] << "," << Mallc[id] << "," << Hospc[id] <<  endl;
            // TEST << q+3 << "," << Airport[id] << "," << Altamount[id] << "," << Vashi[id] << "," << Virar[id] << "," << Mallc[id] << "," << Hospc[id] <<  endl;
            FT << p << endl;
        }
    }

    return 0;
}
