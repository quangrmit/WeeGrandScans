# Hey there!

Thanks for taking the time to work on this assignment!

Through this exercise, we hope to acquaint you with some of our day-to-day work at Ascenda. We hope you'll make full use of the time limit, chew through the problem, and take a good shot at it. Don't worry -- this isn't a leetcode exercise, we'll focus more on clean code than memory optimization.

# Background

In any hotels site like Kaligo.com operated by Ascenda, there's a lot of effort being made to present content in a clean & organised manner. Underneath the hood however, the data procurement process is complex and data is often mismatched & dirty.

This exercise gives you a sneak peak in some of the actions we take to clean up data before it makes it to the site
- Querying multiple suppliers to assimilate data for these different sources
- Building the most complete data set possible
- Sanitizing them to remove any dirty data
- etc.


Your task is to write a simplified version of our data procurement & merging process:
1. Fetch raw hotel data from different suppliers.
2. Parse and clean the raw data.
3. Each supplier may return different attributes about the same hotel. Merge them and preserve what you think is the best data.
4. Return the merged data in JSON format.


# Requirements

- Implement a CLI application that accepts 2 arguments for filtering: `hotel_ids` and `destination_ids` (ordering is important)
  - The format of both these arguments is a string that contains a list of value, each of which is separated by a comma `,`
  - In the case that the list is empty, the value of the argument is `none`.
  - Some examples:
```
my_hotel_merger hotel_id_1,hotel_id_2,hotel_id_3 destination_id_1,destination_id_2
my_hotel_merger hotel_id_4,hotel_id_5 none
my_hotel_merger none destination_id_3
```
- When called, the application should print an array of hotel data in JSON format to standard output. The structure of the hotel data is shown below.
  - The returned hotels should match all of the provided hotel_ids and destination_ids in the input. If a hotel matches the destination_ids but not hotel_ids, it shouldn't be returned.
  - If no hotel_id or destination_id is provided in the input, return all hotels.
- Each hotel should be returned only once (since you've already uniquely merged the data)


The JSON response from your implementation should match the following structure:
```
[
  {
    "id": "iJhz",
    "destination_id": 5432,
    "name": "Beach Villas Singapore",
    "location": {
      "lat": 1.264751,
      "lng": 103.824006,
      "address": "8 Sentosa Gateway, Beach Villas, 098269",
      "city": "Singapore",
      "country": "Singapore"
    },
    "description": "Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station.",
    "amenities": {
      "general": ["outdoor pool", "indoor pool", "business center", "childcare", "wifi", "dry cleaning", "breakfast"],
      "room": ["aircon", "tv", "coffee machine", "kettle", "hair dryer", "iron", "bathtub"]
    },
    "images": {
      "rooms": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg", "description": "Bathroom" }
      ],
      "site": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg", "description": "Front" }
      ],
      "amenities": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg", "description": "RWS" }
      ]
    },
    "booking_conditions": [
      "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
      "Pets are not allowed.",
      "WiFi is available in all areas and is free of charge."
    ]
  }
]
```
- After finishing the implementation, create a bash script file named `runner` at the root of the project. This file should include the command needed to execute your CLI app, and the `hotel_ids` and `destination_ids` are provided via two positional arguments `$1`, `$2`. We need this `runner` script in order to grade your submission automatically.
- You can find a rough example solution here: https://gist.github.com/vu-hoang-kaligo/39fb5baedd20375e55baf947d26eea28

# Supplier data

There are 3 suppliers, you'll have to fetch data from their respective URLs (you can click on these links to check out their responses):

https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme
https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia
https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies

You can assume the following about the supplier data:
- Hotel and destination IDs are already sanitized.
- Each supplier will always return matching hotel and destinations IDs. You can merge the hotel data against these IDs.
- Image links from the suppliers are already verified as working, you only need to worry about the organization of image data for it.
- You should assume that the supplier data will change over time, so your solution should adapt to return whatever is the best-quality data returned by the suppliers.

# Submission

To submit your code, fill out this form: https://forms.gle/mHCVjMzTREbkhTpr9

# What we're expecting

- This is not a "leetcode" question. We're interested in how your solution tackles the problem elegantly. We'll also grade the solution based on the code cleanliness. Do make use of design patterns and other methods for organising your code.
- For the purposes of this exercise, the dataset is truncated and there's a smaller range of suppliers. Ideally, your solution should show us how you'd handle data aggregation if there's many more suppliers.
- We expect you to make appropriate decisions on data cleaning & selecting the best data to be returned.
- No data-analytics approach is needed for this exercise, we're not looking for any fancy machine-learning evaluation for merging the data, some simple rules in code for matching the data is sufficient.