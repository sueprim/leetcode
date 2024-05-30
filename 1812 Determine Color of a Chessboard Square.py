class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        res = (ord(coordinates[0]) - 97) + int(coordinates[1])
        return False if res%2 == 1 else True
