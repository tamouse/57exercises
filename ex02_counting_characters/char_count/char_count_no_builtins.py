class CharCount:
    @staticmethod
    def count(string):
        num_chars = 0
        while True:
            try:
                if string[num_chars]:
                    num_chars += 1
            except IndexError:
                break

        return num_chars
