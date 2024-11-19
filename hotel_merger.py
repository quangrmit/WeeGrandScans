import argparse
import json
from schemas import Acme, Paperflies, Patagonia
from Fetcher import Fetcher


class HotelMerger:

    hotel_fetchers = []
    merged = []
    mapping = {
        'acme': Acme,
        'patagonia': Patagonia,
        'paperflies': Paperflies
    }

    all_hotel_ids = set()
    all_destination_ids = set()

    database = dict()

    @classmethod
    def merge(cls):
        for hotel_fetcher in cls.hotel_fetchers:
            data = hotel_fetcher.fetch()
            for i in range(len(data)):
                obj = hotel_fetcher.hotel_classname.from_dict(data[i])
                data[i] = hotel_fetcher.hotel_classname.adapt(obj)

                hotel_id_key = str(data[i].id)
                cls.all_hotel_ids.add(hotel_id_key)
                destination_id_key = str(data[i].destination_id)
                cls.all_destination_ids.add(destination_id_key)
                key = hotel_id_key + destination_id_key
                if key in cls.database:
                    self_obj = cls.database[key]
                    other_obj = data[i]
                    cls.database[key] = self_obj.merge(other_obj)
                else:
                    cls.database[key] = data[i]
                cls.merged.append(data[i])
        

    @classmethod
    def create_hotel_fetcher(cls, hotel_name):
        if hotel_name in cls.mapping:
            fetcher = Fetcher(hotel_name, cls.mapping[hotel_name])
            cls.hotel_fetchers.append(fetcher)
            return fetcher
        else:
            raise Exception('Invalid hotel name')

    @classmethod
    def find(cls, hotel_ids, destination_ids):

        if hotel_ids == 'none':
            hotel_ids = cls.all_hotel_ids
        else:
            hotel_ids = hotel_ids.split(",")

        if destination_ids == 'none':
            destination_ids = cls.all_destination_ids
        else:
            destination_ids = destination_ids.split(",")

        

        possible_keys = [str(hotel_id) + str(destination_id)
                         for hotel_id in hotel_ids for destination_id in destination_ids]
        res = []
        for key in possible_keys:
            if key in cls.database:
                data = json.loads(cls.database[key].to_json())
                res.append(data)

        print(json.dumps(res))

        return res


def main():
    parser = argparse.ArgumentParser(
        description="Merge hotel information based on hotel and destination IDs.")

    parser.add_argument('hotel_ids', type=str,
                        help="Comma-separated list of hotel IDs or 'none'")
    parser.add_argument('destination_ids', type=str,
                        help="Comma-separated list of destination IDs or 'none'")

    args = parser.parse_args()

    HotelMerger.create_hotel_fetcher('acme')
    HotelMerger.create_hotel_fetcher('patagonia')
    HotelMerger.create_hotel_fetcher('paperflies')

    HotelMerger.merge()

    HotelMerger.find(args.hotel_ids, args.destination_ids)


if __name__ == "__main__":
    main()
