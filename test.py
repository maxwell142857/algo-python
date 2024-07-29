class Product:
    cnt = 0
    def __init__(self, name):
        if Product.productCnt == Limit.get_limit():
            # Product.cnt += 1
            raise UserLimitExceeded()
        self.name = name
        Product.cnt += 1

    def __del__(self):
        Product.productCnt -= 1