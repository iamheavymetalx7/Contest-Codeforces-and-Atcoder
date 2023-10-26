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
int inf = 1000000000000000000;
// using ii = pair<int, int>;

void solve()
{
    int n;
    cin>>n;

    vector<int> a;

    rep(i,0,n){
        int num;
        cin>>num;
        a.push_back(num);
    }
    int curr=a[0];

    rep(i,1,n){
        if (curr!=a[i]){
            cout<<"No"<<endl;
            return;
        }
    }
    cout<<"Yes"<<endl;

}

signed main()
{
    fast
    // int t; cin>>t; while(t--)
    solve();
    return 0;
}