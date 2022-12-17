#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll t, p, i, j, n, x;
    
    cin>>t;
    
    for(;t--;)
    {
        cin>>n;
        p=0;
        
        
        vector<pair<ll, ll>> a, ans;
        
        for(i=1; i<=n; i++)
        {
            cin>>j;
            a.push_back({j, i});
        }
        
        sort(a.begin(), a.end());
        
        for(i=1; i<n; i++)
        {
            if((a[i].first%a[i-1].first)!=0){
                x=(a[i].first/a[i-1].first+1)*a[i-1].first-a[i].first;
                ans.push_back({a[i].second, x});
                a[i].first+=x;
            }
        }
        
        p=ans.size();
        cout<<p<<"\n";
        for(i=0; i<p; i++){
            cout<<ans[i].first<<" "<<ans[i].second<<"\n";
        }
    }
}