class Solution {
#define ll long long
private:
    ll minarea(vector<vector<int>>& grid,ll rowstart,ll rowend,ll colstart,ll colend) {       
        ll minirow = 1e9, maxirow = -1e9;
        ll minicol = 1e9, maxicol = -1e9;
        
        for (ll i = rowstart; i <= rowend; i++) {
            for (ll j = colstart; j <= colend; j++) {
                if (grid[i][j] == 1) {
                    minirow = min(minirow, i);
                    maxirow = max(maxirow, i);
                    minicol = min(minicol, j);
                    maxicol = max(maxicol, j);
                }
            }
        }
        
        ll h = maxirow - minirow + 1;
        ll w = maxicol - minicol + 1;
        
        return h * w;
    }
public:
    long long minimumSum(vector<vector<int>>& grid) {
        ll n = grid.size();
        ll m = grid[0].size();
        
        ll ans = 1e9;
        
        /*
        _________
        |       |
        |_______|
        |   |   |
        |   |   |
        ---------
        */

        for(ll i=0;i<n;i++)
        {
            ll first = minarea(grid,0,i,0,m-1);
            for(ll j=0;j<m;j++)
            {
                ll second = minarea(grid,i+1,n-1,0,j);
                ll third = minarea(grid,i+1,n-1,j+1,m-1);
                ans = min(ans,first+second+third);
            }
        }

        for(ll i=n-1;i>=0;i--)
        {
            ll first = minarea(grid,i,n-1,0,m-1);
            for(ll j=0;j<m;j++)
            {
                ll second = minarea(grid,0,i-1,0,j);
                ll third = minarea(grid,0,i-1,j+1,m-1);
                ans = min(ans,first+second+third);
            }
        }

        for(ll j=0;j<m;j++)
        {
            ll first = minarea(grid,0,n-1,0,j);
            for(ll i=0;i<n;i++)
            {
                ll second = minarea(grid,0,i,j+1,m-1);
                ll third = minarea(grid,i+1,n-1,j+1,m-1);
                ans = min(ans,first+second+third);
            }
        }

        for(ll j=m-1;j>=0;j--)
        {
            ll first = minarea(grid,0,n-1,j,m-1);
            for(ll i=0;i<n;i++)
            {
                ll second = minarea(grid,0,i,0,j-1);
                ll third = minarea(grid,i+1,n-1,0,j-1);
                ans = min(ans,first+second+third);
            }
        }

        for(ll i=0;i<m;i++)
        {
            for(ll j=i+1;j<m;j++)
            {
                ll first = minarea(grid,0,n-1,0,i);
                ll second = minarea(grid,0,n-1,i+1,j);
                ll third = minarea(grid,0,n-1,j+1,m-1);
                ans = min(ans,first+second+third);
            }
        }

        for(ll i=0;i<n;i++)
        {
            for(ll j=i+1;j<n;j++)
            {
                ll first = minarea(grid,0,i,0,m-1);
                ll second = minarea(grid,i+1,j,0,m-1);
                ll third = minarea(grid,j+1,n-1,0,m-1);
                ans = min(ans,first+second+third);
            }
        }

        return ans;
    }
};