import { Component, OnInit } from '@angular/core';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { RestaurantsService } from '../../service/restaurants.service';

@Component({
  selector: 'app-all-restaurants',
  templateUrl: './all-restaurants.component.html',
  styleUrls: ['./all-restaurants.component.scss'],
})
export class AllRestaurantsComponent implements OnInit {
  restaurants: any[];
  faSearch = faSearch;

  constructor(private restaurantsService: RestaurantsService) {
    this.restaurants = this.restaurantsService.listRestaurants();
  }

  ngOnInit(): void {}

  displayList(list) {}
}
