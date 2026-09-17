**Output Model Design:**

**Opinion Base Model:**

topic

sentiment

problem-optional ( could be about shipping or the product itself)

suggested solution -optional ( if the customer left a suggested solution)

**Structured Review Base Model:**

review_id: Id of the review

overall sentiment: sentiment of the review

notable phrases: notable phrases found inthe review

opinions: list of opinions called in group above.

This will be a nested relationship. Customers may write multiple opinions in their feedback such as shipping time, product satisfaction, overall rating.

Required fields will be star rating and review text

Optional fields will be shipping

**Input Model Design:**

The input design will have Review ID, CustomerID, Date, Star Rating, Text Review

**Examples:**

“The item is great but arrived 3 days after expected. I needed it for an event, and I didn’t receive it in time. I will be returning. Very disappointed because this would have been perfect at my event”

“Great product and received on time. Highly recommend”