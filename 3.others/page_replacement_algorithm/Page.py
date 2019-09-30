
def f_print(sth):
    print(sth)

class Page(object):
    def __init__(self, pageNum):
        f_print('Page Create')
        self.pageNum = pageNum

    def get_pagenum(self):
        return self.pageNum

class PageBit(Page):
    def __init__(self, pageNum):
        super().__init__(pageNum)
        self.reference_bit = 0
        self.modify_bit = 0

    def get_bit(self):
        """ return (reference_bit , modify_bit) """
        return self.reference_bit, self.modify_bit

    def set_reference_bit(self, bit):
        if bit != 0 and bit != 1:
            raise ValueError('reference_bit must be 0 or 1')
        self.reference_bit = bit

    def set_modify_bit(self, bit):
        if bit != 0 and bit != 1:
            raise ValueError('modify_bit must be 0 or 1')


# %%
if __name__ == "__main__":
    page_list = [Page(i) for i in range(2)]
    for p in page_list:
        print(p.get_pagenum())

    page_bit_list = [PageBit(i) for i in range(2)]
    for p in page_bit_list:
        print(p.get_bit())
