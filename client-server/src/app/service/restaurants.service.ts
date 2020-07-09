import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class RestaurantsService {
  private static readonly RO_ENDPOINT = `${environment.endpoint_url}/RO`;

  constructor(private http: HttpClient) {}

  /*
  @Input: None
  @Output: List of all restaurants

  Return list of all restaurants in the database
  */
  listRestaurants(): any[] {
    const endpoint = `${RestaurantsService.RO_ENDPOINT}/getAll/`;
    let restaurants: any[];
    this.http.get<any[]>(endpoint).subscribe((data) => {
      restaurants = data;
    });

    return restaurants;
  }
}
