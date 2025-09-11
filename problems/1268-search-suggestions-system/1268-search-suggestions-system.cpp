struct node {
    node* lists[26];
    bool f = false;
    bool containsKey(char ch) { return lists[ch - 'a'] != NULL; }
    void put(char ch, node* node) { lists[ch - 'a'] = node; }
    node* get(char ch) { return lists[ch - 'a']; }
    void setend() { f = true; }
    bool isend() { return f; }
};

class trie {
public:
    node* root;
    trie() { root = new node(); }
    void insert(string word) {
        node* temp = root;
        for (int i = 0; i < word.size(); i++) {
            if (!temp->containsKey(word[i])) {
                temp->put(word[i], new node());
            }
            temp = temp->get(word[i]);
        }
        temp->setend();
    }

    vector<vector<string>> getsuggestion(string word) {
        node* temp = root;
        vector<vector<string>> ans;
        string s;
        for (int i = 0; i < word.size(); i++) {
            if (!temp->containsKey(word[i])) {
                while (i++ < word.size())
                    ans.push_back({});
                break;
            }
            temp = temp->get(word[i]);
            s += word[i];
            string ds = s;
            priority_queue<string, vector<string>, greater<string>> q;
            dfs(temp, q, ds);
            vector<string> v;
            for (int j = 0; j < 3 && !q.empty(); j++) {
                v.push_back(q.top());
                q.pop();
            }
            ans.push_back(v);
        }
        return ans;
    }

    void dfs(node* trav,
             priority_queue<string, vector<string>, greater<string>>& q,
             string& ds) {
        if (trav->isend()) {
            q.push(ds);
        }
        for (char ch = 'a'; ch <= 'z'; ch++) {
            if (trav->containsKey(ch)) {
                ds += ch;
                dfs(trav->get(ch), q, ds);
                ds.pop_back();
            }
        }
    }
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products,
                                             string searchWord) {
        trie t;
        for (int i = 0; i < products.size(); i++) {
            t.insert(products[i]);
        }
        vector<vector<string>> ans = t.getsuggestion(searchWord);
        return ans;
    }
};