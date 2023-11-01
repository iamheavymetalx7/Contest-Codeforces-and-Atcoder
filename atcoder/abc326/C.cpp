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
using ii = pair<int, int>;

void solve()
{

    int n,m;
    cin>>n>>m;
    vector<int> vec(n);
    for(int i=0;i<n;i++)
    {cin>>vec[i];
    }
    sort(vec.begin(),vec.end());


    int j=0;
    int ans=0;

    for(int i=0;i<n;i++){
        while (j<n && vec[j]<(vec[i]+m)){
            j++;
        }
        ans = max(ans,j-i);
    }
    
    cout<<ans<<endl;
    

}

signed main()
{
    fast
    // int t; cin>>t; while(t--)

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    solve();
    return 0;
}