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
        int n;
        cin>>n;
        int modulo = 1e9+7;
        string x1,x2;
        cin>>x1;
        cin>>x2;
        int ans,prev,i;
        if (x1[0]==x2[0]){
            ans =3;
            prev=0;    //vertical
            i=1;
        }
        else{
            ans=6;
            prev=1;
            i=2;   //horizontal
        
        }

        while(i<n){
            if (x1[i]==x2[i]){//vertical
                if (prev==0){//vertical
                    ans*=2;
                }
                prev=0;
                i+=1;
            }
            else{ //horizontal
                if (prev==0){//vertical
                    ans*=2;
                }
                else{//horizontal
                    ans*=3;
                }
                prev=1;
                i+=2;
            }
            ans%=modulo;
        }
        // vector<vector<char>> v(2,vector<char>(n));

        // for(int j=0;j<2;j++){
        //     for(int i=0;i<n;i++){
        //     cin>>v[j][i];
        // }
        // }
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