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
    

    int dp[105][100005];
        vector<int>val(105);
        vector<int>wei(105);

    int recur(int idx, int value_left){
        if (value_left==0) return 0;
        if (idx<0) return 1e15;

        if (dp[idx][value_left]!=-1){
            return dp[idx][value_left];
        }

        int ans = recur(idx-1,value_left);
        if (value_left-val[idx] >=0){

        ans = min(ans,recur(idx-1,value_left-val[idx])+wei[idx]);
        }

        return dp[idx][value_left] =  ans;
    }

    void solve()
    {
        int N,W;
        cin>>N>>W;


        for (int i=0;i<N;i++){
            cin>>wei[i]>>val[i];
        }

        memset(dp,-1,sizeof(dp));

        int maxi =1e5;
        for(int i=maxi;i>=0;i--){
            if(recur(N-1,i)<=W){
                cout<<i<<endl;
                break;
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