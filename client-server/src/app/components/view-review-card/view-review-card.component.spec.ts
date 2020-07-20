import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewReviewCardComponent } from './view-review-card.component';

describe('ViewReviewCardComponent', () => {
  let component: ViewReviewCardComponent;
  let fixture: ComponentFixture<ViewReviewCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewReviewCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewReviewCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
