import { Component, OnInit } from '@angular/core';
import { faCreditCard, faUser, faCalendarAlt, faKey } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.scss']
})
export class PaymentComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  faCreditCard = faCreditCard;
  faUser = faUser;
  faCalendarAlt = faCalendarAlt;
  faKey = faKey;

}
