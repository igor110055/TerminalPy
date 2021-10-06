# def PriceDifferenceAbsolute(priceData):
#     for index in range(0,len(priceData)):
#         element1 = priceData[index]
       
#         def IndexOffset():
#             if index + 1 >= len(priceData):
#                 return -1
#             else:
#                 return index +1
        
#         element2 = priceData[IndexOffset()]
        
#         changeAbsolute = element2 - element1
        
#         print('changeAbsolute: ',changeAbsolute)

def PriceDifferencePercentage(priceData):
    PriceDifference = []
    for index in range(0,len(priceData)):
        element1 = priceData[index]
       
        def IndexOffset():
            if index + 1 >= len(priceData):
                return -1
            else:
                return index +1
        
        element2 = priceData[IndexOffset()]
        
        changePercentage = ((element2 / element1) - 1) * 100
        PriceDifference.append(changePercentage)
        #print('changePercentage: ',changePercentage)
    return PriceDifference

