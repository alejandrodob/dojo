class Roman(object):

    @classmethod
    def translate(cls, number):
        if number > 3:
            return 'IV'
        return 'I' * number
