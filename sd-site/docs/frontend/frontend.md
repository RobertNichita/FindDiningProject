---
id: frontend
title: Frontend
---

Compliation of how to use **packages** that are used in Angular, and styles set for the project.

## Style Guide

### Default Colours

Some of the default site colours are defined in the global `.scss` file.

To use the colours in your page/component, add this to the top of you `.scss` file

```css
@import "src/styles";
```

Then call on the colour using `$`:

```css
.navbar {
  background-color: $primary-color;
}
```

### Bottom Corner Image

Most pages will have an image at the bottom left corner to spice up the appearance of the page. Simply add the image to the page `.html` file and add the `bottom-left` class to it to format properly.

```html
<img class="bottom-left" src="assets/images/undraw_chef.png" />
```

The `bottom-left` class has been defined in `styles.scss`.
