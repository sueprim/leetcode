class Solution(object):
    def titleToNumber(self, columnTitle):
        # ord(A) =65
        # add up to the answer
        column_number = 0
        
        # go through the string
        i = 1
        for letter in columnTitle[::-1]:
            # ord(letter) - 64 will give the number we want
            number_represented = ord(letter) - 64
            if i != 1:
                # then have it power to the i
                number_to_add = number_represented * (26**(i-1))
            else:
                number_to_add = number_represented
            # and add it to the column_number
            column_number += number_to_add
            # also add 1 to i as it progresses
            i += 1
        
        return column_number
