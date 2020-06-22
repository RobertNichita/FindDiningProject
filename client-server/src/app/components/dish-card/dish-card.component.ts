import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-dish-card',
  exportAs: 'app-dish-card',
  templateUrl: './dish-card.component.html',
  styleUrls: ['./dish-card.component.scss'],
})
export class DishCardComponent implements OnInit {
  totalStars: number = 5;

  @Input() dish: any;

  constructor() {}

  ngOnInit(): void {}
}
