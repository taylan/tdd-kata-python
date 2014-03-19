class FizzBuzz():
    def calc_fizz_buzz(self, num):
        if not 1 <= num <= 100:
            return None
        if num % 15 == 0:
            return 'FizzBuzz'
        if num % 3 == 0:
            return 'Fizz'
        if num % 5 == 0:
            return 'Buzz'
        return ''
