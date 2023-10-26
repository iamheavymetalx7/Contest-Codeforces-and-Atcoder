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

    while(n%2==0){
        n/=2;
    }

    while(n%3==0){
        n/=3;
    }

    if(n==1){
        cout<<"Yes";
    }
    else{cout<<"No";}

    

}

signed main()
{
    fast
    // int t; cin>>t; while(t--)
    solve();
    return 0;
}