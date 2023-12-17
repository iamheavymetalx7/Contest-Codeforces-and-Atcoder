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
        int n,q;
        cin>>n>>q;
        vector<set<int>> a(n);
        for(int i=0;i<n;i++)
        {int c;
        cin>>c;
        a[i].insert(c);

        }

        for(int j=0;j<q;j++){
            int x,y;
            cin>>x>>y;
            x--;y--;

            if (a[x].size()<a[y].size()){
                for(auto i: a[x]){
                    a[y].insert(i);
                }
                a[x].clear();
                cout<<a[y].size()<<endl;
            }
            else{
                for(auto i:a[y]){
                    a[x].insert(i);
                }
                a[y].clear();
                cout<<a[x].size()<<endl;
                swap(a[x],a[y]);
            }

        }
    
    
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