class RecentCounter {
    vector<int> a;
    int start;
public:
    RecentCounter() {
        start = 0;
    }
    
    int ping(int t) {
        a.push_back(t);
        while (a[start] < t - 3000)
            start++;
        return a.size() - start;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */