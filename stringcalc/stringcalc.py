

class StringCalculator():
    SEPERATORS = ','

    @staticmethod
    def _parse_single_number(inp):
        try:
            return int(inp)
        except ValueError:
            return None

    def _split_numbers(self, inp):
        lines = [l for l in inp.splitlines()]
        if '\n' in lines:
            if [l for l in lines if l.strip() == '']:
                return None
        return ','.join(lines).strip().split(self.SEPERATORS)

    def _parse_multiple_numbers(self, inp):
        try:
            return sum(map(int, self._split_numbers(inp)))
        except (ValueError, TypeError):
            return None

    def _parse_custom_delimiter(self, inp):
        delim, inp = inp.split('\n', 1)
        self.SEPERATORS = delim.lstrip('/')
        return inp

    def add(self, inp):
        inp = inp.strip()
        if not inp:
            return 0

        if inp.startswith('//'):
            inp = self._parse_custom_delimiter(inp)

        single_num = self._parse_single_number(inp)
        if single_num:
            return single_num

        multiple_num_sum = self._parse_multiple_numbers(inp)
        if multiple_num_sum:
            return multiple_num_sum

        return ''
