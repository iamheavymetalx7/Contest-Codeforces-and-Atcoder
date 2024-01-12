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
    
    using PII  = array<int,2>;
    void solve()
    {
        int n,q;
        cin>>n>>q;
        int pl=0,pr=0,pu = 0,pd=0;

        deque<PII> pos;    
        
        for(int i=1;i<=n;i++){
        pos.push_back({i,0});
        }
 

        for(int i=0;i<q;i++){
            char o;
            string op;
            cin>>o>>op;
            if (o=='1'){
                int x = pos.front()[0];
                int y = pos.front()[1];
                if (op=="U"){
                    pos.push_front({x,y+1});
                }
                else if (op=="L"){
                    pos.push_front({x-1,y});
                }
                else if (op=="D"){
                    pos.push_front({x,y-1});
                }
                else{
                    pos.push_front({x+1,y});
                }
            }
            else{
                int p =  stoi(op);
                cout<<pos[p-1][0]<<" "<<pos[p-1][1]<<endl;
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