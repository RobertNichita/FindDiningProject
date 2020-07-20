import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-view-review-card',
  templateUrl: './view-review-card.component.html',
  styleUrls: ['./view-review-card.component.scss'],
})
export class ViewReviewCardComponent implements OnInit {
  @Input() review: any;

  totalStars = 5;

  constructor() {}

  ngOnInit(): void {}
}
