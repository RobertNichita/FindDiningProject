---
id: dish-card
title: Dish Card
---

## Usage

Displaying dishes with their ratings. Clicking **View Dish** brings a modal up with dish details, ability to place orders, and dish reviews.

Files exist under `src\app\components\dish-card`

## UI Appearance

![Dish Card](../../static/img/examples/dish-card.PNG "Dish Card")
![Dish Card Modal](../../static/img/examples/dish-card-modal.PNG "Dish Card Modal")

## Tag Fields

**Identifier**: `app-dish-card`

### Input

Specify the input:

| Parameter | Type  | Desc        | Required |
| --------- | ----- | ----------- | -------- |
| `dish`    | `any` | Dish object | Yes      |

Currently, the dish object should contain:

```json
{
  "_id": "{{ id from MongoDB }}",
  "name": "{{ dish name }}",
  "description": "{{ description of dish }}",
  "picture": "{{ path to the image file }}",
  "price": "{{ the price of the dish }}",
  "tags": "{{ TDB }}",
  "specials": "{{ TBD }}"
}
```

Example:

```json
{
  "_id": "5f07ea00b5dbd5fe3e893bd3",
  "name": "Juicy Lamb steak",
  "description": "medium rare lamb steak cooked to perfection",
  "picture": "https://nationalpostcom.files.wordpress.com/2018/12/GettyImages-835995304.jpg",
  "price": "34.99",
  "tags": [],
  "specials": ""
}
```

Add this to the `.html` file. Replace the sections `{{ }}` with the input to be generated.

```html
<app-dish-card [dish]="{{ dish object }}"></app-dish-card>
```

### Output

There is no output yet. The card example above will be generated. When the ordering functionality is present, this component will be edited to add the correct number of the specific dish.
