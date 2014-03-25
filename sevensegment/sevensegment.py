

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
        segments = [self.digits[digit] for digit in list(map(int, str(num)))]
        zipped_segments = zip(*map(lambda x: x.split('\n'), segments))
        lines = '\n'.join(map(lambda y: ' '.join(y), zipped_segments))
        return lines
