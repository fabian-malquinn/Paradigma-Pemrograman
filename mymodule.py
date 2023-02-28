class makanan:
    def __init__(self, harga_coklat, harga_stroberi):
        self.harga_cokelat = harga_coklat
        self.harga_stroberi = harga_stroberi

    def coklat(self):
        print(f"Coklat 1 Biji : {self.harga_cokelat}")

    def stroberi(self):
        print(f"Stroberi 1 Biji : {self.harga_stroberi}")


permen = makanan("Rp.1,000", "Rp.500")
permen.coklat()
permen.stroberi()
