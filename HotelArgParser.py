import argparse
class HotelArgParser:

    @staticmethod
    def create_arg_parser():
        parser = argparse.ArgumentParser(
            description="Merge hotel information based on hotel and destination IDs.")

        parser.add_argument('hotel_ids', type=str,
                            help="Comma-separated list of hotel IDs or 'none'")
        parser.add_argument('destination_ids', type=str,
                            help="Comma-separated list of destination IDs or 'none'")

        args = parser.parse_args()
        return args
