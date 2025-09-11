class SmallestInfiniteSet {
    int c;
    priority_queue<int, vector<int>, greater<int>> h;
    unordered_set<int> a;
public:
    SmallestInfiniteSet() {
        c = 1;
    }
    
    int popSmallest() {
        if (!h.empty())
        {
            int s = h.top();
            h.pop();
            a.erase(s);
            return s;
        }
        return c++;
    }
    
    void addBack(int num) {
        if (num < c && a.find(num) == a.end())
        {
            h.push(num);
            a.insert(num);
        }
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */