# Takes the Cash/Asset Ballance from every Position and Calculates the PnL relative to the 
# Position before it
import Simulator.PortfolioValue
import Simulator.LiquidationPrices

class Formater:
    def __init__(self, HistoryObjFromRuntime2 , price_data):
        self.history = HistoryObjFromRuntime2
        self.price_data = price_data

    def formate(self, leverage=1):
        for index in range (0, len(self.history['Trades'])):
            trade_position = self.history['Trades'][index]
            # Overwrite leverage optionally
            if leverage != 1:
                trade_position['Leverage'] = leverage

            # execute in separate loop for every position (start loop from 0)
            total_cash_ammount = Simulator.PortfolioValue.calc_total_cash_value(trade_position)
            trade_position['TotalCashAmount'] = total_cash_ammount

            total_asset_ammount = Simulator.PortfolioValue.calc_total_asset_value(trade_position)
            trade_position['TotalAssetAmount'] = total_asset_ammount

            total_portfolio_value_cash = Simulator.PortfolioValue.total_portfolio_value(
                total_cash_ammount,
                total_asset_ammount,
                trade_position['AssetPrice']
            )
            trade_position['TotalPortfolioValue'] = total_portfolio_value_cash


        for index in range(1, len(self.history['Trades'])):

            trade_position = self.history['Trades'][index]
            prev_trade_position = self.history['Trades'][index - 1]

            asset_price_change_percentage = Simulator.PortfolioValue.calc_price_change(trade_position, prev_trade_position)
            # knock_out = Simulator.LiquidationPrices.Binance(self.price_data, trade_position)

            # Calculate the PnL for every previous Position
            if prev_trade_position['Direction'] == 'Long':
                PnL = asset_price_change_percentage * prev_trade_position['Leverage'] 
                trade_position['PnL'] = round(PnL, 2) 
            elif prev_trade_position['Direction'] == 'Short':
                invert_PnL =  (- asset_price_change_percentage) * prev_trade_position['Leverage'] 
                trade_position['PnL'] = round(invert_PnL, 2)


# put closing date and closing price for every position and corresponding PnL
# adding pnl from previous position to next is confusing
# add closing condition

#fix logic errors in Porfoliovalue.totalPortfolioValue, calc_total_asset_value
# calc_total_cash_value

# Bug PLEASE FIX
# sometimes positions like this end up in the first place,
# Direction Long but without any cash Ballance, should have been an cant buy error in Simulator Engine
# {'Open': '2022-02-22T08:00:00', 'Direction': 'Long', 'AssetPrice': 37504.3725, 'PositionSize': 0.5, 'Leverage': 20, 'AssetBallance': 0.1, 'CashBallance': 0, 'From': 0, 'To': 0, 'ID': 140651586436080}