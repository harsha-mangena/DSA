class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Replaces periods in an IPv4 address with [.].

        :param address: A string representing the IPv4 address to defang.
        :type address: str
        :return: A defanged IPv4 address.
        :rtype: str
        """
        address = address.split(".")
        return "[.]".join(address)