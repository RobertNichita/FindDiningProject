import { Component, OnInit, Input } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import reviews from '../../../assets/data/reviews.json';

@Component({
  selector: 'app-dish-card',
  exportAs: 'app-dish-card',
  templateUrl: './dish-card.component.html',
  styleUrls: ['./dish-card.component.scss'],
})
export class DishCardComponent implements OnInit {
  // evenutally call reviews of the dishes
  reviews: any[];
  value: number = 0;
  totalStars: number = 5;

  @Input() dish: any;

  constructor(private modalService: NgbModal) {
    this.reviews = reviews;
  }

  ngOnInit(): void {}

  openDish(content) {
    this.modalService.open(content, { size: 'xl' });
  }
}
