import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private static readonly AUTH_ENDPOINT = `${environment.endpoint_url}/auth/`;

  constructor(private http: HttpClient) {}

  addNewUser(userData): void {
    const endpoint = `${LoginService.AUTH_ENDPOINT}`;
    this.http.post<any>(endpoint, userData).subscribe((data) => {
      console.log(data);
    });
  }
}
