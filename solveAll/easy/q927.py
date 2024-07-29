class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(s):
            tmp,domain = s.split('@')
            local = []
            for c in tmp:
                if c == '+':
                    break
                if c == '.':
                    continue
                local.append(c)
            return ''.join(local)+'@'+domain
        
        check = set()
        for email in emails:
            check.add(normalize(email))
        return len(check)
