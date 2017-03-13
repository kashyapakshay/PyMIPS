class Utils(object):
    def __init__(self):
        pass

    @staticmethod
    def int2bs(s, n):
        """ Converts an integer string to a 2s complement binary string.

            Args: s = Integer string to convert.to 2s complement binary.
                  n = Length of outputted binary string.

            Example Input: stpd("4", 4)
            Example Output: "0100"

            Example Input: stpd("-3", 16)
            Example Output: "1111111111111101" """

        x = int(s)                              # Convert string to integer, store in x.
        if x >= 0:                              # If not negative, use python's binary converter and strip the "0b"
            ret = str(bin(x))[2:]
            return ("0"*(n-len(ret)) + ret)     # Pad with 0s to length.
        else:
            ret = 2**n - abs(x)                 # If negative, convert to 2s complement integer
            return bin(ret)[2:]                 # Convert to binary using python's binary converter and strip the "0b"

    @staticmethod
    def bs2hex(v):
        """ Converts a binary string into hex.

            Args: v = Binary string to convert to hex

            Example Input: bs2hex("1010000010001111")
            Example Output: "a08f" """

        return(hex(int(v,2))[2:])
