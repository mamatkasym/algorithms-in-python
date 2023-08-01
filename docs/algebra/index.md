# Algebra

## Calculate power 
For given numbers `base`, `power`, and `mod` calculate `base^power % mod` .

    def power_modulo(base: int, power: int, mod: int) -> int:
        """
        returns n^k mod m
        TC: log(k + m)
        """
        res = 1
        while power > 0:
            if power % 2:
                res = res * base % mod
            power //= 2
            base = base * base % mod
    
        return res