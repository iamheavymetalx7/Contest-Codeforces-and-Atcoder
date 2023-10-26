#include <bits/stdc++.h>

using namespace std;
#define int long long
#define pi (3.141592653589)
#define mod 1000000007
#define float double
#define ff first
#define ss second
#define mk make_pair
#define pb push_back
#define rep(i, start, end) for (int i = start; i < end; i++)
#define ld long double
#define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
// int inf = 1000000000000000000;
#define ii = pair<int, int>;

int get_diff(string &a, string &b){

    int len1,len2;
    len1=a.size();
    len2=b.size();
    // cout<<a<<" "<<b<<endl;
    int i=0,j=0;

    if (abs(len1-len2)>1){
        return 10;
    }

    int cnt=0;

    while (i<len1 && j<len2){
        if (a[i]==b[j]){
            i++;
            j++;
            }
        else{
            cnt+=1;
            break;
        }


    }

    // cout<<"before: "<<i<<" "<<j<<endl;



    if (len1==len2){
        i+=1;
        j+=1;
    }
    else if (len1<len2){
        j+=1;
    }
    else{
        i+=1;
    }
    // cout<<"afterwards: "<<i<<" "<<j<<endl;
    for(int k=i;k<len1;k++){

        // cout<<a[k]<<" "<<b[j]<<" "<<k<<" "<<j<<endl;
        if (a[k]!=b[j]){
            cnt++;
            j++;
        }
        else{
            j++;
        }
    }

    // cout<<"the current count is: "<<cnt<<endl;
    // cout<<"************************************"<<endl;
    return cnt;

}

void solve()
{
    int n;
    string s;
    cin>>n>>s;

    vector<int> arr;

    rep(i,0,n){
        string s1;
        cin>>s1;
        // cout<<s1<<endl;
        int val = get_diff(s,s1);
        if (val<=1){
            arr.pb(i+1);
        }
    

    }
    cout<<arr.size()<<endl;
    for (auto x: arr){
        cout<<x<<" ";
    }
    

}

signed main()
{
    fast
    // int t; cin>>t; while(t--)
    solve();
    return 0;
}