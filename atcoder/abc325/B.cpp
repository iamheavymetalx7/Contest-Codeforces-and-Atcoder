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
    vector<pair<int,int>> vec;

    rep(i,0,n){
    int a,b;
    cin>>a>>b;
    vec.push_back({a,b});
    }

    int ans =0;
    for(int j=0;j<=24;j++){
        int cnt=0;
        for(int x=0;x<n;x++){
            // cout<<vec[x].ff<<" "<<vec[x].ss<<"************"<<endl;
            int curr_time = vec[x].ss+j;
            // cout<<curr_time<<endl;
            curr_time%=24;
            if (curr_time>=9 && curr_time<=17){
                cnt+=vec[x].ff;
            }
        }
        ans = max(ans,cnt);
    }
    cout<<ans;
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