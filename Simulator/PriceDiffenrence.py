def PriceDiffPercent(AssetData):
    PriceDifference = [0]
    for index in range(2,len(AssetData)):
        element2 = AssetData[index]
        element1 = AssetData[index-1]
        changePercentage = ((element2 / element1) - 1) * 100
        PriceDifference.append(round(changePercentage))

    return PriceDifference

# def PriceDifferencePercentage(priceData):
#     PriceDifference = []
#     for index in range(0,len(priceData)):
#         element1 = priceData[index]
       
#         def IndexOffset():
#             if index + 1 >= len(priceData):
#                 return -1
#             else:
#                 return index +1
        
#         element2 = priceData[IndexOffset()]
        
#         changePercentage = ((element2 / element1) - 1) * 100
#         PriceDifference.append(changePercentage)
        
#     return PriceDifference
