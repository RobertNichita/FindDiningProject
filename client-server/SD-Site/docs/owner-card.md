---
id: owner-card
title: Restaurant Owner Card
---

## Usage

Displaying dishes with their ratings. Files exist under `src\app\components\owner-card`

## UI Appearance

![alt text](../static/img/examples/owner-card.PNG "Restaurant Owner Card")

## Tag Fields

**Identifier**: `app-owner-card`

### Input

There is 1 input needed:

1. `story: any` - Story object

Currently, the story object should contain:

```json
{
  "type": "story",
  "name": "{{ owner name }}",
  "profile_pic": "{{ path to image }}",
  "bio": "{{ brief biography of the owner }}",
  "restaurant": "{{ restaurant name }}",
  "url": "{{ link to the restaurant page }}"
}
```

Example:

```json
{
  "type": "story",
  "name": "Robert Downey",
  "profile_pic": "assets/images/undraw_chef.png",
  "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  "restaurant": "Rob's Ribs",
  "url": "/"
}
```

Add this to the `.html` file. Replace the sections `{{ }}` with the input to be generated.

```html
<app-owner-card [story]="{{ story object }}"></app-owner-card>
```

### Output

There is no output. The card example above will be generated.
