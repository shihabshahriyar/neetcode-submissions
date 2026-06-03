class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'NONE'

        return 'SHIHAB'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'NONE':
            return []

        return s.split('SHIHAB')
