import { Component } from '@angular/core';
import {
  faFacebookSquare,
  faTwitter,
  faInstagram,
} from '@fortawesome/free-brands-svg-icons';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  faFacebook = faFacebookSquare;
  faTwitter = faTwitter;
  faInstagram = faInstagram;
}
