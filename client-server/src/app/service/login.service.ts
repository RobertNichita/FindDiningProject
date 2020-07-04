import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private static readonly AUTH_ENDPOINT = `${environment.endpoint_url}/auth`;

  constructor(private http: HttpClient) {}

  /*
  @Input: JSON user object from auth
  @Output: None
  Add logged in user to the database. Updates the time if user already exists.
  */
  addNewUser(userData): void {
    const endpoint = `${LoginService.AUTH_ENDPOINT}/signup/`;
    userData.role = 'BU'; // will change once get user endpoint is available
    this.http.post<any>(endpoint, userData).subscribe((data) => {});
  }

  /*
  @Input: JSON object - source section of user profile
  @Output: None

  Assign the 'Restauraut Owner' role to the user using their email.
  */
  updateUser(userData): void {
    const endpoint = `${LoginService.AUTH_ENDPOINT}/reassign/`;
    const userObject = {
      email: userData._value.email,
      role: 'RO',
    };
    this.http.post<any>(endpoint, userObject).subscribe((data) => {});
  }
}
