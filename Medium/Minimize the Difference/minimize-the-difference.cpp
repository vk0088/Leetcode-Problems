//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Array
{
public:
    template <class T>
    static void input(vector<T> &A,int n)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d ",&A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
public:
    int minimizeDifference(int n, int k, vector<int>& a) {

        vector<pair<int, int>> prefixMinMax(n), suffixMinMax(n);
        
        prefixMinMax[0] = {a[0], a[0]};
        suffixMinMax[n - 1] = {a[n - 1], a[n - 1]};
        
        for (int i = 1; i < n; i++) {
            int revIdx = n - i - 1;
            prefixMinMax[i] = {
                min(prefixMinMax[i - 1].first, a[i]),
                max(prefixMinMax[i - 1].second, a[i])
            };
            suffixMinMax[revIdx] = {
                min(suffixMinMax[revIdx + 1].first, a[revIdx]),
                max(suffixMinMax[revIdx + 1].second, a[revIdx])
            };
        }
        
        int minDiff = INT_MAX;

        for (int i = 0; i <= n - k; i++) {
            int minElem = i == 0 ? suffixMinMax[i + k].first : (i + k == n ? prefixMinMax[i - 1].first : min(prefixMinMax[i - 1].first, suffixMinMax[i + k].first));
            int maxElem = i == 0 ? suffixMinMax[i + k].second : (i + k == n ? prefixMinMax[i - 1].second : max(prefixMinMax[i - 1].second, suffixMinMax[i + k].second));
            minDiff = min(minDiff, maxElem - minElem);
        }
        
        return minDiff;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int n;
        scanf("%d",&n);
        
        
        int k;
        scanf("%d",&k);
        
        
        vector<int> arr(n);
        Array::input(arr,n);
        
        Solution obj;
        int res = obj.minimizeDifference(n, k, arr);
        
        cout<<res<<endl;
        
    }
}

// } Driver Code Ends