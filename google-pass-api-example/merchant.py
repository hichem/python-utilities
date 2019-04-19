class Merchant:

    merchantId = ''
    loyaltyClasses = []
    name = ''

    def __init__(self, merchant_id, name):
        self.merchantId = merchant_id
        self.name = name

    def get_loyalty_classes(self):
        return self.loyaltyClasses

    def add_loyalty_class(self, class_descriptor):
        new_class = 'loyalty_' + class_descriptor
        self.loyaltyClasses.append(new_class)
