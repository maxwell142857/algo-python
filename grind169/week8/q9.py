class Codec:
    def __init__(self) -> None:
        self.divide = chr(255)
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        d = self.divide
        return d.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = s.split(self.divide)
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))