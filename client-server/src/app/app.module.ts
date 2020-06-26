import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { DishCardComponent } from './components/dish-card/dish-card.component';
import { OwnerCardComponent } from './components/owner-card/owner-card.component';
import { CarouselComponent } from './components/carousel/carousel.component';
import { FilterlistCardComponent } from './components/filterlist-card/filterlist-card.component';
import { ReviewCardComponent } from './components/review-card/review-card.component';

import { RatingModule } from 'ng-starrating';
import { CarouselModule } from 'ngx-bootstrap/carousel';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { SignupComponent } from './signup/signup.component';
import { RestaurantCardComponent } from './components/restaurant-card/restaurant-card.component';
import { PaymentComponent } from './payment/payment.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    SignupComponent,
    DishCardComponent,
    OwnerCardComponent,
    CarouselComponent,
    FilterlistCardComponent,
    ReviewCardComponent,
    RestaurantCardComponent,
    PaymentComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    FontAwesomeModule,
    RatingModule,
    CarouselModule.forRoot(),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
