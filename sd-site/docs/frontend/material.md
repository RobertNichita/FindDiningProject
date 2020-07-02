---
id: material
title: Angular Material
---

[Documentation](https://material.angular.io/) |
[npm package](https://www.npmjs.com/package/@angular/material)

## Usage

Add pre-made UI components to your code. Basic installation and imports have already been done.

## How to Use

First import the module copmonent you want to use from the package in the `app.module.ts` file.

```javascript
import { MatButtonModule } from "@angular/material/button";
```

Make sure to add the module to imports.

```javascript
@NgModule({
  declarations: [...],
  imports: [
    ...,
    MatButtonModule
  ],
  ...
})
```

To use the component in the `.html` template, copy the example code from the documentation and paste it where desired.

```html
<fa-icon [icon]="faCoffee"></fa-icon>
```

## Modifications

You can change component properties depending on what Angular Material allows. Read the documentation.
