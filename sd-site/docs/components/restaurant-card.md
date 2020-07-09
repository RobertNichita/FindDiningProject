---
id: restaurant-card
title: Restaurant Card
---

## Usage

Displaying dishes with their ratings. Files exist under `src\app\components\restaurant-card`

## UI Appearance

![alt text](../../static/img/examples/restaurant-card.PNG "Restaurant Card")

## Tag Fields

**Identifier**: `app-restaurant-card`

### Input

Specify the input:

| Parameter    | Type  | Desc              | Required |
| ------------ | ----- | ----------------- | -------- |
| `restaurant` | `any` | Restaurant object | Yes      |

The restaurant object should contain:

```json
{
  "_id": "{{ MongoDB id of restaurant }}",
  "name": "{{ restaurant name }}",
  "address": "{{ restaurant address }}",
  "phone": "{{ restuarant phone number }}",
  "email": "{{ restaurant email }}",
  "city": "{{ city restaurant is in }}",
  "cuisine": "{{ type of cuisine }}",
  "pricepoint": "{{ restaurant price point }}",
  "rating": "{{ restaurant rating }}",
  "twitter": "{{ restaurant twitter url }}",
  "instagram": "{{ restaurant instagram url }}",
  "bio": "{{ restaurant bio }}",
  "GEO_location": "{\"longitude\": 19.421700, \"latitude\" : 13.216966}",
  "external_delivery_link": "{{ self explainatory }}",
  "cover_photo_url": "{{ url to page cover photo}}",
  "logo_url": "{{ url to restaurant logo }}"
}
```

Example:

```json
{
  "_id": "5f0219fb0c491ec3860430d6",
  "name": "popeyes",
  "address": "200 chicago st",
  "phone": 6475040680,
  "email": "popeyeschicken@popeyes.com",
  "city": "chicago",
  "cuisine": "american",
  "pricepoint": "low",
  "rating": 4.7,
  "twitter": "https://twitter.com/KEEMSTAR",
  "instagram": "https://www.instagram.com/dramaalert/?hl=en",
  "bio": "We server the best chicken in the world! Classic american style",
  "GEO_location": "{\"longitude\": 19.421700, \"latitude\" : 13.216966}",
  "external_delivery_link": "https://play.typeracer.com/",
  "Cover_Photo_URL": "https://cdn.mos.cms.futurecdn.net/BVb3Wzn9orDR8mwVnhrSyd-1200-80.jpg",
  "Logo_URL": "https://cdn.mos.cms.futurecdn.net/BVb3Wzn9orDR8mwVnhrSyd-1200-80.jpg"
}
```

Add this to the `.html` file. Replace the sections `{{ }}` with the input to be generated.

```html
<app-restaurant-card [restaurant]="{{ restaurant }}"></app-restaurant-card>
```

### Output

There is no output. The card example above will be generated.

The id will be set on the card button to link with the individual restaurant page.
