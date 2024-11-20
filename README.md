# Kaligo Hotel Merger
This solution works under the assumption that the API URLs of the suppliers have the same base, and only differ in the last part. E.g.
https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme
https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia
https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies \
This README file consists of 2 parts (Design explanation and what happens when there are more suppliers)

## Design explanation (main components only)
### 1. Schema classes
- `Hotel`: Specify the schema to use universally. All other schemas must adapt to this using their `adapt()` method
- `BaseSupplierSchema`: Force implementation of `adapt()` method for specific supplier classes

- `Acme(BaseSupplierSchema)`: Inherits `BaseSupplierSchema`. Describes the attributes when fetching from Acme and its specific implementation of `adapt()`

- `Patagonia(BaseSupplierSchema)` and `Paperflies(BaseSupplierSchema)`: Do the same thing as Acme, but for different suppliers

### 2. `Fetcher` class
- Description: This class is created to fetch data from the suppliers' respective API URLs, and store them as an array of objects (`Acme`, `Patagonia` or `Paperflies`)
- Attributes: 
    - `base_url`: The mutual prefix of API URLs
    - `hotel_classname`: Specifying the type of object schema we will be fetching
    - `url`: The complete URL to fetch, by appending the hotel name to the end.
- Methods:
    - `__init__(self, hotel_name, hotel_classname)`: 
        - Create a `Fetcher` object
        - Build the specific API URL for that supplier (appending the `hotel_name`) 
        - Let the `Fetcher` object know which supplier object to call `adapt()` from.
    - `fetch()`: 
        - Fetch from the specified URL
        - Create instances of (`Acme`, `Patagonia`, `Paperflies`) based on the `hotel_classname`
        - Return the list of objects
### 3. `HotelMerger` class
- Description: This class represents the database which is used for the main `find()` operation, as mentioned in the assignment requirements
- Methods:
    - `create_hotel_fetcher(hotel_name)`: Create a `Fetcher` object which the `hotel_name` variable to specify the classname of the supplier
    - `merge()`: 
        - Fetch the supplier objects by calling `fetch()` from each `hotel_fetcher`
        - Loop through each supplier objects, call `adapt()` to convert them to a uniform `Hotel` schema
        - Combine `Hotel` objects with the same id, using values from different objects to create the most complete object
    - `find(hotel_ids, destination_ids)`: Search the database for the correct hotel_ids and destination_ids

### 4. Attribute value selection strategy:
*This problem arises when we want to merge 2 data objects (that are considered the same) whose attributes' values are different. Therefore, I pick the values based on the following criteria:*
- Pick the value that is not null (pick either if both are null)
- If the type of value is `int`, follow the above criterion
- If the type of value is `List`, or `str`, pick the one that is longer in length.


## What happens when we scale up (more suppliers)
Let's say we want to add another supplier called 'Quang', with the URL extension of 'quang' (https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/quang), we would want to update the following:

-  Update the mapping in `HotelMerger`:

    `mapping = {
        'acme': Acme,
        'patagonia': Patagonia,
        'paperflies': Paperflies,
        'quang': Quang,
    }`

- Write a new schema class (the attribute names have to match the JSON fetch results for the `from_dict()` method to work) and how to adapt to `Hotel` schema. E.g 

    ```
    class Quang(BaseSupplierSchema):
        quangId: int
        quangDestId: str
        ...

        def adapt(ins) -> Hotel:
            hotel = Hotel()
            hotel.id = str(ins.quangId)
            ...
    ```
- Create 1 more hotel fetcher named 'quang' in the client code. E.g
    ```
    HotelMerger.create_hotel_fetcher('acme')
    HotelMerger.create_hotel_fetcher('patagonia')
    HotelMerger.create_hotel_fetcher('paperflies')


    HotelMerger.create_hotel_fetcher('quang')
    ```

### That's it! all the merging code and value selection for attributes have been done dynamically and automatically