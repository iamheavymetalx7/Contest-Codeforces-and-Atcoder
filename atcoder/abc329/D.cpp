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
        int k,n;
        cin>>k>>n;

        // cout<<k<<" "<<n<<endl;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }

        vector<int> cnt(k+1,0);
        int ans = 0;
        for(int i=0;i<n;i++){
            cnt[arr[i]]++;
            if (cnt[arr[i]]>cnt[ans]){
                ans = arr[i];
            }
            else if(cnt[ans]==cnt[arr[i]]){
                ans = min(ans,arr[i]);
            }
            cout<<ans<<endl;


        }

        // priority_queue<pair<int,int>> pq;
        // unordered_map<int,int> mp;


        // // here pq is max wala, max element at top

        // for(int i=0;i<n;i++){
        //     mp[arr[i]]++;
        //     // cout<<"Pushing: "<<mp[arr[i]]<<" "<<-arr[i]<<endl;
        //     pq.push({mp[arr[i]],-arr[i]});

        //     auto x = pq.top();
        //     // cout<<x.first<<" "<<x.second<<endl;  
        //     cout<<-x.second<<endl;


        // }    

        // while (!pq.empty()){
        //     auto x = pq.top();
        //     pq.pop();
        //     cout<<x.first<<" "<<x.second<<endl;
        // }
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