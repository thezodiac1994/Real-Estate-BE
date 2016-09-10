#include <bits/stdc++.h>

using namespace std;

map <string,int> m;

int main () {

    m["Jan-Mar"] = 0;
    m["Apr-Jun"] = 1;
    m["Jul-Sep"] = 2;
    m["Oct-Dec"] = 3;


    freopen("QvsP.txt","r",stdin);
    freopen("id_vs_name.txt","w",stdout);


    int id,tot,vis[1001] = {0};
    string ln,s,q,name;

    while(cin >> id){
        getline(cin,name);
        int hi,lo,med,yr = 0;
        do{
            cin >> lo >> med >> hi >> yr >> q;
            //cout << name << " " << yr << endl;;
            tot = yr - 2009;
            tot = tot * 4 + m[q];
            if(!vis[id]){
                cout << id << " " << name << endl;
                // scanf(" ");
                vis[id] = 1;
           }
        } while(yr!=2016 || m[q]!=1);

    }

}
