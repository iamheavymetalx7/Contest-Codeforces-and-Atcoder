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

    void dfs(int node,vector<vector<int>>&adj,vector<int>&vis){
        vis[node]=1;
        for(auto it : adj[node]){
            if (!vis[it]){
                dfs(it,adj,vis);
            }
        }
    }

    bool check(vector<int> & edgeIND,vector<vector<int>>&edges,int n){
        vector<vector<int>> adj(n+1, vector<int>());
        for (auto it: edgeIND){
            auto iter  = edges[it];
            int a=iter[0],b=iter[1],w=iter[2];
            adj[a].pb(b),adj[b].pb(a);
        }        

        int cc=0;
        vector<int> vis(n+1,0);

        for(int i=1;i<=n;i++){
                if(!vis[i]){
                    dfs(i,adj,vis);
                    cc++;
                }
	    }
	
	    return (cc==1);

    }

    void backtrack(int ind,int sum,vector<int>&edgeIND,vector<vector<int>>&edges,int n,int m,int k,int&ans,int picked){
        if (picked>=n) return;

        if (ind>=m){
            /*
            check if valid tree:
            1. if there is only one connected component -> dfs
            2. if there are n-1 edges 
            */

           if (check(edgeIND,edges,n)&&edgeIND.size()==n-1){
            ans = min(ans,sum%k);
           }
           return;
        }

        //pick;
        edgeIND.pb(ind);
        backtrack(ind+1,sum+edges[ind][2],edgeIND,edges,n,m,k,ans,picked+1);
        edgeIND.pop_back();

        //not pick
        backtrack(ind+1,sum,edgeIND,edges,n,m,k,ans,picked);

    }
    void solve()
    {	int n,m,k;
        cin>>n>>m>>k;

        vector<vector<int>> edges;
        for(int i=0;i<m;i++){
            int a,b,c;
            cin>>a>>b>>c;
            edges.pb({a,b,c});

        }
        int ans = 1e18;
        vector<int> edgeIND;
        backtrack(0,0,edgeIND,edges,n,m,k,ans,0);
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