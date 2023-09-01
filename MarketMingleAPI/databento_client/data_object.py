
class DataParameters:
    """
    schema : ['mbo', 'mbp-1', 'mbp-10', 'tbbo', 'trades', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 
                'definition', 'statistics', 'status', 'imbalance']

    symbol : ['raw_symbol', 'instrument_id', 'parent','continuous']
    """
    def __init__(self,symbols, schema, start, end, symbol_type, dataset = "GLBX.MDP3"):
        self.dataset = dataset
        self.symbols = symbols
        self.schema = schema
        self.start = start
        self.end = end
        self.stype_in = symbol_type