import { Component, OnInit } from '@angular/core';
import { StarRatingComponent } from 'ng-starrating';
import dishes from '../../assets/data/dishes.json';
import stories from '../../assets/data/stories.json';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  totalStars: number = 5;
  dishes: any[];
  stories: any[];

  constructor() {
    this.dishes = dishes;
    this.stories = stories;
  }

  ngOnInit(): void {}
}
