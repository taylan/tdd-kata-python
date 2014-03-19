

class StringCalculator():
    def _parse_single_number(self, inp):
        try:
            return int(inp)
        except ValueError:
            return None

    def _parse_multiple_numbers(self, inp):
        try:
            return sum(map(int, inp.strip().split(' ')))
        except ValueError:
            return None

    def add(self, inp):
        if not inp:
            return 0

        single_num = self._parse_single_number(inp)
        if single_num:
            return single_num

        multiple_num_sum = self._parse_multiple_numbers(inp)
        if multiple_num_sum:
            return multiple_num_sum

        return ''
