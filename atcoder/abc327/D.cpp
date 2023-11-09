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
    {	int n,m;
        cin >>n>>m;
        vector<vector<int>> g(n);
        vector<int> a(m),b(m);
        for (int i=0;i<m;i++) cin>>a[i], a[i]--;

        for (int i=0;i<m;i++) cin>>b[i],b[i]--;

        for(int i=0;i<m;i++){
            g[a[i]].pb(b[i]);
            g[b[i]].pb(a[i]);
        }

        // for(int i=0;i<n;i++){
        //     for(int j=0;j<g[i].size();j++){
        //         cout<<g[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }

        

        vector<int> color(n,-1);

        queue<int> q;

        bool bipartite = true;

        for(int i=0;i<n;i++){
            if (color[i]==-1){
                q.push(i);
                color[i]=0;
                while (!q.empty()){
                    auto node = q.front();q.pop();

                    for (auto nei: g[node]){
                        if (color[nei]==-1){
                            color[nei]=1-color[node];
                            q.push(nei);
                        }
                        else{
                            if (color[nei]==color[node]) bipartite=false;
                        }
                    }
                }
            }
        }

        // for(int i=0;i<n;i++){
        //     cout<<color[i]<<" ";
        // }
        // cout<<endl;

        if (bipartite){cout<<"Yes"<<endl;}
        else cout<<"No"<<endl;



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