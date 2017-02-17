#include <bits/stdc++.h>

using namespace std;

map <string,int> m;

int main () {

    m["Jan-Mar"] = 0;
    m["Apr-Jun"] = 1;
    m["Jul-Sep"] = 2;
    m["Oct-Dec"] = 3;


    freopen("QvsP.txt","r",stdin);
    freopen("timevsprice.txt","w",stdout);


    int id,tot;
    string ln,s,q,name;

    while(cin >> id){
        getline(cin,name);
        int hi,lo,med,yr = 0;
        do{
            cin >> lo >> med >> hi >> yr >> q;
            //cout << name << " " << yr << endl;;
            tot = yr - 2009;
            tot = tot * 4 + m[q];
            cout << id << " " << tot << " " << med  << endl;
           // scanf(" ");
        } while(yr!=2016 || m[q]!=1);

    }

}
