import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DishCardComponent } from './dish-card/dish-card.component';
import { OwnerCardComponent } from './owner-card/owner-card.component';

@NgModule({
  declarations: [DishCardComponent, OwnerCardComponent],
  imports: [CommonModule],
})
export class ComponentsModule {}
