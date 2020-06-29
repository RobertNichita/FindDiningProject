---
id: fortawesome
title: Font Awesome Icons
---

[npm package](https://www.npmjs.com/package/@fortawesome/angular-fontawesome)

## Usage

Add icons into your code.

## How to Use

First import the icon you want from the package in the `.ts` file.

```javascript
import { faCoffee } from "@fortawesome/free-solid-svg-icons";
```

In the class declaration, create a variable for the icon.

```javascript
export class AppComponent {
  faCoffee = faCoffee;
}
```

Use the icon in the `.html` template, place it in the desired location.

```html
<fa-icon [icon]="faCoffee"></fa-icon>
```

## Modifications

You can change the icon properties (such as size and colour) by attaching a CSS class to the icon.

```html
<fa-icon class="icons" [icon]="faCoffee"></fa-icon>
```

```css
.icons {
  color: blue;
  font-size: 20px;
}
```
