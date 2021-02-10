import { Component, OnInit } from '@angular/core';
import { TitleService } from '../title.service';
import { IDataPoint } from '../data-point';
import { Subject } from 'rxjs';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent implements OnInit {
  public titleFilter: string | null;
  public directorFilter: string | null;
  public actorFilter: string | null;
  public yearData: IDataPoint[];
  public genreData: IDataPoint[];
  public countryData: IDataPoint[];

  private titleFilterChanged: Subject<string> = new Subject<string>();
  private directorFilterChanged: Subject<string> = new Subject<string>();
  private actorFilterChanged: Subject<string> = new Subject<string>();

  constructor(private titleService: TitleService) {}

  private getYears(): void {
    this.titleService
      .getYears(this.titleFilter, this.directorFilter, this.actorFilter)
      .subscribe((response) => {
        this.yearData = response;
      });
  }

  private getGenres(): void {
    this.titleService
      .getGenres(this.titleFilter, this.directorFilter, this.actorFilter)
      .subscribe((response) => {
        this.genreData = response;
      });
  }

  private getCountries(): void {
    this.titleService
      .getCountries(this.titleFilter, this.directorFilter, this.actorFilter)
      .subscribe((response) => {
        this.countryData = response;
      });
  }

  private getAllData() {
    this.getYears();
    this.getGenres();
    this.getCountries();
  }

  public onTitleFilterChanged(filterText: string): void {
    if (this.titleFilterChanged.observers.length === 0) {
      this.titleFilterChanged
        .pipe(debounceTime(500), distinctUntilChanged())
        .subscribe((response) => {
          this.getAllData();
        });
    }
    this.titleFilterChanged.next(filterText);
  }

  public onDirectorFilterChanged(filterText: string): void {
    if (this.directorFilterChanged.observers.length === 0) {
      this.directorFilterChanged
        .pipe(debounceTime(500), distinctUntilChanged())
        .subscribe((response) => {
          this.getAllData();
        });
    }
    this.directorFilterChanged.next(filterText);
  }

  public onActorFilterChanged(filterText: string): void {
    if (this.actorFilterChanged.observers.length === 0) {
      this.actorFilterChanged
        .pipe(debounceTime(500), distinctUntilChanged())
        .subscribe((response) => {
          this.getAllData();
        });
    }
    this.actorFilterChanged.next(filterText);
  }

  ngOnInit(): void {
    this.getAllData();
  }
}
