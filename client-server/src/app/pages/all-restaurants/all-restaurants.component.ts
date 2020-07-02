import { Component, OnInit } from '@angular/core';
import restaurants from '../../../assets/data/restaurants.json';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-all-restaurants',
  templateUrl: './all-restaurants.component.html',
  styleUrls: ['./all-restaurants.component.scss']
})
export class AllRestaurantsComponent implements OnInit {

  restaurants = restaurants;
  faSearch = faSearch;
  constructor() { 
    this.restaurants = restaurants;
  }

  ngOnInit(): void {
  }

  displayList(list){
    
  }

}
