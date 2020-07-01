import { Component, OnInit, Input, HostListener } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { faMapMarkerAlt, faPhone } from '@fortawesome/free-solid-svg-icons';
import { faHeart, faEnvelope } from '@fortawesome/free-regular-svg-icons';
import { faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';
import dishes from '../../../assets/data/dishes.json';

@Component({
  selector: 'app-restaurant-page',
  templateUrl: './restaurant-page.component.html',
  styleUrls: ['./restaurant-page.component.scss'],
})
export class RestaurantPageComponent implements OnInit {
  @Input() userId: any; // pass the user id everywhere

  restaurantId: string;
  dishes: any[];
  restaurantDetails: any;

  restaurantDetails1 = {
    id: '123',
    name: "Rob's Ribs Ribs Ribs Ribs",
    address: '666 Address Road',
    phone: '416-123-4567',
    email: 'contact@email.com',
    city: 'Scarborough',
    cuisine: 'Ribs',
    pricePoint: '$$',
    rating: '4.7',
    twitter: 'https://twitter.com/',
    instagram: 'https://www.instagram.com/',
    bio:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    category: [
      {
        name: 'Appetizer',
        menu: dishes,
      },
      {
        name: 'Main',
        menu: dishes,
      },
    ],
  };

  restaurantDetails2 = {
    id: '124',
    name: "Rob's Ribs",
    address: '123 Address Road',
    phone: '416-123-4567',
    email: 'contact@email.com',
    city: 'Scarborough',
    cuisine: 'Ribs',
    pricePoint: '$$',
    rating: '4.7',
    twitter: 'https://twitter.com/',
    instagram: 'https://www.instagram.com/',
    bio:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    category: [
      {
        name: 'Appetizer',
        menu: dishes,
      },
      {
        name: 'Dessert',
        menu: dishes,
      },
    ],
  };

  totalStars = 5;
  faMapMarker = faMapMarkerAlt;
  faPhone = faPhone;
  faMail = faEnvelope;
  faHeartLine = faHeart;
  faTwitter = faTwitter;
  faInstagram = faInstagram;

  constructor(private route: ActivatedRoute) {
    this.dishes = dishes;
  }

  ngOnInit(): void {
    this.restaurantId = this.route.snapshot.queryParams.restaurantId;
    // TODO: this will change to call endpoint using restaurant id to get details
    this.restaurantDetails =
      this.restaurantDetails1.id == this.restaurantId
        ? this.restaurantDetails1
        : this.restaurantDetails2;
  }

  @HostListener('window:resize', ['$event'])
  onResize() {
    var el1 = document.getElementById('info-col1');
    var el2 = document.getElementById('info-col2');
    var el3 = document.getElementById('info-row');

    if (window.innerWidth < 750) {
      el1.classList.remove('col-md-7');
      el2.classList.remove('col-md-5');
      el3.classList.remove('row');
    } else {
      el1.classList.add('col-md-7');
      el2.classList.add('col-md-5');
      el3.classList.add('row');
    }
  }
}
