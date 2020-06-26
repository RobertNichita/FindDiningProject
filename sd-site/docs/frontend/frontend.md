---
id: frontend
title: Frontend
---

Compliation of how to use **packages** that are used in Angular.

## Style Guide

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
