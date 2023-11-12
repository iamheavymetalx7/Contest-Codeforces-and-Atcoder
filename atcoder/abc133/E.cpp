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

    vector<int> g[100100];

    int n,k;
    int dfs(int node, int par){
        
        int curr=k-1;
        if (par){
            curr--;
        }

        if (g[node].size() > k){
            return 0;
        }
        int cnt=1;

        for(auto v:g[node]){
            if (v!=par){

            cnt*=curr;
            cnt%=mod;
            curr--;
            cnt*=dfs(v,node);
            cnt%=mod;}
        }
        return cnt;
    }
    
    void solve()
    {
        cin>>n>>k;

        for (int j=0;j<n-1;j++){
            int a,b;
            cin>>a>>b;
            g[a].pb(b);
            g[b].pb(a);
        }

        cout<<(k*dfs(1,0))%mod<<endl;
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