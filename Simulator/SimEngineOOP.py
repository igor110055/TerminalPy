

class Engine:
    def __init__(self) -> None:
        self.cash = [0]
        self.asset = [0.01]
        pass

    def buy(self, asset_price, position_size):
        self.collateral = self.asset[-1]
        if self.collateral == 0:
            # If the first Trade that our Bot would make would be a Sell we could not 
            # execute that if we would not have Bitcoin in our Account
            # But in our Scenrio thats not going to happen
            # print('Cant sell')  
            pass
        else:
            self.buying_power = self.collateral * position_size
            CashAmount = round(self.buying_power * asset_price, 2)
            self.cash.append(CashAmount)
        pass

    def sell(self, asset_price, position_size):
        self.collateral = self.cash[-1]
        if self.collateral == 0:
            # If the first Trade that our Bot would make would be a buy we obviously cannot 
            # execute that since we have no Cash in our Account
            # print('Cant buy')
            pass
        else:
            self.selling_power = self.collateral * position_size
            AssetAmount = round(self.selling_power/asset_price, 8)
            self.asset.append(AssetAmount)
        pass

    def return_asset(self):
        return self.asset

    def return_cash(self):
        return self.cash