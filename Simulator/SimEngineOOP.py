

class Engine:
    def __init__(self) -> None:
        self.cash = [0]
        self.asset = [0.1]
        pass

    def buy(self, asset_price, position_size):
        collateral = self.cash[-1]
        if collateral > 0:
            self.buying_power = collateral * position_size
            new_asset_amount = round(self.buying_power/asset_price, 2)
            self.asset.append(self.asset[-1] + new_asset_amount) 
            new_cash_ballance = (1 - position_size) * collateral
            self.cash.append(self.cash[-1] - new_cash_ballance)
        else:
            # If the first Trade that our Bot would make would be a buy we obviously cannot 
            # execute that since we have no Cash in our Account
            print('Cant buy')

    def sell(self, asset_price, position_size):
        collateral = self.asset[-1]
        if collateral > 0:
            self.selling_power = collateral * position_size
            new_cash_ballance = round(self.selling_power * asset_price, 8)
            self.cash.append(self.cash[-1] + new_cash_ballance)
            new_asset_amount = (1 - position_size) * collateral
            self.asset.append(self.asset[-1] - new_asset_amount)

            # self.buying_power = self.collateral * position_size
            # CashAmount = round(self.buying_power * asset_price, 2)
            # self.cash.append(CashAmount) 
        else:
             # If the first Trade that our Bot would make would be a Sell we could not 
            # execute that if we would not have Bitcoin in our Account
            # But in our Scenrio thats not going to happen
            print('Cant sell')
            
        pass

    def return_asset(self):
        return self.asset

    def return_cash(self):
        return self.cash