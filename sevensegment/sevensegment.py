

class SevenSegment():
    digits = ['._.\n|.|\n|_|',
              '...\n..|\n..|',
              '._.\n._|\n|_.',
              '._.\n._|\n._|',
              '...\n|_|\n..|',
              '._.\n|_.\n._|',
              '._.\n|_.\n|_|',
              '._.\n..|\n..|',
              '._.\n|_|\n|_|',
              '._.\n|_|\n..|']

    def render(self, num):
        if len(str(num)) == 1:
            return self.digits[num]
        return ''
