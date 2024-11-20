from HotelMerger import HotelMerger
from HotelArgParser import HotelArgParser

def main():

    args = HotelArgParser.create_arg_parser()

    HotelMerger.create_hotel_fetcher('acme')
    HotelMerger.create_hotel_fetcher('patagonia')
    HotelMerger.create_hotel_fetcher('paperflies')

    HotelMerger.merge()

    HotelMerger.find(args.hotel_ids, args.destination_ids)


if __name__ == "__main__":
    main()
