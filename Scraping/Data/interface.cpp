#include <bits/stdc++.h>

using namespace std;

map <int,double> Airport;
map <int,double> Altamount,Vashi,Virar;
map <int,int> Mallc;
map <int, string> names;

vector <pair <int,int>> TP;
vector <double> theta;
double mat[356][6];

int main () {


    int id,q,p,tmat = 1;
    double d;

    ifstream Air ("AirportDistance.txt");
    while(Air >> id){
        Air >> d;
        Airport[id] = d;
        //cout << d << endl;
        mat[id][tmat] = d;
    }

    ifstream Alta ("AltamountDistance.txt");
    tmat++;
    while(Alta >> id){
        Alta >> d;
        Altamount[id] = d;
        //cout << d << endl;
        mat[id][tmat] = d;
    }



    ifstream Vashif ("VashiDistance.txt");
    tmat++;
    while(Vashif >> id){
        Vashif >> d;
        Vashi[id] = d;
        //cout << d << endl;
        mat[id][tmat] = d;
    }

    ifstream Virarf ("VirarDistance.txt");
    tmat++;
    while(Virarf >> id){
        Virarf >> d;
        Virar[id] = d;
        //cout << d << endl;
        mat[id][tmat] = d;
    }

    ifstream Malls ("ShoppingMallCount.txt");
    tmat++;
    while(Malls >> id){
        Malls >> d;
        Mallc[id] = d;
        //cout << d << endl;
        mat[id][tmat] = d;
    }

/*
    ifstream TP("TimevsPrice.txt");
    ofstream IP("ip.txt");
    ofstream TEST("test.txt");


    while(TP >> id){
        TP >> q >> p;
        if(q<27)
            IP << q << " " << Airport[id] << " " << Altamount[id] << " " << Vashi[id] << " " << Virar[id] << " " << Mallc[id] << " "  << p << endl;
        else TEST << q << " " << Airport[id] << " " << Altamount[id] << " " << Vashi[id] << " " << Virar[id]  << " " << Mallc[id] << " " << p << endl;
    }

*/
    ifstream Thf("theta_g.txt");
    double _th;
    while(Thf >> _th){
        theta.push_back(_th);
    }

    ifstream nmf ("id_vs_name.txt");
    string s;
    while(nmf >> id){
        getline(nmf,s);
        names[id] = s;
        cout << id << " " << s << "\n";
    }

    cout << "enter the area id (1-355)\n";
    int ID,time = 30;
    while(ID){
        time = 30;
        cin >> ID;
        cout << "Gradient Descent price estimate for the coming quarters\n";
        while(time<35){
            double ans = theta[0] * time;
            //cout << ans << " ";
            for(int i=1;i<=5;i++){
                ans = ans + mat[ID][i] * theta[i];
                //if(time==30)
                //cout << endl << theta[i] << " " << mat[ID][i] << endl;

            }
            if(ans<5000)
                ans += 2000;
            else if(ans<20000)
                ans += 1000;

            cout << ans<< endl;
            time++;
        }
    }
}
