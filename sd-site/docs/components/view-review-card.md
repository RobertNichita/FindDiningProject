---
id: view-review-card
title: View Review Card
---

## Usage

Displays reviews.

Files exist under `src\app\components\view-review-card`

## UI Appearance

![alt text](../../static/img/examples/view-review-card.PNG "View Review Card")

## Tag Fields

**Identifier**: `app-view-review-card`

### Input

Specify the input:

| Parameter | Type  | Desc            | Required |
| --------- | ----- | --------------- | -------- |
| `review`  | `any` | A review object | Yes      |

Currently, the review object should contain:

```json
{
  "name": "{{ user name }}",
  "date": "{{ date review was posted }}}",
  "image_path": "{{ url to user image, provided by Auth0 }}",
  "rating": "{{ review rating }}",
  "title": "{{ review title }}",
  "review": "{{ review content }}"
}
```

Example:

```json
{
  "name": "Bob",
  "date": "June 29",
  "image_path": "https://i2.wp.com/cdn.auth0.com/avatars/e.png?ssl=1",
  "rating": 4.3,
  "title": "Good Food",
  "review": "It's really good"
}
```

Add this to the `.html` file. Replace the sections `{{ }}` with the input to be generated.

```html
<app-view-review-card [review]="{{ review object }}"></app-view-review-card>
```

Example:

```html
<app-review-card
  [width]="600"
  (review)="displayReview($event)"
></app-review-card>
```

### Output

There is no output. The card example above will be generated.
