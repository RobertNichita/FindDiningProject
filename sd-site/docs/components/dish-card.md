---
id: dish-card
title: Dish Card
---

## Usage

Displaying dishes with their ratings. Files exist under `src\app\components\dish-card`

## UI Appearance

![alt text](../../static/img/examples/dish-card.PNG "Dish Card")

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
  "type": "dish",
  "name": "{{ dish name }}",
  "rating": "{{ rating number out of 5 (whole numbers) }}",
  "price": "{{ the price of the dish }}",
  "image": "{{ path to the image file }}",
  "url": "{{ link to the dish page }}"
}
```

Example:

```json
{
  "type": "dish",
  "name": "Special Dish",
  "rating": "4",
  "price": "2.99",
  "image": "assets/images/cuisines/chinese.png",
  "url": "/"
}
```

Add this to the `.html` file. Replace the sections `{{ }}` with the input to be generated.

```html
<app-dish-card [dish]="{{ dish object }}"></app-dish-card>
```

### Output

There is no output. The card example above will be generated.
