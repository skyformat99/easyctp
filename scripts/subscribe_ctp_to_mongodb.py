from argparse import ArgumentParser

from easyctp.facade import MarketDataExporter, MongoStrategy

if __name__ == '__main__':
    opt = ArgumentParser()
    opt.add_argument('--user', required=True)
    opt.add_argument('--password', required=True)
    opt.add_argument('--broker', required=True)
    opt.add_argument('--front', required=True)
    opt.add_argument('--trade_front', type=str, help='订阅所有合约时需要设置 trade_front')
    opt.add_argument('--instruments', type=str, default='all', help='订阅所有合约时需要设置 trade_front')
    opt.add_argument('--mongodb', help='like mongodb://user:password@127.0.0.1:8086/database_name')
    args = opt.parse_args()
    instrument_ids = args.instruments if args.instruments == 'all' else args.instruments.split(',')
    if instrument_ids == 'all' and args.trade_front is None:
        raise Exception('订阅所有合约时需要设置 trade_front')
    mongo_strategy = MongoStrategy(args.mongodb)
    MarketDataExporter.export_to(mongo_strategy, user=args.user, password=args.password, broker=args.broker,
                                 front=args.front,
                                 instrument_ids=instrument_ids,
                                 trade_front=args.trade_front)
