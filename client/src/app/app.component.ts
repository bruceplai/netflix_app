import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { ITitle } from './title';
import { TitleService } from './title.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  public title = 'netflix';
  public displayedColumns: string[] = ['title', 'type', 'director', 'cast'];
  public dataSource = new MatTableDataSource<ITitle>();

  constructor(private titleService: TitleService) {}

  private getData() {
    this.titleService.getTitles().subscribe(response => {
      this.dataSource.data = response;
    });
  }

  ngOnInit() {
    this.getData();
  }
}
