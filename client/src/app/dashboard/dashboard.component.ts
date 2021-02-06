import { Component, OnInit } from '@angular/core';
import { TitleService } from '../title.service';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent implements OnInit {
  public titleFilter: string | null;
  public directorFilter: string | null;

  constructor(private titleService: TitleService) { }

  private getYears(): void {
    this.titleService
      .getYears(this.titleFilter, this.directorFilter)
      .subscribe((response) => {
        console.log(response);
      });
  }

  private getRatings(): void {
    this.titleService
      .getRatings(this.titleFilter, this.directorFilter)
      .subscribe((response) => {
        console.log(response);
      });
  }

  private getGenres(): void {
    this.titleService
      .getGenres(this.titleFilter, this.directorFilter)
      .subscribe((response) => {
        console.log(response);
      });
  }

  private getCountries(): void {
    this.titleService
      .getCountries(this.titleFilter, this.directorFilter)
      .subscribe((response) => {
        console.log(response);
      });
  }

  private getAllData() {
    this.getYears();
    this.getRatings();
    this.getGenres();
    this.getCountries();
  }

  public doFilter(): void {
    this.getAllData();
  }

  ngOnInit(): void {
    this.getAllData();
  }
}
