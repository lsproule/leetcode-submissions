class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = []

        for string in strs:
            final_string.append(":-\n" + string)
        return "".join(final_string)

    def decode(self, s: str) -> List[str]:
        return s.split(":-\n")[1:]
