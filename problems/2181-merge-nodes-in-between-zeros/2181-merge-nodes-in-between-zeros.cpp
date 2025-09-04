/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* temp = new ListNode();
        ListNode* ret = temp;
        head = head->next;
        int s = 0;
        while (head)
        {
            if (head->val != 0)
                s += head->val;
            else
            {
                ListNode* nn = new ListNode(s);
                temp->next = nn;
                temp = temp->next;
                s = 0;
            }
            head = head->next;
        }
        return ret->next;
    }
};