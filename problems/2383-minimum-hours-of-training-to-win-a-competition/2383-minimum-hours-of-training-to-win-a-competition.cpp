class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        int c = 0;
        for (int i = 0; i < energy.size(); i++)
        {
            if (energy[i] >= initialEnergy)
            {
                c += energy[i] - initialEnergy + 1;
                initialEnergy += energy[i] - initialEnergy + 1;
            }
            if (experience[i] >= initialExperience)
            {
                c += experience[i] - initialExperience + 1;
                initialExperience += experience[i] - initialExperience + 1;
            }
            initialEnergy -= energy[i];
            initialExperience += experience[i];
        }
        return c;
    }
};