import { Component, OnInit } from '@angular/core';
import restaurants from '../../../assets/data/restaurants.json'

@Component({
  selector: 'app-all-restaurants',
  templateUrl: './all-restaurants.component.html',
  styleUrls: ['./all-restaurants.component.scss']
})
export class AllRestaurantsComponent implements OnInit {

  restaurants = restaurants;
  constructor() { 
    this.restaurants = restaurants;
  }

  ngOnInit(): void {
  }

  displayList(list){
    
  }

}
