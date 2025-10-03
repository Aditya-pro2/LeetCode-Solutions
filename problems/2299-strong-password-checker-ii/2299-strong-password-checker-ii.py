class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return  any(c.isdigit() for c in password) and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c in '!@#$%^&*()-+' for c in password) and all(a != b for a, b in pairwise(password)) and len(password) > 7