import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DishCardComponent } from './dish-card/dish-card.component';
import { OwnerCardComponent } from './owner-card/owner-card.component';
import { FilterlistCardComponent } from './filterlist-card/filterlist-card.component';
import { ReviewCardComponent } from './review-card/review-card.component';

@NgModule({
  declarations: [
    DishCardComponent,
    OwnerCardComponent,
    FilterlistCardComponent,
    ReviewCardComponent,
  ],
  imports: [CommonModule],
})
export class ComponentsModule {}
