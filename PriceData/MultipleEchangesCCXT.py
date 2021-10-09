import ccxt

exchanges = [
'aax'
,'aofex'
,'ascendex'
,'bequant'
,'bibox'
,'bigone'
,'binance'
,'binancecoinm'
,'binanceus'
,'binanceusdm'
,'bit2c'
,'bitbank'
,'bitbay'
,'bitbns'
,'bitcoincom'
,'bitfinex'
,'bitfinex2'
,'bitflyer'
,'bitforex'
,'bitget'
,'bithumb'
,'bitmart'
,'bitmex'
,'bitpanda'
,'bitso'
,'bitstamp'
,'bitstamp1'
,'bittrex'
,'bitvavo'
,'bitz'
,'bl3p'
,'braziliex'
,'btcalpha'
,'btcbox'
,'btcmarkets'
,'btctradeua'
,'btcturk'
,'buda'
,'bw'
,'bybit'
,'cdax'
,'cex'
,'coinbase'
,'coinbaseprime'
,'coinbasepro'
,'coincheck'
,'coinegg'
,'coinex'
,'coinfalcon'
,'coinfloor'
,'coinmarketcap'
,'coinmate'
,'coinone'
,'coinspot'
,'crex24'
,'currencycom'
,'delta'
,'deribit'
,'digifinex'
,'eqonex'
,'equos'
,'exmo'
,'exx'
,'flowbtc'
,'ftx'
,'gateio'
,'gemini'
,'gopax'
,'hbtc'
,'hitbtc'
,'hollaex'
,'huobi'
,'huobijp'
,'huobipro'
,'idex'
,'independentreserve'
,'indodax'
,'itbit'
,'kraken'
,'kucoin'
,'kuna'
,'latoken'
,'lbank'
,'liquid'
,'luno'
,'lykke'
,'mercado'
,'mixcoins'
,'ndax'
,'novadax'
,'oceanex'
,'okcoin'
,'okex'
,'okex3'
,'okex5'
,'paymium'
,'phemex'
,'poloniex'
,'probit'
,'qtrade'
,'ripio'
,'stex'
,'therock'
,'tidebit'
,'tidex'
,'timex'
,'upbit'
,'vcc'
,'wavesexchange'
,'whitebit'
,'xena'
,'yobit'
,'zaif'
,'zb']

exchange_execss = [
ccxt.aax(),
ccxt.aofex(),
ccxt.ascendex(),
ccxt.bequant(),
ccxt.bibox(),
ccxt.bigone(),
ccxt.binance(),
ccxt.binancecoinm(),
ccxt.binanceus(),
ccxt.binanceusdm(),
ccxt.bit2c(),
ccxt.bitbank(),
ccxt.bitbay(),
ccxt.bitbns(),
ccxt.bitcoincom(),
ccxt.bitfinex(),
ccxt.bitfinex2(),
ccxt.bitflyer(),
ccxt.bitforex(),
ccxt.bitget(),
ccxt.bithumb(),
ccxt.bitmart(),
ccxt.bitmex(),
ccxt.bitpanda(),
ccxt.bitso(),
ccxt.bitstamp(),
ccxt.bitstamp1(),
ccxt.bittrex(),
ccxt.bitvavo(),
ccxt.bitz(),
ccxt.bl3p(),
ccxt.braziliex(),
ccxt.btcalpha(),
ccxt.btcbox(),
ccxt.btcmarkets(),
ccxt.btctradeua(),
ccxt.btcturk(),
ccxt.buda(),
ccxt.bw(),
ccxt.bybit(),
ccxt.cdax(),
ccxt.cex(),
ccxt.coinbase(),
ccxt.coinbaseprime(),
ccxt.coinbasepro(),
ccxt.coincheck(),
ccxt.coinegg(),
ccxt.coinex(),
ccxt.coinfalcon(),
ccxt.coinfloor(),
ccxt.coinmarketcap(),
ccxt.coinmate(),
ccxt.coinone(),
ccxt.coinspot(),
ccxt.crex24(),
ccxt.currencycom(),
ccxt.delta(),
ccxt.deribit(),
ccxt.digifinex(),
ccxt.eqonex(),
ccxt.equos(),
ccxt.exmo(),
ccxt.exx(),
ccxt.flowbtc(),
ccxt.ftx(),
ccxt.gateio(),
ccxt.gemini(),
ccxt.gopax(),
ccxt.hbtc(),
ccxt.hitbtc(),
ccxt.hollaex(),
ccxt.huobi(),
ccxt.huobijp(),
ccxt.huobipro(),
ccxt.idex(),
ccxt.independentreserve(),
ccxt.indodax(),
ccxt.itbit(),
ccxt.kraken(),
ccxt.kucoin(),
ccxt.kuna(),
ccxt.latoken(),
ccxt.lbank(),
ccxt.liquid(),
ccxt.luno(),
ccxt.lykke(),
ccxt.mercado(),
ccxt.mixcoins(),
ccxt.ndax(),
ccxt.novadax(),
ccxt.oceanex(),
ccxt.okcoin(),
ccxt.okex(),
ccxt.okex3(),
ccxt.okex5(),
ccxt.paymium(),
ccxt.phemex(),
ccxt.poloniex(),
ccxt.probit(),
ccxt.qtrade(),
ccxt.ripio(),
ccxt.stex(),
ccxt.therock(),
ccxt.tidebit(),
ccxt.tidex(),
ccxt.timex(),
ccxt.upbit(),
ccxt.vcc(),
ccxt.wavesexchange(),
ccxt.whitebit(),
ccxt.xena(),
ccxt.yobit(),
ccxt.zaif(),
ccxt.zb()
]


for i in exchanges:
    f = getattr(ccxt, i)
    result = f()
    print()