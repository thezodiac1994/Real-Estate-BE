#include <bits/stdc++.h>

using namespace std;

map <string,int> m;

int main () {

    m["Jan-Mar"] = 0;
    m["Apr-Jun"] = 1;
    m["Jul-Sep"] = 2;
    m["Oct-Dec"] = 3;


    freopen("QvsP.txt","r",stdin);
    freopen("QvsP_f.txt","w",stdout);


    string ln,s,q;
    int tot = 0,t = 33;
    //cin >> t;

    while(t--){
        while(getline(cin,s)){
            cout << s << endl;
            int hi,lo,med,yr;
            cin >> lo >> med >> hi >> yr >> q;
            tot = yr - 2009;
            tot = tot * 4 + m[q];
            cout << tot << " " << med << endl;
            //scanf(" ");
        }
        cin >> s >> s;
        scanf(" ");
    }

}
