import { Component, OnInit, HostListener } from '@angular/core';
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

  cuisines = [
    { path: 'assets/images/cuisines/chinese.png', caption: 'Chinese' },
    { path: 'assets/images/cuisines/greek.jpg', caption: 'Greek' },
    { path: 'assets/images/cuisines/indian.jpg', caption: 'Indian' },
    { path: 'assets/images/cuisines/italian.png', caption: 'Italian' },
    { path: 'assets/images/cuisines/japanese.jpg', caption: 'Japanese' },
    { path: 'assets/images/cuisines/thai.jpg', caption: 'Thai' },
    { path: 'assets/images/cuisines/vietnamese.jpg', caption: 'Vietnamese' },
  ];

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
