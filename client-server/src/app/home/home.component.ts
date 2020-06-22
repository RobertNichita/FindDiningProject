import { Component, OnInit, HostListener } from '@angular/core';
import { StarRatingComponent } from 'ng-starrating';
import {
  faArrowUp,
  faArrowCircleDown,
} from '@fortawesome/free-solid-svg-icons';
import dishes from '../../assets/data/dishes.json';
import stories from '../../assets/data/stories.json';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  isShow: boolean;
  topPosToStartShowing = 100;
  faArrowUp = faArrowUp;
  faArrowCircleDown = faArrowCircleDown;

  totalStars: number = 5;
  dishes: any[];
  stories: any[];

  constructor() {
    this.dishes = dishes;
    this.stories = stories;
  }

  ngOnInit(): void {}

  @HostListener('window:scroll')
  checkScroll() {
    const scrollPosition =
      window.pageYOffset ||
      document.documentElement.scrollTop ||
      document.body.scrollTop ||
      0;

    if (scrollPosition >= this.topPosToStartShowing) {
      this.isShow = true;
    } else {
      this.isShow = false;
    }
  }

  gotoTop() {
    window.scroll({
      top: 0,
      left: 0,
      behavior: 'smooth',
    });
  }

  scrollDown() {
    const newPosition = document.getElementById('scroll').offsetTop;
    window.scroll({
      top: newPosition,
      left: 0,
      behavior: 'smooth',
    });
  }
}
