---
id: aos
title: AOS Animations
---

[Demo](https://michalsnik.github.io/aos/) |
[npm package](https://www.npmjs.com/package/aos)

## Usage

Add animations to components.

## How to Use

First import the package to the `.ts` file.

```javascript
import AOS from "aos";
import "aos/dist/aos.css";
```

In the `ngOnInit()` function, add:

```javascript
AOS.init({
  delay: 300,
  duration: 1500,
  once: false,
  anchorPlacement: "top-bottom",
});
```

Then attach the animation property to an HTML tag.

```html
<div data-aos="animation_name"></div>
```

A list of possible animations can be seen [here](https://www.npmjs.com/package/aos#-animations).

## Modifications

The animation properties can be edited in the `AOS.init()` function:

| Parameter         | Desc                                                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `delay`           | How long to wait until the animation appears when you reach it                                                                          |
| `duration`        | How long it takes for the animation to transition into place                                                                            |
| `once`            | If you only want the animation to show once on the page (i.e. if you scroll back up and back down, the animation will not appear again) |
| `anchorPlacement` | Which part of the component should it reach before loading                                                                              |

All possible properties are [here](https://github.com/michalsnik/aos#1-initialize-aos).
