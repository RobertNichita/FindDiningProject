import { Component, OnInit } from '@angular/core';
import orders from '../../../assets/data/orders.json';

@Component({
  selector: 'app-restuarant-dashboard',
  templateUrl: './restuarant-dashboard.component.html',
  styleUrls: ['./restuarant-dashboard.component.scss'],
})
export class RestuarantDashboardComponent implements OnInit {
  orders = orders;
  constructor() {}

  ngOnInit(): void {}
}
