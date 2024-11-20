import json
from schemas import Acme, Paperflies, Patagonia
from Fetcher import Fetcher


class HotelMerger:

    hotel_fetchers = []

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
            # Fetch the data objs
            json_data = hotel_fetcher.fetch()
      
            for supplier_json_obj in json_data:
                # Convert JSON to supplier instance
                supplier_instance = hotel_fetcher.hotel_classname.from_dict(supplier_json_obj)
                hotel_instance = hotel_fetcher.hotel_classname.adapt(supplier_instance) # Adapt supplier instance to mutual Hotel instance

                # Add to key list (for searching in 'none' Command line argument cases)
                hotel_id_key = str(hotel_instance.id)
                cls.all_hotel_ids.add(hotel_id_key)

                # Add to key list (for searching in 'none' Command line argument cases)
                destination_id_key = str(hotel_instance.destination_id)
                cls.all_destination_ids.add(destination_id_key)
                
                key = hotel_id_key + destination_id_key

                if key in cls.database:
                    # Merge 2 objs that are considered 'same' in the database
                    self_obj = cls.database[key]
                    other_obj = hotel_instance
                    cls.database[key] = self_obj.merge(other_obj)
                else:
                    cls.database[key] = hotel_instance

        

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

        
        # Generate possible combination of keys to query
        possible_keys = [str(hotel_id) + str(destination_id)
                         for hotel_id in hotel_ids for destination_id in destination_ids]
                         
        res = []
        for key in possible_keys:
            if key in cls.database:
                data = json.loads(cls.database[key].to_json())
                res.append(data)

        print(json.dumps(res))

        return res


